#  # Tresure Map
row1 = ["🥱", "🥱", "🥱"]
row2 = ["🥱", "🥱", "🥱"]
row3 = ["🥱", "🥱", "🥱"]
print(f"{row1}\n{row2}\n{row3}")

map = [row1, row2, row3]
position = input("Where do you want to put the tresure? ")
horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal-1] = "😎"

print(f"{row1}\n{row2}\n{row3}")
