import os
import time
import asyncio
from aiavatar import VoicevoxSpeechController

VV_URL = os.environ['VV_URL']
VV_SPEAKER = os.environ['VV_SPEAKER']

print(f'VV_URL {VV_URL}')
print(f'VV_SPEAKER {VV_SPEAKER}')

speech_controller = VoicevoxSpeechController(VV_URL, VV_SPEAKER, device_index=-1)

async def main():
    await speech_controller.speak('こんにちは')

if __name__ == "__main__":
    asyncio.run(main())
