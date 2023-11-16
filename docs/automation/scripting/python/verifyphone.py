phone = input("Enter Phone Number: ")
if phone[:3] == "+91" and len(phone) == 13:
    print("phone",phone, "is valid")
else:
    print("Phone",phone,"phone is not valid")
