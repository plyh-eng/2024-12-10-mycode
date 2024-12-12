#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Accessing Open APIs with Python"""

# standard library
import json

# 3rd party library
import requests

# Define URL as a global constant (this will not change)
NET = 'http://api.citybik.es/v2/networks'

def main():
    """making API requests"""
    
    # Call the web service
    resp = requests.get(NET)  # sends an HTTP GET
    
    # strip JSON data off response and convert
    # to python data types
    data = resp.json()
            
    # display our Pythonic data
    print("\n\nConverted Python data")
    print(data)
    
    print('\n\nPeople in Space: ', data.get('number'))
    
    netwk = data.get('networks') # 
    print(netwk) # this is the list of dict

    # for-loop across astros
    # display names of those in space
    for ntw in netwk:
        print(f"ntw['id'] is from:", (ntw['location'])['city'])

if __name__ == '__main__':
    main()

