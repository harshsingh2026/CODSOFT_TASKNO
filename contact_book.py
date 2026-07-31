# ==============================
# Contact Book Application
# ==============================

contacts = {}

while True:
    print("\n" + "=" * 40)
    print("         CONTACT BOOK")
    print("=" * 40)
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    # ----------------------------
    # Add Contact
    # ----------------------------
    if choice == "1":
        name = input("Enter Name: ").strip()

        if name in contacts:
            print("Contact already exists!")
            continue

        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email: ").strip()
        address = input("Enter Address: ").strip()

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact Added Successfully!")

    # ----------------------------
    # View Contacts
    # ----------------------------
    elif choice == "2":

        if not contacts:
            print("No contacts found.")
        else:
            print("\n" + "-" * 60)
            print("{:<20} {:<15}".format("NAME", "PHONE"))
            print("-" * 60)

            for name, details in contacts.items():
                print("{:<20} {:<15}".format(name, details["Phone"]))

    # ----------------------------
    # Search Contact
    # ----------------------------
    elif choice == "3":

        search = input("Enter Name or Phone Number: ").strip()

        found = False

        for name, details in contacts.items():

            if search.lower() == name.lower() or search == details["Phone"]:

                print("\nContact Found")
                print("-" * 30)
                print("Name    :", name)
                print("Phone   :", details["Phone"])
                print("Email   :", details["Email"])
                print("Address :", details["Address"])

                found = True
                break

        if not found:
            print("Contact Not Found!")

    # ----------------------------
    # Update Contact
    # ----------------------------
    elif choice == "4":

        name = input("Enter Contact Name to Update: ").strip()

        if name in contacts:

            print("Leave blank if you don't want to change a field.\n")

            phone = input("New Phone: ")
            email = input("New Email: ")
            address = input("New Address: ")

            if phone:
                contacts[name]["Phone"] = phone

            if email:
                contacts[name]["Email"] = email

            if address:
                contacts[name]["Address"] = address

            print("Contact Updated Successfully!")

        else:
            print("Contact Not Found!")

    # ----------------------------
    # Delete Contact
    # ----------------------------
    elif choice == "5":

        name = input("Enter Contact Name to Delete: ").strip()

        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    # ----------------------------
    # Exit
    # ----------------------------
    elif choice == "6":
        print("Thank you for using Contact Book.")
        break

    # ----------------------------
    # Invalid Choice
    # ----------------------------
    else:
        print("Invalid Choice! Please enter 1-6.")