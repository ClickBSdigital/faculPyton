Funcionalidades Implementadas:

01= Autenticação de Usuários :

    Login com usuário e senha
    Dois tipos de usuários: admin e operador
    caça de sessão

02= Administração :

    Cadastro de usuários
    Configuração do estacionamento (vagas, taxas, acréscimos)
    Relatórios gerais (veículos, histórico, caixa)

03= Operações do Operador :

    Registro de entrada/saída de veículos
    Cálculo automático de valores
    caixa
    Visualização de status em tempo real

04= Relatórios :

    Status desmontado
    Fluxo de veículos por período
    Histórico de operações

05= Integração com MySQL :

    Todas as operações persistentes no banco
    Consultas
    Tratamento de erros

06= Como usar:

    Configurar as credenciais do MySQL emconfig.py
    Executar o scriptmain.py
    Faça login com um usuário admin (crie diretamente no banco se necessário)
    Operadores de cadastro e configuração do estacionamento
    Operadores podem registrar entradas/saídas e controlar a caixa

07= Melhorias Possível:

    Interface gráfica com Tkinter/PyQt
    Geração de relatórios em PDF
    Integração com leitores de placa
    Sistema de notificações
    Controle de descontos/promoções
    Histórico de
    Backup do banco
 
    Este sistema cobre todas as necessidades básicas de um estacionamento com controle de acesso, financeiro e operacional, totalmente integrado ao MySQL.


###############################################################

Documentação do Sistema de Estacionamento

1. Visão Geral

    Sistema completo para gerenciamento de estacionamento com controle de acesso, finanças e operações. Desenvolvido em Python com integração ao MySQL, oferece funcionalidades para administradores e operadores.

2. Arquitetura do Sistema

    estacionaHub/
    ├── config.py          # Configurações do banco de dados
    ├── database.py        # Conexão e operações no MySQL
    ├── models.py          # Classes de modelo (entidades)
    ├── auth.py            # Sistema de autenticação
    ├── admin.py           # Funcionalidades administrativas
    ├── operator.py        # Operações do operador
    ├── reports.py         # Sistema de relatórios
    └── main.py            # Ponto de entrada

3. Banco de Dados

    Tabelas Principais:
    usuários
        Gerência de funcionários (login, senha, tipo)
        Campos: id, nome, usuário, senha, tipo (admin/operador), ativo
    configuração
        Configurações do estacionamento
        Campos: max_vagas, taxa_hora, acrescimo_percentual, arredondar_hora
    veículos
        Registros de entrada/saída
        Campos: placa, modelo, hora_entrada, hora_saida, valor_pago, usuario_id
    caixa
        diário financeiro
        Campos: usuario_id, data, total_recebido

4. Funcionalidades

    Autenticação:
        Login com usuário/senha
        caça de sessão
        Dois perfis: admin e operador
    Administração:
        Cadastro de usuários
        Configuração de parâmetros (vagas, taxas, acréscimos)
        Relatórios gerais (veículos, histórico, caixa)
    Operações:
        Registro de entrada/saída de veículos
        Cálculo automático de valores
        caixa
        Monitoramento de vagas em tempo real
    Relatórios:
        Status desmontado
        Fluxo de veículos por período
        Histórico financeiro

5. Tecnologias

    Backend : Python 3.8+
    Banco de Dados : MySQL 8.0+
    Bibliotecas : mysql-connector-python
    Manual de Uso

    ###########################################
    
    Manual de Uso

1. Instalação

1. Pré-requisitos:

    pip install mysql-connector-python  

2. o que é banco de dados:

Execute o script SQL fornecido
Atualize com suas credenciais config.py

3. Executar o sistema:
    
    python main.py

2. Fluxo de Operação

Para Administradores:

1. Login Inicial

    Usuário: admin (criado diretamente no banco)
    Senha: definida durante a criação

2. Menu Principal

    === MENU ADMIN ===
    1. Cadastrar Usuário
    2. Configurar Estacionamento
    3. Ver Relatórios
    4. Sair

3. Usuário Cadastrado

    Preencha: Nome, Usuário, Senha, Tipo (admin/operador)
    Exemplo:

    Nome: João Silva
    Usuário: joao.silva
    Senha: 123456
    Tipo: operador

4. qual.

    Defina:

    Máximo de vagas (ex: 50)
    Taxa por hora (ex: 5,00)
    Percentual de acréscimo (ex: 10,00)
    Arredondar hora (1-Sim/0-Não)

5. Relatórios

    Opções:
        (sem estacionamento)
        Histórico de veículos
        Caixa

Para Operadores:

1. Conecte-se

    Usar credenciais cadastradas pelo administrador

2. Menu Principal

    === MENU OPERADOR ===
    1. Registrar Entrada
    2. Registrar Saída
    3. Abrir Caixa
    4. Fechar Caixa
    5. Ver Status
    6. Sair

3. Entrada do Registrador

    Informe:
        Placa do veículo (ex: ABC1234)
        Modelo (ex: Gol)
    Sistema verifica disponibilidade de vagas

4. Registrador

    Informe uma placa
    Sistema calcula automaticamente:
        Tempo de chuva
        Valor a pagar (com acréscimos se aplicáveis)

Exemplo de cavia:

    Placa: ABC1234
    Tempo: 2.5 horas
    Valor a pagar: R$13.75

5. Carreira de Caixa

    Abrir Caixa : Inicia o expediente
    Fechar Caixa : Fechar o dia e mostrar o total recebido

        Caixa fechado!
        Total recebido: R$250.00

6. Ver Status

    Exibir:
        Vagas ocupadas/disponíveis
        Configurações de calendários
        Status da caixa

3. Cálculo de Valores
    O sistema calcula o valor pago considerando:

    1. Taxa base : (configuração)taxa_hora
    2. Acréscimo : Aplicado por períodos > 1 hora

        Valor = (taxa_hora * horas) * (1 + acrescimo_percentual/100)

    3. Arredondamento : Se ativado, arredonda para hora cheia

    Exemplo Prático:

        Configuração: Taxa R$ 5,00, Acréscimo 10%
        Permanência: 2,5 horas
        Cálculo:

            Base = 5.00 * 2.5 = R$12.50
            Acréscimo = 12.50 * 10% = R$1.25
            Total = R$13.75

4. Boas Práticas

    1. Para Administradores:

        Mantenha as configurações atualizadas
        Monitore relatórios semanalmente
        Cadastro apenas usuários necessários

    2. Para Operadores:

        Abra a caixa no início do expediente
        Verifique a disponibilidade de vagas antes da entrada do registrador
        Feche o caixa diariamente

    3. Segurança:

        Use senhas fortes
        logout ao terminar
        Não correndo
        
5. Solução de Problemas Comuns
__________________________________________________________________________
|Problema                         | …                                     |
|"Erro de berço"	              |     Verifique credenciais nãoconfig.py|
|"Usuário não encontrado"	      |Verifique se está ativo no banco       |
|"Estaa lotado"	                  | Aguarde saída de veículos             |
|"Caixa já aberto"	              | Verifique se outro operador abriu     |
|"Valor Reto"	                  | Verifique configurações de taxas      |
|_________________________________|_______________________________________|

6. Manutenção

    1. Backup do Banco:

        mysqldump -u root -p estacionamento_db > backup.sql

    2. Atualizações:
        Mantenha bibliotecas atualizadas
        Teste novas versões em ambiente de homologação

----------------------------------------------------------

Considerações Financeiras

Este sistema oferece uma solução completa para gerenciamento de estacionamento, com:

    capa de acesso seguro
    Operações simplificadas
    Relatórios detalhados
    Cálculos financeiros automatizados
    
Para suporte adicional ou sugestões de melhorias, consulte o código-fonte ou entre em contato com a equipe de desenvolvimento.
