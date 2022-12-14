# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import unittest, time
import random
class Vich(unittest.TestCase):
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
        rand_cel = ''.join(random.choice(numbers) for i in range(13))
        return rand_cel

    def test_vich(self):
        driver = self.driver
        number=self.generate_random_cel()
        driver.get("http://test.rpn19.ru/business/dashboard/dashboard.xhtml")
        #driver.get("http://127.0.0.1:48080/business/dashboard/dashboard.xhtml")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("a.yakovenko@webdom.net")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("dBE<9HFC")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#j_idt70 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(9) > a > div").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Сертификаты ВИЧ\"] > span").click()
        driver.find_element(By.XPATH,"//button[@id='tableForm:j_idt82']/span").click()
        time.sleep(2)
        driver.find_element(By.ID,"bsoIncomeForm:firstBarcode").clear()
        driver.find_element(By.ID,"bsoIncomeForm:firstBarcode").send_keys(number)
        driver.find_element(By.ID,"bsoIncomeForm:lastBarcode").click()
        driver.find_element(By.ID,"bsoIncomeForm:lastBarcode").clear()
        driver.find_element(By.ID,"bsoIncomeForm:lastBarcode").send_keys(int(number)+10)
        driver.find_element(By.ID,"bsoIncomeForm:incomeDate_input").click()
        driver.find_element(By.ID, "bsoIncomeForm:incomeDate_input").send_keys("18.03.2020")
        driver.find_element(By.ID, "bsoIncomeForm:firstBarcode").click()
        driver.find_element(By.XPATH,"//button[@id='bsoIncomeForm:j_idt108']/span").click()
        driver.find_element(By.XPATH,"//button[@id='bsoIncomeForm:j_idt107']/span").click()
        time.sleep(2)
        driver.find_element(By.ID,"tableForm:main-table:j_id10").click()
        driver.find_element(By.ID,"tableForm:main-table:j_id10").clear()
        driver.find_element(By.ID,"tableForm:main-table:j_id10").send_keys(number+ Keys.ENTER)
        time.sleep(2)
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']/tr[" + str(1) + "]/td[" + str(1) + "]").text == number

if __name__ == "__main__":
    unittest.main()
