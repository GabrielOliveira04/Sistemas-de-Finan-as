💼 Sistema de Gestão Financeira

Bem-vindo ao Sistema de Gestão Financeira! Este projeto tem como objetivo criar e gerenciar contas bancárias, movimentar dinheiro, gerar relatórios financeiros e criar gráficos de acompanhamento.

🌐 Tecnologias Utilizadas

Python 3.13

SQLModel (Para manipulação do banco de dados)

Matplotlib (Para visualização de gráficos)

🛠️ Configuração e Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/financas.git
cd financas

Crie um ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

Instale as dependências:

pip install -r requirements.txt

Execute o sistema:

python main.py

🔧 Funcionalidades

Criar conta bancária com saldo inicial

Desativar conta (se o saldo for 0)

Transferir saldo entre contas

Movimentar dinheiro (Entrada/Saída)

Filtrar histórico por datas

Gerar gráfico de contas ativas

📚 Estrutura do Projeto

financas/
│-- models.py    # Definição das tabelas do banco
│-- view.py      # Lógica de negócio
│-- template.py  # Interface de linha de comando
│-- main.py      # Ponto de entrada do programa
│-- requirements.txt

👨‍💻 Como Usar

Ao iniciar o sistema, você verá o seguinte menu:

[1] -> Criar conta
[2] -> Desativar conta
[3] -> Transferir dinheiro
[4] -> Movimentar dinheiro
[5] -> Total contas
[6] -> Filtrar histórico
[7] -> Gráfico
[0] -> Sair

Exemplo de criação de conta:

Digite o nome de algum dos bancos abaixo:
--- Banco do Brasil ---
--- Santander ---
Santander
Digite o valor atual disponível na conta:
1000
Conta criada com sucesso!

📊 Exemplo de Gráfico

Ao selecionar a opção de gerar um gráfico, um gráfico de barras será exibido com os bancos e seus respectivos saldos.

🚀 Melhorias Futuras

Implementação de interface gráfica

Integração com banco de dados SQL completo

Autenticação de usuários

🎬 GIF Representativo



🛠️ Contribuição

Se quiser contribuir, faça um fork do repositório e envie um pull request!

👥 Autores
Da uma olhada e da uma moral :
https://www.linkedin.com/in/gabriel-de-oliveira-pontes-131288246/
