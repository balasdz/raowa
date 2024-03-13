from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# تهيئة متصفح Chrome
driver = webdriver.Chrome()

try:
    # افتح موقع YouLikeHits
    driver.get("https://www.youlikehits.com/login.php")

    # انتظر حتى يتم تحميل حقل اسم المستخدم وأدخل اسم المستخدم وكلمة المرور
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    username_field.send_keys("اسم المستخدم هنا")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("كلمة المرور هنا")

    # انتظر حتى يتم تحميل زر تسجيل الدخول وانقر عليه
    login_button = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/center/form/table/tbody/tr[3]/td/span/input")
    login_button.click()

    # انتظر حتى يتم تحميل صفحة النقاط الحالية
    current_points = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "currentpoints")))
    print("نقاطك الحالية: " + current_points.text)

    # قم بزيارة صفحة المواقع لجمع النقاط
    driver.get("https://www.youlikehits.com/websites.php")

    # انتظر حتى يتم تحميل الزر "Visit" وقم بالضغط عليه لزيارة الموقع
    visit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Visit")))
    visit_button.click()

    # انتظر حتى يتم فتح نافذة جديدة
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    # قم بتحويل التركيز إلى النافذة الجديدة وبعد ذلك أغلقها
    driver.switch_to.window(driver.window_handles[1])
    driver.close()

    # استعد التركيز إلى النافذة الأصلية
    driver.switch_to.window(driver.window_handles[0])

finally:
    # بعد الانتهاء، أغلق المتصفح
    driver.quit()
