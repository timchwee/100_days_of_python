def caesar_cipher_transform(text, shift_amount):
  """
  Performs a Caesar cipher transformation (encryption or decryption) on the given text.

  Args:
    text: The string to be transformed.
    shift_amount: An integer representing the number of positions to shift
                  each letter. Positive for encoding, negative for decoding.

  Returns:
    The transformed text as a string.
  """
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  transformed_text = ""

  # Normalize the shift_amount to be within the range of the alphabet size (0-25)
  # This handles very large shifts or negative shifts gracefully by wrapping around.
  # For example, a shift of 27 is effectively 1 (27 % 26 = 1).
  # A shift of -1 is effectively 25 (-1 % 26 = 25 in Python for negative numbers,
  # which correctly wraps backwards).
  normalized_shift = shift_amount % len(alphabet)

  for char in text:
    if char.isalpha():  # Check if the character is an alphabet letter
      is_upper = char.isupper() # Remember if original character was uppercase
      char_lower = char.lower() # Convert to lowercase for consistent indexing

      try:
        # Find the current position of the letter in the alphabet list
        current_index = alphabet.index(char_lower)

        # Calculate the new shifted position
        # The modulo operator (%) ensures wrapping around the alphabet
        new_index = (current_index + normalized_shift) % len(alphabet)

        # Get the new character from the alphabet list
        shifted_char = alphabet[new_index]

        # Convert back to uppercase if the original character was uppercase
        if is_upper:
          transformed_text += shifted_char.upper()
        else:
          transformed_text += shifted_char

      except ValueError:
        # This handles cases where a character might be alphabetic but not in our
        # defined alphabet list (e.g., non-English alphabetic characters if extended).
        transformed_text += char
    else:
      # If the character is not an alphabet letter (e.g., space, number, punctuation),
      # add it to the transformed_text without shifting.
      transformed_text += char

  return transformed_text

# --- Main Program Flow ---
print("--- Caesar Cipher Program ---")

# Ask the user for the mode (encode or decode)
while True:
  mode_choice = input("Do you want to 'encode' or 'decode' the message? (e/d): ").lower()
  if mode_choice in ['e', 'd']:
    break
  else:
    print("Invalid choice. Please enter 'e' for encode or 'd' for decode.")

# Get input text and shift amount from the user
user_text = input("Enter your message: ")
while True:
  try:
    user_shift = int(input("Enter the shift number: "))
    break
  except ValueError:
    print("Invalid shift number. Please enter an integer.")

# Adjust the shift amount based on the chosen mode
final_shift_amount = user_shift
if mode_choice == 'd':
  final_shift_amount = -user_shift # For decoding, we shift backwards

# Perform the Caesar cipher transformation
result_message = caesar_cipher_transform(user_text, final_shift_amount)

# Print the final result
print(f"\nOriginal Message: {user_text}")
print(f"Shift Amount: {user_shift}")
print(f"Mode: {'Encode' if mode_choice == 'e' else 'Decode'}")
print(f"Transformed Message: {result_message}")

print("\n--- Example: Encoding and then Decoding ---")
# Encoding
example_encode_text = "tim is trying"
example_encode_shift = 1
encoded_message = caesar_cipher_transform(example_encode_text, example_encode_shift)
print(f"Original: '{example_encode_text}', Shift: {example_encode_shift}, Encoded: '{encoded_message}'")

# Decoding the encoded message
example_decode_text = encoded_message # Use the output from encoding
example_decode_shift = 1 # Use the same shift amount, but for decoding
decoded_message = caesar_cipher_transform(example_decode_text, -example_decode_shift) # Pass negative shift for decoding
print(f"Encoded: '{example_decode_text}', Shift: {example_decode_shift}, Decoded: '{decoded_message}'")


