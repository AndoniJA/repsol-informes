import requests

TOKEN = "8474282235:AAEEW6v74vMq5d4kXDS9LNYAHuv0Xi35Yk4"
CHAT_ID = "6877119669"

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": texto}
    r = requests.get(url, params=params)
    return r.status_code

def main():
    mensaje = "Informe diario automático de Repsol"
    status = enviar_mensaje(mensaje)
    print(f"Mensaje enviado con código: {status}")

if __name__ == "__main__":
    main()
