import requests
import os

API_KEY = os.environ.get("STEAM_API_KEY")
STEAM_ID = os.environ.get("STEAM_ID")

url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
params = {
    "key": API_KEY,
    "steamid": STEAM_ID,
    "include_appinfo": True,
    "include_played_free_games": True,
    "format": "json"
}

response = requests.get(url, params=params)
data = response.json()["response"]["games"]

# 플레이 타임 상위 3개 게임
top_games = sorted(data, key=lambda x: x["playtime_forever"], reverse=True)[:3]

markdown = "## 🎮 My Top Played Steam Games\n\n"
for game in top_games:
    hours = game["playtime_forever"] // 60
    markdown += f"- **{game['name']}** — {hours} hours played\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown)
