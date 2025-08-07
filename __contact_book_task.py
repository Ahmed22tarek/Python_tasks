contacts = {
    "Ahmed": "010",
    "Sara": "011",
    "Omar": "012"
}

print("Contact Names:")
for name in contacts.keys():
    print(f"{name}")

search_name = input("\nEnter a name to search for their phone number: ")

if search_name in contacts:
    print(f"{search_name}'s phone number is: {contacts[search_name]}")
else:
    print(f"Sorry, {search_name} is not in the contact book.")