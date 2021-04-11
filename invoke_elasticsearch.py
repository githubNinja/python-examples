import os
import argparse

from elasticsearch import Elasticsearch as ElasticsearchClient, RequestsHttpConnection, helpers
from requests_aws4auth import AWS4Auth


def parse_arguments():
    parser = argparse.ArgumentParser(description='Asset location create incident ticket')
    parser.add_argument('--aws_access_key_id', required=True, help='access_key_id')
    parser.add_argument('--aws_secret_access_key', required=True, help='access_key')
    parser.add_argument('--aws_session', required=True, help='session')
    args = parser.parse_args()
    return args


def invoke_api_request(aws_key_id, aws_access_key, aws_session):
     es_host = 'search-config-inventory-audit-mf3aa5q5lrjyesial5kqdqmdr4.us-east-1.es.amazonaws.com'
     aws_auth = AWS4Auth(aws_key_id,
                    aws_access_key,
                    'us-east-1',
                    'es',
                    session_token=aws_session)
     es = ElasticsearchClient(hosts=[{'host': es_host, 'port': 443}],
                              http_auth=aws_auth,
                              use_ssl=True,
                              verify_certs=True,
                              connection_class=RequestsHttpConnection)
     search_query = {

     }
     es.search(index="onecloud-app-logging-om-omjdsc*")


if __name__ == '__main__':
    arguments = parse_arguments()
    access_key_id = arguments.aws_access_key_id
    access_key = arguments.aws_secret_access_key
    session = arguments.aws_session
    invoke_api_request(access_key_id, access_key, session)
