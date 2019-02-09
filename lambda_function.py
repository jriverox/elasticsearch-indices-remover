import boto3
from requests_aws4auth import AWS4Auth
from elasticsearch import Elasticsearch, RequestsHttpConnection
import curator
import os

host = os.environ['host'] # For example, search-my-domain.region.es.amazonaws.com
region = os.environ['region'] # For example, us-west-1
prefix = os.environ['indices_prefix']
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

def lambda_handler(event, context):
    #es = Elasticsearch([host])

    es = Elasticsearch(
        hosts = [{'host': host, 'port': 443}],
        http_auth = awsauth,
        use_ssl = True,
        verify_certs = True,
        connection_class = RequestsHttpConnection
    )

    idx_list = curator.IndexList(es)
    print(f"Indices existentes: {idx_list.indices}")
    idx_list.filter_by_regex(kind='prefix', value=prefix)
    print(f'Indices que cumplen el prefijo: {prefix}: {idx_list.indices}')
    idx_list.filter_by_age(source='creation_date', direction='older', unit='minutes', unit_count=30)
    print(f'Indices que finalmente se eliminaran: {idx_list.indices}')

    if idx_list:
        curator.DeleteIndices(idx_list).do_action()
    else:
        print("No hay indices por eliminar")