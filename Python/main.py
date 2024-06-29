import requests

url = "https://auth.mail.ru/cgi-bin/auth"
url2 = "https://mail.ru"

payload = {
'username':'serig85t@mail.ru',
'Login' :'serig85t@mail.ru',
'password': 'miting-ratitsid',
'Password': 'miting-ratitsid',
'g-recaptcha-response': '03AFcWeA7hTvgmuFMkrbbwI9aVj6xR1aPpDYrrAduiq_IvRMfNHOVUNBoQFHMSLqUSz265oXgwdMJaSCwkDGLpAnBWy0Jen5pm7BsQ6pNTStDsxtp3a6_sQKw8O45fqEtfFFeY8Lv0fGKwvp4B2IEeEJS7NIGXaFF5XaEaRunU36QmVHF6s6TLPOYxZR3rO_JALftLSjLgL22ZIJ5Ohstmac34RMkHV-BWtTON3WpPKXgkI92nsfhlfoIB2isvBMRjkCsJFzrCsIpMNVEk68PllEnnq-ngxNIDCgGN8Vq4k6bLMWLm416kby1cFkm0ZuERKYiJeyuiUDHr1dvwc5J3anZpmERu9apBHv5MsX4Nv7fMyOoj9DRBa9zOIpeQIYUVh66joDE6khOJivLB1nBpVmj9HpZ6JVEN5fQLJTwkBUkfYeRFJ3__ihH0rW2RaVIky5r2UKeBlZkCkwViZKv6T5FTNeUQhsp5m6tnTBNfI-8OSjgmQsguNJUEDT1sdurfS4-0MClc-T3Wn0SLgRjcrelIfvlqzcdjwdlv-8l3hrQlJHdGkMFzvCOFF4liQdg3lOAtZ_ZoiIbVzcUbcTt2Zzf372g92mhFkgxb59UCfxxcgHFVufPRdo66f900DKMT8CUy7h34vWiFmK4w11BJg8hrlvoU_gCD4IfNVhLq_3cJFHTCbwFCmFUGD2AEkQ6-DiMd3aZDWKVS_vfaYRR6D7C6kDHjBnDIPrPQBQRPeGS55OjzMF0-abzibRG0LRvQmXr0W1woTGWHp_OxWT9mxXda1gVFk5RNqgyNdU97OaH9jktst_7IIZ7KIh9o67wsXFXHJZuabRRziwr7iOMeu43lY3hgB74zlerPUi5QH6eT9KQBHoup04SEQbG01kOW6mOHNZdta_tqDMkPfR84GLVWH8tRif7MMzXdXJVCMvVYx4jFF8cb0DdpKyEno-AwnXF6OHHZc3hBq2aJDfNROynw2yIVm3SS-ze4ULLMg_4rZ4UIVTT0buNPUoLO8Yk-lwhdi5eZ9FKtjvdR11pQTdyiESlafIuQ7mFOEISpV1IiKUJab8yUj_RHzHOoBxpEtkAyf3WyqW35doo_0OkjX4XHBNy65_JtI_kOA7MwUn-Jm3Wo4pgonzbu6VHtzMHJ65IOOOnEP10EpHvkdzRzehwAA3WjMP029BYHapLZn12H8TlQzLDvZ_HXQ1NkJ3DWg498CIanR9qLJEm94rp6A2IuWaHY6gNuJ2SGt0Pfe7W7b4kRehx-ad4-iURD5_wspWoCRkNIeww8eVAPFe-dsECNnyRSU2CvFvmCmUwRU0pKe535HIg1zdiXxGxCGL44CvvfrR53jaHhVkY3tRm-1Ld9tfnO9ttcAYnPygRZxXcz8pJT-UBZ_bDtjfKeDtZ85ZHoLCARZTjzOAjBi6K5-JP4_D8u3G0s4MGtvg4PasWlyv-4ctkugxGfFUHx6PIDs1Cs-48HSQYkrBhfEEQo1xvm3h1Xpoa40VoaFtWiHNNGZwwiWTTy_hjziZjHOnaWikBEuHKLLnN_9Jke42pCOJ2LEOm0fIuLE6NIxsuClQtuiNvxX8ajDGs7BAEttPUNUduhA-O_iCOfaSD4_ZQJITEGGDY9Zx4GjNamUROwUGKL49wEu4WBmsfu0F4lhgVjObhS6ck12AbYP83u5py8d98n7BdxrKDS-3olPQHucDIU0FgKvbM3bpeK-7uEgFlTwTnFc8hmvKoYfincRJ5TfpDm2Z1rEjz6FwIHsvXeNbvK6llU9z4DeK9dKumhcz8CLL7tVdFqtKieOeYeAdWjrjJgjF8s-QoHkmQtN4MW8brkk7q3armyGlMeiLWlF3D_sDBAJfyuT_U5YuWxATRrsCHi8M46fZYwkH9UC8Ajp_LruChpLAPN7AA4orO5JS8PbESdSkSp4gvQpEP8uGuzFe3Lwshf2diyatE5NvbGuISoZCUXpeuRe4g',
'saveauth': '1',
'new_auth_form': '1',
'FromAccount': 'opener=account&twoSteps=1',
'act_token': 'fc2f1a064a534542ae2dea0668e11ed9',
'page': 'https://e.mail.ru/messages/inbox?authid=lxzzg21z.6&back=1&dwhsplit=s10273.b1ss12743s&from=login&x-login-auth=1',
'back': '1',
'lang': 'ru_RU'}


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
s = requests.Session()

#response = s.get('https://auth.mail.ru')
r1 = s.request("GET", url = url2, headers=headers)
response = s.request("POST", url, data=payload, headers=headers)
with open('file_mail_ru.html', 'w+', encoding= "utf-8") as file:
    file.write(response.text)

print(r1.cookies)
print(response.cookies)
print(response.status_code)
print(response.url)
print(response.headers)


print(response.text)

