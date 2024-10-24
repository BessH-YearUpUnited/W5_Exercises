list1 = [1,2,3,'banana', (5,6)]
tuple1 = (1,2,3, 3, 3)
set1 = {3,5,9}

dict1 = {
    'orderID': 1234,
    'prod_name': ['overalls', 'shirt', 'socks'],
    'customerID': 'BILBO',
    'qty': 4,
    'price':79.99,
    'notes': list1}

dict2 = {
    'orderID': 6789,
    'prod_name': 'staff',
    'customerID': 'GANDD',
    'qty': 1,
    'price':159.99

}

dict1.update({'discount':.15})
dict2.pop('orderID')
dict2.popitem()
dict2['prod_name'] = 'wizard staff'

del dict2['qty']

#dict1['customerID'] = 'GANDD'
# print(dict1['customerID'], dict1['discount'])
print(dict1)
