BASE_URL = 'http://data.fixer.io/api/latest?access_key='
API_KEY = 'YOUR_API_KEY'
url = BASE_URL + API_KEY

senderEmail = 'YOUR_EMAIL_ADDRESS'
appPassword = 'APPLICATION_PASSWORD'
receivers = ['YOUR_RECEIVERS']

rules ={ 
        'archive': True,
        'mail' : True,
        #defualt, meaning all of currency rates
        #'preferred': None
        'preferred': ['BTC', 'IRR']
        }

