# # # # # even and odd number print

# # # # # num = int(input("Enter you number: "))

# # # # # if num % 2 == 0:
# # # # #     print(f"{num} is an even number")
# # # # # else:
# # # # #     print(f"{num} is an odd number")


# # # # # def is_even(num):
# # # # #     return num % 2 ==0


# # # # # checking number is  postive, negative or zero


# # # # while True:
# # # #     try:
# # # #         num1 = int(input("Enter you number : "))

# # # #         if num1 > 0:
# # # #             print(f"{num1} is an postive number")
# # # #         elif num1 < 0:
# # # #             print(f"{num1} is an negative")
# # # #         else:
# # # #             print("The number is Zero")

# # # #         break

# # # #     except ValueError:
# # # #         print(" Please enter a valid number.")


# # # # while True:
# # # #     try:
# # # #         first_number = int(input("Enter first number : "))
# # # #         second_number = int(input("Enter second number : "))

# # # #         if first_number > second_number:
# # # #             print(f"{first_number} is largest number.")
# # # #         elif second_number > nufirst_numberm1:
# # # #             print(f"{second_number} is largest number")
# # # #         else:
# # # #             print(f"Both numbers are equal")
# # # #         break
# # # #     except ValueError:
# # # #         print("Enter a valid whole number.")

# # # # while True:
# # # #     try:
# # # #         first_number = int(input("Enter first number : "))
# # # #         second_number = int(input("Enter second number : "))
# # # #         break

# # # #     except ValueError:
# # # #         print("Enter a valid whole number.")

# # # # if first_number > second_number:
# # # #     print(f"{first_number} is largest number.")
# # # # elif second_number > first_number:
# # # #     print(f"{second_number} is largest number")
# # # # else:
# # # #     print(f"Both numbers are equal")

# # # while True:
# # #     try:
# # #         student_marks = int(input("Enter marks obtained between 0 to 100 : "))

# # #         if 0 <= student_marks <= 100:
# # #             break
# # #         else:
# # #             print("Marks must between 0 and 100")

# # #     except ValueError:
# # #         print("Enter a valid whole number.")

# # # if student_marks >= 90:
# # #     grade = "A"
# # # elif student_marks >= 80:
# # #     grade = "B"
# # # elif student_marks >= 70:
# # #     grade = "C"
# # # elif student_marks >= 60:
# # #     grade = "D"
# # # else:
# # #     grade = "Fail"

# # # print(f"Marks : {student_marks}")
# # # print(f"Grade : {grade}")


# # # while True:
# # #     try:
# # #         num = int(input("Enter a number : "))
# # #         break
# # #     except ValueError:
# # #         print("Enter a valid whole number")

# # # for i in range(1, 11):
# # #     result = num * i
# # #     print(f"{num} x {i} = {result}")

# # # while True:
# # #     try:
# # #         num = int(input("Enter a positive number: "))

# # #         # Validate positive number here

# # #         break

# # #     except ValueError:
# # #         print("Enter a valid whole number.")

# # # total = 0

# # # for i in range(1, num + 1):

# # #     total = i + total

# # # # Update total here

# # # print(f"Sum = {total}").


# # word = input("Enter a word: ")

# # vowel_count = 0

# # for letter in word:

# #     if letter in "aeiou":
# #         vowel_count += 1

# # print(f"Total vowels: {vowel_count}")


# numbers = [12,22,56,452,654,3256]

# largest = max(numbers)

# print(f"Largest Number= {largest}")


numbers = [12, 22, 56, 452, 654, 3256]

smallest = min(numbers)

print(f"Smallest Number= {smallest}")
