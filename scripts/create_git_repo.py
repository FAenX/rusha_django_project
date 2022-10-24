#

import json
import subprocess

import yaml
import logging
from django.db import connection

from rest_framework import serializers
from .post_receive_templates import replace_template

class JoinSerializer(serializers.Serializer):
    application_id = serializers.CharField(max_length=100)
    application_name = serializers.CharField(max_length=100)
    framework = serializers.CharField(max_length=100)


# react app post receive
def main():
    cur = connection.cursor()
    data = cur.execute(
        f"""SELECT 
                ra.application_name, 
                ra.framework,
                rq.application_id
            FROM rusha_applications_api_nginxconfcreatequeue rq
            JOIN rusha_applications_api_application ra ON rq.application_id = ra.id        
            WHERE rq.status = 'pending'
        """).fetchall()
    
    serializer = JoinSerializer(data=data, many=True)
    serializer.is_valid(raise_exception=False)
    to_json = json.dumps(serializer.data, indent=4)
    to_dict = json.loads(to_json)

    # if to dict is empty, return
    if not to_dict:
        logging.info('No pending applications')
        return


    for item in to_dict:
        application_name = item['application_name']
        framework = item['framework']
        application_id = item['application_id']
        create_git_repo(application_name, application_id)
    


def create_git_repo(application_name, application_id):
    with open(f'/home/manu/private/rusha_django/rusha_config.yml', 'r') as f:
        yaml_content = yaml.load(f, Loader=yaml.FullLoader)
        git_dir_path = f"{yaml_content['git_dir']}/{application_name}.git"
        project_path = f"{yaml_content['applications_dir']}/{application_name}"
        tempdir = f"{yaml_content['tmp_dir']}/{application_name}"
        subprocess.check_call(f'git init --bare --shared=all {git_dir_path}', shell=True)

    
    with open(f'{git_dir_path}/hooks/post-receive', 'w') as file:
        template = replace_template(tempdir, project_path, git_dir_path)
        file.write(template)

    # update status to done
    cur = connection.cursor()
    cur.execute(
        f"""
        UPDATE 
        rusha_applications_api_nginxconfcreatequeue 
        SET status = 'done' 
        WHERE application_id ='{application_id}'
        """)
    cur.close()

    # update local git repo column on rusha_applications_api_application
    cur = connection.cursor()
    cur.execute(
        f"""
        UPDATE
        rusha_applications_api_application
        SET local_git_repo = '{git_dir_path}'
        WHERE id = '{application_id}'
        """)
    cur.close()

    subprocess.check_call(f'chmod +x {git_dir_path}/hooks/post-receive', shell=True)

    return git_dir_path
    