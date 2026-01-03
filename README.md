# SoketEventPy

**Для работы необходимы** 
**Библиотеки:** 

	mcrcon
	socketio
	json
	pyyaml
Плагины:

Временный белый список - https://modrinth.com/plugin/whitelistbytime

 **Команды для установки:**

	mcrcon - pip install mcrcon
	socketio - pip install "python-socketio[client]" 
	json - встроиная 
	pyyaml - pip install pyyaml
 
**Файл конфигурации config.yml**

В нем находятся все настройки для работы:

	ip - ip адрес сервера
 	rcon - rcon порт по которому идет подключение к консоли сервера 
  	password - пароль для подключения к консоли сервера 
   	promo - промокод для скидки
	twich - сумма за балы канала
	price - сумма доната без учета промокода
	price_promo - сумма доната с учетом промокода

**Файл конфигурации токенов token.yml**

В нем находятся все токены с которых нужно получать информацию
