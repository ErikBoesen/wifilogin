import requests
# TODO: auto-detect target URL? Could try sending a request to a known page and seeing what we get back?
# TODO: Do we need to include mac address parameters etc.?
# TODO: Must we give a user agent?
TARGET_URL = 'https://guestwifi.fccps.org/login.html'
TARGET_URL = 'https://guestwifi.fccps.org/fs/customwebauth/login.html?switch_url=https://guestwifi.fccps.org/login.html&ap_mac=50:17:ff:b3:e5:90&client_mac=d4:61:9d:25:2a:f6&wlan=FCCPS-Guest&redirect=detectportal.firefox.com/success.txt'

form = {
    # TODO: Figure out what 4 means; it's statically set upon clicking agree
    'buttonClicked': '4',
    # TODO: Does it matter what goes here? I don't think so.
    'redirect_url': 'https://erikboesen.com',
    'err_flag': '0',
    'persistent': '1'  # for cookies or something?
}
session = requests.session()
r = requests.post(TARGET_URL, data=form)
print(r.json())
