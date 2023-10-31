from app.backend.db.models import OldEmployeeLaborDatumModel
from datetime import datetime
from app.backend.classes.helper_class import HelperClass

class OldEmployeeLaborDatumClass:
    def __init__(self, db):
        self.db = db

    def get(self, field, value):
        try:
            data = self.db.query(OldEmployeeLaborDatumModel).filter(getattr(OldEmployeeLaborDatumModel, field) == value).first()
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def store(self, old_employee_labor_datum_inputs):
        numeric_rut = HelperClass().numeric_rut(str(old_employee_labor_datum_inputs['rut']))

        employee_labor_datum = OldEmployeeLaborDatumModel()
        employee_labor_datum.rut = numeric_rut
        employee_labor_datum.contract_type_id = old_employee_labor_datum_inputs['contract_type_id']
        employee_labor_datum.branch_office_id = old_employee_labor_datum_inputs['branch_office_id']
        employee_labor_datum.address = old_employee_labor_datum_inputs['address']
        employee_labor_datum.region_id = old_employee_labor_datum_inputs['region_id']
        employee_labor_datum.commune_id = old_employee_labor_datum_inputs['commune_id']
        employee_labor_datum.civil_state_id = old_employee_labor_datum_inputs['civil_state_id']
        employee_labor_datum.health_id = old_employee_labor_datum_inputs['health_id']
        employee_labor_datum.pention_id = old_employee_labor_datum_inputs['pention_id']
        employee_labor_datum.job_position_id = old_employee_labor_datum_inputs['job_position_id']
        employee_labor_datum.employee_type_id = old_employee_labor_datum_inputs['employee_type_id']
        employee_labor_datum.regime_id = old_employee_labor_datum_inputs['regime_id']
        employee_labor_datum.status_id = old_employee_labor_datum_inputs['status_id']
        employee_labor_datum.health_payment_id = old_employee_labor_datum_inputs['health_payment_id']
        employee_labor_datum.extra_health_payment_type_id = old_employee_labor_datum_inputs['extra_health_payment_type_id']
        employee_labor_datum.apv_payment_type_id = old_employee_labor_datum_inputs['apv_payment_type_id']
        employee_labor_datum.entrance_pention = old_employee_labor_datum_inputs['entrance_pention']
        employee_labor_datum.entrance_company = old_employee_labor_datum_inputs['entrance_company']
        employee_labor_datum.entrance_health = old_employee_labor_datum_inputs['entrance_health']
        employee_labor_datum.exit_company  = old_employee_labor_datum_inputs['exit_company']
        employee_labor_datum.salary = old_employee_labor_datum_inputs['salary']
        employee_labor_datum.collation = old_employee_labor_datum_inputs['collation']
        employee_labor_datum.locomotion = old_employee_labor_datum_inputs['locomotion']
        employee_labor_datum.extra_health_amount = old_employee_labor_datum_inputs['extra_health_amount']
        employee_labor_datum.apv_amount = old_employee_labor_datum_inputs['apv_amount']
        employee_labor_datum.added_date = datetime.now()
        

        self.db.add(employee_labor_datum)

        try:
            self.db.commit()

            return 1
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"