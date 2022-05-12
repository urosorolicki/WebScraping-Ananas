import json
import requests
import pandas as pd
import urllib
import time
from google.colab import files
import io 

# Define URL  
url = 'https://www.ananas.rs'

# API request urld
result = urllib.request.urlopen('https://api.stage.ananastest.com'\
.format(url)).read().decode('UTF-8')

print(result)