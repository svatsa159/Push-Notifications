import requests
def notify_users(message):
    PARAMS = {'message':message}
    r = requests.post(url = 'http://localhost:4000/personalised_notification/', params = PARAMS)