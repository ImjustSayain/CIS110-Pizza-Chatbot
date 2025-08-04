print("Hello, my name is Alex your virtual assistant. I will help you order a pizza")
print("I'm going to get our order started i just need to ask a few questions first. After typing a response, press enter.")
userName = input("\nEnter your name:  ")
if userName.lower() == "keyshawn reed":
    print(f"\nMy creator, {userName}. Pleasure to serve you!")
else:
    print(f"\nHello, {userName}. Nice to meet you!")
size = input("\nWhat size do you want? Enter small medium or large:  ")
flavor = input("\nEnter the flavor of pizza:  ")
crustType = input("\What type of crust do you want  ")
quantity = input("\nHow many of these do you want to order? Enter a numeric value:  ")
quantity = int(quantity)
method = input("\nIs this carry out or delivery:  ")

if method.lower() == "delivery":
   deliveryFee = 5
else:
    deliveryFee = 0

salesTax = 1.1
if size.lower() == "small":
   pizzaCost = 8.99
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large":
     pizzaCost= 17.99

total = (pizzaCost * quantity) * salesTax
print("-" * 10)
print(f"Thank you, {userName}, for your order")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust cost ${total:,.2f}.")

if total >= 50:
    print("\nCongratulations! You've been awarded a $10 Off coupon for your next order")
else:
    print("n\Order over $50 will recieve a free $10 Off coupon")

print("-" * 10)