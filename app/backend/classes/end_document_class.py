from app.backend.db.models import DocumentEmployeeModel
from app.backend.classes.hr_setting_class import HrSettingClass
from app.backend.classes.employee_labor_datum_class import EmployeeLaborDatumClass
from app.backend.classes.helper_class import HelperClass
import json


class EndDocumentClass:
    def __init__(self, db):
        self.db = db

    def indemnity_years(self, indemnity_year_inputs):
        try:
            hr_settings = HrSettingClass(self.db).get()
            employee_labor_datum = EmployeeLaborDatumClass(self.db).get("rut", indemnity_year_inputs['rut'])
            employee_labor_datum = json.loads(employee_labor_datum)
            gratification = HelperClass.gratification(employee_labor_datum["EmployeeLaborDatumModel"]["salary"])
            if gratification > hr_settings.top_gratification:
                gratification = hr_settings.top_gratification
            years = HelperClass().get_end_document_total_years(employee_labor_datum["EmployeeLaborDatumModel"]["entrance_company"], indemnity_year_inputs['exit_company'] )
            
            if years > 11:
                years = 11

            result = (int(employee_labor_datum["EmployeeLaborDatumModel"]["salary"]) + 
                    int(employee_labor_datum["EmployeeLaborDatumModel"]["collation"]) + 
                    int(employee_labor_datum["EmployeeLaborDatumModel"]["locomotion"]) + 
                    int(gratification)) * (years) 
            return result
        
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def substitute_compensation(self, substitute_compesation_inputs):
        try:
            hr_settings = HrSettingClass(self.db).get()
            employee_labor_datum = EmployeeLaborDatumClass(self.db).get("rut", substitute_compesation_inputs['rut'])
            employee_labor_datum = json.loads(employee_labor_datum)

            gratification = HelperClass.gratification(employee_labor_datum["EmployeeLaborDatumModel"]["salary"])
            if gratification > hr_settings.top_gratification:
                gratification = hr_settings.top_gratification

            result = (int(employee_labor_datum["EmployeeLaborDatumModel"]["salary"])  
                    + int(employee_labor_datum["EmployeeLaborDatumModel"]["collation"]) 
                    + int(employee_labor_datum["EmployeeLaborDatumModel"]["locomotion"])  
                    + int(gratification))
           
            return result
        
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def fertility_proportional(self, fertility_proportional_inputs):
        employee_labor_datum = EmployeeLaborDatumClass(self.db).get("rut", fertility_proportional_inputs['rut'])
        employee_labor_datum = json.loads(employee_labor_datum)
        
        start_date = fertility_proportional_inputs['exit_company']
        end_date = HelperClass.add_business_days(start_date, fertility_proportional_inputs['balance'], fertility_proportional_inputs['number_holidays'])
        end_date_split = HelperClass().split(str(end_date), " ")
        weekends_between_dates = HelperClass.count_weekends(start_date, end_date_split[0])
        total = int(fertility_proportional_inputs['balance']) + int(weekends_between_dates) + int(fertility_proportional_inputs['number_holidays'])
        vacation_day_value = HelperClass.vacation_day_value(employee_labor_datum["EmployeeLaborDatumModel"]["salary"])

        result = int(vacation_day_value) * int(total)

        if result < 0:
            result = 0

        return result
    
    def total_vacations(self, fertility_proportional_inputs):
        start_date = fertility_proportional_inputs['exit_company']
        end_date = HelperClass.add_business_days(start_date, fertility_proportional_inputs['balance'], fertility_proportional_inputs['number_holidays'])
        end_date_split = HelperClass().split(str(end_date), " ")
        weekends_between_dates = HelperClass.count_weekends(start_date, end_date_split[0])
        total = int(fertility_proportional_inputs['balance']) + int(weekends_between_dates) + int(fertility_proportional_inputs['number_holidays'])
        
        result = int(total)

        if result < 0:
            result = 0

        return result

