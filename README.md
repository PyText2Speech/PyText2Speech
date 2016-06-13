[![travis-ci status](https://travis-ci.org/chairco/PyText2Speech.svg?branch=master)](https://travis-ci.org/chairco/PyText2Speech)


PyText2Speech
---
PyText2Speech is a python3 package providing a function to easy to speach test with different languages.
This package now integrate with google, IBM watson, Industrial Technology 
Research Institute of Taiwan ([ITRI](https://www.itri.org.tw/)), Baidu.

Project setup
---


### Basic Python Setup

this is a python3 project. while you are start project, please use virtual environment.

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
   

### Mac Preparation

brew install sox

### Windows Preparation

install sox, and modify PATH variable so our program can execute sox


### Linux Preparation

install sox with your package management system


### Account Setting

The text speech test is providing by those IBM watson, Industrial Technology Research Institute of Taiwan ([ITRI](https://www.itri.org.tw/)), Baidu service, before you should apply the account and can use it.

Execute this package at first time, we will create a JSON file pytext2speech.json at your "~/" path, and you just input the service's acoount and password, congratulation it can work now.

JSON file format example:
```json    
    {
     "BAIDU":
            {
                "name":"",
                "pwd":""
            },
    "GOOGLE":
            {
                "name":"",
                "pwd":""
            },
    "WATSON":
            {
                "name":"",
                "pwd":""
            },
    "ITRI":
            {
                "name":"",
                "pwd":""
            }
    }
```


License
---
The MIT License (MIT)

Copyright (c) 2016 PyText2Speech