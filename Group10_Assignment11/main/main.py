'''
Name: Aaron Paulson, Ben Marquis
email: Paulsoar@mail.uc.edu, marquibm@mail.uc.edu
Assignment: Group 10 Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: For this assignment we grabbed an API from the Department of Agriculture and parsed the data into a dictionary and printed our results
Citations:http://www.ers.usda.gov/developer/
Anything else that's relevant: 
'''
#Main.py
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
    
