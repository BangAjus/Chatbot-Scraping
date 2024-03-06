from bs4 import BeautifulSoup as bs
import requests

def config(url):

    header = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    req = requests.get(url, headers = header)

    return bs(req.text, 'html.parser')

def description():

    url = 'https://www.kaamalaresort.com/'
    sup = config(url)


    desc = sup.findAll('p')
    desc = desc[1].string

    return desc

def facilities():

    url = 'https://www.kaamalaresort.com/'
    sup = config(url)
    
    fac = sup.findAll("section",
                      {"id":"facilities"})

    items = []
    for i in fac:
        item = i.findAll('h3')

        for j in item:
            print(j.string)
            items.append(j.string)
    
    return items

def faclities_detail():

    url = 'https://www.kaamalaresort.com/'
    sup = config(url)

    fac = sup.findAll("section",
                    {"id":"facilities"})

    items = []
    detail = []
    link = []
    for i in fac:
        item = i.findAll('h3')

        for j in item:
            print(j.string)
            items.append(j.string)

    for i in fac:
        p = i.findAll('p')[1:-1]

        for j in p:
            print(j.string)
            detail.append(j.string)

    for i in fac:
        href = i.findAll('a')

        for j in href:
            print(j.get('href'))
            link.append(j.get('href'))
    link[4] = 'https://www.kaamalaresort.com' + link[4]

    return items, detail, link

def rooms():

    url = 'https://www.kaamalaresort.com/'
    sup = config(url)

    acc = sup.findAll("section",
                  {"id":"Accomodation"})

    items = []
    for i in acc:
        item = i.findAll('h4')

        for j in item:
            print(j.string)
            items.append(j.string)
    
    return items

def rooms_detail():

    url = 'https://www.kaamalaresort.com/'
    sup = config(url)

    acc = sup.findAll("section",
                    {"id":"Accomodation"})

    items = []
    href = []
    infos = []
    for i in acc:
        item = i.findAll('h4')

        for j in item:
            print(j.string)
            items.append(j.string)

    for i in acc:
        link = i.findAll('a')

        for j in link:
            print(j.get('href'))
            href.append('https://www.kaamalaresort.com' + j.get('href'))

    for i in href:
        sup = config(i)
        detail = sup.findAll('div', 'portfolio-info')

        for j in detail:
            item = j.findAll('li')
            store = []

            for k in item:
                print(k.text)
                store.append(k.text)

            infos.append(store)

    return items, href, infos

def booking():

    url = 'https://www.kaamalaresort.com/'
    sup = config(url)

    book = sup.findAll('header')
    href = None

    for i in book:
        href = i.find('a', 'get-started-btn ml-auto mr-4').get('href')

    return href

