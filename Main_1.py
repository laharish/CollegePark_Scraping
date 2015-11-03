import Scraping_2
from selenium import webdriver
import time
import regex as re


path_to_chromedriver = 'F:/Technical/Python/chromedriver_win32/chromedriver.exe'


browser = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'http://proxy.lib.iastate.edu/login?url=http://proxy.lib.iastate.edu/login?url=http://www.lexisnexis.com/us/lnacademic'
browser.get(url)
time.sleep(5)
init_date='01/01/2002'
fin_date='12/31/2008'
time.sleep(35)
browser.switch_to_frame('mainFrame')
browser.find_element_by_xpath('//*[@id="lblAdvancDwn"]').click()
time.sleep(2)
browser.find_element_by_id('txtFrmDate').clear()
browser.find_element_by_id('txtFrmDate').send_keys(init_date)
browser.find_element_by_id('txtToDate').clear()
browser.find_element_by_id('txtToDate').send_keys(fin_date)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="OkButt"]').click()


indicies = "(((#ST000CP97# and (PRODUCT PRICING #80PLUS#)))) OR (((#ST00096SW# and (PRODUCT PROMOTION #80PLUS#)))) OR (((#ST0009WXX# and (PRODUCT ENHANCEMENTS #80PLUS#)))) OR (((#ST000DG3K# and (DISRUPTIVE INNOVATION #80PLUS#)))) OR (((#ST000A4IH# and (PRODUCT INNOVATION #80PLUS#)))) OR (((#ST00096SV# and (PRODUCT DEVELOPMENT #80PLUS#)))) OR (((#STX001211# and (NEW PRODUCTS #80PLUS#)))) OR (((#STX001083# and (MARKETING ADVERTISING EXPENDITURE #80PLUS#)))) OR (((#STX001654# and (SUPPLY CHAIN MANAGEMENT #80PLUS#)))) OR (((#STX001978# and (BUSINESS EXPANSION #80PLUS#)))) OR (((#ST000DF2W# and (NEW MANUFACTURING FACILITIES #80PLUS#))))"

with open('F:/College Park/More Than 500.txt') as file:
    for firm in file:
        query=firm.strip()+" AND "+indicies
        Scraping_2.scrape(query, re.sub('[^A-Za-z0-9]+ ', '', firm[firm.strip().find('and') + 5:firm.strip().find('#80')]), browser)
