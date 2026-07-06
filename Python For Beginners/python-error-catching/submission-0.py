def divide_numbers(a: str, b: str) -> None:
    try:
        val1 = int(a);
        val2 = int(b)
        print(val1/val2)
    except Exception as error:
        print(f"An error occurred: {error}")



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
