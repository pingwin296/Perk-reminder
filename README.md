## Setup

Before running the application, you need to create a .env file in the root directory of the project.

Add the following variables to your .env file:

DISCORD_TOKEN=your_discord_bot_token

STREAM_URL=your_tiktok_stream_url

CHANNEL_ID=your_discord_channel_id   

USER_ID=your_discord_user_id         
## Notes
DISCORD_TOKEN – your Discord bot token

STREAM_URL – TikTok live stream URL

CHANNEL_ID – ID of the Discord channel where messages will be sent (optional)

USER_ID – ID of the user to send direct messages to (optional)

At least one of CHANNEL_ID or USER_ID should be provided.

## How to run

Install dependencies:

pip install -r requirements.txt

Run the bot:

python main.py
