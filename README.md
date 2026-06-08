# ChargeGrid Intelligence Dashboard

Prova de conceito desenvolvida para o GoodWe Challenge da FIAP.

O projeto simula um sistema inteligente de gerenciamento de carregamento de veículos elétricos em ambientes comerciais, demonstrando conceitos como controle de demanda, tarifação automática, inteligência artificial e monitoramento em tempo real.

---

# Integrantes

| Nome               | RM     |
| ------------------ | ------ |
| Gabriel Camarosani | 569189 |
| Gustavo Lima       | 571709 |
| Lucas Seiji        | 569673 |
| Pedro Souza        | 569311 |
| Bruno Yudi         | 571776 |

Professor: Alexandre Russi

---

# Objetivo do Projeto

O objetivo do projeto é demonstrar, por meio de uma prova de conceito funcional, como o ChargeGrid Intelligence pode auxiliar no gerenciamento de estações de carregamento de veículos elétricos em ambientes comerciais.

A proposta busca solucionar problemas identificados na Sprint 1, como sobrecarga de energia, dificuldades de cobrança, falta de integração entre equipamentos e desperdício energético.

---

# Evolução da Sprint 1 para a Sprint 2

Na Sprint 1 foram estudados os principais desafios do ChargeGrid Intelligence e propostas possíveis soluções para cada problema.

Na Sprint 2, essas ideias foram transformadas em uma prova de conceito funcional utilizando Python e Streamlit, permitindo simular situações reais de utilização do sistema.

---

# Funcionalidades

O dashboard permite:

* Simular a quantidade de carros conectados
* Distribuir automaticamente a energia disponível
* Calcular o consumo total
* Calcular o valor da cobrança
* Identificar situações de pico de demanda
* Exibir decisões automáticas da inteligência artificial

---

# Como o Sistema Funciona

O usuário escolhe a quantidade de veículos conectados através de um controle na tela.

A partir dessa informação, o sistema:

1. Calcula a energia disponível para cada veículo
2. Calcula o consumo total da estação
3. Calcula o valor da cobrança
4. Verifica se existe pico de demanda
5. Exibe uma decisão automática da IA

Se a quantidade de carros for superior a 8, o sistema entende que existe um pico de demanda e ativa uma ação de contenção para evitar sobrecarga.

---

# Pilares Aplicados

## Controle de Demanda

A energia disponível é distribuída entre todos os veículos conectados para evitar sobrecarga da rede.

## Tarifação e Pagamento

O sistema calcula automaticamente o valor da cobrança com base no consumo total.

## Inteligência Artificial

A IA analisa a quantidade de veículos conectados e toma decisões automáticas para otimizar o uso da energia.

## Protocolos Abertos

O projeto considera a integração de diferentes carregadores em uma única plataforma de monitoramento, permitindo uma gestão centralizada da rede de carregamento.

---

# Lógica Utilizada

Potência total disponível:

100 kW

Consumo por veículo:

10 kWh

Tarifa:

R$ 1,20 por kWh

Fórmulas:

Energia por carro:

energia_total / quantidade_de_carros

Consumo total:

quantidade_de_carros × 10

Valor da cobrança:

consumo_total × 1.20

---

# Tecnologias Utilizadas

* Python
* Streamlit
* GitHub

---

# Como Executar

Instale as dependências:

pip install -r requirements.txt

Execute o dashboard:

streamlit run dashboard.py

O sistema abrirá automaticamente no navegador.

---

# Estrutura do Projeto

ChargeGrid-Intelligence-Dashboard/

dashboard.py

requirements.txt

README.md

---

# Próximos Passos

* Adicionar gráficos de consumo
* Criar histórico de carregamentos
* Simular múltiplos carregadores
* Melhorar as decisões da inteligência artificial
* Adicionar mais informações ao dashboard

---

# Conclusão

A prova de conceito desenvolvida demonstra como os conceitos estudados na Sprint 1 podem ser aplicados na prática. O dashboard permite visualizar o funcionamento básico de um sistema de gerenciamento de carregamento de veículos elétricos, utilizando controle de demanda, tarifação automática e inteligência artificial para otimizar o uso da energia.

O projeto representa uma evolução da proposta inicial e demonstra o potencial do ChargeGrid Intelligence para tornar o carregamento de veículos elétricos mais eficiente e organizado.

---

Projeto acadêmico desenvolvido para o GoodWe Challenge – FIAP.
