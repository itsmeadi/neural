from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import Select, WebDriverWait
driver = webdriver.Chrome('./chromedriver')
url= "https://indane.co.in/new_customer.php"
driver.maximize_window()
driver.get(url)

select = Select(driver.find_element_by_id("bgstate"))

options = select.options
i=0
for x in options:
	print x.text
	select.select_by_index(i)
	driver.implicitly_wait(5)
	time.sleep(1)
	select1 = Select(driver.find_element_by_id("bgdistrict"))
	options1 = select1.options
	for x1 in options1:
		print x1.text
	i=i+1

content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")

dis=soup.find("select",{"id":"bgdistrict"})
opt = dis.find_all("option")
for x in opt:
	print x
driver.quit()
