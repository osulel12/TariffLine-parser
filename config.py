import os
from dotenv import load_dotenv


# Подгружаем наши переменные окружения
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

dict_config = {'iframe_account_page': '//div[@class="account-page"]//iframe',
               'div_user_login': 'PageContent_Login1_UserName',
               'div_user_pass': 'PageContent_Login1_Password',
               'my_login_itc': os.getenv('MY_LOGIN_ITC'),
               'my_pass_itc': os.getenv('MY_PASS_ITC'),
               'button_login': 'PageContent_Login1_DivButton',
               'button_bulk_download': '//div[@class="heading-wrapper"]/button[@class="Button__ButtonStyled-sc-1a4z789-0 kzbaZI primary"]',
               'type_tariff': '//label[@for="data-type-Tariff"]',
               'source_applied': '//label[@for="data-source-Applied"]',
               'option_mfn': '//label[@for="data-type-option-MFN"]',
               'check_box_ntlc': '//label[@for="product-level-8"]',
               'reporting_country': "//div[@class='Form__Inputs-sc-17z8j4b-2 esPQiy']/div[2]//div[@class='css-1wy0on6 select__indicators']",
               'button_show_downloads': '//div[@class="col-md-6 text-right"]/button[@class="Button__ButtonStyled-sc-1a4z789-0 kzbaZI"]',
               'button_delete_all': "//button[@class='SmallButton__ButtonStyled-sc-t72cnh-0 kkDbuS']",
               'button_yes_by_modal_window': "//div[@class='MuiDialogActions-root MuiDialogActions-spacing']//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary'][2]",
               'button_back_new_data': "//div[@class='col-md-6 text-right']//button[@class='Button__ButtonStyled-sc-1a4z789-0 kzbaZI primary']",
               'effectively_applied_option': "//label[@for='data-type-option-Applied']",
               'min_option': "//label[@for='secondary-data-type-option-MIN']",
               'trade_agreement_option': "//label[@for='secondary-data-type-option-TA']",
               'year_select': "//div[@id='select-year']//div[@class='css-1wy0on6 select__indicators']"




}