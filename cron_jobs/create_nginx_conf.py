from application import Application
from cron_jobs.queries import get_pending_applications, update_application_status
from nginx_static_files_with_proxy_configuration import NginxStaticFilesWithProxyConfiguration


class NginxConf:
    def create_nginx_conf(self):
        pending_applications = get_pending_applications()
        for application in pending_applications:
            application = Application(application)
            application()
            if application.framework == 'react':
                NginxStaticFilesWithProxyConfiguration(application).create_nginx_static_files_with_proxy_configuration()
            update_application_status(application.id)
