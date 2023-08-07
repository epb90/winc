from models import *

# List of user details
user_details = [
    {'name': 'Alice', 'address': '123 Main St, City, Country', 'billing': '123 Main St, City, Country'},
    {'name': 'Bob', 'address': '456 Park Ave, Town, Country', 'billing': '456 Park Ave, Town, Country'},
    {'name': 'Eva', 'address': '789 Lane Rd, Village, Country', 'billing': '789 Lane Rd, Village, Country'},
    {'name': 'Max', 'address': '10th Ave, Suburb, Country', 'billing': '10th Ave, Suburb, Country'},
    {'name': 'Sophia', 'address': '56 Crescent St, Urban, Country', 'billing': '56 Crescent St, Urban, Country'},
    {'name': 'Liam', 'address': '90 Elm St, Downtown, Country', 'billing': '90 Elm St, Downtown, Country'},
    {'name': 'Olivia', 'address': '34 Maple Rd, Beach, Country', 'billing': '34 Maple Rd, Beach, Country'},
    {'name': 'Noah', 'address': '55 Oak Dr, Island, Country', 'billing': '55 Oak Dr, Island, Country'},
    {'name': 'Ava', 'address': '12 Pine Ln, Mountain, Country', 'billing': '12 Pine Ln, Mountain, Country'},
    {'name': 'William', 'address': '76 Hillside Ave, Valley, Country', 'billing': '76 Hillside Ave, Valley, Country'},
    {'name': 'Isabella', 'address': '31 River View, Canyon, Country', 'billing': '31 River View, Canyon, Country'},
    {'name': 'James', 'address': '22 Sunset Blvd, Prairie, Country', 'billing': '22 Sunset Blvd, Prairie, Country'},
    {'name': 'Sophie', 'address': '44 Sunrise Ave, Desert, Country', 'billing': '44 Sunrise Ave, Desert, Country'},
    {'name': 'Alexander', 'address': '25 Dusk Rd, Savanna, Country', 'billing': '25 Dusk Rd, Savanna, Country'},
    {'name': 'Emily', 'address': '15 Dawn St, Oasis, Country', 'billing': '15 Dawn St, Oasis, Country'}
]

# List of item tags
item_tags = [
    {'name': 'shoe'},
    {'name': 'trousers'},
    {'name': 'jeans'},
    {'name': 'sweater'},
    {'name': 'tshirt'},
    {'name': 'hoodie'},
    {'name': 'headwear'}
]

# List of color tags
color_tags = [
    {'name': 'red'},
    {'name': 'blue'},
    {'name': 'green'},
    {'name': 'yellow'},
    {'name': 'orange'},
    {'name': 'purple'},
    {'name': 'pink'},
    {'name': 'brown'},
    {'name': 'gray'},
    {'name': 'teal'},
    {'name': 'navy'},
    {'name': 'maroon'},
    {'name': 'black'},
    {'name': 'white'}
]

# List of size tags
size_tags = [
    {'name': 'XS'},
    {'name': 'S'},
    {'name': 'M'},
    {'name': 'L'},
    {'name': 'XL'},
    {'name': 'XXL'},
    {'name': '36'},
    {'name': '37'},
    {'name': '38'},
    {'name': '39'},
    {'name': '40'},
    {'name': '41'},
    {'name': '42'},
    {'name': '43'},
    {'name': '44'},
    {'name': '45'}
]

# List of products 

product_list = [
    {
        'name': 'Sneakers',
        'description': 'Comfortable sneakers for everyday use.',
        'price_per_unit': 50.0,
        'qty_in_stock': 100,
        'owner_id': 1,
        'tags': [item_tags[0]['name'], color_tags[12]['name']],
    },
    {
        'name': 'Denim Jeans',
        'description': 'Classic denim jeans for men.',
        'price_per_unit': 65.0,
        'qty_in_stock': 50,
        'owner_id': 3,
        'tags': [item_tags[2]['name'], item_tags[1]['name'], color_tags[1]['name']],
    },
]

def add_products(product_list):
    for product_info in product_list:
        tags = []
        for tag_name in product_info['tags']:
            try:
                tag = Tags.get(name=tag_name)
                tags.append(tag)
            except Tags.DoesNotExist:
                print(f"Tag '{tag_name}' not found in the database.")
        product = Product(
            name=product_info['name'],
            description=product_info['description'],
            price_per_unit=product_info['price_per_unit'],
            qty_in_stock=product_info['qty_in_stock'],
            owner_id=product_info['owner_id']
        )
        product.save()
        product.tags.add(tags)


# Function to add tags to the database
def add_tags(tags_list):
    for tag_info in tags_list:
        try:
            tag = Tags.get(name=tag_info['name'])
        except Tags.DoesNotExist:
            tag = Tags(**tag_info)
            tag.save()


# Function to add users to the database
def add_users():
    for user_info in user_details:
        try:
            user = User.get(User.name == user_info['name'])
        except DoesNotExist:
            user = User(**user_info)
            user.save()

def populate_database():
    add_users()
    add_tags(item_tags)
    add_tags(color_tags)
    add_tags(size_tags)
    add_products(product_list)