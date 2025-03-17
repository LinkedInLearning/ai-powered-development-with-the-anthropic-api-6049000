import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()
user_message = input("Enter your message to Claude: ")

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=8192,
    temperature=1,
    messages=[
        {
            "role": "user",
            "content": user_message
        }
    ]
)
print("\nClaude's response:")
print(message.content[0].text)