# Telegram bot to check IP of your friend

This bot return you the URL with get-parameter of your chat_id, like http://xxx:ppp/memStorage?memId=2377666 
You send this URL to you friend.
When friend open this url - he will see funny image and Python Flask get his IP, 
  behind this - script, using the IP API https://ipapi.co/{yourIp}/json/ - get info about IP info in Json object
  And return this info on your Telegram chat.
  
  To run this:
  
  0. Change config.py to your parameter.
  1. Run fishPage.py - this page with image.
  2. Run telegramBot.py - properly, Bot.
  
