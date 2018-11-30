import requests
# TODO: auto-detect target URL? Could try sending a request to a known page and seeing what we get back?
# TODO: Do we need to include mac address parameters etc.?
TARGET_URL = 'https://guestwifi.fccps.org/login.html'

payload = {
    # TODO: Figure out what 4 means; it's statically set upon clicking agree
    'buttonClicked': '4',
    # TODO: Does it matter what goes here? I don't think so.
    'redirect_url': 'https://erikboesen.com',
    'err_flag': '0',
    'persistent': '1'  # for cookies or something?
}
session = requests.session()
requests.post(TARGET_URL, data=payload)
print(r.response)
