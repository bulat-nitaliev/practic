import aiohttp

class Http:
    url_http:str = 'http://practic:7000'

    async def get(self, url, headers:dict={}):
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=headers) as response:
                return await response.json()
            
    async def post(self, url:str, headers:dict, data:dict):
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, headers=headers, data=data) as response:
                return await response.json()
            
    async def delete(self, url:str, headers:dict):    
        async with aiohttp.ClientSession() as session:
            async with session.delete(url=url, headers=headers) as response:
                return  {'result': 'success'}
            
http = Http()


async def register(data:dict)->None:
    url = 'http://practic:7000/api/users/'
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            # return await response.json()
            content_type = response.headers.get('Content-Type')
            if content_type == 'application/json':
                data = await response.json()
                print(data)
            else:
                html_content = await response.text()
                # print(html_content)


async def login(data:dict)->None:
    url = 'http://practic:7000/api/token/'
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            return await response.json()

async def islam(data:dict, access_token)->None:
    url = http.url_http + '/api/islam/'
    print(url)
    
    headers={'Authorization': f'Bearer {access_token["access"]}',
        'accept': 'application/json'
    }
    return await http.post(url=url,headers=headers, data=data)

async def vredprivichki(data:dict, access_token)->None:
    url_vr = http.url_http + '/api/vredprivichki/'
    
    headers={'Authorization': f'Bearer {access_token["access"]}',
        'accept': 'application/json'
    }
    return await http.post(url_vr, headers, data)

async def cel_list(access_token)->None:
    url_vr = http.url_http + '/api/cel/'
    
    headers={'Authorization': f'Bearer {access_token["access"]}',
        'accept': 'application/json'
    }
    return await http.get(url_vr,headers)

async def create_cel(data:dict, access_token)->None:
    url_cel = http.url_http + '/api/cel/'
    
    headers={'Authorization': f'Bearer {access_token["access"]}',
        'accept': 'application/json'
    }
    return await http.post(url_cel, headers, data)

async def create_comment(data:dict, access_token)->None:
    url_comment = http.url_http + '/api/comment/'
    
    headers={'Authorization': f'Bearer {access_token["access"]}',
        'accept': 'application/json'
    }
    return await http.post(url_comment, headers, data)
        
async def destroy_cel(id,access_token)->None:
    url = http.url_http + f'/api/cel/{id}/'
    
    headers={'Authorization': f'Bearer {access_token["access"]}',
        'accept': 'application/json'
    }
    return await http.delete(url, headers)
