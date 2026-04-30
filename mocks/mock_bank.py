from flask import Flask, request
import sys

app = Flask(__name__)

@app.route("/receive", methods=["POST"])
def receive():
    print(f"[BANK {PORT}] RECEIVED:")
    print(request.data.decode("utf-8"))
    return {"status": "received"}

if __name__ == "__main__":
    PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3001
    app.run(port=PORT)