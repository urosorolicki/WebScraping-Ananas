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
import reload
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

conn = GoogleAnalyticsQuery(secrets='/your-directory/ga-creds/client_secret.json',
                            token_file_name='/your-directory/ga-creds/analytics.dat')

query = {
    'ids': '999999999',
    'metrics': 'sessions',
    'dimensions': 'date',
    'start_date': '2017-07-20',
    'end_date': '2017-08-07'
}

df1, metadata = conn.execute_query(**query)
print(df1)
df1.date = df1.date.replace({'2017': ''}, regex=True)
df1.date = df1.date.map(lambda x: str(
    x)[2:]) + '-' + df1.date.map(lambda x: str(x)[:2])
df1.head(5)
df1['sessions'].describe()
sum(df1.sessions)
f1 = plt.figure(figsize=(12, 8))
plt.plot(df1.sessions, '-ko', lw=2, markerfacecolor='white',
         markersize=7, markeredgewidth=2)
plt.xticks(range(len(df1.sessions)), df1.date,
           size='small', rotation='vertical')
plt.xlabel('Date')
plt.ylabel('Number of sessions')
plt.show()
df2 = []

conn = GoogleAnalyticsQuery(secrets='/your-directory/ga-creds/client_secret.json',
                            token_file_name='/your-directory/ga-creds/analytics.dat')

query = {
    'ids': '999999999',
    'metrics': 'sessions',
    'dimensions': 'country',
    'sort': '-sessions',
    'start_date': '2017-07-20',
    'end_date': '2017-08-07'
}

df2, metadata = conn.execute_query(**query)
df2.head(20)
reload(sys)
sys.setdefaultencoding("utf-8")
shapefile = 'ne_10m_admin_0_countries'
num_colors = 9
title = 'Visitors in period from July 20'
imgfile = '.png'
description = '''
Number of sessions were obtained by Google Analytics. Author: R. Righart'''.strip()
cnt = []
mapper = country(from_key='name', to_key='iso3')
for i in range(0, len(df2)):
    A = mapper(df2.country[i])
    cnt.append(A)
df2.index = cnt
df2.head(5)
values = df2.sessions
values = stats.rankdata(values, "average")/len(values)
num_colors = 11
cm = plt.get_cmap('Reds')
nw = float("{0:.2f}".format(num_colors))
scheme = [cm(i / nw) for i in range(num_colors)]
bins = np.linspace(values.min(), values.max(), num_colors)
df2['bin'] = np.digitize(values, bins) - 1
mpl.style.use('classic')
fig = plt.figure(figsize=(22, 12))

ax = fig.add_subplot(111, axisbg='w', frame_on=False)
fig.suptitle('Number of sessions', fontsize=30, y=.95)

m = Basemap(lon_0=0, projection='robin')
m.drawmapboundary(color='w')

m.readshapefile(shapefile, 'units', color='#444444', linewidth=.2)
for info, shape in zip(m.units_info, m.units):
    iso3 = info['ADM0_A3']
    if iso3 not in df2.index:
        color = '#dddddd'
    else:
        color = scheme[df2.ix[iso3]['bin']]

    patches = [Polygon(np.array(shape), True)]
    pc = PatchCollection(patches)
    pc.set_facecolor(color)
    ax.add_collection(pc)

ax.axhspan(0, 1000 * 1800, facecolor='w', edgecolor='w', zorder=2)
ax_legend = fig.add_axes([0.35, 0.14, 0.3, 0.03], zorder=3)
cmap = mpl.colors.ListedColormap(scheme)
cb = mpl.colorbar.ColorbarBase(
    ax_legend, cmap=cmap, ticks=bins, boundaries=bins, orientation='horizontal')
cb.ax.set_xticklabels([str(round(i, 1)) for i in bins])
plt.annotate(description, xy=(-.8, -3.2), size=14, xycoords='axes fraction')
plt.savefig(imgfile, bbox_inches='tight', pad_inches=.2)
plt.show()
ndd = df2.head(30)
fig = plt.figure(figsize=(10, 8), facecolor='w')
fig.subplots_adjust(wspace=0.2)

ax1 = plt.subplot(1, 1, 1)
barwd = 0.6
r1 = range(len(ndd))
ax1.barh(r1, ndd.sort_values(by='sessions', ascending=True).sessions,
         height=0.4, align="center", color="orange")
ax1.set_yticks(r1)
ax1.set_yticklabels(ndd.sort_values(
    by='sessions', ascending=True).country, size=9)
plt.show()
df3 = []

conn = GoogleAnalyticsQuery(secrets='/your-directory/ga-creds/client_secret.json',
                            token_file_name='/your-directory/ga-creds/analytics.dat')

query = {
    'ids': '999999999',
    'metrics': 'sessions',
    'dimensions': 'deviceCategory',
    'sort': '-sessions',
    'start_date': '2017-07-20',
    'end_date': '2017-08-07'
}

df3, metadata = conn.execute_query(**query)
df3
plotly.tools.set_credentials_file(username='rrighart', api_key='9999999')
fig = {
    'data': [{'labels': df3.deviceCategory,
              'values': df3.sessions,
              'type': 'pie'}],
    'layout': {'title': 'Number of sessions as a function of device'}
}

py.iplot(fig)
df3a = []

conn = GoogleAnalyticsQuery(secrets='/your-directory/ga-creds/client_secret.json',
                            token_file_name='/your-directory/ga-creds/analytics.dat')

query = {
    'ids': '999999999',
    'metrics': 'sessions',
    'dimensions': 'deviceCategory',
    'sort': '-sessions',
    'start_date': '2017-07-20',
    'end_date': '2017-07-26'
}

df3a, metadata = conn.execute_query(**query)

df3b = []

conn = GoogleAnalyticsQuery(secrets='/your-directory/ga-creds/client_secret.json',
                            token_file_name='/your-directory/ga-creds/analytics.dat')

query = {
    'ids': '999999999',
    'metrics': 'sessions',
    'dimensions': 'deviceCategory',
    'sort': '-sessions',
    'start_date': '2017-07-27',
    'end_date': '2017-08-02'
}

df3b, metadata = conn.execute_query(**query)
print(df3a)
print(df3b)
fig = {
    'data': [
        {
            'labels': df3a.deviceCategory,
            'values': df3a.sessions,
            'type': 'pie',
            'domain': {'x': [0, .48], 'y': [.21, 1]},
            'name': '1st Week'
        },
        {
            'labels': df3b.deviceCategory,
            'values': df3b.sessions,
            'type': 'pie',
            'domain': {'x': [.49, .97], 'y': [.21, 1]},
            'name': '2nd Week'
        }
    ],
    'layout': {'title': 'Device use over time',
               'showlegend': False}
}

py.iplot(fig)
df1.to_csv('df1.csv', sep=",", index=False)
df2.to_csv('df2.csv', sep=",", index=False)
df3.to_csv('df3.csv', sep=",", index=False)
df3a.to_csv('df3a.csv', sep=",", index=False)
df3b.to_csv('df3b.csv', sep=",", index=False)
