from party import most_and_least_common_type

treats = [
     {'type': 'dessert'},
     {'type': 'dessert'},
     {'type': 'appetizer'},
     {'type': 'dessert'},
     {'type': 'appetizer'},
     {'type': 'drink'},
]

most_and_least_common_type(treats)



# Single item in list
treats = [
     {'type': 'drink'},
]

most_and_least_common_type(treats)


# Tie for most
treats = [
     {'type': 'dessert'},
     {'type': 'dessert'},
     {'type': 'appetizer'},
     {'type': 'appetizer'},
     {'type': 'drink'},
]

most_and_least_common_type(treats)



# Tie for least
treats = [
     {'type': 'dessert'},
     {'type': 'dessert'},
     {'type': 'appetizer'},
     {'type': 'dessert'},
     {'type': 'appetizer'},
     {'type': 'drink'},
     {'type': 'chips'},
]

most_and_least_common_type(treats)




# Empty list
treats = []

most_and_least_common_type(treats)

