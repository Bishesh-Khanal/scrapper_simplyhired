from scrapper import scrape
import pandas as pd

#If the program gives 'status code = 403', do the following:
'''
1. Go to 'https://www.simplyhired.com/'
2. Go to 'inspect elements'
3. Go to 'Network'
4. Refresh
5. Go to the one with the domain-name: 'www.simplyhired.com'
6. Go to 'Headers'
7. Go to 'Request Headers'
8. Copy all of it and paste in the dictionary below in given manner
'''
headers = {
        'authority': 'www.simplyhired.com',
        'method': 'GET',
        'path': '/',
        'scheme': 'https',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Cookie': 'shk=1h31lp1tai0dq801; shk=1h31lp1tai0dq801; _ga=GA1.1.537460492.1686904558; indeed_rcc=st:arq:r:shk:rjc:rjs; arq=ZPrY-kFIOlCXGE7d9MwWC4acRxxUAz25dFcHY9SnhJBh60--_mlKmKF4WQ; r=X7lVBAnHTQ42iqe0MmPmIgw-gG_8vsUJshkEzqPdQAUmrAB9Q-z7Xg7AKJO1aAYOVQEkiSWB-MkyxTrordY1Ow; rjc={%22slots%22:[0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C2]%2C%22lastVisited%22:1686905029304}; rjs={%22slots%22:[0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C14]%2C%22lastVisited%22:1686905045011}; st=LcDe3Jl1meRLctXhrXM7NEX8FGzlhzg8PUm8WC20XkGcas1vFGon-wBAlguuR6JH; csrf=5EpEXzNZ2So5PIt2xzxRYgL4OKSE_SeT5YjtlX00NsbD-mgQYbf2qb1_s7M-xrzVL1FGRDK51INedszGbXWe; __cf_bm=7B2Fk97ovey.ZrEjUUPzWvxKg6ll5VvJIlwa0VavrIc-1696406029-0-AdwAhLb3iwx2PKwOZkWbwxytQfW6nqsASS8Ed01GMDUBcuAfuz+skSuCUW6cCeaSke39tAD3sHFNnaDWlcJb8k8=; rq=%5B%22q%3Dcomputer%26l%3Dremote%252F%26ts%3D1696406317572%22%2C%22q%3Dcomputer%26l%3Dremote%26ts%3D1696401614054%22%2C%22q%3Ddata%2Banalyst%26l%3DNew%2BYork%26ts%3D1696337643979%22%2C%22q%3Dastrophysics%26l%3DNew%2BYork%26ts%3D1696335709784%22%2C%22q%3Dcomputer%26l%3DNew%2BYork%26ts%3D1696334738769%22%2C%22q%3Dcomputer%2Bscience%26l%3Dremote%26ts%3D1696334439264%22%2C%22q%3Dbiology%26l%3Dremote%26ts%3D1696334349574%22%2C%22q%3Dbiology%26l%3D%26ts%3D1696334343030%22%5D; OptanonConsent=isIABGlobal=false&datestamp=Wed+Oct+04+2023+13%3A46%3A30+GMT%2B0545+(Nepal+Time)&version=202301.2.0&hosts=&consentId=27a9c722-8672-466f-a440-c3f66adadf7a&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CC0003%3A1%2CC0007%3A0&isGpcEnabled=0&AwaitingReconsent=false; _ga_9GC5K2RCSP=GS1.1.1696401252.8.1.1696406490.0.0.0',
        'Sec-Ch-Ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': "Windows",
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47'
    }

'''
Please be careful while entering the query and location!!
THERE CAN ONLY BE ONE ' '(SPACE) IN THE query AND THE location EACH FOR THE PROGRAM TO RUN!!!!!!
THE QUERY AND LOCATION BOTH NEED TO BE VALID FOR THE simplylearn website FOR THE PROGRAM TO RUN!!!!!
'''
query = input('Enter the sector whose jobs you want: ')

location = input('Enter the location or enter remote/Remote: ')

pages_to_scrape = int(input('Enter the number of pages to scrape: '))

if ' ' not in query:
    if ' ' not in location:
        URL = 'https://www.simplyhired.com/search?q=' + query + '&l=' + location
    else:
        URL = 'https://www.simplyhired.com/search?q=' + query + '&l=' + location[0:location.index(' ')] + '+' + location[location.index(' ')+1:len(location)]
else:
    if ' ' not in location:
        URL = 'https://www.simplyhired.com/search?q=' + query[0:query.index(' ')] + '+' + query[query.index(' ')+1:len(query)] + '&l=' + location
    else:
        URL = 'https://www.simplyhired.com/search?q=' + query[0:query.index(' ')] + '+' + query[query.index(' ')+1:len(query)] + '&l=' + location[0:location.index(' ')] + '+' + location[location.index(' ')+1:len(location)]

jobs_dictionary = {'Job': [], 'Salary': [], 'Company': [], 'Rating': [], 'Posted': []}

pages_visited = pd.Series(['1'])

pages_visited.name = 'Page Numbers Visited'

jobs_dataFrame = scrape(URL, headers, jobs_dictionary, pages_visited, pages_to_scrape)

jobs_dataFrame.to_csv('jobs_uncleaned.csv')