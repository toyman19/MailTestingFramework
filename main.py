#Print Menu
menu = ["Set Envelope Sender (req)","Set Envelope Recipient (req)", "Set Sender", "Set Subject", "Add Body","Add Attachment", "Send", "Quit"]

while quit!=1:

#User selection
    while True:
        print("Mail sending motherfucker\n\nMenu:")
        for iteration, item in enumerate(menu):
            print(str(iteration+1)+". "+item)

        wybor = int(input("\nWhich option to choose?:\n"))
        if wybor == 1:
            mailfrom = input("Please enter a sender: ")
            print(f"OK - Setting envelope sender as {mailfrom}\n")
        if wybor == 2:
            rcptto = input("Please enter a recipient: ")
        if wybor == 3:
            fromh = input("Please enter the from header: ")
        if wybor == 4:
            subject = input("Please enter email subject: ")
        if wybor == 5:
            body_option = input("Please choose an option: "
                "\n1. Write body"
                "\n2. Load template")
            if body_option == 1:
                body = input("Please enter e-mail body")
            elif body_option == 2:
                body_template = input("Please choose a template: "
                    "\n1. SPAM"
                    "\n2. Malware")
                if body_template == 1:
                    body = "Do you need some viagra?"
                if body_template == 2:
                    body = "I am bad bad email"
        if wybor == 6:
            break
        if wybor == 7:
            break
        if wybor == 8:
            quit = 1
            print("See you later wally-gator!")
            break
