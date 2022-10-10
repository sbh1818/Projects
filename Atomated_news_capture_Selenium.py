from selenium import webdriver
import pandas as pd
from datetime import datetime
website= "https://www.ptinews.com/"
driver=webdriver.Chrome()
driver.get(website)
contents=driver.find_elements(by="xpath",value='//div[@class="news-description"]')
titles,gists,links=[],[],[]
for content in contents:
    title=content.find_element(by="xpath",value='./h3/a').text
    gist=content.find_element(by="xpath",value='./p/a').text
    link=content.find_element(by="xpath",value='./p/a').get_attribute('href')
    titles.append(title)
    gists.append(gist)
    links.append(link)
my_dict={'title':titles,'gist':gists,'link':links}
df_headlines=pd.DataFrame(my_dict)
now = datetime.now()
dt_string = now.strftime("%d.%m.%Y_%H.%M.%S")
df_headlines.to_csv('headlines_{}.csv'.format(dt_string))
driver.quit()
