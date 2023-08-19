from selenium.webdriver.common.by import By

class Login:

    button_loginpage_xpath = "//a[contains(text(),'Log in')]"
    txtbox_email_xpath = "//input[@id='Email']"
    txtbox_password_xpath = "//input[@id='Password']"
    button_login_xpath = "//button[@class='button-1 login-button']"

    def __init__(self, driver):
        self.driver = driver

    def GotoLogin(self):
        self.driver.find_element(By.XPATH, self.button_loginpage_xpath).click()

    def Email(self, email):
        self.driver.find_element(By.XPATH, self.txtbox_email_xpath).send_keys(email)

    def Password(self, password):
        self.driver.find_element(By.XPATH, self.txtbox_password_xpath).send_keys(password)

    def Clicklogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()