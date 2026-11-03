correct_otp = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:

    otp = input("Enter OTP: ")

    if otp == "":
        print("Blank entry. Try again.")
        continue

    attempts += 1

    if otp == correct_otp:
        print("OTP verified successfully")
        break

    else:
        print("Incorrect OTP")

else:
    print("Account locked for 30 minutes")