from mongoengine import Document, StringField, ListField

#ke thua 
class Poll(Document):
    question = StringField()
    options = ListField(StringField())
    code = StringField()    