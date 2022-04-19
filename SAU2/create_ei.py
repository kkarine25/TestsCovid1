# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time
import random
import string
import datetime

class CreateEi(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True

    def generate_random_string(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(8))
        return rand_string
    
    def test_create_ei(self):
        driver = self.driver
        driver.get("http://sau.rpn19.ru:11080/business/dashboard/dashboard.xhtml#")
        now = datetime.datetime.now()
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("borisova@webdom.net")
        driver.find_element_by_id("form:passwordInput").send_keys("cudEJkKl")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_xpath("//div[@id='j_idt70']/div/ul/li[5]/a/div/div[2]").click()
        driver.find_element_by_link_text(u"Сформировать экстренное извещение").click()
        driver.find_element_by_id("searchForm:j_idt82_input").click()
        driver.find_element_by_id("searchForm:j_idt82_input").clear()
        driver.find_element_by_id("searchForm:j_idt82_input").send_keys(self.generate_random_string())
        driver.find_element_by_id("searchForm:j_idt85_input").click()
        driver.find_element_by_id("searchForm:j_idt85_input").clear()
        driver.find_element_by_id("searchForm:j_idt85_input").send_keys(u"Динозавр")
        driver.find_element_by_id("searchForm:j_idt88_input").click()
        driver.find_element_by_id("searchForm:j_idt88_input").clear()
        driver.find_element_by_id("searchForm:j_idt88_input").send_keys(u"Динозаврович")
        driver.find_element_by_id("searchForm:dateFrom_input").click()
        driver.find_element_by_id("searchForm:dateFrom_input").clear()
        driver.find_element_by_id("searchForm:dateFrom_input").send_keys("14.09.1999")
        driver.find_element_by_xpath("//button[@id='searchForm:j_idt93']/span").click()
        driver.find_element_by_css_selector("a > span.ui-button-text.ui-c").click()
        driver.find_element_by_css_selector("span.ui-radiobutton-icon.ui-icon.ui-icon-blank.ui-c").click()
        driver.find_element_by_id("j_idt78:j_idt97:inn").click()
        driver.find_element_by_id("j_idt78:j_idt97:inn").clear()
        driver.find_element_by_id("j_idt78:j_idt97:inn").send_keys("111235")
        driver.find_element_by_id("j_idt78:j_idt97:snils").click()
        driver.find_element_by_id("j_idt78:j_idt97:snils").clear()
        driver.find_element_by_id("j_idt78:j_idt97:snils").send_keys("698-541-233 33")
        driver.find_element_by_id("j_idt78:j_idt97:addressesTableList_table_buttons_panel").click()
        driver.find_element_by_xpath("//button[@id='j_idt78:j_idt97:tf_addressesTableList_add']/span[2]").click()
        driver.find_element_by_id("tableFieldItemForm:city_input").click()
        driver.find_element_by_xpath("//table[@id='tableFieldItemForm:tableFieldPanel']/tbody/tr[4]/td").click()
        driver.find_element_by_id("tableFieldItemForm:city_input").click()
        driver.find_element_by_id("tableFieldItemForm:city_input").clear()
        driver.find_element_by_id("tableFieldItemForm:city_input").send_keys(u"г. Санкт-Петербург"+Keys.TAB)
        #driver.find_element_by_xpath("//span[@id='tableFieldItemForm:city_panel']/ul/li").click()
        driver.find_element_by_id("tableFieldItemForm:j_idt203_content").click()
        driver.find_element_by_id("tableFieldItemForm:cityArea_label").click()
        driver.find_element_by_id("tableFieldItemForm:cityArea_filter").clear()
        driver.find_element_by_id("tableFieldItemForm:cityArea_filter").send_keys(u"Васи")
        time.sleep(2)
        driver.find_element_by_id("tableFieldItemForm:cityArea_3").click()
        time.sleep(2)
        driver.find_element_by_id("tableFieldItemForm:planningStructureElement").click()
        driver.find_element_by_id("tableFieldItemForm:planningStructureElement").clear()
        driver.find_element_by_id("tableFieldItemForm:planningStructureElement").send_keys("1")
        driver.find_element_by_id("tableFieldItemForm:street_input").click()
        #driver.find_element_by_xpath("//table[@id='tableFieldItemForm:tableFieldPanel']/tbody/tr[7]/td").click()
        driver.find_element_by_id("tableFieldItemForm:street_input").click()
        driver.find_element_by_id("tableFieldItemForm:street_input").clear()
        driver.find_element_by_id("tableFieldItemForm:street_input").send_keys(u"1-я В.О. линия"+Keys.TAB)
        driver.find_element_by_id("tableFieldItemForm:j_idt203_content").click()
        #time.sleep(2)
        #driver.find_element_by_xpath("//span[@id='tableFieldItemForm:street_panel']/ul/li").click()
        driver.find_element_by_id("tableFieldItemForm:house_input").click()
        driver.find_element_by_id("tableFieldItemForm:house_input").clear()
        driver.find_element_by_id("tableFieldItemForm:house_input").send_keys("10")
        #driver.find_element_by_xpath("//span[@id='tableFieldItemForm:house_panel']/ul/li").click()
        driver.find_element_by_id("tableFieldItemForm:flat").click()
        driver.find_element_by_id("tableFieldItemForm:flat").clear()
        driver.find_element_by_id("tableFieldItemForm:flat").send_keys("1")
        driver.find_element_by_id("tableFieldItemForm:comment").click()
        driver.find_element_by_id("tableFieldItemForm:comment").clear()
        driver.find_element_by_id("tableFieldItemForm:comment").send_keys(u"Динозаврик")
        driver.find_element_by_xpath("//button[@id='tableFieldItemForm:j_idt205']/span").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[@id='j_idt78:j_idt97:tf_contactTableList_add']/span[2]").click()
        driver.find_element_by_id("tableFieldItemForm:data").click()
        driver.find_element_by_id("tableFieldItemForm:data").clear()
        driver.find_element_by_id("tableFieldItemForm:data").send_keys("+77777777777")
        driver.find_element_by_id("tableFieldItemForm:comments").click()
        driver.find_element_by_id("tableFieldItemForm:comments").clear()
        driver.find_element_by_id("tableFieldItemForm:comments").send_keys(u"Але, Динозаврик")
        driver.find_element_by_xpath("//button[@id='tableFieldItemForm:j_idt205']/span").click()
        driver.find_element_by_xpath("//button[@id='j_idt78:j_idt97:tf_identityDocumentsTableList_add']/span[2]").click()
        driver.find_element_by_id("tableFieldItemForm:identityDocumentsType_label").click()
        time.sleep(1)
        driver.find_element_by_id("tableFieldItemForm:identityDocumentsType_7").click()
        driver.find_element_by_id("tableFieldItemForm:series").click()
        driver.find_element_by_id("tableFieldItemForm:series").clear()
        driver.find_element_by_id("tableFieldItemForm:series").send_keys("7777")
        driver.find_element_by_id("tableFieldItemForm:identityDocumentsNumber").click()
        driver.find_element_by_id("tableFieldItemForm:identityDocumentsNumber").clear()
        driver.find_element_by_id("tableFieldItemForm:identityDocumentsNumber").send_keys("888888")
        driver.find_element_by_id("tableFieldItemForm:issuedBy").click()
        driver.find_element_by_id("tableFieldItemForm:issuedBy").clear()
        driver.find_element_by_id("tableFieldItemForm:issuedBy").send_keys(u"УФМС Динозавриков")
        driver.find_element_by_id("tableFieldItemForm:issuedDate_input").click()
        driver.find_element_by_id("tableFieldItemForm:issuedDate_input").clear()
        driver.find_element_by_id("tableFieldItemForm:issuedDate_input").send_keys("10.01.2000")
        driver.find_element_by_id("tableFieldItemForm:issuedCode").click()
        driver.find_element_by_id("tableFieldItemForm:issuedCode").clear()
        driver.find_element_by_id("tableFieldItemForm:issuedCode").send_keys("554-444")
        driver.find_element_by_id("tableFieldItemForm:validity_input").click()
        driver.find_element_by_id("tableFieldItemForm:validity_input").clear()
        driver.find_element_by_id("tableFieldItemForm:validity_input").send_keys("10.01.2045")
        driver.find_element_by_xpath("//button[@id='tableFieldItemForm:j_idt205']/span").click()
        driver.find_element_by_link_text(u"Регистрирующее учреждение").click()
        driver.find_element_by_id("j_idt78:j_idt97:dateStartDisease_input").click()
        driver.find_element_by_id("j_idt78:j_idt97:dateStartDisease_input").clear()
        driver.find_element_by_id("j_idt78:j_idt97:dateStartDisease_input").send_keys("01.02.2022")
        #driver.find_element_by_id("j_idt78:j_idt97:j_id82_content").click()
        driver.find_element_by_link_text(u"Место работы/учёбы").click()
        driver.find_element_by_xpath("//button[@id='j_idt78:j_idt97:tf_jobsTable_add']/span[2]").click()
        driver.find_element_by_id("tableFieldItemForm2:socialStatus_label").click()
        driver.find_element_by_id("tableFieldItemForm2:socialStatus_2").click()
        time.sleep(1)
        driver.find_element_by_id("tableFieldItemForm2:j_idt207").click()
        window_before = driver.window_handles[0]
        driver.find_element_by_id("tableFieldItemForm2:orgName_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(2)
        driver.find_element_by_id("tableForm:main-table:j_id13").click()
        driver.find_element_by_id("tableForm:main-table:j_id13").clear()
        driver.find_element_by_id("tableForm:main-table:j_id13").send_keys(
            u"Евангелическо-Лютеранская церковь" + Keys.ENTER)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#tableForm\:main-table_data > tr > td:nth-child(1)").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(3)
        driver.find_element_by_id("tableFieldItemForm2:orgCategory_label").click()
        driver.find_element_by_id("tableFieldItemForm2:orgCategory_1").click()
        driver.find_element_by_id("tableFieldItemForm2:organizationsTypes_label").click()
        driver.find_element_by_id("tableFieldItemForm2:organizationsTypes_1").click()
        driver.find_element_by_id("tableFieldItemForm2:region_label").click()
        driver.find_element_by_id("tableFieldItemForm2:region_1").click()
        driver.find_element_by_id("tableFieldItemForm2:office").click()
        driver.find_element_by_id("tableFieldItemForm2:office").clear()
        driver.find_element_by_id("tableFieldItemForm2:office").send_keys("1")
        driver.find_element_by_id("tableFieldItemForm2:lastVisitedDate_input").click()
        driver.find_element_by_id("tableFieldItemForm2:lastVisitedDate_input").clear()
        driver.find_element_by_id("tableFieldItemForm2:lastVisitedDate_input").send_keys("19.03.2022")
        driver.find_element_by_id("tableFieldItemForm2:comment").click()
        driver.find_element_by_id("tableFieldItemForm2:comment").clear()
        driver.find_element_by_id("tableFieldItemForm2:comment").send_keys(u"Динозаврики тоже работают")
        driver.find_element_by_xpath("//button[@id='tableFieldItemForm2:saveTableButton2']/span").click()
        driver.find_element_by_link_text(u"Диагнозы").click()
        driver.find_element_by_id("j_idt78:j_idt97:conditionSeverity_label").click()
        driver.find_element_by_id("j_idt78:j_idt97:conditionSeverity_1").click()
        driver.find_element_by_css_selector("span.ui-chkbox-icon.ui-icon.ui-icon-blank.ui-c").click()
        driver.find_element_by_xpath("//button[@id='j_idt78:j_idt97:tf_diagnosesTable_add']/span[2]").click()
        driver.find_element_by_id("tableFieldItemForm2:diagnose_input").click()
        driver.find_element_by_id("tableFieldItemForm2:diagnose_input").send_keys("Covid")
        time.sleep(2)
        driver.find_element_by_xpath("//span[@id='tableFieldItemForm2:diagnose_panel']/ul/li[2]").click()
        time.sleep(2)
        driver.find_element_by_id("tableFieldItemForm2:diagStatus_label").click()
        driver.find_element_by_id("tableFieldItemForm2:diagStatus_1").click()
        time.sleep(1)
        driver.find_element_by_id("tableFieldItemForm2:j_idt207").click()
        window_before = driver.window_handles[0]
        driver.find_element_by_id("tableFieldItemForm2:whoIsSet_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#tableForm\:main-table_data > tr > td:nth-child(1)").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(3)
        driver.find_element_by_id("tableFieldItemForm2:whoIsSetPerson").click()
        driver.find_element_by_id("tableFieldItemForm2:whoIsSetPerson").clear()
        driver.find_element_by_id("tableFieldItemForm2:whoIsSetPerson").send_keys(u"Иванов ИИ")
        driver.find_element_by_xpath("//button[@id='tableFieldItemForm2:saveTableButton2']/span").click()
        driver.find_element_by_link_text(u"Исследования").click()
        driver.find_element_by_xpath("//button[@id='j_idt78:j_idt97:tf_analyzesTable_add']/span[2]").click()
        driver.find_element_by_id("tableFieldItemForm2:analysisDate_input").click()
        driver.find_element_by_id("tableFieldItemForm2:analysisDate_input").clear()
        driver.find_element_by_id("tableFieldItemForm2:analysisDate_input").send_keys(now.strftime("%d.%m.%Y"))
        driver.find_element_by_id("tableFieldItemForm2:whoCreatedStr").click()
        driver.find_element_by_id("tableFieldItemForm2:resultDate_input").click()
        driver.find_element_by_id("tableFieldItemForm2:resultDate_input").clear()
        driver.find_element_by_id("tableFieldItemForm2:resultDate_input").send_keys(now.strftime("%d.%m.%Y"))
        driver.find_element_by_id("tableFieldItemForm2:whoCreatedStr").click()
        driver.find_element_by_id("tableFieldItemForm2:nameAnalysis_label").click()
        driver.find_element_by_id("tableFieldItemForm2:nameAnalysis_1").click()
        window_before = driver.window_handles[0]
        driver.find_element_by_id("tableFieldItemForm2:pathogenType_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#tableForm\:main-table_data > tr > td:nth-child(1)").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(3)
        driver.find_element_by_id("tableFieldItemForm2:resultAnalysis_label").click()
        driver.find_element_by_id("tableFieldItemForm2:resultAnalysis_1").click()
        time.sleep(1)
        driver.find_element_by_id("tableFieldItemForm2:j_idt207").click()
        window_before = driver.window_handles[0]
        driver.find_element_by_id("tableFieldItemForm2:whoCreated_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#tableForm\:main-table_data > tr > td:nth-child(1)").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(3)
        driver.find_element_by_xpath("//button[@id='tableFieldItemForm2:saveTableButton2']/span").click()
        driver.find_element_by_link_text(u"Госпитализация").click()
        driver.find_element_by_id("j_idt78:j_idt97:j_id134").click()
        driver.find_element_by_xpath("//label[@for='j_idt78:j_idt97:needHospitalization:0']").click()
        driver.find_element_by_xpath("//button[@id='j_idt78:j_idt97:tf_hospitalizationTable_add']/span[2]").click()
        driver.find_element_by_id("tableFieldItemForm2:medicalHistoryNumber").click()
        driver.find_element_by_id("tableFieldItemForm2:medicalHistoryNumber").clear()
        driver.find_element_by_id("tableFieldItemForm2:medicalHistoryNumber").send_keys("777")
        window_before = driver.window_handles[0]
        driver.find_element_by_id("tableFieldItemForm2:institution_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#tableForm\:main-table_data > tr > td:nth-child(1)").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(3)
        window_before = driver.window_handles[0]
        driver.find_element_by_id("tableFieldItemForm2:department_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#tableForm\:main-table_data > tr > td:nth-child(1)").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(3)
        driver.find_element_by_id("tableFieldItemForm2:receiptDate_input").click()
        driver.find_element_by_id("tableFieldItemForm2:receiptDate_input").clear()
        driver.find_element_by_id("tableFieldItemForm2:receiptDate_input").send_keys(now.strftime("%d.%m.%Y"))
        driver.find_element_by_id("tableFieldItemForm2:medicalHistoryNumber").click()
        time.sleep(1)
        driver.find_element_by_id("tableFieldItemForm2:dischargeDate_input").click()
        driver.find_element_by_id("tableFieldItemForm2:dischargeDate_input").clear()
        driver.find_element_by_id("tableFieldItemForm2:dischargeDate_input").send_keys(now.strftime("%d.%m.%Y"))
        driver.find_element_by_id("tableFieldItemForm2:j_idt207_content").click()
        driver.find_element_by_id("tableFieldItemForm2:treatmentOutcome_label").click()
        driver.find_element_by_id("tableFieldItemForm2:treatmentOutcome_1").click()
        driver.find_element_by_xpath("//button[@id='tableFieldItemForm2:saveTableButton2']/span").click()
        driver.find_element_by_link_text(u"Исход заболевания").click()
        driver.find_element_by_id("j_idt78:j_idt97:j_id142").click()
        driver.find_element_by_id("j_idt78:j_idt97:diseaseOutcome_label").click()
        driver.find_element_by_id("j_idt78:j_idt97:diseaseOutcome_1").click()
        time.sleep(1)
        driver.find_element_by_id("j_idt78:j_idt97:receiptDate_input").click()
        driver.find_element_by_id("j_idt78:j_idt97:receiptDate_input").clear()
        driver.find_element_by_id("j_idt78:j_idt97:receiptDate_input").send_keys(now.strftime("%d.%m.%Y"))
        driver.find_element_by_id("j_idt78:j_idt97:j_id142_content").click()
        driver.find_element_by_link_text(u"Посещение ММС").click()
        driver.find_element_by_xpath("//button[@id='j_idt78:j_idt97:tf_mmcVisits_add']/span[2]").click()

        driver.find_element_by_id("tableFieldItemForm2:eventName").click()
        driver.find_element_by_id("tableFieldItemForm2:eventName").clear()
        driver.find_element_by_id("tableFieldItemForm2:eventName").send_keys(u"Лечим Динозавриков")
        driver.find_element_by_id("tableFieldItemForm2:eventLocation").click()
        driver.find_element_by_id("tableFieldItemForm2:eventLocation").clear()
        driver.find_element_by_id("tableFieldItemForm2:eventLocation").send_keys(u"Динозавриков ул 88")
        #driver.find_element_by_id("tableFieldItemForm2:visitDate_input").send_keys("19.03.2022")
        #driver.find_element_by_id("tableFieldItemForm2:tableFieldPanel2").click()
        #time.sleep(2)
        driver.find_element_by_xpath("//button[@id='tableFieldItemForm2:saveTableButton2']/span").click()
        driver.find_element_by_link_text(u"Эпиданамнез").click()
        driver.find_element_by_id("j_idt78:j_idt97:j_id174").click()
        driver.find_element_by_xpath("//label[@for='j_idt78:j_idt97:pregnants:1']").click()
        driver.find_element_by_xpath("//label[@for='j_idt78:j_idt97:donors:1']").click()
        driver.find_element_by_xpath("//button[@id='j_idt78:j_idt97:tf_stayPlaces_add']/span[2]").click()
        window_before = driver.window_handles[0]
        driver.find_element_by_id("tableFieldItemForm2:orgName_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#tableForm\:main-table_data > tr > td:nth-child(1)").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(3)
        driver.find_element_by_id("tableFieldItemForm2:arriveDateFrom_input").click()
        driver.find_element_by_id("tableFieldItemForm2:arriveDateFrom_input").clear()
        driver.find_element_by_id("tableFieldItemForm2:arriveDateFrom_input").send_keys("01.03.2022")
        driver.find_element_by_id("tableFieldItemForm2:city_input").click()
        driver.find_element_by_id("tableFieldItemForm2:flat").click()
        driver.find_element_by_id("tableFieldItemForm2:arriveDateTo_input").click()
        driver.find_element_by_id("tableFieldItemForm2:arriveDateTo_input").clear()
        driver.find_element_by_id("tableFieldItemForm2:arriveDateTo_input").send_keys(now.strftime("%d.%m.%Y"))
        driver.find_element_by_id("tableFieldItemForm2:city_input").click()
        driver.find_element_by_id("tableFieldItemForm2:j_idt207_content").click()
        driver.find_element_by_id("tableFieldItemForm2:note").click()
        driver.find_element_by_id("tableFieldItemForm2:note").clear()
        driver.find_element_by_id("tableFieldItemForm2:note").send_keys(u"Динозаврики рулят")
        driver.find_element_by_xpath("//button[@id='tableFieldItemForm2:saveTableButton2']/span").click()
        time.sleep(2)
        driver.find_element_by_id("j_idt78:j_idt97:arriveCountry_label").click()
        time.sleep(1)
        driver.find_element_by_id("j_idt78:j_idt97:arriveCountry_102").click()
        driver.find_element_by_id("j_idt78:j_idt97:arriveDate_input").click()
        driver.find_element_by_id("j_idt78:j_idt97:arriveDate_input").clear()
        driver.find_element_by_id("j_idt78:j_idt97:arriveDate_input").send_keys("10.03.2022")
        driver.find_element_by_xpath("//table[@id='j_idt78:j_idt97:j_id190']/tbody/tr[3]").click()
        driver.find_element_by_id("j_idt78:j_idt97:arrivalWay").click()
        driver.find_element_by_id("j_idt78:j_idt97:arrivalWay").clear()
        driver.find_element_by_id("j_idt78:j_idt97:arrivalWay").send_keys(u"самолет, 66699")
        driver.find_element_by_id("j_idt78:j_idt97:amountPeopleInTouristGroup_input").click()
        driver.find_element_by_id("j_idt78:j_idt97:amountPeopleInTouristGroup_input").clear()
        driver.find_element_by_id("j_idt78:j_idt97:amountPeopleInTouristGroup_input").send_keys("5")
        driver.find_element_by_id("j_idt78:j_idt97:guideMobilePhone").click()
        driver.find_element_by_id("j_idt78:j_idt97:guideMobilePhone").clear()
        driver.find_element_by_id("j_idt78:j_idt97:guideMobilePhone").send_keys("+74236572866")
        driver.find_element_by_id("j_idt78:j_idt97:riskFactor_label").click()
        driver.find_element_by_id("j_idt78:j_idt97:riskFactor_label").click()
        driver.find_element_by_id("j_idt78:j_idt97:riskFactorDescription").click()
        driver.find_element_by_id("j_idt78:j_idt97:riskFactorDescription").clear()
        driver.find_element_by_id("j_idt78:j_idt97:riskFactorDescription").send_keys(u"динозаврики могут затянуть на танцпол")
        driver.find_element_by_id("j_idt78:j_idt97:riskFactorDate_input").click()
        driver.find_element_by_id("j_idt78:j_idt97:riskFactorDate_input").clear()
        driver.find_element_by_id("j_idt78:j_idt97:riskFactorDate_input").send_keys("20.03.2022")
        driver.find_element_by_xpath("//table[@id='j_idt78:j_idt97:j_id206']/tbody/tr[3]").click()
        self.driver.execute_script("scroll(0, -250);")
        time.sleep(2)
        driver.find_element_by_link_text(u"Сведения о вакцинации").click()
        time.sleep(1)
        driver.find_element_by_id("j_idt78:j_idt97:j_id215").click()
        driver.find_element_by_xpath("//label[@for='j_idt78:j_idt97:isVaccinated:0']").click()
        driver.find_element_by_xpath("//button[@id='j_idt78:j_idt97:tf_vaccinationInformationTable_add']/span[2]").click()
        window_before = driver.window_handles[0]
        driver.find_element_by_id("tableFieldItemForm2:institution1_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#tableForm\:main-table_data > tr > td:nth-child(1)").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(3)
        driver.find_element_by_id("tableFieldItemForm2:vaccine1").click()
        driver.find_element_by_id("tableFieldItemForm2:vaccine1_2").click()
        time.sleep(1)
        driver.find_element_by_id("tableFieldItemForm2:vaccinationDate1_input").click()
        driver.find_element_by_id("tableFieldItemForm2:vaccinationDate1_input").clear()
        driver.find_element_by_id("tableFieldItemForm2:vaccinationDate1_input").send_keys("05.02.2022"+Keys.TAB)

        driver.find_element_by_xpath("//table[@id='tableFieldItemForm2:tableFieldPanel2']/tbody/tr[4]").click()
        driver.find_element_by_id("tableFieldItemForm2:seria1").click()
        driver.find_element_by_id("tableFieldItemForm2:seria1").clear()
        driver.find_element_by_id("tableFieldItemForm2:seria1").send_keys("1111")
        driver.find_element_by_id("tableFieldItemForm2:dose1").click()
        driver.find_element_by_id("tableFieldItemForm2:dose1").clear()
        driver.find_element_by_id("tableFieldItemForm2:dose1").send_keys("555")
        window_before = driver.window_handles[0]
        driver.find_element_by_id("tableFieldItemForm2:institution2_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#tableForm\:main-table_data > tr > td:nth-child(1)").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(3)
        driver.find_element_by_id("tableFieldItemForm2:vaccine2").click()
        driver.find_element_by_id("tableFieldItemForm2:vaccine2_2").click()
        time.sleep(2)
        driver.find_element_by_id("tableFieldItemForm2:vaccinationDate2_input").click()
        driver.find_element_by_id("tableFieldItemForm2:vaccinationDate2_input").clear()
        driver.find_element_by_id("tableFieldItemForm2:vaccinationDate2_input").send_keys("09.02.2022"+Keys.TAB)
        driver.find_element_by_xpath("//table[@id='tableFieldItemForm2:tableFieldPanel2']/tbody/tr[9]").click()
        driver.find_element_by_id("tableFieldItemForm2:seria2").click()
        driver.find_element_by_id("tableFieldItemForm2:seria2").clear()
        driver.find_element_by_id("tableFieldItemForm2:seria2").send_keys("2222")
        driver.find_element_by_id("tableFieldItemForm2:dose2").click()
        driver.find_element_by_id("tableFieldItemForm2:dose2").clear()
        driver.find_element_by_id("tableFieldItemForm2:dose2").send_keys("1")
        driver.find_element_by_xpath("//button[@id='tableFieldItemForm2:saveTableButton2']/span").click()
        driver.find_element_by_link_text(u"Служебные поля").click()
        numberIss = driver.find_element_by_id("j_idt78:docNumber").get_attribute("value")
        driver.find_element_by_xpath("//button[@id='j_idt78:j_idt81']/span").click()
        time.sleep(4)
        assert (driver.find_element_by_id("dialogForm:j_idt209_content").text) == "Эпидемиологический номер " + numberIss + " присвоен пациенту"
        driver.find_element_by_xpath("//button[@id='dialogForm:j_idt211']/span").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
