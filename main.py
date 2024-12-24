from usuario import Usuario
from administrador import Administrador

# Criando instâncias
u = Usuario("Gabriel", "gabriel@exemplo.com")
a = Administrador("Admin", "admin@exemplo.com")

# Imprimindo os detalhes dos usuários
u.imprime_usuario()  # Esperado: "Gabriel (gabriel@exemplo.com)"
a.imprime_usuario()  # Esperado: "Admin (admin@exemplo.com) – Administrador"

# Imprimindo a quantidade de instâncias criadas
print(Usuario.quantidade)  # Esperado: 2
