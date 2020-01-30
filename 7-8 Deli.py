sandwhich_orders = ['turkey', 'ham', 'italian']
finished_sandwhiches = []

while sandwhich_orders:
    current_sandwhich = sandwhich_orders.pop()

    print("We got your order for the " + current_sandwhich + " sandwhich. We are making it now!")
    finished_sandwhiches.append(current_sandwhich)
print("\nWe finished your order! The following sandwhiches were made:")
for sandwhich in finished_sandwhiches:
    print(sandwhich.title())