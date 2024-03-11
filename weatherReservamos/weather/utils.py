import logging
import requests
from requests import RequestException

from weatherReservamos.weather.constants import RESULT_TYPE, CITY, COUNTRY, MEXICO

logger = logging.getLogger(__name__)


def filter_cities(data):
    return data.get(RESULT_TYPE, '') == CITY and data.get(COUNTRY, '') == MEXICO


def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        logger.warning(f"{url}, {e}")
    return []
