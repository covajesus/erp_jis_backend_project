from app.backend.db.models import PayrollFamilyAsignationIndicatorModel, PayrollIndicatorModel, PayrollManualInputModel
from app.backend.classes.payroll_item_value_class import PayrollItemValueClass
from app.backend.classes.helper_class import HelperClass

class PayrollFamilyBurdenClass:
    def __init__(self, db):
        self.db = db

    def get(self, section_id, period):
        data = self.db.query(PayrollFamilyAsignationIndicatorModel.amount). \
                        outerjoin(PayrollIndicatorModel, PayrollIndicatorModel.indicator_id == PayrollFamilyAsignationIndicatorModel.id). \
                        filter(PayrollIndicatorModel.period == period, PayrollIndicatorModel.indicator_type_id == 9, PayrollFamilyAsignationIndicatorModel.section_id == section_id).first()

        return data.amount
    
    def multiple_store(self, form_data, family_burdens):
        helper = HelperClass()
        numeric_rut = helper.numeric_rut(str(family_burdens['rut']))

        payroll_item_value_data = {
            'item_id': 33,
            'rut': numeric_rut,
            'period': form_data.period,
            'amount': family_burdens['section']
        }
        PayrollItemValueClass(self.db).store(payroll_item_value_data)

        payroll_item_value_data = {
            'item_id': 18,
            'rut': numeric_rut,
            'period': form_data.period,
            'amount': family_burdens['family_amount']
        }
        PayrollItemValueClass(self.db).store(payroll_item_value_data)

        payroll_item_value_data = {
            'item_id': 90,
            'rut': numeric_rut,
            'period': form_data.period,
            'amount': family_burdens['retroactive_amount']
        }
        PayrollItemValueClass(self.db).store(payroll_item_value_data)

        return 1