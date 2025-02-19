<h1>Email Service</h1>
Это приложение позволяет создавать email-кампании, отправлять письма подписчикам и отслеживать их открытие.

# Для работы приложения вам понадобятся:

<h4>Python 2.7</h4>
<h4>Django 1.9.9</h4>
<h4>Redis (для Celery)</h4>
<h4>Docker и Docker Compose (рекомендуется)</h4>

# Установка
<h4>Клонируйте репозиторий</h4>
<h4>git clone 'https://github.com/BloodCharry/EmailService.git'</h4>
cd email-service

# Установите зависимости
<p>Если вы используете Docker, зависимости будут установлены автоматически. Если нет, выполните:</p>
<h4>pip install -r requirements.txt</h4>

# Запустите контейнеры Docker
<h4>docker-compose up --build</h4>
<h4>Приложение будет доступно по адресу: 'http://localhost:8000'.</h4>

# Настройте SMTP
<h3>Создайте файл .env и внесите данные</h3>

# Для отправки писем настройте SMTP в файле settings.py:
 <h4>EMAIL_HOST_USER = 'your-email@example.com'</h4>
 <h4>EMAIL_HOST_PASSWORD = 'your-password'</h4>
 <h4>SECRET_KEY = 'your-django-secretkey'</h4>
 <h4>DJANGO_DEBUG=True</h4>

# Использование
<h3>Создание email-кампании</h3>
<h4>Откройте админ-панель Django: 'http://localhost:8000/admin' или модельное окно 'http://localhost:8000/create-campaign/'</h4>
<h4>Создайте новую кампанию, указав тему, HTML-шаблон и запланированное время (если нужно).</h4>

Пример шаблона:
<p><p>Hello {{ first_name }} {{ last_name }},</p></p>
<p>This is a test email!</p>
<img src="http://localhost:8000/track-open/{{ subscriber_id }}/" alt="" style="display:none;" />

# Отправка писем
<p>После создания кампании Celery автоматически отправит письма подписчикам. Если указано запланированное время, письма будут отправлены в указанное время.</p>

# Отслеживание открытия писем
<p>Когда подписчик открывает письмо, загружается изображение (например, 1x1 пиксель), которое вызывает метод track_open. Статус подписчика обновляется в базе данных.</p>
