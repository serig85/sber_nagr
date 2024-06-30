import requests


s = requests.Session()
payload = {
    'cf': 'akk-login',
    'ulogin': 'serig85t',
    'pass': 'mitingratitsid',
    'x': '9',
    'y': '12'
}
url = 'https://www.wmmail.ru/index.php'

s.post(url=url, data=payload)
response = s.get('https://www.wmmail.ru/index.php?cf=html2-viewallloginakk')

print(response.text)
with open('file_wmmail.html', "w+", encoding="windows-1251") as file:
    file.write(response.text)
