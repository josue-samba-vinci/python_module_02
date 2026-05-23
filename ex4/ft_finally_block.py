class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass

def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else
        raise Plant 



if __name__ == "__main__":
    print("=== Garden Watering System ===")

    print()



    print("Cleanup always happens, even with errors!")
