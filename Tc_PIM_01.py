from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
# To use the Python Selenium Selector you have to use the By class
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Baskar:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    username = 'Admin'
    password = 'admin123'
    # username_locator is a TagName
    username_locator = 'username'
    # password_locator is a TagName
    password_locator = 'password'
    # Submit Button Locator as XPATH
    submitBox_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    # Startup method for the CRM application
    def Browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    # Method for login into the CRM application
    def login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.submitBox_locator).click()


Baskar().Browsing()

Baskar().login()


def pim (self):
 self.driver.find_element_by_id("oxd-main-menu-item active")
 pim_module.click()

# Click the "Add Employee" button
add_employee = driver.find_element_by_id("btnAdd")
add_employee.click()

# Fill out the employee details form
first_name = driver.find_element_by_id("firstName")
first_name.send_keys("John")

last_name = driver.find_element_by_id("lastName")
last_name.send_keys("Doe")

employee_id = driver.find_element_by_id("employeeId")
employee_id.send_keys("12345")

save_button = driver.find_element_by_id("btnSave")
save_button.click()


# Click the "Save" button
save_button = driver.find_element_by_id("btnSave")
save_button.click()

# Close the browser window
driver.quit()