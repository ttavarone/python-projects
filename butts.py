import urllib.request
import json
term = "water"
contents = urllib.request.urlopen("http://api.urbandictionary.com/v0/define?term="+term).read()
initialJSON = json.loads(contents)
definitionsString = json.dumps(initialJSON, indent=4)
definitions = []
for x in definitions:
    first = definitions[0].split('{')
    defin = first[1]
    definitions.append(defin)
for x in definitions:
    print(x.count())
#https://www.w3schools.com/python/python_json.asp
