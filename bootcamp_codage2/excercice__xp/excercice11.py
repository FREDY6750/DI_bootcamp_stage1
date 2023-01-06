sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
sandwich_orders.append("Pastrami sandwich")
sandwich_orders.append("Pastrami sandwich")
sandwich_orders.append("Pastrami sandwich")
print("desole nous n'avons plus de Pastrami sandwich")
i="Pastrami sandwich"
while i in sandwich_orders:
    sandwich_orders.remove(i)
print(sandwich_orders)