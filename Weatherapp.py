import requests
import json

# Global Variables used.
symbols = "',.<>\|`¬!£$%^&*()_-+={}]['@;:/?"


# This Function contains code from other sources to help decode the JSON data the API handed back:
# https://www.dataquest.io/blog/python-api-tutorial/
def jprint(obj):
    flag = False
    weather = ""
    weather_list = []
    # Create a formatted string of the Python JSON object. This line was sourced from the link above.
    text = json.dumps(obj, sort_keys=True, indent=4)
    # Creates a list from the string of JSON text.
    text_list = text.split()
    # Looping through the list of data returned by the api and removing all unnecessary data.
    for i in text_list:
        if i == '"weather":':
            flag = True
        elif i == '"icon":':
            flag = False
        else:
            if flag == True:
                # Cleaning up the output of the broader clearance of unnecessary data.
                if "[]{};:," in i:
                    continue
                else:
                    weather_list.append(i)
    weather_list.remove("[")
    weather_list.remove("{")
    weather_list.remove('"description":')
    for i in weather_list:
        weather = str(weather) + " " + str(i)

    print(weather)


def country():
    country = input("Which country's weather are you interested in?")
    # Validating for symbols to try to avoid any bad data being sent further.
    while symbols in country:
        country = input("The previous country is invalid.")
    link = "http://api.openweathermap.org/data/2.5/weather?q=" + country + "&appid=61f9fc39e3ee4a14eab7ef212ae91500"
    response = requests.get(link)
    # Using the status codes to validate the input.
    while response.status_code != 200 and response.status_code != 301:
        country = input("The previous country is invalid.")
        link = "http://api.openweathermap.org/data/2.5/weather?q=" + country + "&appid=61f9fc39e3ee4a14eab7ef212ae91500"
        response = requests.get(link)
    jprint(response.json())



#Justas' modified version of functions.
def countryChatbot(stuff):
    if len(stuff) < 2:
        return "Too short city name"
    country = stuff #modified input
    # Validating for symbols to try to avoid any bad data being sent further.
    while symbols in country:
        return "Failed to find country, try again but without symbols." #modified error
    link = "http://api.openweathermap.org/data/2.5/weather?q=" + country + "&appid=61f9fc39e3ee4a14eab7ef212ae91500"
    response = requests.get(link)
    # Using the status codes to validate the input.
    while response.status_code != 200 and response.status_code != 301:
        return "The previous country is invalid." #modified
        link = "http://api.openweathermap.org/data/2.5/weather?q=" + country + "&appid=61f9fc39e3ee4a14eab7ef212ae91500"
        response = requests.get(link)
    return jprint2(response.json()) #modified jprint returning

def jprint2(obj):
    flag = False
    weather = ""
    weather_list = []
    # Create a formatted string of the Python JSON object. This line was sourced from the link above.
    text = json.dumps(obj, sort_keys=True, indent=4)
    # Creates a list from the string of JSON text.
    text_list = text.split()
    # Looping through the list of data returned by the api and removing all unnecessary data.
    for i in text_list:
        if i == '"weather":':
            flag = True
        elif i == '"icon":':
            flag = False
        else:
            if flag == True:
                # Cleaning up the output of the broader clearance of unnecessary data.
                if "[]{};:," in i:
                    continue
                else:
                    weather_list.append(i)
    weather_list.remove("[")
    weather_list.remove("{")
    weather_list.remove('"description":')
    for i in weather_list:
        weather = str(weather) + " " + str(i)

    return weather #modified to return


