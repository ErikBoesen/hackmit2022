from distutils.command.config import config
import slack
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

client = slack.WebClient(token=os.environ['SLACK_TOCKEN'])

client.chat_postMessage(channel='#test', text='Hello World!')