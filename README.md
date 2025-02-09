# tarefa-interfaces
## Descrição:
  Este é um repositório dedicado a tarefa da unidade 4, capítulo 6, utlizando da placa de desenvolvimento BitDogLab com o Rasoberry Pi Pico W
e o kit de desenvolvimento SDK. Compile o arquivo `tarefa-interfaces.c` seguindo o arquivo `CMakeLists.txt`. Foi utilizado neste uma maquina de
estado do rp2040 para controle preciso da matriz de leds ws2812b, também foi utilizado arquivos auxiliares contidos na pasta `inc` para controle do display
OLED ssd1306, além de divervas funções e bibliotecas da SDK, em destaque uma chamada pelo cabeçalho `tusb.h`, que me permitiu flexibilidade no recebimento
de dados pelo monitor serial, já que funçôes usuais como `scanf` são bloqueantes e pausam o fluxo de dados e até atrapalham as interrupções implementadas
nos botões.
## Detalhes do código:
  As interrupções dos botões utilizam de mesmo barramento e são diferenciadas na função de callback que, além de modificar o estado dos leds verde e azul,
também modificam os bits de uma flag que manda dados para o monitor serial e para o display no loop da main. A comunicação com o display usa da interface i2c, inicializada
na main mas configurada nos arquivos da pasta `inc`, que foi configurado para um tela interativa que mostra o estado dos leds verde e azul e também mostrando o caractere
recebido no monitor serial. O arquivo `ws2812b.pio` contém as instruções em assembly para a comunicação com a matriz de leds. Como dito anteriormente, a placa conversa com o
computador via uart_usb, por um monitor serial, que recebe e envia dados. E, por fim, modifiquei o arquivo `font.h` para suportar caracteres minúsculos utilizando de um script
em python que está na pasta `script-fontes`, para desenhar em um quadrado 8x8 e obter diretamente o seu valor em decimal, esse script foi feito por IA e não é de minha
autoria, mas me auxiliou e me deu agilidade para o cálculo dos hexadecimais das fontes.

### Vídeo demostrativo
  O vídeo se encontra no drive pelo [Link](https://drive.google.com/file/d/1KNAeEg4WB6Gqd0ZtqmX69JWs-Z_QWC4L/view?usp=drive_link).
