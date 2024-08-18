# Air Alert Telegram
Telegram bot for monitor one channel for keyword and alert group of air danger

## How to start project:
### 1. Fill out env file
```text
API_ID=
API_HASH=
PHONE_NUMBER=+
CHANNEL_USERNAME=
GROUP_USERNAME=
KEYWORDS=
SESSION_PATH=session.session
```
### 2. Spawn session:
```bash
# spawn session of app:
sh spawn_session.sh -e <path to filled out env file>
# or run manualy:
python alert.py --id $API_ID --hash $API_HASH --phone $PHONE_NUMBER --channel $CHANNEL_USERNAME --group $GROUP_USERNAME --keyword "$KEYWORDS"
```
### 3. Build container:
```bash
docker compose -f docker-compose.yaml --env-file <path to filled out env file> build
```
### 4. Start project in detached mode:
```bash
docker compose -f docker-compose.yaml up -d
```