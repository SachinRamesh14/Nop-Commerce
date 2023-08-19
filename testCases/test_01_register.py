from pageObjects.RegisterPage import Register
from utilities.readproperties import ReadConfig
from utilities import customlogger

class Test_Registeration:
    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()

    def testcase_register(self, setup):
        self.logger.info("******** Register my ID ********")
        self.driver= setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseurl)
        self.registerobj = Register(self.driver)

        self.registerobj.Gotoregisterpage()
        self.registerobj.Gender()
        self.registerobj.Firstname("sachin")
        self.registerobj.Lastname("Ramesh")
        self.registerobj.DateOfBirth()
        self.registerobj.Email(self.email)
        self.registerobj.Companyname("ABC Ltd")
        self.registerobj.Password(self.password)
        self.registerobj.Confirmpassword(self.password)
        self.registerobj.ClickRegister()

        self.Registercomplete = self.registerobj.RegisterConformation()

        if self.Registercomplete == True:
            self.logger.info("******** Registration Complete testcase passed ***********")
            self.driver.close()
            assert True

        else:
            self.logger.info("********* Testcase Falied ***********")
            self.driver.close()
            assert False

        self.logger.info("******* TEST_REGISTER IS COMPLETED **********")