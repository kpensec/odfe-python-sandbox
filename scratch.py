# insert boiler plate

from elasticsearch import Elasticsearch
from .secret import user, password

cli = Elasticsearch(
        ["localhost:9200"],
        verify_certs=False # 
        http_auth=(user,password)
)

cli.search("config")
