from operator import contains
from models import *
from populate_db import *

# Do not modify these lines
__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"


def search(term) -> list:
    products = []
    term = term.lower()

    query = (
        Product.select().where(
        fn.LOWER(Product.name).contains(term) or fn.LOWER(Product.description).contains(term)
        )
    )
    products = [product for product in query]
    if not products:
        print(f'{term} was not found in database.')
    return products

def list_user_products(user_id) -> list:
    user_products = []
    query = (Product.select()
            .where(Product.owner_id == user_id))
    user_products = [product for product in query]
    if not user_products:
        print(f'No products found for {user_id}')
    return user_products


def list_products_per_tag(tag):
    tag_products = []
    query = (Product.select()
             .join(Tags, on=(Product.id == Tags.id))
             .where(fn.LOWER(Product.name).contains(fn.LOWER(tag))))
    tag_products = [product.name for product in query]
    if not tag_products:
        print(f'No products found under tag {tag}.')
    return tag_products



def add_product_to_user(user_id, product):
    try:
        user = User.get_by_id(user_id)
    except DoesNotExist:
        return f'Invalid user input.'
    product.owner = user
    product.save()
    return f'{user.name} successfully added {product.name} to the catalog.'


def update_stock(product_id, new_quantity):
    try:
        product = Product.get_by_id(product_id)
    except DoesNotExist:
        return f'Product id not found in database.'
    product.qty_in_stock = new_quantity
    product.save()
    return f'Amount of {product_id} (product_id) updated to: {new_quantity}'

def purchase_product(product_id, buyer_id, quantity):
    try:
        product = Product.get_by_id(product_id)
    except DoesNotExist:
        return f'Product does not exist.'
    if quantity > product.qty_in_stock:
        return f'Currently not enough in stock.'
    try:
        buyer = User.get_by_id(buyer_id)
    except DoesNotExist:
        return f'User not found in database.'
    product.qty_in_stock -= quantity
    product.save()

    transaction = Transaction()
    transaction.product = product
    transaction.buyer = buyer
    transaction.price_per_unit = product.price_per_unit
    transaction.qty_sold = quantity
    transaction.save()
    tot_price = transaction.price_per_unit * transaction.qty_sold
    return f'{quantity} of {product.name} for a total of €{tot_price} sold to {buyer.name}'

def remove_product(product_id):
    try:
        product = Product.get_by_id(product_id)
    except DoesNotExist:
        return 'Product id not found in database.'
    product.delete()
    return f'Product with following id {product_id} has been successfully removed'

if __name__ == "__main__":
    pass