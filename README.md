<h1>Email Service</h1>
Это приложение позволяет создавать email-кампании, отправлять письма подписчикам и отслеживать их открытие.

# Для работы приложения вам понадобятся:

<h4>Python 2.7</h4>
<h4>Django 1.9.9</h4>
<h4>Redis (для Celery)</h4>
<h4>Docker и Docker Compose (рекомендуется)</h4>

# Установка
1. Клонируйте репозиторий
git clone https://github.com/BloodCharry/EmailService.git
cd email-service

3. Установите зависимости
Если вы используете Docker, зависимости будут установлены автоматически. Если нет, выполните:
pip install -r requirements.txt

3. Запустите контейнеры Docker
docker-compose up --build
Приложение будет доступно по адресу: http://localhost:8000 .

1. Настройте SMTP
Создайте файл .env и внесите данные

Для отправки писем настройте SMTP в файле settings.py:
 EMAIL_HOST_USER = 'your-email@example.com'
 EMAIL_HOST_PASSWORD = 'your-password'
 SECRET_KEY = 'your-django-secretkey'
 DJANGO_DEBUG=True

Использование
1. Создание email-кампании
Откройте админ-панель Django: http://localhost:8000/admin или модельное окно http://localhost:8000/create-campaign/
Создайте новую кампанию, указав тему, HTML-шаблон и запланированное время (если нужно).

Пример шаблона:
<p>Hello {{ first_name }} {{ last_name }},</p>
<p>This is a test email!</p>
<img src="http://localhost:8000/track-open/{{ subscriber_id }}/" alt="" style="display:none;" />

2. Отправка писем
После создания кампании Celery автоматически отправит письма подписчикам. Если указано запланированное время, письма будут отправлены в указанное время.

3. Отслеживание открытия писем
Когда подписчик открывает письмо, загружается изображение (например, 1x1 пиксель), которое вызывает метод track_open. Статус подписчика обновляется в базе данных.
