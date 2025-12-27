def ft_count_harvest_recursive(day=1, deadline=None):
    if deadline is None:
        deadline = int(input("Days until harvest: "))
    print(f"Day {day}")
    if day == deadline:
        print("Harvest time!")
    else:
        ft_count_harvest_recursive(day + 1, deadline)
