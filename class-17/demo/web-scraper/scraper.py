import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Engineer&where=seattle&intcid=skr_navigation_nhpso_searchMain'

response = requests.get(URL)

# print(dir(response))

content = response.content
# print(content)

soup = BeautifulSoup(content, 'html.parser')

# print(soup.prettify())

result = soup.find(id='SearchResults')

# print(result.length())

job_result = result.find_all('section', class_='card-content')
# print(type(job_result))

# print(len(job_result))

# print(job_result[7])
# title0 = job_result[7].find('h2', class_='title').text.strip()
# location0 = job_result[7].find('div', class_='location').text.strip()
# company0 = job_result[7].find('div', class_='company').text.strip()

# print(title0)
# print(location0)
# print(company0)


final_result = []

for jobs in job_result:
    job_dict={}
    if jobs.find('h2', class_='title'):
        title = jobs.find('h2', class_='title').text.strip()
        job_dict['title'] = title
        location = jobs.find('div', class_='location').text.strip()
        job_dict['location'] = location
        company = jobs.find('div', class_='company').text.strip()
        job_dict['company'] = company

        final_result.append(job_dict)

print(final_result)
