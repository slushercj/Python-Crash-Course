def make_car(manufacturer, model, **args):
    """Makes a car"""
    args['manufacturer'] = manufacturer
    args['model'] = model

    return args

car = make_car('RAM', '1500', trim='limited', color='black')

print(car)