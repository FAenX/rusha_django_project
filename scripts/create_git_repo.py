#

import json
import subprocess

import yaml
import logging
from django.db import connection

from rest_framework import serializers

class JoinSerializer(serializers.Serializer):
    application_id = serializers.CharField(max_length=100)
    application_name = serializers.CharField(max_length=100)
    framework = serializers.CharField(max_length=100)


# react app post receive
def create_react_git_bare_repo():
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
    print(to_dict)
    for item in to_dict:
        application_name = item['application_name']
        framework = item['framework']
        application_id = item['application_id']
        main(application_name)
    


def main(application_name):
    with open(f'rusha_config.yml', 'r') as f:
        yaml_content = yaml.load(f, Loader=yaml.FullLoader)
        git_dir_path = f"{yaml_content['git_dir']}/{application_name}.git"
        project_path = f"{yaml_content['applications_dir']}/{application_name}"
        tempdir = f"{yaml_content['tmp_dir']}/{application_name}"
        subprocess.check_call(f'git init --bare --shared=all {git_dir_path}', shell=True)

    template = f'''
# create a post-receive file
#!/bin/bash
# generated automatically

# Deploy the content to the temporary directory
mkdir -p {tempdir}
mkdir -p {project_path}
git --work-tree={tempdir} --git-dir={git_dir_path} checkout -f || exit;

rm -rf {project_path}/*
cp -r {tempdir}/* {project_path} || exit;
rm -rf {tempdir} || exit;
cd {project_path} || exit;

# create a Dockerfile 
# add multiline string to a file
cat <<EOF > {project_path}/Dockerfile
# Name the node stage "builder"
FROM node:14 AS builder
# Set working directory
WORKDIR /app
# Copy all files from current directory to working dir in image
COPY . .
# install node modules and build assets
RUN npm install && npm run build

# nginx state for serving content
FROM nginx:alpine
# Set working directory to nginx asset directory
WORKDIR /usr/share/nginx/html
# Remove default nginx static assets
RUN rm -rf ./*
# Copy static assets from builder stage
COPY --from=builder /app/build .
# Containers run nginx with global directives and daemon off
ENTRYPOINT ["nginx", "-g", "daemon off;"]
EOF

# docker build -t react-nginx .;
# kubectl apply -f {project_path}/k8s.yaml;


'''  

    with open(f'{git_dir_path}/hooks/post-receive', 'w') as file:
        file.write(template)

    subprocess.check_call(f'chmod +x {git_dir_path}/hooks/post-receive', shell=True)

    return git_dir_path
    