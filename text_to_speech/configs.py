# -*- encoding=utf8 -*-
import json
import os

from pprint import pprint

file = os.path.expanduser('~/pytext2speech.json')
ck_key = ['BAIDU', 'ITRI', 'WATSON']
try:
    with open(file, 'r') as fp:
        server = json.load(fp)
        for k, v in server.items():
            if k in ck_key: 
                if v['name'] == '' or v['pwd'] == '':
                    raise ValueError(str(k), u'JSON setting is empty,' \
                                    'name = ',str(v['name']), 'pwd = ',\
                                    str(v['pwd']))
except Exception as e:
    server = {
                'BAIDU': {'name': '','pwd': ''},
                'GOOGLE': {'name': '', 'pwd': ''},
                'ITRI': {'name': '', 'pwd': ''},
                'WATSON': {'name': '','pwd': ''}
            }
    with open(file, 'w') as fp:
        json.dump(server, fp)
    msg = "Not exist pytext2speech.json file at %s. " \
          "Already create JSON file, please maintenance it." \
          "message." % os.path.expanduser('~/')
    raise Exception(msg, e)
except ValueError as e:
    raise Exception(e)
