import slack
from flask import Flask
from slackeventsapi import SlackEventAdapter

SLACK_TOKEN = "xoxb-4183333094306-4207050518496-iTyCBK5u4c3QEazz3wBJc8wH"
SIGNING_SECRET ="e607a56e808fcdaba1e3bb537e4cd67a"


app = Flask(__name__)
 
slack_event_adapter = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)


client = slack.WebClient(token=SLACK_TOKEN)

@slack_event_adapter.on('message')
def message(payload):
    print(payload)
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
 
    if text == "Whatsup":
        client.chat_postMessage(channel=channel_id,text="Hello")
if __name__ == "__main__":
    app.run(debug=True)