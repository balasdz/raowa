import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class Setup:
    def __init__(self):
        self.project_directory = os.path.dirname(os.path.abspath(__file__))
        self.chromedriver_path = os.path.join(self.project_directory, "chromedriver.exe")

    def init(self):
        # إعداد خيارات المستعرض
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # إعداد خدمة المستعرض
        service = Service(self.chromedriver_path)

        # تهيئة مستعرض Chrome
        self.browser = webdriver.Chrome(service=service, options=chrome_options)

    def close_browser(self):
        self.browser.quit()

class YouLikeHits:
    def __init__(self):
        self.setup = Setup()

    def get_point(self):
        point = self.setup.browser.find_element(By.ID, 'currentpoints')
        print('Your point is: ' + point.text)
        return point

    def go_to_website(self):
        # انتقال إلى موقع YouLikeHits
        self.setup.browser.get('https://www.youlikehits.com/login.php')
        WebDriverWait(self.setup.browser, 10).until(EC.presence_of_element_located((By.ID, 'username')))

        # ملء اسم المستخدم وكلمة المرور وتسجيل الدخول
        uid = self.setup.browser.find_element(By.ID, 'username')
        uid.send_keys('am plays')
        pwd = self.setup.browser.find_element(By.ID, 'password')
        pwd.send_keys('78945612')
        btn = self.setup.browser.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/center/form/table/tbody/tr[3]/td/span/input')
        btn.click()

        print('Getting credits... Please do not terminate the program.')
        while True:
            try:
                self.setup.browser.get('https://www.youlikehits.com/youtubenew2.php')
                WebDriverWait(self.setup.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="listall"]/center/a[1]')))
                yt_view = self.setup.browser.find_element(By.XPATH, '//*[@id="listall"]/center/a[1]')
                yt_view.click()

                element_present = EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Points Added')]"))
                WebDriverWait(self.setup.browser, 1000).until(element_present)

            except:
                while True:
                    self.setup.browser.get('https://www.youlikehits.com/websites.php')
                    WebDriverWait(self.setup.browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Visit")))
                    surf = self.setup.browser.find_element(By.LINK_TEXT, "Visit")
                    surf.click()
                    WebDriverWait(self.setup.browser, 10).until(EC.number_of_windows_to_be(2))
                    self.setup.browser.switch_to.window(self.setup.browser.window_handles[1])
                    self.setup.browser.close()
                    self.setup.browser.switch_to.window(self.setup.browser.window_handles[0])

    def close_browser(self):
        self.setup.close_browser()

if __name__ == "__main__":
    ylh = YouLikeHits()
    try:
        ylh.setup.init()
        ylh.go_to_website()
    except:
        ylh.get_point()
        print('Content not found to watch or surf. Refreshing webpage...')
    finally:
        ylh.close_browser()
