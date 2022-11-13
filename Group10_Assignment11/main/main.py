'''
Created on Nov 3, 2022

@author: marquibm
'''
import json
import requests
response = requests.get('https://api.ers.usda.gov/data/arms/state?api_key=CRt5lRKn8IPXTH1QzYhcNIFFjxeBmrZQ79jOFp6G')
json_string = response.content
    
parsed_json = json.loads(json_string) # Now we have a python dictionary
    
    #print(parsed_json)
    #print(parsed_json['data'][0]['description'])
    #print(parsed_json['data'][0]['directionsInfo'])
    
#total = int(parsed_json['total'])        # The number of parks that were returned
    
for states in parsed_json['data']:    #Get the value associated with the parsed_json{'data']
    print (states)

print(('ID:')+(parsed_json['data'][3]['id']))
print(('Code:')+(parsed_json['data'][3]['code']))
print(('Name:')+(parsed_json['data'][3]['name']))
print(parsed_json['data'][3])
#for ID in parsed_json['id']:
    #print(ID('id'))
    
