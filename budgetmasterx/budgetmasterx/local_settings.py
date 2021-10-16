SECRET_KEY = 'django-insecure-+nua^&+%eye35k$c07+2#_qg++b+_oz=fu+tuu5k^gfq*k2x#7'

DATABASES ={
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'budgetmasterx_database',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit':True
        }
    }
}