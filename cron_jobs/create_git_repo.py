#

import json
import subprocess

import yaml
import logging
from queries import get_pending_applications, update_application_status, update_git_dir
from post_receive_templates import replace_template
from application import Application


class GitRepo:
    def create_git_repo(self):
        pending_applications = get_pending_applications()
        for application in pending_applications:
            application = Application(application)
            application()
            with open(f'/home/manu/private/rusha_django/rusha_config.yml', 'r') as f:
                yaml_content = yaml.load(f, Loader=yaml.FullLoader)
                git_dir_path = f"{yaml_content['git_dir']}/{application.application_name}.git"
                project_path = f"{yaml_content['applications_dir']}/{application.application_name}"
                tempdir = f"{yaml_content['tmp_dir']}/{application.application_name}"
                subprocess.check_call(f'git init --bare --shared=all {git_dir_path}', shell=True)

    
            with open(f'{git_dir_path}/hooks/post-receive', 'w') as file:
                template = replace_template(tempdir, project_path, git_dir_path)
                file.write(template)

            print(application)

            update_application_status(application.id)
            update_git_dir(application.id, git_dir_path)

            subprocess.check_call(f'chmod +x {git_dir_path}/hooks/post-receive', shell=True)

            return git_dir_path
            