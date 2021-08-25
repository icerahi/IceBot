import json
import requests

CODE_EVALUATION_URL = u'https://api.hackerearth.com/v4/partner/code-evaluation/submissions/'
CLIENT_SECRET = 'df9b1ea280455a60bea0ecc0df28c98969d99b56'

def execute():
 

    data = {    
        'source': "print('hello Word')",
        'lang': 'PYTHON3',
        'time_limit': 5,
        'memory_limit': 246323,
        'input': '',
       # 'callback' : callback,
       # 'id': "client-001"
    }
    headers = {"client-secret": CLIENT_SECRET}
   # input_file.close()
   # source.close()
    resp = requests.post(CODE_EVALUATION_URL, json=data, headers=headers)
    """
    This will also work:
    resp = requests.post(CODE_EVALUATION_URL, data=data, headers=headers)
    """
    dict = json.loads(resp.text)
    print(dict)
    return dict

execute()