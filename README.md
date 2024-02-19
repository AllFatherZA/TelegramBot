Financial Trading Bot
This project comprises a Python script that integrates MetaTrader 5 (MT5) for executing financial instrument trades and uses a Telegram bot for receiving trade commands. It allows users to send buy or sell orders through Telegram messages, which are then processed and executed on the MT5 platform.

Features
Integration with MetaTrader 5: Executes buy and sell orders on the MT5 platform.
Telegram Bot Interface: Receives and processes commands via Telegram messages.
Environment Variables for Security: Utilizes environment variables to securely manage API keys.
Prerequisites
Before running the script, ensure you have:

Python 3.x installed on your system.
MetaTrader 5 (MT5) installed and logged in to a trading account.
A Telegram bot token. You can create a new bot and get a token by talking to @BotFather on Telegram.
Installation
Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Install Required Python Packages
bash
Copy code
pip install pyTelegramBotAPI yfinance MetaTrader5 python-dotenv
Environment Setup
Create a .env file in the root directory of your project and add your Telegram bot API key:

makefile
Copy code
MY_SECRET_KEY=your_telegram_bot_api_key
Usage
Run the script with:

bash
Copy code
python your_script_name.py
To execute buy or sell orders, send a Telegram message to your bot in the following format:

Copy code
Buy 1.0 EURUSD
or

Copy code
Sell 0.5 GBPUSD
Where Buy or Sell is the order type, 1.0 or 0.5 represents the lot size, and EURUSD, GBPUSD are examples of financial instrument symbols.

Commands
Buy: Executes a buy order for the specified symbol and lot size.
Sell: Executes a sell order for the specified symbol and lot size.
Contributing
Contributions to improve the script or add new features are welcome. Please feel free to fork the repository and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
