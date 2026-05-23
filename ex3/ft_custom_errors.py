class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, plant_error: str = "plant is wilting!"):
        super().__init__(plant_error)


class WaterError(GardenError):
    def __init__(self, water_error: str = "Not enough water in the tank!"):
        super().__init__(water_error)


def plant_wilting(wilting: bool = False) -> None:
    if wilting is True:
        raise PlantError()


def water_left(tank_level: int) -> None:
    if tank_level <= 0:
        raise WaterError()


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    print()

    plant = "tomato"
    try:
        print("Testing PlantError...")
        plant_wilting(True)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: The {plant}{e}")

    print()

    try:
        print("Testing WaterError...")
        water_left(0)
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print()

    try:
        print("Testing catching all garden errors...")
        plant_wilting(True)
    except GardenError as e:
        print(f"Caught {e.__class__.__name__}: The {plant} {e}")
    try:
        water_left(0)
    except GardenError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print()

    print("\nAll custom error types work correctly!")