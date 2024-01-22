# Emulador de Terminal Linux em Python

Este projeto consiste em dois scripts Python que implementam um emulador de terminal Linux simples, permitindo a execução de comandos básicos e a transferência de arquivos entre o servidor e o cliente. Existem versões para comunicação via TCP e UDP.

## Funcionalidades

### TCPServer (`TCPServer.py`)

O script `TCPServer.py` implementa um servidor que recebe comandos do cliente via TCP, executa-os e envia a saída de volta.

Comandos suportados:
- `ls`: Listar os arquivos no diretório atual.
- `pwd`: Obter o diretório de trabalho atual.
- `cd [diretório]`: Mudar de diretório.
- `scp [arquivo]`: Enviar um arquivo para o cliente.

### TCPClient (`TCPClient.py`)

O script `TCPClient.py` implementa um cliente que se conecta ao servidor via TCP, envia comandos e recebe a saída ou transfere arquivos, dependendo do comando.

Comandos suportados:
- `ls`
- `pwd`
- `cd [diretório]`
- `scp [arquivo]`

### UDPServer (`UDPServer.py`)

O script `UDPServer.py` implementa um servidor que recebe comandos do cliente via UDP, executa-os e envia a saída de volta.

Comandos suportados são os mesmos da versão TCP.

### UDPClient (`UDPClient.py`)

O script `UDPClient.py` implementa um cliente que envia comandos para o servidor via UDP e recebe a saída ou transfere arquivos, dependendo do comando.

Comandos suportados são os mesmos da versão TCP.

## Como Usar

1. Execute o servidor TCP:
    ```bash
    python TCPServer.py
    ```

2. Execute o cliente TCP em outra instância do terminal ou em outra máquina:
    ```bash
    python TCPClient.py
    ```

3. Ou, se preferir, use a versão UDP. Execute o servidor UDP:
    ```bash
    python UDPServer.py
    ```

4. E o cliente UDP em outra instância do terminal ou em outra máquina:
    ```bash
    python UDPClient.py
    ```

5. Digite os comandos suportados na linha de comando do cliente.

6. Para transferência de arquivos, use o comando `scp [arquivo]`.

7. Para encerrar a execução, digite `break` no cliente.

## Configuração

Certifique-se de ter Python instalado em seu sistema.

