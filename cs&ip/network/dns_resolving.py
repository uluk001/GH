import socket
import requests
import time

url = 'https://api.github.com/users/octocat'

start = time.time()
ip = socket.gethostbyname('api.instagram.com')
dns_time = time.time() - start

print(f"DNS резолвинг: {ip} за {dns_time*1000:.2f}ms")

start = time.time()
response = requests.get(url)
total_time = time.time() - start

print(f"Полный HTTP запрос: {total_time*1000:.2f}ms")
