import os

import hashlib
import binascii
 
def process_request(request):
    password = request.GET["password"]
 
    # BAD: Inbound authentication made by comparison to string literal
    if password == "myPa55word":
        redirect("login")
 
    hashed_password = load_from_config('hashed_password', CONFIG_FILE)
    salt = load_from_config('salt', CONFIG_FILE)
 
    #GOOD: Inbound authentication made by comparing to a hash password from a config file.
    dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
    hashed_input = binascii.hexlify(dk)
    if hashed_input == hashed_password:
        redirect("login")

def AWS():
    if os.getenv("JOB_IS_RUNNING_ON_CI"):
        S3_CLIENT = boto3.client("s3")
    else:
        S3_CLIENT = boto3.client(
            "s3",
            aws_access_key_id=" AKIAIOSFODNN7EXAMPLE",
            aws_secret_access_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY", 
            )