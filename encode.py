import base64
import mpesa_keys


def build_pwd(formatted_time):
    #made up of the business short code(business_shortCode) + stringformattedtime
    data_to_encode=mpesa_keys.business_shortCode + mpesa_keys.lipa_na_mpesa_passkey + formatted_time
    encoded_password=base64.b64encode(data_to_encode.encode())#we need a bytes-like object, the .encode() encodes it to a utf-8
    #print(encoded_string)#output: b'MjAyMjA4MjQxNjE4NTU='..is in binary/bytes  '    '

    new_password=encoded_password.decode('utf-8')
    #print(decoded_password)#output:MjAyMjA4MjQxNjI1NTc=

    return new_password