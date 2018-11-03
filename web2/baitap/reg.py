from mongoengine import Document, StringField, IntField

class Reg(Document):
    firstname = StringField()
    lastname = StringField()
    email = StringField()
    yob = IntField()
    gender = StringField()
    code = StringField()
