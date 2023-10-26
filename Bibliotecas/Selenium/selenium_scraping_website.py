import os
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
os.environ['PATH']+=r"C:\\selenium_drivers\\chromedriver-win32\\chromedriver-win32"

website = "https://www.thesun.co.uk/sport/football/"


driver = webdriver.Chrome()
driver.get(website)


#xpath find in sequel

div = driver.find_element(by='xpath', value='//div[@class="article-recommendation-container]')

titles = []
subtitles = []
links = []

for h2 in div:
    title = h2.driver.find_element(by='xpath', value='//div[@class="article-recommendation-container]/a/h2').text
    subtitle = h2.driver.find_element(by='xpath', value='./a/p').text
    link = h2.driver.find_element(by='xpath', value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)
    

dict_ = {"title": titles,
         "subtitle": subtitles,
         "link": links}
df = pd.DataFrame(dict_)
print(df)
df.to_csv("Headlines.csv")
driver.quit()

#comparação com beutiful soup 
# from bs4 import BeautifulSoup
# import requests
# import time

# i = False
# list = list()
# while i == False:
#     print("Insert keywords for seach one job")
#     answer = input("> ")
#     answer = answer.lower()
#     list.append(answer)
#     close = input("Do you want insert another keyword? y/n: ")
#     if close.lower() == "y":
#         continue;
#     else:
#          break;



# def main(): 

    


#     print(list)
#     print(f"filtering jobs by... {list}")
#     # get request
#     html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

#     #intancia beutifulsoup e argumentos
#     soup = BeautifulSoup(html_text, 'lxml')

#     # tag macro> tags especificas
#     li = soup.find_all('li', class_ ='clearfix job-bx wht-shd-bx')

#     #index variável contadora 1- job; 2 - job....

#     for index, jobs in enumerate(li) :
#         publish_date = jobs.find('span', class_ ='sim-posted').text
#     # filtro de data
#         if "few" in publish_date.lower():

#             company_name = jobs.find('h3', class_='joblist-comp-name').text.replace(" ","")
#             skills = jobs.find('span',class_ = 'srp-skills').text.replace(" ","")
#         # iterando as keywords dadas dentro do scraping    
#         for answer in range(len(list)):
#                 if list[answer] in skills.lower():
#                     with open(f'C:\\Users\\arthu\\OneDrive\\Documentos\\Projetos\\Projetos de estudo\\Python\\Programas\\web scraping jobs site\\data{index}.txt', 'w') as f:
#                         link = jobs.header.h2.a['href']
                                
#                         print("------------------------------")

#                         print(f'COMPANY: {company_name}')
                        
#                         print(f'SKILLS: {skills}')
                    
#                         print(f'LINK: {link}')


# if __name__ == '__main__':
#     while True:
#         main()
#         print(f"waiting {time_waiting}")
#         time_waiting = time.sleep(10)
        