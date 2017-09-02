from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import Select, WebDriverWait
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
driver = webdriver.Chrome('./chromedriver')
url= "http://jansunwai.up.nic.in/"
#driver.maximize_window()
# url='http://jansunwai.up.nic.in/OnlineEntryNew.aspx'
# urll='http://127.0.0.1:58895'
# session_id='cbe353f7b1d9230b4ec646b17c77509a'
# driver = webdriver.Remote(command_executor=urll,desired_capabilities={})
# driver.session_id = session_id
# print "!"

driver.get(url)
raw_input("Enter1\n")
tabs2 =driver.window_handles
print tabs2
driver.switch_to_window(driver.window_handles[1])

urll = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
session_id = driver.session_id 

print urll
print session_id
print "-----"
def go():
	select = Select(driver.find_element_by_id("District"))
	#waitForElementPresent(select)
		
	hin=driver.find_element_by_id("aHindi")
	eng=driver.find_element_by_id("aEnglish")
	#eng.click()
	options = select.options
	i=j=k=0
	ti=1

	for x in options:
		print i," District="+x.text
		driver.implicitly_wait(30)
		select.select_by_index(i)
		time.sleep(ti)
		selectT = Select(driver.find_element_by_id("Tehsil"))
		optionsT = selectT.options
		j=0
		for xT in optionsT:
			print i," ",j,"---Tehsil="+xT.text
			driver.implicitly_wait(30)
			
			selectT.select_by_index(j)
			time.sleep(ti)
			selectB = Select(driver.find_element_by_id("Block"))
			optionsB = selectB.options
			k=0
			for xB in optionsB:
				print i," ",j," ",k,"------Block="+xB.text
				driver.implicitly_wait(30)
				selectB.select_by_index(k)
				time.sleep(ti)
				selectV = Select(driver.find_element_by_id("Village"))
				optionsV = selectV.options
				for xV in optionsV:
					print "---------Village="+xV.text
				k=k+1
			j=j+1			
		i=i+1

	content = driver.page_source.encode('utf-8').strip()
	soup = BeautifulSoup(content,"html.parser")
	#driver.quit()

go()
raw_input("Press2\n")
print("***********\n\n\n\n\n")
#go()