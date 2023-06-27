import os
from dotenv import load_dotenv
load_dotenv()


def set_tw_vars(runtype):
    if runtype == "test":
        os.environ['TWILIO_ACCOUNT_SID'] = os.getenv('TWILIO_ACCOUNT_SID_TEST')
        os.environ['TWILIO_AUTH_TOKEN'] = os.getenv('TWILIO_AUTH_TOKEN_TEST')
    if runtype == "prod":
        os.environ['TWILIO_ACCOUNT_SID'] = os.getenv('TWILIO_ACCOUNT_SID_PROD')
        os.environ['TWILIO_AUTH_TOKEN'] = os.getenv('TWILIO_AUTH_TOKEN_PROD')


def print_tw_vars():
    print(
        f'SID is {os.getenv("TWILIO_ACCOUNT_SID")} and Auth is {os.getenv("TWILIO_AUTH_TOKEN")}')
    if os.environ['TWILIO_ACCOUNT_SID'] == os.getenv('TWILIO_ACCOUNT_SID_TEST'):
        print("The credentials are for testing")
    else:
        print("The credentials are for production")


# print_tw_vars()
# set_tw_vars("test")
# print_tw_vars()
# set_tw_vars("prod")
# print_tw_vars()
