
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time
import pandas as pd


def change(l):
    ans= []
    for i in range(len(l)):
        if i < len(l)-1:
            pchange = abs(((l[i] - l[i+1])/l[i]))*100
            ans.append(pchange)
        if i == len(l)-1:
            ans.append(None)    
   
    return ans
    

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window() 
driver.get('https://in.finance.yahoo.com/quote/AAPL?ltr=1')
time.sleep(1)

data = driver.find_element_by_xpath('//*[@id="quote-nav"]/ul/li[5]/a/span')
data.click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,'Download').click()

time.sleep(2)

driver.quit()

df = pd.read_csv('AAPL (1).csv')

lst = df['Adj Close']
ans = change(lst)
df['Adj PercentageChange'] = ans
 
print(df)


