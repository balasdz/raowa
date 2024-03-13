from flask import Flask, request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.service import Service
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
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

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
        self.browser.get('https://www.youlikehits.com/youtubenew2.php')
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="listall"]/center/a[1]')))
        youtube_button = self.browser.find_element(By.XPATH, '//*[@id="listall"]/center/a[1]')
        youtube_button.click()
        WebDriverWait(self.browser, 1000).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Points Added')]")))

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
