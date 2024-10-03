# ChatGPT Bash Command Helper

## Overview

The **ChatGPT Bash Command Helper** is a Python-based command-line tool that allows users to interact with OpenAI's ChatGPT to generate and execute Bash commands. It serves as an interactive assistant that helps users find and run commands while maintaining a history of interactions.

## Features

- **Interactive Command Line**: Engage with ChatGPT in real-time to get Bash commands.
- **Command Execution**: Run the generated commands directly from the interface.
- **Command History**: Maintain a log of all commands for future reference.
- **Input Sanitization**: Prevent code injection through input sanitization.
- **Error Handling**: Receive feedback on command execution, including success messages and error handling.

## Prerequisites

- Python 3.6 or higher
- `requests` library (for making API calls)

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/chatgpt-bash-command-helper.git
   cd chatgpt-bash-command-helper
   ```

2. **Set Up a Virtual Environment (Optional)**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # OR
   .\venv\Scripts\activate  # On Windows
   ```

3. **Install Required Packages**:

   ```bash
   pip install requests
   ```

4. **Set Up OpenAI API Key**:

   Make sure to set your OpenAI API key as an environment variable:

   ```bash
   export OPENAI_API_KEY='your_api_key_here'
   ```

## Usage

1. **Run the Application**:

   Execute the script using Python:

   ```bash
   python3 chatgpt_bash_command_helper.py
   ```

2. **Interact with ChatGPT**:

   - Type your request (e.g., "How do I list files in a directory?") and press Enter.
   - The assistant will respond with the appropriate Bash command in the format `command: <your-command>`.

3. **Execute Commands**:

   - If you receive a command, type `run it` to execute the last generated command.
   - The output of the command will be displayed.

4. **Exit the Application**:

   Type `exit` or `quit` to exit the interactive session.

## Example Interaction

```
➜  itermProject git:(main) ./chatgpt.py 
/Library/Python/3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
ChatGPT Bash Command Helper (type 'exit' or 'quit' to end)
You: ls file command
ChatGPT: Error: Response format invalid. Please provide a command in the format 'command: <your-command>'.
You: get me a command for ls
You: get me a command for ls
ChatGPT: command: ls
You: how do i find all files by date
You: how do i find all files by date
ChatGPT: command: ls -lt 
You: run it
You: Running command: ls -lt
ChatGPT: total 24
-rw-r--r--  1 harshalingareddy  staff   191 Oct  3 16:58 command_history.txt
-rwxr-xr-x  1 harshalingareddy  staff  4169 Oct  3 16:53 chatgpt.py
```

## Logging

All commands are logged to `command_history.txt` in the project directory with timestamps for future reference.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenAI](https://openai.com/) for providing the ChatGPT API.
- [Python](https://www.python.org/) for the programming language used.
