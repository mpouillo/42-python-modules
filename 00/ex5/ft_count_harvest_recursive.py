def ft_count_harvest_recursive(day: int = 1, deadline: int = 0) -> None:
    if deadline == 0:
        deadline = int(input("Days until harvest: "))
    print(f"Day {day}")
    if day == deadline or deadline < 1:
        print("Harvest time!")
    else:
        ft_count_harvest_recursive(day + 1, deadline)
