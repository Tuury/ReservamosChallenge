RESULT_TYPE = 'result_type'
CITY = 'city'
COUNTRY = 'country'
MEXICO = 'México'
DAY_FORMAT = "%Y-%m-%d"
API_KEY='a5a47c18197737e8eeca634cd6acb581'# in a production environment this would be saved in a local variable and loaded from settings.py
OPENWEATHER_URL = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly&appid={}&units=metric'
RESERVAMOS_URL = 'https://search.reservamos.mx/api/v2/places?q={}'