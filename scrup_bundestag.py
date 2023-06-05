import requests
from bs4 import BeautifulSoup
import json
# persons_url_list = []

# for i in range(0, 748, 12):
#     url = f'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=12&noFilterSet=true&offset={i}'
#     # print(url)
    
#     q = requests.get(url)
#     result = q.content
    
#     soup = BeautifulSoup(result, 'lxml')
#     persons = soup.find_all(class_='bt-slide-content')
        
#     for person in persons:
#         person_page_url = person.find('a').get('href')
#         # print(person_page_url)
#         # person_page_url = person.get('href')
#         persons_url_list.append(person_page_url)
        
# with open('persons_url_list.txt', 'a') as file:
#     for line in persons_url_list:
#         file.write(f'{line}\n')

with open('persons_url_list.txt') as file:
    
    lines = [line.strip() for line in file.readlines()]
    
    data_dict = []
    count = 0
    
    for line in lines:
        q = requests.get(line)
        result = q.content
        
        soup = BeautifulSoup(result, 'lxml')
        person = soup.find(class_='bt-biografie-name').find('h3').text
        person_name_company = person.strip().split(',')
        person_name = person_name_company[0]
        person_company = person_name_company[1].strip()
        
        social_network = soup.find_all(class_='bt-link-extern')
        
        social_network_urls = []
        for item in social_network:
            social_network_urls.append(item.get('href'))
        
        data = {
            'person_name': person_name,
            'company_name': person_company,
            'social_networks': social_network_urls
        }
        count += 1
        print(f'#{count}: {line} is done!')
        
        data_dict.append(data)
        
        with open('data.json', 'w') as json_file:
            json.dump(data_dict, json_file, indent=4)
            