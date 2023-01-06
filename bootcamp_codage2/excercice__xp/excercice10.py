sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches=[]
res=finished_sandwiches.insert(1, sandwich_orders.pop(sandwich_orders.index("Tuna sandwich")))
res=finished_sandwiches.insert(2, sandwich_orders.pop(sandwich_orders.index("Avocado sandwich")))
res=finished_sandwiches.insert(5, sandwich_orders.pop(sandwich_orders.index("Egg sandwich")))
res=finished_sandwiches.insert(4, sandwich_orders.pop(sandwich_orders.index("Sabih sandwich")))
res=finished_sandwiches.insert(3, sandwich_orders.pop(sandwich_orders.index("Pastrami sandwich")))
print(finished_sandwiches)
print("I made your tuna sandwich.")