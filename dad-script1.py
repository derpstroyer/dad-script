from bs4 import BeautifulSoup
import requests
import twilio
import time

while True:
    url = "http://www.nasdaq.com/symbol/exls"

    r = requests.get(url)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, 'html.parser')

    elem = soup.find(id='qwidget_netchange')

    raw_num = elem.text

    num = float(raw_num)

    if num > 0.25:
        username = 'ACa0a692ebfb58c431597f503662481c20'  # account sid
        password = 'ba8b3ee2ba0ba09646da1d97701cf777'  # auth token

        num_to_txt = '+18603248257'
        twilio_num = '+18607852138'

        message_body = ('The EXL stock has raised by' + str(num))

        base_url = 'https://api.twilio.com/2010-04-01/Accounts'
        message_url = base_url + '/' + username + '/Messages'

        auth_cred = (username, password)
        post_data = {
            "From": twilio_num,
            "To": num_to_txt,
            "Body": message_body,
        }
        r = requests.post(message_url, data=post_data, auth=auth_cred)
        time.sleep(600)
