from twilio.rest import TwilioRestClient

account_sid="ACa657ab3682fbd17ba6b31fca7881f281"
auth_token="75af116fbc412de0ffec6d44438909b1"
client=TwilioRestClient(account_sid,auth_token)

message=client.sms.messages.create(
    body="Sandesh how r u?",
    to="+**********",
    from_="+**********")
print message.sid
