from django.db import connection
from rushiwa_applications_api import serializers as rusha_applications_api_serializers
from rushiwa_applications_api.models import Application
from django.forms.models import model_to_dict

import json
import logging




def get_pending_applications():
    try:
        cur = connection.cursor()
        data = cur.execute(
            f"""SELECT *
                FROM rusha_applications_api_nginxconfcreatequeue rq
                JOIN rusha_applications_api_application ra ON rq.application_id = ra.id        
                WHERE rq.status = 'pending'
            """)
        data = cur.fetchall()
        headers = [i[0] for i in cur.description]
        data = [dict(zip(headers, row)) for row in data]
        cur.close()
        
        
        return  data
    except Exception as e:
        logging.error(f'get_pending_applications error: {e}')
        raise e

def update_application_status(application_id, status):
    try:
        cur = connection.cursor()
        cur.execute(
            f"""UPDATE rusha_applications_api_nginxconfcreatequeue
                SET status = '{status}'
                WHERE application_id = '{application_id}'
            """)

        cur.close()
        return 0
    except Exception as e:
        logging.error(f'update_application_status error: {e}')
        raise e

def update_git_dir(application_id, git_dir_path):
    try:
        cur = connection.cursor()
        cur.execute(
            f"""UPDATE rusha_applications_api_application
                SET local_git_repo = '{git_dir_path}'
                WHERE id = '{application_id}'
            """)

        cur.close()
        return 0
    except Exception as e:
        logging.error(f'update_git_dir error: {e}')
        raise e