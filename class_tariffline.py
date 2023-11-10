from selenium import webdriver
from selenium.common.exceptions import TimeoutException as time_ex
from selenium.common.exceptions import NoSuchElementException as no_element
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from config import dict_config

import time


class Its_tariff_line_parser:

    def __init__(self, version_browser, page_url):
        self.version_browser = version_browser
        self.page_url = page_url

    @staticmethod
    def cleaning_downloads_value(browser, actions):
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, dict_config['button_show_downloads']))).click()
        actions.move_to_element(WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, dict_config['button_delete_all'])))).click()
        actions.perform()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, dict_config['button_yes_by_modal_window']))).click()

    @staticmethod
    def back_new_download(browser, actions):
        actions.move_to_element(WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, dict_config['button_back_new_data']))))
        actions.click()
        actions.perform()


    @staticmethod
    def setting_option(browser, actions, type_tariff, effectively_tariff=None):

        # Выюираем Bulk загрузку
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, dict_config['button_bulk_download']))).click()
        actions.move_to_element(WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, dict_config['type_tariff'])))).click()
        actions.move_to_element(WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, dict_config['source_applied'])))).click()
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, type_tariff))).click()
        if effectively_tariff:
            actions.move_to_element(WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, effectively_tariff)))).click()
        # Так как не все элементы отображаются в поле видимости, переместимся к необходимым
        # Перемещаемся к параметру ntlc
        actions.move_to_element(WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, dict_config['check_box_ntlc'])))).click()
        actions.perform()

    @staticmethod
    def choose_reporter_and_year(browser, actions, list_out_country=['react-select-2-option-0-2']):
        # Так как не все элементы отображаются в поле видимости, переместимся к необходимым
        reporting_country = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, dict_config['reporting_country'])))
        # Перемещаемся к выборы страны
        actions.move_to_element(reporting_country)
        actions.perform()
        reporting_country.click()



        # reporting_country.click()
        list_num_id_country_2 = [i.get_attribute('id') for i in
                                 browser.find_elements(By.XPATH,
                                                       "//div[@class='css-fk865s-option select__option']")]

        dct = {i.text: i.get_attribute('id') for i in browser.find_elements(By.XPATH,
                                                       "//div[@class='css-fk865s-option select__option']")}
        print(dct)



        for i in list_num_id_country_2:
            try:
                WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, i))).click()
                reporting_country.click()
            except:
                pass

        for j in list_out_country:
            try:
                WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, j))).click()
            except time_ex:
                pass
        browser.maximize_window()
        year_l = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, dict_config['year_select'])))
        actions.move_to_element(year_l)
        actions.click()
        actions.perform()
        time.sleep(5)
        # year_l.click()
        l_y = [i.get_attribute('id') for i in
                                 browser.find_elements(By.XPATH,
                                                       "//div[@class='css-fk865s-option select__option']")]
        dct_y = {i.text: i.get_attribute('id') for i in browser.find_elements(By.XPATH,
                                                       "//div[@class='css-fk865s-option select__option']")}
        print(dct_y)
        for i in l_y:
            try:
                WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, i))).click()
                year_l.click()
            except:
                pass

        # for j in list_out_country:
        #     WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, j))).click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
                                    "//div[@class='CheckBox__CheckBoxStyled-sc-a52059-0 cwIdzb']//label[@for='agreement-cb']"))).click()
        print(WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
                                    "//div[@class='CheckBox__CheckBoxStyled-sc-a52059-0 cwIdzb']//label[@for='agreement-cb']"))).text)
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
                                    "//div[@class='col-md-6']//button[@class='Button__ButtonStyled-sc-1a4z789-0 kzbaZI primary']"))).click()



        time.sleep(5)

    def get_data_tarrif(self):

        with webdriver.Chrome(ChromeDriverManager(driver_version=self.version_browser).install()) as browser:
            # Создаем объект ActionChains для дальнейшего перемещения к нужным нам элементам страницы
            actions = ActionChains(browser)
            browser.get(self.page_url)

            # Переключаемся на фрейм, чтобы авторизироваться
            iframe = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH, dict_config['iframe_account_page'])))
            browser.switch_to.frame(iframe)

            # Находим на странице элементы формы и заполняем их
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, dict_config['div_user_login']))).send_keys(dict_config['my_login_itc'])

            # Вводим пароль
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, dict_config['div_user_pass']))).send_keys(dict_config['my_pass_itc'])

            # Находим на странице кнопку отправки формы
            try:
                WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, dict_config['button_login']))).click()
                time.sleep(3)
            except:
                time.sleep(3)

            # Перезагружаем страницу и выбираем нужный тип загрузки
            browser.refresh()
            try:
                self.cleaning_downloads_value(browser, actions)
                self.back_new_download(browser, actions)
            except time_ex:
                print('Скаченные ранее данные отсутствуют')

            # # Выюираем Bulk загрузку
            # WebDriverWait(browser, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, dict_config['button_bulk_download']))).click()
            # Настраиваем параметры скачивания
            for i, type_option in enumerate([dict_config['option_mfn'], dict_config['effectively_applied_option']]):
                if i > 0:
                    for option_by_partner in [dict_config['min_option'], dict_config['trade_agreement_option']]:
                        self.setting_option(browser, actions, type_option, option_by_partner)
                        self.choose_reporter_and_year(browser, actions)
                        self.back_new_download(browser, actions)
                        time.sleep(5)
                else:
                    self.setting_option(browser, actions, type_option)
                    self.choose_reporter_and_year(browser, actions)
                    self.back_new_download(browser, actions)
                    time.sleep(5)







# with webdriver.Chrome(ChromeDriverManager(driver_version='118.0.5993.70').install()) as browser:
#     # Переходим на нужный сайт
#     browser.get('https://www.macmap.org/en/download')
#     # browser.maximize_window()
#     # with open('ht.txt', 'w', encoding='utf-8') as fl:
#     #     fl.write(browser.page_source)
#     iframe = WebDriverWait(browser, 5).until(
#         EC.presence_of_element_located((By.XPATH, '//div[@class="account-page"]//iframe')))
#     browser.switch_to.frame(iframe)
#     # print(browser.page_source)
#
#     # Находим на странице элементы формы и заполняем их
#     WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'PageContent_Login1_DivUserName')))
#     browser.find_element(By.ID, 'PageContent_Login1_UserName').send_keys('a.ryzhkov@aemcx.ru')
#
#
#     # Вводим пароль
#     WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'PageContent_Login1_DivPassword')))
#     password = browser.find_element(By.ID, 'PageContent_Login1_Password')
#     password.send_keys('1233Q')
#     # time.sleep(2)

#     # Находим на странице кнопку отправки формы
#     try:
#         WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'PageContent_Login1_DivButton'))).click()
#         time.sleep(3)
#     except:
#         print('ex')
#         time.sleep(3)
#
#     # with open('file_auturiz_html.txt', 'w', encoding='utf-8') as fl:
#     #     fl.write(browser.page_source)
#     browser.refresh()
#     time.sleep(3)
#     browser.find_element(By.XPATH, '//div[@class="heading-wrapper"]/button[@class="Button__ButtonStyled-sc-1a4z789-0 kzbaZI primary"]').click()
#     for i in browser.find_elements(By.XPATH, '//button[@class="Button__ButtonStyled-sc-1a4z789-0 kzbaZI primary"]'):
#         print(i.text)
#     # print(browser.find_element(By.XPATH, '//button[@class="Button__ButtonStyled-sc-1a4z789-0 kzbaZI primary"]').text)
#     time.sleep(5)
#     browser.find_element(By.XPATH, '//label[@for="data-type-Tariff"]').click()
#     # with open('ht_2.txt', 'w', encoding='utf-8') as fl:
#     #     fl.write(browser.page_source)
#     # time.sleep(3)
#     browser.find_element(By.XPATH, '//label[@for="data-type-option-MFN"]').click()
#     time.sleep(2)
#
#     actions = ActionChains(browser)
#     target = browser.find_element(By.XPATH, '//label[@for="product-level-8"]')
#     actions.move_to_element(target)
#     actions.click()
#     actions.perform()
#     # WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//label[@for="product-level-8"]'))).click()
#     # browser.find_element(By.ID, 'product-level-8').click()
#     # browser.find_element(By.XPATH, '//label[@for="product-level-8"]').click()
#     # browser.find_element(By.ID, 'product-level-8').click()
#     # browser.find_element(By.XPATH, '//label[@for="product-level-8"]').click()
#
#
#     clk = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
#                 (By.XPATH, "//div[@class='css-1bpl54v-control select__control']/div[1]")))
#     clk2 = WebDriverWait(browser, 10).\
#         until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Form__Inputs-sc-17z8j4b-2 esPQiy']/div[2]")))
#     time.sleep(2)
#     clk2.click()
#     list_num_id_country = [i.get_attribute('id').split('-')[-1] for i in browser.find_elements(By.XPATH, "//div[@class='css-fk865s-option select__option']")]
#     for i in browser.find_elements(By.XPATH, "//div[@class='css-fk865s-option select__option']"):
#         print(i.get_attribute('id'))
#     for i in range(240):
#         try:
#             WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.ID, f'react-select-2-option-0-{i}')))
#             print(i)
#         except:
#             print(f'net {i}')
#     time.sleep(1)
#     clk2.click()
#     time.sleep(1)
#     for country in range(2):
#         try:
#             clk2.click()
#             time.sleep(1)
#             # WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, f'react-select-2-option-0-{country}'))).click()
#             browser.find_element(By.ID, f'react-select-2-option-0-{country}').click()
#             # browser.find_element(By.ID, f'react-select-2-option-0-0').click()
#
#             time.sleep(1)
#         except:
#             with open('ht_list_id.txt', 'w', encoding='utf-8') as fl:
#                 fl.write(browser.page_source)
#         # print(country.text)
#         # country.click()
#     # with open('ht_list_country.txt', 'w', encoding='utf-8') as fl:
#     #     fl.write(browser.page_source)
#     clc_year = WebDriverWait(browser, 10).\
#         until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Form__Inputs-sc-17z8j4b-2 esPQiy']/div[4]")))
#     clc_year.click()
#     with open('ht_year_list.txt', 'w', encoding='utf-8') as fl:
#         fl.write(browser.page_source)
#     time.sleep(3)
#     for i in range(15):
#         try:
#             WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.ID, f'react-select-4-option-1-{i}')))
#             print(i)
#         except:
#             print(f'net {i}')
#     clc_year.click()
#     time.sleep(2)
#     for year in range(3):
#         try:
#             clc_year.click()
#             time.sleep(1)
#             # WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, f'react-select-2-option-0-{country}'))).click()
#             browser.find_element(By.ID, f'react-select-4-option-1-{year}').click()
#             # browser.find_element(By.ID, f'react-select-2-option-0-0').click()
#
#             time.sleep(1)
#         except:
#             pass
#     # WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'CheckBox__CheckBoxStyled-sc-a52059-0 cwIdzb'))).click()
#     target2 = browser.find_element(By.XPATH, "//div[@class='CheckBox__CheckBoxStyled-sc-a52059-0 cwIdzb']")
#     actions.move_to_element(target2)
#     actions.click()
#     actions.perform()
#     time.sleep(3)
#     WebDriverWait(browser, 3).until(
#         EC.element_to_be_clickable((By.XPATH,  "//div[@class='col-md-6']/button[@class='Button__ButtonStyled-sc-1a4z789-0 kzbaZI primary'][1]"))).click()
#     time.sleep(5)
#     # WebDriverWait(browser, 120).until(
#     #     EC.text_to_be_present_in_element((By.XPATH,
#     #                                 "//tr[@class='customized-download-item'][1]/td/a[@class='StatusLink__StatusLinkStyled-sc-1k1khk5-0 kvpEcC']"), 'Download'))
#     time.sleep(180)
#     browser.find_element(By.XPATH,
#                          "//tr[@class='customized-download-item'][1]/td/a[@class='StatusLink__StatusLinkStyled-sc-1k1khk5-0 kvpEcC download']").click()
#     time.sleep(10)
#     # src = browser.find_element(By.XPATH, "//tr[@class='customized-download-item'][1]/td/a[@class='StatusLink__StatusLinkStyled-sc-1k1khk5-0 kvpEcC download']").get_attribute('href')
#     # browser.get(src)
# 'react-select-4-option-1-0'

# PageContent_Login1_UserName
# PageContent_Login1_Password
#
# PageContent_Login1_Button

# 1. Скрол до нужных элементов
# 2. Выкачка сразу всех или по 1
