# ChargeGrid Intelligence Dashboard

Prova de conceito desenvolvida para o GoodWe Challenge da FIAP.

O projeto simula um sistema inteligente de gerenciamento de carregamento de veículos elétricos em ambientes comerciais, unindo um totem de atendimento, um painel de gestão e o Firebase como banco de dados em nuvem.

---

## Integrantes

| Nome | RM |
|---|---|
| Gabriel Camarosani | 569189 |
| Gustavo Lima | 571709 |
| Lucas Seiji | 569673 |
| Pedro Souza | 569311 |
| Bruno Yudi | 571776 |
| Lucas Barreto | 573149 |

---

## Objetivo do Projeto

Demonstrar, por meio de um protótipo funcional, como o ChargeGrid Intelligence pode ajudar a gerenciar estações de carregamento de veículos elétricos em ambientes comerciais, resolvendo problemas como sobrecarga de energia, dificuldade de cobrança, falta de integração entre equipamentos e desperdício energético.

---

## Problema e Justificativa

Com o crescimento da mobilidade elétrica, cresce também a demanda por estações de carregamento. Em ambientes comerciais, vários veículos podem ficar conectados ao mesmo tempo, o que aumenta o consumo de energia e pode causar sobrecarga na rede elétrica.

Além disso, a falta de sistemas inteligentes dificulta o monitoramento do consumo, a cobrança correta dos usuários e o uso eficiente da energia disponível. Por isso, o grupo desenvolveu uma solução capaz de gerenciar essa demanda de forma inteligente e sustentável.

---

## Evolução do Projeto

Na Sprint 1 foram estudados os desafios relacionados ao gerenciamento de eletropostos e propostas as primeiras ideias de solução.

Na Sprint 2 essas ideias viraram uma prova de conceito com Python e Streamlit, simulando cenários de uso do sistema.

Na Sprint 3 o protótipo passou a ser funcional de verdade: um totem de atendimento grava sessões reais de recarga no Firebase, e o dashboard de gestão lê e mostra esses mesmos dados, além da simulação de múltiplos carros conectados.

---

## Arquitetura do Sistema

```
Cliente no Totem
   preenche modelo, porcentagem e kWh
        abaixo
Totem.py grava a sessão no Firestore
        abaixo
Operador acessa o Dashboard e faz login
        abaixo
Firebase Authentication valida o acesso
        abaixo
Dashboard busca as sessões no Firestore
        abaixo
Painel mostra simulação, cálculos e histórico real
```

---

## Funcionalidades

O sistema permite:

* Registrar sessões reais de recarga pelo totem, informando modelo do carro, porcentagem de bateria e kWh.
* Calcular a energia restante, o tempo estimado e o valor da recarga assim que a sessão é registrada.
* Fazer login e cadastro de operadores usando o Firebase Authentication.
* Simular a quantidade de carros conectados ao mesmo tempo em uma estação.
* Distribuir automaticamente a energia disponível entre os carros simulados.
* Calcular o consumo total e o valor da cobrança da simulação.
* Identificar situações de pico de demanda e mostrar a decisão automática da inteligência artificial.
* Exibir o histórico completo de sessões reais de recarga, vindo direto do Firestore.

---

## Como o Sistema Funciona

No totem, o cliente informa o modelo do carro, a porcentagem de bateria atual e a capacidade em kWh. Com esses dados, o sistema calcula a energia que ainda falta para completar a carga, o tempo estimado de recarga e o valor total a pagar, e grava tudo no Firebase.

No dashboard, o operador escolhe a quantidade de carros conectados em uma simulação, e o sistema:

1. Calcula a energia disponível por veículo.
2. Calcula o consumo total da estação.
3. Calcula o valor da cobrança.
4. Verifica se existe pico de demanda.
5. Exibe uma decisão automática da inteligência artificial.

Quando a quantidade simulada de veículos passa de 8, o sistema identifica pico de demanda e recomenda ações para evitar sobrecarga.

---

## Justificativas Técnicas

Python foi escolhido por ser simples, eficiente e muito usado em automação e análise de dados.

Streamlit permite criar um painel interativo com rapidez, facilitando a visualização das informações.

CustomTkinter foi usado no totem por oferecer uma interface gráfica moderna, adequada para um equipamento fixo de atendimento.

Firebase (Firestore e Authentication) foi escolhido para dar uma camada real de dados ao protótipo, permitindo que o totem e o dashboard compartilhem informações verdadeiras em tempo real, com acesso restrito a operadores autorizados.

O controle de demanda foi implementado para mostrar como um sistema inteligente pode evitar sobrecargas elétricas, distribuindo melhor a energia disponível.

A inteligência artificial simula decisões automáticas com base na quantidade de veículos conectados, ajudando a otimizar o consumo energético.

---

## Lógica Utilizada na Simulação

Potência total disponível: 100 kW

Consumo por veículo na simulação: 10 kWh

Tarifa: R$ 1,20 por kWh

Energia por veículo = energia total dividida pela quantidade de carros

Consumo total = quantidade de carros multiplicada por 10

Valor da cobrança = consumo total multiplicado por 1,20

---

## Sustentabilidade e Energias Renováveis

O projeto considera conceitos de eficiência energética e sustentabilidade estudados durante o semestre. O controle inteligente da demanda ajuda a reduzir desperdícios e melhora o aproveitamento da energia disponível nos carregadores.

A proposta pode ser integrada futuramente a sistemas de energia solar fotovoltaica, permitindo que parte da energia usada nas recargas venha de fontes renováveis.

A solução contribui para:

* Redução do desperdício de energia.
* Melhor aproveitamento dos recursos energéticos.
* Incentivo à mobilidade elétrica.
* Redução dos impactos ambientais.
* Desenvolvimento de soluções sustentáveis para cidades inteligentes.

---

## Tecnologias Utilizadas

* Python
* Streamlit
* CustomTkinter
* Firebase (Firestore e Authentication)
* Pandas
* GitHub

---

## Como Executar o Projeto

Este projeto usa o Firebase (Firestore e Authentication) para guardar dados e autenticar operadores. Antes de rodar, siga os passos abaixo.

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Configure o Firebase:

* Coloque o arquivo firebase_service_account.json na pasta raiz do projeto.
* Crie um arquivo .env na raiz do projeto seguindo o modelo de .env.example, preenchendo com a chave da API do Firebase e o identificador do projeto.

3. Rode o dashboard:

```bash
streamlit run dashboard.py
```

4. Rode o totem, em outro terminal, na mesma pasta:

```bash
python Totem.py
```

Os arquivos .env e firebase_service_account.json guardam dados sensíveis e por isso não são enviados ao repositório, conforme definido no .gitignore.

---

## Estrutura do Projeto

```
ChargeGrid Intelligence Dashboard

dashboard.py           painel de gestão em Streamlit
Totem.py                aplicação de atendimento ao cliente
calculos_totem.py       cálculos usados pelo totem
firestore_service.py    comunicação com o Firestore
auth_service.py         autenticação no Firebase
firebase_config.py      configuração geral do Firebase
requirements.txt        lista de dependências do projeto
sessoes.csv             cópia local do histórico de sessões
.env.example            modelo de arquivo de variáveis de ambiente
README.md               apresentação do projeto
```

---

## Impactos Esperados

* Melhor distribuição de energia.
* Redução de sobrecargas elétricas.
* Diminuição do desperdício energético.
* Maior eficiência operacional.
* Melhor monitoramento dos carregadores.
* Incentivo à mobilidade elétrica sustentável.

---

## Próximos Passos

* Adicionar gráficos de consumo ao dashboard.
* Criar um histórico visual mais completo dos carregamentos.
* Simular múltiplos carregadores ao mesmo tempo.
* Adicionar novas regras de automação para a tomada de decisão.
* Adicionar novas métricas ao dashboard.

---

## Conclusão

O ChargeGrid Intelligence Dashboard demonstra, na prática, como os conceitos estudados desde a Sprint 1 podem ser aplicados em um sistema funcional. O totem registra recargas reais, o Firebase guarda essas informações com segurança, e o dashboard transforma tudo isso em um painel de gestão simples e útil para o operador.

O projeto representa uma evolução da proposta inicial e demonstra a viabilidade técnica do ChargeGrid Intelligence para ambientes comerciais.
