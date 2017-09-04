from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import Select, WebDriverWait
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
driver = webdriver.Chrome('./chromedriver')
url= "http://jansunwai.up.nic.in/"
# url='http://jansunwai.up.nic.in/OnlineEntryNew.aspx'
# urll='http://127.0.0.1:47325'
# session_id='5914658b0b67b6e091d690130ee5f855'
# driver = webdriver.Remote(command_executor=urll,desired_capabilities={})
# driver.session_id = session_id
# print "!"
# By byValue = By.cssSelector("#alertSubCatSelectBox > option[value='18222216517']");
# //By byText = By.xpath("//select[@id='alertSubCatSelectBox']/option[text()='Item x']");
# Select(driver.find_element_by_xpath("District"))
# new WebDriverWait(driver, 10).until(ExpectedConditions.presenceOfElementLocated(byValue));
# element = WebDriverWait(driver, 2).until(
#     EC.presence_of_element_located((By.ID, "District"))
# )



driver.get(url)
i1=int(raw_input("Enter1\n"))
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
	ti=0
	sel="Select"
	selectT=Select(driver.find_element_by_id("Tehsil"))
	selectB=Select(driver.find_element_by_id("Block"))
	selectV=Select(driver.find_element_by_id("Village"))
	selectV1=None
	selectB1=None
	selectT1=None

	for x in options:
		#print i," District="+x.text
		driver.implicitly_wait(30)
		select.select_by_index(i)
		sS=select.first_selected_option.text
		if(sel in sS):
			i=i+1
			continue
		if(i<i1):
			i=i+1
			continue	
		print i," Districts="+sS
		
		time.sleep(ti)
		while(selectT==selectT1):
			selectT = Select(driver.find_element_by_id("Tehsil"))
			pass
		print "selectT=",selectT	
		optionsT = selectT.options
		selectT1=selectT
		j=0
		for xT in optionsT:
			driver.implicitly_wait(30)
			
			selectT.select_by_index(j)
			sT=selectT.first_selected_option.text
			if(sel in sT):
				j=j+1
				continue
			print i," ",j,"---Tehsil="+sT
			
			time.sleep(ti)
			while(selectB==selectB1):
				selectB = Select(driver.find_element_by_id("Block"))
				pass
			selectB1=selectB
			
			optionsB = selectB.options
			k=0
			for xB in optionsB:
				
				driver.implicitly_wait(30)
				selectB.select_by_index(k)
				sB=selectB.first_selected_option.text
				if(sel in sB):
					k=k+1
					continue
				print i," ",j," ",k,"------Block="+sB
				
				time.sleep(ti)
				while(selectV1==selectV):
					selectV = Select(driver.find_element_by_id("Village"))
				selectV1=selectV
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