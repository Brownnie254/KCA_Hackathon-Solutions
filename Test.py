from flask import Flask, request
from africastalking.SMS import SMS

app = Flask(__name__)

# Define a dictionary to store user session data
session_data = {}

# Dictionary to store mapping of Till Numbers to their names
till_numbers = {
    "12345": "MaThree Transport System"
}

# Africa's Talking API credentials
username = "YOUR_USERNAME"
api_key = "YOUR_API_KEY"

# Initialize Africa's Talking SMS
sms = SMS(username, api_key)

@app.route('/', methods=['POST'])
def ussd_callback():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "").strip()

    if text == '':
        response = "CON Welcome to MaThree Transport System\n"
        response += "Please select an option:\n"
        response += "1. Pay using Till Number\n"
    
    elif text == '0':
        response = "CON You have returned to the main menu. Please select an option:\n"
        response += "1. Pay using Till Number"

    elif text == '1':
        response = "CON Enter the Till Number:"
    
    elif text.startswith('1*'):
        parts = text.split('*')
        if len(parts) == 2:
            till_number = parts[1]
            session_data[phone_number] = {'till_number': till_number}
            response = "CON Enter the amount you're paying:"
    
    elif '*' not in text and phone_number in session_data and 'amount' not in session_data[phone_number]:
        # User has entered the amount
        amount = text
        till_number = session_data[phone_number]['till_number']
        if till_number in till_numbers:
            till_name = till_numbers[till_number]
            session_data[phone_number]['amount'] = amount
            
            # Send SMS to the phone number with the transaction details
            sms_message = f"Thank you for choosing {till_name}. You have paid {amount} KES. Safe journey!"
            sms.send("Thank you", [phone_number], sms_message)

            response = f"END Thank you for choosing {till_name}.\n\nYou have paid {amount} KES to Till Number {till_number}. Safe journey!"
        else:
            response = "END Invalid Till Number. Please try again."
    
    else:
        response = "END Invalid selection. Please try again."
        
    # Ensure response ends with a newline character
    response += "\n"
    return response

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
