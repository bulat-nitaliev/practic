import asyncio, aiohttp

async def register(data:dict)->None:
    url = 'http://127.0.0.1:8000/api/users/'
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            return await response.json()


async def login(data:dict)->None:
    url = 'http://127.0.0.1:8000/api/token/'
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            return await response.json()

async def islam(data:dict, access_token)->None:
    url = 'http://127.0.0.1:8000/api/islam/'
    
    headers={'Authorization': f'Bearer {access_token["access"]}',
        'accept': 'application/json'
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as response:
            return await response.json()