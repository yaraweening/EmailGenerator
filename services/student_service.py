from model.student import Student
from flask import make_response
from utils.DecimalEncoder import Encoder
import json
from utils.JwtToken import validate_token

def add_student_service(student_data):
    try:
        firstname = student_data['firstname']
        lastname = student_data['lastname']
        phone = student_data['phone']
        email = student_data['email']
        class_id = student_data['class_id']

        student = Student(firstname=firstname, lastname=lastname, phone=phone,
                          email=email, class_id=class_id)
        student.save()
        return make_response({'message' : f'succesfully inserted student with id: {student.id}'}, 201)   
    except Exception as e:
        return make_response({'message' : str(e)}, 404)  

def get_student_service():
    students = []
    try:
        for student in Student.objects:
            student_data = {}
            student_data['_id'] = str(student.id)
            student_data['firstname'] = student.firstname
            student_data['lastname'] = student.lastname
            student_data['phone'] = student.phone
            student_data['email'] = student.email
            student_data['class_id'] = student.class_id
            students.append(student_data)

        return {"students": students}
    except Exception as e:
        return make_response({'message' : str(e)}, 404)  

def get_studentbyid_service(student_id):
    students = []
    try:
        student_data = Student.objects[:1](id=student_id)
        for student in student_data:
            student_data = {}
            student_data['_id'] = str(student.id)
            student_data['firstname'] = student.firstname
            student_data['lastname'] = student.lastname
            student_data['phone'] = student.phone
            student_data['email'] = student.email
            student_data['class_id'] = student.class_id
            students.append(student_data)

        return {"student": students}
    except Exception as e:
        return make_response({'message' : str(e)}, 404)  

def update_student_service(student_id, student_data):
    try:
        student = Student.objects(id=student_id) # return a queryset
        if student:     
            student = student.get(id=student_id) # return an object from queryset
            student.firstname = student_data['firstname']
            student.lastname = student_data['lastname']
            student.phone = student_data['phone']
            student.email = student_data['email']
            student.class_id = student_data['class_id']
            student.save()
        
            return make_response({'message' : 'succesfully updated'},201)   
        else:
            return make_response({'message' : "student does not exists"}, 404) 
    except Exception as e:
        return make_response({'message' : str(e)}, 404)  

def delete_student_service(student_id):
    try:
        student = Student.objects(id=student_id) 
        if student:     
            student.delete()
        
            return make_response({'message' : 'succesfully delected'}, 200)   
        else:
            return make_response({'message' : 'student does not exists'}, 404)   
    except Exception as e:
        return make_response({'message' : str(e)}, 404)   
        