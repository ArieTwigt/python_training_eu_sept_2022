
desired_amount = 1000
print(f"The desired amount is {desired_amount}")

donated_amount = 0

donations_list = [50, 450, 600, 100, 300, 40, 100, 500]

for donation in donations_list:
    
    print(f"Currently donated amount {donated_amount}")
    print(f"Adding {donation}")
    donated_amount += donation
    print(f"Total amount now is: {donated_amount}")

    if donated_amount > 1000:
        print("Thanks for the donations, we will proceed")
        break


print(f"Thanks for the donations: {donated_amount} ")
# keywords that can be used in loops
# - continue - Stop the current iteration of the loop, proceed ('continue') to the next
# - break - Stop ('break') the entire loop and proceed with the code
# - pass
