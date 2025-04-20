import requests
import os

API_KEY = os.environ.get("STEAM_API_KEY")
STEAM_ID = os.environ.get("STEAM_ID")

# 1. 소유한 게임 목록 가져오기
url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
params = {
    "key": API_KEY,
    "steamid": STEAM_ID,
    "include_appinfo": True,
    "include_played_free_games": True,
    "format": "json"
}

response = requests.get(url, params=params)
games = response.json()["response"]["games"]

# 2. 플레이타임 기준 정렬 → 상위 5개 추출
top_games = sorted(games, key=lambda x: x["playtime_forever"], reverse=True)[:5]

# 3. 마크다운 생성
markdown = "## 🎮 Top 5 Most Played Games\n\n"
markdown += "| Icon | Game | Playtime |\n"
markdown += "|------|------|----------|\n"

for game in top_games:
    hours = game["playtime_forever"] // 60
    icon_url = f"https://cdn.cloudflare.steamstatic.com/steam/apps/{game['appid']}/capsule_184x69.jpg"
    markdown += f"| ![]({icon_url}) | **{game['name']}** | {hours}h |\n"

# 4. 저장
with open("myTop5.txt", "w", encoding="utf-8") as f:
    f.write(markdown)

print("Saved your top 5 games!")
