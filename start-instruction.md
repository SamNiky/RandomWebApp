The project is running with django-celery-redis chain

For start:
1. In 4 terminals go directory RandomWebApp/Random/ 
---- cd RandomWebApp/random
   
2. Run Redis with brew, or other methods in terminal 1
---- brew services start redis
   
2.1 Check start redis
---- redis-cli ping
----> PONG

2.2 Run redis server
---- redis-server
   
3. Run django server in terminal 2
---- python manage.py runserver
   
4. Run celery beat in terminal 3
---- celery -A Random beat
   
5. Run celery worker in terminal 4
---- celery -A Random worker -l INFO