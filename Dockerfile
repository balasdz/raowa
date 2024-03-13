# استخدام صورة بيثون
FROM python:3.8-slim

# تحديث وتثبيت الحزم الضرورية
RUN apt-get update && \
    apt-get install -y wget unzip curl && \
    apt-get clean

# تنزيل وفك ضغط متصفح Chrome
RUN wget https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.128/linux64/chrome-linux64.zip && \
    unzip chrome-linux64.zip && \
    mv chrome-linux64 /usr/bin/chrome && \
    chmod +x /usr/bin/chrome && \
    rm chrome-linux64.zip

# تنزيل وفك ضغط مدير التشغيل بالإصدار المطلوب
RUN wget https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.128/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    mv chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver-linux64.zip

# إنشاء وتحريك إلى دليل التطبيق
WORKDIR /app

# نسخ ملفات التطبيق إلى دليل العمل في الصورة
COPY . /app

# تثبيت متطلبات التطبيق
RUN pip install --no-cache-dir -r requirements.txt

# تشغيل التطبيق عند بدء تشغيل الصورة
CMD ["python", "auto.py"]
