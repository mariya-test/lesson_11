from smartphone import Smartphone

catalog = [
    Smartphone("samsung", "galaxy", 89005432215),
    Smartphone("samsung", "galaxy", 89005432214),
    Smartphone("samsung", "galaxy", 89005432213),
    Smartphone("samsung", "f6", 89005432212),
    Smartphone("nokia",  "x4", 89005432211)
]

for smartphone in catalog:
    print(f"{smartphone.marka} - {smartphone.model}. {smartphone.number}")
