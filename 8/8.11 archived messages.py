text_messages = ['Hey, what time do you want to meet?', 'I love you', 'What do you want to eat?']
sent_messages = []

def show_messages(messages):
    """Shows each message of the list of messages passed in"""
    print("\nList of messages: ")
    for message in messages:
        print(message)

def send_messages(unsent_messages, sent_messages):
    """Sends text messages, moving each to the sent messages list"""
    while unsent_messages:
        message = unsent_messages.pop()
        print(f"Sending message: '{message}'")
        sent_messages.append(message)

send_messages(text_messages[:], sent_messages)

show_messages(text_messages)
show_messages(sent_messages)