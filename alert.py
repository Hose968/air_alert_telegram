import asyncio
import sys
from telethon import TelegramClient, events

from optparse import OptionParser

parser = OptionParser()

parser.add_option("-i", "--id", dest = "api_id", help = "api id to connect app registered by Telefgram")
parser.add_option("-a", "--hash", dest = "api_hash", help = "api hash to connect app registered by Telefgram")
parser.add_option("-p", "--phone", dest="phone_number", help = "phone number to connect to Telegram app with '+'")
parser.add_option("-c", "--channel", dest="channel", help = "source channel Telegram username to monitor")
parser.add_option("-g", "--group", dest = "group", help = "destination Telegram group username/id to notify")
parser.add_option("-k", "--keyword", dest = "keyword", help = "keywords to monitor source by")
parser.add_option("-s", "--session", dest= "session", help= "Telegram app session path", default=None)

opt, _ = parser.parse_args()

api_id = opt.api_id
api_hash = opt.api_hash
phone_number = opt.phone_number

if not opt.session:
    client = TelegramClient('session', api_id, api_hash)
    sys.exit(0)
else:
    client = TelegramClient(opt.session, api_id, api_hash)

CHANNEL_USERNAME = opt.channel 
GROUP_USERNAME = opt.group 
KEYWORD = opt.keyword

async def main():
    await client.start()

    # Get the channel and group entities
    channel_entity = await client.get_entity(CHANNEL_USERNAME)
    group_entity = await client.get_entity(GROUP_USERNAME)

    # Event handler for new messages in the specified channel
    @client.on(events.NewMessage(chats=channel_entity))
    async def handler(event):
        if KEYWORD in event.raw_text:
            # Get the first video from saved messages
            saved_messages = await client.get_messages('me', limit=1)
            if saved_messages:
                video = saved_messages[0]

                # Send the video to the group
                await client.send_file(group_entity, video, caption="Саня біжи!!!! " + KEYWORD)

    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())