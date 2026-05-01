from flask import Flask, redirect, request
import requests

app = Flask(__name__)

N8N_WEBHOOK = "https://jorge-n8n.rijyaf.easypanel.host/webhook/e8fcb585-51c7-42fc-997b-3ceb206b980e"
SITE_DESTINO = "https://checkout.nenipremios.com.br/?pdv_code=j2777o"

@app.route("/track/<phone>")
def track(phone):
    try:
        # Envia o zap do lead pro seu n8n
        requests.post(N8N_WEBHOOK, json={"phone": phone, "event": "click_site"})
    except:
        pass
    return redirect(SITE_DESTINO)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)