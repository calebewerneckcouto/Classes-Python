from usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)  # Chama o construtor da classe pai (Usuario)

    def imprime_usuario(self):
        print(f"{self.nome} ({self.email}) – Administrador")
