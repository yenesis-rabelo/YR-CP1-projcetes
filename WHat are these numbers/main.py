#Yenesis Rabelo What are these numberd


#get users input as a number
user_input = float (input("Enter a number:"))


#format the number as an integer  with comma
integer_format = f"{int(user_input):,}"
print(f"As an integer with commas: {integer_format}")


#format the number as a float with 4 decimal places
float_format = f"{user_input:.4f}"
print(f"As a float with 4 decimal places: {float_format}")


#formating the number as a percentage 
percentage_format = f"{user_input:.2%}"
print(f"As a percentage: {percentage_format}")


#formating the number as a dollar sign 
dollar_format = f"${user_input:,.2f}"
print(f"As a dollar amount: {dollar_format}")