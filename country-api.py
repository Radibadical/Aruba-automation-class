import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://restcountries.eu/rest/v2/all'
response = request.get(url)
print(response)
print(response.status_code)

countries = response.text
data_python=json.loads(countries)
country = input("enter country name, Capitalize the first letter:")

for i in range (len(data_python)):
    if data_python[i]["name"] == country:
        print("it is the number " +str(i)+ " in the countries list")
        print("The population is " + str(data_python[i]["population"]))
        break
    else:
        i+=1
    if i == len(data_python):
        print("no this country")