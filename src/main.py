#from class_category import Category
#from class_product import Product
#from src.utils import load_data
#from pprint import pprint

#def main():
#    data = load_data()
#    list_category = []
#    for unit in data:
#        list_product = [un for un in unit["products"]]
#        category = Category(unit["name"], unit["description"], unit["products"])
#        list_category.append(f'{category.get_name()} \n'
#                             f'{category.get_description()} \n'
#                             f'{category.get_goods()} \n\n'
#                             )
#        result = []
#        for element in list_product:
#            product = Product(element["name"], element["description"],
#                              element["price"], element["quantity"])
#            list_category.append(f'{product.get_product_name()}\n'
#                          f'{product.new_price}\n'
#                          f'{product.get_product_quantity()}\n\n'
#                          )
#       pprint(list_category)
#if __name__ == '__main__':
#    main()