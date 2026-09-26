s="Python is a simple to learn language"
word=s.split()
longest_word=max(word,key=len)
shortest_word=min(word,key=len)
print("Longest word",longest_word)
print("Shortest word",shortest_word)