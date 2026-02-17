#Bloque try - except
try:
    age = int(input("Enter your age: "))
    print(f"Your age is: {age}")
except ValueError:
    print("Error: Please enter a valid number.")

# Capturar múltiples excepciones
try:
    a = int(input("Enter a number: "))
    result = 100 / a
    print(f"Result: {result}")
except ValueError:
    print("Error: That is not a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

#Capturar el mensaje del error con as
try:
    numbers = [10, 20, 30]
    print(numbers[10])
except IndexError as e:
    print(f"Error caught: {e}")
# Output: Error caught: list index out of range

#Bloque else
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input.")
else:
    print(f"You entered: {number}")


#Bloque finally
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Process finished.")


#Estructura completa try - except - else - finally
try:
    price = float(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))
    total = price * quantity
except ValueError:
    print("Error: Please enter valid numbers.")
else:
    print(f"Total: ${total:.2f}")
finally:
    print("Transaction completed.")