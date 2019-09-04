from store import Store

Supermart = Store()
Supermart.add_product('apple', 0.60, 'produce').add_product('orange', 0.90, 'produce')
Supermart.sell_product(0).product_info('apple')
Supermart.add_product('banana', .32, 'produce')
Supermart.change_price('orange', 0.02, True)
Supermart.product_info('orange')
Supermart.inflation('orange', 0.2)
Supermart.product_info('orange')
Supermart.set_clearence('produce', 0.2)
Supermart.product_info('orange')
Supermart.product_info('banana')

