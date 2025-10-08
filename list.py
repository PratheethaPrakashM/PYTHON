items = []
print("Enter the items to be added in inventory\n")
while True:
    item = input()
    
    if item.lower() == 'done':
        break

    name, quantity, price = [i.strip() for i in item.split(',')]
    
    dict = {
        'name': name,
        'quantity': int(quantity),
        'price': float(price)
    }
    
    items.append(dict)

print(items)
total=0
for i in items:
    print(f"{i['name']}={i['quantity']*i['price']}rs")
    total+=i['quantity']
print("Total quantity=",total)
search=input("Enter the item to search\n")
for i in items:
    if search.lower()==i['name'].lower():
        print(i)
items_out=[]
print("Enter the item name and quantity sold\n")
while True:
    sold_items=input()
    if sold_items.lower() == 'done':
        break
    n, q = [i.strip() for i in sold_items.split(',')]
    for i in items:
        if n.lower() == i['name'].lower():
            if int(q)<=i['quantity']:
                i['quantity']-=int(q)
            else:
                print("Insufficient quantity\n")
        
        if i['quantity']==0:
            items_out.append(i['name'])

print("Upated Inventory: ",items)    
print("Items out of stock: ",items_out)
