from getpass import getpass
import requests
import json

def put(url, payload):
    url = 'https://' + ip + ':' + port + url
    r = requests.put(url, data=json.dumps(payload), auth=(username,password), headers=headers, verify=False)
    print (r.status_code)
    return (r.text)

def post(url, payload):
    url = 'https://' + ip + ':' + port + url
    r = requests.post(url, data=json.dumps(payload), auth=(username,password), headers=headers, verify=False)
    print (r.status_code)
    print (r.text)
    return (r)

def patch(url, payload):
    url = 'https://' + ip + ':' + port + url
    r = requests.post(url, data=json.dumps(payload), auth=(username,password), headers=headers, verify=False)
    print (r.status_code)
    print (r.text)
    return (r)

def delete(url):
    url = 'https://' + ip + ':' + port + url
    r = requests.delete(url, auth=(username,password), headers=headers, verify=False)
    print (r.status_code)
    print (r.text)

def get(url):
    url = 'https://' + ip + ':' + port + url
    payload = {'deep': True }
    r = requests.get(url, auth=(username,password), headers=headers, verify=False, params=payload)
    print (r.status_code)
    #print(r.text)
    return r

requests.packages.urllib3.disable_warnings()
headers = {'Connection': 'Close', 'Accept': 'application/json', 'Content-Type': 'application/json'}

#ip = '192.168.3.5'
#port = '9182'
#username = 'Administrator'
#password = 'Versa!23'

ip = '127.0.0.1'
port = '9182'
username = 'sdwanapi'
password = 'v3R5@#aPY'
