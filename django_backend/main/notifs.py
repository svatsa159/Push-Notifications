import requests
def notify_users(message):
    PARAMS = {'message':message}
    r = requests.post(url = 'http://35.224.23.154:4000/personalised_notification/', params = PARAMS)