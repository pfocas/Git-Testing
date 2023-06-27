from twilio.rest import Client
import PFEnv

PFEnv.print_tw_vars()
PFEnv.set_tw_vars("test")
PFEnv.print_tw_vars()
PFEnv.set_tw_vars("prod")
PFEnv.print_tw_vars()

client = Client()

message = client.messages.create(
    to="+6421550915",
    from_="+14179003746",
    body="After Upgrade!")

print(message.sid)

print('hi')  # Line 1
# Line 2
# Line 3 --
# line 4
