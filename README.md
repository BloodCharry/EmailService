<h1>Email Service</h1>

Это приложение позволяет создавать email-кампании, отправлять письма подписчикам и отслеживать их открытие.

Для работы приложения вам понадобятся:
<h4>Python 2.7</h4>
<h4>Django 1.9.9</h4>
<h4>Redis (для Celery)</h4>
<h4>Docker и Docker Compose (рекомендуется)</h4>

Установка
<h4>Клонируйте репозиторий:</h4>
```bash
git clone https://github.com/BloodCharry/EmailService.git
cd email-service
```

<h4>Установите зависимости:</h4>
Если вы используете Docker, зависимости будут установлены автоматически. Если нет, выполните:
```bash
pip install -r requirements.txt
```

<h4>Запустите контейнеры Docker:</h4>
```bash
docker-compose up --build
```

Приложение будет доступно по адресу: http://localhost:8000 .

Настройте SMTP
<h3>Создайте файл `.env` и внесите данные:</h3>
```plaintext
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-password'
SECRET_KEY = 'your-django-secretkey'
DJANGO_DEBUG=True
```

Использование
Создание email-кампании
<h4>Откройте админ-панель Django:</h4>
[http://localhost:8000/admin](http://localhost:8000/admin)
или модельное окно:
[http://localhost:8000/create-campaign/](http://localhost:8000/create-campaign/)

<h4>Создайте новую кампанию, указав тему, HTML-шаблон и запланированное время (если нужно).</h4>

Пример шаблона:

<p>Hello {{ first_name }} {{ last_name }},</p>
<p>This is a test email!</p>
<img src="http://localhost:8000/track-open/{{ subscriber_id }}/" alt="" style="display:none;" />

Отправка писем
После создания кампании Celery автоматически отправит письма подписчикам. Если указано запланированное время, письма будут отправлены в указанное время.

Отслеживание открытия писем
Когда подписчик открывает письмо, загружается изображение (например, 1x1 пиксель), которое вызывает метод track_open. Статус подписчика обновляется в базе данных.

