from collections import defaultdict
suffixes = defaultdict(set)
for word in open('words.txt'):
    if word.startswith('#'):
        continue
    first_letter, suffix = word[0], word[1:].strip()
    suffixes[suffix].add(first_letter)
for suffix in sorted(suffixes, key=lambda x: (len(suffixes[x]), x)):
    num_words = len(suffixes[suffix])
    first_letters = " ".join(sorted(suffixes[suffix]))
    print(f'{num_words:>2} {suffix:<22} [{first_letters}]')
