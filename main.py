import json
import requests
import re

base_url = 'https://api-hermes.pathao.com'

DataAccessToken = json.dumps({
    'client_id': 'l4zbqP7apr',
    'client_secret': '2RGljzzrtYtWE11bNSA0Q0bvcWF9Sm0JOcgS5J9b',
    'username': 'damask.online@gmail.com',
    'password': 'damask123',
    'grant_type': 'password'
})

HeadersAccessToken = {
'accept' : "application/json",
'content-type' : "application/json"
}

r = requests.post(base_url + '/aladdin/api/v1/issue-token', data=DataAccessToken, headers=HeadersAccessToken)

print(r.text)

acc_token = r.json()['access_token']
ref_token = r.json()['refresh_token']

HeadersCreateOrder = {
'Authorization' : 'Bearer ' + acc_token,
'accept' : "application/json",
'content-type' : "application/json"
}

cityZones = ['']

#r2 = requests.get(base_url + '/aladdin/api/v1/countries/1/city-list', headers=HeadersCreateOrder)
#cities = r2.json()['data']['data']
cities = [{'city_id': 52, 'city_name': 'Bagerhat'}, {'city_id': 62, 'city_name': 'Bandarban '}, {'city_id': 34, 'city_name': 'Barguna '}, {'city_id': 17, 'city_name': 'Barisal'}, {'city_id': 32, 'city_name': 'B. Baria'}, {'city_id': 53, 'city_name': 'Bhola'}, {'city_id': 9, 'city_name': 'Bogra'}, {'city_id': 8, 'city_name': 'Chandpur'}, {'city_id': 15, 'city_name': 'Chapainawabganj'}, {'city_id': 2, 'city_name': 'Chittagong'}, {'city_id': 61, 'city_name': 'Chuadanga'}, {'city_id': 11, 'city_name': "Cox's Bazar"}, {'city_id': 5, 'city_name': 'Cumilla'}, {'city_id': 1, 'city_name': 'Dhaka'}, {'city_id': 35, 'city_name': 'Dinajpur'}, {'city_id': 18, 'city_name': 'Faridpur'}, {'city_id': 6, 'city_name': 'Feni'}, {'city_id': 38, 'city_name': 'Gaibandha'}, {'city_id': 22, 'city_name': 'Gazipur'}, {'city_id': 56, 'city_name': 'Gopalgonj '}, {'city_id': 30, 'city_name': 'Habiganj'}, {'city_id': 41, 'city_name': 'Jamalpur'}, {'city_id': 19, 'city_name': 'Jashore'}, {'city_id': 27, 'city_name': 'Jhalokathi'}, {'city_id': 49, 'city_name': 'Jhenidah'}, {'city_id': 48, 'city_name': 'Joypurhat'}, {'city_id': 63, 'city_name': 'Khagrachari'}, {'city_id': 20, 'city_name': 'Khulna'}, {'city_id': 42, 'city_name': 'Kishoreganj'}, {'city_id': 55, 'city_name': 'Kurigram '}, {'city_id': 28, 'city_name': 'Kushtia'}, {'city_id': 40, 'city_name': 'Lakshmipur'}, {'city_id': 57, 'city_name': 'Lalmonirhat '}, {'city_id': 43, 'city_name': 'Madaripur'}, {'city_id': 60, 'city_name': 'Magura '}, {'city_id': 16, 'city_name': 'Manikganj'}, {'city_id': 50, 'city_name': 'Meherpur'}, {'city_id': 12, 'city_name': 'Moulvibazar'}, {'city_id': 23, 'city_name': 'Munsiganj'}, {'city_id': 26, 'city_name': 'Mymensingh'}, {'city_id': 46, 'city_name': 'Naogaon'}, {'city_id': 54, 'city_name': 'Narail '}, {'city_id': 21, 'city_name': 'Narayanganj'}, {'city_id': 47, 'city_name': 'Narshingdi'}, {'city_id': 14, 'city_name': 'Natore'}, {'city_id': 44, 'city_name': 'Netrakona'}, {'city_id': 39, 'city_name': 'Nilphamari'}, {'city_id': 7, 'city_name': 'Noakhali'}, {'city_id': 24, 'city_name': 'Pabna'}, {'city_id': 37, 'city_name': 'Panchagarh'}, {'city_id': 29, 'city_name': 'Patuakhali'}, {'city_id': 31, 'city_name': 'Pirojpur'}, {'city_id': 58, 'city_name': 'Rajbari '}, {'city_id': 4, 'city_name': 'Rajshahi'}, {'city_id': 59, 'city_name': 'Rangamati '}, {'city_id': 25, 'city_name': 'Rangpur'}, {'city_id': 51, 'city_name': 'Satkhira'}, {'city_id': 64, 'city_name': 'Shariatpur '}, {'city_id': 33, 'city_name': 'Sherpur'}, {'city_id': 10, 'city_name': 'Sirajganj'}, {'city_id': 45, 'city_name': 'Sunamganj'}, {'city_id': 3, 'city_name': 'Sylhet'}, {'city_id': 13, 'city_name': 'Tangail'}, {'city_id': 36, 'city_name': 'Thakurgaon '}]

print(cities)

for i in cities:
    r3 = requests.get(base_url + '/aladdin/api/v1/cities/'+str(i['city_id'])+'/zone-list', headers=HeadersCreateOrder)
    print(r3.text)
    zones = r3.json()['data']['data']

    for j in zones:
        cityZones.append(str(i['city_name'] + '>' + j['zone_name'] + '>' + str(i['city_id']) + '>' + str(j['zone_id']) + '>').lower())

print(cityZones)

DataCreateOrder = {
    'store_id': 3855,
    'merchant_order_id': "90000000",
    'sender_name': "Damask",
    'sender_phone': "01679386155",
    'recipient_name': "Dummy entry",
    'recipient_phone': "01618116916",
    'recipient_address': "500 west kazipara",
    'recipient_city': 1,
    'recipient_zone': 1,
    # 'recipient_area': 1,
    'delivery_type': 48,
    'item_type': 2,
    'special_instruction': "",
    'item_quantity': 1,
    'item_weight': 0.5,
    'amount_to_collect': 1450,
    # 'item_description': "<item description>"
}

step = 0

while True:
    inp = input('Enter Data: ')

    for step in range(30):
        if step == 2:
            DataCreateOrder['recipient_name'] = re.search('Customer Name :	(.*)Inv Date :	', inp)
            step += 1
        elif step == 8:
            DataCreateOrder['recipient_address'] = re.search('Cus Address :	(.*)Phone No :	', inp)
            step += 1
        elif step == 11:
            DataCreateOrder['recipient_phone'] = re.search('Phone No :	(.*)Total Amt. :	', inp)
            step += 1
        elif step == 16:
            DataCreateOrder['merchant_order_id'] = re.search('Inv. Ref:	(.*)Disc Amt.:	', inp)
            step += 1
        elif step == 21:
            DataCreateOrder['amount_to_collect'] = re.search('Net Total.:	(.*)\n  \n  Bill No:  INV10040745 Status: Open', inp)
            step += 1
        elif step == 22:
            if inp.isdigit():
                for i in cityZones:
                    if i.__contains__('>' + inp + '>'):
                        print(i)
                        DataCreateOrder['recipient_zone'] = int(inp)
                        DataCreateOrder['recipient_city'] = i.split('>')[2]
                        step += 1
                        break
            else:
                for i in cityZones:
                    if i.__contains__(inp):
                        print(i)
        elif step == 23:
            if inp.isdigit():
                DataCreateOrder['item_quantity'] = inp
                step += 1

        print(DataCreateOrder)

        if step == 24:
            #r1 = requests.post(base_url + '/aladdin/api/v1/orders', data=json.dumps(DataCreateOrder), headers=HeadersCreateOrder)

           # print(r1.text)
            step = 0
