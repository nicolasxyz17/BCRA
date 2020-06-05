"""
"""
import pandas as pd
import matplotlib.pyplot as plt

#Import
datos = pd.read_excel('IPC-TC.xlsx', header=0, index_col=0)
#Data source: BCRA

#Plot
with plt.style.context('Solarize_Light2'):
    plt.rcParams['figure.figsize'] = [15, 6]
    datos.iloc[:,0].plot(color='dimgrey')
    datos.iloc[:,1].plot(color='seagreen')
    plt.legend()
    plt.xlabel('')
    plt.title('IPC y tipo de cambio, variaciones % interanuales')
    plt.axvspan('2008-11-30', '2010-02-28', facecolor='lightcoral', alpha=0.5)
    plt.axvspan('2012-10-31', '2015-01-31', facecolor='lightcoral', alpha=0.5)
    plt.axvspan('2015-11-30', '2017-01-31', facecolor='lightcoral', alpha=0.5)
    plt.axvspan('2018-02-28', '2020-04-30', facecolor='lightcoral', alpha=0.5)
plt.show()










