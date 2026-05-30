
🔑 How to Get Your Hugging Face API Token

Go to Hugging Face and log in to your account.
Click on your profile picture (top-right corner) → Settings.
Go to the "Access Tokens" tab (under the "Account" section).
Create a new token (or use an existing one):

Click "New Token".
Give it a name (e.g., whisper-api).
Select the read role (minimum required for inference).
Click "Generate".

Copy the token (it will look like hf_abcdef123456...).


- Get your token: https://huggingface.co/settings/tokens
- Save in `.env`:
  HF_TOKEN=your_token_here
  HA_TOKEN=your_home_assistant_token
  HA_IP=your_home_assistant_ip
