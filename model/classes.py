from mongoengine import Document, StringField, DecimalField, IntField, EmailField

class Classes(Document):
    class_id = IntField(required=True, min_value=1)
    name = StringField(required=True, max_length=256)
    nrOfStudents = IntField(required=True, min_value=0)
    meta = {'collection': 'Classes'}
    meta = {'db_alias': 'ClassesMS'}