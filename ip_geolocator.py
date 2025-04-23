import requests

def geolocate_ip(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()
    print(data)