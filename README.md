# PingCheck - Dockerized Ping Monitor with Discord Alerts

PingCheck is a lightweight Python tool that continuously pings a specified IP address or hostname and sends alerts to a Discord channel if the host becomes unreachable. The project is fully dockerized and includes a CI/CD workflow to automatically build and push Docker images to GitHub Container Registry (GHCR).

## Features
- Continuous ping monitoring
- Sends failure alerts to a Discord webhook
- Alert interval configurable (default: 30 minutes)
- Fully dockerized for easy deployment
- CI/CD with GitHub Actions for automatic builds and GHCR push

## Environment Variables
- `TARGET_IP`: IP address or hostname to ping
- `DISCORD_WEBHOOK`: Discord webhook URL to send alerts

## Getting Started

### Prerequisites
- Docker installed on your machine
- GitHub account (for GHCR usage)
- Discord webhook URL

### Build and Run Locally

```bash
# Clone the repository
git clone https://github.com/<your-username>/pingcheck.git
cd pingcheck

# Build Docker image
docker build -t pingcheck .

# Run container with environment variables
docker run -d \
  -e TARGET_IP="192.168.8.250" \
  -e DISCORD_WEBHOOK="https://discord.com/api/webhooks/..." \
  --name pingcheck pingcheck

# View logs
docker logs pingcheck

# Stop the container
docker stop pingcheck
```

### Using GitHub Container Registry

```bash
# Pull the image from GHCR
docker pull ghcr.io/<your-username>/pingcheck:latest

# Run it with environment variables
docker run -d \
  -e TARGET_IP="192.168.8.250" \
  -e DISCORD_WEBHOOK="https://discord.com/api/webhooks/..." \
  --name pingcheck ghcr.io/<your-username>/pingcheck:latest
```

## CI/CD
This project includes a GitHub Actions workflow (`.github/workflows/docker-build.yml`) that automatically:
1. Builds the Docker image on each push to `main`
2. Tags it as `latest` and by commit SHA
3. Pushes it to GHCR

### Secrets for CI/CD
- `GHCR_PAT`: Personal Access Token with `read:packages`, `write:packages`, and `repo` scopes (required if pushing to GHCR)

## License
This project is open-source and available under the MIT License.

