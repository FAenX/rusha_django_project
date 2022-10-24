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
        from scripts.create_git_repo import  main
        
        main()
    
    except Exception as e:
        raise e
        
    logging.info('-----------------')

if __name__ == '__main__':
    main()
