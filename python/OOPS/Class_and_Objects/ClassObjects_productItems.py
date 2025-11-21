class Product:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price
class User:
    def __init__(self):
        self.products=[]
    def addproducts(self,id,name,price):
        p = Product(id,name,price)
        self.products.append(p)
    def showproducts(self):
        print("------------Products-----------------")
        for product in self.products:
            print(f"{product.id} {product.name} {product.price}")
    def deleteproduct(self,id):
        is_found=False
        for product in self.products:
            if product.id==id:
                self.products.remove(product)
                is_found=True
                break
        if is_found==False:
            print("Item is not found")
        else:
            print("id: "+str(id)+ " is removed successfully!")
    def update(self,id,name,price):
        for product in self.products:
            if product.id==id:
                product.name=name
                product.price=price 
                

user= User()
user.addproducts(1,"laptop",65000)
user.addproducts(2,"watch",2000)
user.addproducts(3,"bike",75000)
user.addproducts(4,"suite",5000)
user.showproducts()
user.deleteproduct(6)
user.showproducts()
user.update(1,"mobile",50000)
user.deleteproduct(4)



"""
------------Products-----------------
1 laptop 65000
2 watch 2000
3 bike 75000
4 suite 5000
Item is not found
------------Products-----------------
1 laptop 65000
2 watch 2000
3 bike 75000
4 suite 5000
id: 4 is removed successfully!

=== Code Execution Successful ===
"""