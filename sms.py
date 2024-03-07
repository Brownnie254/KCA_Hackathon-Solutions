import africastalking

# TODO: Initialize Africa's Talking

africastalking.initialize(
    username='sandbox',
    api_key='b7f22b1928e61b99273f64d43206e7aac3bcf740a64ae97163cf6efea6099c80'
)

sms = africastalking.SMS

class send_sms():

    def send(self):
        
        #TODO: Send message
        def sending(self):
            # Set the numbers in international format
            recipients = ["+254722123123"]
            # Set your message
            message = "Hey AT Ninja!";
            # Set your shortCode or senderId
            sender = "XXYYZZ"
            try:
                response = self.sms.send(message, recipients, sender)
                print (response)
            except Exception as e:
                print (f'Houston, we have a problem: {e}')

        pass #delete this code