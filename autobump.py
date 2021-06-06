import requests
import time

token = "TOKEN"

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Authorization' : token
}

id = input(f"[?] Salon ID: ")
print("")

while True:
    requests.post(
        f"https://discord.com/api/channels/{id}/messages",
        headers = headers,
        json = {"content" : "!d bump"}
    )
    print("[+] Serveur Bumpé")
    time.sleep(121 * 60)