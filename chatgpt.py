#!/usr/bin/env python3

import os
import requests
import re
import subprocess
from datetime import datetime

# ANSI escape sequences for colored output
class Color:
    USER = "\033[94m"  # Blue
    ASSISTANT = "\033[92m"  # Green
    RESET = "\033[0m"  # Reset to default

def log_command(command):
    """Log the user's command to a file with a timestamp."""
    with open("command_history.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {command}\n")

def chat_with_gpt(messages):
    """Send messages to the ChatGPT API and return the response."""
    api_key = os.getenv("OPENAI_API_KEY")
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"

def sanitize_input(input_text):
    """Sanitize user input to prevent code injection."""
    return re.sub(r'[^a-zA-Z0-9\s\-\/\.\_\~\|\:]', '', input_text).strip()

def run_command(command):
    """Execute a shell command and return its output."""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout.strip() or "Command executed successfully with no output."
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.stderr.strip()}"

def pretty_print_user(input_text):
    """Format and print the user's input."""
    print(f"{Color.USER}You: {input_text}{Color.RESET}")

def pretty_print_assistant(response_text):
    """Format and print the assistant's response."""
    print(f"{Color.ASSISTANT}ChatGPT: {response_text}{Color.RESET}")

def main():
    """Main function to run the interactive ChatGPT session."""
    print("ChatGPT Bash Command Helper (type 'exit' or 'quit' to end)")
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant that only provides Bash commands. "
                                       "When giving a command, format it as: command: <your-command>."}
    ]

    last_command = ""  # Store the last command provided by ChatGPT

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting...")
            break

        sanitized_input = sanitize_input(user_input)
        log_command(sanitized_input)  # Log the sanitized command

        # Check if the user wants to run the last command provided
        if sanitized_input.lower() == "run it":
            if last_command:
                pretty_print_user(f"Running command: {last_command}")
                command_output = run_command(last_command)
                pretty_print_assistant(command_output)
            else:
                print("No command available to run. Please ask for a command first.")
            continue

        # Add user input to the conversation history
        messages.append({"role": "user", "content": sanitized_input})

        # Limit the message history to the last 10 exchanges
        if len(messages) > 12:  # 1 system + 10 user/assistant exchanges
            messages = messages[-12:]

        # Get the response from ChatGPT
        response = chat_with_gpt(messages)

        # Check if the response adheres to the expected format
        if response.startswith("command: "):
            last_command = response[len("command: "):].strip()  # Extract the command
            messages.append({"role": "assistant", "content": response})  # Log assistant response
            pretty_print_user(sanitized_input)
            pretty_print_assistant(response)
        else:
            # If response is not in the correct format, notify the user
            pretty_print_assistant("Error: Response format invalid. Please provide a command in the format 'command: <your-command>'.")

if __name__ == "__main__":
    main()
