"""
"""
import requests
import pandas as pd
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------------
token = "BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTk1Njk1ODQsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJuZXRvbGVkbzE3QGdtYWlsLmNvbSJ9.O8bSMbKohJh6df1nDOyf9LLKesW9VI_SuSDP9u2C5H6C9cFBKwr2z06KNkxOr3timVMSCUKAHidRDjXrOl21qw"
headers = {"Authorization": token}

key = 'tasa_badlar'
key_ = 'tasa_leliq'

url = "https://api.estadisticasbcra.com/" + key
url_ = "https://api.estadisticasbcra.com/" + key_

#Request
request = requests.get(url, headers=headers).json()
request_ = requests.get(url_, headers=headers).json()
#-----------------------------------------------------------------------------

#Table
table = pd.DataFrame(request)
table.columns = ['Date', 'Badlar']
table.set_index('Date', inplace=True, drop=True)

table_ = pd.DataFrame(request_)
table_.columns = ['Date', 'Leliq']
table_.set_index('Date', inplace=True, drop=True)

#Concat
frames = [table, table_]
result = pd.concat(frames, axis=1).dropna()

#Plot
with plt.style.context('Solarize_Light2'):
    plt.rcParams['figure.figsize'] = [15, 6]
    result.plot()
    plt.title('Badlar vs Leliq')
plt.show()

#-----------------------------------------------------------------------------
#Spread Leliq-Badlar
spread = result.iloc[:,1] - result.iloc[:,0]

#Plot
with plt.style.context('Solarize_Light2'):
    plt.rcParams['figure.figsize'] = [15, 6]
    spread.plot()
    plt.title('Spread')
plt.show()




