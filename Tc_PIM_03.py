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
pim_module = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'menu_pim_viewPimModule'))
)
pim_module.click()

# Wait for the employee list to be visible and click on the first employee
employee_list = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'employeeListTable'))
)
first_employee = employee_list.find_element(By.TAG_NAME, 'tr')
first_employee.click()

# Find the delete button and click on it
delete_button = driver.find_element(By.ID, 'btnDelete')
delete_button.click()

# Wait for the confirmation dialog to be visible and click on OK
confirmation_dialog = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'dialogDeleteBtn'))
)
confirmation_dialog.click()

# Wait for the successful deletion message to be visible
success_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'deleteConfModal'))
)

# Close the browser
driver.quit()