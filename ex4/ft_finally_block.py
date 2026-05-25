class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    plants_valid = (["Tomato", "Letucce", "Carrots"])
    plants_invalid = (["Tomato", "letucce", "Carrots"])
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    test_watering_system(plants_valid)
    print()
    print("Testing invalid plants...")
    test_watering_system(plants_invalid)
    print()
    print("Cleanup always happens, even with errors!")
