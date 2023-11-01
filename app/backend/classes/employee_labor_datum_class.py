from app.backend.db.models import EmployeeLaborDatumModel, HealthModel, PentionModel, EmployeeModel, CommuneModel, RegionModel, CivilStateModel, JobPositionModel, BranchOfficeModel
from datetime import datetime
from app.backend.classes.helper_class import HelperClass

class EmployeeLaborDatumClass:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        try:
            data = self.db.query(EmployeeLaborDatumModel).order_by(EmployeeLaborDatumModel.id).all()
            if not data:
                return "No data found"
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def get(self, field, value):
        try:
            data = self.db.query(EmployeeLaborDatumModel, RegionModel, HealthModel, CommuneModel, CivilStateModel, JobPositionModel, BranchOfficeModel, PentionModel). \
                        outerjoin(RegionModel, RegionModel.id == EmployeeLaborDatumModel.region_id). \
                        outerjoin(CommuneModel, CommuneModel.id == EmployeeLaborDatumModel.commune_id). \
                        outerjoin(CivilStateModel, CivilStateModel.id == EmployeeLaborDatumModel.civil_state_id). \
                        outerjoin(JobPositionModel, JobPositionModel.id == EmployeeLaborDatumModel.job_position_id). \
                        outerjoin(BranchOfficeModel, BranchOfficeModel.id == EmployeeLaborDatumModel.branch_office_id). \
                        outerjoin(PentionModel, PentionModel.id == EmployeeLaborDatumModel.pention_id). \
                        outerjoin(HealthModel, HealthModel.id == EmployeeLaborDatumModel.health_id). \
                        filter(getattr(EmployeeLaborDatumModel, field) == value).first()
            
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def store(self, employee_labor_datum_inputs):
        numeric_rut = HelperClass().numeric_rut(str(employee_labor_datum_inputs['rut']))

        employee_labor_datum = EmployeeLaborDatumModel()
        employee_labor_datum.rut = numeric_rut
        employee_labor_datum.visual_rut = employee_labor_datum_inputs['rut']
        employee_labor_datum.added_date = datetime.now()

        self.db.add(employee_labor_datum)

        try:
            self.db.commit()

            return 1
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def delete(self, rut):
        try:
            data = self.db.query(EmployeeLaborDatumModel).filter(EmployeeLaborDatumModel.rut == rut).first()
            if data:
                self.db.delete(data)
                self.db.commit()
                return 1
            else:
                return "No data found"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def update(self, id, employee_labor_datum_inputs):
        employee_labor_datum = self.db.query(EmployeeLaborDatumModel).filter(EmployeeLaborDatumModel.rut == id).first()

        if 'rut' in employee_labor_datum_inputs and employee_labor_datum_inputs['rut'] is not None:
            numeric_rut = HelperClass().numeric_rut(str(employee_labor_datum_inputs['rut']))
            employee_labor_datum.rut =  numeric_rut
            employee_labor_datum.visual_rut = employee_labor_datum_inputs['rut']
        
        if 'contract_type_id' in employee_labor_datum_inputs and employee_labor_datum_inputs['contract_type_id'] is not None:
            employee_labor_datum.contract_type_id = employee_labor_datum_inputs['contract_type_id']
         
        if 'branch_office_id' in employee_labor_datum_inputs and employee_labor_datum_inputs['branch_office_id'] is not None:
             employee_labor_datum.branch_office_id = employee_labor_datum_inputs['branch_office_id']
        
        if 'address' in employee_labor_datum_inputs and employee_labor_datum_inputs['address'] is not None:
                 employee_labor_datum.address = employee_labor_datum_inputs['address']

        if 'region_id' in employee_labor_datum_inputs and employee_labor_datum_inputs['region_id'] is not None:
            employee_labor_datum.region_id = employee_labor_datum_inputs['region_id']
        
        if 'commune_id' in employee_labor_datum_inputs and employee_labor_datum_inputs['commune_id'] is not None:
            employee_labor_datum.commune_id = employee_labor_datum_inputs['commune_id']
        
        if 'civil_state_id' in employee_labor_datum_inputs and employee_labor_datum_inputs['civil_state_id'] is not None:
            employee_labor_datum.civil_state_id = employee_labor_datum_inputs['civil_state_id']
        
        if 'health_id' in employee_labor_datum_inputs and employee_labor_datum_inputs['health_id'] is not None:
            employee_labor_datum.health_id = employee_labor_datum_inputs['health_id']
        
        if 'pention_id' in employee_labor_datum_inputs and employee_labor_datum_inputs['pention_id'] is not None:
            employee_labor_datum.pention_id = employee_labor_datum_inputs['pention_id']

        if 'job_position_id' in employee_labor_datum_inputs and employee_labor_datum_inputs['job_position_id'] is not None:
            employee_labor_datum.job_position_id = employee_labor_datum_inputs['job_position_id']

        if 'employee_type_id' in employee_labor_datum_inputs and employee_labor_datum_inputs['employee_type_id'] is not None:
            employee_labor_datum.employee_type_id = employee_labor_datum_inputs['employee_type_id']

        if 'regime_id' in employee_labor_datum_inputs and employee_labor_datum_inputs['regime_id'] is not None:
            employee_labor_datum.regime_id = employee_labor_datum_inputs['regime_id']

        if 'entrance_pention' in employee_labor_datum_inputs and employee_labor_datum_inputs['entrance_pention'] is not None:
            employee_labor_datum.entrance_pention = employee_labor_datum_inputs['entrance_pention']

        if 'entrance_company' in employee_labor_datum_inputs and employee_labor_datum_inputs['entrance_company'] is not None:
            employee_labor_datum.entrance_company = employee_labor_datum_inputs['entrance_company']

        if 'entrance_health' in employee_labor_datum_inputs and employee_labor_datum_inputs['entrance_health'] is not None:
            employee_labor_datum.entrance_health = employee_labor_datum_inputs['entrance_health']

        if 'salary' in employee_labor_datum_inputs and employee_labor_datum_inputs['salary'] is not None:
            employee_labor_datum.salary = employee_labor_datum_inputs['salary']

        if 'collation' in employee_labor_datum_inputs and employee_labor_datum_inputs['collation'] is not None:
            employee_labor_datum.collation = employee_labor_datum_inputs['collation']

        if 'locomotion' in employee_labor_datum_inputs and employee_labor_datum_inputs['locomotion'] is not None:
            employee_labor_datum.locomotion = employee_labor_datum_inputs['locomotion']

        if 'extra_health_payment_type_id' in employee_labor_datum_inputs and employee_labor_datum_inputs['extra_health_payment_type_id'] is not None:
            employee_labor_datum.extra_health_payment_type_id = employee_labor_datum_inputs['extra_health_payment_type_id']

        if 'extra_health_amount' in employee_labor_datum_inputs and employee_labor_datum_inputs['extra_health_amount'] is not None:
            employee_labor_datum.extra_health_amount = employee_labor_datum_inputs['extra_health_amount']

        if 'apv_payment_type_id' in employee_labor_datum_inputs and employee_labor_datum_inputs['apv_payment_type_id'] is not None:
            employee_labor_datum.apv_payment_type_id = employee_labor_datum_inputs['apv_payment_type_id']

        if 'apv_amount' in employee_labor_datum_inputs and employee_labor_datum_inputs['apv_amount'] is not None:
            employee_labor_datum.apv_amount = employee_labor_datum_inputs['apv_amount']

        employee_labor_datum.updated_date = datetime.now()

        self.db.add(employee_labor_datum)

        try:
            self.db.commit()

            return 1
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"

        return 1
    
    def active_employee_total(self):
        total = self.db.query(EmployeeModel).count()

        return total
    
    def distribution_totals(self):
        full_time_total = self.db.query(EmployeeLaborDatumModel).filter(EmployeeLaborDatumModel.employee_type_id == 1).count()
        part_time_total = self.db.query(EmployeeLaborDatumModel).filter(EmployeeLaborDatumModel.employee_type_id == 2).count()

        totals = [
            {'schedule': 'Full-Time', 'Total': full_time_total},
            {'schedule': 'Part-Time', 'Total': part_time_total}
        ]
    
        return totals