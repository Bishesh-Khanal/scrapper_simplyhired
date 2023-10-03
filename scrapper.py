import requests
from bs4 import BeautifulSoup
import pandas as pd

def error_detection(job, tag, class_):
    global current
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



