SECRET_KEY = 'django-insecure-67w-$g9%@$^$#ft^s72-k&-lx%r=8hj8l=c4cc96^ubhw%#iu('

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'login_databse',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}