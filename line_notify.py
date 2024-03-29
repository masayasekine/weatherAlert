import requests
import os

def line_notify(request_message):
    '''
    引数で渡されたrequest_messageを送信するクラス
    コメント追加
    '''
    
    url = 'https://notify-api.line.me/api/notify'
    access_token = os.environ['NOTIFY_TOKEN']

    payload = {'message' : request_message}
    headers = {'Authorization' : 'Bearer ' + access_token}
    res = requests.post(url, data=payload, headers=headers)
    print(res)
