# simple_aiogram_webhook
Это пример простого эхо бота с технологией webhook-ов.

Для работы этого бота, да и как в целом для работы webhook-ов на `aiogram <https://github.com/aiogram>` необходимо скачать `ngrok <https://ngrok.com/>`.
После этого заходим через Windows PowerShell в папку с установленным файлом (Можно так сделать написав set-location 'путь к папке'), получаем `токен <https://dashboard.ngrok.com/get-started/your-authtoken>` после пишем 
```
./ngrok authtoken (Ваш токен для `токен <https://dashboard.ngrok.com/get-started/your-authtoken>`). 
```
Дальше после введения кода аутентификации мы должны запустиь ngrok. Пишем ./ngrok http (port). 
Порт выбирайте на свое усмотрение, но для работы бота я использовал 8080-ый порт. 
Потом нам выведет окно с запущенным ngrok, там мы выбираем первую ссылку после строки Forwarding она выглядит как-то так: https://6ec8-78-37-108-80.ngrok-free.app. 
После если вы захотите запустить своего бота, то. Закинте бота 
```python
a = 5
```
