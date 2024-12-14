Telegram Force Subscription Bot

This is a Telegram bot that enforces force subscription to a specific channel before users can interact with it. The bot checks if a user has joined the required channel and provides a verification mechanism.


---

Features

1. Force Subscription:
Users must join a specific channel before they can use the bot's features.


2. Verification Button:
After joining the channel, users can click "Verify" to access the bot.


3. Welcome Message:
A customizable start message with inline buttons and an image.




---

Requirements

Python 3.10 or higher

Telegram Bot Token

python-telegram-bot library



---

Setup Instructions

1. Clone the Repository

git clone https://github.com/YourRepoLink/telegram-force-subscription-bot.git
cd telegram-force-subscription-bot


2. Install Dependencies
Install the required libraries:

pip install -r requirements.txt


3. Add Your Bot Token
Edit config.py and replace YOUR_BOT_TOKEN and channel username:

BOT_TOKEN = "YOUR_BOT_TOKEN"
FORCE_CHANNEL = "Sparrow_Bots"


4. Run the Bot
Run the bot locally using:

python main.py




---

Deployment

Heroku Deployment

1. Install the Heroku CLI and log in:

heroku login


2. Create a Heroku app and deploy:

heroku create your-app-name
git push heroku main




---

Docker Deployment

1. Build the Docker image:

docker build -t telegram-bot .


2. Run the container:

docker run -d --name telegram-bot-container telegram-bot




---

Render.com Deployment

1. Add the files (main.py, config.py, requirements.txt, render.yaml) to your repository.


2. Connect your repository to Render.com.


3. Deploy the project as a worker service.




---

Bot Commands

/start: Starts the bot and checks if the user is subscribed.



---

File Overview

main.py: Contains the bot logic.

config.py: Stores the bot token and force subscription channel.

requirements.txt: Lists required Python libraries.

Dockerfile: For Docker deployments.

Procfile: For Heroku deployments.

render.yaml: For Render.com deployments.

README.md: Instructions for setting up and deploying the bot.



---

License

This project is licensed under the MIT License.


---

Support

For any issues, contact the owner on Telegram: https://t.me/Harhsu_Raven .


---

Enjoy Building Your Telegram Bot!


---

Notes:

Replace "YOUR_BOT_TOKEN" in config.py with your actual Telegram bot token.

Replace Sparrow_Bots with your Telegram channel's username.


Let me know if you need further modifications!

