import anthropic
from dotenv import load_dotenv

load_dotenv()

with open('prompt.txt', 'r') as file:
    prompt_template = file.read()

CLAUDE_CONFIG = {
    "model": "claude-3-5-sonnet-20241022",
    "max_tokens": 8192,
    "temperature": 1
}

client = anthropic.Anthropic()
messages = []

cuisine_type = input("What type of cuisine would you like a meal plan for? ")
system_prompt = prompt_template.replace("{{cuisine_type}}", cuisine_type)
messages.append({"role": "user", "content": system_prompt})

response = client.messages.create(
    messages=messages,
    **CLAUDE_CONFIG
)

assistant_message = response.content[0].text
print("\nClaude:", assistant_message)
print("\nContinue chatting with Claude")

while True:
    user_message = input("\nYou: ")
    if user_message.lower() == 'quit':
        break

    messages.append({"role": "user", "content": user_message})

    response = client.messages.create(
        messages=messages
    **CLAUDE_CONFIG
    )

    assistant_message = response.content[0].text

    print("\nClaude:", assistant_message)
    messages.append({"role": "assistant", "content": assistant_message})

print("\nConversation ended. Goodbye!")