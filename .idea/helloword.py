from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver

class FacebookProcess:
    #định nghĩa thuộc tính
    def __init__(self, userName, passWord):
        self.userName = userName
        self.passWord=password
        self.driver=self.GetDriver()

    def GetDriver(self):


        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome('/home/quang/Downloads/chromedriver', chrome_options=chrome_options)
        return driver

    def LogIn():
        import time
        xpaths = {'usernameTxtBox': "//input[@name='email']",
                  'passwordTxtBox': "//input[@name='pass']",
                  'submitButton': "//input[@value='Đăng nhập']"
                  }

        driver.get('https://www.facebook.com')
        driver.find_element_by_xpath("//input[@name='email']").send_keys(userName)
        time.sleep(1)
        driver.find_element_by_xpath("//input[@name='pass']").send_keys(passWord)
        time.sleep(1)
        driver.find_element_by_xpath(xpaths['submitButton']).click()

    def AddFriends(username, password):
        driver.get("https://www.facebook.com/find-friends/browser/")
        time.sleep(5)
        while True:
            ds = driver.find_elements_by_xpath("//button[text()='Thêm bạn bè']")
            for i in ds:
                try:
                    driver.execute_script("window.scrollTo(0,1080)")
                    i.click()
                    time.sleep(3)
                    need_close = driver.find_elements_by_xpath("//div[contains(text(),'Đề xuất kết bạn cho')]")
                    if len(need_close) == 1:
                        driver.find_element_by_xpath("(//a[text()='Đóng'])[2]").click()
                    else:
                        ex = driver.find_elements_by_xpath("//h3[text()='Người này có biết bạn không?']")
                        if len(ex) == 1:
                            driver.find_element_by_xpath("//a[text()='Hủy']").click()
                    time.sleep(1)
                except:
                    pass


def AddFriendsToGroup(username, password):
    LogIn(username, password)
    driver.get(
        "https://www.facebook.com/groups/1914454625240523/?notif_id=1524675681093496&notif_t=group_added_to_group&ref=notif")
    while (True):
        xx = driver.find_elements_by_xpath("//button[text()='Thêm thành viên']")
        if len(xx) <= 1:
            driver.get(
                "https://www.facebook.com/groups/1914454625240523/?notif_id=1524675681093496&notif_t=group_added_to_group&ref=notif")
        for i in xx:
            try:
                driver.execute_script("window.scrollTo(0,480)")
                i.click()
                time.sleep(1)
                ex = driver.find_elements_by_xpath("//h3[text()='Đã là thành viên']")
                if len(ex) == 1:
                    driver.find_element_by_xpath("//a[text()='Đóng']").click()
                    driver.get(
                        "https://www.facebook.com/groups/1914454625240523/?notif_id=1524675681093496&notif_t=group_added_to_group&ref=notif")
                    print("đã là thành viên")
                    time.sleep(2)

            except:
                pass
        time.sleep(15)


username = "nguyen2anh2"
password = "Trang290994"
AddFriends('nguyen2anh2', 'Trang290994')
driver.quit()
