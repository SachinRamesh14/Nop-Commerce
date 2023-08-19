from selenium.webdriver.common.by import By

class Order:

    txtbox_search_xpath = "//input[@name='q']"
    select_searchresult_xpath = "//span[contains(text(),'Apple MacBook Pro 13-inch')]"
    button_addcart_xpath = "//button[@id='add-to-cart-button-4']"
    select_searchresult2_xpath = "//ul[@id='ui-id-1']"
    dropdown_size_xpath = "//select[@name='product_attribute_9']"
    select_size_xpath = "//*[@data-attr-value='24']"
    click_colour_xpath = "//*[@id='color-squares-10']/li[3]/label/span/span"
    txt_validate_xpath = "//*[contains(text(),'The product has been added to your ')]"

    def __init__(self, driver):
        self.driver = driver


    def Search(self, productname):
        self.driver.find_element(By.XPATH, self.txtbox_search_xpath).send_keys(productname)
        self.driver.find_element(By.XPATH, self.select_searchresult_xpath).click()

    def AddtoCard(self):
        self.driver.find_element(By.XPATH, self.button_addcart_xpath).click()

    def SecondSearch(self,entername):
        self.driver.find_element(By.XPATH, self.txtbox_search_xpath).send_keys(entername)
        self.driver.find_element(By.XPATH, self.select_searchresult2_xpath).click()

    def SelectSize(self):
        self.driver.find_element(By.XPATH, self.dropdown_size_xpath).click()
        self.driver.find_element(By.XPATH, self.select_size_xpath).click()

    def SelectColour(self):
        self.driver.find_element(By.XPATH, self.click_colour_xpath).click()

    def SavetoCart(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_validate_xpath).is_displayed()
        except:
            return False
