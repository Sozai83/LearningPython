from datetime import datetime

def getCurrentTime():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")


class Messenger:
    def __init__(self, listeners=[]):
        self.listeners = listeners
    
    def send(self, message):
        for listener in self.listeners:
            listener.receive(message)

    def receive(self, message):
        pass

# 1. Finish creating the TooManyMessagesException class
class TooManyMessagesException(Exception):
    def __init__(self, message):
        super().__init__(f'Message: {message} could not be added. Please clear existing messages.')

class SaveMessages(Messenger):
    def __init__(self, listeners=[]):
        super().__init__(listeners)
        self.messages = []
        self.max_messages = 10
        
    def receive(self, message):
        if len(self.messages) >= self.max_messages:
            raise TooManyMessagesException(message)
        
        self.messages.append({'message': message, 'time': getCurrentTime()})
        
    def printMessages(self):
        for m in self.messages:
            print(f'Message: "{m["message"]}" Time: {m["time"]}')
        self.messages = []

listener = SaveMessages()
sender = Messenger([listener])

# 3. Catch a TooManyMessagesException and print the messages 
for i in range(0, 20):
    try:
        sender.send(f'This is message {i}')
    except TooManyMessagesException:
        listener.printMessages()
        sender.send(f'This is message {i}')
listener.printMessages()