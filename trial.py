from flask import Flask, request

app = Flask(__name__)

# Define a dictionary to store user session data
session_data = {}

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
        response += "2. Exit\n"
    
    elif text == '1':
        response = "CON Enter Till Number:"
    
    elif text.startswith('1*'):
        parts = text.split('*')
        if len(parts) == 2:
            till_number = parts[1]
            session_data[phone_number] = {'till_number': till_number}
            response = "CON Enter the amount you're paying:"
        elif len(parts) == 3:
            amount = parts[2]
            session_data[phone_number]['amount'] = amount
            response = "END Thank you for paying KES {} to Metro KDA 234T, Ref No OEM7892uk, 6/3/2024. 6:30pm . Your journey is now covered by MaThree Transport System.".format(amount)
 
    elif text == '2':
        response = "END Thank you for using MaThree Transport System. Goodbye!"
    
    else:
        response = "END Invalid selection. Please try again."
    
    return response

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
