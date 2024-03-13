# استخدام صورة بيثون
FROM python:3.8-slim

# تحديث وتثبيت الحزم الضرورية
RUN apt-get update && \
    apt-get install -y wget unzip curl && \
    apt-get clean

# تنزيل وتثبيت متصفح Chrome من خلال ملف deb
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# تنزيل وتثبيت مدير التشغيل
RUN wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE -O latest_release && \
    wget https://chromedriver.storage.googleapis.com/$(cat latest_release)/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver_linux64.zip latest_release

# إنشاء وتحريك إلى دليل التطبيق
WORKDIR /app

# نسخ ملفات التطبيق إلى دليل العمل في الصورة
COPY . /app

# تثبيت متطلبات التطبيق
RUN pip install --no-cache-dir -r requirements.txt

# تشغيل التطبيق عند بدء تشغيل الصورة
CMD ["python", "auto.py"]
