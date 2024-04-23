import requests
from app.backend.db.models import DteBackgroundModel, CurrentDteBackgroundModel
import json
from app.backend.classes.helper_class import HelperClass
from app.backend.classes.dte_setting_class import DteSettingClass
from app.backend.classes.dte_background_class import DteBackgroundClass
from app.backend.classes.current_dte_background_class import CurrentDteBackgroundClass
from datetime import datetime

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

    def very_sent_to_sii(self):
        data = self.db.query(DteBackgroundModel).filter(
                DteBackgroundModel.track_id == 0).first()

        url = "https://apigateway.cl/api/v1/sii/dte/emitidos/verificar?certificacion=0"

        payload = json.dumps({
        "auth": {
                    "cert": {
                    "cert-data": "-----BEGIN CERTIFICATE-----\nMIIGjjCCBXagAwIBAgIDAR4jMA0GCSqGSIb3DQEBCwUAMIGmMQswCQYDVQQGEwJD\nTDEYMBYGA1UEChMPQWNlcHRhLmNvbSBTLkEuMUgwRgYDVQQDEz9BY2VwdGEuY29t\nIEF1dG9yaWRhZCBDZXJ0aWZpY2Fkb3JhIENsYXNlIDMgUGVyc29uYSBOYXR1cmFs\nIC0gRzQxHjAcBgkqhkiG9w0BCQEWD2luZm9AYWNlcHRhLmNvbTETMBEGA1UEBRMK\nOTY5MTkwNTAtODAeFw0yMTA3MDgyMzQwMjZaFw0yNDA3MDgyMzQwMjZaMIGXMQsw\nCQYDVQQGEwJDTDEYMBYGA1UEDBMPUEVSU09OQSBOQVRVUkFMMSswKQYDVQQDEyJN\nQVJDRUxPIEFMRUpBTkRSTyBJTlpVTlpBIEdPTlpBTEVaMSwwKgYJKoZIhvcNAQkB\nFh1DUklTVElBTklOWlVOWkFASklTUEFSS0lORy5DTDETMBEGA1UEBRMKMTAwMzM3\nNDEtSzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK/zoDtqd7+qB7aX\njS/kiBnLOf62orrMMdL3G22l0NJBziWVv/DezIgoFONUEF2XNXBWNAKTbLABvGIZ\nNFLyE4QuevdLd5AXuOt0q4+Y2msZemrP3zIkuT1dkNo/djj5gmFY3hC1i9DEj2ZQ\nF3kwcN9rrhQrzg3I0ixrRfdozMIypvCY4pWoJOvaNc8Z1a2Brq09QXQ3zUB3jXW7\nezxQlOCqv6G37UB9FzInnwAmicz5/92YtvFAXXJd4dtuaoPQt7Hn8XzhP8wmtj9j\nE9uHUbzK4CmQm4bYb1hmceg4crTHybTLUHngSlfI7QbDsLroaUlNgq8Kte8qDNxg\nqAhLkW0CAwEAAaOCAtAwggLMMB8GA1UdIwQYMBaAFKr9vcXpN032mU1XjsFxGvnr\nwwbjMB0GA1UdDgQWBBQYpMku0lGJKNQdxadkxl0mirm7uTALBgNVHQ8EBAMCBPAw\nHQYDVR0lBBYwFAYIKwYBBQUHAwIGCCsGAQUFBwMEMBEGCWCGSAGG+EIBAQQEAwIF\noDCB+gYDVR0gBIHyMIHvMIHsBggrBgEEAbVrAjCB3zAxBggrBgEFBQcCARYlaHR0\ncHM6Ly9hY2c0LmFjZXB0YS5jb20vQ1BTLUFjZXB0YWNvbTCBqQYIKwYBBQUHAgIw\ngZwwFhYPQWNlcHRhLmNvbSBTLkEuMAMCAQIagYFFbCB0aXR1bGFyIGhhIHNpZG8g\ndmFsaWRhZG8gZW4gZm9ybWEgcHJlc2VuY2lhbCwgcXVlZGFuZG8gaGFiaWxpdGFk\nbyBlbCBDZXJ0aWZpY2FkbyBwYXJhIHVzbyB0cmlidXRhcmlvLCBwYWdvcywgY29t\nZXJjaW8geSBvdHJvcy4wWgYDVR0SBFMwUaAYBggrBgEEAcEBAqAMFgo5NjkxOTA1\nMC04oCQGCCsGAQUFBwgDoBgwFgwKOTY5MTkwNTAtOAYIKwYBBAHBAQKBD2luZm9A\nYWNlcHRhLmNvbTBoBgNVHREEYTBfoBgGCCsGAQQBwQEBoAwWCjEwMDMzNzQxLUug\nJAYIKwYBBQUHCAOgGDAWDAoxMDAzMzc0MS1LBggrBgEEAcEBAoEdQ1JJU1RJQU5J\nTlpVTlpBQEpJU1BBUktJTkcuQ0wwRwYIKwYBBQUHAQEEOzA5MDcGCCsGAQUFBzAB\nhitodHRwczovL2FjZzQuYWNlcHRhLmNvbS9hY2c0L29jc3AvQ2xhc2UzLUc0MD8G\nA1UdHwQ4MDYwNKAyoDCGLmh0dHBzOi8vYWNnNC5hY2VwdGEuY29tL2FjZzQvY3Js\nL0NsYXNlMy1HNC5jcmwwDQYJKoZIhvcNAQELBQADggEBAAyvyBRFLpuF947AuBDm\nllTVh2Txrn2TK8bCl0iljnaCOdG3idmE5x9Ta7anzV0fL+ujQrUsSd7fa1n4PN9a\nn5rBmC/HR1DhBm4WIoVbVy3oz1GT2bmnfLOBqNKMvFNX0MJoOwYIkPxUcwRZXoPe\n6qe4tp4LAQiIUSxIbtVflXrctqX9m8PYf5wNA8gkiKK4qp8h+d+ZySAEHVFlHWb8\nY6TznjIwY05T46ATEyOVagDSijwW1Nj8m/8eJTF0vDKIzW6Uaa7YIPzVnkV0IHyE\nTyRne1CdJvynaEgs/BX84I1ovtsH2iEDX83xmKxtrdtPgO+Qin0kqHEu1EaEj9Qt\n6L0=\n-----END CERTIFICATE-----",
                    "pkey-data": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCv86A7ane/qge2\nl40v5IgZyzn+tqK6zDHS9xttpdDSQc4llb/w3syIKBTjVBBdlzVwVjQCk2ywAbxi\nGTRS8hOELnr3S3eQF7jrdKuPmNprGXpqz98yJLk9XZDaP3Y4+YJhWN4QtYvQxI9m\nUBd5MHDfa64UK84NyNIsa0X3aMzCMqbwmOKVqCTr2jXPGdWtga6tPUF0N81Ad411\nu3s8UJTgqr+ht+1AfRcyJ58AJonM+f/dmLbxQF1yXeHbbmqD0Lex5/F84T/MJrY/\nYxPbh1G8yuApkJuG2G9YZnHoOHK0x8m0y1B54EpXyO0Gw7C66GlJTYKvCrXvKgzc\nYKgIS5FtAgMBAAECggEBAJpWKwCzHSMD9AwX14JhBXkKqG5iqU8M+c9Bbc+6GPe1\nPSv+tQSFigcMkXXuMQTHM9q74pc31ah1fVbXIOx45uGVG8t7aP79r/jot+wXec9j\n49t5RyBm0g2f2wV1kS/cvJ7DItapSGDxaY+nRU/KS9fOTj3nRrEUrDbGSfMA/EqC\nRQT8BaHNDE9HwxsPOG66CCj9Bk40lZJD1XbWTey0NdhzcFDJya9gWvNQeKnXMo20\n9dltDvHhob2ULnbyUV3CNPsNFw/vCvqrb839ZUrBCh+IqCMrU/nrLuqmCpBIG+2/\naiNHgE7pIhfF/QpCbDwlbIH0HxQUTdPnJvAmmwZWGIkCgYEA/xF0WM4pQCRQF+Og\nCNdKjWkF/ZXS/tnpjxr2DmvMKwZX2nXMBHC7aHpfUCzj/Td69uK+AG4LnRkP1L3U\nyV0kXbMGUFcofVhYTDnPPNdlNyL5n2LKEmnYAYaJyYitEGoJN2hwplDMGH8kSKBH\nuymYN5ry5FfQfJGh17cjb/vP1s8CgYEAsJguDDB0uNC/oCEi1tSDG4RopV8tk/PH\nbtK1Fk0Qu7NliHr+PKb9w69wiw8BZ7dDU+igqJrywXl+Tnm8CvpbOAL8qQZqMzXM\nGvGBelWSq2HzxrIURD4X1yqzPvRKCTEbAPn4cgnmUBIpOtkdDJjrwuMD8dIT6J4y\nqmlpYZEWYwMCgYAEw4awwejzUbpNN+sdPygdTADYo5u1Nsyt54sA6fJ+OzgY1Gpj\nCtf1M5PkI3J+oDKjuchiqat926H4DzOSLzMmrNlJVtdiv+umQM4mDL/PL9AJsgak\nIWXvYVvhb7QLwm85obG46XlmW7mJwbSVQkmdgD9ZFGrIaM/k/36h8MoI8QKBgD8R\nChjmUTkTq+vXCacpW+0+21R76j4VaJrmey+MtDYkelVEf3lPtf7lr86pvDm7FDtq\nL74nIB0Cc545EXPmNx+IyYzfspu5UbwplbEH0IqOP84tGNnKRx9bq4oHGk2wENHH\nc/feGzdrVPgkQ6CVGFWQV39MJDoGDVgYrz7d3t3bAoGBAK+UnIFrRJ5UMsIM5Ao2\nryKtwPemdHypIVK3WOV1yRpa5aBqemrTQkijbLx8lVxoeID8Lw4zHybK6V9mAHsf\nRhfHsmBz3f4mYoKVoyVDelxpx+IGkGibvzNQB5BFWuu8kZeDPkhcPbk4pHFUf/jm\nCvLdtcSmumV5hxnVdtwjdlQD\n-----END PRIVATE KEY-----"
                    }
        },
        "dte": {
            "emisor": "76063822-6",
            "dte": 39,
            "folio": data.folio
        }
        })
        headers = {
                'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZDU0ZDU3Y2MwYzQ0MGQxMzBhMTAyZGUxMzY1NmMxMTYwMDdkZWU0MDk0NTFhNDNkN2NmYmI4MzEwY2E1ZDZlMTJhOWE5YjhjZmNiMjFhNzEiLCJpYXQiOjE3MTMyOTkxNzQsIm5iZiI6MTcxMzI5OTE3NCwiZXhwIjo0ODY4OTcyNzc0LCJzdWIiOiI1NzYiLCJzY29wZXMiOltdfQ.raiFUdWy9tnClakm5uCoPJR8x7YMwHSSzdUSO5LcgJeUwebfPAIh9BnmxIcCN6rOp7DU19qi3kHNNrOmuxOVwxj9ysmoG_W0jBwdEffnt4XLtpEMLp3OtM848gwGflgx6Y3GFksPJeg2tdinntPPSHfxvPPCATUV52bPrQ04y9dTgpbTSyR5rAnSERr1OawLBP9cMXFMHv_CCVAUC614cvKNq51e2XK7U1n4FhQ3qTwLORfv1yzfENGrhFKcdciWrRi47DCEwH5C7zKk7hTqPj5YBxwX-NIGZJgDjJDFKixXlgR1iqigchfo-C8z5xnNgzybkva9X1-kIJt5EFVqLDXxxl9gAY_6k7Sxke6xhvImjQgsLg39oMGBiYp61K6MXvwhC1AZgTxiD3iPLhhlEJouA9zOnChFo5vdnIPwl0wyX0EgK27SCQqZIYujNvLnxNUCikF3QZ_kJfyAdzfiWhNC2J25Q10xxBcFkhtG9aw5j8pwUQS84oOr6BNC8ca54S-wZJIse758BDEnk3-WMlpuYPkmq8kRK3eeCyt-B06zUPr8BgnQP16c4m6DubEEhjrL7D3cCIgmwFG68BKt0G4iv5kRl5nilzhcr424fxva_UORfWk-xXGMd9bjFT3Ak77AIcZMDrDOIGj7VPE6IPoUWYHBw4PB6Co61L6QA_Y',
                'Content-Type': 'application/json',
                'Cookie': '0chW9sKq57wqKBvjuHb6qbBG2RQgUCymhec2t7wz=eyJpdiI6IjVQdEVDd2E2OThLcHlyU2Rrckp5K3c9PSIsInZhbHVlIjoiZUVCS0szOXVjcGpXdnBtQURGMTNQamhOcmJGSXV5U1cvaTZ0TGFPMU9tcFhjT0FZZ25xYUlSRHUrRnNhTy9lMEdCbFJhc0JUWEcrZDBieTllOVFCaGQ2K1YxbklZQ2tFVC9TbmhJZmF3S2RnaGl0ei9IQUptNk8yaWNCNm5TSTI2dzJ1UkJvZS8wcG5PakduK3pGeUwwbGtERm8xRTdnMkpUVDRUUUU4YVQ0a2FmanJkelFoNVRyNFZMTVRRYTlPV3VUclZwbWNRU0x2VW1nMm13bFV4VlJ3aHVWRXdXa24vcVFRVmZwNk41bDkzQklNeVl5b1cySzRNS0Z1VHNqSDA4SVh4UmY3Q0RkaUpCbVpjKzRJTjFCekdrTWprNXdPUHlVVi9pZzhRSGc0ZkxjSThNK3VFOWgwT0Q3QllFYUNJZ0c1czFRdXY1Wkp3ZlNhc05nb204SjRhaXVMTlBqUkdSZ2wxcGNPMm1ZVEUxaEFPNWloYzgrbGdvWTFxaHEvIiwibWFjIjoiYzIyYzNmMjNlNzdmYTJjYmIwMjJkM2I0YTE4MzU5NTU5YTY4MWEyZDAwNjFiOGUyZDgxYzk0MTkzM2IwY2M2NyIsInRhZyI6IiJ9; XSRF-TOKEN=eyJpdiI6Ik9hcnQwejI5UzdDUE82cFpLc3RJZ0E9PSIsInZhbHVlIjoid2hsdWJNZWFISHRXdGQxcWtnNnZVNnJzNjFPZEkwWDZOaUZuZGdCMjRodTcrOWFFbkZmR0FiWnBJN3A3RzZvYmNDRlZVQ1dEN3M2S1BrU01VMUdTNmNCV2NuVjhDUlBvN1RCY2pxT0RWY1gyNExvZEx1T0dJWUZtSGJITG5tVzIiLCJtYWMiOiI1NThiZDBkN2JkZWMyOWJkYzIzNDI5NzFlMTU4YmE0YWViYmUwOTRiZjhiNDYwZmE2NmM4MjEzNTdkNDU4NWJkIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6ImtvWURKL05SaFZmcTN6azBlMGROOWc9PSIsInZhbHVlIjoiaWlyZnBOOWJjZjd3RW05WStzYUI4TTk0ODVEdkFDNG5LUXo1dnMzYmJvb1AwK0tZaElhU2xFZ2JDUWJpTXN5VG5samF2UWV4dWRHKytjVC82YUVZRVhHQ2ZLQm1LRlFNZ25iSWVCMG56N1lYNlBrY0pNQ29ORzZhckNJUHdERjMiLCJtYWMiOiJkYzI5ZjA2MDU1MTMxM2U4OGVjNTkwMWRmOTA3MmRhODM1Mzk2MWY4NjIxM2M0ODFmYWJkZWU1NTg0MTdjYjkwIiwidGFnIjoiIn0%3D'
                }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
   
    def send_to_sii(self, machine_id):
        url = "https://jisparking.com/api/folio_background/"+ str(machine_id) +"?api_token=AtWYamNvDOfgDOEY6UbXgvGqDiRPR7QOt9Si1hbeMmat4g2Qfxzg7LlT5yzNz5LOozQbcA9uibaSTu4t"
        response = requests.post(url)
        response_decoded = json.loads(response.text)
        if "data" in response_decoded:
            data = response_decoded["data"]
            for item in data:
                folio_number = item['folio']
                date = item['bill_date']

                date = HelperClass().split(str(date), " ")

                url2 = "https://jisparking.com/api/api_transaction/show/"+ str(folio_number) +"?api_token=AtWYamNvDOfgDOEY6UbXgvGqDiRPR7QOt9Si1hbeMmat4g2Qfxzg7LlT5yzNz5LOozQbcA9uibaSTu4t"
                response_2 = requests.get(url2)

                response_decoded_2 = json.loads(response_2.text)

                total_amount = response_decoded_2['data']['total']

                url3 = "https://jisparking.com/api/caf/show/"+ str(folio_number) +"?api_token=AtWYamNvDOfgDOEY6UbXgvGqDiRPR7QOt9Si1hbeMmat4g2Qfxzg7LlT5yzNz5LOozQbcA9uibaSTu4t"
                response_3 = requests.get(url3)

                response_decoded_3 = json.loads(response_3.text)

                caf = response_decoded_3['data']['xml_base64']

                dte_settings = DteSettingClass(self.db).get()

                folio_quantity_to_send = dte_settings.folio_quantity_to_send

                folio_quantity_sent = dte_settings.folio_quantity_sent

                folio_quantity_limit = dte_settings.folio_quantity_limit

                if int(folio_quantity_to_send)- int(folio_quantity_sent) < int(folio_quantity_limit):

                    url = "https://apigateway.cl/api/v1/libredte/dte/documentos/generar?normalizar=1&formato=json&enviar_sii=0&gzip=0&retry=1&"

                    payload = json.dumps({
                    "auth": {
                        "cert": {
                        "cert-data": "-----BEGIN CERTIFICATE-----\nMIIGjjCCBXagAwIBAgIDAR4jMA0GCSqGSIb3DQEBCwUAMIGmMQswCQYDVQQGEwJD\nTDEYMBYGA1UEChMPQWNlcHRhLmNvbSBTLkEuMUgwRgYDVQQDEz9BY2VwdGEuY29t\nIEF1dG9yaWRhZCBDZXJ0aWZpY2Fkb3JhIENsYXNlIDMgUGVyc29uYSBOYXR1cmFs\nIC0gRzQxHjAcBgkqhkiG9w0BCQEWD2luZm9AYWNlcHRhLmNvbTETMBEGA1UEBRMK\nOTY5MTkwNTAtODAeFw0yMTA3MDgyMzQwMjZaFw0yNDA3MDgyMzQwMjZaMIGXMQsw\nCQYDVQQGEwJDTDEYMBYGA1UEDBMPUEVSU09OQSBOQVRVUkFMMSswKQYDVQQDEyJN\nQVJDRUxPIEFMRUpBTkRSTyBJTlpVTlpBIEdPTlpBTEVaMSwwKgYJKoZIhvcNAQkB\nFh1DUklTVElBTklOWlVOWkFASklTUEFSS0lORy5DTDETMBEGA1UEBRMKMTAwMzM3\nNDEtSzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK/zoDtqd7+qB7aX\njS/kiBnLOf62orrMMdL3G22l0NJBziWVv/DezIgoFONUEF2XNXBWNAKTbLABvGIZ\nNFLyE4QuevdLd5AXuOt0q4+Y2msZemrP3zIkuT1dkNo/djj5gmFY3hC1i9DEj2ZQ\nF3kwcN9rrhQrzg3I0ixrRfdozMIypvCY4pWoJOvaNc8Z1a2Brq09QXQ3zUB3jXW7\nezxQlOCqv6G37UB9FzInnwAmicz5/92YtvFAXXJd4dtuaoPQt7Hn8XzhP8wmtj9j\nE9uHUbzK4CmQm4bYb1hmceg4crTHybTLUHngSlfI7QbDsLroaUlNgq8Kte8qDNxg\nqAhLkW0CAwEAAaOCAtAwggLMMB8GA1UdIwQYMBaAFKr9vcXpN032mU1XjsFxGvnr\nwwbjMB0GA1UdDgQWBBQYpMku0lGJKNQdxadkxl0mirm7uTALBgNVHQ8EBAMCBPAw\nHQYDVR0lBBYwFAYIKwYBBQUHAwIGCCsGAQUFBwMEMBEGCWCGSAGG+EIBAQQEAwIF\noDCB+gYDVR0gBIHyMIHvMIHsBggrBgEEAbVrAjCB3zAxBggrBgEFBQcCARYlaHR0\ncHM6Ly9hY2c0LmFjZXB0YS5jb20vQ1BTLUFjZXB0YWNvbTCBqQYIKwYBBQUHAgIw\ngZwwFhYPQWNlcHRhLmNvbSBTLkEuMAMCAQIagYFFbCB0aXR1bGFyIGhhIHNpZG8g\ndmFsaWRhZG8gZW4gZm9ybWEgcHJlc2VuY2lhbCwgcXVlZGFuZG8gaGFiaWxpdGFk\nbyBlbCBDZXJ0aWZpY2FkbyBwYXJhIHVzbyB0cmlidXRhcmlvLCBwYWdvcywgY29t\nZXJjaW8geSBvdHJvcy4wWgYDVR0SBFMwUaAYBggrBgEEAcEBAqAMFgo5NjkxOTA1\nMC04oCQGCCsGAQUFBwgDoBgwFgwKOTY5MTkwNTAtOAYIKwYBBAHBAQKBD2luZm9A\nYWNlcHRhLmNvbTBoBgNVHREEYTBfoBgGCCsGAQQBwQEBoAwWCjEwMDMzNzQxLUug\nJAYIKwYBBQUHCAOgGDAWDAoxMDAzMzc0MS1LBggrBgEEAcEBAoEdQ1JJU1RJQU5J\nTlpVTlpBQEpJU1BBUktJTkcuQ0wwRwYIKwYBBQUHAQEEOzA5MDcGCCsGAQUFBzAB\nhitodHRwczovL2FjZzQuYWNlcHRhLmNvbS9hY2c0L29jc3AvQ2xhc2UzLUc0MD8G\nA1UdHwQ4MDYwNKAyoDCGLmh0dHBzOi8vYWNnNC5hY2VwdGEuY29tL2FjZzQvY3Js\nL0NsYXNlMy1HNC5jcmwwDQYJKoZIhvcNAQELBQADggEBAAyvyBRFLpuF947AuBDm\nllTVh2Txrn2TK8bCl0iljnaCOdG3idmE5x9Ta7anzV0fL+ujQrUsSd7fa1n4PN9a\nn5rBmC/HR1DhBm4WIoVbVy3oz1GT2bmnfLOBqNKMvFNX0MJoOwYIkPxUcwRZXoPe\n6qe4tp4LAQiIUSxIbtVflXrctqX9m8PYf5wNA8gkiKK4qp8h+d+ZySAEHVFlHWb8\nY6TznjIwY05T46ATEyOVagDSijwW1Nj8m/8eJTF0vDKIzW6Uaa7YIPzVnkV0IHyE\nTyRne1CdJvynaEgs/BX84I1ovtsH2iEDX83xmKxtrdtPgO+Qin0kqHEu1EaEj9Qt\n6L0=\n-----END CERTIFICATE-----",
                        "pkey-data": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCv86A7ane/qge2\nl40v5IgZyzn+tqK6zDHS9xttpdDSQc4llb/w3syIKBTjVBBdlzVwVjQCk2ywAbxi\nGTRS8hOELnr3S3eQF7jrdKuPmNprGXpqz98yJLk9XZDaP3Y4+YJhWN4QtYvQxI9m\nUBd5MHDfa64UK84NyNIsa0X3aMzCMqbwmOKVqCTr2jXPGdWtga6tPUF0N81Ad411\nu3s8UJTgqr+ht+1AfRcyJ58AJonM+f/dmLbxQF1yXeHbbmqD0Lex5/F84T/MJrY/\nYxPbh1G8yuApkJuG2G9YZnHoOHK0x8m0y1B54EpXyO0Gw7C66GlJTYKvCrXvKgzc\nYKgIS5FtAgMBAAECggEBAJpWKwCzHSMD9AwX14JhBXkKqG5iqU8M+c9Bbc+6GPe1\nPSv+tQSFigcMkXXuMQTHM9q74pc31ah1fVbXIOx45uGVG8t7aP79r/jot+wXec9j\n49t5RyBm0g2f2wV1kS/cvJ7DItapSGDxaY+nRU/KS9fOTj3nRrEUrDbGSfMA/EqC\nRQT8BaHNDE9HwxsPOG66CCj9Bk40lZJD1XbWTey0NdhzcFDJya9gWvNQeKnXMo20\n9dltDvHhob2ULnbyUV3CNPsNFw/vCvqrb839ZUrBCh+IqCMrU/nrLuqmCpBIG+2/\naiNHgE7pIhfF/QpCbDwlbIH0HxQUTdPnJvAmmwZWGIkCgYEA/xF0WM4pQCRQF+Og\nCNdKjWkF/ZXS/tnpjxr2DmvMKwZX2nXMBHC7aHpfUCzj/Td69uK+AG4LnRkP1L3U\nyV0kXbMGUFcofVhYTDnPPNdlNyL5n2LKEmnYAYaJyYitEGoJN2hwplDMGH8kSKBH\nuymYN5ry5FfQfJGh17cjb/vP1s8CgYEAsJguDDB0uNC/oCEi1tSDG4RopV8tk/PH\nbtK1Fk0Qu7NliHr+PKb9w69wiw8BZ7dDU+igqJrywXl+Tnm8CvpbOAL8qQZqMzXM\nGvGBelWSq2HzxrIURD4X1yqzPvRKCTEbAPn4cgnmUBIpOtkdDJjrwuMD8dIT6J4y\nqmlpYZEWYwMCgYAEw4awwejzUbpNN+sdPygdTADYo5u1Nsyt54sA6fJ+OzgY1Gpj\nCtf1M5PkI3J+oDKjuchiqat926H4DzOSLzMmrNlJVtdiv+umQM4mDL/PL9AJsgak\nIWXvYVvhb7QLwm85obG46XlmW7mJwbSVQkmdgD9ZFGrIaM/k/36h8MoI8QKBgD8R\nChjmUTkTq+vXCacpW+0+21R76j4VaJrmey+MtDYkelVEf3lPtf7lr86pvDm7FDtq\nL74nIB0Cc545EXPmNx+IyYzfspu5UbwplbEH0IqOP84tGNnKRx9bq4oHGk2wENHH\nc/feGzdrVPgkQ6CVGFWQV39MJDoGDVgYrz7d3t3bAoGBAK+UnIFrRJ5UMsIM5Ao2\nryKtwPemdHypIVK3WOV1yRpa5aBqemrTQkijbLx8lVxoeID8Lw4zHybK6V9mAHsf\nRhfHsmBz3f4mYoKVoyVDelxpx+IGkGibvzNQB5BFWuu8kZeDPkhcPbk4pHFUf/jm\nCvLdtcSmumV5hxnVdtwjdlQD\n-----END PRIVATE KEY-----"
                        }
                    },
                    "dte": {
                        "Encabezado": {
                        "IdDoc": {
                            "TipoDTE": 39,
                            "Folio": folio_number,
                            "FchEmis": str(date[0])
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
                            "GiroRecep": "Particular",
                            "DirRecep": "Santiago",
                            "CmnaRecep": "Estacion Central"
                        }
                        },
                        "Detalle": {
                        "NmbItem": "Venta",
                        "QtyItem": 1,
                        "PrcItem": total_amount
                        }
                    },
                    "resolucion": {
                        "fecha": "2014-06-17",
                        "numero": 57
                    },
                    "caf": str(caf),
                    })
                    headers = {
                    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZDU0ZDU3Y2MwYzQ0MGQxMzBhMTAyZGUxMzY1NmMxMTYwMDdkZWU0MDk0NTFhNDNkN2NmYmI4MzEwY2E1ZDZlMTJhOWE5YjhjZmNiMjFhNzEiLCJpYXQiOjE3MTMyOTkxNzQsIm5iZiI6MTcxMzI5OTE3NCwiZXhwIjo0ODY4OTcyNzc0LCJzdWIiOiI1NzYiLCJzY29wZXMiOltdfQ.raiFUdWy9tnClakm5uCoPJR8x7YMwHSSzdUSO5LcgJeUwebfPAIh9BnmxIcCN6rOp7DU19qi3kHNNrOmuxOVwxj9ysmoG_W0jBwdEffnt4XLtpEMLp3OtM848gwGflgx6Y3GFksPJeg2tdinntPPSHfxvPPCATUV52bPrQ04y9dTgpbTSyR5rAnSERr1OawLBP9cMXFMHv_CCVAUC614cvKNq51e2XK7U1n4FhQ3qTwLORfv1yzfENGrhFKcdciWrRi47DCEwH5C7zKk7hTqPj5YBxwX-NIGZJgDjJDFKixXlgR1iqigchfo-C8z5xnNgzybkva9X1-kIJt5EFVqLDXxxl9gAY_6k7Sxke6xhvImjQgsLg39oMGBiYp61K6MXvwhC1AZgTxiD3iPLhhlEJouA9zOnChFo5vdnIPwl0wyX0EgK27SCQqZIYujNvLnxNUCikF3QZ_kJfyAdzfiWhNC2J25Q10xxBcFkhtG9aw5j8pwUQS84oOr6BNC8ca54S-wZJIse758BDEnk3-WMlpuYPkmq8kRK3eeCyt-B06zUPr8BgnQP16c4m6DubEEhjrL7D3cCIgmwFG68BKt0G4iv5kRl5nilzhcr424fxva_UORfWk-xXGMd9bjFT3Ak77AIcZMDrDOIGj7VPE6IPoUWYHBw4PB6Co61L6QA_Y',
                    'Content-Type': 'application/json',
                    'Cookie': '0chW9sKq57wqKBvjuHb6qbBG2RQgUCymhec2t7wz=eyJpdiI6IjVQdEVDd2E2OThLcHlyU2Rrckp5K3c9PSIsInZhbHVlIjoiZUVCS0szOXVjcGpXdnBtQURGMTNQamhOcmJGSXV5U1cvaTZ0TGFPMU9tcFhjT0FZZ25xYUlSRHUrRnNhTy9lMEdCbFJhc0JUWEcrZDBieTllOVFCaGQ2K1YxbklZQ2tFVC9TbmhJZmF3S2RnaGl0ei9IQUptNk8yaWNCNm5TSTI2dzJ1UkJvZS8wcG5PakduK3pGeUwwbGtERm8xRTdnMkpUVDRUUUU4YVQ0a2FmanJkelFoNVRyNFZMTVRRYTlPV3VUclZwbWNRU0x2VW1nMm13bFV4VlJ3aHVWRXdXa24vcVFRVmZwNk41bDkzQklNeVl5b1cySzRNS0Z1VHNqSDA4SVh4UmY3Q0RkaUpCbVpjKzRJTjFCekdrTWprNXdPUHlVVi9pZzhRSGc0ZkxjSThNK3VFOWgwT0Q3QllFYUNJZ0c1czFRdXY1Wkp3ZlNhc05nb204SjRhaXVMTlBqUkdSZ2wxcGNPMm1ZVEUxaEFPNWloYzgrbGdvWTFxaHEvIiwibWFjIjoiYzIyYzNmMjNlNzdmYTJjYmIwMjJkM2I0YTE4MzU5NTU5YTY4MWEyZDAwNjFiOGUyZDgxYzk0MTkzM2IwY2M2NyIsInRhZyI6IiJ9; XSRF-TOKEN=eyJpdiI6Ik9hcnQwejI5UzdDUE82cFpLc3RJZ0E9PSIsInZhbHVlIjoid2hsdWJNZWFISHRXdGQxcWtnNnZVNnJzNjFPZEkwWDZOaUZuZGdCMjRodTcrOWFFbkZmR0FiWnBJN3A3RzZvYmNDRlZVQ1dEN3M2S1BrU01VMUdTNmNCV2NuVjhDUlBvN1RCY2pxT0RWY1gyNExvZEx1T0dJWUZtSGJITG5tVzIiLCJtYWMiOiI1NThiZDBkN2JkZWMyOWJkYzIzNDI5NzFlMTU4YmE0YWViYmUwOTRiZjhiNDYwZmE2NmM4MjEzNTdkNDU4NWJkIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6ImtvWURKL05SaFZmcTN6azBlMGROOWc9PSIsInZhbHVlIjoiaWlyZnBOOWJjZjd3RW05WStzYUI4TTk0ODVEdkFDNG5LUXo1dnMzYmJvb1AwK0tZaElhU2xFZ2JDUWJpTXN5VG5samF2UWV4dWRHKytjVC82YUVZRVhHQ2ZLQm1LRlFNZ25iSWVCMG56N1lYNlBrY0pNQ29ORzZhckNJUHdERjMiLCJtYWMiOiJkYzI5ZjA2MDU1MTMxM2U4OGVjNTkwMWRmOTA3MmRhODM1Mzk2MWY4NjIxM2M0ODFmYWJkZWU1NTg0MTdjYjkwIiwidGFnIjoiIn0%3D'
                    }

                    response = requests.request("POST", url, headers=headers, data=payload)

                    rate_limit_limit = response.headers.get('X-RateLimit-Remaining')

                    if int(folio_quantity_to_send) - int(rate_limit_limit) < int(folio_quantity_limit):
                        DteSettingClass(self.db).update(rate_limit_limit)
                
                        response_decoded = json.loads(response.text)

                        xml = response_decoded.get("xml")

                        url = "https://apigateway.cl/api/v1/libredte/dte/envios/enviar?certificacion=0&gzip=0&retry=1"

                        payload = json.dumps({
                        "auth": {
                            "cert": {
                            "cert-data": "-----BEGIN CERTIFICATE-----\nMIIGjjCCBXagAwIBAgIDAR4jMA0GCSqGSIb3DQEBCwUAMIGmMQswCQYDVQQGEwJD\nTDEYMBYGA1UEChMPQWNlcHRhLmNvbSBTLkEuMUgwRgYDVQQDEz9BY2VwdGEuY29t\nIEF1dG9yaWRhZCBDZXJ0aWZpY2Fkb3JhIENsYXNlIDMgUGVyc29uYSBOYXR1cmFs\nIC0gRzQxHjAcBgkqhkiG9w0BCQEWD2luZm9AYWNlcHRhLmNvbTETMBEGA1UEBRMK\nOTY5MTkwNTAtODAeFw0yMTA3MDgyMzQwMjZaFw0yNDA3MDgyMzQwMjZaMIGXMQsw\nCQYDVQQGEwJDTDEYMBYGA1UEDBMPUEVSU09OQSBOQVRVUkFMMSswKQYDVQQDEyJN\nQVJDRUxPIEFMRUpBTkRSTyBJTlpVTlpBIEdPTlpBTEVaMSwwKgYJKoZIhvcNAQkB\nFh1DUklTVElBTklOWlVOWkFASklTUEFSS0lORy5DTDETMBEGA1UEBRMKMTAwMzM3\nNDEtSzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK/zoDtqd7+qB7aX\njS/kiBnLOf62orrMMdL3G22l0NJBziWVv/DezIgoFONUEF2XNXBWNAKTbLABvGIZ\nNFLyE4QuevdLd5AXuOt0q4+Y2msZemrP3zIkuT1dkNo/djj5gmFY3hC1i9DEj2ZQ\nF3kwcN9rrhQrzg3I0ixrRfdozMIypvCY4pWoJOvaNc8Z1a2Brq09QXQ3zUB3jXW7\nezxQlOCqv6G37UB9FzInnwAmicz5/92YtvFAXXJd4dtuaoPQt7Hn8XzhP8wmtj9j\nE9uHUbzK4CmQm4bYb1hmceg4crTHybTLUHngSlfI7QbDsLroaUlNgq8Kte8qDNxg\nqAhLkW0CAwEAAaOCAtAwggLMMB8GA1UdIwQYMBaAFKr9vcXpN032mU1XjsFxGvnr\nwwbjMB0GA1UdDgQWBBQYpMku0lGJKNQdxadkxl0mirm7uTALBgNVHQ8EBAMCBPAw\nHQYDVR0lBBYwFAYIKwYBBQUHAwIGCCsGAQUFBwMEMBEGCWCGSAGG+EIBAQQEAwIF\noDCB+gYDVR0gBIHyMIHvMIHsBggrBgEEAbVrAjCB3zAxBggrBgEFBQcCARYlaHR0\ncHM6Ly9hY2c0LmFjZXB0YS5jb20vQ1BTLUFjZXB0YWNvbTCBqQYIKwYBBQUHAgIw\ngZwwFhYPQWNlcHRhLmNvbSBTLkEuMAMCAQIagYFFbCB0aXR1bGFyIGhhIHNpZG8g\ndmFsaWRhZG8gZW4gZm9ybWEgcHJlc2VuY2lhbCwgcXVlZGFuZG8gaGFiaWxpdGFk\nbyBlbCBDZXJ0aWZpY2FkbyBwYXJhIHVzbyB0cmlidXRhcmlvLCBwYWdvcywgY29t\nZXJjaW8geSBvdHJvcy4wWgYDVR0SBFMwUaAYBggrBgEEAcEBAqAMFgo5NjkxOTA1\nMC04oCQGCCsGAQUFBwgDoBgwFgwKOTY5MTkwNTAtOAYIKwYBBAHBAQKBD2luZm9A\nYWNlcHRhLmNvbTBoBgNVHREEYTBfoBgGCCsGAQQBwQEBoAwWCjEwMDMzNzQxLUug\nJAYIKwYBBQUHCAOgGDAWDAoxMDAzMzc0MS1LBggrBgEEAcEBAoEdQ1JJU1RJQU5J\nTlpVTlpBQEpJU1BBUktJTkcuQ0wwRwYIKwYBBQUHAQEEOzA5MDcGCCsGAQUFBzAB\nhitodHRwczovL2FjZzQuYWNlcHRhLmNvbS9hY2c0L29jc3AvQ2xhc2UzLUc0MD8G\nA1UdHwQ4MDYwNKAyoDCGLmh0dHBzOi8vYWNnNC5hY2VwdGEuY29tL2FjZzQvY3Js\nL0NsYXNlMy1HNC5jcmwwDQYJKoZIhvcNAQELBQADggEBAAyvyBRFLpuF947AuBDm\nllTVh2Txrn2TK8bCl0iljnaCOdG3idmE5x9Ta7anzV0fL+ujQrUsSd7fa1n4PN9a\nn5rBmC/HR1DhBm4WIoVbVy3oz1GT2bmnfLOBqNKMvFNX0MJoOwYIkPxUcwRZXoPe\n6qe4tp4LAQiIUSxIbtVflXrctqX9m8PYf5wNA8gkiKK4qp8h+d+ZySAEHVFlHWb8\nY6TznjIwY05T46ATEyOVagDSijwW1Nj8m/8eJTF0vDKIzW6Uaa7YIPzVnkV0IHyE\nTyRne1CdJvynaEgs/BX84I1ovtsH2iEDX83xmKxtrdtPgO+Qin0kqHEu1EaEj9Qt\n6L0=\n-----END CERTIFICATE-----",
                            "pkey-data": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCv86A7ane/qge2\nl40v5IgZyzn+tqK6zDHS9xttpdDSQc4llb/w3syIKBTjVBBdlzVwVjQCk2ywAbxi\nGTRS8hOELnr3S3eQF7jrdKuPmNprGXpqz98yJLk9XZDaP3Y4+YJhWN4QtYvQxI9m\nUBd5MHDfa64UK84NyNIsa0X3aMzCMqbwmOKVqCTr2jXPGdWtga6tPUF0N81Ad411\nu3s8UJTgqr+ht+1AfRcyJ58AJonM+f/dmLbxQF1yXeHbbmqD0Lex5/F84T/MJrY/\nYxPbh1G8yuApkJuG2G9YZnHoOHK0x8m0y1B54EpXyO0Gw7C66GlJTYKvCrXvKgzc\nYKgIS5FtAgMBAAECggEBAJpWKwCzHSMD9AwX14JhBXkKqG5iqU8M+c9Bbc+6GPe1\nPSv+tQSFigcMkXXuMQTHM9q74pc31ah1fVbXIOx45uGVG8t7aP79r/jot+wXec9j\n49t5RyBm0g2f2wV1kS/cvJ7DItapSGDxaY+nRU/KS9fOTj3nRrEUrDbGSfMA/EqC\nRQT8BaHNDE9HwxsPOG66CCj9Bk40lZJD1XbWTey0NdhzcFDJya9gWvNQeKnXMo20\n9dltDvHhob2ULnbyUV3CNPsNFw/vCvqrb839ZUrBCh+IqCMrU/nrLuqmCpBIG+2/\naiNHgE7pIhfF/QpCbDwlbIH0HxQUTdPnJvAmmwZWGIkCgYEA/xF0WM4pQCRQF+Og\nCNdKjWkF/ZXS/tnpjxr2DmvMKwZX2nXMBHC7aHpfUCzj/Td69uK+AG4LnRkP1L3U\nyV0kXbMGUFcofVhYTDnPPNdlNyL5n2LKEmnYAYaJyYitEGoJN2hwplDMGH8kSKBH\nuymYN5ry5FfQfJGh17cjb/vP1s8CgYEAsJguDDB0uNC/oCEi1tSDG4RopV8tk/PH\nbtK1Fk0Qu7NliHr+PKb9w69wiw8BZ7dDU+igqJrywXl+Tnm8CvpbOAL8qQZqMzXM\nGvGBelWSq2HzxrIURD4X1yqzPvRKCTEbAPn4cgnmUBIpOtkdDJjrwuMD8dIT6J4y\nqmlpYZEWYwMCgYAEw4awwejzUbpNN+sdPygdTADYo5u1Nsyt54sA6fJ+OzgY1Gpj\nCtf1M5PkI3J+oDKjuchiqat926H4DzOSLzMmrNlJVtdiv+umQM4mDL/PL9AJsgak\nIWXvYVvhb7QLwm85obG46XlmW7mJwbSVQkmdgD9ZFGrIaM/k/36h8MoI8QKBgD8R\nChjmUTkTq+vXCacpW+0+21R76j4VaJrmey+MtDYkelVEf3lPtf7lr86pvDm7FDtq\nL74nIB0Cc545EXPmNx+IyYzfspu5UbwplbEH0IqOP84tGNnKRx9bq4oHGk2wENHH\nc/feGzdrVPgkQ6CVGFWQV39MJDoGDVgYrz7d3t3bAoGBAK+UnIFrRJ5UMsIM5Ao2\nryKtwPemdHypIVK3WOV1yRpa5aBqemrTQkijbLx8lVxoeID8Lw4zHybK6V9mAHsf\nRhfHsmBz3f4mYoKVoyVDelxpx+IGkGibvzNQB5BFWuu8kZeDPkhcPbk4pHFUf/jm\nCvLdtcSmumV5hxnVdtwjdlQD\n-----END PRIVATE KEY-----"
                            }
                        },
                        "emisor": "76063822-6",
                        "xml": str(xml['sii'])
                        })
                        headers = {
                        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZDU0ZDU3Y2MwYzQ0MGQxMzBhMTAyZGUxMzY1NmMxMTYwMDdkZWU0MDk0NTFhNDNkN2NmYmI4MzEwY2E1ZDZlMTJhOWE5YjhjZmNiMjFhNzEiLCJpYXQiOjE3MTMyOTkxNzQsIm5iZiI6MTcxMzI5OTE3NCwiZXhwIjo0ODY4OTcyNzc0LCJzdWIiOiI1NzYiLCJzY29wZXMiOltdfQ.raiFUdWy9tnClakm5uCoPJR8x7YMwHSSzdUSO5LcgJeUwebfPAIh9BnmxIcCN6rOp7DU19qi3kHNNrOmuxOVwxj9ysmoG_W0jBwdEffnt4XLtpEMLp3OtM848gwGflgx6Y3GFksPJeg2tdinntPPSHfxvPPCATUV52bPrQ04y9dTgpbTSyR5rAnSERr1OawLBP9cMXFMHv_CCVAUC614cvKNq51e2XK7U1n4FhQ3qTwLORfv1yzfENGrhFKcdciWrRi47DCEwH5C7zKk7hTqPj5YBxwX-NIGZJgDjJDFKixXlgR1iqigchfo-C8z5xnNgzybkva9X1-kIJt5EFVqLDXxxl9gAY_6k7Sxke6xhvImjQgsLg39oMGBiYp61K6MXvwhC1AZgTxiD3iPLhhlEJouA9zOnChFo5vdnIPwl0wyX0EgK27SCQqZIYujNvLnxNUCikF3QZ_kJfyAdzfiWhNC2J25Q10xxBcFkhtG9aw5j8pwUQS84oOr6BNC8ca54S-wZJIse758BDEnk3-WMlpuYPkmq8kRK3eeCyt-B06zUPr8BgnQP16c4m6DubEEhjrL7D3cCIgmwFG68BKt0G4iv5kRl5nilzhcr424fxva_UORfWk-xXGMd9bjFT3Ak77AIcZMDrDOIGj7VPE6IPoUWYHBw4PB6Co61L6QA_Y',
                        'Content-Type': 'application/json'
                        }

                        response = requests.request("POST", url, headers=headers, data=payload)

                        DteSettingClass(self.db).update(rate_limit_limit)

                        response_decoded = json.loads(response.text)

                        track_id = response_decoded.get("track_id")

                        sii_date = response_decoded.get("fecha_recepcion")

                        status = response_decoded.get("estado")
                        print(status)
                        if status == 'REC':
                            print(folio_number)
                            print(track_id)
                            print(sii_date)
                            url4 = "https://jisparking.com/api/folio_background/update/"+ str(folio_number) +"/"+ str(track_id) +"/"+ str(sii_date) +"?api_token=AtWYamNvDOfgDOEY6UbXgvGqDiRPR7QOt9Si1hbeMmat4g2Qfxzg7LlT5yzNz5LOozQbcA9uibaSTu4t"
                            response_4 = requests.get(url4)
                    
    def send_to_sii2(self, machine_id):

        if machine_id == 1:
            branch_office_ids = (1, 11)
        elif machine_id == 2:
            branch_office_ids = (11, 23)
        elif machine_id == 3:
            branch_office_ids = (23, 35)
        elif machine_id == 4:
            branch_office_ids = (35, 46)
        elif machine_id == 5:
            branch_office_ids = (46, 58)
        elif machine_id == 6:
            branch_office_ids = (58, 70)
        elif machine_id == 7:
            branch_office_ids = (70, 82)
        elif machine_id == 8:
            branch_office_ids = (82, 94)
        elif machine_id == 9:
            branch_office_ids = (94, 106)
        elif machine_id == 10:
            branch_office_ids = (106, 118)
        elif machine_id == 11:
            branch_office_ids = (118, 130)

        data = self.db.query(CurrentDteBackgroundModel).filter(
                CurrentDteBackgroundModel.branch_office_id >= branch_office_ids[0],
                CurrentDteBackgroundModel.branch_office_id < branch_office_ids[1]
            ).all()

        dte_settings = DteSettingClass(self.db).get()

        folio_quantity_to_send = dte_settings.folio_quantity_to_send

        folio_quantity_sent = dte_settings.folio_quantity_sent

        folio_quantity_limit = dte_settings.folio_quantity_limit

        if int(folio_quantity_to_send)- int(folio_quantity_sent) < int(folio_quantity_limit):
            for item in data:
                date = HelperClass().split(str(item.added_date), " ")

                url = "https://apigateway.cl/api/v1/libredte/dte/documentos/generar?normalizar=1&formato=json&enviar_sii=0&gzip=0&retry=1&"

                payload = json.dumps({
                "auth": {
                    "cert": {
                    "cert-data": "-----BEGIN CERTIFICATE-----\nMIIGjjCCBXagAwIBAgIDAR4jMA0GCSqGSIb3DQEBCwUAMIGmMQswCQYDVQQGEwJD\nTDEYMBYGA1UEChMPQWNlcHRhLmNvbSBTLkEuMUgwRgYDVQQDEz9BY2VwdGEuY29t\nIEF1dG9yaWRhZCBDZXJ0aWZpY2Fkb3JhIENsYXNlIDMgUGVyc29uYSBOYXR1cmFs\nIC0gRzQxHjAcBgkqhkiG9w0BCQEWD2luZm9AYWNlcHRhLmNvbTETMBEGA1UEBRMK\nOTY5MTkwNTAtODAeFw0yMTA3MDgyMzQwMjZaFw0yNDA3MDgyMzQwMjZaMIGXMQsw\nCQYDVQQGEwJDTDEYMBYGA1UEDBMPUEVSU09OQSBOQVRVUkFMMSswKQYDVQQDEyJN\nQVJDRUxPIEFMRUpBTkRSTyBJTlpVTlpBIEdPTlpBTEVaMSwwKgYJKoZIhvcNAQkB\nFh1DUklTVElBTklOWlVOWkFASklTUEFSS0lORy5DTDETMBEGA1UEBRMKMTAwMzM3\nNDEtSzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK/zoDtqd7+qB7aX\njS/kiBnLOf62orrMMdL3G22l0NJBziWVv/DezIgoFONUEF2XNXBWNAKTbLABvGIZ\nNFLyE4QuevdLd5AXuOt0q4+Y2msZemrP3zIkuT1dkNo/djj5gmFY3hC1i9DEj2ZQ\nF3kwcN9rrhQrzg3I0ixrRfdozMIypvCY4pWoJOvaNc8Z1a2Brq09QXQ3zUB3jXW7\nezxQlOCqv6G37UB9FzInnwAmicz5/92YtvFAXXJd4dtuaoPQt7Hn8XzhP8wmtj9j\nE9uHUbzK4CmQm4bYb1hmceg4crTHybTLUHngSlfI7QbDsLroaUlNgq8Kte8qDNxg\nqAhLkW0CAwEAAaOCAtAwggLMMB8GA1UdIwQYMBaAFKr9vcXpN032mU1XjsFxGvnr\nwwbjMB0GA1UdDgQWBBQYpMku0lGJKNQdxadkxl0mirm7uTALBgNVHQ8EBAMCBPAw\nHQYDVR0lBBYwFAYIKwYBBQUHAwIGCCsGAQUFBwMEMBEGCWCGSAGG+EIBAQQEAwIF\noDCB+gYDVR0gBIHyMIHvMIHsBggrBgEEAbVrAjCB3zAxBggrBgEFBQcCARYlaHR0\ncHM6Ly9hY2c0LmFjZXB0YS5jb20vQ1BTLUFjZXB0YWNvbTCBqQYIKwYBBQUHAgIw\ngZwwFhYPQWNlcHRhLmNvbSBTLkEuMAMCAQIagYFFbCB0aXR1bGFyIGhhIHNpZG8g\ndmFsaWRhZG8gZW4gZm9ybWEgcHJlc2VuY2lhbCwgcXVlZGFuZG8gaGFiaWxpdGFk\nbyBlbCBDZXJ0aWZpY2FkbyBwYXJhIHVzbyB0cmlidXRhcmlvLCBwYWdvcywgY29t\nZXJjaW8geSBvdHJvcy4wWgYDVR0SBFMwUaAYBggrBgEEAcEBAqAMFgo5NjkxOTA1\nMC04oCQGCCsGAQUFBwgDoBgwFgwKOTY5MTkwNTAtOAYIKwYBBAHBAQKBD2luZm9A\nYWNlcHRhLmNvbTBoBgNVHREEYTBfoBgGCCsGAQQBwQEBoAwWCjEwMDMzNzQxLUug\nJAYIKwYBBQUHCAOgGDAWDAoxMDAzMzc0MS1LBggrBgEEAcEBAoEdQ1JJU1RJQU5J\nTlpVTlpBQEpJU1BBUktJTkcuQ0wwRwYIKwYBBQUHAQEEOzA5MDcGCCsGAQUFBzAB\nhitodHRwczovL2FjZzQuYWNlcHRhLmNvbS9hY2c0L29jc3AvQ2xhc2UzLUc0MD8G\nA1UdHwQ4MDYwNKAyoDCGLmh0dHBzOi8vYWNnNC5hY2VwdGEuY29tL2FjZzQvY3Js\nL0NsYXNlMy1HNC5jcmwwDQYJKoZIhvcNAQELBQADggEBAAyvyBRFLpuF947AuBDm\nllTVh2Txrn2TK8bCl0iljnaCOdG3idmE5x9Ta7anzV0fL+ujQrUsSd7fa1n4PN9a\nn5rBmC/HR1DhBm4WIoVbVy3oz1GT2bmnfLOBqNKMvFNX0MJoOwYIkPxUcwRZXoPe\n6qe4tp4LAQiIUSxIbtVflXrctqX9m8PYf5wNA8gkiKK4qp8h+d+ZySAEHVFlHWb8\nY6TznjIwY05T46ATEyOVagDSijwW1Nj8m/8eJTF0vDKIzW6Uaa7YIPzVnkV0IHyE\nTyRne1CdJvynaEgs/BX84I1ovtsH2iEDX83xmKxtrdtPgO+Qin0kqHEu1EaEj9Qt\n6L0=\n-----END CERTIFICATE-----",
                    "pkey-data": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCv86A7ane/qge2\nl40v5IgZyzn+tqK6zDHS9xttpdDSQc4llb/w3syIKBTjVBBdlzVwVjQCk2ywAbxi\nGTRS8hOELnr3S3eQF7jrdKuPmNprGXpqz98yJLk9XZDaP3Y4+YJhWN4QtYvQxI9m\nUBd5MHDfa64UK84NyNIsa0X3aMzCMqbwmOKVqCTr2jXPGdWtga6tPUF0N81Ad411\nu3s8UJTgqr+ht+1AfRcyJ58AJonM+f/dmLbxQF1yXeHbbmqD0Lex5/F84T/MJrY/\nYxPbh1G8yuApkJuG2G9YZnHoOHK0x8m0y1B54EpXyO0Gw7C66GlJTYKvCrXvKgzc\nYKgIS5FtAgMBAAECggEBAJpWKwCzHSMD9AwX14JhBXkKqG5iqU8M+c9Bbc+6GPe1\nPSv+tQSFigcMkXXuMQTHM9q74pc31ah1fVbXIOx45uGVG8t7aP79r/jot+wXec9j\n49t5RyBm0g2f2wV1kS/cvJ7DItapSGDxaY+nRU/KS9fOTj3nRrEUrDbGSfMA/EqC\nRQT8BaHNDE9HwxsPOG66CCj9Bk40lZJD1XbWTey0NdhzcFDJya9gWvNQeKnXMo20\n9dltDvHhob2ULnbyUV3CNPsNFw/vCvqrb839ZUrBCh+IqCMrU/nrLuqmCpBIG+2/\naiNHgE7pIhfF/QpCbDwlbIH0HxQUTdPnJvAmmwZWGIkCgYEA/xF0WM4pQCRQF+Og\nCNdKjWkF/ZXS/tnpjxr2DmvMKwZX2nXMBHC7aHpfUCzj/Td69uK+AG4LnRkP1L3U\nyV0kXbMGUFcofVhYTDnPPNdlNyL5n2LKEmnYAYaJyYitEGoJN2hwplDMGH8kSKBH\nuymYN5ry5FfQfJGh17cjb/vP1s8CgYEAsJguDDB0uNC/oCEi1tSDG4RopV8tk/PH\nbtK1Fk0Qu7NliHr+PKb9w69wiw8BZ7dDU+igqJrywXl+Tnm8CvpbOAL8qQZqMzXM\nGvGBelWSq2HzxrIURD4X1yqzPvRKCTEbAPn4cgnmUBIpOtkdDJjrwuMD8dIT6J4y\nqmlpYZEWYwMCgYAEw4awwejzUbpNN+sdPygdTADYo5u1Nsyt54sA6fJ+OzgY1Gpj\nCtf1M5PkI3J+oDKjuchiqat926H4DzOSLzMmrNlJVtdiv+umQM4mDL/PL9AJsgak\nIWXvYVvhb7QLwm85obG46XlmW7mJwbSVQkmdgD9ZFGrIaM/k/36h8MoI8QKBgD8R\nChjmUTkTq+vXCacpW+0+21R76j4VaJrmey+MtDYkelVEf3lPtf7lr86pvDm7FDtq\nL74nIB0Cc545EXPmNx+IyYzfspu5UbwplbEH0IqOP84tGNnKRx9bq4oHGk2wENHH\nc/feGzdrVPgkQ6CVGFWQV39MJDoGDVgYrz7d3t3bAoGBAK+UnIFrRJ5UMsIM5Ao2\nryKtwPemdHypIVK3WOV1yRpa5aBqemrTQkijbLx8lVxoeID8Lw4zHybK6V9mAHsf\nRhfHsmBz3f4mYoKVoyVDelxpx+IGkGibvzNQB5BFWuu8kZeDPkhcPbk4pHFUf/jm\nCvLdtcSmumV5hxnVdtwjdlQD\n-----END PRIVATE KEY-----"
                    }
                },
                "dte": {
                    "Encabezado": {
                    "IdDoc": {
                        "TipoDTE": 39,
                        "Folio": item.folio,
                        "FchEmis": str(date[0])
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
                        "GiroRecep": "Particular",
                        "DirRecep": "Santiago",
                        "CmnaRecep": "Estacion Central"
                    }
                    },
                    "Detalle": {
                    "NmbItem": "Venta",
                    "QtyItem": 1,
                    "PrcItem": item.amount
                    }
                },
                "resolucion": {
                    "fecha": "2014-06-17",
                    "numero": 57
                },
                "caf": str(item.caf),
                })
                headers = {
                'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZDU0ZDU3Y2MwYzQ0MGQxMzBhMTAyZGUxMzY1NmMxMTYwMDdkZWU0MDk0NTFhNDNkN2NmYmI4MzEwY2E1ZDZlMTJhOWE5YjhjZmNiMjFhNzEiLCJpYXQiOjE3MTMyOTkxNzQsIm5iZiI6MTcxMzI5OTE3NCwiZXhwIjo0ODY4OTcyNzc0LCJzdWIiOiI1NzYiLCJzY29wZXMiOltdfQ.raiFUdWy9tnClakm5uCoPJR8x7YMwHSSzdUSO5LcgJeUwebfPAIh9BnmxIcCN6rOp7DU19qi3kHNNrOmuxOVwxj9ysmoG_W0jBwdEffnt4XLtpEMLp3OtM848gwGflgx6Y3GFksPJeg2tdinntPPSHfxvPPCATUV52bPrQ04y9dTgpbTSyR5rAnSERr1OawLBP9cMXFMHv_CCVAUC614cvKNq51e2XK7U1n4FhQ3qTwLORfv1yzfENGrhFKcdciWrRi47DCEwH5C7zKk7hTqPj5YBxwX-NIGZJgDjJDFKixXlgR1iqigchfo-C8z5xnNgzybkva9X1-kIJt5EFVqLDXxxl9gAY_6k7Sxke6xhvImjQgsLg39oMGBiYp61K6MXvwhC1AZgTxiD3iPLhhlEJouA9zOnChFo5vdnIPwl0wyX0EgK27SCQqZIYujNvLnxNUCikF3QZ_kJfyAdzfiWhNC2J25Q10xxBcFkhtG9aw5j8pwUQS84oOr6BNC8ca54S-wZJIse758BDEnk3-WMlpuYPkmq8kRK3eeCyt-B06zUPr8BgnQP16c4m6DubEEhjrL7D3cCIgmwFG68BKt0G4iv5kRl5nilzhcr424fxva_UORfWk-xXGMd9bjFT3Ak77AIcZMDrDOIGj7VPE6IPoUWYHBw4PB6Co61L6QA_Y',
                'Content-Type': 'application/json',
                'Cookie': '0chW9sKq57wqKBvjuHb6qbBG2RQgUCymhec2t7wz=eyJpdiI6IjVQdEVDd2E2OThLcHlyU2Rrckp5K3c9PSIsInZhbHVlIjoiZUVCS0szOXVjcGpXdnBtQURGMTNQamhOcmJGSXV5U1cvaTZ0TGFPMU9tcFhjT0FZZ25xYUlSRHUrRnNhTy9lMEdCbFJhc0JUWEcrZDBieTllOVFCaGQ2K1YxbklZQ2tFVC9TbmhJZmF3S2RnaGl0ei9IQUptNk8yaWNCNm5TSTI2dzJ1UkJvZS8wcG5PakduK3pGeUwwbGtERm8xRTdnMkpUVDRUUUU4YVQ0a2FmanJkelFoNVRyNFZMTVRRYTlPV3VUclZwbWNRU0x2VW1nMm13bFV4VlJ3aHVWRXdXa24vcVFRVmZwNk41bDkzQklNeVl5b1cySzRNS0Z1VHNqSDA4SVh4UmY3Q0RkaUpCbVpjKzRJTjFCekdrTWprNXdPUHlVVi9pZzhRSGc0ZkxjSThNK3VFOWgwT0Q3QllFYUNJZ0c1czFRdXY1Wkp3ZlNhc05nb204SjRhaXVMTlBqUkdSZ2wxcGNPMm1ZVEUxaEFPNWloYzgrbGdvWTFxaHEvIiwibWFjIjoiYzIyYzNmMjNlNzdmYTJjYmIwMjJkM2I0YTE4MzU5NTU5YTY4MWEyZDAwNjFiOGUyZDgxYzk0MTkzM2IwY2M2NyIsInRhZyI6IiJ9; XSRF-TOKEN=eyJpdiI6Ik9hcnQwejI5UzdDUE82cFpLc3RJZ0E9PSIsInZhbHVlIjoid2hsdWJNZWFISHRXdGQxcWtnNnZVNnJzNjFPZEkwWDZOaUZuZGdCMjRodTcrOWFFbkZmR0FiWnBJN3A3RzZvYmNDRlZVQ1dEN3M2S1BrU01VMUdTNmNCV2NuVjhDUlBvN1RCY2pxT0RWY1gyNExvZEx1T0dJWUZtSGJITG5tVzIiLCJtYWMiOiI1NThiZDBkN2JkZWMyOWJkYzIzNDI5NzFlMTU4YmE0YWViYmUwOTRiZjhiNDYwZmE2NmM4MjEzNTdkNDU4NWJkIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6ImtvWURKL05SaFZmcTN6azBlMGROOWc9PSIsInZhbHVlIjoiaWlyZnBOOWJjZjd3RW05WStzYUI4TTk0ODVEdkFDNG5LUXo1dnMzYmJvb1AwK0tZaElhU2xFZ2JDUWJpTXN5VG5samF2UWV4dWRHKytjVC82YUVZRVhHQ2ZLQm1LRlFNZ25iSWVCMG56N1lYNlBrY0pNQ29ORzZhckNJUHdERjMiLCJtYWMiOiJkYzI5ZjA2MDU1MTMxM2U4OGVjNTkwMWRmOTA3MmRhODM1Mzk2MWY4NjIxM2M0ODFmYWJkZWU1NTg0MTdjYjkwIiwidGFnIjoiIn0%3D'
                }

                response = requests.request("POST", url, headers=headers, data=payload)

                rate_limit_limit = response.headers.get('X-RateLimit-Remaining')

                if int(folio_quantity_to_send) - int(rate_limit_limit) < int(folio_quantity_limit):

                    DteSettingClass(self.db).update(rate_limit_limit)
                
                    response_decoded = json.loads(response.text)

                    xml = response_decoded.get("xml")

                    url = "https://apigateway.cl/api/v1/libredte/dte/envios/enviar?certificacion=0&gzip=0&retry=1"

                    payload = json.dumps({
                    "auth": {
                        "cert": {
                        "cert-data": "-----BEGIN CERTIFICATE-----\nMIIGjjCCBXagAwIBAgIDAR4jMA0GCSqGSIb3DQEBCwUAMIGmMQswCQYDVQQGEwJD\nTDEYMBYGA1UEChMPQWNlcHRhLmNvbSBTLkEuMUgwRgYDVQQDEz9BY2VwdGEuY29t\nIEF1dG9yaWRhZCBDZXJ0aWZpY2Fkb3JhIENsYXNlIDMgUGVyc29uYSBOYXR1cmFs\nIC0gRzQxHjAcBgkqhkiG9w0BCQEWD2luZm9AYWNlcHRhLmNvbTETMBEGA1UEBRMK\nOTY5MTkwNTAtODAeFw0yMTA3MDgyMzQwMjZaFw0yNDA3MDgyMzQwMjZaMIGXMQsw\nCQYDVQQGEwJDTDEYMBYGA1UEDBMPUEVSU09OQSBOQVRVUkFMMSswKQYDVQQDEyJN\nQVJDRUxPIEFMRUpBTkRSTyBJTlpVTlpBIEdPTlpBTEVaMSwwKgYJKoZIhvcNAQkB\nFh1DUklTVElBTklOWlVOWkFASklTUEFSS0lORy5DTDETMBEGA1UEBRMKMTAwMzM3\nNDEtSzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK/zoDtqd7+qB7aX\njS/kiBnLOf62orrMMdL3G22l0NJBziWVv/DezIgoFONUEF2XNXBWNAKTbLABvGIZ\nNFLyE4QuevdLd5AXuOt0q4+Y2msZemrP3zIkuT1dkNo/djj5gmFY3hC1i9DEj2ZQ\nF3kwcN9rrhQrzg3I0ixrRfdozMIypvCY4pWoJOvaNc8Z1a2Brq09QXQ3zUB3jXW7\nezxQlOCqv6G37UB9FzInnwAmicz5/92YtvFAXXJd4dtuaoPQt7Hn8XzhP8wmtj9j\nE9uHUbzK4CmQm4bYb1hmceg4crTHybTLUHngSlfI7QbDsLroaUlNgq8Kte8qDNxg\nqAhLkW0CAwEAAaOCAtAwggLMMB8GA1UdIwQYMBaAFKr9vcXpN032mU1XjsFxGvnr\nwwbjMB0GA1UdDgQWBBQYpMku0lGJKNQdxadkxl0mirm7uTALBgNVHQ8EBAMCBPAw\nHQYDVR0lBBYwFAYIKwYBBQUHAwIGCCsGAQUFBwMEMBEGCWCGSAGG+EIBAQQEAwIF\noDCB+gYDVR0gBIHyMIHvMIHsBggrBgEEAbVrAjCB3zAxBggrBgEFBQcCARYlaHR0\ncHM6Ly9hY2c0LmFjZXB0YS5jb20vQ1BTLUFjZXB0YWNvbTCBqQYIKwYBBQUHAgIw\ngZwwFhYPQWNlcHRhLmNvbSBTLkEuMAMCAQIagYFFbCB0aXR1bGFyIGhhIHNpZG8g\ndmFsaWRhZG8gZW4gZm9ybWEgcHJlc2VuY2lhbCwgcXVlZGFuZG8gaGFiaWxpdGFk\nbyBlbCBDZXJ0aWZpY2FkbyBwYXJhIHVzbyB0cmlidXRhcmlvLCBwYWdvcywgY29t\nZXJjaW8geSBvdHJvcy4wWgYDVR0SBFMwUaAYBggrBgEEAcEBAqAMFgo5NjkxOTA1\nMC04oCQGCCsGAQUFBwgDoBgwFgwKOTY5MTkwNTAtOAYIKwYBBAHBAQKBD2luZm9A\nYWNlcHRhLmNvbTBoBgNVHREEYTBfoBgGCCsGAQQBwQEBoAwWCjEwMDMzNzQxLUug\nJAYIKwYBBQUHCAOgGDAWDAoxMDAzMzc0MS1LBggrBgEEAcEBAoEdQ1JJU1RJQU5J\nTlpVTlpBQEpJU1BBUktJTkcuQ0wwRwYIKwYBBQUHAQEEOzA5MDcGCCsGAQUFBzAB\nhitodHRwczovL2FjZzQuYWNlcHRhLmNvbS9hY2c0L29jc3AvQ2xhc2UzLUc0MD8G\nA1UdHwQ4MDYwNKAyoDCGLmh0dHBzOi8vYWNnNC5hY2VwdGEuY29tL2FjZzQvY3Js\nL0NsYXNlMy1HNC5jcmwwDQYJKoZIhvcNAQELBQADggEBAAyvyBRFLpuF947AuBDm\nllTVh2Txrn2TK8bCl0iljnaCOdG3idmE5x9Ta7anzV0fL+ujQrUsSd7fa1n4PN9a\nn5rBmC/HR1DhBm4WIoVbVy3oz1GT2bmnfLOBqNKMvFNX0MJoOwYIkPxUcwRZXoPe\n6qe4tp4LAQiIUSxIbtVflXrctqX9m8PYf5wNA8gkiKK4qp8h+d+ZySAEHVFlHWb8\nY6TznjIwY05T46ATEyOVagDSijwW1Nj8m/8eJTF0vDKIzW6Uaa7YIPzVnkV0IHyE\nTyRne1CdJvynaEgs/BX84I1ovtsH2iEDX83xmKxtrdtPgO+Qin0kqHEu1EaEj9Qt\n6L0=\n-----END CERTIFICATE-----",
                        "pkey-data": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCv86A7ane/qge2\nl40v5IgZyzn+tqK6zDHS9xttpdDSQc4llb/w3syIKBTjVBBdlzVwVjQCk2ywAbxi\nGTRS8hOELnr3S3eQF7jrdKuPmNprGXpqz98yJLk9XZDaP3Y4+YJhWN4QtYvQxI9m\nUBd5MHDfa64UK84NyNIsa0X3aMzCMqbwmOKVqCTr2jXPGdWtga6tPUF0N81Ad411\nu3s8UJTgqr+ht+1AfRcyJ58AJonM+f/dmLbxQF1yXeHbbmqD0Lex5/F84T/MJrY/\nYxPbh1G8yuApkJuG2G9YZnHoOHK0x8m0y1B54EpXyO0Gw7C66GlJTYKvCrXvKgzc\nYKgIS5FtAgMBAAECggEBAJpWKwCzHSMD9AwX14JhBXkKqG5iqU8M+c9Bbc+6GPe1\nPSv+tQSFigcMkXXuMQTHM9q74pc31ah1fVbXIOx45uGVG8t7aP79r/jot+wXec9j\n49t5RyBm0g2f2wV1kS/cvJ7DItapSGDxaY+nRU/KS9fOTj3nRrEUrDbGSfMA/EqC\nRQT8BaHNDE9HwxsPOG66CCj9Bk40lZJD1XbWTey0NdhzcFDJya9gWvNQeKnXMo20\n9dltDvHhob2ULnbyUV3CNPsNFw/vCvqrb839ZUrBCh+IqCMrU/nrLuqmCpBIG+2/\naiNHgE7pIhfF/QpCbDwlbIH0HxQUTdPnJvAmmwZWGIkCgYEA/xF0WM4pQCRQF+Og\nCNdKjWkF/ZXS/tnpjxr2DmvMKwZX2nXMBHC7aHpfUCzj/Td69uK+AG4LnRkP1L3U\nyV0kXbMGUFcofVhYTDnPPNdlNyL5n2LKEmnYAYaJyYitEGoJN2hwplDMGH8kSKBH\nuymYN5ry5FfQfJGh17cjb/vP1s8CgYEAsJguDDB0uNC/oCEi1tSDG4RopV8tk/PH\nbtK1Fk0Qu7NliHr+PKb9w69wiw8BZ7dDU+igqJrywXl+Tnm8CvpbOAL8qQZqMzXM\nGvGBelWSq2HzxrIURD4X1yqzPvRKCTEbAPn4cgnmUBIpOtkdDJjrwuMD8dIT6J4y\nqmlpYZEWYwMCgYAEw4awwejzUbpNN+sdPygdTADYo5u1Nsyt54sA6fJ+OzgY1Gpj\nCtf1M5PkI3J+oDKjuchiqat926H4DzOSLzMmrNlJVtdiv+umQM4mDL/PL9AJsgak\nIWXvYVvhb7QLwm85obG46XlmW7mJwbSVQkmdgD9ZFGrIaM/k/36h8MoI8QKBgD8R\nChjmUTkTq+vXCacpW+0+21R76j4VaJrmey+MtDYkelVEf3lPtf7lr86pvDm7FDtq\nL74nIB0Cc545EXPmNx+IyYzfspu5UbwplbEH0IqOP84tGNnKRx9bq4oHGk2wENHH\nc/feGzdrVPgkQ6CVGFWQV39MJDoGDVgYrz7d3t3bAoGBAK+UnIFrRJ5UMsIM5Ao2\nryKtwPemdHypIVK3WOV1yRpa5aBqemrTQkijbLx8lVxoeID8Lw4zHybK6V9mAHsf\nRhfHsmBz3f4mYoKVoyVDelxpx+IGkGibvzNQB5BFWuu8kZeDPkhcPbk4pHFUf/jm\nCvLdtcSmumV5hxnVdtwjdlQD\n-----END PRIVATE KEY-----"
                        }
                    },
                    "emisor": "76063822-6",
                    "xml": str(xml['sii'])
                    })
                    headers = {
                    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZDU0ZDU3Y2MwYzQ0MGQxMzBhMTAyZGUxMzY1NmMxMTYwMDdkZWU0MDk0NTFhNDNkN2NmYmI4MzEwY2E1ZDZlMTJhOWE5YjhjZmNiMjFhNzEiLCJpYXQiOjE3MTMyOTkxNzQsIm5iZiI6MTcxMzI5OTE3NCwiZXhwIjo0ODY4OTcyNzc0LCJzdWIiOiI1NzYiLCJzY29wZXMiOltdfQ.raiFUdWy9tnClakm5uCoPJR8x7YMwHSSzdUSO5LcgJeUwebfPAIh9BnmxIcCN6rOp7DU19qi3kHNNrOmuxOVwxj9ysmoG_W0jBwdEffnt4XLtpEMLp3OtM848gwGflgx6Y3GFksPJeg2tdinntPPSHfxvPPCATUV52bPrQ04y9dTgpbTSyR5rAnSERr1OawLBP9cMXFMHv_CCVAUC614cvKNq51e2XK7U1n4FhQ3qTwLORfv1yzfENGrhFKcdciWrRi47DCEwH5C7zKk7hTqPj5YBxwX-NIGZJgDjJDFKixXlgR1iqigchfo-C8z5xnNgzybkva9X1-kIJt5EFVqLDXxxl9gAY_6k7Sxke6xhvImjQgsLg39oMGBiYp61K6MXvwhC1AZgTxiD3iPLhhlEJouA9zOnChFo5vdnIPwl0wyX0EgK27SCQqZIYujNvLnxNUCikF3QZ_kJfyAdzfiWhNC2J25Q10xxBcFkhtG9aw5j8pwUQS84oOr6BNC8ca54S-wZJIse758BDEnk3-WMlpuYPkmq8kRK3eeCyt-B06zUPr8BgnQP16c4m6DubEEhjrL7D3cCIgmwFG68BKt0G4iv5kRl5nilzhcr424fxva_UORfWk-xXGMd9bjFT3Ak77AIcZMDrDOIGj7VPE6IPoUWYHBw4PB6Co61L6QA_Y',
                    'Content-Type': 'application/json'
                    }

                    response = requests.request("POST", url, headers=headers, data=payload)

                    DteSettingClass(self.db).update(rate_limit_limit)

                    response_decoded = json.loads(response.text)

                    track_id = response_decoded.get("track_id")

                    sii_date = response_decoded.get("fecha_recepcion")

                    status = response_decoded.get("estado")

                    inputs = {}

                    inputs['track_id'] = track_id

                    inputs['sii_date'] = sii_date

                    DteBackgroundClass(self.db).update(item.folio, inputs)
       
                    if status == 'REC':
                        CurrentDteBackgroundClass(self.db).delete(item.folio)
                else:
                    current_date = datetime.now()
                    current_formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

                    DteSettingClass(self.db).last_folio_sent(current_formatted_date)

                    DteSettingClass(self.db).status(0)
        else:
            exit()

        return 1
