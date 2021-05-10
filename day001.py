NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]

PY_CONTENT_CREATORS = [
    "brian okken",
    "michael kennedy",
    "trey hunner",
    "matt harrison",
    "julian sequeira",
    "dan bader",
    "michael kennedy",
    "brian okken",
    "dan bader",
]


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
    each name appears only once"""
    NEWNAMES = []

    for i in names:
        if i.title() not in NEWNAMES:
            NEWNAMES.append(i.title())

    return NEWNAMES


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)

    res = []

    res.append(sorted(names, key=lambda x: x.split(" ")[-1]))
    res = res[0]
    res.reverse()

    return res


def shortest_first_name(names):
    """Returns the shortest first name (str).
    You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    firstnames = []

    for name in names:
        firstnames.append(name.split(" ")[0])

    res = min((word for word in firstnames if word), key=len)

    return res


print(shortest_first_name(NAMES))
