import requests
import random

name = ''

# This is the URL of Google Form
#                                        <---------------------- Replace This Part -------------->
url = "https://docs.google.com/forms/d/e/1FAIpQLSfxx3IIT6geNAFPA-VwvHXnsVs1UQMKKDZjgQ7bb7x3G71yjA/formResponse"

def get_name():
    global name
    first_names = ['A','B','C','D']
    last_names = ['W','X','Y','Z']
    i = random.randint(0,len(first_names)-1)
    j = random.randint(0,len(last_names)-1)
    name = first_names[i] + " " + last_names[j]
    return name

def get_phone():
    n=9
    range_start = 10**(n-1)
    range_end = (10**n)-1
    num = random.randint(range_start, range_end)
    return str('9' + str(num))

def get_email():
    global name
    email = name.lower().replace(' ','.') + "@gmail.com"
    return email

def get_gender():
    gender = ['Male', 'Female', 'Prefer not to say']
    i = random.randint(0,len(gender)-1)
    return gender[i]

def send_fake_data():
    data = {
        "entry.2005620554": get_name(),   #
        "entry.1045781291": get_email(),  # Replace these numbers with the ones found in the webpage source code
        "entry.1065046570": get_gender(), #
        "entry.1166974658": get_phone()   #
    }
    
    print(data)
    result = requests.post(url, data)
    print(result)


n=int(input("How many spam entries do you wan to send "))
for i in range(n):
    send_fake_data()
