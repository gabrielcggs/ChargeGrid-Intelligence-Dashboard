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
| Lucas Barreto      | 573149 |

---

# Objetivo do Projeto

O objetivo do projeto é demonstrar, por meio de uma prova de conceito funcional, como o ChargeGrid Intelligence pode auxiliar no gerenciamento de estações de carregamento de veículos elétricos em ambientes comerciais.

A proposta busca solucionar problemas identificados na Sprint 1, como sobrecarga de energia, dificuldades de cobrança, falta de integração entre equipamentos e desperdício energético.

---

# Problema e Justificativa

Com o crescimento da mobilidade elétrica, a demanda por estações de carregamento aumenta constantemente. Em ambientes comerciais, vários veículos podem estar conectados ao mesmo tempo, aumentando o consumo energético e podendo causar sobrecarga na rede elétrica.

Além disso, a falta de sistemas inteligentes dificulta o monitoramento do consumo, a cobrança dos usuários e a utilização eficiente da energia disponível.

Diante desse cenário, torna-se necessário o desenvolvimento de soluções capazes de gerenciar a demanda energética de forma inteligente e sustentável.

---

# Evolução da Sprint 1 para a Sprint 2

Na Sprint 1 foram estudados os desafios relacionados ao gerenciamento de eletropostos e propostas possíveis soluções para cada problema.

Na Sprint 2 essas ideias foram transformadas em uma prova de conceito funcional utilizando Python e Streamlit, permitindo simular cenários reais de utilização do sistema.

---

# Arquitetura do Sistema

O funcionamento da solução segue o fluxo abaixo:

```text
Usuário
   ↓
Dashboard Streamlit
   ↓
Simulação de Veículos
   ↓
Controle de Demanda
   ↓
Cálculo de Consumo
   ↓
Análise da IA
   ↓
Resultados e Indicadores
```

---

# Funcionalidades

O dashboard permite:

* Simular a quantidade de carros conectados;
* Distribuir automaticamente a energia disponível;
* Calcular o consumo total;
* Calcular o valor da cobrança;
* Identificar situações de pico de demanda;
* Exibir decisões automáticas da inteligência artificial.

---

# Como o Sistema Funciona

O usuário define a quantidade de veículos conectados.

A partir dessa informação o sistema:

1. Calcula a energia disponível por veículo;
2. Calcula o consumo total da estação;
3. Calcula o valor da cobrança;
4. Verifica se existe pico de demanda;
5. Exibe uma decisão automática da IA.

Caso a quantidade de veículos seja superior a 8, o sistema identifica uma situação de pico de demanda e recomenda ações para evitar sobrecarga.

---

# Fluxograma

```text
Início
   ↓
Definir quantidade de veículos
   ↓
Calcular energia disponível
   ↓
Calcular consumo total
   ↓
Verificar demanda
   ↓
Existe pico?
   ↓
Sim → Ativar contenção
Não → Operação normal
   ↓
Exibir resultados
   ↓
Fim
```

---

# Justificativas Técnicas

## Python

Foi escolhido por ser uma linguagem simples, eficiente e amplamente utilizada em projetos de automação, análise de dados e inteligência artificial.

## Streamlit

Permite criar dashboards interativos rapidamente, facilitando a visualização das informações geradas pelo sistema.

## Controle de Demanda

Foi implementado para demonstrar como um sistema inteligente pode evitar sobrecargas elétricas distribuindo melhor a energia disponível.

## Inteligência Artificial

A IA simula decisões automáticas baseadas na quantidade de veículos conectados, auxiliando na otimização do consumo energético.

---

# Pilares Aplicados

## Controle de Demanda

A energia disponível é distribuída entre todos os veículos conectados para evitar sobrecarga da rede.

## Tarifação e Pagamento

O sistema calcula automaticamente o valor da cobrança com base no consumo total.

## Inteligência Artificial

A IA analisa a quantidade de veículos conectados e toma decisões automáticas para otimizar o uso da energia.

## Protocolos Abertos

## Protocolos Abertos

A solução foi planejada para permitir a integração de diferentes carregadores em uma única plataforma de monitoramento, facilitando o gerenciamento centralizado da rede.

---

# Lógica Utilizada

Potência total disponível:

100 kW

Consumo por veículo:

10 kWh

Tarifa:

R$ 1,20 por kWh

Fórmulas utilizadas:

Energia por veículo:

energia_total / quantidade_de_carros

Consumo total:

quantidade_de_carros × 10

Valor da cobrança:

consumo_total × 1.20

---

# Sustentabilidade e Energias Renováveis

O projeto foi desenvolvido considerando os conceitos de eficiência energética e sustentabilidade estudados durante o semestre.

O controle inteligente da demanda contribui para reduzir desperdícios energéticos e melhorar a utilização da energia disponível nos carregadores.

Além disso, a proposta pode ser integrada futuramente a sistemas de energia solar fotovoltaica, permitindo que parte da energia utilizada nos carregamentos seja proveniente de fontes renováveis.

A solução contribui para:

* Redução do desperdício de energia;
* Melhor aproveitamento dos recursos energéticos;
* Incentivo à mobilidade elétrica;
* Redução dos impactos ambientais;
* Desenvolvimento de soluções sustentáveis para cidades inteligentes.

---

# Tecnologias Utilizadas

* Python
* Streamlit
* GitHub

---

# Como Executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o dashboard (digite no terminal):

```bash
streamlit run dashboard.py
```

O sistema será aberto automaticamente no navegador.

---

# Estrutura do Projeto

```text
ChargeGrid-Intelligence-Dashboard/

dashboard.py
requirements.txt
README.md
```

---

# Impactos Esperados

* Melhor distribuição de energia;
* Redução de sobrecargas elétricas;
* Diminuição do desperdício energético;
* Maior eficiência operacional;
* Melhor monitoramento dos carregadores;
* Incentivo à mobilidade elétrica sustentável.

---

# Próximos Passos

* Adicionar gráficos de consumo;
* Criar histórico de carregamentos;
* Simular múltiplos carregadores;
* Adicionar novas regras de automação para tomada de decisão
* Adicionar novas métricas ao dashboard.

---

# Conclusão

A prova de conceito desenvolvida demonstra como os conceitos estudados na Sprint 1 podem ser aplicados na prática. O dashboard permite visualizar o funcionamento básico de um sistema de gerenciamento de carregamento de veículos elétricos, utilizando controle de demanda, tarifação automática e inteligência artificial para otimizar o uso da energia.

O projeto representa uma evolução da proposta inicial e demonstra a viabilidade técnica do ChargeGrid Intelligence para ambientes comerciais.

