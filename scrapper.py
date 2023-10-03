import requests
from bs4 import BeautifulSoup
import pandas as pd

<<<<<<< HEAD
def error_detection(job, tag, class_):
    global current
=======
headers = {
        'authority': 'www.simplyhired.com',
        'method': 'GET',
        'path': '/search?q=computer+science&l=Remote',
        'scheme': 'https',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Cookie': 'shk=1h31lp1tai0dq801; shk=1h31lp1tai0dq801; _ga=GA1.1.537460492.1686904558; indeed_rcc=st:arq:r:shk:rjc:rjs; arq=ZPrY-kFIOlCXGE7d9MwWC4acRxxUAz25dFcHY9SnhJBh60--_mlKmKF4WQ; r=X7lVBAnHTQ42iqe0MmPmIgw-gG_8vsUJshkEzqPdQAUmrAB9Q-z7Xg7AKJO1aAYOVQEkiSWB-MkyxTrordY1Ow; rjc={%22slots%22:[0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C2]%2C%22lastVisited%22:1686905029304}; rjs={%22slots%22:[0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C14]%2C%22lastVisited%22:1686905045011}; st=LcDe3Jl1meRLctXhrXM7NEX8FGzlhzg8PUm8WC20XkGcas1vFGon-wBAlguuR6JH; csrf=y3eySfkzT_7JtF-nsAo4ydIozkUYHOgvjLt32l-X2FXXfIEBNNDIexDsQyy8WKQd5tWJfJ5fCUonrSCSvSIp; __cf_bm=I0_BrOwysOS_AF6eU9rX317QEmLSytFsdeiDMmvw9Wk-1696178734-0-AUAtL24G5A1uytW/eiAT+Vkeog7dmml6FDYJXjtyLo/cjogPltwwUA/FD7YSBAqBiQKt3HHP4rOfKYg9YuDX7UI=; OptanonConsent=isIABGlobal=false&datestamp=Sun+Oct+01+2023+22%3A24%3A50+GMT%2B0545+(Nepal+Time)&version=202301.2.0&hosts=&consentId=27a9c722-8672-466f-a440-c3f66adadf7a&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CC0003%3A1%2CC0007%3A0&isGpcEnabled=0&AwaitingReconsent=false; rq=%5B%22q%3Dcomputer%2Bscience%26l%3DRemote%26ts%3D1696178757551%22%2C%22q%3Dcomputer%2Bscience%26l%3DRemote%252Fpage%252F2%26ts%3D1696175986198%22%2C%22q%3Dcomputer%2Bscience%26l%3DRemote%26ts%3D1696175977180%22%2C%22q%3Ddata%2Bscientist%26l%3DRemote%26ts%3D1696166893867%22%2C%22q%3Dcomputer%26l%3DRemote%26ts%3D1696072358373%22%2C%22q%3Dcomputer%26l%3Dremote%26ts%3D1696072339176%22%2C%22q%3Dengineer%26l%3DRemote%26ts%3D1696072089433%22%2C%22q%3Dcomputer%2Bscientist%26l%3DRemote%26ts%3D1696072067834%22%5D; _ga_9GC5K2RCSP=GS1.1.1696174579.6.1.1696178409.0.0.0',
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
data = {'Job': [], 'Salary': [], 'Company': [], 'Posted': []}

html_text = requests.get('https://www.simplyhired.com/search?q=computer+science&l=Remote', headers = headers)
print(html_text.status_code)
soup = BeautifulSoup(html_text.text, 'lxml')
jobs = soup.find_all('div', class_ = 'css-f8dtpc' )
for job in jobs:
    job_name = job.find('a', class_ = 'chakra-button css-1y7j4hn').text
    salary = job.find('p', class_ = 'chakra-text css-1ejkpji').text
    company = job.find('span', class_ = 'css-lvyu5j').text
>>>>>>> 8456223f4ac1fab21b18dbf9125d5fcc66496356
    try:
        current = job.find(tag, class_ = class_).text
    except:
        current = 'N/A'

def scrape(URL, headers, jobs_dictionary):
    html_contents = requests.get(URL, headers = headers)
    print('status code = ', html_contents.status_code)
    soup = BeautifulSoup(html_contents.text, 'lxml')
    jobs = soup.find_all('li', class_ = 'css-0' )
    
    for job in jobs:
        error_detection(job, 'a', 'chakra-button css-1y7j4hn')
        jobs_dictionary['Job'].append(current)
        error_detection(job, 'p', 'chakra-text css-1ejkpji')
        jobs_dictionary['Salary'].append(current)
        error_detection(job, 'span', 'css-lvyu5j')
        jobs_dictionary['Company'].append(current)
        error_detection(job, 'p', 'chakra-text css-5yilgw')
        jobs_dictionary['Posted'].append(current)
        
    return pd.DataFrame(jobs_dictionary)



