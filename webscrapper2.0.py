import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from oauth2client.service_account import ServiceAccountCredentials
import gspread


driver = webdriver.Chrome()
driver.get('https://economictimes.indiatimes.com/tech/technology')

Credentials = ServiceAccountCredentials.from_json_keyfile_name('news.json')
file = gspread.authorize(credentials=Credentials)

sheet = file.open('Web news scrapper')

sheet = sheet.sheet1

for i in range(1, 11):
    Headline = driver.find_element(By.XPATH, '/html/body/main/div[10]/section/div['+str(i)+']/div[2]/h4/a').text
    content = driver.find_element(By.XPATH, '/html/body/main/div[10]/section/div['+str(i)+']/div[2]/p').text
    time = driver.find_element(By.XPATH, '/html/body/main/div[10]/section/div['+str(i)+']/time').text

    print(Headline)
    print(content)
    print(time)

    sheet.update_acell('A'+str(i+1), Headline)
    sheet.update_acell('B'+str(i+1), content)
    sheet.update_acell('C'+str(i+1), time)