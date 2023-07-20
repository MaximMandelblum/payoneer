from flask import Flask, request

app = Flask(__name__)
counter = 0

@app.route('/', methods=['GET', 'POST'])
def handle_requests():
    global counter
    if request.method == 'POST':
        counter += 1
    return f"Counter: {counter}"

# App healthcheck Called by curl http://localhost:5000/healthcheck  
@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)