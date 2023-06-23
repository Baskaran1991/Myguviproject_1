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

# Click on the PIM module link
pim_module_link = driver.find_element(By.ID, 'pim_module')
pim_module_link.click()

# Wait for the employee list page to load
employee_list_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'employee_list'))
)

# Find the edit button for the desired employee and click on it
edit_button = driver.find_element(By.XPATH, '//button[contains(text(), "Edit")]')
edit_button.click()

# Wait for the employee details page to load
employee_details_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'employee_details'))
)

# Edit the employee details (replace the placeholders with the actual details)
first_name_field = driver.find_element(By.ID, 'first_name')
last_name_field = driver.find_element(By.ID, 'last_name')
email_field = driver.find_element(By.ID, 'email')

first_name_field.clear()
first_name_field.send_keys('John')

last_name_field.clear()
last_name_field.send_keys('Doe')

email_field.clear()
email_field.send_keys('john.doe@example.com')

# Save the changes
save_button = driver.find_element(By.XPATH, '//button[contains(text(), "Save")]')
save_button.click()

# Wait for the changes to be saved
success_message_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'success_message'))
)

# Close the browser
driver.quit()
