from weather import call_weather_api
from line_notify import line_notify

if __name__=='__main__':

    weather_data = call_weather_api()
    rainy_flag = False
    request_message = ''

    for i in weather_data['list']:
        weather_id = i['weather'][0]['id']
        if(weather_id < 700):
            rainy_flag = True
        
    if(rainy_flag):
        request_message = '\n It\'s Rainy Today! \n Please go out with umbrella!'
    else:
        request_message = '\n It\'s Sunny Today!'

    if request_message:
        print(request_message)
        line_notify(request_message)
