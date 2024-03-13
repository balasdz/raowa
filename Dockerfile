# استخدام صورة بيثون
FROM python:3.8-slim

# تحديث وتثبيت الحزم الضرورية
RUN apt-get update && \
    apt-get install -y wget unzip curl && \
    apt-get clean

# تحميل وتثبيت متصفح Chrome ومفتاحه
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get -y update && \
    apt-get -y install google-chrome-stable

# تحميل وتثبيت مدير التشغيل
RUN wget https://chromedriver.storage.googleapis.com/94.0.4606.41/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver

# إنشاء وتحريك إلى دليل التطبيق
WORKDIR /app

# نسخ ملفات التطبيق إلى دليل العمل في الصورة
COPY auto.py /app/

# تثبيت متطلبات التطبيق
RUN pip install --no-cache-dir selenium

# تشغيل التطبيق عند بدء تشغيل الصورة
CMD ["python", "auto.py"]
