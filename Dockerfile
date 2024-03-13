# استخدم صورة Selenium Standalone Chrome
FROM selenium/standalone-chrome:latest

# تعيين مجلد العمل
WORKDIR /usr/src/app

# نسخ ملف auto.py إلى مجلد العمل في الحاوية
COPY auto.py .

# تحديد الأمر الافتراضي لتشغيل عند بدء تشغيل الحاوية
CMD ["python3", "auto.py"]
