# This is the 1st version, made for custom usage. 
# So it's not finished yet.

# DON'T FORGET TO DOWNLOAD THE WEBDRIVER
# Chrome, Firefox or Edge

# Import stuff
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import xlrd 

# Excel location path for windows. The excel (.xls) spreadsheet is containing the value of voucher and fixed amount value
excel_loc = 'D:\\Spreadsheet\\data_code_vouc.xls'
wb = xlrd.open_workbook(excel_loc)
sheet = wb.sheet_by_index(0)

# Create webdriver object, I use chrome. (https://chromedriver.chromium.org/downloads)
options = Options()
options.add_argument('user-data-dir=C:\\Users\\Danie\\AppData\\Local\\Google\\Chrome\\User Data')
driver = webdriver.Chrome(options=options)

# Total entries
start = 1
total = 100

# Value field

limit = '1'
date_1 = '2022-01-25'
time_1 = '12:00 AM'
date_2 = '2022-07-31'
time_2 = '11:59 PM'

def start_app():
    for i in range(start, total+1 ):
            
        driver.get("https://example.myshopify.com/admin/discounts/new") # Change the 'example' domain name of myshopify 
        print(f'Kode ke: {i} dari {total}')

        # Voucher Code 
        element_disc_code = driver.find_element_by_id('PolarisTextField1')
        element_disc_code.send_keys(sheet.cell_value(i, 0))

        # Types
        element_types = driver.find_element_by_css_selector("#PolarisChoiceList1 > ul:nth-child(2) > li:nth-child(2) > label:nth-child(1) > span:nth-child(2)")
        element_types.click()

        # Value 
        element_value = driver.find_element_by_id('fixedAmountValueField')
        element_value.send_keys(str(sheet.cell_value(i, 1)))
        
        # Haven't created a label yet to work with
        # Applies to 
        # Minimum Requirements
        # Customer Eligibility
        
        # Usage
        element_usage = driver.find_element_by_css_selector("#PolarisChoiceList5\[\] > ul:nth-child(2) > li:nth-child(1) > label:nth-child(1)")
        element_usage.click()

        # Usage limit
        element_usage_limit = driver.find_element_by_id('totalUsageLimit')
        element_usage_limit.send_keys(limit)

        # ------------------- Dates ---------------------
        # Start dates
        element_active_dates_1 = driver.find_element_by_id("StartEmbeddedDatePicker")
        element_active_dates_1.send_keys(Keys.CONTROL, "a"); 
        element_active_dates_1.send_keys(Keys.DELETE)
        element_active_dates_1.send_keys(date_1)

        # Start times
        element_active_time_1 = driver.find_element_by_id("StartTimeField")
        element_active_time_1.send_keys(Keys.CONTROL, "a"); 
        element_active_time_1.send_keys(Keys.DELETE)
        element_active_time_1.send_keys(time_1)

        # Check end date options 
        # Check this if only you want to set the end dates
        element_end_date = driver.find_element_by_css_selector('div.Polaris-FormLayout--grouped_17srt:nth-child(2) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(1) > span:nth-child(1) > span:nth-child(2)').click()

        # End dates
        element_active_dates_2 = driver.find_element_by_id("EndEmbeddedDatePicker")
        element_active_dates_2.send_keys(Keys.CONTROL, "a"); 
        element_active_dates_2.send_keys(Keys.DELETE)
        element_active_dates_2.send_keys(date_2)

        # End times
        element_active_time_2 = driver.find_element_by_id("EndTimeField")
        element_active_time_2.send_keys(Keys.CONTROL, "a"); 
        element_active_time_2.send_keys(Keys.DELETE)
        element_active_time_2.send_keys(time_2)

        # Submit
        element_submit = driver.find_element_by_css_selector('#AppFrameMain > div > div > div.Polaris-Page__Content_xd1mk > div > div:nth-child(3) > div > div > div:nth-child(2) > button > span > span').click()
    
    # 
    driver.close()
try:
    start_app()
except TimeoutException as ex:
    driver.refresh()
    start_app()