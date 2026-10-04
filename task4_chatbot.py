"""Task 4: Basic Chatbot - Horizon TechX Python Internship"""

RESPONSES = {
    "hello": "Hi!",
    "hi": "Hi!",
    "how are you": "I'm fine, thanks!",
    "what is your name": "I'm PyBot, your simple chatbot.",
    "help": "Try saying: hello, how are you, what is your name, or bye.",
    "bye": "Goodbye!",
}


def get_response(user_input):
    text = user_input.strip().lower().rstrip("?!.")
    return RESPONSES.get(text, "Sorry, I don't understand that. Type 'help' for options.")


def chatbot():
    print("PyBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if not user_input.strip():
            print("PyBot: Please type something.")
            continue

        reply = get_response(user_input)
        print("PyBot:", reply)

        if user_input.strip().lower().rstrip("?!.") == "bye":
            break


if __name__ == "__main__":
    chatbot()
