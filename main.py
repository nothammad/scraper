from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

service = Service(executable_path="./chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(service=service, options=options)

url = "https://github.com/collections/machine-learning"
driver.get(url)
time.sleep(3)  

projects = driver.find_elements(By.XPATH, "//h1[@class='h3 lh-condensed']")

project_list = []
for proj in projects:
    name = proj.text
    url = proj.find_element(By.TAG_NAME, "a").get_attribute("href")
    project_list.append({"project_name": name, "project_url": url})

driver.quit()

df = pd.DataFrame(project_list)
df.to_csv("project_list.csv", index=False)
print("✅ Scraped and saved to project_list.csv")
