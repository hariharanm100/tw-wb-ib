import redis, sqlite3, time
from flask import Flask, render_template, request, g, current_app

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)
        return "Webhook received!"


if __name__ == "__main__":
	app.run(debug=True)
    