def show_messages (messages) :
    print("Showing all messages")
    for message in messages :
        print(message)
def send_messages(messages, sent_messages) :
    print("Sending all messages")
    while messages :
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

text_messages = ["Hi there!" , "How are you?"]
show_messages(text_messages)

sent_messages = []
send_messages(text_messages[:], sent_messages)

print("\n---Final Lists---")
print(text_messages)
print(sent_messages)