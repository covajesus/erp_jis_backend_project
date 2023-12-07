from app.backend.db.models import EmployeeModel, EmployeeLaborDatumModel, PayrollEmployeeModel
from app.backend.classes.helper_class import HelperClass
from app.backend.classes.payroll_period_class import PayrollPeriodClass
from datetime import datetime

class PayrollClass:
    def __init__(self, db):
        self.db = db

    def close_period(self, open_period_payroll_inputs):
        response = PayrollPeriodClass(self.db).close_period(open_period_payroll_inputs)

        return response
    
    def verifiy_existence(self, period):
        try:
            payroll_employee = self.db.query(PayrollEmployeeModel).filter(PayrollEmployeeModel.period == period).count()
            if payroll_employee:
                return payroll_employee
            else:
                return 0
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def open(self, open_period_payroll_inputs):
        try:
            if self.verifiy_existence(open_period_payroll_inputs['period'] == 0):
                employees = self.db.query(EmployeeModel.rut, EmployeeModel.visual_rut, EmployeeModel.names, 
                                    EmployeeModel.father_lastname, EmployeeModel.mother_lastname, EmployeeLaborDatumModel.contract_type_id,
                                    EmployeeLaborDatumModel.branch_office_id, EmployeeLaborDatumModel.health_id, EmployeeLaborDatumModel.pention_id,
                                    EmployeeLaborDatumModel.employee_type_id, EmployeeLaborDatumModel.regime_id, EmployeeLaborDatumModel.health_payment_id,
                                    EmployeeLaborDatumModel.extra_health_payment_type_id, EmployeeLaborDatumModel.apv_payment_type_id,
                                    EmployeeLaborDatumModel.salary, EmployeeLaborDatumModel.collation, EmployeeLaborDatumModel.locomotion,
                                    EmployeeLaborDatumModel.extra_health_amount, EmployeeLaborDatumModel.apv_amount
                                    ). \
                            outerjoin(EmployeeLaborDatumModel, EmployeeLaborDatumModel.rut == EmployeeModel.rut).all()
                
                for employee in employees:
                    payroll_employee = PayrollEmployeeModel()
                    payroll_employee.rut = employee.rut
                    payroll_employee.visual_rut = employee.visual_rut
                    payroll_employee.period = open_period_payroll_inputs['period']
                    payroll_employee.names = employee.names
                    payroll_employee.father_lastname = employee.father_lastname
                    payroll_employee.mother_lastname = employee.mother_lastname
                    payroll_employee.contract_type_id = employee.contract_type_id
                    payroll_employee.branch_office_id = employee.branch_office_id
                    payroll_employee.health_id = employee.health_id
                    payroll_employee.pention_id = employee.pention_id
                    payroll_employee.employee_type_id = employee.employee_type_id
                    payroll_employee.regime_id = employee.regime_id
                    payroll_employee.health_payment_id = employee.health_payment_id
                    payroll_employee.extra_health_payment_type_id = employee.extra_health_payment_type_id
                    payroll_employee.apv_payment_type_id = employee.apv_payment_type_id
                    payroll_employee.salary = employee.salary
                    payroll_employee.collation = employee.collation
                    payroll_employee.locomotion = employee.locomotion
                    extra_health_amount = HelperClass().return_zero_empty_input(employee.extra_health_amount)
                    payroll_employee.extra_health_amount = extra_health_amount
                    apv_amount = HelperClass().return_zero_empty_input(employee.apv_amount)
                    payroll_employee.apv_amount = apv_amount
                    payroll_employee.added_date = datetime.now()
                    payroll_employee.updated_date = datetime.now()
                    self.db.add(payroll_employee)
                    self.db.commit()

            payroll_opening = PayrollPeriodClass(self.db).open(open_period_payroll_inputs)
            
            return payroll_opening.id
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def clean(self, open_period_payroll_inputs):
        try:
            period = open_period_payroll_inputs['period']

            payroll_employees = self.db.query(PayrollEmployeeModel).filter(PayrollEmployeeModel.period == period).all()
            payroll_employee_quantity = self.db.query(PayrollEmployeeModel).filter(PayrollEmployeeModel.period == period).count()
            if payroll_employee_quantity > 0:
                for payroll_employee in payroll_employees:
                    self.db.delete(payroll_employee)
                    self.db.commit()
            
            return 1
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"