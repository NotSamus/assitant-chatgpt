# Orange and Blue Chatbot

This chatbot application, developed by Jesus R. Lopez and Alejandro Rodriguez, leverages the OpenAI ChatGPT API to provide an interactive conversational experience. It's designed to be compatible with the most current version of the OpenAI API.

Before you begin, ensure you're aware of the OpenAI model you intend to use and that your API key is securely stored in a .env file.

## Installation

To set up the project and install all necessary dependencies, follow these steps:

1. **Create a Virtual Environment:**
   It's highly recommended to use a virtual environment to manage project dependencies. This prevents conflicts with other Python projects on your system.

```
python3 -m venv venv
```

2. **Activate the Virtual Environment:**
   You'll need to activate the virtual environment in each terminal session where you plan to run the chatbot.

- On Linux/macOS:

```
source venv/bin/activate
```

- On Windows (Command Prompt):

```
venv\Scripts\activate.bat
```

- On Windows (PowerShell):

```
venv\Scripts\Activate.ps1
```

3. **Install Required Packages:**
   Once your virtual environment is active, install the project's dependencies using pip:

```
pip install -r requirements.txt
```

## Configuration

**OpenAI API Key**
Your **OpenAI API** key must be stored securely in a .env file at the root of your project directory. This file should contain your key in the following format:

```
OPENAI_API_KEY="your_api_key_here"
```

Replace `"your_api_key_here"` with your actual OpenAI API key.

Security Note: Never commit your `.env` file directly to version control (e.g., Git repositories). Add `.env` to your `.gitignore` file to prevent accidental exposure of your API key.

## Troubleshooting & FAQs

1. **Updating the OpenAI API Client Library:**
   To ensure you're using the latest features and bug fixes for the OpenAI API client library, you can update it using the following command:

```
openai migrate
```

Note: This command is typically used for migrating older `openai` Python client code to newer versions. For general updates of the installed package, `pip install --upgrade openai` is often more appropriate.

2. **pyaudio Installation Issues:**
   If you encounter problems installing pyaudio, it's likely due to a missing dependency: portaudio. You'll need to install portaudio manually on your operating system.

- On Linux (Debian-based distributions like Ubuntu):

```
sudo apt-get install portaudio19-dev
```

- On Linux (Fedora):

```
sudo dnf install portaudio-devel
```

- On macOS:

```
brew install portaudio
```

(This requires Homebrew. If you don't have Homebrew, you can install it from brew.sh).
