import time
from selenium import webdriver


def start(username, password):
        driver = webdriver.Chrome()
        driver.get('http://jxpj.hlju.edu.cn/index.php?c=index&a=pager&id=43&kcdm=1412016281&kcxh=02&zgh=2009002&term=2020-2021-2')
        driver.implicitly_wait(10)
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("password").send_keys(password)
        time.sleep(1)
        driver.find_element_by_id("dlan").click()
        driver.find_element_by_link_text("学习体验调查与评教").click()
        counts_pingke = len(driver.find_elements_by_xpath(
            "/html/body/div[4]/div[2]/table/tbody/tr[*]/td[8]/a"))
        for pingke in range(counts_pingke):
            pingkes = driver.find_elements_by_xpath(
                "/html/body/div[4]/div[2]/table/tbody/tr[*]/td[8]/a")
            pingkes[pingke].click()
            driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[2]/div[1]/div/ins").click()
            driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[4]/div[1]/div/ins").click()
            driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[6]/div[1]/div/ins").click()
            driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[8]/div[2]/div/ins").click()
            driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[10]/div[1]/div/ins").click()
            driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[12]/div[1]/div/ins").click()
            driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[14]/div[1]/div/ins").click()
            driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[16]/div[2]/div/ins").click()
            driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[18]/div[1]/div/ins").click()
            driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[20]/textarea").send_keys('非常满意')
            driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[22]/textarea").send_keys('不需要改进')
            driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[23]/input[1]").click()
            driver.find_element_by_xpath("/html/body/div[5]/div/input[1]").click()
