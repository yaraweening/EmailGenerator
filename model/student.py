from mongoengine import Document, StringField, DecimalField, IntField, EmailField

class Student(Document):
    firstname = StringField(required=True, max_length=256)
    lastname = StringField(required=True, max_length=256)
    phone = StringField(required=True, max_length=256)
    email = EmailField(required=True, max_length=256)
    class_id = IntField(required=True, min_value=0)
    meta = {'collection': 'Students'}
    meta = {'db_alias': 'StudentsMS'}