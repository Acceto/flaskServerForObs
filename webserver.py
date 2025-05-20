
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import obsws_python as obs


# Configuration
OBS_HOST = "localhost"
OBS_PORT = 4455  # par défaut depuis OBS v28+
OBS_PASSWORD = '9XKudoxJTfx4QjlQ'  # à configurer dans OBS
INFOS_FILE = "infos.txt"  # fichier lu par OBS pour afficher le texte

# Flask setup
app = Flask(__name__)
CORS(app)

# Connexion


def obs_startRecord():
    try:
        cl = obs.ReqClient(host='localhost', port=4455, password=OBS_PASSWORD, timeout=3)
        # GetVersion, returns a response object
        resp = cl.get_version()
        # Access it's field as an attribute
        print(f"OBS Version: {resp.obs_version}")
        cl.start_record()

        return cl
    except Exception as e:
        print ('connexion error : ', e)

def obs_stopRecord():
    try:
        cl = obs.ReqClient(host='localhost', port=4455, password=OBS_PASSWORD, timeout=3)
        # GetVersion, returns a response object
        resp = cl.get_version()
        # Access it's field as an attribute
        print(f"OBS Version: {resp.obs_version}")
        cl.stop_record()

        return cl
    except Exception as e:
        print ('connexion error : ', e)



@app.route("/")
def index():
    return send_file("formulaire.html")

@app.route("/save", methods=["POST"])
def save_info():
    data = request.json
    text = data.get("text", "")
    
    with open(INFOS_FILE, "w", encoding="utf-8") as f:
        f.write(text)
    
    return {"status": "OK", "message": "Texte enregistré."}

# Endpoint Flask
@app.route("/start-recording", methods=["POST"])
def start_recording():
    try:
        result = obs_startRecord()
        return jsonify(result)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
# Endpoint Flask
@app.route("/stop-recording", methods=["POST"])
def stop_recording():
    try:
        result = obs_stopRecord()
        return jsonify(result)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# Démarrage du serveur Flask
if __name__ == "__main__":
    app.run(debug=True, port=5000)