import requests, json, time
import pandas as pd
from io import StringIO

# get unix timestamp in milliseconds    
timestamp = int(time.time()) * 1000

# request smard data with default values
def requestSmardData (
    modulIDs = [8004169], 
    timestamp_from_in_milliseconds = (int(time.time()) * 1000) - (3*3600)*1000, 
    timestamp_to_in_milliseconds   = (int(time.time()) * 1000),
    region   = "DE",
    language = "de",
    type     = "discrete"
    ):
    
    # http request content
    url  = "https://www.smard.de/nip-download-manager/nip/download/market-data"
    body = json.dumps({
        "request_form": [
            {
                "format": "CSV",
                "moduleIds": modulIDs,
                "region": region,
                "timestamp_from": timestamp_from_in_milliseconds,
                "timestamp_to": timestamp_to_in_milliseconds,
                "type": type,
                "language": language
            }]})
    
    # http response
    data = requests.post(url, body)

    # create pandas dataframe out of response string (csv)
    df = pd.read_csv(StringIO(data.text), sep=';')
    
    return df
