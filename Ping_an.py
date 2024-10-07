from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import Ping_An_Class

############################################################################################
# 创建 ChromeOptions 对象
chrome_options = Options()
# 添加实验性选项以连接到指定端口上的调试器
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# 初始化 WebDriver，并且将创建的 options 传递给它
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://pacz.pa18.com/cms/#/OrderCenter/Offer')

# 等待页面加载完成，并且元素可见
wait = WebDriverWait(driver, 10)  # 最多等待10秒

# 记录当前窗口的句柄
original_window = driver.current_window_handle

button1 = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                 '//*[@id="root"]/div[2]/section/section/main/div[1]/div/div/div/div/div[3]/div[1]/div[3]/div[1]/button[1]')))

# 点击按钮
button1.click()

# 等待新窗口出现，并且确保有两个窗口句柄
wait.until(EC.number_of_windows_to_be(2))

# 循环遍历直到找到新的窗口句柄
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break
# 定位iframe
iframe = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]')))
driver.switch_to.frame(iframe)
# 现在可以在新窗口中执行操作
select_location = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="agentCode"]')))

# 创建 Select 对象
select = Select(select_location)

wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="agentCode"]/option[@value="0"]'),
                                            '12000228 平安创展保险销售服务有限公司台州分公司'))
select.select_by_value('0')
time.sleep(1)
wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="mainContent"]/div[2]/div[2]/form/div[2]/div/div/button[1]'))).click()

time.sleep(3)
#################################################################################################
df = pd.read_excel('平安.xlsx')

# 标志变量，用于判断是否是第一次循环
is_first_iteration = True

for index, row in df.iterrows():
    owner = row['车主']
    vin = row['车架号']

    # 创建 ClickPage 实例
    click_page_instance = Ping_An_Class.ClickPage(owner, vin, driver)

    if is_first_iteration:
        # 第一次循环时执行所有操作
        click_page_instance.input_owner_driver_name()
        click_page_instance.input_owner_driver_idno()
        click_page_instance.input_owner_driver_telephone()
        click_page_instance.select_owner_driver_province()
        click_page_instance.select_owner_driver_city()
        click_page_instance.select_owner_driver_county()
        click_page_instance.input_vehicle_license_code()
        click_page_instance.input_engine_number()
        click_page_instance.input_vehicle_frame_number()
        click_page_instance.input_first_registration_date('2023-09-23')
        click_page_instance.click_vehicle_type_validation_button()
        # click_page_instance.click_quote_button()
        click_page_instance.click_syx_checkbox()
        #定位去年保险公司
        #如有则爬下信息放入excel  如无就为平安并按下报价 获取分部输入excel
    else:
        # 后续循环时只执行部分操作
        click_page_instance.input_owner_driver_name()
        click_page_instance.input_vehicle_frame_number()
        # 定位去年保险公司
        # 如有则爬下信息放入excel  如无就为平安并按下报价 获取分部输入excel

    # 更新标志变量
    is_first_iteration = False




