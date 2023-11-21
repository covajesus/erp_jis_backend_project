# Dentro de la función scrape() en tu servidor FastAPI

from fastapi import APIRouter, Depends
import httpx
from bs4 import BeautifulSoup
import requests


provisional_indicators = APIRouter(
    prefix="/provisional_indicators",
    tags=["Provisional_Indicators"]
)

@provisional_indicators.get("/scrape")
async def scrape():
    try:
        url = 'https://www.previred.com/indicadores-previsionales/'

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        td_elements = soup.find_all('td')

        # Crea una lista vacía para almacenar los datos
        data = []

        for td in td_elements:
            # Agrega el texto del elemento 'td' a la lista 'data'
            data.append(td.text)

        # Devuelve la lista 'data'
        return data
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"error": "Error en el servidor"}

