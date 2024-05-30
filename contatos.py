def add_contact(contacts, name, phone_number, email):
  contact = {"name": name, "phone": phone_number, "email": email, "favorite": False}
  contacts.append(contact)
  print(f"O contato {name} foi adicionado com sucesso!")
  return

contacts = []

while True:
  print("\n Menu do Gerenciador de Lista de contatos")
  print("1. Adicionar contato")
  print("2. Visualizar contatos")
  print("3. Editar contato")
  print("4. Marcar/Descamarcar contato como favorito")
  print("5. Visualizar conttaos favoritados")
  print("5. Apagar contato")
  print("6. Sair")
  chosen_option = input("Digite sua escolha: ")
  
  if (chosen_option == "1"):
    print("\nPor favor, digite as informações abaixo: ")
    name = input("Nome do contato: ")
    phone_number = input("Número de telefone: ")
    email = input("Email: ")
    add_contact(contacts, name, phone_number, email)
  elif (chosen_option == "6"):
    break