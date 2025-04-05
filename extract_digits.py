string = input("Enter the string containing numbers: ")
digits = [charac for charac in string if charac.isdigit()]
print("Extracted digits:", ' '.join(digits))



#OR
#string = input("Enter the string containing numbers: ")
#digits = []
#for character in string:
#    if character.isdigit():
#        digits.append(character)
#print("Extracted digits:", ' '.join(digits))



#OR
#string = input("enter the string containing numbers : ")
#for charac in string:
#   if charac.isdigit():
#        print(charac)
