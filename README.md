# aiogram-webhook
## NGROK

To work with this bot, and generally to work with webhooks on [aiogram](https://github.com/aiogram), 
we need to download [ngrok](https://ngrok.com/) for your PC or VPS. After that, open __Windows PowerShell__ 
and navigate to the folder with the installed file (Type in __Windows PowerShell__: __`set-location 'path to folder'`__). 
Obtain the [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken) from the website, then run the following command:
```
chmod +x ngrok
./ngrok authtoken (Ваш токен). 
```
#### After entering the authentication code, we need to start ngrok by running the following command:
```
./ngrok http (port).
 ```
You can choose any port you like, but for the bot to work, I used port __8080__. 
Then a window with the running __ngrok__ will appear. Copy the first URL after the __Forwarding__ line, 
it should look something like this: __https://6ec8-78-37-108-80.ngrok-free.app__. You need to paste this URL 
when you start the bot (I set it up in the __webhook_polling__ method).
If you want to run this bot, replace the parameter __YOUR_TELEGRAM_API_TOKEN__ with your __API token__, 
which you can obtain from the [BotFather bot](https://t.me/BotFather), and change the parameter __YOUR_USER_ID__ 
to your __user_id__. However, this is optional. If you don't want to receive a message about the start and stop of the bot, 
simply do not enter the __admin_list__ parameter in the last line of code. 
Here is a link to the bot for getting your __user_id__ in Telegram: [username_to_id_bot](https://t.me/username_to_id_bot). 
Launch and try it out.
## WEBHOOK_POLLING
If you are creating your own __aiogram bot__, instead of the line __executor.start_polling(dp, skip_updates=True)__, 
use the line __webhook_pooling(dp, token_tg, port=8080)__. These 3 parameters are mandatory, the rest are optional.
Here is a list of additional parameters:
- __admin_list__: Pass a list of your bot admins or a list with a single element - your __id__.
- __startup_message__ and __shutdown_message__: Specify what you want to send to the __admin_list__ when the bot starts and stops.
### If you have any issues or questions, contact [simeonlimon](https://t.me/simeonlimon).
