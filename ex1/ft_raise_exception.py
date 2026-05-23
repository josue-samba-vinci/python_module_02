def input_temperature(temp_str: str) -> int:
    if int(temp_str) > 40:
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    if int(temp_str) < 0:
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")
    return int(temp_str)


def test_temperature() -> None:
    try:
        print("Input data is '25'")
        temp = input_temperature("25")
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print()

    try:
        print("Input data is 'abc'")
        temp = input_temperature("abc")
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print()

    try:
        print("Input data is '100'")
        temp = input_temperature("100")
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print()

    try:
        print("Input data is '-50'")
        temp = input_temperature("-50")
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()