
# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# 2. Then check for the number of times the letters in the word LOVE occurs.   
# 3. Then combine these numbers to make a 2 digit number and print it out.


def calculate_love_score(name1, name2):
  """
  Calculates a 'love score' between two names based on the occurrences
  of letters in the words 'TRUE' and 'LOVE'.

  Args:
    name1: The first person's name (string).
    name2: The second person's name (string).
  """

  # Combine both names into a single string and convert to lowercase
  combined_names = (name1 + name2).lower()

  # Calculate the 'TRUE' score
  true_score = 0
  true_letters = "true"
  for char in true_letters:
    true_score += combined_names.count(char)

  # Calculate the 'LOVE' score
  love_score = 0
  love_letters = "love"
  for char in love_letters:
    love_score += combined_names.count(char)

  # Combine the scores to form a two-digit number
  # Convert scores to strings and concatenate them
  love_score_str = str(true_score) + str(love_score)

  # Print the final love score
  print(love_score_str)

# Example Usage:
print("--- Kanye West and Kim Kardashian ---")
calculate_love_score("Kanye West", "Kim Kardashian") # Expected Output: 42

print("\n--- Angela Yu and Jack Bauer ---")
calculate_love_score("Angela Yu", "Jack Bauer") # Expected Output: 53

print("\n--- John Doe and Jane Smith ---")
calculate_love_score("John Doe", "Jane Smith")

print("\n--- Taylor Swift and Travis Kelce ---")
calculate_love_score("Taylor Swift", "Travis Kelce")