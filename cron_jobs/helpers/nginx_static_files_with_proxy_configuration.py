# create nginx static files wirh external proxy configuration    

import os
import logging

from .queries import update_application_status


class NginxStaticFilesWithProxyConfiguration:
    def __init__(self, application):
        self.application = application
        self.application_name = application.application_name
        self.framework = application.framework
        self.id = application.id
        self.application_port = application.application_port
        self.domain_name = application.domain_name
        self.application_path = application.application_path
        self.proxy_host_name_and_or_port = application.proxy_host_name_and_or_port
    
    def create_nginx_static_files_with_proxy_configuration(self):
        
        try:
            # create
            # /etc/nginx/sites-available/application_name.conf
            # /etc/nginx/sites-enabled/application_name.conf

            template = f'''
server {{
    listen 80;
    server_name {self.domain_name};
    location / {{
        proxy_pass {self.proxy_host_name_and_or_port}$uri;
    }}
}}
            '''
            
            # create /etc/nginx/sites-available/application_name.conf
            with open(f'/etc/nginx/sites-available/{self.application_name}.conf', 'w') as f:
                f.write(template)

            # create symlink if not exists
            if not os.path.exists(f'/etc/nginx/sites-enabled/{self.application_name}.conf'):
                os.symlink(f'/etc/nginx/sites-available/{self.application_name}.conf', f'/etc/nginx/sites-enabled/{self.application_name}.conf')

            # reload nginx if valid
            # os.system('nginx -t')
            os.system('systemctl restart nginx')
            return
            

            

        except Exception as e:
            logging.getLogger().setLevel(logging.ERROR)
            logging.getLogger().error(e)
            raise e
        
    