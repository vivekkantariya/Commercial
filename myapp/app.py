from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Replace with your actual database credentials
db = mysql.connector.connect(
    host="localhost",
    user="unknown",
    password="password",
    database="hackathon"
)
cursor = db.cursor()

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']

        # Perform the payment processing here (you may use payment gateways like Stripe, PayPal, etc.)

        # For demonstration, assuming payment is successful
        payment_success = True

        if payment_success:
            is_subscribe = 1
        else:
            is_subscribe = 0

        # Insert data into the database
        query = "INSERT INTO admin_login (full_name, email, subscribe) VALUES (%s, %s, %s)"
        values = (full_name, email, is_subscribe)
        cursor.execute(query, values)
        db.commit()

        return render_template('successpayment.html', payment_success=payment_success)

    return render_template('payment.html')

if __name__ == '__main__':
    app.run(debug=True)
