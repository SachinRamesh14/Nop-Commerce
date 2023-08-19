from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Cart:
    button_cart_xpath = "//a[contains(text(),'Shopping cart')]"
    checkbox_terms_xpath = "//input[@id='termsofservice']"
    button_checkout_xpath = "//button[@id='checkout']"
    dropdown_country_xpath = "//*[@id='BillingNewAddress_CountryId']"
    dropdown_state_xpath = "//*[@id='BillingNewAddress_StateProvinceId']"
    txtbox_city_xpath = "//input[@name='BillingNewAddress.City']"
    txtbox_address_xpath = "//input[@name='BillingNewAddress.Address1']"
    txtbox_address2_xpath = "//input[@name='BillingNewAddress.Address2']"
    txtbox_zipcode_xpath = "//input[@name='BillingNewAddress.ZipPostalCode']"
    txtbox_phone_xpath = "//input[@name='BillingNewAddress.PhoneNumber']"
    button_save_xpath = "//button[@onclick='Billing.save()']"

    checkbox_airway_xpath = "//input[@id='shippingoption_1']"
    button_save2_xpath = "//button[@onclick='ShippingMethod.save()']"

    checkbox_payment_xpath = "//*[@id='paymentmethod_1']"
    button_save3_xpath = "//*[@onclick='PaymentMethod.save()']"

    txtbox_name_xpath = "//*[@id='CardholderName']"
    txtbox_number_xpath = "//*[@id='CardNumber']"
    dropdown_month_xpath = "//*[@id='ExpireMonth']"
    select_month_xpath = "//*[@id='ExpireMonth']/option[5]"
    dropdown_year_xpath = "//*[@id='ExpireYear']"
    select_year_xpath = "//*[@id='ExpireYear']/option[3]"
    txtbox_cvv_xpath = "//*[@id='CardCode']"
    button_save4_xpath = "//button[@onclick='PaymentInfo.save()']"

    button_confirm_xpath = "//*[@onclick='ConfirmOrder.save()']"

    txt_confirmorder_xpath = "//*[contains(text(),'Your order has been successfully processed!')]"



    def __init__(self, driver):
        self.driver = driver


    def Gotocart(self):
        self.driver.find_element(By.XPATH, self.button_cart_xpath).click()

    def ClickCheckbox(self):
        self.driver.find_element(By.XPATH, self.checkbox_terms_xpath).click()

    def Clickcheckout(self):
        self.driver.find_element(By.XPATH, self.button_checkout_xpath).click()

    def Country(self):
        country = Select(self.driver.find_element(By.XPATH, self.dropdown_country_xpath))
        country.select_by_visible_text("India")

    def State(self):
        state = Select(self.driver.find_element(By.XPATH, self.dropdown_state_xpath))
        state.select_by_visible_text("Other")

    def City(self, city):
        self.driver.find_element(By.XPATH, self.txtbox_city_xpath).send_keys(city)

    def Address(self,address):
        self.driver.find_element(By.XPATH, self.txtbox_address_xpath).send_keys(address)

    def Zipcode(self, zipcode):
        self.driver.find_element(By.XPATH, self.txtbox_zipcode_xpath).send_keys(zipcode)

    def Phone(self, phone):
        self.driver.find_element(By.XPATH, self.txtbox_phone_xpath).send_keys(phone)

    def BillingSave(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()

    def Shippingway(self):
        self.driver.find_element(By.XPATH, self.checkbox_airway_xpath).click()

    def Shippingsave(self):
        self.driver.find_element(By.XPATH, self.button_save2_xpath).click()

    def Paymentoption(self):
        self.driver.find_element(By.XPATH, self.checkbox_payment_xpath).click()

    def PaymentoptionSave(self):
        self.driver.find_element(By.XPATH, self.button_save3_xpath).click()

    def CardHoldername(self, name):
        self.driver.find_element(By.XPATH, self.txtbox_name_xpath).send_keys(name)

    def Cardnumber(self, number):
        self.driver.find_element(By.XPATH, self.txtbox_number_xpath).send_keys(number)

    def Selectmonth(self):
        self.driver.find_element(By.XPATH, self.dropdown_month_xpath).click()
        self.driver.find_element(By.XPATH, self.select_month_xpath).click()

    def Selectyear(self):
        self.driver.find_element(By.XPATH, self.dropdown_year_xpath).click()
        self.driver.find_element(By.XPATH, self.select_year_xpath).click()

    def CVV(self, cvv):
        self.driver.find_element(By.XPATH, self.txtbox_cvv_xpath).send_keys(cvv)

    def PaymentInfoSave(self):
        self.driver.find_element(By.XPATH, self.button_save4_xpath).click()

    def ConfirmOrder(self):
        self.driver.find_element(By.XPATH, self.button_confirm_xpath).click()

    def OrderSuccessful(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_confirmorder_xpath).is_displayed()
        except:
            return False