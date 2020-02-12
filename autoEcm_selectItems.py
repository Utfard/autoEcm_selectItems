from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
#from selenium.common.exceptions import NoSuchElementException
from time import sleep
#########################################
##### Fill in INTRANET credentials ######
#########################################
user = "user.name"
password = "password"
#########################################
browser = webdriver.Firefox()
browser.implicitly_wait(120)
timeout = 600
sleepTimer = 2
global itemId
global currentPage
global itemName
#currentPage = 3

def waitForHomePage():
        try:
            element_present = EC.presence_of_element_located((By.ID, 'ctl00_onetidHeadbnnr2'))
            WebDriverWait(browser, timeout).until(element_present)
        except TimeoutException:
            print ("Timed out waiting for page to load")
            return;

# def selectProductByElementId(itemId):
#     ##### Click specific item from list
#     browser.find_element_by_xpath("(//a[@class='wfs-accessrequestbtn'])["+str(itemId)+"]").click()
#     #and contains(@onclick 'selectDevice')
#     return;

def selectPage(currentPage):
    for page in range (currentPage):
        browser.find_element_by_id('pagingWPQ2next').click()
        sleep(sleepTimer)
#        print("Page:"+str(currentPage))
    return;   
        

def searchItem(itemName):
    sleep(sleepTimer)
##### Click New GSM Request
    browser.get ('http://ecm.app.orange.intra/workflows/gsm/_layouts/15/bws/orange/wfs/gsm/gsminit.aspx') 
    sleep(sleepTimer)
##### Click Select Category - SH
    browser.find_element_by_xpath("//a[@class='wfs-accessrequestbtn' and contains (@onclick,'Second Hand')]").click()
    sleep(sleepTimer)
##### Click S
    browser.find_element_by_id('inplaceSearchDiv_WPQ2_lsinput').click()
    sleep(sleepTimer)   
    browser.find_element_by_id('inplaceSearchDiv_WPQ2_lsinput').send_keys(itemName)
    sleep(sleepTimer)   
    browser.find_element_by_id('inplaceSearchDiv_WPQ2_lsinput').send_keys(Keys.RETURN)
    sleep(sleepTimer)    
    browser.find_element_by_xpath("//a[contains(text(),'Select Device')]").click()
    sleep(sleepTimer)    
    if ("You can create one request per item" in browser.page_source):  # Item already bought ? Increase itemId &moveOn
        return
    ##### Check I confirm
    browser.find_element_by_id('WFS_GSM_SubcategoryConfirmation_7d5e1565-3663-4f0f-b76a-8e9c092e7188_$BooleanField').click()
    sleep(sleepTimer)    
    ##### Submit page
    sleep(sleepTimer)
    browser.find_element_by_xpath("//a[@id='BWS.Orange.WFS.GSM.CustomActionsTab.CustomActionsGroup.StartWorkflow-Large']").click()  
    return

    

def main():

 
    url = "ecm.app.orange.intra/workflows/gsm/SitePages/Home.aspx"
    baseUrl="http://" + user + ":" + password +"@" + url

    browser.get(baseUrl + '/')

    waitForHomePage()

    with open('lista.txt', 'r', encoding='utf-8') as f:
        for itemName in f:
            if itemName.endswith('\n'):
                itemName = itemName[:-1]
            print(itemName)    
            searchItem(itemName)
if __name__ == "__main__":
    main()
