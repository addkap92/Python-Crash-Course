def build_car(manufacturer, model, **other):
    car_profile = {}
    car_profile['Manufacturer'] = manufacturer.title()
    car_profile['Model'] = model.title()

    for key, value in other.items():
        car_profile[key.title()] = value.title()
    return car_profile

new_car = build_car('subaru', 'forester', color='blue', seats='leather')
print(new_car)