def add_contact(contacts, name, phone_number, email):
  contact = {"name": name, "phone": phone_number, "email": email, "favorite": False}
  contacts.append(contact)
  print(f"\nO contato {name} foi adicionado com sucesso!")
  return

def view_contacts(contacts):
  print("\nLista de contatos existentes: ")
  for index, contact in enumerate(contacts, start=1):
    name = contact["name"]
    phone = contact["phone"]
    email = contact["email"]
    favorite = '★' if contact["favorite"] else '☆'
    print(f"{index}. Nome: {name}, \n   Telefone: {phone}, \n   E-mail: {email}, \n   Favorito: {favorite}")
  return

def update_contact(contacts, contact_info_keys, contact_index):
  try:
    contact_index_adjusted = int(contact_index) - 1
    chosen_contact = contacts[contact_index_adjusted]
    print("\nInformações do contato:")
    for index, key in enumerate(contact_info_keys, start=1):
      print(f"{index} - {key}")

    info_index_to_update = input("Digite o número referente a informação que gostaria de atualizar: ")
    info_index_to_update_adusted = int(info_index_to_update) - 1
    info_new_value = input(f"Digite o novo {contact_info_keys[info_index_to_update_adusted]}: ")

    key_to_update = list(chosen_contact.keys())[info_index_to_update_adusted]
    contacts[contact_index_adjusted][key_to_update] = info_new_value
    
    print(f"Atualizado o {contact_info_keys[info_index_to_update_adusted]} para {info_new_value} com sucesso!")
    view_contacts(contacts)
  except Exception as e:
    print(f"Error: {e}")
  return

contacts = []
contact_info_keys = ['Nome', 'Telefone', 'E-mail']
while True:
  print("\n Menu do Gerenciador de Contatos")
  print("1. Adicionar contato")
  print("2. Visualizar contatos")
  print("3. Editar contato")
  print("4. Marcar/Descamarcar contato como favorito")
  print("5. Visualizar contatos favoritados")
  print("5. Apagar contato")
  print("6. Sair")
  chosen_option = input("Digite sua escolha: ")

  if (chosen_option == "1"):
    print("\nPor favor, digite as informações abaixo.")
    name = input("Nome do contato: ")
    phone_number = input("Número de telefone: ")
    email = input("Email: ")
    add_contact(contacts, name, phone_number, email)
  elif (chosen_option == "2"):
    view_contacts(contacts)
  elif (chosen_option == "3"):
    view_contacts(contacts)
    contact_index = input("Digite o número referente ao contato que deseja editar: ")
    update_contact(contacts, contact_info_keys, contact_index)
  elif (chosen_option == "6"):
    break