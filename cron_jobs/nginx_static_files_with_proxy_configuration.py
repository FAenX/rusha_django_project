# create nginx static files wirh external proxy configuration    
import os


class NginxStaticFilesWithProxyConfiguration:
    def __init__(self, application):
        self.application = application
        self.application_name = application.application_name
        self.framework = application.framework
        self.id = application.id
        self.application_port = application.application_port
        self.application_host = application.application_host
        self.application_domain = application.application_domain
        self.application_path = application.application_path
    
    def create_nginx_static_files_with_proxy_configuration(self):
        
        try:
            # create
            # /etc/nginx/sites-available/application_name.conf
            # /etc/nginx/sites-enabled/application_name.conf

            template = f'''
            server {{
                listen 80;
                server_name {self.application_domain};
                location /api/ {{
                    proxy_pass http://{self.application_host}:{self.application_port};
                    proxy_set_header Host $host;
                    proxy_set_header X-Real-IP $remote_addr;
                    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                }}
                location / {{
                    alias {self.application_path};
                }}
            }}
                        '''

            # create /etc/nginx/sites-available/application_name.conf
            with open(f'/etc/nginx/sites-available/{self.application_name}.conf', 'w') as f:
                f.write(template)

            # create /etc/nginx/sites-enabled/application_name.conf
            os.symlink(f'/etc/nginx/sites-available/{self.application_name}.conf', 
                f'/etc/nginx/sites-enabled/{self.application_name}.conf')

        except Exception as e:
            print(f'exception {e}')
            raise e
        
    