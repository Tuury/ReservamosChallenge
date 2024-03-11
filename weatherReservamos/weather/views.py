from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from weatherReservamos.weather.constants import API_KEY, OPENWEATHER_URL, DAY_FORMAT, RESERVAMOS_URL
from weatherReservamos.weather.utils import filter_cities, make_request


class WeatherForecastView(APIView):
    """
    Endpoint API to get the weather forecast.

    Parameters:
    - name (str): The name of the city.

    Returns:
    list of cities with the forecast for the next 7 days.

    """

    def get_coordinates(self, city_name) -> list:
        response = make_request(RESERVAMOS_URL.format(city_name))
        cities = list(filter(filter_cities, response))
        if cities:
            return [(city.get('lat'), city.get('long'), city.get('display')) for city in cities if
                    city.get('city_ascii_name', '').startswith(city_name)]
        return []

    def get(self, request, *args, **kwargs) -> Response:
        city_name = request.query_params.get('name', '')
        if not city_name:
            return Response({'error': 'name parameter required'})

        coordinates = self.get_coordinates(city_name)
        if coordinates:
            return Response(self.get_weather(coordinates))
        else:
            return Response({'error': 'City not found'}, status=404)

    def get_weather(self, coordinates) -> list:
        cities_forecast = []
        for c in coordinates:
            latitude, longitud, city_name = c
            weather_forecast = self.get_weather_for_coordinates(latitude, longitud)
            cities_forecast.append({city_name: weather_forecast})
        return cities_forecast

    def get_weather_for_coordinates(self, latitude, longitude) -> list:
        data = make_request(OPENWEATHER_URL.format(latitude, longitude, API_KEY))
        daily_temperature = [{
            'date': datetime.fromtimestamp(day.get('dt', '')).strftime(DAY_FORMAT),
            'max_temperature': day.get('temp', {}).get('max'),
            'min_temperature': day.get('temp', {}).get('min'),
        } for day in data.get('daily', [])]

        return daily_temperature
