from datetime import datetime


class Veiculo:
    """
    Classe para gerenciar as operações com veículos no sistema
    """

    def __init__(self, db):
        self.db = db

    def cadastrar(self):
        """Cadastra um novo veículo no sistema"""
        print("\n" + "=" * 50)
        print("          CADASTRAR NOVO VEÍCULO")
        print("=" * 50)

        try:
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

            query = """
                INSERT INTO veiculos (placa, modelo, cor, hora_entrada, hora_saida)
                VALUES (?, ?, ?, ?, NULL)
            """

            sucesso = self.db.executar_query(query, (placa, modelo, cor, hora_entrada))

            if sucesso:
                print("✅ Veículo cadastrado com sucesso!")
            else:
                print("❌ Erro ao cadastrar veículo!")

        except Exception as erro:
            print(f"❌ Erro inesperado ao cadastrar veículo: {erro}")

    def listar(self):
        """Lista todos os veículos cadastrados"""
        print("\n" + "=" * 50)
        print("           LISTA DE VEÍCULOS CADASTRADOS")
        print("=" * 50)

        try:
            veiculos = self.db.buscar_dados(
                "SELECT * FROM veiculos ORDER BY hora_entrada DESC"
            )

            if not veiculos:
                print("📭 Nenhum veículo cadastrado no sistema.")
                return

            print(f"📊 Total de veículos encontrados: {len(veiculos)}")
            print("-" * 50)

            for veiculo in veiculos:
                id_vei, placa, modelo, cor, hora_entrada, hora_saida = veiculo

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
                print(f"🔸 Status: {status}")
                print("-" * 40)

        except Exception as erro:
            print(f"❌ Erro ao listar veículos: {erro}")

    def atualizar(self):
        """Atualiza os dados de um veículo"""
        print("\n" + "=" * 50)
        print("           ATUALIZAR DADOS DO VEÍCULO")
        print("=" * 50)

        try:
            placa = (
                input("Digite a placa do veículo a ser atualizado: ").upper().strip()
            )

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
                placa_antiga,
                modelo_antigo,
                cor_antiga,
                hora_entrada,
                hora_saida,
            ) = veiculo

            print(f"\n📝 Editando veículo - Placa: {placa_antiga}")
            print("Deixe em branco para manter o valor atual:")

            novo_modelo = input(f"Novo modelo [{modelo_antigo}]: ").strip()
            nova_cor = input(f"Nova cor [{cor_antiga}]: ").strip()

            modelo_final = novo_modelo if novo_modelo else modelo_antigo
            cor_final = nova_cor if nova_cor else cor_antiga

            if modelo_final == modelo_antigo and cor_final == cor_antiga:
                print("ℹ️  Nenhum dado foi alterado.")
                return

            query = "UPDATE veiculos SET modelo = ?, cor = ? WHERE placa = ?"
            sucesso = self.db.executar_query(query, (modelo_final, cor_final, placa))

            if sucesso:
                print("✅ Veículo atualizado com sucesso!")
            else:
                print("❌ Erro ao atualizar veículo!")

        except Exception as erro:
            print(f"❌ Erro ao atualizar veículo: {erro}")

    def excluir(self):
        """Exclui um veículo do sistema"""
        print("\n" + "=" * 50)
        print("             EXCLUIR VEÍCULO")
        print("=" * 50)

        try:
            placa = input("Digite a placa do veículo a ser excluído: ").upper().strip()

            if not placa:
                print("❌ Erro: Placa não pode estar vazia!")
                return

            veiculo = self.db.buscar_um(
                "SELECT * FROM veiculos WHERE placa = ?", (placa,)
            )

            if not veiculo:
                print("❌ Veículo não encontrado!")
                return

            id_vei, placa_veic, modelo, cor, hora_entrada, hora_saida = veiculo

            print(f"\n📋 Dados do veículo a ser excluído:")
            print(f"Placa: {placa_veic}")
            print(f"Modelo: {modelo}")
            print(f"Cor: {cor}")
            print(f"Entrada: {hora_entrada}")

            confirmacao = input(
                f"\n⚠️  TEM CERTEZA que deseja excluir o veículo {placa}? (s/n): "
            ).lower()

            if confirmacao == "s":
                sucesso = self.db.executar_query(
                    "DELETE FROM veiculos WHERE placa = ?", (placa,)
                )

                if sucesso:
                    print("✅ Veículo excluído com sucesso!")
                else:
                    print("❌ Erro ao excluir veículo!")
            else:
                print("ℹ️  Operação cancelada pelo usuário.")

        except Exception as erro:
            print(f"❌ Erro ao excluir veículo: {erro}")

    def registrar_saida(self):
        """Registra a saída de um veículo"""
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

            id_vei, placa_veic, modelo, cor, hora_entrada, hora_saida = veiculo

            if hora_saida is not None:
                print("❌ Este veículo já teve sua saída registrada!")
                print(f"🕒 Saída registrada em: {hora_saida}")
                return

            hora_saida = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            sucesso = self.db.executar_query(
                "UPDATE veiculos SET hora_saida = ? WHERE placa = ?",
                (hora_saida, placa),
            )

            if sucesso:
                print("✅ Saída registrada com sucesso!")
                print(f"🕒 Horário de saída: {hora_saida}")
            else:
                print("❌ Erro ao registrar saída!")

        except Exception as erro:
            print(f"❌ Erro ao registrar saída: {erro}")

    def listar_estacionados(self):
        """Lista apenas os veículos que ainda estão no estacionamento"""
        print("\n" + "=" * 50)
        print("      VEÍCULOS NO ESTACIONAMENTO")
        print("=" * 50)

        try:
            veiculos = self.db.buscar_dados(
                "SELECT * FROM veiculos WHERE hora_saida IS NULL ORDER BY hora_entrada DESC"
            )

            if not veiculos:
                print("📭 Nenhum veículo no estacionamento no momento.")
                return

            print(f"🅿️  Veículos no estacionamento: {len(veiculos)}")
            print("-" * 50)

            for veiculo in veiculos:
                id_vei, placa, modelo, cor, hora_entrada, hora_saida = veiculo

                print(f"\n🔸 Placa: {placa}")
                print(f"🔸 Modelo: {modelo}")
                print(f"🔸 Cor: {cor}")
                print(f"🔸 Entrada: {hora_entrada}")
                print(f"🔸 Tempo estacionado: Desde {hora_entrada}")
                print("-" * 30)

        except Exception as erro:
            print(f"❌ Erro ao listar veículos estacionados: {erro}")


if __name__ == "__main__":
    from database.database import Database

    db = Database()
    veiculo = Veiculo(db)
    print("🎉 Classe Veiculo carregada com sucesso!")
