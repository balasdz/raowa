# استخدام تكوين البيئة الافتراضي لمنفذ Railway
ARG PORT=8080
FROM python:3.9

# تعيين المتغيرات
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# تثبيت الاعتماديات
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# تعيين مسار العمل الافتراضي
WORKDIR /app

# نسخ الملفات إلى العمل الحالي
COPY . /app

# تشغيل التطبيق باستخدام Uvicorn عند تشغيل الحاوية
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
