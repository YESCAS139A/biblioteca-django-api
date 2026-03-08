import requests

# Configuración
TOKEN_URL = 'http://127.0.0.1:8080/o/token/'
API_URL = 'http://127.0.0.1:8080/api/libros/'

CLIENT_ID = '3H96REq4KQV9mPWlOqP8ly1emnUOAMgw6kXvZpD2'
CLIENT_SECRET = 'VCwHxKKo12IzRFqWy4J80sC0YPcxbwkYA2jTu8odFnhuWSaNKpunqSP8FEmocyibaH59mhPNH89WK5g5iyKep4HgMX0192BTW2Tisv3Gq1dKR4J2ZJt1Wte8L31XZIcU'
USERNAME = 'admin'
PASSWORD = 'admin123'

print("=== Obteniendo Token OAuth 2.0 ===")

# Obtener token
response = requests.post(TOKEN_URL, data={
    'grant_type': 'password',
    'username': USERNAME,
    'password': PASSWORD,
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'scope': 'read write'
})

if response.status_code == 200:
    token_data = response.json()
    access_token = token_data['access_token']
    
    print(f"✅ Token obtenido: {access_token[:50]}...")
    
    # Usar token para acceder a API
    headers = {'Authorization': f'Bearer {access_token}'}
    api_response = requests.get(API_URL, headers=headers)
    
    print(f"Status Code: {api_response.status_code}")
    print(f"Data: {api_response.json()}")
else:
    print(f"❌ Error: {response.status_code}")
    print(response.json())