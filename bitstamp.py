import websocket
import ssl
import json 


def comprar():
    pass

def vender():
    pass


def ao_abrir(ws):
    print('Abriu a conexão')
    json_subscribe = """
    {
        "event": "bts:subscribe",
        "data": {
            "channel": "live_trades_btcusd"
        }
    }
    """
    ws.send(json_subscribe)


def ao_fechar(ws, close_status_code, close_msg):
    print('Fechou a conexão')

def erro(ws, erro):
    print('Deu erro')
    print(erro)

def ao_receber_mensagem(ws, mensagem):
    mensagem = json.loads(mensagem)#asdasdfsdf
    price = mensagem['data']['price']
    print(price)

#Lógica de compra e venda
    if price > 90000:
        vender()
    elif price < 81000:
        comprar()
    else:
        print('Aguarde')

if __name__ == "__main__":

    ws = websocket.WebSocketApp("wss://ws.bitstamp.net",
                                on_open=ao_abrir,
                                on_close=ao_fechar,  
                                on_message=ao_receber_mensagem,
                                on_error=erro)
    
    ws.run_forever(sslopt={'cert_reqs': ssl.CERT_NONE})