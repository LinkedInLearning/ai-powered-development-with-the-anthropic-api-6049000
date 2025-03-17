import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()
messages = []

print("Chat with Claude")

while True:
    user_message = input("\nYou: ")
    if user_message.lower() == 'quit':
        break

    messages.append({"role": "user", "content": user_message})

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=8192,
        temperature=1,
        messages=messages
    )

    assistant_message = response.content[0].text

    print("\nClaude:", assistant_message)
    messages.append({"role": "assistant", "content": assistant_message})

print("\nConversation ended. Goodbye!")