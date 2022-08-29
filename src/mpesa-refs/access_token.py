import requests
from requests.auth import HTTPBasicAuth
import mpesa_keys

#generate the access token
def generate_access_token():
    consumer_key=mpesa_keys.consumer_key
    consumer_secret=mpesa_keys.consumer_secret
    apiurl=("https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials")

    r=requests.get(apiurl, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    json_response=r.json()
    #output: {'access_token': 'xUFdPn3AoryaASxlu4iJAWj5ZjPE', 'expires_in': '3599'}
    my_token=json_response["access_token"]

    return my_token


