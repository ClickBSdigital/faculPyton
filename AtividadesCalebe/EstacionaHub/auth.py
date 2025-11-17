from models import Usuario


class AuthSystem:
    def __init__(self):
        self.usuario_atual = None

    def login(self):
        print("\n=== LOGIN ===")
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        user_data = Usuario.autenticar(usuario, senha)
        if user_data:
            self.usuario_atual = Usuario(**user_data)
            print(f"\nBem-vindo, {self.usuario_atual.nome}!")
            return True
        print("Credenciais inválidas!")
        return False

    def logout(self):
        self.usuario_atual = None
        print("Logout realizado com sucesso!")

    def is_admin(self):
        return self.usuario_atual and self.usuario_atual.tipo == "admin"
