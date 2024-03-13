# استخدام صورة بيثون
FROM python:3.8-slim

# تحديث وتثبيت الحزم الضرورية
RUN apt-get update && \
    apt-get install -y wget unzip curl && \
    apt-get clean

# تثبيت متصفح Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# نسخ ملف مدير التشغيل (ChromeDriver) إلى داخل الحاوية
COPY chromedriver /usr/bin/chromedriver

# تعيين الأذونات لملف مدير التشغيل
RUN chmod +x /usr/bin/chromedriver

# إنشاء وتحريك إلى دليل التطبيق
WORKDIR /app

# نسخ ملفات التطبيق إلى دليل العمل في الصورة
COPY . /app

# تثبيت متطلبات التطبيق
RUN pip install --no-cache-dir -r requirements.txt

# تشغيل التطبيق عند بدء تشغيل الصورة
CMD ["python", "auto.py"]
