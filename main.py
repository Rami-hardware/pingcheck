import os
import platform
import time
import requests


def send_discord_alert(webhook_url, host):
    data = {
        "content": f"⚠️ Alert: {host} is unreachable ❌"
    }
    try:
        requests.post(webhook_url, json=data)
        print("🔔 Sent alert to Discord.")
    except Exception as e:
        print(f"Failed to send Discord alert: {e}")

def ping_forever(host, webhook_url=None, delay=2, alert_interval=1800):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    last_alert_time = 0

    try:
        while True:
            response = os.system(f"ping {param} 1 {host}")
            
            if response == 0:
                print(f"{host} is reachable ✅")
            else:
                print(f"{host} is unreachable ❌")
                if webhook_url:
                    now = time.time()
                    if now - last_alert_time > alert_interval:
                        send_discord_alert(webhook_url, host)
                        last_alert_time = now
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    webhook_url = os.getenv("DISCORD_WEBHOOK")  # ✅ safer
    ip = os.getenv("ip")
    ping_forever(ip, webhook_url, delay=2)
