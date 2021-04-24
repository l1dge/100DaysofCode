cars = {
    "Ford": ["Falcon", "Focus", "Festiva", "Fairlane"],
    "Holden": ["Commodore", "Captiva", "Barina", "Trailblazer"],
    "Nissan": ["Maxima", "Pulsar", "350Z", "Navara"],
    "Honda": ["Civic", "Accord", "Odyssey", "Jazz"],
    "Jeep": ["Grand Cherokee", "Cherokee", "Trailhawk", "Trackhawk"],
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
    (original order)"""
    for make, cars in cars.items():
        if make == "Jeep":
            Jeeps = [car for car in cars]
    res = ""
    z = 0

    for i in Jeeps:
        tot = len(Jeeps)
        if z <= tot - 2:
            res += i + ", "
            z += 1
        else:
            res += i

    return res


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    res = []
    for make, cars in cars.items():
        res.append(cars[0])

    print(res)


def get_all_matching_models(cars=cars, grep="trail"):
    """return a list of all models containing the case insensitive
    'grep' string which defaults to 'trail' for this exercise,
    sort the resulting sequence alphabetically"""
    res = []
    for make, car in cars.items():
        res.extend([i for i in car if grep.lower() in i.lower()])

    print(sorted(res))


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
    sorted alphabetically"""
    carsort = {}
    for make, car in cars.items():
        carsort = {make: sorted(car)}
        cars.update(carsort)

    print(cars)


get_all_jeeps(cars)
get_first_model_each_manufacturer(cars)
get_all_matching_models(cars=cars, grep="CO")
sort_car_models(cars)