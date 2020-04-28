"""
"""
import requests
import pandas as pd
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------------
token = "BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTk1Njk1ODQsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJuZXRvbGVkbzE3QGdtYWlsLmNvbSJ9.O8bSMbKohJh6df1nDOyf9LLKesW9VI_SuSDP9u2C5H6C9cFBKwr2z06KNkxOr3timVMSCUKAHidRDjXrOl21qw"
headers = {"Authorization": token}

key = 'base'

url = "https://api.estadisticasbcra.com/" + key

#Request
request = requests.get(url, headers=headers).json()
#-----------------------------------------------------------------------------

#Table
table = pd.DataFrame(request)
table.columns = ['Date', 'Base Monetaria']

# Converting the index as DatetimeIndex
idx = pd.to_datetime(table['Date'])
index = pd.DatetimeIndex(idx.values)
table = table.set_index(index)
table.drop('Date', axis=1, inplace=True)

#To Monthly
table_mth = table.resample('M').mean()

#Annual Growth
table_mth['% a/a'] = table_mth.pct_change(12) 












