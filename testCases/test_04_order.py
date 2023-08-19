from pageObjects.LoginPage import Login
from pageObjects.ShoppingCartPage import Cart
from utilities import customlogger
from utilities.readproperties import ReadConfig

class Test_Shipping:
    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()

    def test_order_confirmation(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseurl)
        self.logger.info("******** Order the products ********")

        self.loginobj = Login(self.driver)
        self.loginobj.GotoLogin()
        self.loginobj.Email(self.email)
        self.loginobj.Password(self.password)
        self.loginobj.Clicklogin()

        self.cartobj = Cart(self.driver)
        self.cartobj.Gotocart()
        self.cartobj.ClickCheckbox()
        self.cartobj.Clickcheckout()
        self.cartobj.Country()
        self.cartobj.State()
        self.cartobj.City("mumbai")
        self.cartobj.Address("24, west street")
        self.cartobj.Zipcode("321654")
        self.cartobj.Phone("9876543210")
        self.cartobj.BillingSave()
        self.logger.info("****** Biiling address saved ******")

        self.cartobj.Shippingway()
        self.cartobj.Shippingsave()
        self.logger.info("****** Shipping way saved ******")

        self.cartobj.Paymentoption()
        self.cartobj.PaymentoptionSave()
        self.logger.info("****** payment option saved ******")

        self.cartobj.CardHoldername("sachin")
        self.cartobj.Cardnumber("6069943131613065")
        self.cartobj.Selectmonth()
        self.cartobj.Selectyear()
        self.cartobj.CVV("113")
        self.cartobj.PaymentInfoSave()
        self.logger.info("****** Payment Info Save ******")

        self.cartobj.ConfirmOrder()

        self.Orderconfirm = self.cartobj.OrderSuccessful()

        if self.Orderconfirm == True:
            self.logger.info("******** order Complete testcase passed ***********")
            self.driver.close()
            assert True

        else:
            self.logger.info("********* Testcase Falied ***********")
            self.driver.close()
            assert False

        self.logger.info("******* TEST_Shipping IS COMPLETED **********")
