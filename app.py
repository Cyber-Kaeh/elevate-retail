from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/purchasing')
def purchasing():
    return render_template('purchasing.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
