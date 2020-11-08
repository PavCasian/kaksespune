from mongoengine import Document, StringField, ListField, DateTimeField
from datetime import datetime

# Translation object will be included
# class Translation(EmbeddedDocument):
#     name = StringField()
#     russian = StringField()
#     romanian = StringField()
#     translations = ListField(EmbeddedDocumentField(Translation))


class Word(Document):
    name = StringField()
    other_versions = ListField()  # of the name
    date_added = DateTimeField(default=datetime.utcnow)
    date_updated = DateTimeField(default=None)
    # each list can contain multiple translating words
    russian_trans = ListField(StringField(max_length=50))
    romanian_trans = ListField(StringField(max_length=50))



