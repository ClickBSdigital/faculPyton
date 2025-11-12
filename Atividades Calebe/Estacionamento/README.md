🚗 Sistema de Gerenciamento de Veículos
📋 Sobre o Projeto
Sistema completo para controle de entrada e saída de veículos em estacionamento, desenvolvido em Python com interface console e banco de dados SQLite. Implementa operações CRUD completas com arquitetura modular seguindo boas práticas de programação.

🎯 Funcionalidades
✅ Operações Principais (CRUD)
🚗 Cadastrar Veículo - Registro completo com placa, modelo, cor e horário de entrada

📊 Listar Veículos - Visualização de todos os veículos cadastrados

✏️ Atualizar Veículo - Edição de modelo e cor dos veículos

🗑️ Excluir Veículo - Remoção segura com confirmação

🚪 Registrar Saída - Controle de horário de saída dos veículos

📈 Funcionalidades Adicionais
🅿️ Veículos Estacionados - Lista apenas veículos presentes no estacionamento

📈 Estatísticas - Relatórios em tempo real do sistema

💾 Persistência - Dados salvos automaticamente em banco SQLite

🎨 Interface Amigável - Menu intuitivo com emojis e formatação

🛠️ Tecnologias Utilizadas
Tecnologia	Versão	Finalidade
Python	3.8+	Linguagem de programação principal
SQLite3	3.35+	Banco de dados embutido
POO	-	Programação Orientada a Objetos
Datetime	-	Controle de datas e horários
OS	-	Operações do sistema
=Estrutura do Projeto
text
sistema_veiculos/
│
├── 📁 database/
│   └── 📄 database.py          # Gerenciamento do banco de dados
│
├── 📁 models/
│   └── 📄 veiculo.py           # Classe Veiculo e operações CRUD
│
├── 📁 main/
│   └── 📄 sistema.py           # Programa principal e interface
│
├── 📄 veiculos.db              # Banco de dados (criado automaticamente)
└── 📄 README.md                # Esta documentação
=Arquitetura do Sistema
text
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   CAMADA DE     │    │   CAMADA DE     │    │   CAMADA DE     │
│  APRESENTAÇÃO   │◄──►│    NEGÓCIO      │◄──►│     DADOS       │
│                 │    │                 │    │                 │
│  main/sistema.py│    │models/veiculo.py│    │ database/       │
│     - Menu      │    │     - CRUD      │    │ database.py     │
│     - Interface │    │  - Validações   │    │   - SQLite      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
=Instalação e Configuração
Pré-requisitos
Python 3.8 ou superior

SQLite3 (geralmente incluso no Python)

=Como Executar
Clone ou baixe o projeto:

bash
git clone [url-do-repositorio]
cd sistema_veiculos
Execute o sistema:

bash
python main/sistema.py
=Execução Alternativa
bash
# Navegue para a pasta do projeto
cd sistema_veiculos

# Execute o arquivo principal
python3 main/sistema.py

# Ou execute diretamente (se tiver permissão)
./main/sistema.py
=Estrutura do Banco de Dados
Tabela: veiculos
Campo	Tipo	Descrição
id_vei	INTEGER PRIMARY KEY AUTOINCREMENT	ID único do veículo
placa	TEXT NOT NULL UNIQUE	Placa do veículo (única)
modelo	TEXT NOT NULL	Modelo do veículo
cor	TEXT NOT NULL	Cor do veículo
hora_entrada	TEXT NOT NULL	Data e hora de entrada
hora_saida	TEXT	Data e hora de saída (NULL se ainda estacionado)
=Como Usar o Sistema
1. Cadastrar Veículo
Acesse a opção 1 do menu

Informe placa, modelo e cor

Sistema registra automaticamente a hora de entrada

2. Listar Veículos
Opção 2: Lista todos os veículos

Opção 3: Lista apenas veículos estacionados

Visualize status (🅿️ Estacionado / ✅ Saída registrada)

3. Gerenciar Veículos
Opção 4: Atualizar dados (modelo/cor)

Opção 5: Excluir veículo (com confirmação)

Opção 6: Registrar saída

4. Relatórios
Opção 7: Estatísticas do sistema

Total de veículos, ocupação, últimos cadastros

Solução de Problemas
Erros Comuns e Soluções:
Problema	Causa	Solução
ModuleNotFoundError	Dependências não instaladas	Verifique se Python está instalado
sqlite3.OperationalError	Banco corrompido	Delete veiculos.db para recriar
KeyboardInterrupt	Ctrl+C pressionado	Use a opção de saída do menu
UNIQUE constraint failed	Placa duplicada	Use outra placa ou edite a existente
Debug
python
# Para debug, execute com verbose
python main/sistema.py --debug
Conceitos de Programação Aplicados
Paradigmas Utilizados
Programação Orientada a Objetos (POO)

Modularização e Separação de Concerns

Tratamento de Exceções

Documentação e Boas Práticas

Padrões de Projeto
MVC (Model-View-Controller) - Separação de camadas

CRUD (Create, Read, Update, Delete) - Operações de dados

Singleton - Gerenciamento de conexão com banco

Segurança
Prevenção contra SQL Injection usando parâmetros

Validação de entrada do usuário

Tratamento de erros específicos

Para o Professor
Destaques do Projeto
Arquitetura Limpa

Separação clara entre apresentação, negócio e dados

Código modular e reutilizável

Tratamento de Erros Robusto

Try/except em todas as operações críticas

Mensagens de erro amigáveis ao usuário

Interface Amigável

Menu intuitivo com emojis

Formatação consistente

Feedback visual claro

Documentação Completa

Docstrings em todas as funções

Comentários explicativos

README detalhado

O que Aprendi
Python Avançado: POO, módulos, datas, tratamento de exceções

Banco de Dados: SQLite, queries parametrizadas, transações

Arquitetura de Software: MVC, separação de responsabilidades

UX/UI: Design de interfaces console amigáveis

🔮 Possíveis Melhorias Futuras
Interface web com Flask/Django

Relatórios em PDF

Sistema de usuários e permissões

Calculadora de tarifas

Backup automático do banco

API REST para integração

Autor
Seu Nome
🎓 Curso: [Nome do Curso]
🏫 Instituição: [Nome da Instituição]
📧 Email: [seu.email@instituicao.com]
🔗 GitHub: [seu-usuario-github]

Licença
Este projeto é desenvolvido para fins educacionais sob a licença MIT.

Suporte
Em caso de dúvidas ou problemas:

Verifique esta documentação

Confirme os pré-requisitos

Execute em modo debug

Entre em contato com o autor

<div align="center">
Obrigado por utilizar o Sistema de Gerenciamento de Veículos!

Desenvolvido com 💙 e ☕ para fins educacionais

</div>
Checklist de Entrega
Sistema executando sem erros

Todas as funcionalidades CRUD implementadas

Banco de dados persistindo dados

Documentação completa

Código comentado e organizado

Tratamento de erros implementado

Interface amigável e intuitiva

Iniciando o Sistema:

bash
python main/sistema.py
O sistema criará automaticamente o banco de dados e estará pronto para uso! 