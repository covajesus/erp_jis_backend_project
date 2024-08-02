from app.backend.db.models import EmployeeModel, EmployeeLaborDatumModel, EmployeeViewModel, ClockUserModel, BranchOfficeModel, OldEmployeeModel, OldEmployeeLaborDatumModel, SupervisorModel, EmployeeLaborDatumModel
from datetime import datetime
from sqlalchemy import func
from app.backend.classes.helper_class import HelperClass
from app.backend.classes.dropbox_class import DropboxClass
import json

class EmployeeClass:
    def __init__(self, db):
        self.db = db
    
    def store(self, employee_inputs):
        numeric_rut = HelperClass().numeric_rut(str(employee_inputs['rut']))

        employee = EmployeeModel()
        employee.rut = numeric_rut
        employee.visual_rut = employee_inputs['rut']
        employee.names = employee_inputs['names']
        employee.father_lastname = employee_inputs['father_lastname']
        employee.mother_lastname = employee_inputs['mother_lastname']
        employee.gender_id = employee_inputs['gender_id']
        employee.nationality_id = employee_inputs['nationality_id']
        employee.personal_email = employee_inputs['personal_email']
        employee.cellphone = employee_inputs['cellphone']
        employee.born_date = employee_inputs['born_date']
        employee.added_date = datetime.now()

        self.db.add(employee)

        try:
            self.db.commit()

            return 1
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def delete(self, rut):
        try:
            data = self.db.query(EmployeeModel).filter(EmployeeModel.rut == rut).first()
            if data:
                self.db.delete(data)
                self.db.commit()
                return 1
            else:
                return "No data found"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def update(self, id, employee_inputs):
        employee =  self.db.query(EmployeeModel).filter(EmployeeModel.rut == id).first()

        if 'rut' in employee_inputs and employee_inputs['rut'] is not None:
            numeric_rut = HelperClass().numeric_rut(str(employee_inputs['rut']))
            employee.rut = numeric_rut
            employee.visual_rut = employee_inputs['rut']
        
        if 'names' in employee_inputs and employee_inputs['names'] is not None:
            employee.names = employee_inputs['names']
        
        if 'father_lastname' in employee_inputs and employee_inputs['father_lastname'] is not None:
            employee.father_lastname = employee_inputs['father_lastname']
        
        if 'mother_lastname' in employee_inputs and employee_inputs['mother_lastname'] is not None:
            employee.mother_lastname = employee_inputs['mother_lastname']

        if 'gender_id' in employee_inputs and employee_inputs['gender_id'] is not None:
            employee.gender_id = employee_inputs['gender_id']

        if 'nationality_id' in employee_inputs and employee_inputs['nationality_id'] is not None:
            employee.nationality_id = employee_inputs['nationality_id']
        
        if 'personal_email' in employee_inputs and employee_inputs['personal_email'] is not None:
            employee.personal_email = employee_inputs['personal_email']
        
        if 'cellphone' in employee_inputs and employee_inputs['cellphone'] is not None:
            employee.cellphone = employee_inputs['cellphone']
        
        if 'born_date' in employee_inputs and employee_inputs['born_date'] is not None:
            employee.born_date = employee_inputs['born_date']

        if 'signature' in employee_inputs and employee_inputs['signature'] is not None:
            employee.signature = employee_inputs['signature']

        if 'signature_type_id' in employee_inputs and employee_inputs['signature_type_id'] is not None:
            employee.signature_type_id = employee_inputs['signature_type_id']

        if 'picture' in employee_inputs and employee_inputs['picture'] is not None:
            employee.picture = employee_inputs['picture']

        employee.update_date = datetime.now()

        self.db.add(employee)

        try:
            self.db.commit()

            return 1
        except Exception as e:
            return 0
    
    def get_birthdays(self):
        today = datetime.today()

        employees = self.db.query(
            EmployeeModel.rut,
            EmployeeModel.names,
            EmployeeModel.father_lastname,
            BranchOfficeModel.branch_office,
            func.DATE_FORMAT(EmployeeModel.born_date, "%d").label('day'),
            func.DATE_FORMAT(EmployeeModel.born_date, "%M").label('month')
        ) \
        .join(EmployeeLaborDatumModel, EmployeeLaborDatumModel.rut == EmployeeModel.rut) \
        .join(BranchOfficeModel, BranchOfficeModel.id == EmployeeLaborDatumModel.branch_office_id) \
        .filter(func.DAY(EmployeeModel.born_date) >= today.day, func.MONTH(EmployeeModel.born_date) == today.month) \
        .order_by(func.DAY(EmployeeModel.born_date)) \
        .limit(4) \
        .all()

        # Serializar la lista de objetos employees a formato JSON
        serialized_employees = json.dumps([employee._asdict() for employee in employees])

        return serialized_employees
    
    def gender_totals(self):
        men_total = self.db.query(EmployeeModel).filter(EmployeeModel.gender_id == 1).count()
        women_total = self.db.query(EmployeeModel).filter(EmployeeModel.gender_id == 2).count()

        totals = [
            {'gender': 'Men', 'total': men_total},
            {'gender': 'Women', 'total': women_total}
        ]
    
        return totals
    

    def validate_cellphone(self, cellphone):
        existence = self.db.query(EmployeeModel).filter(EmployeeModel.cellphone == cellphone).count()
        employeeExistence = self.db.query(EmployeeModel).filter(EmployeeModel.cellphone == cellphone).first()

        if existence == 1:
            return 1, employeeExistence
        else:
            return 0