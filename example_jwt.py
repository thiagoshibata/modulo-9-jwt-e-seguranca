from datetime import datetime, timedelta, timezone
from flask import Flask, jsonify, request
import jwt

app = Flask(__name__)

@app.route("/", methods=["POST"])
def login():
    token = jwt.encode(
        payload={
            'exp': datetime.now(timezone.utc) + timedelta(minutes=1)
        },
        key="minhaChave",
        algorithm="HS256"
    )
    print(token)
    return jsonify({"token": token}), 200

@app.route("/secret", methods=["POST"])
def secret():
    raw_token = request.headers.get("Authorization")
    token = raw_token.split()[1]

    try:
        token_information = jwt.decode(
                token, key="minhaChave",
                algorithms="HS256"
            )
        print(token_information)
    except Exception as expection:
        return jsonify({"Erro": str(expection)}), 400

    return jsonify({"meu":"segredo"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
