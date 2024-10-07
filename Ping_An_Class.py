from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class ClickPage:
    def __init__(self, name, VIN, driver):
        self.name = name  # 名称
        self.VIN = VIN  # 车架号
        self.driver = driver  # 将 driver 存储为实例属性

    # 添加显式等待
    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def input_owner_driver_name(self):
        """输入行驶证车主名称"""
        # input_element = self.driver.find_element(By.XPATH, "//input[@name='ownerDriver-name']")
        input_element = self.wait_for_element(By.XPATH, "//input[@name='ownerDriver-name']")
        input_element.clear()
        input_element.send_keys(self.name)

    def input_owner_driver_idno(self):
        """输入行驶证车主身份证号"""
        input_element = self.driver.find_element(By.XPATH, "//input[@name='ownerDriver-idno']")
        input_element.clear()
        input_element.send_keys("341821200204293919")  # 填写数据

    def input_owner_driver_telephone(self):
        """输入行驶证车主电话号码"""
        input_element = self.driver.find_element(By.XPATH, "//input[@name='ownerDriver-telephone']")
        input_element.clear()
        input_element.send_keys("13888888888")  # 填写数据

    def select_owner_driver_province(self):
        """选择行驶证车主省份"""
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, '//select[@name="ownerDriver-province"]/option[@value="1"]'),
                '北京'
            )
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//select[@name="ownerDriver-province"]/option[@value="1"]'))
        )
        select_element = Select(self.driver.find_element(By.NAME, "ownerDriver-province"))
        select_element.select_by_value('1')

    def select_owner_driver_city(self):
        """选择行驶证车主市"""
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, '//*[@id="ownerDriverInfoDiv"]/div[2]/div/div/select[3]/option[@value="1"]'),
                '北京市'
            )
        )
        select_element = Select(self.driver.find_element(By.NAME, "ownerDriver-city"))
        select_element.select_by_value('1')

    def select_owner_driver_county(self):
        """选择行驶证车主区"""
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, '//*[@id="ownerDriverInfoDiv"]/div[2]/div/div/select[4]/option[@value="1"]'),
                '东城区'
            )
        )
        select_element = Select(self.driver.find_element(By.NAME, "ownerDriver-county"))
        select_element.select_by_value('1')

    def input_vehicle_license_code(self):
        """输入车辆信息: 车牌号"""
        input_element = self.driver.find_element(By.XPATH, "//input[@id='vehicleLicenseCodeId']")
        input_element.clear()
        input_element.send_keys('浙B-7824X')

    def input_engine_number(self):
        """输入车辆信息: 发动机号"""
        input_element = self.driver.find_element(By.XPATH, "//input[@id='engineNo']")
        input_element.clear()
        input_element.send_keys('EW328177')

    def input_vehicle_frame_number(self):
        """输入车辆信息: 车架号"""
        input_element = self.driver.find_element(By.XPATH, "//input[@id='vehicleFrameNo']")
        time.sleep(0.5)
        input_element.clear()
        input_element.send_keys(self.VIN)

    def click_vehicle_type_validation_button(self):
        """点击车型校验按钮"""
        button_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@ng-click='vehicleTypeQueryFn()']"))
        )
        button_element.click()

    def click_syx_checkbox(self):
        """勾选商业险复选框"""
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@ng-model='ctrl.isCheckedComm']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", checkbox)
        checkbox.click()

    def input_first_registration_date(self,data):
        """输入车辆信息: 初次登记日期"""
        # 等待直到初次登记日期的输入框变得可见并且可以被点击
        input_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@ng-model='veh.firstRegisterDate']"))
        )

        # 清空输入框
        input_element.clear()

        # 输入新的日期
        input_element.send_keys(data)

    def click_quote_button(self):
        """点击报价按钮"""
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@ng-click=\"quoteEvent.applyQueryAndQuote('N')\"]"))
        )
        button.click()

