from datetime import datetime

class Veiculo:
    """
    Classe para gerenciar as operações com veículos no sistema
    Implementa as operações CRUD: Create, Read, Update, Delete
    """
    
    def __init__(self, db):
        """
        Inicializa a classe Veiculo com conexão ao banco de dados
        
        Args:
            db: Instância da classe Database para operações no banco
        """
        self.db = db
        
        
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa

    def __str__(self):
        return f"{self.modelo} ({self.placa})"

    
    def cadastrar(self):
        """Cadastra um novo veículo no sistema"""
        print("\n" + "="*50)
        print("          CADASTRAR NOVO VEÍCULO")
        print("="*50)
        
        try:
            # Coleta dados do usuário
            placa = input("Placa do veículo: ").upper().strip()
            modelo = input("Modelo do veículo: ").strip()
            cor = input("Cor do veículo: ").strip()
            
            # Validações básicas
            if not placa or not modelo or not cor:
                print("❌ Erro: Todos os campos são obrigatórios!")
                return
            
            # Verifica se a placa já existe usando o método específico
            if self.db.verificar_placa_existe(placa):
                print("❌ Erro: Já existe um veículo com esta placa!")
                return
            
            # Obtém a hora atual formatada
            hora_entrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Prepara e executa a query de inserção
            query = """
                INSERT INTO veiculos (placa, modelo, cor, hora_entrada, hora_saida)
                VALUES (?, ?, ?, ?, NULL)
            """
            
            # Executa a query e verifica se foi bem-sucedida
            sucesso = self.db.executar_query(query, (placa, modelo, cor, hora_entrada))
            
            if sucesso:
                print("✅ Veículo cadastrado com sucesso!")
            else:
                print("❌ Erro ao cadastrar veículo!")
            
        except Exception as erro:
            print(f"❌ Erro inesperado ao cadastrar veículo: {erro}")
    
    def listar(self):
        """Lista todos os veículos cadastrados no sistema"""
        print("\n" + "="*50)
        print("           LISTA DE VEÍCULOS CADASTRADOS")
        print("="*50)
        
        try:
            # Busca todos os veículos no banco
            veiculos = self.db.buscar_dados("SELECT * FROM veiculos ORDER BY hora_entrada DESC")
            
            if not veiculos:
                print("📭 Nenhum veículo cadastrado no sistema.")
                return
            
            print(f"📊 Total de veículos encontrados: {len(veiculos)}")
            print("-" * 50)
            
            for veiculo in veiculos:
                # Desempacota os dados do veículo
                id_vei, placa, modelo, cor, hora_entrada, hora_saida = veiculo
                
                # Determina o status do veículo
                if hora_saida is None:
                    status = "🅿️  NO ESTACIONAMENTO"
                    status_cor = "VERDE"
                else:
                    status = "✅ SAÍDA REGISTRADA"
                    status_cor = "AZUL"
                
                # Exibe os dados formatados
                print(f"\n🔸 ID: {id_vei}")
                print(f"🔸 Placa: {placa}")
                print(f"🔸 Modelo: {modelo}")
                print(f"🔸 Cor: {cor}")
                print(f"🔸 Entrada: {hora_entrada}")
                print(f"🔸 Saída: {hora_saida if hora_saida else 'Ainda no estacionamento'}")
                print(f"🔸 Status: {status}")
                print("-" * 40)
                
        except Exception as erro:
            print(f"❌ Erro ao listar veículos: {erro}")
    
    def atualizar(self):
        """Atualiza os dados de um veículo existente"""
        print("\n" + "="*50)
        print("           ATUALIZAR DADOS DO VEÍCULO")
        print("="*50)
        
        try:
            placa = input("Digite a placa do veículo a ser atualizado: ").upper().strip()
            
            if not placa:
                print("❌ Erro: Placa não pode estar vazia!")
                return
            
            # Verifica se o veículo existe - CORREÇÃO AQUI
            veiculo = self.db.buscar_um("SELECT * FROM veiculos WHERE placa = ?", (placa,))
            
            if not veiculo:
                print("❌ Veículo não encontrado!")
                return
            
            # Desempacota os dados do veículo encontrado
            id_vei, placa_antiga, modelo_antigo, cor_antiga, hora_entrada, hora_saida = veiculo
            
            print(f"\n📝 Editando veículo - Placa: {placa_antiga}")
            print("Deixe em branco para manter o valor atual:")
            
            # Solicita novos dados
            novo_modelo = input(f"Novo modelo [{modelo_antigo}]: ").strip()
            nova_cor = input(f"Nova cor [{cor_antiga}]: ").strip()
            
            # Mantém valores antigos se não forem informados novos
            modelo_final = novo_modelo if novo_modelo else modelo_antigo
            cor_final = nova_cor if nova_cor else cor_antiga
            
            # Valida se pelo menos um campo foi alterado
            if modelo_final == modelo_antigo and cor_final == cor_antiga:
                print("ℹ️  Nenhum dado foi alterado.")
                return
            
            # Executa a atualização
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
        print("\n" + "="*50)
        print("             EXCLUIR VEÍCULO")
        print("="*50)
        
        try:
            placa = input("Digite a placa do veículo a ser excluído: ").upper().strip()
            
            if not placa:
                print("❌ Erro: Placa não pode estar vazia!")
                return
            
            # Verifica se o veículo existe
            veiculo = self.db.buscar_um("SELECT * FROM veiculos WHERE placa = ?", (placa,))
            
            if not veiculo:
                print("❌ Veículo não encontrado!")
                return
            
            id_vei, placa_veic, modelo, cor, hora_entrada, hora_saida = veiculo
            
            # Mostra dados do veículo para confirmação
            print(f"\n📋 Dados do veículo a ser excluído:")
            print(f"Placa: {placa_veic}")
            print(f"Modelo: {modelo}")
            print(f"Cor: {cor}")
            print(f"Entrada: {hora_entrada}")
            
            # Confirmação de segurança
            confirmacao = input(f"\n⚠️  TEM CERTEZA que deseja excluir o veículo {placa}? (s/n): ").lower()
            
            if confirmacao == 's':
                sucesso = self.db.executar_query("DELETE FROM veiculos WHERE placa = ?", (placa,))
                
                if sucesso:
                    print("✅ Veículo excluído com sucesso!")
                else:
                    print("❌ Erro ao excluir veículo!")
            else:
                print("ℹ️  Operação cancelada pelo usuário.")
                
        except Exception as erro:
            print(f"❌ Erro ao excluir veículo: {erro}")
    
    def registrar_saida(self):
        """Registra a saída de um veículo do estacionamento"""
        print("\n" + "="*50)
        print("           REGISTRAR SAÍDA DE VEÍCULO")
        print("="*50)
        
        try:
            placa = input("Digite a placa do veículo: ").upper().strip()
            
            if not placa:
                print("❌ Erro: Placa não pode estar vazia!")
                return
            
            # Verifica se o veículo existe
            veiculo = self.db.buscar_um("SELECT * FROM veiculos WHERE placa = ?", (placa,))
            
            if not veiculo:
                print("❌ Veículo não encontrado!")
                return
            
            id_vei, placa_veic, modelo, cor, hora_entrada, hora_saida = veiculo
            
            # Verifica se já teve saída registrada - CORREÇÃO AQUI
            if hora_saida is not None:
                print("❌ Este veículo já teve sua saída registrada!")
                print(f"🕒 Saída registrada em: {hora_saida}")
                return
            
            # Registra a hora de saída atual
            hora_saida = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Executa a atualização
            sucesso = self.db.executar_query(
                "UPDATE veiculos SET hora_saida = ? WHERE placa = ?", 
                (hora_saida, placa)
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
        print("\n" + "="*50)
        print("      VEÍCULOS NO ESTACIONAMENTO")
        print("="*50)
        
        try:
            # Busca veículos sem hora de saída
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
            
    

# Teste da classe
if __name__ == "__main__":
    from database.database import Database
    db = Database()
    veiculo = Veiculo(db)
    print("🎉 Classe Veiculo carregada com sucesso!")