import requests
# TODO: auto-detect target URL? Could try sending a request to a known page and seeing what we get back?
# TODO: Do we need to include mac address parameters etc.?
# TODO: Must we give a user agent?
TARGET_URL = 'https://guestwifi.fccps.org/fs/customwebauth/login.html?switch_url=https://guestwifi.fccps.org/login.html&ap_mac=50:17:ff:b3:e5:90&client_mac=d4:61:9d:25:2a:f6&wlan=FCCPS-Guest&redirect=detectportal.firefox.com/success.txt'
TARGET_URL = 'https://guestwifi.fccps.org/login.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Cookie': '_ga=GA1.2.1537255449.1539107283; nmstat=1545096671460',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded',
}
form = {
    # TODO: Figure out what 4 means; it's statically set upon clicking agree
    'buttonClicked': '4',
    # TODO: Does it matter what goes here? I don't think so.
    'redirect_url': 'https://erikboesen.com',
    'err_flag': '0',
}
session = requests.Session()
r = session.post(TARGET_URL, data=form)
print(r.text)
