class ItemToPurchase:
  
    def __init__(self):
        
        self.item_name=None
        self.item_price=0
        self.item_quantity=0
        self.item_description=None
    
    def print_item_cost(self):
        print(self.item_name+" "+str(self.item_quantity)+' @ $'+str(self.item_price)+' = $'+str(self.item_price*self.item_quantity))
        return self.item_price*self.item_quantity

    def print_item_description(self):
        string = '{}: {}'.format(self.item_name, self.item_description)
        print(string, end='\n')
        return string

class ShoppingCart:
    def __init__(self):
        self.customer.name=None
        self.current_date='January 1, 2016'
        self.cart_items=[]

    def add_item(self, string):
        print('\nADD ITEM TO CART', end='\n')
        item_name = str(input('Enter the item name: '))
        item_description = str(input('\nEnter the item description: '))
        item_price = int(input('\nEnter the item price: '))
        item_quantity = int(input('\nEnter the item quantity: '))
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

    def remove_item(self):
        print('\nREMOVE ITEM FROM CART', end='\n')
        string = str(input('Enter name of item to remove: '))
        i = 0
        for item in self.cart_items:
            if(item.item_name == string):               
                del self.cart_items[i]
                i += 1
                
                flag=True
                
                break

            else:

                flag=False

        if(flag==False):
            print('Item not found in cart. Nothing removed')

    def modify_item(self):
        print('\nCHANGE ITEM QUANTITY', end='\n')
        name = str(input('Enter the item name: '))       
        for item in self.cart_items:
            if(item.item_name == name):
                quantity = int(input('Enter the new quantity: '))
                item.item_quantity = quantity
                flag=True

                break

            else:

                flag=False

        if(flag==False):
            print('Item not found in cart. Nothing modified')

    def get_num_items_in_cart(self):
        num_items=0
        for item in self.cart_items:
            num_items= num_items+item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0
        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)
            total_cost += cost
        return total_cost

    def print_total():
        total_cost = get_cost_of_cart()
        if (total_cost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            output_cart()

    def print_descriptions(self):
        print('\nOUTPUT ITEMS\' DESCRIPTIONS')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date),end='\n')
        print('\nItem Descriptions', end='\n')
        for item in self.cart_items:
            print('{}: {}'.format(item.item_name, item.item_description), end='\n')
 
if __name__ == "__main__":
  
 
    item1=ItemToPurchase()
    item2=ItemToPurchase()
  

    item1.item_name=input('Item 1\nEnter the item name:\n')
    item1.item_price=int(input('Enter the item price:\n'))
    item1.item_quantity=int(input('Enter the item quantity:\n'))
  

    
    item2.item_name=input('\nItem 2\nEnter the item name:\n')
    item2.item_price=int(input('Enter the item price:\n'))
    item2.item_quantity=int(input('Enter the item quantity:\n'))
  
   
    print('\nTOTAL COST')
    value1=item1.print_item_cost()
    value2=item2.print_item_cost()
    print('\nTotal: $'+str(value1+value2))
