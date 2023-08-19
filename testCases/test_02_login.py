import time
from pageObjects.LoginPage import Login
from utilities import customlogger
from utilities.readproperties import ReadConfig

class Test_Login:

    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()

    def test_login(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseurl)
        self.loginobj = Login(self.driver)

        self.logger.info("********* NAGATIVE LOG IN ********")
        self.loginobj.GotoLogin()
        self.loginobj.Email("bvc@gmail.com")
        self.loginobj.Password("gghgb")
        self.loginobj.Clicklogin()

        self.logger.info("******* input wrong password ***********")
        self.loginobj.GotoLogin()
        self.loginobj.Email(self.email)
        self.loginobj.Password("password")
        self.loginobj.Clicklogin()

        self.logger.info("******** POSITIVE LOG IN ************")
        self.loginobj.GotoLogin()
        self.loginobj.Email(self.email)
        self.loginobj.Password(self.password)
        self.loginobj.Clicklogin()
        time.sleep(2)

        self.logger.info("******** Test Login successful ********")
        self.driver.close()

