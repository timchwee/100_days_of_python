def caesar_cipher_transform(text, shift_amount):
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  transformed_text = ""

  normalized_shift = shift_amount % len(alphabet)

  for char in text:
    if char.isalpha():
      is_upper = char.isupper()
      char_lower = char.lower()

      try:
        current_index = alphabet.index(char_lower)
        new_index = (current_index + normalized_shift) % len(alphabet)
        shifted_char = alphabet[new_index]

        if is_upper:
          transformed_text += shifted_char.upper()
        else:
          transformed_text += shifted_char

      except ValueError:
        transformed_text += char
    else:
      transformed_text += char

  return transformed_text

print("--- Caesar Cipher Program ---")

while True:
  mode_choice = input("Do you want to 'encode' or 'decode' the message? (e/d): ").lower()
  if mode_choice in ['e', 'd']:
    break
  else:
    print("Invalid choice. Please enter 'e' for encode or 'd' for decode.")

user_text = input("Enter your message: ")
while True:
  try:
    user_shift = int(input("Enter the shift number: "))
    break
  except ValueError:
    print("Invalid shift number. Please enter an integer.")

final_shift_amount = user_shift
if mode_choice == 'd':
  final_shift_amount = -user_shift

result_message = caesar_cipher_transform(user_text, final_shift_amount)

print(f"\nOriginal Message: {user_text}")
print(f"Shift Amount: {user_shift}")
print(f"Mode: {'Encode' if mode_choice == 'e' else 'Decode'}")
print(f"Transformed Message: {result_message}")
