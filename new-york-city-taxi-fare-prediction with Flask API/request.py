import requests
url = 'http://127.0.0.1:5000/predict'
r = requests.post(url,json={
    "distance(km)":[0.78,0.5,5],
    "passenger_count":[2,1,2]
})
print(r.json())