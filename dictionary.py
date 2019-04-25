import requests
import json
outfile = open('data.json', 'w')
file = open('slownik.txt', 'w')
di= {"komputer":"Urzadzenie do przetwarzania informacji","A":"Pierwsza litera alfacetu","Laptop":"przenośny komputer"}
word = input("Podaj słowo")
spr = 0;
for s in di:
    if s==word:
        print(slownik[s])
        spr =1;
if(spr == 0):
    app_id = '11138763'
    app_key = '3df6820c701ddbe9c77fe7aa1ee1b849'

    language = 'en'
    word_id = word

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

        

    di[word] = str(r.json()['results'][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0])
for s in di:
        json.dump(s+":"+di[s]+'\n', outfile)
print(di)
outfile.close()
