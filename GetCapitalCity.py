# Program to get Capital city using Country name or code
# author : susmitha srinivasalu

import requests
nameUrl = "https://restcountries.eu/rest/v2/name/"
codeUrl = "https://restcountries.eu/rest/v2/alpha/"

print("You can find the Capital of a Country by giving Country Name or Code")
print('''         >.Press 0 for exit
         >.Press 1 to enter the Country Name
         >.Press 2 to Enter the Country Code''')
while True:
    print(" ")
    try:
        option_num = input("Enter the option :")
        if option_num == "1":
            name = input("Enter a Country name :")
            get_countryName = requests.get(nameUrl+name)
            jsonObj = get_countryName.json()
            for i in jsonObj:
                capitalCity = i['capital']
                countryName = i['name']
                print('The capital of the country {} is {}'.format(countryName, capitalCity))
        elif option_num == "2":
            code = input("Enter a Country Code :")
            get_countryCode = requests.get(codeUrl+code)
            jsonObj = get_countryCode.json()
            capitalCity = jsonObj['capital']
            countryName = jsonObj['name']
            print('The Country with Code {} is {}. The capital of the country {} is {}'.format(code, countryName, countryName, capitalCity))
        elif option_num == "0":
            break
            exit()
        else:
            print("Please Enter a valid Option")
    except:
        print("Invalid input. Please enter a valid country name or code")

