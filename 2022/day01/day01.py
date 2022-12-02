with open("day01_data.txt") as f:
    lines = f.readlines()

    current_total = 0
    elf_totals = []

    for line in lines:
        if line.strip() == "":
            elf_totals.append(current_total)
            current_total = 0
        else:
            item_calories = int(line.strip())
            current_total += item_calories

    else:
        if current_total > 0:
            elf_totals.append(current_total)

    # sort the list in descending order
    elf_totals.sort()
    print(f" Top Elf - Total Calories: {max(elf_totals)}")
    print(f" Top Three Elves - Total Calories: {sum(elf_totals[-3:])}")
