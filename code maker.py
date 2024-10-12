print("hi")
print("To encode your message type 1 and decode your message type 2")







import random
import string
# Function to generate a random three-letter string
def generate_random_letters():
    return ''.join(random.choices(string.ascii_lowercase, k=3))

# Function to encode a message




def encode_message(message):
    words = message.split()
    encoded_list = []
    for word in words:
        random_prefix = generate_random_letters()
        random_suffix = generate_random_letters()
        new_word = f"{random_prefix}{word}{random_suffix}"
        encoded_list.append(new_word)
    return ' '.join(encoded_list)




# Function to decode a message



def decode_message(encoded_message):
    words = encoded_message.split()
    decoded_list = []
    for word in words:
        # Remove the first and last three characters
        decoded_word = word[3:-3]
        decoded_list.append(decoded_word)
    return ' '.join(decoded_list)





a=int(input("type your response here, 1 for encoding your message and 2 for decoding your message"))
if a==1:
    original_message=input("type youe message here")
    encoded_message = encode_message(original_message)
    print("Encoded Message:", encoded_message)
elif a==2:
    original_message=input("type youe message here")
    decoded_message = decode_message(original_message)
    print("Decoded Message:", decoded_message)
else: print("invalid response")


















































    



