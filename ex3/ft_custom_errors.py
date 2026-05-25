class GardenError(Exception):
    def __init__(self, garden_error: str = "Unknown garden error"):
        super().__init__(garden_error)


class PlantError(GardenError):
    def __init__(self, plant_error: str = "Unknown plant error"):
        super().__init__(plant_error)


class WaterError(GardenError):
    def __init__(self, water_error: str = "Unknown water error"):
        super().__init__(water_error)


def plant_wilting(plant_name: str, wilting: bool = False) -> None:
    if wilting is True:
        raise PlantError(f"The {plant_name} is wilting!")


def water_left(tank_level: int) -> None:
    if tank_level <= 0:
        raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    print()

    try:
        print("Testing PlantError...")
        plant_wilting("tomato", True)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print()

    try:
        print("Testing WaterError...")
        water_left(0)
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print()

    try:
        print("Testing catching all garden errors...")
        plant_wilting("tomato", True)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        water_left(0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print()

    print("All custom error types work correctly!")
