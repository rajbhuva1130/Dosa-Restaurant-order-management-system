import json

class Dosa:
    def __init__(self,filename):
        self.file = filename
        with open(filename, "r") as f:
            self.data = json.load(f)
            
        customers = {}
        items = {}
        
        for data in self.data:
            phone_number = data['phone']
            customer_name = data['name']
            
            customers[phone_number] = customer_name
            
            # item_name = data['item'].get('name')
            # item_price = data['item'].get('price')
            
            # if item_name  not in items:
            #     items[item_name] = {'price': item_price, 'orders': 1}
            
            # else:
            #     quantity = items[item_name]['orders'] + 1
            #     items[item_name]['orders'] = quantity
                
        print("customer:",customers)
        # print('items',items)
            
            
if __name__ == "__main__":
    import sys

    input_file = sys.argv[1]
    Dosa(input_file)   
