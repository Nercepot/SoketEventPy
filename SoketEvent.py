import parsTokens
import socketio
import json
from mcrcon import MCRcon
from LogicParser import ip, password, port, promo, twich_price, price, price_promo

tokens = parsTokens.load_tokens_from_yaml('token.yml')

for token in tokens:
    mc = MCRcon(ip, password, port=port)
    sio = socketio.Client()

    @sio.on('connect')
    def on_connect():
        sio.emit('add-user', {"token": token, "type": "alert_widget"})

    @sio.on('donation')
    def on_message(data):
        y = json.loads(data)
        username = y['username']
        amount = y['amount']
        currency = y['currency']
        message = y['message']
        billing = y['billing_system']

        if (builtins == 'moneymailru'):
            if (message == promo):
                if (float(amount) == price_promo):
                    command = "twl add " + username + "30:d"
                    return command
            elif (float(amount) == price):
                command = "twl add " + username + "30:d"
                return command
        elif (builtins == 'TWITCH'):
            if (float(amount) == twich_price):
                command = "twl add " + username + "30:d"
                return command

    mc.connect()
    mc.command(on_command())

    sio.connect('wss://socket.donationalerts.ru:443', transports='websocket')

    while True:
        on_connect()