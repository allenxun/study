# -*- coding: UTF-8 -*-
import json
import requests
import sys

from bs4 import BeautifulSoup

s = requests.Session()

class JD:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
            'Referer': 'https://www.jd.com/'
        }

    def get_login_data(self):
        url = 'https://passport.jd.com/new/login.aspx'
        html = s.get(url, headers=self.headers).content
        soup = BeautifulSoup(html, 'lxml')
        display = soup.select('#o-authcode')[0].get('style')
        auth_code = ''
        if not display:
            auth_code_url = soup.select('#JD_Verification1')[0].get('src2')
            auth_code = self.get_auth_img(auth_code_url)
        uuid = soup.select('#uuid')[0].get('value')
        eid = soup.select('#eid')[0].get('value')
        fp = soup.select('input[name="fp"]')[0].get('value')  # session id
        _t = soup.select('input[name="_t"]')[0].get('value')  # token
        login_type = soup.select('input[name="loginType"]')[0].get('value')
        pub_key = soup.select('input[name="pubKey"]')[0].get('value')
        sa_token = soup.select('input[name="sa_token"]')[0].get('value')

        data = {
            'uuid': uuid,
            'eid': eid,
            'fp': fp,
            '_t': _t,
            'loginType': login_type,
            'loginname': self.username,
            'nloginpwd': self.password,
            'chkRememberMe': True,
            'authcode': '',
            'pubKey': pub_key,
            'sa_token': sa_token,
            'authCode': auth_code
        }
        return data

    def get_auth_img(self, url):
        auth_code_url = 'http:' + url
        auth_img = s.get(auth_code_url, headers=self.headers)
        file_path = sys.path[0] + '/auth_jpg/auth.jpg'
        
        with open(file_path, 'wb') as f:
            f.write(auth_img.content)
            
        code = self.get_auth_code(file_path)
        return code

    def get_auth_code(self,file_path):
        print(file_path)
        code = input("auth_code")
         
    def login(self):
        """
        登录
        :return:
        """
        url = 'https://passport.jd.com/uc/loginService'
        data = self.get_login_data()
        headers = {
            'Referer': 'https://passport.jd.com/uc/login?ltype=logout',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
            'X-Requested-With': 'XMLHttpRequest'
        }
        content = s.post(url, data=data, headers=headers).text
        result = json.loads(content[1: -1])
        return result

def handle():
    url = 'www.jd.com'
    pass


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    jd = JD(username, password)
    result = jd.login()
    if result.get('success'):
        print('sucess')
        handle()
    else:
        print('fail')
