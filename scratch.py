# insert boiler plate

from elasticsearch import Elasticsearch
from config import user, password

cli = Elasticsearch(
        ["https://localhost:9200"],
        verify_certs=False, #  TODO check cert!!!
        http_auth=(user,password)
)

print(cli.search("config"))
