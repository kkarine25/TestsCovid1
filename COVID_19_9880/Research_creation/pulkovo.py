# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os

from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.support.wait import WebDriverWait


class CreatePulcovo(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_create_pulcovo(self):
        driver = self.driver
        #driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://test.rpn19.ru/business/dashboard/dashboard.xhtml")
        #driver.get("http://127.0.0.1:48080/business/dashboard/dashboard.xhtml")
        #driver.get("https://rpn19.ru:11443/documents/")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("pulkovo@pulkovo.ru")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("pulkovo@pulkovo.ru")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,"#j_idt70 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Создание заявки на исследование 2\"] > span").click()
        driver.find_element(By.CSS_SELECTOR,"#buttonsForm\:createPcr").click()
        time.sleep(3)
        numberIss=driver.find_element(By.ID,"itemForm:number").get_attribute("value")

        #driver.find_element(By.CSS_SELECTOR,
        #    "#itemForm\:tabView\:materialType > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.ID,"itemForm:tabView:materialType_label").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:materialType_items").click()

        driver.find_element(By.ID,"itemForm:tabView:materialType_2").click()
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:tabView:materialDate_input").click()
        driver.find_element(By.ID,"itemForm:tabView:materialDate_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:materialDate_input").send_keys("030820211000")
        #driver.find_element(By.CSS_SELECTOR, "#itemForm\:tabView\:j_id72").click()
        #driver.find_element(By.CSS_SELECTOR,"body.main-body").click()
        driver.find_element(By.ID,"itemForm:tabView:lastName").click()
        driver.find_element(By.ID,"itemForm:tabView:lastName").clear()
        driver.find_element(By.ID,"itemForm:tabView:lastName").send_keys(u"СаблинАнтител")
        driver.find_element(By.ID,"itemForm:tabView:firstName").click()
        driver.find_element(By.ID,"itemForm:tabView:firstName").clear()
        driver.find_element(By.ID,"itemForm:tabView:firstName").send_keys(u"Роман")
        driver.find_element(By.ID,"itemForm:tabView:patronymicName").click()
        driver.find_element(By.ID,"itemForm:tabView:patronymicName").clear()
        driver.find_element(By.ID,"itemForm:tabView:patronymicName").send_keys(u"Евгеньевич")
        driver.find_element(By.CSS_SELECTOR,
            "#itemForm\:tabView\:sex > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.ID,"itemForm:tabView:birthDate_input").click()
        driver.find_element(By.ID,"itemForm:tabView:birthDate_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:birthDate_input").send_keys("08.08.1999")
        driver.find_element(By.CSS_SELECTOR, "body.main-body").click()
        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()
        driver.find_element(By.ID,"itemForm:tabView:email").click()
        driver.find_element(By.ID,"itemForm:tabView:email").clear()
        driver.find_element(By.ID,"itemForm:tabView:email").send_keys("shamkin@proweb.ru")
        driver.find_element(By.ID,"itemForm:tabView:phone").click()
        driver.find_element(By.ID,"itemForm:tabView:phone").clear()
        driver.find_element(By.ID,"itemForm:tabView:phone").send_keys("+7(812)123-12-12")
        driver.find_element(By.ID,"itemForm:tabView:snils").click()
        driver.find_element(By.ID,"itemForm:tabView:snils").clear()
        driver.find_element(By.ID,"itemForm:tabView:snils").send_keys("78945212399")
        driver.find_element(By.ID,"itemForm:tabView:polisOmsSeria").click()
        driver.find_element(By.ID,"itemForm:tabView:polisOmsSeria").clear()
        driver.find_element(By.ID,"itemForm:tabView:polisOmsSeria").send_keys("745631")
        driver.find_element(By.ID,"itemForm:tabView:polisOmsNumber").click()
        driver.find_element(By.ID,"itemForm:tabView:polisOmsNumber").clear()
        driver.find_element(By.ID,"itemForm:tabView:polisOmsNumber").send_keys("147856")
        driver.find_element(By.ID,"itemForm:tabView:city_input").click()
        driver.find_element(By.ID,"itemForm:tabView:city_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:city_input").send_keys(u"Ярославль"+Keys.TAB)
        #driver.find_element(By.XPATH,"//span[@id='itemForm:tabView:city_panel']/ul[1]/li[1]/span").click()
        driver.find_element(By.ID,"itemForm:tabView:homeAddressStreet_input").click()
        driver.find_element(By.ID,"itemForm:tabView:homeAddressStreet_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:homeAddressStreet_input").send_keys(u"Мира")
        driver.find_element(By.ID,"itemForm:tabView:homeAddressBuilding_input").click()
        driver.find_element(By.ID,"itemForm:tabView:homeAddressBuilding_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:homeAddressBuilding_input").send_keys("1")
        time.sleep(2)

        driver.find_element(By.ID,"itemForm:tabView:homeAddressFlat").click()
        driver.find_element(By.ID,"itemForm:tabView:homeAddressFlat").clear()
        driver.find_element(By.ID,"itemForm:tabView:homeAddressFlat").send_keys("18")

        driver.find_element(By.ID,"itemForm:tabView:orgName").clear()
        driver.find_element(By.ID,"itemForm:tabView:orgName").send_keys(u"Институт")
        driver.find_element(By.ID,"itemForm:tabView:workAddressStreet_input").click()
        driver.find_element(By.ID,"itemForm:tabView:workAddressStreet_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:workAddressStreet_input").send_keys(u"Мира")
        driver.find_element(By.ID,"itemForm:tabView:workAddressBuilding_input").click()
        driver.find_element(By.ID,"itemForm:tabView:workAddressBuilding_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:workAddressBuilding_input").send_keys("24")
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:tabView:patientCategory").click()
        driver.find_element(By.ID,"itemForm:tabView:patientCategory_label").click()
        driver.find_element(By.ID,"itemForm:tabView:patientCategory_2").click()
        driver.find_element(By.ID,"itemForm:tabView:sender").click()
        driver.find_element(By.ID,"itemForm:tabView:sender").clear()
        driver.find_element(By.ID,"itemForm:tabView:sender").send_keys(u"Иванов И.И.")
        driver.find_element(By.ID,"itemForm:tabView:arrivalDate_input").click()
        driver.find_element(By.ID,"itemForm:tabView:arrivalDate_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:arrivalDate_input").send_keys("20.11.2020")
        #driver.find_element(By.CSS_SELECTOR, "body.main-body").click()
        driver.find_element(By.ID,"itemForm:tabView:departureCountry").click()
        driver.find_element(By.ID,"itemForm:tabView:departureCountry_label").click()
        #driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:departureCountry_items").click()
        driver.find_element(By.ID,"itemForm:tabView:departureCountry_2").click()
        driver.find_element(By.ID,"itemForm:tabView:flightNumber").click()
        driver.find_element(By.ID,"itemForm:tabView:flightNumber").clear()
        driver.find_element(By.ID,"itemForm:tabView:flightNumber").send_keys(u"74ке")
        driver.find_element(By.ID,"itemForm:tabView:issueDate_input").click()
        driver.find_element(By.ID,"itemForm:tabView:issueDate_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:issueDate_input").send_keys("22.02.2021")
        driver.find_element(By.ID,"itemForm:tabView:flightNumber").click()
        driver.find_element(By.ID,"itemForm:tabView:description").click()
        driver.find_element(By.ID,"itemForm:tabView:description").clear()
        driver.find_element(By.ID,"itemForm:tabView:description").send_keys(u"Нет")
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        element = driver.find_element(By.ID, "itemForm:j_id5")
        driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:j_id5").click()
        driver.find_element(By.CSS_SELECTOR,"div > div > div.ui-growl-message > p")
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:j_id4").click()
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR,
            "#j_idt71 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Поиск исследований\"] > span").click()
        driver.find_element(By.ID,"filtersForm:j_idt79:j_idt105").click()
        driver.find_element(By.ID,"filtersForm:j_idt79:j_idt105").clear()
        driver.find_element(By.ID,"filtersForm:j_idt79:j_idt105").send_keys(numberIss)

        driver.find_element(By.ID,"filtersForm:j_idt211").click()
        time.sleep(15)
        driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        #driver.find_element(By.XPATH,"//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(1) + "]").click()
        wait = WebDriverWait(driver, 10)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles
        actionChains = ActionChains(driver)
        actionChains.double_click(driver.find_element(By.XPATH,"//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(1) + "]")).perform()
        time.sleep(2)
        wait.until(ec.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        driver.find_element(By.ID,"itemForm:j_id4")



