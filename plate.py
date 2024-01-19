def main():
    vanity_plate = input("Enter your vanity plate: ")
    if is_valid(vanity_plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    def has_valid_length(s):
        return 2 <= len(s) <= 6

    def starts_with_two_letters(s):
        return s[:2].isalpha()

    def has_valid_characters(s):
        return all(c.isalnum() for c in s)

    def numbers_at_end_only(s):
        return s[-1].isdigit() and (not s[:-1] or s[:-1].isalpha())

    def first_number_not_zero(s):
        return not s[0].isdigit() or s[0] != '0'
    
    print(f"Length: {has_valid_length(s)}")
    print(f"Starts with letters: {starts_with_two_letters(s)}")
    print(f"Valid characters: {has_valid_characters(s)}")
    print(f"Numbers at end only: {numbers_at_end_only(s)}")
    print(f"First number not zero: {first_number_not_zero(s)}")

    if has_valid_length(s) and starts_with_two_letters(s) and has_valid_characters(s) and numbers_at_end_only(s) and first_number_not_zero(s):
        return True
    return False

if __name__ == "__main__":
    main()


