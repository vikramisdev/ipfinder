from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def log_ip():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    print(f"Visitor IP: {ip}")
    return "Visit logged."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
