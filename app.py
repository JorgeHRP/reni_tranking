from flask import Flask, redirect
import requests

app = Flask(__name__)

N8N_WEBHOOK = "https://jorge-n8n.rijyaf.easypanel.host/webhook/e8fcb585-51c7-42fc-997b-3ceb206b980e"
SITE_DESTINO = "https://seusite.com"

@app.route("/track/<phone>")
def track(phone):
    # Criamos o payload exatamente como o n8n gosta
    data = {
        "phone": str(phone),
        "event": "click_site",
        "status": "active"
    }
    
    try:
        # verify=False ignora erros de SSL se o seu host estiver com frescura
        # timeout=5 garante que o script não trave se o n8n demorar
        requests.post(
            N8N_WEBHOOK, 
            json=data, 
            headers={"Content-Type": "application/json"},
            timeout=5,
            verify=True 
        )
    except Exception as e:
        print(f"Erro ao chamar n8n: {e}")
        # Mesmo se o n8n falhar, o lead NÃO pode ficar travado, 
        # por isso o redirect fica fora do bloco try
        
    return redirect(SITE_DESTINO)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)