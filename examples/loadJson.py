import json
with open('./docDB.json') as f:
  data = json.load(f)


  mongodb_client = MongoClient(
            host=host,
            port=port,
            ssl=tls,
            ssl_ca_certs=tls_ca_file,
            connect=True,
            connectTimeoutMS=DocumentDbIndexTool.CONNECT_TIMEOUT,
            serverSelectionTimeoutMS=DocumentDbIndexTool.CONNECT_TIMEOUT)