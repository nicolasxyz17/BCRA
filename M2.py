"""
"""
import requests
import pandas as pd
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------------
token = "BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTk1Njk1ODQsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJuZXRvbGVkbzE3QGdtYWlsLmNvbSJ9.O8bSMbKohJh6df1nDOyf9LLKesW9VI_SuSDP9u2C5H6C9cFBKwr2z06KNkxOr3timVMSCUKAHidRDjXrOl21qw"
headers = {"Authorization": token}

key = 'm2_privado_variacion_mensual'

url = "https://api.estadisticasbcra.com/" + key

#Request
request = requests.get(url, headers=headers).json()
#-----------------------------------------------------------------------------

#Table
table = pd.DataFrame(request)
table.columns = ['Date', 'M2']

# Converting the index as DatetimeIndex
idx = pd.to_datetime(table['Date'])
index = pd.DatetimeIndex(idx.values)
table = table.set_index(index)
table.drop('Date', axis=1, inplace=True)

#To Monthly
table_mth = table.resample('M').mean()

#Plot
with plt.style.context('Solarize_Light2'):
    plt.rcParams['figure.figsize'] = [10, 5]
    table_mth['2004':'2020'].plot()
    plt.title('Crecimiento de M2 Privado, en % a/a')
plt.show()










