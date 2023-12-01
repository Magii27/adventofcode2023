import os
from pathlib import Path

print("###" + " CREATE DAY ".center(20, " ") + "###")
print("┌" + "—" * 69 + "┐")
print("│" + "<│ AdventOfCode 2023 │>".center(69) + "│")
print("│" + ("<│ CREATE DAY " + "│>").center(69) + "│", end="\n\n")
print("—" * 2 + " SET DAY " + "—" * 60)

day = input("> ")

data_filename = "Day" + str(day) + "Data.txt"
py_filename = "Day" + str(day)

txt_ex = True
py_ex = True

file_root = Path(__file__).parents[1]
print(file_root)
data_root = file_root / "DayData/"

if not os.path.exists(data_root / data_filename):
    txt_ex = False

    open(data_root / data_filename, 'w').close()

if not os.path.exists(file_root / (py_filename + ".py")):
    py_ex = False

    des_f = open(file_root / (py_filename + ".txt"), 'w')
    src_f = open(Path(__file__).parents[0] / "defaultpy.txt", 'r')

    for line in src_f:
        if "{day}" in line:
            line = line.replace("{day}", str(day))
        des_f.write(line)

    src_f.close()
    des_f.close()

    os.rename(file_root / (py_filename + ".txt"), file_root / (py_filename + ".py"))

print("\n" + "—" * 2 + " CREATED FILES " + "—" * 54)
if not txt_ex:
    print("> " + data_filename)
if not py_ex:
    print("> " + py_filename + ".py")

print("\n" + "—" * 2 + " INFORMATION " + "—" * 56)

if txt_ex:
    print("> " + data_filename + " already exists")
if py_ex:
    print("> " + py_filename + ".py" + " already exists")

print("> Program successfully completed")
print("—" * 71)
