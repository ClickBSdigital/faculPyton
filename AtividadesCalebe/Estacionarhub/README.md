🚗 Sistema de Gerenciamento de Veículos - Estacionamento Plus Pro
📋 Sobre o Projeto
Sistema completo para controle comercial de estacionamento, desenvolvido em Python com interface console e banco de dados SQLite. Implementa operações CRUD completas com sistema de cobrança por tempo, controle de usuários, turnos e caixa registradora, seguindo arquitetura modular e boas práticas de programação.

👥 Grupo de Desenvolvimento
___________________________________________________________________________________
|Nome	                                |Matrícula	    | Função Principal        |
________________________________________|_______________|_________________________|
|Eliandro Aparecido Elias da Silva  	|28986976	    | Desenvolvedor Full Stack|
|Jowilson Ribas Nunes                   |57441136	    | Desenvolvedor Back-end  |
|Vanessa de Almeida Martins	            |7590686	    | Desenvolvedor Front-end |
|Yan Torres Martins                     |53546866	    | Documentação e Testes   |
|Carlos hagamenon Oliveira gomes        |48286226       | Documentação e Testes   |
|_______________________________________|_______________|_________________________|



🎓 Curso: Tecnologia em Análise e Desenvolvimento de Sistemas
🏫 Instituição: Senac Hub Academy
👨‍🏫 Professor: Calebe
📅 Data de Entrega: [Data]

🎯 Funcionalidades
🔐 Sistema de Segurança e Usuários
👤 Login Seguro - Autenticação com criptografia SHA-256

👑 Perfis de Acesso - Admin, Gerente e Operador

🔐 Controle de Permissões - Acesso granular por função

📊 Gerenciamento de Usuários - Criação e ativação/desativação

💼 Sistema de Turnos e Caixa
🆕 Abrir Turno - Início de jornada com saldo inicial configurável

🔄 Fechar Turno - Encerramento com relatório completo e saldo final

💰 Caixa Registradora - Saldo em tempo real e movimentações

📈 Relatórios por Turno - Vendas, saldo e operações

💵 Controle de Fluxo - Sangrias e entradas registradas

✅ Operações Principais (CRUD)
🚗 Cadastrar Veículo - Registro completo com auditoria de usuário

📊 Listar Veículos - Visualização com histórico completo

✏️ Atualizar Veículo - Edição de dados com rastreamento

🗑️ Excluir Veículo - Remoção segura com confirmação

🚪 Registrar Saída - Cálculo automático de valor + registro no caixa

💰 Sistema de Cobrança Avançado
⏰ Cálculo Inteligente - Baseado no tempo real de permanência

🎁 Tolerância Gratuita - Período inicial sem cobrança (configurável)

📈 Acréscimos Progressivos - Valor adicional por horas extras

💵 Cobrança Automática - Integração com caixa registradora

🅿️ Controle de Capacidade
🔢 Vagas Limitadas - Número configurável de vagas totais

📊 Monitoramento em Tempo Real - Vagas ocupadas e disponíveis

🚫 Bloqueio Automático - Impede entrada quando lotado

⚙️ Configuração Flexível - Ajuste dinâmico de capacidade

📈 Relatórios e Analytics
📊 Estatísticas Completas - Ocupação, faturamento, eficiência

💸 Relatórios Financeiros - Faturamento total, diário e por turno

👤 Auditoria de Operações - Quem fez o que e quando

📋 Histórico Detalhado - Todas as operações com timestamp

🛠️ Tecnologias Utilizadas
Tecnologia	Versão	Finalidade
Python	3.8+	Linguagem de programação principal
SQLite3	3.35+	Banco de dados embutido
Hashlib	-	Criptografia de senhas
Datetime	-	Controle de datas e horários
OS	-	Operações do sistema
📁 Estrutura do Projeto
text
Estacionamento/
│
├── 📁 database/
│   ├── 📄 __init__.py
│   └── 📄 database.py          # Gerenciamento do banco de dados
│
├── 📁 models/
│   ├── 📄 __init__.py
│   └── 📄 veiculo.py           # Classe Veiculo e operações CRUD
│
├── 📁 main/
│   └── 📄 sistema.py           # Programa principal e interface
│
├── 📄 veiculos.db              # Banco de dados (criado automaticamente)
└── 📄 README.md                # Esta documentação
🏗️ Arquitetura do Sistema
text
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   CAMADA DE     │    │   CAMADA DE     │   │   CAMADA DE     │
│  APRESENTAÇÃO   │◄──►│    NEGÓCIO      │◄──►│     DADOS      │
│                 │    │                 │    │                 │
│  main/sistema.py│    │ models/veiculo.py│    │ database/       │
│     - Menu      │    │     - CRUD      │    │ database.py    │
│     - Login     │    │  - Cálculos     │    │   - SQLite     │
│     - Turnos    │    │  - Validações   │    │   - Usuários   │
│     - Relatórios│    │  - Auditoria    │    │   - Turnos     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
⚙️ Instalação e Configuração
Pré-requisitos
Python 3.8 ou superior

SQLite3 (geralmente incluso no Python)

🚀 Como Executar
Clone ou baixe o projeto:

bash
git clone [url-do-repositorio]
cd Estacionamento
Execute o sistema:

bash
python main/sistema.py
🔧 Execução Alternativa
bash
# Navegue para a pasta do projeto
cd Estacionamento

# Execute o arquivo principal
python3 main/sistema.py
📊 Estrutura do Banco de Dados
Tabela: veiculos
Campo	Tipo	Descrição
id_vei	INTEGER PRIMARY KEY AUTOINCREMENT	ID único do veículo
placa	TEXT NOT NULL UNIQUE	Placa do veículo (única)
modelo	TEXT NOT NULL	Modelo do veículo
cor	TEXT NOT NULL	Cor do veículo
hora_entrada	TEXT NOT NULL	Data e hora de entrada
hora_saida	TEXT	Data e hora de saída (NULL se ainda estacionado)
valor_pago	REAL DEFAULT 0	Valor cobrado pela estadia
tempo_permanencia	TEXT	Tempo total formatado (HH:MM)
id_usuario_entrada	INTEGER	Usuário que registrou a entrada
id_usuario_saida	INTEGER	Usuário que registrou a saída
id_turno_entrada	INTEGER	Turno quando entrou
id_turno_saida	INTEGER	Turno quando saiu
Tabela: usuarios
Campo	Tipo	Descrição
id_usuario	INTEGER PRIMARY KEY AUTOINCREMENT	ID único do usuário
username	TEXT UNIQUE NOT NULL	Nome de usuário para login
senha_hash	TEXT NOT NULL	Senha criptografada
nome	TEXT NOT NULL	Nome completo do usuário
perfil	TEXT NOT NULL	Perfil (admin, gerente, operador)
ativo	INTEGER DEFAULT 1	Status do usuário
Tabela: turnos
Campo	Tipo	Descrição
id_turno	INTEGER PRIMARY KEY AUTOINCREMENT	ID único do turno
id_usuario	INTEGER NOT NULL	Usuário responsável pelo turno
data_abertura	TEXT NOT NULL	Data e hora de abertura
data_fechamento	TEXT	Data e hora de fechamento
saldo_inicial	REAL NOT NULL	Saldo inicial do caixa
saldo_final	REAL	Saldo final do caixa
total_vendas	REAL DEFAULT 0	Total de vendas no turno
status	TEXT DEFAULT 'aberto'	Status do turno
Tabela: movimentacoes_caixa
Campo	Tipo	Descrição
id_movimentacao	INTEGER PRIMARY KEY AUTOINCREMENT	ID único da movimentação
id_turno	INTEGER NOT NULL	Turno da movimentação
id_veiculo	INTEGER	Veículo relacionado (se aplicável)
tipo	TEXT NOT NULL	Tipo (venda, entrada, saida, sangria)
valor	REAL NOT NULL	Valor da movimentação
descricao	TEXT	Descrição da movimentação
data_hora	TEXT NOT NULL	Data e hora da movimentação
Tabela: config
Campo	Tipo	Descrição
id	INTEGER PRIMARY KEY AUTOINCREMENT	ID único da configuração
chave	TEXT UNIQUE NOT NULL	Nome da configuração
valor	TEXT NOT NULL	Valor da configuração
Configurações padrão:

total_vagas: 20

valor_hora: 10.00

acrescimo_hora_extra: 2.00

tolerancia_minutos: 15

saldo_inicial_caixa: 100.00

🎮 Como Usar o Sistema
1. 🔐 Primeiro Acesso
text
Usuário: admin
Senha: admin123
⚠️ Altere a senha padrão após o primeiro acesso!

2. 💼 Fluxo de Trabalho Diário
text
1. 🔐 LOGIN → 2. 🆕 ABRIR TURNO → 3. 🚗 OPERAR → 4. 🔄 FECHAR TURNO → 5. 👋 SAIR
3. 📋 Menu Principal Atualizado
text
SISTEMA DE GERENCIAMENTO DE VEÍCULOS
==================================================
1. 🚗  Cadastrar veículo
2. 📊  Listar todos os veículos
3. 🅿️   Veículos no estacionamento
4. ✏️   Atualizar veículo
5. 🗑️   Excluir veículo
6. 🚪  Registrar saída de veículo
7. 📈  Estatísticas do sistema
8. ⚙️   Configurar vagas
9. 💰  Configurar valores
10. 💵 Relatório financeiro
11. 👥  Gerenciar usuários
12. 💼 Status do caixa
13. 🆕 Abrir turno          ← NOVA OPÇÃO
14. 🔄 Fechar turno         ← OPÇÃO RENUMERADA
0. 👋  Sair do sistema
==================================================
4. 🆕 Como Abrir um Turno
Selecione a opção 13 no menu principal

Informe o saldo inicial (sugerido: R$ 100,00)

Confirme a abertura do turno

Agora pode operar - cadastrar veículos e registrar saídas

5. 💰 Sistema de Cobrança
Exemplo de Cálculo:

text
⏰ Tempo: 2 horas e 30 minutos
🎁 Tolerância: 15 minutos
⏱️ Tempo cobrado: 2 horas e 15 minutos
💰 Cálculo: 1ª hora (R$ 10,00) + 2 horas extras (R$ 4,00) = R$ 14,00
6. 👑 Perfis de Usuário
👑 Admin: Acesso total ao sistema

👨‍💼 Gerente: Relatórios e configurações básicas

👨‍💻 Operador: Apenas operações de entrada/saída

🐛 Solução de Problemas
Erros Comuns e Soluções:
Problema	Causa	Solução
ModuleNotFoundError	Dependências não instaladas	Verifique se Python está instalado
sqlite3.OperationalError	Banco corrompido	Delete veiculos.db para recriar
Erro de login	Credenciais incorretas	Use admin/admin123 (primeiro acesso)
UNIQUE constraint failed	Placa duplicada	Use outra placa ou edite a existente
"Nenhum turno aberto"	Turno não iniciado	Use opção 13 para abrir turno
🔍 Debug
bash
# Para debug, execute com verbose
python main/sistema.py
📚 Conceitos de Programação Aplicados
🎯 Paradigmas Utilizados
Programação Orientada a Objetos (POO) - Classes e encapsulamento

Modularização e Separação de Concerns - Arquitetura em 3 camadas

Tratamento de Exceções - Robustez e estabilidade

Documentação e Boas Práticas - Código limpo e documentado

🏗️ Padrões de Projeto
MVC (Model-View-Controller) - Separação de camadas

DAO (Data Access Object) - Abstração do banco de dados

Singleton - Gerenciamento de conexão com banco

Factory - Criação de objetos de negócio

🔒 Segurança
Criptografia SHA-256 para senhas

Prevenção contra SQL Injection usando parâmetros

Validação de entrada do usuário

Controle de acesso por perfis

⚡ Otimizações
Consultas eficientes com índices automáticos

Gerenciamento de memória - Conexões fechadas adequadamente

Cálculos em tempo real - Performance otimizada

🎓 Para o Professor
✨ Destaques do Projeto
🏗️ Arquitetura Empresarial

Separação clara em 3 camadas (Apresentação, Negócio, Dados)

Código modular e altamente reutilizável

Facilidade de manutenção e extensão

🔐 Sistema de Segurança Completo

Autenticação segura com criptografia

Controle de acesso por perfis

Auditoria completa de operações

💼 Gestão Comercial Profissional

Controle completo de turnos (abertura e fechamento)

Caixa registradora integrado

Relatórios financeiros detalhados

⚡ Sistema de Cobrança Inteligente

Cálculos automáticos baseados em tempo real

Tolerância configurável para clientes

Acréscimos progressivos por uso

🔄 Controle de Processos

Fluxo de trabalho definido (Login → Abrir Turno → Operar → Fechar Turno)

Validações em todas as operações

Prevenção de erros e inconsistências

📝 O que Aprendemos
Habilidades Técnicas:
Python Avançado: POO, módulos, tratamento de exceções, datas

Banco de Dados: SQLite, queries complexas, transações, relações

Arquitetura de Software: MVC, separação de responsabilidades

Segurança: Criptografia, autenticação, controle de acesso

Lógica de Negócio: Sistemas comerciais, fluxo de caixa, turnos

Habilidades de Projeto:
Gestão de Requisitos: Coleta e implementação de funcionalidades

Desenvolvimento Iterativo: Implementação em fases crescentes

Testes e Validação: Garantia de qualidade do código

Documentação: Criação de documentação técnica completa

Habilidades de Trabalho em Equipe:
Git e Versionamento: Controle de versão colaborativo

Divisão de Tarefas: Organização eficiente do trabalho

Comunicação Técnica: Coordenação entre membros do grupo

Resolução de Problemas: Abordagem colaborativa para desafios

🔮 Possíveis Melhorias Futuras
🌐 Interface Web com Flask/Django

📱 Aplicativo Mobile para controle remoto

💳 Integração com Pagamentos digitais (PIX, cartão)

📊 Relatórios em PDF com gráficos e analytics

🔔 Sistema de Notificações por e-mail/SMS

🎫 Impressão de Comprovantes térmicos

📸 Reconhecimento de Placas automático

☁️ Backup em Nuvem automático

🔗 API REST para integração com outros sistemas

📅 Sistema de Reservas online

👨‍💻 Contribuições do Grupo
Desenvolvimento:
Eliandro Aparecido Elias da Silva: Arquitetura do sistema, módulo de segurança, database, turnos e caixa

[Colega 1]: CRUD de veículos, validações, tratamento de erros

[Colega 2]: Interface do usuário, menus, relatórios

[Colega 3]: Documentação, testes, configurações

Funcionalidades por Membro:
Módulo Database e Segurança: Eliandro - 100%

Módulo Veículos: [Colega 1] - 70%, Eliandro - 30%

Módulo Sistema e Interface: [Colega 2] - 80%, [Todos] - 20%

Documentação e Testes: [Colega 3] - 90%, [Todos] - 10%

📄 Licença
Este projeto é desenvolvido para fins educacionais sob a licença MIT.

🆘 Suporte
Em caso de dúvidas ou problemas:

📖 Verifique esta documentação - A maioria das dúvidas está respondida aqui

🔧 Confirme os pré-requisitos - Python 3.8+ e SQLite3 instalados

🐛 Execute em modo debug - Para identificar erros específicos

📞 Entre em contato com a equipe de desenvolvimento

Contato da Equipe: [email-do-grupo@senac.edu.br]

<div align="center">
🎉 AGRADECIMENTOS
Agradecemos ao Professor Calebe pela orientação, paciência e oportunidade de desenvolver este projeto completo!

🎓 Desenvolvido como trabalho acadêmico da disciplina de Programação em Python

✨ Obrigado por utilizar o Sistema de Estacionamento Plus Pro!

Desenvolvido com 💙, ☕ e 🤝 pela nossa equipe

</div>
📋 Checklist de Entrega
✅ Funcionalidades Implementadas:
Sistema de Login seguro com perfis

🆕 Abrir Turno - Início controlado de jornada

🔄 Fechar Turno - Encerramento com relatório

Caixa Registradora integrado

CRUD Completo de veículos com auditoria

Sistema de Cobrança inteligente por tempo

Controle de Vagas em tempo real

Relatórios Financeiros completos

Interface Amigável com menus intuitivos

Persistência em banco de dados SQLite

Tratamento de Erros robusto

Validações de entrada do usuário

Documentação completa e profissional

✅ Qualidade do Código:
Arquitetura modular em 3 camadas

Código comentado e organizado

Boas práticas de programação

Segurança contra SQL injection

Otimização de performance

Tratamento de exceções completo

✅ Documentação:
README completo com instruções detalhadas

Comentários no código

Estrutura do projeto documentada

Manual de uso do sistema

Diagramas de arquitetura

🚀 Iniciando o Sistema:
bash
# Execute na pasta do projeto
cd Estacionamento
python main/sistema.py
Credenciais iniciais:

👤 Usuário: admin

🔒 Senha: admin123

Fluxo obrigatório para operar:

🔐 Login com credenciais válidas

🆕 Abrir turno (opção 13) com saldo inicial

🚗 Operar normalmente (cadastrar veículos, registrar saídas)

🔄 Fechar turno (opção 14) ao final do expediente

O sistema criará automaticamente o banco de dados e estará pronto para uso! 🎯

<div align="center">
⭐ Se este projeto foi útil, deixe uma estrela no repositório!
🚀 Pronto para transformar seu estacionamento em um negócio digital profissional!

</div>