class ItemToPurchase:
  
    def __init__(self):
        
        self.item_name=None
        self.item_price=0.0
        self.item_quantity=0
      
    
    def print_item_cost(self):
        print(self.item_name+" "+str(self.item_quantity)+' @ $'+str(self.item_price)+' = $'+str(self.item_price*self.item_quantity))
        return self.item_price*self.item_quantity
      
 
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
