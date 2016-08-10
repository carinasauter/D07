# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


def capitalize_nested(t):
    for index, s in enumerate(t):
        if type(s) == str:
            t[index] = s.upper()
        else:
            capitalize_nested(s)
    return t


def main():
    pass


if __name__ == '__main__':
    main()
