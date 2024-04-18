import requests
from app.backend.db.models import DteBackgroundModel, CurrentDteBackgroundModel
import json

class DteClass:
    def __init__(self, db):
        self.db = db

    def get_total_quantity(user_inputs):

        if user_inputs['rol_id'] == 4 or user_inputs['rol_id'] == 5:
            user_inputs['rol_id'] = 1

        if user_inputs['rol_id'] == 3:
            user_inputs['rol_id'] = 4

        url = "https://jisparking.com/api/dte/receivable/"+ str(user_inputs['rol_id']) +"/"+ str(user_inputs['rut']) +"?api_token="+ str(user_inputs['api_token']) +""

        payload={}
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text
    
    def get_total_amount(user_inputs):

        if user_inputs['rol_id'] == 4 or user_inputs['rol_id'] == 5:
            user_inputs['rol_id'] = 1

        if user_inputs['rol_id'] == 3:
            user_inputs['rol_id'] = 4
            
        url = "https://jisparking.com/api/dte/receivable/"+ str(user_inputs['rol_id']) +"/"+ str(user_inputs['rut']) +"?api_token="+ str(user_inputs['api_token']) +""

        payload={}
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text

    def send_to_sii(self):
        data = self.db.query(CurrentDteBackgroundModel).all()

        for item in data:
            url = "https://apigateway.cl/api/v1/libredte/dte/documentos/generar?normalizar=1&formato=json&enviar_sii=0&gzip=0&retry=1&"

            payload = json.dumps({
                                    "dte": {
                                        "Encabezado": {
                                            "IdDoc": {
                                                "TipoDTE": 39,
                                                "Folio": item.folio
                                            },
                                            "Emisor": {
                                                "RUTEmisor": "76063822-6",
                                                "RznSoc": "J I S PARKING SPA",
                                                "GiroEmis": "EXPLOTACION DE ESTACIONAMIENTOS DE VEHICULOS AUTOMOTORES Y PARQUIMETRO",
                                                "Acteco": "522120",
                                                "DirOrigen": "Matucana 40",
                                                "CmnaOrigen": "Estacion Central"
                                            },
                                            "Receptor": {
                                                "RUTRecep": "66666666-6",
                                                "RznSocRecep": "Cliente Generico",
                                                "GiroRecep":"Particular",
                                                "DirRecep":"Santiago",
                                                "CmnaRecep":"Estacion Central"
                                            }
                                        },
                                        "Detalle": {
                                            "NmbItem": "Venta",
                                            "QtyItem": 1,
                                            "PrcItem": item.amount
                                        },
                                        "resolucion": {
                                            "fecha": "2014-06-17",
                                            "numero": 57
                                        },
                                        "caf": item.caf
                                    }
                                })
            
            headers = {
                'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZDU0ZDU3Y2MwYzQ0MGQxMzBhMTAyZGUxMzY1NmMxMTYwMDdkZWU0MDk0NTFhNDNkN2NmYmI4MzEwY2E1ZDZlMTJhOWE5YjhjZmNiMjFhNzEiLCJpYXQiOjE3MTMyOTkxNzQsIm5iZiI6MTcxMzI5OTE3NCwiZXhwIjo0ODY4OTcyNzc0LCJzdWIiOiI1NzYiLCJzY29wZXMiOltdfQ.raiFUdWy9tnClakm5uCoPJR8x7YMwHSSzdUSO5LcgJeUwebfPAIh9BnmxIcCN6rOp7DU19qi3kHNNrOmuxOVwxj9ysmoG_W0jBwdEffnt4XLtpEMLp3OtM848gwGflgx6Y3GFksPJeg2tdinntPPSHfxvPPCATUV52bPrQ04y9dTgpbTSyR5rAnSERr1OawLBP9cMXFMHv_CCVAUC614cvKNq51e2XK7U1n4FhQ3qTwLORfv1yzfENGrhFKcdciWrRi47DCEwH5C7zKk7hTqPj5YBxwX-NIGZJgDjJDFKixXlgR1iqigchfo-C8z5xnNgzybkva9X1-kIJt5EFVqLDXxxl9gAY_6k7Sxke6xhvImjQgsLg39oMGBiYp61K6MXvwhC1AZgTxiD3iPLhhlEJouA9zOnChFo5vdnIPwl0wyX0EgK27SCQqZIYujNvLnxNUCikF3QZ_kJfyAdzfiWhNC2J25Q10xxBcFkhtG9aw5j8pwUQS84oOr6BNC8ca54S-wZJIse758BDEnk3-WMlpuYPkmq8kRK3eeCyt-B06zUPr8BgnQP16c4m6DubEEhjrL7D3cCIgmwFG68BKt0G4iv5kRl5nilzhcr424fxva_UORfWk-xXGMd9bjFT3Ak77AIcZMDrDOIGj7VPE6IPoUWYHBw4PB6Co61L6QA_Y',
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            return 1
