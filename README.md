# slack-bot

## Quick Start

```bash
docker compose up --build -d
```

## Development Notes

- [x] receive slack mention event
- [x] post slack message
- [x] oauth token and monitoring channel
- [x] openai integration code

## slack bot Pre-requisities

- docker
- docker compose

### Options

- [ ] Socket Mode On
- [ ] Event Subscriptions On

### Socket Mode

- [ ] Enable Socket Mode

### OAuth & Permissions

- Scopes
  - Bot Token Scopes
    - app_mentions:read
    - channels:history
    - channels:read
    - chat:write

### Event Subscriptions

- On
- Subscribe to bot events
  - app_mention

### App level Token

- Scope
  - connections:write
  - authorizations:read

### Where is Tokens

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
