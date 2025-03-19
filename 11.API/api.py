# import requests 

# # Get (URL) 

# # status kod
#     # om ok -> konvertera svar till json
#     # om ej ok -> error 
    
    
# # Get request för att hämta produkterna 
# response = requests.get('https://fakestoreapi.com/products')

# if response.status_code == 200:
#     products = response.json() # konvertera till json
#     print(f'all products: {products}')  # visa alla produkter
    
# else: 
#     print(f'error: fetching products. status code: {response.status_code}')


#....................................................................................................................................
# GET

# import requests 

# base_ur1 = 'https://fakestoreapi.com/products'

# response = requests.get(base_ur1)

# if response is None:
#     print(f'error: fetching products. status code:{response.status_code}')
    
# else:
#     products = response.json()
#     for product in products:
#         print(f'fetching product: {product}')
        
        
        
#  POST
# import requests

# base_ur1 = 'https://fakestoreapi.com/products'

# product_data = {
#     'name': product['new product'],
#     'price' : product['50000'],
#     'description': product['good product'],
#     'category' : 'clothes',
#     'stock_id' : 'jacket'    
    
# }

# response = requests.post(base_ur1)

# if response.status_code == 200:
#     print(f'product updated successfully')
#     print(response.json())
# else:
#     print(f'error updating product status code{response.status_code}')
    
    

# PUT

# import requests

# product_id = product[id]
# ur1 = 'https://fakestoreapi.com/products/{products_id}'

# updated_product = {
#     'name': 'updated product',
#     'price': '299',
#     'description': 'good product',
#     'category' : 'clothes',
#     'stock_id': 'jacket' 
# }

# response = requests.put(base_ur1)

# if response.status_code == 200:
#     print('product updated successfully')
#     print(response.json())
# else:
#     print(f'error updating product status code{response.status_code}')
    
    
# DELETE 

# import requests

# product_id = product[id]
# ur1 = 'https://fakestoreapi.com/products/{products_id}'

# response = requests.delete(ur1)

# if response.status_code == 200:
#     print('produc_id is now deleted succesfully')
# else:
#     print(f'error deleting product, status code: {response.status_code}')
    
    
#...........................................................................................................

import requests

base_ur1 = 'http://rickandmortapi.com/api/'

endpoint = 'character'

r = requests.get(base_ur1 + endpoint)



