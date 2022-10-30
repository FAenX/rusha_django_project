from django.db import connection
from rusha_applications_api import serializers as rusha_applications_api_serializers

import json
import logging




def get_pending_applications():
    cur = connection.cursor()
    data = cur.execute(
        f"""SELECT *
            FROM rusha_applications_api_nginxconfcreatequeue rq
            JOIN rusha_applications_api_application ra ON rq.application_id = ra.id        
            WHERE rq.status = 'pending'
        """).fetchall()
    
    cur.close()
    
    serializer = rusha_applications_api_serializers.ApplicationSerializer(data=data, many=True)
    serializer.is_valid(raise_exception=False)
    to_json = json.dumps(serializer.data, indent=4)
    to_dict = json.loads(to_json)

    print (serializer.is_valid())

   

    # if to dict is empty, return
    if not to_dict:
        logging.info('No pending applications')
        return []
    
    return to_dict

def update_application_status(application_id):
    cur = connection.cursor()
    cur.execute(
        f"""UPDATE rusha_applications_api_nginxconfcreatequeue
            SET status = 'pending'
            WHERE application_id = '{application_id}'
        """)

    cur.close()

def update_git_dir(application_id, git_dir_path):
    cur = connection.cursor()
    cur.execute(
        f"""UPDATE rusha_applications_api_application
            SET local_git_repo = '{git_dir_path}'
            WHERE id = '{application_id}'
        """)

    cur.close()