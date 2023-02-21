import os
from pathlib import Path
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt import App
import openai


class Env:
    def __init__(self):
        self.get_token()

    def get_token(self):
        env_path = Path(".") / ".env"
        load_dotenv(dotenv_path=env_path)


class SlackBot:
    def __init__(self):
        self.client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])

    def get_channel_id(self, channel_name):
        response = self.client.conversations_list()
        channels = response["channels"]
        for channel in channels:
            if channel["name"] == channel_name:
                channel_id = channel["id"]
        return channel_id

    def get_message(self, channel_id: str):
        response = self.client.conversations_history(channel=channel_id)
        messages = response.data["messages"]
        for message in messages:
            if "U04QCRDFB8V" in message["text"]:
                print(message["text"].replace("<@U04QCRDFB8V>", ""))
        return response

    def post_message_in_thread(self, channel_id, message, text):
        print("post_message")
        result = self.client.chat_postMessage(
            channel=channel_id, thread_ts=message, text=text
        )
        return result


class ChatGPT:
    def __init__(self):
        Env()
        openai.api_key = os.environ["OPEN_AI_TOKEN"]

    def generate_text(self, text):
        print("generative text")
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = response.choices[0].text
        print(response)
        print(message)
        return message


Env()
app = App(token=os.environ["SLACK_BOT_TOKEN"])
slackBot = SlackBot()
chatGPT = ChatGPT()


@app.command("/hello-socket-mode")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"<@{user_id}>")


@app.event("app_mention")
def event_test(event):
    print("get mention")
    for data in event["blocks"][0]["elements"][0]["elements"]:
        if data["type"] == "text":
            input_text = data["text"]
    slackBot.post_message_in_thread(
        channel_id=event["channel"],
        message=event["event_ts"],
        text=chatGPT.generate_text(input_text),
    )
    print(event)


if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
