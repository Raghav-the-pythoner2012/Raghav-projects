emoji_dict = {
    "😊": "smiling with a face and smiling face",
    "😂": "face with tears of joy",
    "🎶": "music notes",
    "🐶": "dog face",
    "🌙": "crescent moon"
}


def emoji_meaning(emoji):
    return emoji_dict.get(emoji, "Unknown emoji")


print("Welcome to the Emoji _to Text Converter")
emoji_input = input("Enter an emoji:")
text_output = emoji_meaning(emoji_input)
print(f"The meaning of the emoji is :{text_output}")