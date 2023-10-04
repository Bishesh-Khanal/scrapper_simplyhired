import requests
from bs4 import BeautifulSoup
import pandas as pd

def error_detection(item, tag, classs=0):
    global current
    try:
        current = item.find(tag, class_ = classs).text
    except:
        current = 'N/A'
        
def scrape(URL, headers, jobs_dictionary, pages_visited, pages_to_scrape):
    html_contents = requests.get(URL, headers = headers)
    print('page status code = ', html_contents.status_code)
    
    soup = BeautifulSoup(html_contents.text, 'lxml')
    jobs = soup.find_all('li', class_ = 'css-0' )
    for job in jobs:
        error_detection(job, 'a', 'chakra-button css-1y7j4hn')
        jobs_dictionary['Job'].append(current)
        
        job_link = "https://www.simplyhired.com" + job.find('a', 'chakra-button css-1y7j4hn')['href']
        jobs_dictionary['Job Link'].append(job_link)
        
        job_contents = requests.get(job_link, headers = headers)
        print('Job status code = ', job_contents.status_code)
        
        soup_job_details = BeautifulSoup(job_contents.text, 'lxml')
        job_details = soup_job_details.find('div', class_ = 'css-1u3q0w0')
        
        job_type = job_details.find('div', class_ = 'css-1ebprri')
        error_detection(job_type, 'span', 'chakra-stack css-xtodu4')
        jobs_dictionary['Type'].append(current)
        
        job_benefits_qualifications = job_details.find_all('div', class_ = 'css-1ebprri')
        i = 1
        
        try:
            job_benefits_list = job_benefits_qualifications[i]
            if job_benefits_list.find('h3').text != 'Qualifications':
                job_benefits = job_benefits_list.find_all('li', class_ = 'chakra-wrap__listitem css-1yp4ln')
                benefits = []
                for job_benefit in job_benefits:
                    benefits.append(job_benefit.text)
                jobs_dictionary['Benefits'].append(', '.join(map(str, benefits)))
                i = i + 1
            else:
                jobs_dictionary['Benefits'].append('N/A')
        except:
            jobs_dictionary['Benefits'].append('N/A')
        
        try:
            job_qualificatons_list = job_benefits_qualifications[i]
            job_qualifications =  job_qualificatons_list.find_all('li', class_ = 'chakra-wrap__listitem css-1yp4ln')
            qualifications = []
            for job_qualification in job_qualifications:
                qualifications.append(job_qualification.text)
            jobs_dictionary['Qualifications'].append(', '.join(map(str, qualifications)))
        except:
            jobs_dictionary['Qualifications'].append('N/A')
        
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