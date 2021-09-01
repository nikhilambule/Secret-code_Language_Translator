# Rule: if word starts from vowel add yay: apple -> appleyay
#       if word starts with consonant add first word at the end add ay: cat => atcay



# Take input sentence from user

sentence = input("Enter yor sentence: ").strip().lower()

# Split the sentence into words

split_sent = sentence.split()

print("\nYour sentence in splitted form\n")

print(split_sent)

print(" ")


# Convert into code language
new_codelanguage = []

for word in split_sent:
    if word[0] in "aeiou":
        new_codelanguage.append(word + "yay")

    elif True:
        word_c = word + word[0]
        word_c1 = word_c[1:]
        new_codelanguage.append(word_c1 + "ay")

print("Coded words\n")
print(new_codelanguage)
print(" ")


output = " ".join(new_codelanguage)

print("Coded sentence:\n")
print(output)
