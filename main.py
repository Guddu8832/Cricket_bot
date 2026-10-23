from flask import Flask
import requests, threading, time, os
app = Flask(__name__)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL = "@cricket_prediction_ipl_psl"
API_KEY = os.environ.get("API_KEY")

@app.route('/')
def home():
    return "Bot Live - Guddu8832"

def cricket_loop():
    while True:
        try:
            url = f"https://api.cricapi.com/v1/currentMatches?apikey={API_KEY}&offset=0"
            data = requests.get(url).json()
            if data.get('data'):
                match = data['data'][0]
                msg = f"🏏 *{match['name']}*\n\n📊 {match['status']}\n\n⚡ Fast Score: {CHANNEL}"
                requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL}&text={msg}&parse_mode=Markdown")
        except Exception as e:
            print(e)
        time.sleep(300)

threading.Thread(target=cricket_loop).start()
app.run(host='0.0.0.0', port=10000)
