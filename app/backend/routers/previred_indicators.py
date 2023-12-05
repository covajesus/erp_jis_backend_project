from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import PreviredIndicator, UserLogin
from app.backend.classes.payroll_indicator_class import PayrollIndicatorClass
from app.backend.classes.payroll_uf_indicator_class import PayrollUfIndicatorClass
from app.backend.classes.payroll_utm_uta_indicator_class import PayrollUtmUtaIndicatorClass
from app.backend.classes.payroll_taxable_income_cap_indicator_class import PayrollTaxableIncomeCapIndicatorClass
from app.backend.classes.payroll_minium_taxable_income_indicator_class import PayrollMiniumTaxableIncomeIndicatorClass
from app.backend.classes.payroll_voluntary_previtional_indicator_class import PayrollVoluntaryPrevitionalIndicatorClass
from app.backend.classes.payroll_umployment_insurance_indicator_class import PayrollUmploymentInsuranceIndicatorClass
from app.backend.classes.payroll_afp_quote_indicator_class import PayrollAfpQuoteIndicatorClass
from app.backend.classes.payroll_family_asignation_indicator_class import PayrollFamilyAsignationIndicatorClass
from app.backend.classes.payroll_heavy_duty_quote_indicator_class import PayrollHeavyDutyQuoteIndicatorClass
from app.backend.classes.payroll_ccaf_indicator_class import PayrollCcafIndicator
from app.backend.auth.auth_user import get_current_active_user

previred_indicators = APIRouter(
    prefix="/previred_indicators",
    tags=["PreviredIndicators"]
)

@previred_indicators.post("/{period}")
def index(period:str, db: Session = Depends(get_db)):

    payroll_indicator_data = PayrollIndicatorClass(db).get_all(period)
    payroll_indicator_data = PayrollUfIndicatorClass(db).get_all(period)
    payroll_indicator_data = PayrollUtmUtaIndicatorClass(db).get_all(period)
    payroll_indicator_data = PayrollUtmUtaIndicatorClass(db).get_all(period)
    payroll_indicator_data = PayrollMiniumTaxableIncomeIndicatorClass(db).get_all(period)
    payroll_indicator_data = PayrollVoluntaryPrevitionalIndicatorClass(db).get_all(period)
    payroll_indicator_data = PayrollUmploymentInsuranceIndicatorClass(db).get_all(period)
    payroll_indicator_data = PayrollAfpQuoteIndicatorClass(db).get_all(period)
    payroll_indicator_data = PayrollFamilyAsignationIndicatorClass(db).get_all(period)
    payroll_indicator_data = PayrollHeavyDutyQuoteIndicatorClass(db).get_all(period)
    payroll_indicator_data = PayrollCcafIndicator(db).get_all(period)

    return {"message": 1}

@previred_indicators.post("/store")
def store(previred_indicator:PreviredIndicator, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    previred_indicator_inputs = previred_indicator.dict()

    PayrollIndicatorClass(db).store(previred_indicator_inputs)
    PayrollUfIndicatorClass(db).store(previred_indicator_inputs)
    PayrollUtmUtaIndicatorClass(db).store(previred_indicator_inputs)
    PayrollTaxableIncomeCapIndicatorClass(db).store(previred_indicator_inputs)
    PayrollMiniumTaxableIncomeIndicatorClass(db).store(previred_indicator_inputs)
    PayrollVoluntaryPrevitionalIndicatorClass(db).store(previred_indicator_inputs)
    PayrollUmploymentInsuranceIndicatorClass(db).store(previred_indicator_inputs)
    PayrollAfpQuoteIndicatorClass(db).store(previred_indicator_inputs)
    PayrollFamilyAsignationIndicatorClass(db).store(previred_indicator_inputs)
    PayrollHeavyDutyQuoteIndicatorClass(db).store(previred_indicator_inputs)
    PayrollCcafIndicator(db).store(previred_indicator_inputs)

    return {"message": 1}