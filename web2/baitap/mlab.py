import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds147033.mlab.com:47033/c4e22-regis

host = "ds147033.mlab.com"
port = 47033
db_name = "c4e22-regis"
user_name = "admin1"
password = "admin2"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())