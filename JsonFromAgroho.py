from urllib import request
import json
"""
this program gets the json file from agroho.com and prints the data
in the file named "AgrohoJson.html". it can be viewed using text
editor or web browser. it is an example of using JSON with Python.

"""
agroho_url = "http://api.agroho.com/islam/json/qa_discussed.php"
response = request.urlopen(agroho_url)
encoding = response.headers.get_content_charset()
jsonData = json.loads(response.read().decode(encoding))
# print(type(jsonData))
# print(jsonData)
with open("AgrohoJson.html", "w") as file:  # prints AgrohoJson.html in the same directory
    json.dump(jsonData, file)

"""for line in jsonData:
    print(line['qa_title'])"""
