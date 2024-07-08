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

async def vredprivichki(data:dict, access_token)->None:
    url_vr = 'http://127.0.0.1:8000/api/vredprivichki/'
    
    headers={'Authorization': f'Bearer {access_token["access"]}',
        'accept': 'application/json'
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url_vr, headers=headers, data=data) as response:
            return await response.json()

async def cel_list(access_token)->None:
    url_vr = 'http://127.0.0.1:8000/api/cel/'
    
    headers={'Authorization': f'Bearer {access_token["access"]}',
        'accept': 'application/json'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url_vr, headers=headers) as response:
            return await response.json()

async def create_cel(data:dict, access_token)->None:
    url_cel = 'http://127.0.0.1:8000/api/cel/'
    
    headers={'Authorization': f'Bearer {access_token["access"]}',
        'accept': 'application/json'
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url_cel, headers=headers, data=data) as response:
            return await response.json()

async def create_comment(data:dict, access_token)->None:
    url_comment = 'http://127.0.0.1:8000/api/comment/'
    
    headers={'Authorization': f'Bearer {access_token["access"]}',
        'accept': 'application/json'
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url_comment, headers=headers, data=data) as response:
            return await response.json()