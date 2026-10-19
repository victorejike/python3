def status_code(code):
    match code:
        case 200:
            return "success"
        case 400 | 404:
            return "Client Error status codde failed"
        case _:
            return "unknown status"

def main():
    user_code = int(input("Enter a code ? "))

    # Pass the code into the function and capture the string result
    status_result = status_code(user_code)

    # FIXED: Typo corrected to match exactly what the function returns
    if status_result == "unknown status":
        print("Not found try again")
    else:
        # FIXED: Removed the accidental subtraction sign (-)
        print(f"That is your status: {status_result}")

main()
