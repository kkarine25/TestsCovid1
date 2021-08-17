# -*- coding: utf-8 -*-
import glob
#COV-1010 Не выгружаются адреса в отчет /reports/covid-research-by-institution

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os
from openpyxl import load_workbook

class CovidResearchByInstitutionNew(unittest.TestCase):
    def setUp(self):
        download_dir = "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\COVID_19_9880\\otchet\\downloads_exel"
        chrome_options = webdriver.ChromeOptions()
        preferences = {"download.default_directory": download_dir,
                       "directory_upgrade": True,
                       "safebrowsing.enabled": True}
        chrome_options.add_experimental_option("prefs", preferences)
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe", options=chrome_options)
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True

        '''
        options = webdriver.ChromeOptions()
        #options.add_argument()
        pathdow ='C:/Users/user/PycharmProjects/TestsCovid1/COVID_19_9880/Filling_Lab_Tablets/downloads_exel'



        #self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True
        '''

        '''    
        def genlog(self):    
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        if not os.path.exists("Logs"):
            os.mkdir("Logs")
        handler = logging.FileHandler(str('logs/' + (time.strftime(''%d.%m.%Y_%H.%M_'', (time.localtime())))  + 'lab_planshet_1.log'))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        try:
            self.lab_planshet()
        except Exception as e:
            logger.error('Error detected', exc_info=True)
        else:
            logger.info('Test complete without errors')    

    def test_lab_planshet(self):
        self.genlog()
    '''

    def test_covid_research_by_institution_new(self):
        driver = self.driver
        #driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://auraep.ru:9880/business/dashboard/dashboard.xhtml#")
        # driver.get("https://rpn19.ru:11443/documents/")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("supervisor")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("Ivwdk1Rp")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_css_selector(
            "#j_idt66 > div.nano.layout-tabmenu-nav > ul > li:nth-child(13) > a > div").click()
        driver.find_element_by_id("reportsForm:j_idt75:2:j_idt77").click()

        #фильтры
        driver.find_element_by_id("buildForm:j_idt76_input").click()
        driver.find_element_by_id("buildForm:j_idt76_input").clear()
        for date in "1202.80.10":
            driver.find_element_by_id("buildForm:j_idt76_input").send_keys(Keys.HOME, date)
        driver.find_element_by_id("buildForm:j_idt78_input").click()
        driver.find_element_by_id("buildForm:j_idt78_input").clear()
        for date in "1202.80.61":
            driver.find_element_by_id("buildForm:j_idt78_input").send_keys(Keys.HOME, date)

        driver.find_element_by_id("buildForm:j_idt79").click()
        time.sleep(2)
        #driver.find_element_by_id("buildForm:j_idt79_label").click()
        driver.find_element_by_css_selector("#buildForm\:j_idt79_panel").click()
        time.sleep(5)
        driver.find_element_by_css_selector(
            "#buildForm\:j_idt79_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(987) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        # driver.find_element_by_css_selector("#buildForm\:j_idt79_panel").click()
        #driver.find_element_by_css_selector(
        #    "#buildForm\:j_idt79_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(81) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()

        driver.find_element_by_id("buildForm:j_idt81").click()
        # driver.find_element_by_id("buildForm:j_idt79_label").click()
        driver.find_element_by_css_selector("#buildForm\:j_idt81_panel").click()
        driver.find_element_by_css_selector(
            "#buildForm\:j_idt81_panel > div.ui-widget-header.ui-corner-all.ui-selectcheckboxmenu-header.ui-helper-clearfix > div.ui-chkbox.ui-widget > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default.ui-state-active > span").click()
        driver.find_element_by_css_selector(
            "#buildForm\:j_idt81_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(4) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector("body").click()
        driver.find_element_by_id("buildForm:j_idt91").click()
        time.sleep(3)

        assert (driver.find_element_by_id("dataForm:j_idt96").text == "01.08.2021 00:00 - 16.08.2021 23:59")
        assert (driver.find_element_by_id("dataForm:j_idt98").text == "Определение наличия РНК SARS-CoV-2")
        assert (driver.find_element_by_id("dataForm:j_idt100").text == "Набор реагентов для выявления РНК коронавируса SARS-CoV-2 методом ОТ-ПЦР в режиме реального времени \"РеалБест РНК SARS-CoV-2\"")
        assert (driver.find_element_by_id("dataForm:j_idt158").text == "23")

        driver.find_element_by_id("buildForm:j_idt92").click()
        time.sleep(3)

        rootpath = 'C:\\Users\\user\\PycharmProjects\\TestsCovid1\\COVID_19_9880\\otchet\\downloads_exel'
        filelist = [os.path.join(rootpath, f) for f in os.listdir(rootpath)]
        filelist = [f for f in filelist if os.path.isfile(f)]
        newest = max(filelist, key=lambda x: os.stat(x).st_mtime)

        wb = load_workbook(newest)
        sheet_ranges = wb['1']
        str1 = sheet_ranges['A21'].value
        str2 = sheet_ranges['A48'].value


        assert (str1 == "Учреждение, направившее материал: ПАО \"Сбербанк\" (Ветеранов 114 корпус 1)")
        assert (str2 == "Учреждение, направившее материал: Администрация Адмиралтейского района Санкт-Петербурга")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
