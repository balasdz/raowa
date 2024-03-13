from flask import Flask, request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

app = Flask(__name__)

class YouLikeHits:
    def __init__(self):
        self.browser = None

    def init_browser(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def login(self):
        self.browser.get('https://www.youlikehits.com/login.php')
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, 'username')))
        username = self.browser.find_element(By.ID, 'username')
        username.send_keys('am plays')
        password = self.browser.find_element(By.ID, 'password')
        password.send_keys('78945612')
        login_button = self.browser.find_element(By.XPATH, '//input[@name="submit"]')
        login_button.click()

    def perform_task(self):
        while True:
            try:
                self.browser.get('https://www.youlikehits.com/websites.php')
                WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Visit")))
                surf = self.browser.find_element(By.LINK_TEXT, "Visit")
                surf.click()
                WebDriverWait(self.browser, 10).until(EC.number_of_windows_to_be(2))
                self.browser.switch_to.window(self.browser.window_handles[1])
                self.browser.close()
                self.browser.switch_to.window(self.browser.window_handles[0])
                break
            except:
                pass

    def close_browser(self):
        self.browser.quit()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        ylh = YouLikeHits()
        ylh.init_browser()
        ylh.login()
        ylh.perform_task()
        ylh.close_browser()
        return "Task completed successfully!"

if __name__ == '__main__':
    port = int(os.getenv("PORT", default=5050))
    app.run(host='0.0.0.0', port=port)
