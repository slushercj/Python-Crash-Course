text_messages = ['Hey, what time do you want to meet?', 'I love you', 'What do you want to eat?']
sent_messages = []

def show_messages(messages):
    print("\nList of sent messages: ")
    for message in messages:
        print(message)

def send_messages(unsent_messages, sent_messages):
    while unsent_messages:
        message = unsent_messages.pop()
        print(f"Sending message: '{message}'")
        sent_messages.append(message)

send_messages(text_messages, sent_messages)

show_messages(sent_messages)