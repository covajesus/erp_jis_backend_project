from app.backend.db.models import EmployeeLaborDatumModel, HealthModel, PentionModel, EmployeeModel, CommuneModel, RegionModel, CivilStateModel, JobPositionModel, BranchOfficeModel
from datetime import datetime
from app.backend.classes.helper_class import HelperClass
import json

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

            if data:
                employee_labor_data, region, health, commune, civil_state, job_position, branch_office, pention = data

                # Función para formatear la fecha a una cadena
                def format_date(date):
                    return date.strftime('%Y-%m-%d %H:%M:%S') if date else None

                # Serializar los datos de la región
                serialized_region = {
                    "id": region.id,
                    "region": region.region,
                    "region_remuneration_code": region.region_remuneration_code,
                    "added_date": format_date(region.added_date),
                    "updated_date": format_date(region.updated_date)
                }

                # Serializar los datos de la salud
                serialized_health = {
                    "id": health.id,
                    "health_remuneration_code": health.health_remuneration_code,
                    "health": health.health,
                    "rut": health.rut,
                    "previred_code": health.previred_code,
                    "added_date": format_date(health.added_date),
                    "updated_date": format_date(health.updated_date)
                }

                # Serializar los datos de la comuna
                serialized_commune = {
                    "id": commune.id,
                    "region_id": commune.region_id,
                    "commune": commune.commune,
                    "added_date": format_date(commune.added_date),
                    "updated_date": format_date(commune.updated_date)
                }

                # Serializar los datos del estado civil
                serialized_civil_state = {
                    "id": civil_state.id,
                    "civil_state": civil_state.civil_state,
                    "added_date": format_date(civil_state.added_date),
                    "updated_date": format_date(civil_state.updated_date)
                }

                # Serializar los datos del cargo
                serialized_job_position = {
                    "id": job_position.id,
                    "job_position": job_position.job_position,
                    "functions": job_position.functions,
                    "added_date": format_date(job_position.added_date),
                    "updated_date": format_date(job_position.updated_date)
                }

                # Serializar los datos de la sucursal
                serialized_branch_office = {
                    "id": branch_office.id,
                    "branch_office": branch_office.branch_office,
                    "address": branch_office.address,
                    "region_id": branch_office.region_id,
                    "commune_id": branch_office.commune_id,
                    "segment_id": branch_office.segment_id,
                    "zone_id": branch_office.zone_id,
                    "principal_id": branch_office.principal_id,
                    "status_id": branch_office.status_id,
                    "visibility_id": branch_office.visibility_id,
                    "opening_date": branch_office.opening_date,
                    "dte_code": branch_office.dte_code,
                    "added_date": format_date(branch_office.added_date),
                    "updated_date": format_date(branch_office.updated_date)
                }

                # Serializar los datos de la pensión
                serialized_pention = {
                    "id": pention.id,
                    "pention": pention.pention,
                    "pention_remuneration_code": pention.pention_remuneration_code,
                    "rut": pention.rut,
                    "amount": pention.amount,
                    "previred_code": pention.previred_code,
                    "added_date": format_date(pention.added_date),
                    "updated_date": format_date(pention.updated_date)
                }

                # Serializar los datos del empleado
                serialized_employee_labor_data = {
                    "id": employee_labor_data.id,
                    "rut": employee_labor_data.rut,
                    "contract_type_id": employee_labor_data.contract_type_id,
                    "branch_office_id": employee_labor_data.branch_office_id,
                    "address": employee_labor_data.address,
                    "region_id": region.id if region else None,
                    "region_name": region.region if region else None,
                    "commune_id": commune.id if commune else None,
                    "commune_name": commune.commune if commune else None,
                    "civil_state_id": civil_state.id if civil_state else None,
                    "civil_state_name": civil_state.civil_state if civil_state else None,
                    "health_id": health.id if health else None,
                    "health_name": health.health if health else None,
                    "pention_id": pention.id if pention else None,
                    "pention_name": pention.pention if pention else None,
                    "job_position_id": job_position.id if job_position else None,
                    "job_position_name": job_position.job_position if job_position else None,
                    "extra_health_payment_type_id": employee_labor_data.extra_health_payment_type_id,
                    "employee_type_id": employee_labor_data.employee_type_id,
                    "regime_id": employee_labor_data.regime_id,
                    "status_id": employee_labor_data.status_id,
                    "health_payment_id": employee_labor_data.health_payment_id,
                    "entrance_pention": format_date(employee_labor_data.entrance_pention),
                    "entrance_company": format_date(employee_labor_data.entrance_company),
                    "entrance_health": format_date(employee_labor_data.entrance_health),
                    "exit_company": format_date(employee_labor_data.exit_company),
                    "salary": employee_labor_data.salary,
                    "collation": employee_labor_data.collation,
                    "locomotion": employee_labor_data.locomotion,
                    "extra_health_amount": employee_labor_data.extra_health_amount,
                    "apv_payment_type_id": employee_labor_data.apv_payment_type_id,
                    "apv_amount": employee_labor_data.apv_amount,
                    "added_date": format_date(employee_labor_data.added_date),
                    "updated_date": format_date(employee_labor_data.updated_date)
                }

                # Convierte el resultado a una cadena JSON
                serialized_result = json.dumps({
                    "employee_labor_data": serialized_employee_labor_data,
                    "region": serialized_region,
                    "health": serialized_health,
                    "commune": serialized_commune,
                    "civil_state": serialized_civil_state,
                    "job_position": serialized_job_position,
                    "branch_office": serialized_branch_office,
                    "pention": serialized_pention
                })

                return serialized_result
            else:
                return "No se encontraron datos para el campo especificado."

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