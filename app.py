from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🔥 Day 6 Automatic Kubernetes Deployment Awesome! 🚀 CI/CD Pipeline Working Successfully ✅ HELM"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)