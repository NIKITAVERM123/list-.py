print("*welcome To ATM*")
# print(b)
card=input("incert your card")
if card=="debit card":
    print(" move next")
    lan=input("select your language : ")
    if lan=="english":
        print("next")
        pin=int(input("enter your pin number : "))
        if pin==1234 or 3636 or 5342 or 6526 :
            print("next")
            tt=input("type of transaction")
            if tt=="withdrawl":
                print(" go to next")
                account=input("select your account")
                if account=="saving" or account=="demate":
                    print("next")
                    amount=int(input("enter ammount"))
                    if amount>=100 and amount<=40000:
                        print("transaction has been procide")
                        a="thankyou for using"
                        print(a)
                    else:
                        print("Not have cash")
                else:
                    print("you didn't have another account")

            else:
                print("choose your type")
        else:
            ("pin incorrect")
    else:
        print("enter your language")
else:
    print("your card has been re")