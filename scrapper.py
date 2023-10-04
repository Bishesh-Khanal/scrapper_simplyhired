import requests
from bs4 import BeautifulSoup
import pandas as pd

def error_detection(job, tag, classs):
    global current
    try:
        current = job.find(tag, class_ = classs).text
    except:
        current = 'N/A'
        
def scrape(URL, headers, jobs_dictionary, pages_visited, pages_to_scrape):
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
        error_detection(job, 'span', 'css-epvm6')
        jobs_dictionary['Rating'].append(current)
        
    navigation = soup.find('nav', class_ = 'css-1hog1e3')
    
    pages = navigation.find_all('a', class_ = 'chakra-link css-1wxsdwr')
    
    for page in pages:
        URL = page['href']
        if len(pages_visited) < pages_to_scrape:
            if str(page.text) in str(pages_visited):
                continue
            else:
                pages_visited.loc[len(pages_visited)] = page.text
                scrape(URL, headers, jobs_dictionary, pages_visited, pages_to_scrape)
        else:
            break

    return pd.DataFrame(jobs_dictionary)