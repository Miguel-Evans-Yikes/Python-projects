from datetime import datetime.now()

class Produto:
    def __init__(self, nome, preço, validade, peso, codigo):
        self.nome = nome
        self.preço = preço
        self.validade = validade
        self.peso = peso
        self.codigo = codigo

#ADICIONAR METODOS GETTERS E SETTERS

    def get_nome(self):
        return self.nome

    def set_nome(self, newNome):
        self.nome = newNome

    def get_preço(self):
        return self.preço

    def set_preço(self, newPreço):
        self.preço = newPreço

    def get_validade(self):
        return self.validade

    @property
    def set_validade(self, newValidade):
        self.validade = newValidade

    def get_peso(self):
        return self.peso

    @property
    def set_peso(self, newPeso):
        self.peso = newPeso

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, newCodigo):
        self.codigo = newCodigo

    


class Storage:
    def __init__(self):
        storage = []

#adiciona um novo objeto na lista storage pelo método append()
    def add_to_store(self):
        nome = input("Digite o nome do novo produto: ")
        preço = float(input("Digite o preço do novo produto: "))
        validade = input("Digite a data de validade do novo produto: ")
        peso = float(input("Digite o peso do novo produto: "))
        codigo = int(input("Digite o nome do novo produto: "))
        return storage.append(Produto(nome,preço,validade,peso,codigo))

#faz busca na lista storage e aplica o método remove()
    def del_from_store(self):
        del_code = int(input("Digite o código do produto a ser excluido: "))
        for item in storage:
            print(f'Produto {item.nome} tem o código {item.codigo} fornecido')
            if item.codigo == del_code:
                storage.remove(item)
            if del_code not in storage[item.codigo]:
                print("Produto não encontrado!")
            

#itera sobre a lista storage mostrando os nomes dos produtos disponíveis
    def show_items(self):
        for prods in storage:
            print(f'\nProdutos disponíveis: {prods.nome}')

#faz busca na lista storage e aplica o método replace()
    def update_nome(self):
        name = input("Digite o nome do produto a ser substituído: ")
        novo_nome = input("Digite o novo nome do Produto: ")

        for i in storage:
            print(f'O Produto {i.nome} foi substituido por {novo}')
            if i.nome == name:
                return i.set_nome(novo_nome)

    def update_preço(self):
        name1 = input("Digite o nome do produto a ter o preço atualizado: ")
        novo_preço = float(input("Digite o novo preço do Produto: "))

        for i in storage:
            print(f'O Produto {i.nome} teve o preço atualizado para{novo_preço}')
            if i.nome == name1:
                return i.set_preço(novo_preço)
            

    def update_codigo(self):
        name2 = input("Digite o nome do produto ter o código atualizado: ")
        novo_codigo = int(input("Digite o novo código do Produto: "))

#E se acontecer de um produto ter o mesmo código de outro(s)?
        for i in storage:
            print(f'O Produto {i.nome} teve o código {i.codigo} atualizado para {novo_codigo}')
            if i.nome == name2:
                return i.set_codigo(novo_codigo)
            




#Informa quais produtos estão perto do vencimento da validade 
    def validade_próxima(self):
        pass
            
        












        
class Faturamento:
    def __init__(self):
        pass

class Cliente:
    def __init__(self):
        pass

class Compra:
    def __init__(self):
        pass



















