from app.backend.classes.payroll_employee_class import PayrollEmployeeClass
from app.backend.classes.payroll_item_value_class import PayrollItemValueClass
from app.backend.classes.payroll_taxable_income_cap_indicator_class import PayrollTaxableIncomeCapIndicatorClass
from app.backend.classes.payroll_item_class import PayrollItemClass
from app.backend.classes.payroll_uf_indicator_class import PayrollUfIndicatorClass
from app.backend.classes.payroll_minium_taxable_income_indicator_class import PayrollMiniumTaxableIncomeIndicatorClass
from app.backend.classes.payroll_afp_quote_indicator_class import PayrollAfpQuoteIndicatorClass
from app.backend.classes.payroll_umployment_insurance_indicator_class import PayrollUmploymentInsuranceIndicatorClass
from app.backend.classes.payroll_second_category_tax_class import PayrollSecondCategoryTaxClass

class PayrollCalculationClass:
    def __init__(self, db):
        self.db = db

    # Función para calcular la planilla de sueldos
    def calculate(self, period = None):
        return '2'