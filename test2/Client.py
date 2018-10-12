# Authors: Meyer Montagner, Pablo Villalba
# Programa que funciona como cliente al servidor. Usado como práctica del concepto de API.

import requests

""" Acceso a endpoint /sayhello/. 
Retorna un JSON con un saludo. """
result = requests.get('http://127.0.0.1:5000/sayhello')  # type: requests.Response
print(result.text)

""" Acceso a endpoint /calculate/<num>. 
Recibe un número en la ruta.
Retorna un JSON con el cuadrado del número. """
result2 = requests.get('http://127.0.0.1:5000/calculate/3.2')  # type: requests.Response
print(result2.text)

""" Acceso a endpoint /calculate/. 
Recibe un número como parámetro.
Retorna un JSON con el cuadrado del número. """
result3 = requests.get('http://127.0.0.1:5000/calculate/?num=3.45')  # type: requests.Response
print(result3.text)

""" Acceso a endpoint /concatenate/. 
Recibe dos cadenas de caracteres como parámetros.
Retorna un JSON con las dos cadenas concatenadas. """
result4 = requests.get('http://127.0.0.1:5000/concatenate/?string1=Alberto&string2=Fernandez') # type: requests.Response
print(result4.text)

""" Acceso a endpoint /users/<id>. 
Recibe un número ID en la ruta.
Retorna un JSON que contiene el nombre del usuario correspondiente al ID. """
result5 = requests.get('http://127.0.0.1:5000/users/1')  # type: requests.Response
print(result5.text)
