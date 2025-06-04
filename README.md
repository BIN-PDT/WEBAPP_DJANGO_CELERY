**1. PROJECT**

```
git clone https://github.com/BIN-PDT/WEBAPP_DJANGO_CELERY.git && rm -rf WEBAPP_DJANGO_CELERY/.git
```

_For privacy reasons, replace the sensitive information in this project with your own._

-   _Register Message Broker to obtain `BROKER_URL` for Celery_.

-   _Register OAuth Application with each Social Provider to obtain `CLIENT_ID` & `CLIENT_SECRET`_.

-   _Replace `EMAIL_ADDRESS` & `EMAIL_PASSWORD` (Application Password) with your Gmail Account_.

-   _Generate `SECRET_KEY`_.

    ```
    python manage.py shell
    ```

    ```python
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
    exit()
    ```

**2. VIRTUAL ENVIRONMENT**

```
python -m venv .venv
```

```
.venv\Scripts\activate.bat
```

**3. DEPENDENCY**

```
python.exe -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

**4. DATABASE**

```
python manage.py migrate
```

**5. RUN CELERY**

```
celery -A a_core worker -P solo -E -l info
```

```
celery -A a_core beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

```
celery -A a_core flower
```

**6. RUN APPLICATION**

```
python manage.py runserver
```
