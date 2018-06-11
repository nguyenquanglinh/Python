import time
import traceback

from selenium import webdriver
from selenium.webdriver import ActionChains


class Driver:
    """
    tạo driver
    """

    def __init__(self):
        self.__get_driver()

    def __get_driver(self):
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_argument("user-data-dir=/tmp/chromedata")

        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome('/home/quang/Downloads/chromedriver', chrome_options=chrome_options)


class Facebook:
    """
    xác định đối tượng facebook có user_name,pass_word
    """

    def __init__(self, user_names, pass_words):
        self.user_name = user_names
        self.pass_word = pass_words
        self.driver = Driver().driver
        self.login_facebook()

    def login_facebook(self):
        import time
        x_paths = {"usernameTxtBox": "//input[@name='email']",
                   "passwordTxtBox": "//input[@name='pass']",
                   "submitButton": "//input[@value='Đăng nhập']"
                   }

        self.driver.get('https://www.facebook.com')
        kt = self.driver.find_elements_by_xpath("//div[@id='userNav']")
        if len(kt) != 1:
            self.driver.find_element_by_xpath("//input[@name='email']").send_keys(self.user_name)
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@name='pass']").send_keys(self.pass_word)
            time.sleep(1)
            self.driver.find_element_by_xpath(x_paths['submitButton']).click()


class AddFriendToGroup:
    def __init__(self, face_book):
        self.face_book = face_book

    def add_friends_to_group(self, str):
        self.face_book.driver.get(str)
        import time
        while True:
            xx = self.face_book.driver.find_elements_by_xpath("//button[text()='Thêm thành viên']")
            if len(xx) <= 1:
                self.face_book.driver.get(str)
            for i in xx:
                try:
                    self.face_book.driver.execute_script("window.scrollTo(0,480)")
                    i.click()
                    time.sleep(1)
                    ex = self.face_book.driver.find_elements_by_xpath("//h3[text()='Đã là thành viên']")
                    if len(ex) == 1:
                        self.face_book.driver.find_element_by_xpath("//a[text()='Đóng']").click()
                        self.face_book.driver.get(str)
                        time.sleep(2)
                except:
                    print('lỗi')
                    pass
            time.sleep(15)


class AddFriend:
    def __init__(self, face_book):
        self.face_book = face_book

    def add_friends(self):
        # self.face_book.driver.get("https://www.facebook.com/find-friends/browser/")
        import time
        time.sleep(3)
        while True:
            ds = self.face_book.driver.find_elements_by_xpath("//button[text()='Thêm bạn bè']")
            for i in ds:
                try:
                    actions = ActionChains(facebook.driver)
                    actions.move_to_element(i).perform()
                    i.click()
                    time.sleep(3)
                    need_close = self.face_book.driver.find_elements_by_xpath(
                        "//div[contains(text(),'Đề xuất kết bạn cho')]")

                    if len(need_close) == 1:
                        self.face_book.driver.find_element_by_xpath("(//a[text()='Đóng'])[2]").click()
                        print('bấm đóng')
                    else:
                        ex = self.face_book.driver.find_elements_by_xpath("//h3[text()='Người này có biết bạn không?']")
                        if len(ex) == 1:
                            self.face_book.driver.find_element_by_xpath("//a[text()='Hủy']").click()
                            print('bấm hủy')
                except:
                    pass


class SendMesage:
    def __init__(self, facebook):
        self.facebook = facebook

    def send(self):
        while True:
            href = self.facebook.driver.find_elements_by_xpath(
                '//a[contains(@href,"https://www.facebook.com/messages")]')
            for i in href:
                try:

                    self.facebook.driver.get(i.get_attribute('href'))
                    time.sleep(2)
                    thanhChat = self.facebook.driver.find_elements_by_xpath("//span[contains(@data-offset-key,'f')]")
                    print(thanhChat[0].get_attribute('data-text'))

                except:
                    print(traceback.format_exc())
                    self.facebook.driver.get('https://www.facebook.com')
                    break
                    pass


user_name = "phamlananh2809"
pass_word = "anhhoang"

str_r = "https://www.facebook.com/groups/1914454625240523/"
facebook = Facebook(user_name, pass_word)
abc = SendMesage(facebook)
abc.send()
add_friend = AddFriend(facebook)
add_friend.add_friends()
