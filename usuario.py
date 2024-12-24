class Usuario:
    quantidade = 0  # Atributo de classe para contar instâncias criadas

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        Usuario.quantidade += 1  # Incrementa a quantidade sempre que uma instância é criada

    def imprime_usuario(self):
        print(f"{self.nome} ({self.email})")
