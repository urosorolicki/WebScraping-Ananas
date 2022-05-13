import pandas as pd
import numpy as np
from google2pandas import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
from geonamescache import GeonamesCache
from geonamescache.mappers import country
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from mpl_toolkits.basemap import Basemap
from scipy import stats
import matplotlib.patches as mpatches
import plotly
import plotly.plotly as py
from IPython.display import Image
from plotly import tools
from plotly.graph_objs import *

url = 'https://raw.githubusercontent.com/RRighart/GA/master/df1.csv'
df1 = pd.read_csv(url, parse_dates=True, delimiter=",", decimal=",")
Image("Fig1.png")
Image("Fig2.png")
Image("Fig3.png")
df1 = []

conn = GoogleAnalyticsQuery(secrets='/your-directory/ga-creds/client_secret.json', token_file_name='/your-directory/ga-creds/analytics.dat')
 
query = {
'ids' : '999999999',
'metrics' : 'sessions',
'dimensions' : 'date',
'start_date' : '2017-07-20',
'end_date' : '2017-08-07'
}
 
df1, metadata = conn.execute_query(**query)
print(df1)
df1.date = df1.date.replace({'2017':''}, regex=True)
df1.date = df1.date.map(lambda x: str(x)[2:]) + '-' + df1.date.map(lambda x: str(x)[:2])
df1.head(5)
df1['sessions'].describe()
sum(df1.sessions)
f1 = plt.figure(figsize=(12,8))
plt.plot(df1.sessions, '-ko', lw = 2, markerfacecolor = 'white', markersize = 7, markeredgewidth = 2)
plt.xticks(range(len(df1.sessions)), df1.date, size='small', rotation='vertical')
plt.xlabel('Date')
plt.ylabel('Number of sessions')
plt.show()
