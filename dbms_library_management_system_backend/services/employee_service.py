from utils.utils import db
from models.employee_model import EmployeeModel
from flask import session
def create_employee(data):
    new_employee = EmployeeModel(
        employee_id=data.get('employee_id'),
        employee_name=data.get('employee_name'),
        employee_email=data.get('employee_email'),
        employee_phone=data.get('employee_phone'),
        gender=data.get('gender'),
        date_of_birth=data.get('date_of_birth'),
        date_of_joining=data.get('date_of_joining'),
        password=data.get('password'),
        country=data.get('country'),
        state=data.get('state'),
        city=data.get('city'),
        street=data.get('street'),
    )
    db.session.add(new_employee)
    db.session.commit()
    return new_employee

def get_employee_by_id(employee_id):
    employee= EmployeeModel.query.get(employee_id)
    return employee.to_dict()

def update_employee(employee_id, employee_name=None, employee_email=None, employee_phone=None, gender=None, date_of_birth=None, date_of_joining=None, password=None, country=None, state=None, city= None, street=None):
    employee = EmployeeModel.query.get(employee_id)
    if employee:
      
        if employee_name:
            employee.employee_name = employee_name
        if employee_email:
            employee.employee_email = employee_email
        if employee_phone:
            employee.employee_phone = employee_phone
        if gender:
            employee.gender = gender
        if date_of_birth:
            employee.date_of_birth = date_of_birth
        if date_of_joining:
            employee.date_of_joining =date_of_joining
        if password:
            employee.password= password
        if country:
            employee.country= country
        if state:
            employee.state= state
        if city:
            employee.city= city
        if street:
            employee.street= street


        db.session.commit() 
        return employee.to_dict() 
    
    return employee  


def delete_employee(employee_id):
    employee = get_employee_by_id(employee_id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return True
    return False

def signup_employee(data):
    
    if EmployeeModel.query.filter_by(employee_email=data['employee_email']).first():
        return None

    new_employee = EmployeeModel(
        employee_id=data['employee_id'],
        employee_name=data['employee_name'],
        employee_email=data['employee_email'],
        employee_phone=data['employee_phone'],
        gender=data['gender'],
        date_of_birth=data['date_of_birth'],
        date_of_joining=data['date_of_joining'],
        country=data['country'],
        state=data['state'],
        city=data['city'],
        street=data['street']
    )
    new_employee.set_password(data['password'])
    db.session.add(new_employee)
    db.session.commit()
    
    return new_employee


def login_employee(employee_email, password):
    employee = EmployeeModel.query.filter_by(employee_email= employee_email).first()
    if employee and employee.check_password(password): 
        session['logged_in']= True
        session['employee_email']= employee.employee_email
        return employee
    return None

def logout_empoyee():
    if 'logged_in' in session:
        session.clear()
        return {"message": "Logout successful"}
    return {"error": "No active session"}