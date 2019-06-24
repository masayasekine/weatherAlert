import requests
from system_constant import NOTIFY_TOKEN, NOTIFY_URL

def line_notify(request_message):
    '''
    引数で渡されたrequest_messageを送信するクラス
    コメント追加
    '''
    
    url = NOTIFY_URL
    access_token = NOTIFY_TOKEN

    payload = {'message' : request_message}
    headers = {'Authorization' : 'Bearer ' + access_token}
    res = requests.post(url, data=payload, headers=headers)
    print(res)
