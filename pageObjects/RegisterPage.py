from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class Register:

    button_registerpage_xpath = "//*[contains(text(),'Register')]"
    radiobtn_male_xpath = "//input[@id='gender-male']"
    txtbox_firstname_xpath = "//input[@id='FirstName']"
    txtbox_lastname_xpath = "//input[@id='LastName']"
    drpdwn_date_xpath = "//select[@name='DateOfBirthDay']"
    drpdwn_month_xpath = "//select[@name='DateOfBirthMonth']"
    drpdwn_year_xpath = "//select[@name='DateOfBirthYear']"
    txtbox_email_xpath = "//input[@id='Email']"
    txtbox_companyname_xpath = "//input[@id='Company']"
    txtbox_password_xpath = "//input[@id='Password']"
    txtbox_confirmpass_Xpath = "//input[@id='ConfirmPassword']"
    button_register_xpath = "//button[@id='register-button']"
    txt_registercompleted_xpath = "//div[contains(text(),'Your registration completed')]"

    def __init__(self, driver):
        self.driver=driver


    def Gotoregisterpage(self):
        self.driver.find_element(By.XPATH, self.button_registerpage_xpath).click()

    def Gender(self):
        self.driver.find_element(By.XPATH, self.radiobtn_male_xpath).click()

    def Firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.txtbox_firstname_xpath).send_keys(firstname)

    def Lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.txtbox_lastname_xpath).send_keys(lastname)

    def DateOfBirth(self):
        date= Select(self.driver.find_element(By.XPATH, self.drpdwn_date_xpath))
        date.select_by_value("14")
        month = Select(self.driver.find_element(By.XPATH, self.drpdwn_month_xpath))
        month.select_by_value("7")
        year = Select(self.driver.find_element(By.XPATH, self.drpdwn_year_xpath))
        year.select_by_value("2000")

    def Email(self, email):
        self.driver.find_element(By.XPATH, self.txtbox_email_xpath).send_keys(email)

    def Companyname(self, companyname):
        self.driver.find_element(By.XPATH, self.txtbox_companyname_xpath).send_keys(companyname)

    def Password(self, password):
        self.driver.find_element(By.XPATH, self.txtbox_password_xpath).send_keys(password)

    def Confirmpassword(self, confirmpassword):
        self.driver.find_element(By.XPATH, self.txtbox_confirmpass_Xpath).send_keys(confirmpassword)

    def ClickRegister(self):
        self.driver.find_element(By.XPATH, self.button_register_xpath).click()

    def RegisterConformation(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_registercompleted_xpath).is_displayed()
        except:
            return False
