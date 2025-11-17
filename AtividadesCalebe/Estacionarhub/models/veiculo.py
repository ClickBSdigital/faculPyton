from datetime import datetime


class Veiculo:
    """
    Classe para gerenciar as operações com veículos no sistema
    """

    def __init__(self, db):
        self.db = db
        self.usuario_logado = None
        self.turno_aberto = None

    def set_usuario_logado(self, usuario):
        """Define o usuário logado atualmente"""
        self.usuario_logado = usuario

    def set_turno_aberto(self, turno):
        """Define o turno aberto atualmente"""
        self.turno_aberto = turno

    def cadastrar(self):
        """Cadastra um novo veículo no sistema"""
        if not self.turno_aberto:
            print("❌ Nenhum turno aberto! Abra um turno primeiro.")
            return

        print("\n" + "=" * 50)
        print("          CADASTRAR NOVO VEÍCULO")
        print("=" * 50)

        # Verifica se há vagas disponíveis
        if not self.db.tem_vaga_disponivel():
            vagas_ocupadas = self.db.get_vagas_ocupadas()
            total_vagas = self.db.get_total_vagas()
            print("❌ ESTACIONAMENTO LOTADO!")
            print(f"🚫 Vagas ocupadas: {vagas_ocupadas}/{total_vagas}")
            print("⏳ Aguarde a saída de algum veículo...")
            return

        try:
            # Mostra vagas disponíveis e valor da hora
            vagas_disponiveis = self.db.get_vagas_disponiveis()
            total_vagas = self.db.get_total_vagas()
            valor_hora = self.db.get_valor_hora()

            print(f"🅿️  Vagas disponíveis: {vagas_disponiveis}/{total_vagas}")
            print(f"💰 Valor da 1ª hora: R$ {valor_hora:.2f}")
            print(
                f"📈 Acréscimo por hora extra: R$ {self.db.get_acrescimo_hora_extra():.2f}"
            )
            print(f"👤 Operador: {self.usuario_logado[2]}")
            print("-" * 50)

            placa = input("Placa do veículo: ").upper().strip()
            modelo = input("Modelo do veículo: ").strip()
            cor = input("Cor do veículo: ").strip()

            if not placa or not modelo or not cor:
                print("❌ Erro: Todos os campos são obrigatórios!")
                return

            if self.db.verificar_placa_existe(placa):
                print("❌ Erro: Já existe um veículo com esta placa!")
                return

            hora_entrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            id_usuario_entrada = self.usuario_logado[0]
            id_turno_entrada = self.turno_aberto[0]

            query = """
                INSERT INTO veiculos (placa, modelo, cor, hora_entrada, hora_saida, valor_pago, 
                                    id_usuario_entrada, id_turno_entrada)
                VALUES (?, ?, ?, ?, NULL, 0, ?, ?)
            """

            sucesso = self.db.executar_query(
                query,
                (
                    placa,
                    modelo,
                    cor,
                    hora_entrada,
                    id_usuario_entrada,
                    id_turno_entrada,
                ),
            )

            if sucesso:
                # Atualiza contagem de vagas após cadastro
                novas_vagas_disponiveis = self.db.get_vagas_disponiveis()
                print("✅ Veículo cadastrado com sucesso!")
                print(f"🅿️  Vagas restantes: {novas_vagas_disponiveis}/{total_vagas}")
                print(f"🕒 Horário de entrada: {hora_entrada}")
                print(f"👤 Registrado por: {self.usuario_logado[2]}")
            else:
                print("❌ Erro ao cadastrar veículo!")

        except Exception as erro:
            print(f"❌ Erro inesperado ao cadastrar veículo: {erro}")

    def registrar_saida(self):
        """Registra a saída de um veículo e calcula o valor a pagar"""
        if not self.turno_aberto:
            print("❌ Nenhum turno aberto! Abra um turno primeiro.")
            return

        print("\n" + "=" * 50)
        print("           REGISTRAR SAÍDA DE VEÍCULO")
        print("=" * 50)

        try:
            placa = input("Digite a placa do veículo: ").upper().strip()

            if not placa:
                print("❌ Erro: Placa não pode estar vazia!")
                return

            veiculo = self.db.buscar_um(
                "SELECT * FROM veiculos WHERE placa = ?", (placa,)
            )

            if not veiculo:
                print("❌ Veículo não encontrado!")
                return

            (
                id_vei,
                placa_veic,
                modelo,
                cor,
                hora_entrada,
                hora_saida,
                valor_pago,
                tempo_permanencia,
                id_usuario_entrada,
                id_usuario_saida,
                id_turno_entrada,
                id_turno_saida,
            ) = veiculo

            if hora_saida is not None:
                print("❌ Este veículo já teve sua saída registrada!")
                print(f"🕒 Saída registrada em: {hora_saida}")
                if valor_pago > 0:
                    print(f"💰 Valor pago: R$ {valor_pago:.2f}")
                return

            hora_saida = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Calcula o valor a pagar
            valor_a_pagar, horas, minutos_totais = self.db.calcular_valor_a_pagar(
                hora_entrada, hora_saida
            )
            tolerancia = self.db.get_tolerancia_minutos()

            print(f"\n📋 DADOS DO VEÍCULO:")
            print(f"🚗 Placa: {placa_veic}")
            print(f"🔧 Modelo: {modelo}")
            print(f"🎨 Cor: {cor}")
            print(f"⏰ Entrada: {hora_entrada}")
            print(f"⏰ Saída: {hora_saida}")
            print(f"⏱️  Tempo total: {minutos_totais:.0f} minutos")
            print(f"🎁 Tolerância: {tolerancia} minutos")
            print(
                f"⏱️  Tempo cobrado: {max(0, minutos_totais - tolerancia):.0f} minutos"
            )
            print("-" * 50)

            if horas == 0:
                print("🎉 Dentro do período de tolerância - ISENTO!")
                valor_a_pagar = 0
            else:
                print(f"💰 VALOR A PAGAR: R$ {valor_a_pagar:.2f}")
                print(f"⏰ Horas cobradas: {horas:.0f}")
                if horas > 1:
                    print(f"📈 Horas extras: {horas - 1:.0f}")

            print("-" * 50)
            confirmacao = input("Confirmar saída e valor? (s/n): ").lower()

            if confirmacao == "s":
                # Formata tempo de permanência para exibição
                horas_int = int(minutos_totais // 60)
                minutos_int = int(minutos_totais % 60)
                tempo_formatado = f"{horas_int:02d}:{minutos_int:02d}"

                id_usuario_saida = self.usuario_logado[0]
                id_turno_saida = self.turno_aberto[0]

                # Atualiza o veículo com saída e valor pago
                sucesso = self.db.executar_query(
                    "UPDATE veiculos SET hora_saida = ?, valor_pago = ?, tempo_permanencia = ?, id_usuario_saida = ?, id_turno_saida = ? WHERE placa = ?",
                    (
                        hora_saida,
                        valor_a_pagar,
                        tempo_formatado,
                        id_usuario_saida,
                        id_turno_saida,
                        placa,
                    ),
                )

                if sucesso and valor_a_pagar > 0:
                    # Registra a venda no caixa
                    self.db.registrar_movimentacao(
                        id_turno_saida,
                        "venda",
                        valor_a_pagar,
                        f"Pagamento veículo {placa} - {modelo}",
                        id_vei,
                    )

                if sucesso:
                    # Mostra vagas disponíveis após saída
                    vagas_disponiveis = self.db.get_vagas_disponiveis()
                    total_vagas = self.db.get_total_vagas()

                    print("✅ Saída registrada com sucesso!")
                    if valor_a_pagar > 0:
                        print(f"💰 Valor cobrado: R$ {valor_a_pagar:.2f}")
                        print(f"💰 Registrado no caixa por: {self.usuario_logado[2]}")
                    print(f"🅿️  Vagas disponíveis: {vagas_disponiveis}/{total_vagas}")
                else:
                    print("❌ Erro ao registrar saída!")
            else:
                print("ℹ️  Operação cancelada pelo usuário.")

        except Exception as erro:
            print(f"❌ Erro ao registrar saída: {erro}")

    # MÉTODOS DE CAIXA E TURNOS (NOVOS)
    def abrir_turno(self):
        """Abre um novo turno de trabalho"""
        print("\n" + "=" * 50)
        print("              ABRIR TURNO")
        print("=" * 50)

        try:
            saldo_inicial = self.db.get_saldo_inicial_caixa()
            print(f"💰 Saldo inicial sugerido: R$ {saldo_inicial:.2f}")

            novo_saldo = input(
                f"Saldo inicial do caixa [R$ {saldo_inicial:.2f}]: "
            ).strip()

            if novo_saldo:
                try:
                    saldo_inicial = float(novo_saldo)
                    if saldo_inicial < 0:
                        print("❌ Erro: Saldo inicial não pode ser negativo!")
                        return
                except ValueError:
                    print("❌ Erro: Digite um valor numérico válido!")
                    return

            id_turno = self.db.abrir_turno(self.usuario_logado[0], saldo_inicial)

            if id_turno:
                # Busca dados completos do turno
                self.turno_aberto = self.db.buscar_um(
                    "SELECT * FROM turnos WHERE id_turno = ?", (id_turno,)
                )
                print("✅ Turno aberto com sucesso!")
                print(f"👤 Operador: {self.usuario_logado[2]}")
                print(f"💰 Saldo inicial: R$ {saldo_inicial:.2f}")
                print(f"🕒 Abertura: {self.turno_aberto[2]}")
            else:
                print("❌ Erro ao abrir turno!")

        except Exception as erro:
            print(f"❌ Erro ao abrir turno: {erro}")

    def fechar_turno(self):
        """Fecha o turno atual"""
        if not self.turno_aberto:
            print("❌ Nenhum turno aberto para fechar!")
            return

        print("\n" + "=" * 50)
        print("              FECHAR TURNO")
        print("=" * 50)

        try:
            saldo_atual = self.db.get_saldo_turno(self.turno_aberto[0])
            total_vendas = self.db.get_total_vendas_turno(self.turno_aberto[0])

            print(f"📊 RESUMO DO TURNO:")
            print(f"👤 Operador: {self.usuario_logado[2]}")
            print(f"🕒 Abertura: {self.turno_aberto[2]}")
            print(f"💰 Saldo inicial: R$ {self.turno_aberto[4]:.2f}")
            print(f"💰 Total de vendas: R$ {total_vendas:.2f}")
            print(f"💰 Saldo atual: R$ {saldo_atual:.2f}")
            print("-" * 50)

            # Conta veículos atendidos neste turno
            veiculos_turno = self.db.buscar_dados(
                """
                SELECT COUNT(*) FROM veiculos 
                WHERE id_turno_entrada = ? OR id_turno_saida = ?
            """,
                (self.turno_aberto[0], self.turno_aberto[0]),
            )

            print(
                f"🚗 Veículos atendidos: {veiculos_turno[0][0] if veiculos_turno else 0}"
            )
            print("-" * 50)

            saldo_final = input(
                f"Saldo final em caixa [R$ {saldo_atual:.2f}]: "
            ).strip()

            if saldo_final:
                try:
                    saldo_final = float(saldo_final)
                    if saldo_final < 0:
                        print("❌ Erro: Saldo final não pode ser negativo!")
                        return
                except ValueError:
                    print("❌ Erro: Digite um valor numérico válido!")
                    return
            else:
                saldo_final = saldo_atual

            confirmacao = input("Confirmar fechamento do turno? (s/n): ").lower()

            if confirmacao == "s":
                sucesso = self.db.fechar_turno(self.turno_aberto[0], saldo_final)

                if sucesso:
                    print("✅ Turno fechado com sucesso!")
                    print(f"💰 Saldo final: R$ {saldo_final:.2f}")
                    self.turno_aberto = None
                else:
                    print("❌ Erro ao fechar turno!")
            else:
                print("ℹ️  Operação cancelada.")

        except Exception as erro:
            print(f"❌ Erro ao fechar turno: {erro}")

    def status_caixa(self):
        """Mostra status atual do caixa"""
        if not self.turno_aberto:
            print("❌ Nenhum turno aberto!")
            return

        print("\n" + "=" * 50)
        print("             STATUS DO CAIXA")
        print("=" * 50)

        try:
            saldo_atual = self.db.get_saldo_turno(self.turno_aberto[0])
            total_vendas = self.db.get_total_vendas_turno(self.turno_aberto[0])

            print(f"👤 Operador: {self.usuario_logado[2]}")
            print(f"🕒 Abertura: {self.turno_aberto[2]}")
            print(f"💰 Saldo inicial: R$ {self.turno_aberto[4]:.2f}")
            print(f"💰 Total de vendas: R$ {total_vendas:.2f}")
            print(f"💰 Saldo atual: R$ {saldo_atual:.2f}")
            print("-" * 50)

            # Últimas movimentações
            movimentacoes = self.db.buscar_dados(
                """
                SELECT tipo, valor, descricao, data_hora 
                FROM movimentacoes_caixa 
                WHERE id_turno = ? 
                ORDER BY data_hora DESC 
                LIMIT 10
            """,
                (self.turno_aberto[0],),
            )

            if movimentacoes:
                print("📋 ÚLTIMAS MOVIMENTAÇÕES:")
                for mov in movimentacoes:
                    tipo, valor, descricao, data_hora = mov
                    icone = (
                        "💵" if tipo == "venda" else "📤" if tipo == "saida" else "💰"
                    )
                    print(
                        f"   {icone} {data_hora[11:16]} - {descricao}: R$ {valor:.2f}"
                    )
            else:
                print("📭 Nenhuma movimentação registrada.")

            print("=" * 50)

        except Exception as erro:
            print(f"❌ Erro ao consultar caixa: {erro}")

    # MÉTODOS EXISTENTES (com pequenas adaptações)
    def listar(self):
        """Lista todos os veículos cadastrados"""
        print("\n" + "=" * 50)
        print("           LISTA DE VEÍCULOS CADASTRADOS")
        print("=" * 50)

        try:
            veiculos = self.db.buscar_dados(
                """
                SELECT v.*, u1.nome as usuario_entrada, u2.nome as usuario_saida 
                FROM veiculos v 
                LEFT JOIN usuarios u1 ON v.id_usuario_entrada = u1.id_usuario 
                LEFT JOIN usuarios u2 ON v.id_usuario_saida = u2.id_usuario 
                ORDER BY v.hora_entrada DESC
            """
            )

            if not veiculos:
                print("📭 Nenhum veículo cadastrado no sistema.")
                return

            print(f"📊 Total de veículos encontrados: {len(veiculos)}")
            print("-" * 50)

            for veiculo in veiculos:
                (
                    id_vei,
                    placa,
                    modelo,
                    cor,
                    hora_entrada,
                    hora_saida,
                    valor_pago,
                    tempo_permanencia,
                    id_usuario_entrada,
                    id_usuario_saida,
                    id_turno_entrada,
                    id_turno_saida,
                    usuario_entrada,
                    usuario_saida,
                ) = veiculo

                if hora_saida is None:
                    status = "🅿️  NO ESTACIONAMENTO"
                else:
                    status = "✅ SAÍDA REGISTRADA"

                print(f"\n🔸 ID: {id_vei}")
                print(f"🔸 Placa: {placa}")
                print(f"🔸 Modelo: {modelo}")
                print(f"🔸 Cor: {cor}")
                print(f"🔸 Entrada: {hora_entrada}")
                print(
                    f"🔸 Saída: {hora_saida if hora_saida else 'Ainda no estacionamento'}"
                )
                if hora_saida and tempo_permanencia:
                    print(f"🔸 Tempo: {tempo_permanencia}")
                if valor_pago > 0:
                    print(f"🔸 Valor pago: R$ {valor_pago:.2f}")
                print(f"🔸 Entrada por: {usuario_entrada}")
                if usuario_saida:
                    print(f"🔸 Saída por: {usuario_saida}")
                print(f"🔸 Status: {status}")
                print("-" * 40)

        except Exception as erro:
            print(f"❌ Erro ao listar veículos: {erro}")

    # ... (os outros métodos existentes como atualizar, excluir, listar_estacionados, etc.
    # permanecem iguais, apenas adaptados para usar self.usuario_logado quando necessário)

    def configurar_valores(self):
        """Configura os valores do estacionamento"""
        if self.usuario_logado[3] != "admin":
            print("❌ Acesso negado! Apenas administradores podem configurar valores.")
            return

        print("\n" + "=" * 50)
        print("        CONFIGURAR VALORES DO ESTACIONAMENTO")
        print("=" * 50)

        try:
            valor_atual = self.db.get_valor_hora()
            acrescimo_atual = self.db.get_acrescimo_hora_extra()
            tolerancia_atual = self.db.get_tolerancia_minutos()
            saldo_inicial = self.db.get_saldo_inicial_caixa()

            print(f"💰 Valor atual da 1ª hora: R$ {valor_atual:.2f}")
            print(f"📈 Acréscimo atual por hora extra: R$ {acrescimo_atual:.2f}")
            print(f"⏰ Tolerância atual: {tolerancia_atual} minutos")
            print(f"💵 Saldo inicial do caixa: R$ {saldo_inicial:.2f}")
            print("-" * 50)

            print("Deixe em branco para manter o valor atual:")

            novo_valor = input(
                f"Novo valor da 1ª hora [R$ {valor_atual:.2f}]: "
            ).strip()
            novo_acrescimo = input(
                f"Novo acréscimo por hora extra [R$ {acrescimo_atual:.2f}]: "
            ).strip()
            nova_tolerancia = input(
                f"Nova tolerância em minutos [{tolerancia_atual}]: "
            ).strip()
            novo_saldo = input(
                f"Novo saldo inicial do caixa [R$ {saldo_inicial:.2f}]: "
            ).strip()

            # Processa novos valores
            if novo_valor:
                try:
                    novo_valor_float = float(novo_valor)
                    if novo_valor_float <= 0:
                        print("❌ Erro: O valor deve ser maior que zero!")
                        return
                    self.db.set_valor_hora(novo_valor_float)
                    print(f"✅ Valor da hora atualizado para R$ {novo_valor_float:.2f}")
                except ValueError:
                    print("❌ Erro: Digite um valor numérico válido!")
                    return

            if novo_acrescimo:
                try:
                    novo_acrescimo_float = float(novo_acrescimo)
                    if novo_acrescimo_float < 0:
                        print("❌ Erro: O acréscimo não pode ser negativo!")
                        return
                    self.db.set_acrescimo_hora_extra(novo_acrescimo_float)
                    print(f"✅ Acréscimo atualizado para R$ {novo_acrescimo_float:.2f}")
                except ValueError:
                    print("❌ Erro: Digite um valor numérico válido!")
                    return

            if nova_tolerancia:
                try:
                    nova_tolerancia_int = int(nova_tolerancia)
                    if nova_tolerancia_int < 0:
                        print("❌ Erro: A tolerância não pode ser negativa!")
                        return
                    self.db.set_tolerancia_minutos(nova_tolerancia_int)
                    print(
                        f"✅ Tolerância atualizada para {nova_tolerancia_int} minutos"
                    )
                except ValueError:
                    print("❌ Erro: Digite um número inteiro válido!")
                    return

            if novo_saldo:
                try:
                    novo_saldo_float = float(novo_saldo)
                    if novo_saldo_float < 0:
                        print("❌ Erro: O saldo não pode ser negativo!")
                        return
                    self.db.executar_query(
                        "INSERT OR REPLACE INTO config (chave, valor) VALUES ('saldo_inicial_caixa', ?)",
                        (str(novo_saldo_float),),
                    )
                    print(f"✅ Saldo inicial atualizado para R$ {novo_saldo_float:.2f}")
                except ValueError:
                    print("❌ Erro: Digite um valor numérico válido!")
                    return

            if (
                not novo_valor
                and not novo_acrescimo
                and not nova_tolerancia
                and not novo_saldo
            ):
                print("ℹ️  Nenhum valor foi alterado.")

        except Exception as erro:
            print(f"❌ Erro ao configurar valores: {erro}")

    def gerenciar_usuarios(self):
        """Gerencia usuários do sistema"""
        if self.usuario_logado[3] != "admin":
            print("❌ Acesso negado! Apenas administradores podem gerenciar usuários.")
            return

        print("\n" + "=" * 50)
        print("           GERENCIAR USUÁRIOS")
        print("=" * 50)

        try:
            while True:
                print("\n1. 📋 Listar usuários")
                print("2. 👤 Adicionar usuário")
                print("3. 🔄 Alterar status do usuário")
                print("4. ↩️  Voltar")

                opcao = input("\nEscolha uma opção: ").strip()

                if opcao == "1":
                    self.listar_usuarios()
                elif opcao == "2":
                    self.adicionar_usuario()
                elif opcao == "3":
                    self.alterar_status_usuario()
                elif opcao == "4":
                    break
                else:
                    print("❌ Opção inválida!")

        except Exception as erro:
            print(f"❌ Erro no gerenciamento de usuários: {erro}")

    def listar_usuarios(self):
        """Lista todos os usuários"""
        usuarios = self.db.listar_usuarios()

        if not usuarios:
            print("📭 Nenhum usuário cadastrado.")
            return

        print(f"\n📋 USUÁRIOS CADASTRADOS ({len(usuarios)}):")
        print("-" * 60)
        for usuario in usuarios:
            id_user, username, nome, perfil, ativo = usuario
            status = "✅ Ativo" if ativo else "❌ Inativo"
            print(f"👤 {nome} ({username})")
            print(f"   🏷️  Perfil: {perfil} | Status: {status}")
            print("-" * 30)

    def adicionar_usuario(self):
        """Adiciona novo usuário"""
        print("\n👤 ADICIONAR NOVO USUÁRIO")
        print("-" * 30)

        username = input("Username: ").strip()
        senha = input("Senha: ").strip()
        nome = input("Nome completo: ").strip()

        print("\nPerfis disponíveis:")
        print("1. 👑 Admin - Acesso total")
        print("2. 👨‍💼 Gerente - Acesso gerencial")
        print("3. 👨‍💻 Operador - Acesso operacional")

        perfil_opcao = input("Escolha o perfil (1-3): ").strip()

        perfis = {"1": "admin", "2": "gerente", "3": "operador"}
        perfil = perfis.get(perfil_opcao, "operador")

        if not username or not senha or not nome:
            print("❌ Todos os campos são obrigatórios!")
            return

        sucesso = self.db.criar_usuario(username, senha, nome, perfil)

        if sucesso:
            print("✅ Usuário criado com sucesso!")
            print(f"👤 {nome} ({username}) - Perfil: {perfil}")
        else:
            print("❌ Erro ao criar usuário! Username já existe.")

    def alterar_status_usuario(self):
        """Altera status de usuário (ativo/inativo)"""
        usuarios = self.db.listar_usuarios()

        if not usuarios:
            print("📭 Nenhum usuário cadastrado.")
            return

        print("\n🔃 ALTERAR STATUS DE USUÁRIO")
        print("-" * 40)

        for i, usuario in enumerate(usuarios, 1):
            id_user, username, nome, perfil, ativo = usuario
            status = "✅ Ativo" if ativo else "❌ Inativo"
            print(f"{i}. {nome} ({username}) - {status}")

        try:
            opcao = int(input("\nEscolha o usuário (número): ")) - 1
            if 0 <= opcao < len(usuarios):
                usuario = usuarios[opcao]
                novo_status = 0 if usuario[4] else 1  # Inverte o status

                query = "UPDATE usuarios SET ativo = ? WHERE id_usuario = ?"
                sucesso = self.db.executar_query(query, (novo_status, usuario[0]))

                if sucesso:
                    status_msg = "ativado" if novo_status else "desativado"
                    print(f"✅ Usuário {status_msg} com sucesso!")
                else:
                    print("❌ Erro ao alterar status!")
            else:
                print("❌ Opção inválida!")
        except ValueError:
            print("❌ Digite um número válido!")


if __name__ == "__main__":
    from database.database import Database

    db = Database()
    veiculo = Veiculo(db)
    print("🎉 Classe Veiculo carregada com sucesso!")
