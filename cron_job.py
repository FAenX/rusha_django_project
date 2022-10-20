#!/home/manu/private/rusha_django/.venv/bin/python

import os
import sys
import logging
import django




def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rusha_django.settings')
    django.setup()
    try:
        
        logging.info('-----------------')
        logging.info('Starting cron job')
        logging.info('try to import rusha_applications_api')
        from scripts.create_git_repo import  create_react_git_bare_repo
        
        create_react_git_bare_repo()
    
    except Exception as e:
        raise e
        
    logging.info('-----------------')

if __name__ == '__main__':
    main()
