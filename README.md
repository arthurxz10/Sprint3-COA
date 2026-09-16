# Sprint 3 — Controle Inteligente de Sessão de Recarga - Explicação Técnica 

**Disciplina:** Arquitetura de Computadores
**Projeto:** ChargeGrid Intelligence — EV Challenge 2026 (FIAP + GoodWe), turma 1CCPY

## Equipe

| Nome | RM |
|---|---|
| Jair Ferreira Dos Santos Neto | 569682 |
| Matheus da Costa Goncalves | 570756 |
| Yan Luiz Neves Lemos | 571717 |
| Arthur dos Santos Bezerra | 569721 |
| Carlos Henrique Fratezi | 571792 |

## Descrição do protótipo

O protótipo simula, em um Raspberry Pi Pico programado em MicroPython, o
funcionamento simplificado de um controlador de energia inspirado no
conceito do **GoodWe Smart Energy Controller**. A cada ciclo, o sistema
recebe (de forma simulada) a potência de geração de energia e o consumo
da residência, calcula a energia disponível e determina o estado da
sessão de recarga do veículo elétrico, sinalizando o resultado por meio
de três LEDs.

## Arquitetura da solução (hardware + software + dados)

```
 ┌────────────────────┐        ┌──────────────────────────┐        ┌───────────────────┐
 │   ENTRADA (dados)   │        │   PROCESSAMENTO (CPU)     │        │   SAÍDA (E/S)      │
 │  geração de energia │  --->  │  Raspberry Pi Pico         │  ---> │  LED verde         │
 │  consumo residencial│        │  disponivel = geração      │        │  LED amarelo       │
 │  (simulados em      │        │              - consumo     │        │  LED vermelho      │
 │   software)         │        │  decide o estado da sessão │        │  Monitor Serial    │
 └────────────────────┘        └──────────────────────────┘        └───────────────────┘
```

- **Entrada:** valores de geração e consumo, simulados em uma lista de
  cenários no próprio código (`cenarios` em `main.py`).
- **Processamento:** o Pico executa `calcular_estado()`, que representa,
  na prática, o papel do processador — busca os dados na memória
  (variáveis), realiza a operação aritmética `disponível = geração -
  consumo` e toma uma decisão lógica com base no resultado.
- **Memória:** os valores de geração, consumo e energia disponível ficam
  armazenados temporariamente em variáveis (registradores/memória de
  trabalho) durante a execução do laço principal.
- **Saída (E/S):** os três LEDs representam a saída física do sistema, e
  o Monitor Serial apresenta a saída textual com todos os dados da
  sessão.

## Estados da sessão de recarga

| Situação | Geração | Consumo | Disponível | Estado | LED |
|---|---|---|---|---|---|
| 1 | 4000 W | 1500 W | 2500 W | RECARGA AUTORIZADA | 🟢 Verde |
| 2 | 1800 W | 1500 W | 300 W | RECARGA REDUZIDA | 🟡 Amarelo |
| 3 | 1000 W | 1800 W | -800 W | RECARGA BLOQUEADA | 🔴 Vermelho |

O limiar de 2000 W (constante `POTENCIA_RECARGA_COMPLETA`) foi adotado
como referência educacional para a potência necessária a uma recarga
completa; valores entre 0 e esse limiar resultam em recarga reduzida, e
valores negativos bloqueiam a recarga.

## Representação de dados (Decimal / Binário / Hexadecimal)

O dado escolhido para demonstrar as três representações é a **potência
disponível** (`disponível`). Exemplo com a Situação 1:

| Representação | Valor |
|---|---|
| Decimal | 2500 |
| Binário | 100111000100 |
| Hexadecimal | 9C4 |

O próprio programa calcula e imprime essas três representações para
cada cenário simulado, usando as funções `para_binario()` e
`para_hexadecimal()` em `main.py`.

## Relação com Arquitetura de Computadores

- **Sistemas numéricos e representação de dados:** conversão de valores
  entre decimal, binário e hexadecimal.
- **Processador:** o microcontrolador do Pico executa o algoritmo de
  decisão (comparação e operação aritmética) a cada ciclo.
- **Memória:** variáveis armazenam temporariamente os dados de entrada e
  o resultado do processamento.
- **Entrada e Saída (E/S):** os LEDs (saída digital) e o Monitor Serial
  (saída textual) demonstram como o processador se comunica com o mundo
  externo.


## Estrutura do repositório

```
├── main.py          # Código MicroPython do protótipo
├── diagram.json      # Circuito do Wokwi (Pico + LEDs)
├── wokwi.toml         # Configuração do projeto Wokwi
├── README.md          # Este documento
└── roteiro_video.md   # Roteiro do vídeo técnico de apresentação
```

## Vídeo e entrega

- Vídeo (YouTube, não listado): *a preencher*
