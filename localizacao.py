import requests

# Faz a requisição à API do ipinfo
response = requests.get("https://ipinfo.io/")
data = response.json()

# Extrai a latitude e longitude do campo 'loc'
latitude, longitude = data['loc'].split(',')

print(f"Latitude: {latitude}, Longitude: {longitude}")
