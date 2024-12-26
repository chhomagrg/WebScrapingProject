import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Automatically manage ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://www.yearupalumni.org/s/1841/home.aspx?sid=1841&gid=2')


results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
driver.quit()

for a in soup.findAll(attrs={'class': 'newsItem'}):
    name = a.find('div', class_='title')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(attrs={'class': 'newsItem'}):
    description = b.find('div', class_='preview')
    if description not in other_results:
        other_results.append(description.text)

df = pd.DataFrame({'Event Names': results, 'Descriptions': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')