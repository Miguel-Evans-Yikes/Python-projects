"""
-App Supermercado:
	*uma cesta de compras
	*cliente tem uma compra
	*uma compra tem itens
	*cada item é um produto com nome, preço, data de validade, descrição, e peso.
	*a cada registro, o item deve permanecer na tela com o total somado
	*a cada finalização de compra, deve ser atualizado o estoque.
	*o faturamento, os itens vendidos diaria e mensalmente devem ser armazenados
	*deve ser possível o cancelamento de itens
	*
"""


class Product:
    def __init__(self, brand: str, name: str, price: float, ex_date: str, weight: float, quantity: float, description: str):

        self.brand = brand
        self.name = name
        self.price = price
        self.ex_date = ex_date
        self.quantity = quantity
        self.weight = weight
        self.desc = description


    #GETTERS E SETTERS
    def set_name(self, newName) -> str:
        self.name = NewName

    def get_name(self) -> str:
        return self.name

    #GETTERS E SETTERS DE PRICE
    def get_Price(self)-> str:
        return self.price

    def set_Price(self, newPrice):
        self.price = newPrice

    #GETTERS E SETTERS DE EX-DATE
    def get_exdate(self) -> str:
        return self.ex_date

    def set_exdate(self, newExdate):
        self.ex_date = newExdate

    #GETTERS E SETTERS DE WEIGHT
    def get_weight(self):
        return self.weight

    def set_weight(self, newWeight):
        self.weight = newWeight

    #GETTERS E SETTERS DE DESC
    def get_desc(self):
        return self.description

    def set_desc(self, newDesc):
        self.description = newDesc


class Purchase:
    def __init__(self):
        pass

    def shop(self, item: Product):
        buy = []
        buy.append(item)

        for i in buy:
            print(f'Item comprado: {item.name}\t\t')
            print(f'\t\tPreço: {item.price}')

        quantidade = int(input("Digite a quantidade do produto: "))
        total = item.price * quantidade
        print(f'Total: {total}')
    
        
             




        

p1 = Product('Sadia','tomate', 1.99, '06/2022', 220,1, 'Tomate orgânico')
p2 = Product('Seara','Lasanha', 12.99, '06/2022', 220,1, 'Lasanha pre-pronta')
p3 = Product('Perdigão','Linguiça', 18.99, '06/2022', 220,1, 'Linguiça toscana levemente apimentada')
p4 = Product('Bordon','Feijoada', 4.99, '06/2022', 220,1, 'Feijoada Baiana caseira')
p5 = Product('Fortaleza','Bolacha', 2.99, '06/2022', 220,1, 'Cream cracker agua e sal')


compra = Purchase()
compra.shop(p1)
compra.shop(p2)
compra.shop(p3)
compra.shop(p4)
compra.shop(p5)
     
        
        

    



