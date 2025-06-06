from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


options = Options()
options.add_argument("--headless")

browser = webdriver.Firefox(options=options)
browser.get('https://www.business-standard.com/finance/news')


articleList = browser.find_elements(By.CLASS_NAME, "cardlist") #finds all the articles on the page

with open("top 5 news.txt", 'w') as file:   #prints them from the returned list one by one
    for i in range(5):
                       
        file.write(articleList[i].text + '\n\n')


browser.quit()
print("Done!")

#only works with firefox for a reason I cannot guess or find anything about