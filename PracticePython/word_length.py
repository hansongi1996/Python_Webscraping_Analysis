words = ['cat', 'elephant', 'dog', 'butterfly', 'ant']
longest_word = max(words, key=len)
shortest_word = min(words, key=len)
print(f"단어 목록: {words}")
print(f"가장 긴 단어: {longest_word} ({len(longest_word)}글자)")
print(f"가장 짧은 단어: {shortest_word} ({len(shortest_word)}글자)")