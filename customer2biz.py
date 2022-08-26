import requests
from requests.auth import HTTPBasicAuth
#keys
import mpesa_keys
from access_token import generate_access_token


#generating access-token
the_token=generate_access_token()


def register_c2b_url():
    api_url=" https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer %s' % the_token
    }

    payload = {
        "ShortCode": mpesa_keys.shortcode,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://mydomain.com/confirmation",
        "ValidationURL": "https://mydomain.com/validation",
    }

    response = requests.request("POST", api_url, headers = headers, json=payload)
    print(response.text.encode('utf8'))

#register_c2b_url() #run once to register url
def simulate_c2b():
    api_url=" https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate" #simulate's link

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % the_token #/access_token=generated_access_token
    }
    payload = {
        "ShortCode": mpesa_keys.shortcode,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "1",
        "Msisdn":mpesa_keys.test_msisdn ,#number initiating the transaction, hence cant use own number/virtual customer
        "BillRefNumber": "0123456",
    }

    response = requests.request("POST", api_url, headers = headers, json=payload)
    print(response.text.encode('utf8'))

simulate_c2b()



