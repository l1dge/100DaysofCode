names = "Julian Bob PyBites Dante Martin Rodolfo".split()
countries = "Australia Spain Global Argentina USA Mexico".split()


def enumerate_names_countries():
    """Outputs:
    1. Julian     Australia
    2. Bob        Spain
    3. PyBites    Global
    4. Dante      Argentina
    5. Martin     USA
    6. Rodolfo    Mexico"""
    for count, (name, country) in enumerate(zip(names, countries), start=1):
        print("{:<1d}. {:<11}{:<15}".format(count, name, country))


enumerate_names_countries()