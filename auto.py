import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YouLikeHits:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.browser = webdriver.Chrome(options=chrome_options)

    def get_point(self):
        self.browser.get('https://www.youlikehits.com/login.php')
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, 'username')))

        uid = self.browser.find_element(By.ID, 'username')
        uid.send_keys('am plays')
        pwd = self.browser.find_element(By.ID, 'password')
        pwd.send_keys('78945612')
        btn = self.browser.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/center/form/table/tbody/tr[3]/td/span/input')
        btn.click()

        print('Getting credits... Please do not terminate the program.')
        while True:
            try:
                self.browser.get('https://www.youlikehits.com/youtubenew2.php')
                WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="listall"]/center/a[1]')))
                yt_view = self.browser.find_element(By.XPATH, '//*[@id="listall"]/center/a[1]')
                yt_view.click()

                element_present = EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Points Added')]"))
                WebDriverWait(self.browser, 1000).until(element_present)

            except:
                while True:
                    self.browser.get('https://www.youlikehits.com/websites.php')
                    WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Visit")))
                    surf = self.browser.find_element(By.LINK_TEXT, "Visit")
                    surf.click()
                    WebDriverWait(self.browser, 10).until(EC.number_of_windows_to_be(2))
                    self.browser.switch_to.window(self.browser.window_handles[1])
                    self.browser.close()
                    self.browser.switch_to.window(self.browser.window_handles[0])

if __name__ == "__main__":
    ylh = YouLikeHits()
    ylh.get_point()
