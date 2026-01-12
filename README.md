# Bot de Trading Bitcoin (Bitstamp)

Este projeto consiste em um bot de automação para trading de Bitcoin utilizando a API da Bitstamp. O sistema monitora preços em tempo real via WebSockets e executa ordens de compra ou venda baseadas em uma lógica de preços pré-definida.

## Funcionalidades

* 
**Conexão via WebSocket**: Monitora o canal `live_trades_btcusd` para obter preços em tempo real.
* 
**Execução Automática**: Realiza ordens de mercado (Market Orders) para compra e venda.
* 
**Gerenciamento de Credenciais**: Utiliza um arquivo separado para chaves de API, garantindo que dados sensíveis não sejam expostos no controle de versão.

##  Tecnologias e Dependências

O projeto foi desenvolvido em Python e utiliza as seguintes bibliotecas:

* 
**BitstampClient (2.2.10)**: Para integração com a exchange.
* 
**websocket-client (1.9.0)**: Para recebimento de dados em tempo real.
* 
**requests (2.32.5)**: Para requisições HTTP.

##  Configuração

### 1. Instalação

Primeiro, instale as dependências necessárias listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt

```

### 2. Credenciais

O bot exige um arquivo chamado `credenciais.py` na raiz do projeto para funcionar. Você deve criá-lo seguindo o modelo abaixo:

```python
# Arquivo: credenciais.py
USERNAME = 'seu_id_de_usuario'
KEY = 'sua_chave_api'
SECRET = 'seu_secret_api'

```

Nota: Este arquivo é ignorado pelo Git para sua segurança.

##  Lógica de Operação

O bot opera com base nos seguintes gatilhos de preço configurados no script `bot_bitcoin.py`:

* 
**Venda**: Disparada quando o preço ultrapassa **90.000**.

* 
**Compra**: Disparada quando o preço cai abaixo de **81.000**.

* 
**Aguardar**: O bot permanece em observação caso o preço esteja entre esses valores.


##  Como rodar

Para iniciar o monitoramento e a execução das ordens, utilize o comando:

```bash
python bot_bitcoin.py

```

---

> **Aviso**: Este software é para fins educacionais. O uso de bots de trading envolve riscos financeiros.

---
