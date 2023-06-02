import os
import asyncio
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

from aiavatar import VoiceRequestListener
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

# Listeners
request_listener = VoiceRequestListener(GOOGLE_API_KEY, device_index=-1)

async def main():
    print(f"main()")
    while True:
        try:
            req = await request_listener.get_request()
            if not req:
                break
            print(f"User: {req}")
        except Exception as ex:
            logger.error(f"Error ex: {ex}")
    print(f"main() exit")

if __name__ == "__main__":
    asyncio.run(main())