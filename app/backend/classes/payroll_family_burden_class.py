from app.backend.db.models import PayrollFamilyAsignationIndicatorModel, PayrollIndicatorModel

class PayrollFamilyBurdenClass:
    def __init__(self, db):
        self.db = db

    def get(self, section_id, period):
        data = self.db.query(PayrollFamilyAsignationIndicatorModel.amount). \
                        outerjoin(PayrollIndicatorModel, PayrollIndicatorModel.indicator_id == PayrollFamilyAsignationIndicatorModel.id). \
                        filter(PayrollIndicatorModel.period == period, PayrollIndicatorModel.indicator_type_id == 9, PayrollFamilyAsignationIndicatorModel.section_id == section_id).first()

        return data.amount