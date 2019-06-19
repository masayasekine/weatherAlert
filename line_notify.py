import requests

def line_notify(request_message):
    '''
    引数で渡されたrequest_messageを送信するクラス
    '''

    url = 'https://notify-api.line.me/api/notify'
    access_token = 'FuKzJ3QyUXpYC50rLvgVMRascjWSksFBlExeWOGEBW3'

    payload = {'message' : request_message}
    headers = {'Authorization' : 'Bearer ' + access_token}
    res = requests.post(url, data=payload, headers=headers)
    print(res)