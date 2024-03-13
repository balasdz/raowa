import os
from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

class YouLikeHits:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")

        self.service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=self.service, options=self.chrome_options)

    def get_point(self):
        self.browser.get('https://www.youlikehits.com/')
        point = self.browser.find_element(By.ID, 'currentpoints')
        print('Your point is: ' + point.text)
        return point

    def go_to_website(self):
        # انتقال إلى موقع YouLikeHits
        self.browser.get('https://www.youlikehits.com/login.php')
        username = self.browser.find_element(By.ID, 'username')
        username.send_keys('your_username_here')
        password = self.browser.find_element(By.ID, 'password')
        password.send_keys('your_password_here')
        login_button = self.browser.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/center/form/table/tbody/tr[3]/td/span/input')
        login_button.click()

        print('Getting credits... Please do not terminate the program.')
        while True:
            try:
                self.browser.get('https://www.youlikehits.com/youtubenew2.php')
                yt_view = self.browser.find_element(By.XPATH, '//*[@id="listall"]/center/a[1]')
                yt_view.click()

                WebDriverWait(self.browser, 1000).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Points Added')]")))

            except:
                self.browser.get('https://www.youlikehits.com/websites.php')
                surf = self.browser.find_element(By.LINK_TEXT, "Visit")
                surf.click()
                WebDriverWait(self.browser, 10).until(EC.number_of_windows_to_be(2))
                self.browser.switch_to.window(self.browser.window_handles[1])
                self.browser.close()
                self.browser.switch_to.window(self.browser.window_handles[0])

    def close_browser(self):
        self.browser.quit()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        ylh = YouLikeHits()
        try:
            ylh.go_to_website()
            return ylh.get_point().text
        finally:
            ylh.close_browser()
    return "OK"

if __name__ == '__main__':
    port = int(os.getenv("PORT", default=5050))
    app.run(host='0.0.0.0', port=port)
