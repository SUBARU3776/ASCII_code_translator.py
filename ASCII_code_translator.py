def translate_ascii_code(code):
    if code < 0 or code > 127:
        return "Invalid ASCII code"
    else:
        return chr(code)

# Please enter ASCII code
code = int(input("Please enter ASCII code: "))

# Translate ASCII codes into characters
character = translate_ascii_code(code)

# Show Results
print(f"ASCII code {code} are '{character}' translated into text")
