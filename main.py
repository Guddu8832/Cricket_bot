from flask import Flask
import requests, threading, time
app = Flask(__name__)

BOT_TOKEN = "8913170172:AAEb-vQE_OUqUeCRcug5A1ZqisJPIhEuQg8"
CHANNEL = "@cricket_prediction_ipl_psl"
API_KEY = "a7663f38-a558-4337-b395-8249c9f7e377"

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
