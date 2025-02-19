# Email Service

Это приложение позволяет создавать email-кампании, отправлять письма подписчикам и отслеживать их открытие.

## Для работы приложения вам понадобятся:

- **Python 2.7**
- **Django 1.9.9**
- **Redis** (для Celery)
- **Docker и Docker Compose** (рекомендуется)

## Установка

### Клонируйте репозиторий:
```
git clone https://github.com/BloodCharry/EmailService.git
cd email-service
```

## Установите зависимости:
### Если вы используете Docker, зависимости будут установлены автоматически. Если нет, выполните:
## pip install -r requirements.txt

Запустите контейнеры Docker:
```
docker-compose up --build
```

## Настройте SMTP
### Создайте файл .env и внесите данные:
```
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-password'
SECRET_KEY = 'your-django-secretkey'
DJANGO_DEBUG=True
```

## Использование
### Создание email-кампании
###Откройте админ-панель Django:
```
http://localhost:8000/admin
```

### или модельное окно:
```
http://localhost:8000/create-campaign/
```

## Создайте новую кампанию, указав тему, HTML-шаблон и запланированное время (если нужно).

### Пример шаблона:
```
<p>Hello {{ first_name }} {{ last_name }},</p>
<p>This is a test email!</p>
<img src="http://localhost:8000/track-open/{{ subscriber.id }}/" alt="" style="display:none;" />
```

## Отправка писем
### После создания кампании Celery автоматически отправит письма подписчикам. Если указано запланированное время, письма будут отправлены в указанное время.

## Отслеживание открытия писем
### Когда подписчик открывает письмо, загружается изображение (например, 1x1 пиксель), которое вызывает метод track_open. Статус подписчика обновляется в базе данных.
