"""
URL configuration for weatherReservamos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from weatherReservamos.weather.views import WeatherForecastView


@api_view(['GET'])
def api_root(request):
    return Response({
        'forecast': reverse('forecast', request=request),
    })


urlpatterns = [
    path('', api_root),
    path('forecast/', WeatherForecastView.as_view(), name='forecast')
]
