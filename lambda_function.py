from databricks import sql
import datetime
import json
import os

def datetime_parser(data_point):
    if isinstance(data_point, datetime.datetime):
        return (str(data_point.isoformat()))
    else:
        return str(data_point)


def lambda_handler(event, context):

    with sql.connect(server_hostname = os.environ.get('SERVER_HOSTNAME'),
                    http_path       = os.environ.get('HTTP_PATH'),
                    access_token    = os.environ.get('ACCESS_TOKEN')
                    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM  hive_metastore.nr_google_drive.track_combined LIMIT 2")
            result = cursor.fetchall()
            result_dict = [x.asDict() for x in result]

    json_data = json.dumps(result_dict ,default=datetime_parser, sort_keys=True)
    return json_data

