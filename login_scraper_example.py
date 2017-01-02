
import requests
from lxml import html

USERNAME = "<USERNAME>"
PASSWORD = "<PASSWORD>"

LOGIN_URL = "http://www.marianos.com/signin?fromUrl=%2Fmypantry"
URL = "http://www.marianos.com/mypantry"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)

    # Create payload
    payload = {
        "usernameField": USERNAME, 
        "passwordField": PASSWORD, 
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    bucket_names = tree.xpath("//div[@class='row ng-scope']/a/text()")

    print(bucket_names)

if __name__ == '__main__':
    main()
