menu_item_not_found = {
    'menu_id': 200,
    'quantity': 2
}

order_strings = {
    'menu_id': "200",
    'quantity': "2"
}

incomplete_order = {
    'menu_id': 4
}


def create_order(menu_id):
    order = {
        'menu_id': menu_id,
        'quantity': 3
    }
    return order
