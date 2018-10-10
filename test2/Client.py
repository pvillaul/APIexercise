import requests
import json

result = requests.get('http://127.0.0.1:5000/sayhello')
print(result.text)

result2 = requests.get('http://127.0.0.1:5000/calculate/9')
print(result2.text)

result3 = requests.get('http://127.0.0.1:5000/calculate/?num=3')
print(result3.text)

result4 = requests.get('http://127.0.0.1:5000/concat/?cad1=Alberto&cad2=Fernandez')
print(result4.text)

result5 = requests.get('http://127.0.0.1:5000/users/1')
print(result5.text)