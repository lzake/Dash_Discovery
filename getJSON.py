import urllib.request
url = input("Enter JSON URL: ")
with urllib.request.urlopen(url) as response:
   html = response.read()
print(html)


### python has a module called json that is good for handling json data also
### here is an example using mapquest's api:

import json
import urllib.request
import pprint

#removed my api key
base_url = 'http://www.mapquestapi.com/traffic/v2/incidents?key=[enter key here]&boundingBox=39.95,-105.25,39.52,-104.71&filters=construction,incidents'
response = urllib.request.urlopen(base_url)
data = json.loads(response.read().decode())
pprint.pprint(data)
