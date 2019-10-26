cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    return ', '.join(cars["Jeep"])


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [manufacturer[0] for manufacturer in cars.values()]


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    return [model for manufacturer in cars.values() for model in manufacturer if grep.lower() in model.lower()]


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    new_cars = {}
    for manufacturer, models in cars.items():
        new_cars[manufacturer] = sorted(models)
    return new_cars

"""
print(get_all_jeeps(cars))
print(get_first_model_each_manufacturer(cars))
print(get_all_matching_models(cars))
print(sort_car_models(cars))
"""

