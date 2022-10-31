from .application import Application
from .queries import get_pending_applications, update_application_status
from .nginx_static_files_with_proxy_configuration import NginxStaticFilesWithProxyConfiguration
import logging

class NginxConf:
    def create_nginx_conf(self):
        try:
            pending_applications = get_pending_applications()
            for application in pending_applications:
                application = Application(application)
                if application.framework == 'react':
                    NginxStaticFilesWithProxyConfiguration(application)\
                    .create_nginx_static_files_with_proxy_configuration()
                    update_application_status(application.application_id, 'completed')
            return 0
        except Exception as e:
            logging.getLogger().setLevel(logging.ERROR)
            logging.getLogger().error(e)
            raise e
