import anthropic
from dotenv import load_dotenv
import os

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

meal_plan = response.content[0].text
print("\nMeal plan generated! Now creating HTML version...")

html_prompt = f"""
Convert this into a beautiful HTML page.
1. Modern styling with CSS
2. Responsive layout
3. Nice typography and spacing
4. Make sure to include all seven days of the meal plan
5. Makes sure you return only the HTML code and nothing else
Here's the meal plan to convert:
{meal_plan}
"""

messages.append({"role": "assistant", "content": meal_plan})
messages.append({"role": "user", "content": html_prompt})

response = client.messages.create(
    messages=messages,
    **CLAUDE_CONFIG
)

html_content = response.content[0].text

with open(f"{cuisine_type.lower()}_meal_plan.html", "w") as f:
    f.write(html_content)

print(f"\nHTML File created:")
print("\nContinue chatting (type 'quit' to end)")


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