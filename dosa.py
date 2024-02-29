import json
import sys

class Dosa:
    """This class take json file and seperate customer name and
       phone number to customers.json file and items name, price
       and total order to items.json"""
    def __init__(self,filename):
        self.file = filename
        with open(filename, "r") as f:
            self.data = json.load(f)

    def get_customer_data(self):
        """Get customer name and phone number from file"""
        customers = {} 
        for data in self.data:
            phone_number = data['phone']
            customer_name = data['name']
            customers[phone_number] = customer_name
        return customers

    def get_item_list(self):
        """Get Items name, Price, and Total order From file"""
        items = {}
        for data in self.data:
            data_items = data['items']
            for item in data_items:
                item_name = item.get('name')
                item_price = item.get('price')

                if item_name not in items:
                    items[item_name] = {'price': item_price, 'orders': 1}
                else:
                    items[item_name]['price'] = item_price
                    items[item_name]['orders'] += 1
        return items
    
    def dump_customer_list(self):
        """dump customer names and their phone numbers in json file"""
        customer_list = self.get_customer_data()
        with open("customers.json", "w") as f:
            f.write(json.dumps(customer_list))
            
    def dump_item_list(self):
        """dump items name, price and total order in json file"""
        item_list = self.get_item_list()
        with  open("items.json", "w") as f:
            f.write(json.dumps(item_list))

if __name__ == "__main__":
    input_file = sys.argv[1]
    dosa = Dosa(input_file)
    print(dosa.dump_customer_list())
    print(dosa.dump_item_list())
