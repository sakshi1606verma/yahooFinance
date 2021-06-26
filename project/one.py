
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
import time
import matplotlib.pyplot as plt
import pandas as pd


def change(l):
    ans= np.array([])
    for i in range(len(l)):
        if i < len(l)-1:
            pchange = abs(((l[i] - l[i+1])/l[i]))*100
            ans = np.append(ans,[pchange])
        if i == len(l)-1:
            ans = np.append(ans,0)    
   
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
dailycu = (1+ans).cumprod()
df['cumutative returns']=dailycu
print(df)
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(dailycu)

ax1.set_title("Cumulative Returns")
plt.show()


