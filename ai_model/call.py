import httpx
import requests

async def MakeCall(people_count):
    async with httpx.AsyncClient() as client:
        try:
            url = f"http://localhost:5000/count"
            response = await client.post(url, json={"people_count": people_count})
            print(f"Server response: {response.status_code}, {response.text}")
        except httpx.RequestError as e:
            print(f"Request failed: {e}")

