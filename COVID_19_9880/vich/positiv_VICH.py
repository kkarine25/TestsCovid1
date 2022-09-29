# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import random
import string


class Vich2(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True

    def generate_random_cel(self):
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        rand_cel = ''.join(random.choice(numbers) for i in range(10))
        return rand_cel


    def test_vich2(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1920,937 | ]]
        driver.get("http://test.rpn19.ru/business/dashboard/dashboard.xhtml#")
        #driver.get("http://127.0.0.1:48080/business/dashboard/dashboard.xhtml")
        driver.find_element(By.ID, "form:usernameInput").click()
        driver.find_element(By.ID, "form:usernameInput").clear()
        driver.find_element(By.ID, "form:usernameInput").send_keys("a.yakovenko@webdom.net")
        driver.find_element(By.ID, "form:passwordInput").click()
        driver.find_element(By.ID, "form:passwordInput").clear()
        driver.find_element(By.ID, "form:passwordInput").send_keys("dBE<9HFC")
        driver.find_element(By.CSS_SELECTOR, "span.ui-button-text.ui-c").click()
        # Копируем номер штрихкода
        driver.find_element(By.CSS_SELECTOR,
                            "#j_idt70 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(9) > a > div").click()
        driver.find_element(By.CSS_SELECTOR, u"a[title=\"Сертификаты ВИЧ\"] > span").click()
        driver.find_element(By.ID, "tableForm:main-table:j_id17").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#tableForm\:main-table\:j_id17_panel > div.ui-widget-header.ui-corner-all.ui-selectcheckboxmenu-header.ui-helper-clearfix > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#tableForm\:main-table\:j_id17_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(1) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_elements(By.CSS_SELECTOR,
                             "#tableForm\:main-table_paginator_bottom > a.ui-paginator-last.ui-state-default.ui-corner-all")[
            -1].click()
        time.sleep(3)
        if driver.find_element(By.XPATH, "//*[@id='tableForm:main-table_data']/tr[1]/td[7]").text != "":
            x = driver.find_element(By.XPATH, "//*[@id='tableForm:main-table_data']/tr[2]/td[1]").text
        else:
            x = driver.find_element(By.XPATH, "//*[@id='tableForm:main-table_data']/tr[1]/td[1]").text
        driver.find_element(By.CSS_SELECTOR,
                            "#j_idt71 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(6) > a > div").click()
        driver.find_element(By.CSS_SELECTOR, u"a[title=\"Создание заявки на исследование 2\"] > span").click()
        q=self.generate_random_cel()

        driver.find_element(By.XPATH, "//button[@id='buttonsForm:createAids']/span").click()
        y=driver.find_element(By.ID, "itemForm:number").get_attribute("value")
        driver.find_element(By.ID, "itemForm:tabView:lastName").click()
        driver.find_element(By.ID, "itemForm:tabView:lastName").clear()
        driver.find_element(By.ID, "itemForm:tabView:lastName").send_keys(q)

        driver.find_element(By.ID, "itemForm:tabView:firstName").clear()
        driver.find_element(By.ID, "itemForm:tabView:firstName").send_keys(u"Иван")
        driver.find_element(By.ID, "itemForm:tabView:patronymicName").clear()
        driver.find_element(By.ID, "itemForm:tabView:patronymicName").send_keys(u"Петрович")
        driver.find_element(By.ID, "itemForm:tabView:birthDate_input").click()
        driver.find_element(By.ID, "itemForm:tabView:birthDate_input").clear()
        driver.find_element(By.ID, "itemForm:tabView:birthDate_input").send_keys("12.03.1989")
        driver.find_element(By.CSS_SELECTOR, "body.main-body").click()
        driver.find_element(By.ID, "itemForm:tabView:sex").click()
        driver.find_element(By.XPATH, "//table[@id='itemForm:tabView:j_id52']/tbody/tr[3]/td[3]").click()
        driver.find_element(By.XPATH, "//*[@id='itemForm:tabView:sex']/tbody/tr/td[1]/div/div[2]/span").click()
        # driver.find_element(By.CSS_SELECTOR,"div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default.ui-state-hover > span.ui-radiobutton-icon.ui-icon.ui-icon-blank.ui-c").click()
        # driver.find_element(By.CSS_SELECTOR,"div.ui-selectonemenu-trigger.ui-state-default.ui-corner-right.ui-state-hover > span.ui-icon.ui-icon-triangle-1-s.ui-c").click()
        driver.execute_script("window.scrollTo(0, window.scrollY + 1400)")
        driver.find_element(By.ID, "itemForm:tabView:patientCategory").click()
        driver.find_element(By.ID, "itemForm:tabView:patientCategory_label").click()
        driver.find_element(By.ID, "itemForm:tabView:patientCategory_2").click()
        window_before = driver.window_handles[0]
        driver.find_element(By.ID, "itemForm:tabView:sendInstitution_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(2)
        driver.find_element(By.ID, "tableForm:main-table:j_id10").click()
        driver.find_element(By.ID, "tableForm:main-table:j_id10").clear()
        driver.find_element(By.ID, "tableForm:main-table:j_id10").send_keys(u"един" + Keys.ENTER)
        driver.find_element(By.CSS_SELECTOR, "#tableForm").click()
        time.sleep(2)
        # driver.find_element(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(1)").click()
        driver.find_element(By.XPATH, "//td[contains(text(), '13 092')]").click()
        time.sleep(2)
        driver.find_element(By.ID, "tableForm:choose").click()
        driver.switch_to.window(window_before)
        driver.execute_script("window.scrollTo(0, window.scrollY - 1400)")
        driver.find_element(By.XPATH, "//button[@id='itemForm:j_id5']").click()
        time.sleep(5)
        # driver.find_element(By.CSS_SELECTOR, "itemForm\:tabView > ul > li.ui-tabs-header.ui-state-default.ui-corner-top.ui-tabs-selected.ui-state-active > a").click()
        driver.find_element(By.XPATH, "//div[@id='itemForm:tabView']/ul/li[6]").click()
        driver.find_element(By.ID, "itemForm:tabView:aidsDensity1_input").click()
        driver.find_element(By.ID, "itemForm:tabView:aidsDensity1_input").clear()
        driver.find_element(By.ID, "itemForm:tabView:aidsDensity1_input").send_keys("1,0000")
        driver.find_element(By.ID, "itemForm:tabView:aidsPositivity1_input").click()
        driver.find_element(By.ID, "itemForm:tabView:aidsPositivity1_input").clear()
        driver.find_element(By.ID, "itemForm:tabView:aidsPositivity1_input").send_keys("2,0000")
        driver.find_element(By.ID, "itemForm:tabView:aidsResult1_label").click()
        driver.find_element(By.ID, "itemForm:tabView:aidsResult1_1").click()
        driver.find_element(By.XPATH, "//button[@id='itemForm:j_id5']/span").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='itemForm:j_id4']/span").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#j_idt71 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(6) > a > div").click()
        driver.find_element(By.CSS_SELECTOR, u"a[title=\"Поиск исследований\"] > span").click()
        driver.find_element(By.ID, "filtersForm:j_idt79:j_idt105").click()
        driver.find_element(By.ID, "filtersForm:j_idt79:j_idt105").clear()
        driver.find_element(By.ID, "filtersForm:j_idt79:j_idt105").send_keys(y)
        driver.find_element(By.XPATH, "//button[@id='filtersForm:j_idt211']/span").click()

        wait = WebDriverWait(driver, 10)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles
        actionChains = ActionChains(driver)
        actionChains.double_click(driver.find_element(By.XPATH, "//tbody[@id='tableForm:main-table_data']/tr/td[2]")).perform()
        wait.until(ec.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        driver.find_element(By.CSS_SELECTOR, "body.main-body").click()

        driver.find_element(By.XPATH, "//div[@id='itemForm:tabView']/ul/li[6]").click()
        driver.find_element(By.ID, "itemForm:tabView:aidsDensity2_input").click()
        driver.find_element(By.ID, "itemForm:tabView:aidsDensity2_input").clear()
        driver.find_element(By.ID, "itemForm:tabView:aidsDensity2_input").send_keys("1,0000")
        driver.find_element(By.ID, "itemForm:tabView:aidsPositivity2_input").click()
        driver.find_element(By.ID, "itemForm:tabView:aidsPositivity2_input").clear()
        driver.find_element(By.ID, "itemForm:tabView:aidsPositivity2_input").send_keys("2,0000")
        driver.find_element(By.ID, "itemForm:tabView:aidsResult2_label").click()
        driver.find_element(By.ID, "itemForm:tabView:aidsResult2_1").click()
        driver.find_element(By.XPATH, "//button[@id='itemForm:j_id5']/span").click()
        time.sleep(3)
        driver.refresh()
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[@id='itemForm:tabView:aidsControlResult']/div[3]").click()
        driver.find_element(By.ID, "itemForm:tabView:aidsControlResult_1").click()
        driver.find_element(By.XPATH, "//button[@id='itemForm:j_id5']/span").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='itemForm:j_id4']/span").click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,
                            "#j_idt71 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(9) > a > div").click()
        driver.find_element(By.CSS_SELECTOR, u"a[title=\"Положительные исследования ВИЧ\"] > span").click()
        driver.find_element(By.ID, "filtersForm:j_idt100").click()
        driver.find_element(By.ID, "filtersForm:j_idt100").clear()
        driver.find_element(By.ID, "filtersForm:j_idt100").send_keys(q)

        driver.find_element(By.ID, "filtersForm:j_idt103").clear()
        driver.find_element(By.ID, "filtersForm:j_idt103").send_keys(u"иван")
        driver.find_element(By.ID, "filtersForm:j_idt106").clear()
        driver.find_element(By.ID, "filtersForm:j_idt106").send_keys(u"петрович")
        driver.find_element(By.XPATH, "//*[@id='filtersForm:j_idt89']/div[2]").click()
        driver.find_element(By.XPATH, "//button[@id='filtersForm:j_idt121']/span").click()
        time.sleep(20)
        assert driver.find_element(By.XPATH,
                                   "//*[@id='filtersForm:resultTable_data']/tr[1]/td[1]").text == y

if __name__ == "__main__":
    unittest.main()
