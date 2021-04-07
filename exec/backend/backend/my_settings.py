DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'plantit',
        'USER': 'a101',
        'PASSWORD': 'secPlantItA101!@#',
        'HOST': 'j4a101.p.ssafy.io',
        'PORT': '3306',
    }
}


SECRET_KEY = {
    'secret':'wosi+z@g^%a%y(c%qqc0c!1qkymn3&bvyu8srvhl+&7z3md-+c', # settings.py의 SECRET_KEY
}

KAKAO_API_KEY = 'f1b1aefa5d6dde0c28145a76f64461cc'

JWT_SECRET_KEY = 'plantit101'

JWT_ALGORITHM = 'HS256'
