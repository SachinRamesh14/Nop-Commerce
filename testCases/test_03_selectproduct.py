from pageObjects.LoginPage import Login
from pageObjects.HomePage import Order
from utilities import customlogger
from utilities.readproperties import ReadConfig

class Test_order:
    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()

    def test_select_product(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseurl)
        self.logger.info("******** select the products ********")

        self.loginobj = Login(self.driver)
        self.loginobj.GotoLogin()
        self.loginobj.Email(self.email)
        self.loginobj.Password(self.password)
        self.loginobj.Clicklogin()

        self.homepageobj = Order(self.driver)
        self.homepageobj.Search("apple")
        self.homepageobj.AddtoCard()
        self.homepageobj.SecondSearch("adidas")
        self.homepageobj.SelectSize()
        self.homepageobj.SelectColour()
        self.homepageobj.AddtoCard()

        self.Addtocart = self.homepageobj.SavetoCart()

        if self.Addtocart == True:
            self.logger.info("******** AddToCart Complete testcase passed ***********")
            self.driver.close()
            assert True

        else:
            self.logger.info("********* Testcase Falied ***********")
            self.driver.close()
            assert False

        self.logger.info("******* TEST_ORDER IS COMPLETED **********")


