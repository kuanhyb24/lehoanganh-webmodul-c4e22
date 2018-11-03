from mongoengine import StringField, IntField, Document

class River(Document):
    name = StringField
    continent = StringField
    length = IntField