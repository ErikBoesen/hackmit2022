from distutils.command.config import config
import slack_sdk
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

client = slack_sdk.WebClient(token=os.environ['SLACK_TOKEN'])

client.chat_postMessage(channel='#test', text='Hello World!')
