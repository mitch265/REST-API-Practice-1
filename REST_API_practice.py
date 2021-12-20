## Code that automatically sends a new email reply to Gorgias ticket
## using Gorgias REST APIs

import requests

def AutomaticReply(ticketID, user, emailText, password):

    ### Create a ticket message ###
    
    url = "https://[your Gorgias username].gorgias.com/api/tickets/{}/messages".format(ticketID)

    payload = {
        "source": {
            "cc": [{}],
            # add an email address to send the reply to
            "to": [{"address": "[email address to receive reply]"}],
            "from": {"address": "{}".format(user)},
            "type": "email"
        },
        "body_text": "{}".format(emailText),
        "from_agent": True,
        "via": "api",
        "channel": "email"
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Basic {}".format(password)
    }

    # Request an API call to POST an email reply based off info in payload and headers.
    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)

# add your personal ticket ID, email, automatic reply, and b64 password
AutomaticReply("[ticketID]", "[user]", "[emailText]", "[password]")

    
