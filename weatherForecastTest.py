import requests
data = requests.get("https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")
data = data.json()
days = []
hrs = []
tempCheck = True
descCheck1 = False
descCheck2 = False
for i in data['list']:
    days.append(i['dt_txt'].split(" ")[0])
    hrs.append(i['dt_txt'].split(" ")[1].split(":")[0])
    if i["main"]["temp"] < i["main"]["temp_min"] or i["main"]["temp"] > i["main"]["temp_max"]:
        tempCheck = False
    if i['weather'][0]['id'] == 500:
        if i['weather'][0]['description'] == "light rain":
            descCheck1 = True
    if i['weather'][0]['id'] == 800:
        if i['weather'][0]['description'] == "clear sky":
            descCheck2 = True
            
    
isHrsInterval = True
for i in range(len(hrs)-1):
    if (int(hrs[i]) +1 != int(hrs[i+1])):
        if (int(hrs[i]) != 23 and int(hrs[i+1]) != 0):
            print(int(hrs[i]),int(hrs[i+1]))
            isHrsInterval = False
            break
        
    
if len(set(days)) >4:
    print("More than 4 days of data present")
elif len(set(days)) == 4:
    print("4 days of data present")
else:
    print("Does not contain 4 days of data")

if isHrsInterval:
    print("Data in hrs interval")
else:
    print("Data not in hrs interval")

if tempCheck:
    print("Temperature check pass")
else:
    print("Temperature check fail")

if descCheck1:
    print("Desc check for id 500 pass")
else:
    print("Desc check for id 500 fail")

if descCheck2:
    print("Desc check for id 800 pass")
else:
    print("Desc check for id 800 fail")
