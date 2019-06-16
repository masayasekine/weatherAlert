import requests

def line_notify(request_message):
    '''
    引数で渡されたrequest_messageを送信するクラス
    '''

    url = 'https://notify-api.line.me/api/notify'
    access_token = 'ulAvGJYAv9gFaHev6aaEWysyN9YKpD3rjbsr5WFR5Og'

    payload = {'message' : request_message}
    headers = {'Authorization' : 'Bearer ' + access_token}
    res = requests.post(url, data=payload, headers=headers)
    print(res)