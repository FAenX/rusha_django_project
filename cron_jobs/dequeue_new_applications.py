#!/home/manu/private/rusha_django/.venv/bin/python

import os
import sys
import logging
import django




def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rusha_django.settings')
    django.setup()
    try:
        logging.getLogger().setLevel(logging.INFO)
        logging.info('-----------------')
        logging.info('Starting cron job')
        from helpers.create_git_repo import GitRepo
        from helpers.create_nginx_conf import NginxConf


        
        GitRepo().create_git_repo()
   
        NginxConf().create_nginx_conf()
    

        logging.info('-----------------')
    
    except Exception as e:
        logging.getLogger().setLevel(logging.ERROR)
        logging.error(e)
        raise e
        
    

if __name__ == '__main__':
    main()
