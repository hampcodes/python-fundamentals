# For: para iterables, cuando sabemos cuanda terminará
# While: Cuando no sabemos cuando terminará y necesitamos una condición

my_list = [1, 2, 3, 4, 5]

print("=== FOR Example ===")
for item in my_list:
    print(item)


print("\n=== WHILE Example ===")

number = 0

while number <= 0:
    number = float(input("Enter a positive number: "))

print(f"Valid number entered: {number}")