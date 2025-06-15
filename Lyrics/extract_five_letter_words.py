with open("wordlist.txt", "r") as file:
    content = file.read()

# Split by spaces and wrap each word in quotes
words = content.split()
lua_list = "{" + ", ".join(f'"{word}"\n' for word in words) + "}"

# Save to output file or print
with open("wordlist.lua", "w") as lua_file:
    lua_file.write(f"local words = {lua_list}\n")

print("Conversion complete! Check 'wordlist.lua'.")