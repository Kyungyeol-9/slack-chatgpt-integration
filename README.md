# slack-bot

## Quick Start

- Slack bot setup
- Update token

```bash
docker compose up --build -d
```

## Development Notes

- [x] receive slack mention event
- [x] post slack message
- [x] oauth token and monitoring channel
- [x] openai integration code

## Pre-requisities

- docker
- docker compose

## Configure

---

### Basic Information

- Add features and functionality
  - Bots

### Socket Mode

- Enable Socket Mode

### OAuth & Permissions

- Scopes
  - Bot Token Scopes
    - app_mentions:read
    - channels:history
    - channels:read
    - chat:write

### Event Subscriptions

- Enable Events On
- Subscribe to bot events
  - app_mention

### App level Token

- Scope
  - connections:write
  - authorizations:read

---

## Where is Tokens

- SLACK_BOT_TOKEN
  - OAuth & Permissions
    - OAuth Tokens for Your Workspace
- SLACK_APP_TOKEN
  - Basic Information
    - App-Level Tokens
- SLACK_SIGNING_SECRET
  - Basic Information
    - App Credentials
      - Signing Secret

## slack bot add to channel

- add bot to slack workspace
- open bot profile
- set add to channel
