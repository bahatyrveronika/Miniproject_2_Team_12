def duplicate_encode(input_string):
  """
  Kata link: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
  """
    # Create an empty dictionary to store the count of each character
    char_count = {}

    # Iterate through each character in the input string
    for char in input_string:
        # Convert the character to lowercase and add it to the dictionary
        # If the character is not already in the dictionary, add it with a count of 1
        # If the character is already in the dictionary, increment its count
        char_count[char.lower()] = char_count.get(char.lower(), 0) + 1

    # Create an empty string to store the output
    output_string = ""

    # Iterate through each character in the input string again
    for char in input_string:
        # Convert the character to lowercase and add it to the output string
        # If the character appears only once, add "(" to the output string
        # If the character appears more than once, add ")" to the output string
        if char_count[char.lower()] == 1:
            output_string += "("
        else:
            output_string += ")"

    # Return the output string
    return output_string
