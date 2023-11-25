def find_anagrams(inputs):
    anagram_groups = {}

    for word in inputs:
        # Convert the word to lowercase and sort its characters
        sorted_word = ''.join(sorted(word.lower()))
        print(sorted_word)

        # Add the word to the corresponding anagram group
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
        print(anagram_groups)

    # Remove groups with only one word
    anagram_groups = {key: value for key, value in anagram_groups.items() if len(value) > 1}
    print(anagram_groups)
    return list(anagram_groups.values())


# Example usage
inputs = ['listen', 'silent', 'elbow', 'below', 'state', 'taste','rank','fan']
anagram_groups = find_anagrams(inputs)
print(anagram_groups)
# Print the anagram groups
for group in anagram_groups:
    print(group)
