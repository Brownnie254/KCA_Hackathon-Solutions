from flask import Flask, request

app = Flask(__name__)

# Define a dictionary to store user session data
session_data = {}

@app.route('/', methods=['POST'])
def ussd_callback():
    response = ""
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "").strip()

    if text == '':
        response = "CON Welcome to Public Transportation Payment\n"
        response += "Please select an option:\n"
        response += "1. Pay for a ticket\n"
    
    elif text == '0':
        response = "CON You have returned to the main menu. Please select an option:\n"
        response += "1. Pay for a ticket"

    elif text == '1':
        response = "CON Enter the payment method:\n"
        response += "1. Paybill\n"
        response += "2. Till Number"
    
    elif text == '1*1':
        response = "CON Enter Business Number:"
    
    elif text.startswith('1*1*'):
        parts = text.split('*')
        if len(parts) == 3:
            session_data[phone_number] = {'business_number': parts[2]}
            response = "CON Enter Account Number:"
    
    elif text.startswith('1*1*') and '*' in text:
        parts = text.split('*')
        if len(parts) == 4:
            session_data[phone_number]['account_number'] = parts[3]
            response = "CON Enter the amount you're paying:"
    
    elif text.startswith('1*1*') and '*' not in text:
        parts = text.split('*')
        if len(parts) == 4:
            amount = parts[3]
            session_data[phone_number]['amount'] = amount
            response = "END You have paid {} KES using Paybill. Thank you!".format(amount)
    
    elif text == '1*2':
        response = "CON Enter Till Number:"
    
    elif text.startswith('1*2*'):
        parts = text.split('*')
        if len(parts) == 3:
            session_data[phone_number] = {'till_number': parts[2]}
            response = "CON Enter the amount you're paying:"
    
    elif text.startswith('1*2*') and '*' in text:
        parts = text.split('*')
        if len(parts) == 4:
            amount = parts[3]
            session_data[phone_number]['amount'] = amount
            response = "END You have paid {} KES using Till Number. Thank you!".format(amount)
  
    else:
        response = "END Invalid selection. Please try again."
    
    return response

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
