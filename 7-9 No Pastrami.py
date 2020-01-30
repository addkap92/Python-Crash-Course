sandwhich_orders = ['turkey','pastrami', 'ham','pastrami', 'italian', 'pastrami']
finished_sandwhiches = []
print("The deli has run out of pastrami!")
while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')
while sandwhich_orders:
    current_sandwhich = sandwhich_orders.pop()
    print("We got your order for the " + current_sandwhich + " sandwhich. We are making it now!")
    finished_sandwhiches.append(current_sandwhich)
print("\nWe finished your order! The following sandwhiches were made:")
for sandwhich in finished_sandwhiches:
    print(sandwhich.title())