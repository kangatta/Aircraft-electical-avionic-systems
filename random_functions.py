import base64
import mpesa_keys
from datetime import datetime



def timestamp_conversion():
    #print(datetime.now())
    unformatted_time=datetime.now()
    #eliminate dashes n spaces in the timestamp
    #strftime--string formatted time
    #%Y %m %d %H %M %S
    formatted_time=unformatted_time.strftime("%Y%m%d%H%M%S")
        ## ie: 20220824150922
    #print(formatted_time,'time now')
    #fx to create timestamp
    return formatted_time