from selenium import webdriver
import time
import FileHandling_3


def scrape(name,firm,browser):
    if(firm.strip()!='ADVANCED MICRO DEVICESINC'):
        browser.switch_to_frame('mainFrame')
    browser.find_element_by_id('terms')
    browser.find_element_by_id('terms').clear()
    browser.find_element_by_id('terms').send_keys(name)
    browser.find_element_by_xpath('//*[@id="srchButt"]').click()
    time.sleep(10)
    try:
        browser.switch_to_default_content()
        browser.switch_to_frame('mainFrame')
        dyn_frame = browser.find_element_by_xpath('//frame[contains(@name, "fr_resultsNav")]')
        framename = dyn_frame.get_attribute('name')
        browser.switch_to_frame(framename)
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="deliveryContainer"]/table/tbody/tr/td[6]/table/tbody/tr/td[1]/table/tbody/tr/td/a[3]/img').click()
        time.sleep(2)
        browser.switch_to_window(browser.window_handles[1])
        browser.find_element_by_xpath('//*[@id="docText"]').click()
        time.sleep(2)
        browser.find_element_by_id("delFmt")
        browser.find_element_by_xpath('//*[@id="delFmt"]/option[4]').click()
        time.sleep(3)
        browser.find_element_by_id("delView")
        browser.find_element_by_xpath('//*[@id="delView"]/option[4]').click()
        browser.find_element_by_xpath('//*[@id="sel"]').click()
        value=browser.find_element_by_xpath('//*[@id="docText"]').text.strip()
        count=value[value.find('-')+1:-1].strip()
        if(int(count)>1000):
            key='501-1000'
        else:
            key='501-'+str(count)
        browser.find_element_by_id('rangetextbox').clear()
        browser.find_element_by_id('rangetextbox').send_keys(key)
        browser.find_element_by_xpath('//*[@id="img_orig_bottom"]/a/img').click()
        time.sleep(20)
        browser.find_element_by_xpath('//*[@id="center"]/center/p/a').click()
        time.sleep(15)
        browser.close()
        browser.switch_to_window(browser.window_handles[0])
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="restoreButtons"]/a[2]').click()
        FileHandling_3.Move(firm.strip())
        time.sleep(5)
    except:
        time.sleep(3)
        browser.switch_to_window(browser.window_handles[0])
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="restoreButtons"]/a[2]').click()
        time.sleep(5)