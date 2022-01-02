from typing import Optional
import httpx

api_key: Optional[str] = None

async def get_report(city: str, state: Optional[str], country: str, units: str):
    q = f'{city}, {country}'
    key = 123
    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={key}&units={units}'

    async with httpx.AsyncClient as client:
        resp = await client.get(url)
        resp.raise_for_status()

    data = resp.json()
    forecast = data['main']
    return forecast