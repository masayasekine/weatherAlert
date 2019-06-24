import json
import requests
from system_constant import WEATHER_KEY


def call_weather_api():
    '''
    APIで天気予報を取得するクラス
    '''
    api_key = WEATHER_KEY
    api = 'http://api.openweathermap.org/data/2.5/forecast?units=metric&q={city}&APPID={key}&cnt={limit}'

    city_name = 'Tokyo,JP'
    # cntパラメータで取得する行数を指定可能（指定しないと3時間単位で5日分来るので膨大な行数になる）
    request_line = 6
    url = api.format(city=city_name, key=api_key, limit=request_line)

    # APIを叩いて結果をJSONで取得
    response = requests.get(url)
    data = response.json()

    return data
