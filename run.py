import requests #module untuk eminta http yang akan discrap
import csv # untuk menampung hasil scrap

# masukan Key 
key = input('Insert Key : ')

# write to csv
write = csv.writer(open(f'scBukalapak/{key}.csv',mode = 'w',newline = ''))
# header = ['no','nama', 'harga', 'stock']
write.writerow(['no','nama', 'harga', 'stock'])

# URL using request
url = 'https://api.bukalapak.com/multistrategy-products?'
count = 0
token = 'irIF3pl-6Qh9hcbfbh9OV4uEWgh25KfdQ2S3PYGjxccU1g'

# looping limit 50 dan page 10 jadi 500 data
for page in range(1,11):
    param = {
    'keywords': key,
    'limit': 50,
    'offset':50,
    'facet': True,
    'page': page,
    'shouldUseSeoMultistrategy': False,
    'isLoggedIn': True,
    'show_search_contexts': True,
    'access_token': token
    }

# get url dan param
    r = requests.get(url,params= param).json()

    products = r['data']

#looping data from bukalapak
    for p in products:
        # print(p)
        name, harga, stock = p['name'], p['price'], p['stock']
        count += 1
        print('count : ', count,'name : ',name,'harga : ', harga,'stock : ',stock)

        #data from json append to csv
        write = csv.writer(open(f'scBukalapak/{key}.csv',mode = 'a',newline = ''))
        data = [count,name, harga, stock]
        write.writerow(data)