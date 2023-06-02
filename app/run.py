import os
import logging
from aiavatar import AIAvatar, WakewordListener

GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
VV_URL = os.environ['VV_URL']
VV_SPEAKER = os.environ['VV_SPEAKER']

# Configure root logger
logger = logging.getLogger()
logger.setLevel(logging.WARNING)

log_format = logging.Formatter("[%(levelname)s] %(asctime)s : %(message)s")
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(log_format)
logger.addHandler(streamHandler)

# Prompt
system_message_content = """あなたは「joy」「angry」「sorrow」「fun」の4つの表情を持っています。
特に表情を表現したい場合は、文章の先頭に[face:joy]のように挿入してください。

例
[face:joy]ねえ、海が見えるよ！[face:fun]早く泳ごうよ。
"""

# Create AIAvatar
app = AIAvatar(
    google_api_key=GOOGLE_API_KEY,
    openai_api_key=OPENAI_API_KEY,
    voicevox_url=VV_URL,
    voicevox_speaker_id=VV_SPEAKER,
    system_message_content=system_message_content,
    input_device=-1,
    output_device=-1
)

# Create WakewordListener
wakewords = ["こんにちは"]

async def on_wakeword(text):
    logger.info(f"Wakeword: {text}")
    await app.start_chat()

wakeword_listener = WakewordListener(
    api_key=GOOGLE_API_KEY,
    wakewords=wakewords,
    on_wakeword=on_wakeword,
    device_index=app.input_device
)

# Start listening
ww_thread = wakeword_listener.start()
ww_thread.join()