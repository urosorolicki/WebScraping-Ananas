import json
import requests
import pandas as pd
import urllib
import time
import io

# Define URL
url = 'https://developer.ananas.rs'

# API request urld
result = urllib.request.urlopen('https://api.stage.ananastest.com/product/api/v1/merchant-integration/import'
                                .format(url)).read().decode('UTF-8')

print(result)
