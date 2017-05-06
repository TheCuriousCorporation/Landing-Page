	#!/usr/bin/env python3
import os

from flask import Flask, render_template
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

@app.route("/")
def index():
    return render_template("index.html")


if __name__=='__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
