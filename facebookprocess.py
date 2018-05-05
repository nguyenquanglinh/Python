from selenium import webdriver


class Driver:
    """
    tạo driver
    """

    def __init__(self):
        self.__get_driver()

    def __get_driver(self):
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options = webdriver.ChromeOptions()
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

    def login_facebook(self) -> object:
        import time
        x_paths = {"usernameTxtBox": "//input[@name='email']",
                   "passwordTxtBox": "//input[@name='pass']",
                   "submitButton": "//input[@value='Đăng nhập']"
                   }

        self.driver.get('https://www.facebook.com')
        self.driver.find_element_by_xpath("//input[@name='email']").send_keys(self.user_name)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='pass']").send_keys(self.pass_word)
        time.sleep(1)
        self.driver.find_element_by_xpath(x_paths['submitButton']).click()


class AddFriend:
    def __init__(self, face_book):
        self.face_book = face_book

    def add_friends(self):
        self.face_book.driver.get("https://www.facebook.com/find-friends/browser/")
        import time
        time.sleep(5)
        while True:
            ds = self.face_book.driver.find_elements_by_xpath("//button[text()='Thêm bạn bè']")
            for i in ds:
                try:
                    self.face_book.driver.execute_script("window.scrollTo(0,1080)")
                    i.click()
                    time.sleep(3)
                    need_close = self.driver.find_elements_by_xpath("//div[contains(text(),'Đề xuất kết bạn cho')]")
                    if len(need_close) == 1:
                        self.driver.find_element_by_xpath("(//a[text()='Đóng'])[2]").click()
                    else:
                        ex = self.face_book.driver.find_elements_by_xpath("//h3[text()='Người này có biết bạn không?']")
                        if len(ex) == 1:
                            self.face_book.driver.find_element_by_xpath("//a[text()='Hủy']").click()
                    time.sleep(1)
                except:
                    pass


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
                    pass
            time.sleep(15)


user_name = "nguyen2anh2"
pass_word = "Trang290994"
str_r = "https://www.facebook.com/groups/1914454625240523/"
facebook = Facebook(user_name, pass_word)
add_friend = AddFriend(facebook)
add_friend.add_friends()
