SISTEMA PERKAL - MECÂNICA AUTOMOTIVA
Sistema completo de gerenciamento para oficina mecânica desenvolvido em Python com MySQL.
Por Eliandro Silva, Faculdade Senac Academy - 03-11-2025

ÍNDICE
Descrição

Funcionalidades

Tecnologias

Estrutura do Projeto

Instalação

Configuração

Como Usar

Banco de Dados

Classes do Sistema

Capturas de Tela

Desenvolvedor

DESCRIÇÃO
O Sistema PERKAL é uma solução completa para gerenciamento de oficinas mecânicas, permitindo o controle de clientes, veículos, serviços, peças, funcionários e ordens de serviço através de uma interface intuitiva em linha de comando.

FUNCIONALIDADES
MÓDULOS IMPLEMENTADOS
Módulo	Status	Funcionalidades
Clientes	✅ Completo	Cadastro, Listagem, Busca, Atualização, Exclusão
Veículos	✅ Completo	Cadastro, Listagem, Busca, Relacionamento com Clientes
Serviços	✅ Completo	Catálogo de Serviços, Preços, Tempos Estimados
Peças	✅ Completo	Controle de Estoque, Preços, Alertas de Estoque Mínimo
Funcionários	✅ Completo	Cadastro da Equipe, Cargos, Salários
Ordens de Serviço	🔧 Desenvolvimento	Gestão Completa de OS

RECURSOS PRINCIPAIS

CRUD Completo em todos os módulos

Interface Amigável com menus hierárquicos

Validação de Dados em todas as entradas

Confirmação de Exclusão para prevenir erros

Relacionamentos entre tabelas (Clientes ↔ Veículos)

Controle de Estoque com alertas visuais

Navegação Intuitiva entre módulos

TECNOLOGIAS
Python 3.8+ - Linguagem principal

MySQL - Banco de dados

mysql-connector-python - Conexão com MySQL

SQLite (Opcional) - Para desenvolvimento

ESTRUTURA DO PROJETO

projeto_perkal/
│
├── 📄 Database.py          # Classe base de conexão
├── 📄 Cliente.py           # CRUD completo de clientes
├── 📄 Veiculo.py           # CRUD completo de veículos
├── 📄 Servico.py           # CRUD completo de serviços
├── 📄 OrdemServico.py      # CRUD completo de OS
├── 📄 Peca.py              # CRUD completo de peças
├── 📄 Funcionario.py       # CRUD completo de funcionários
├── 📄 Main.py              # 🎮 MENU PRINCIPAL (Execute este!)
└── 📄 README.md            # Documentação

INSTALAÇÃO
PRÉ-REQUISITOS
Python 3.8+ instalado

MySQL Server (XAMPP/WAMP ou servidor próprio)

Git (opcional)

PASSOS DE INSTALAÇÃO
Clone o repositório:

bash
git clone https://github.com/seu-usuario/perkal-sistema.git
cd perkal-sistema
Instale as dependências:

bash
pip install mysql-connector-python
Configure o banco de dados (veja seção abaixo)

Execute o sistema:

bash
python Main.py
CONFIGURAÇÃO
CONFIGURAÇÃO DO BANCO DE DADOS
Crie o banco de dados no MySQL:

sql
CREATE DATABASE perkal;
Execute o script SQL para criar as tabelas (disponível no arquivo database_schema.sql)

Configure a conexão no arquivo Database.py:

python
def __init__(self, banco="perkal"):
    self.banco = banco
    self.host = "localhost"
    self.user = "root"
    self.password = ""  # Sua senha do MySQL
CONFIGURAÇÃO ALTERNATIVA (SQLite)
Para desenvolvimento, você pode usar SQLite alterando a classe Database para usar sqlite3 em vez de mysql.connector.

COMO USAR
INICIANDO O SISTEMA
bash
python Main.py
NAVEGAÇÃO NO MENU
Menu Principal - Escolha o módulo desejado (1-7)

Submenus - Navegue pelas operações CRUD de cada módulo

Voltar - Use a opção "Voltar ao Menu Principal" para mudar de módulo

OPERAÇÕES DISPONÍVEIS
Cada módulo oferece estas operações:

Cadastrar - Adicionar novos registros

Listar Todos - Visualizar todos os registros

Buscar por ID - Encontrar registro específico

Atualizar - Modificar dados existentes

Excluir - Remover registros (com confirmação)

BANCO DE DADOS
TABELAS PRINCIPAIS
Tabela	Descrição
cliente	Cadastro de clientes da oficina
veiculo	Veículos dos clientes
servico	Catálogo de serviços oferecidos
peca	Peças em estoque
funcionario	Equipe de funcionários
ordem_servico	Ordens de serviço
os_servicos	Serviços por OS
os_pecas	Peças utilizadas nas OS
RELACIONAMENTOS
Cliente → Veículo (1:N)

Cliente → OrdemServico (1:N)

Veículo → OrdemServico (1:N)

OrdemServico → Servico (N:N via os_servicos)

OrdemServico → Peca (N:N via os_pecas)

CLASSES DO SISTEMA
Database (Database.py)
Gerencia conexões com o banco de dados

Métodos genéricos para execução de queries

Cliente (Cliente.py)
Gerencia cadastro de clientes

Atributos: nome, cpf, telefone, cidade, email, endereço

Veiculo (Veiculo.py)
Controla veículos dos clientes

Atributos: marca, modelo, ano, placa, cor, km_rodados

Servico (Servico.py)
Catálogo de serviços da oficina

Atributos: nome_servico, descricao, preco, tempo_estimado

Peca (Peca.py)
Gestão de estoque de peças

Atributos: nome_peca, preco_custo, preco_venda, estoque, estoque_minimo

Funcionario (Funcionario.py)
Cadastro da equipe

Atributos: nome, cpf, cargo, salario, data_admissao

OrdemServico (OrdemServico.py)
Gestão de ordens de serviço (em desenvolvimento)

Atributos: status, observacoes, total, datas

CAPTURAS DE TELA
text
==================================================
          SISTEMA DE GERENCIAMENTO - PERKAL
==================================================
1.  Gerenciar Clientes
2.  Gerenciar Veículos  
3.  Gerenciar Serviços
4.  Gerenciar Ordens de Serviço
5.  Gerenciar Peças
6.  Gerenciar Funcionários
7.  Sair do Sistema
==================================================
Digite a opção desejada (1-7): 1

CARACTERÍSTICAS DA INTERFACE
Menus Hierárquicos - Navegação intuitiva

Cores e Emojis - Feedback visual amigável

Validação Rigorosa - Prevenção de erros

Confirmações - Segurança em operações críticas

Formatação Tabular - Dados organizados

Mensagens de Status - Feedback claro das operações

PERSONALIZAÇÃO
ADICIONAR NOVOS MÓDULOS
Crie nova classe no padrão existente

Adicione menu no Main.py

Implemente funções de gerenciamento

Atualize o banco de dados

MODIFICAR BANCO DE DADOS
Altere o schema SQL e atualize os métodos nas classes correspondentes.

DESENVOLVEDOR
Eliandro Silva
Email: eliandro@clickbsdigital.com.br
GitHub: https://github.com/ClickBSdigital

LICENÇA
Este projeto é para fins educacionais e de portfólio.

Se este projeto foi útil, deixe uma estrela no repositório!

PRÓXIMOS PASSOS
Completar módulo de Ordens de Serviço

Implementar relatórios e estatísticas

Desenvolver interface web

Adicionar autenticação de usuários

Implementar backup automático

Versão: 1.0
Última Atualização: Dezembro 2024