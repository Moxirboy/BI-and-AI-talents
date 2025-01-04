#Create a program to ask name and year of birth from user and tell them their age.
import datetime
# name=input("Please enter your name:")
# birth_year=int(input("Please enter your birth year: "))
# print(f"your age is {datetime.datetime.now().year-birth_year}")


print(f"{(name := input('Please enter your name: '))} your age is {datetime.datetime.now().year - int(input('Please enter your birth year: '))}")
