def duplicate_count(text):
  """
  Kata link: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
  """
    # Convert the string to lowercase and create a set of characters
    unique_chars = set(text.lower())
    
    # Initialize a count variable to 0
    count = 0
    
    # Iterate over each character in the set of unique characters
    for char in unique_chars:
        # If the character occurs more than once in the input string
        if text.lower().count(char) > 1:
            # Increment the count variable
            count += 1
            
    # Return the count variable
    return count
