def find_max_substring_count(word):
    max_count = 0
    max_substring = ""

    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            substring = word[i:j]
            count = word.count(substring)
            if count > max_count or (count >= max_count and len(substring) > len(max_substring)):
                max_count = count
                max_substring = substring

    return max_count, max_substring


wr = input('Введите запос: ')
_, substr = find_max_substring_count(wr)
ans = wr.split(substr)
print(ans)

count = 0
for h in range(len(ans)):
    cur_count = 0
    if ans[h] == '':
        cur_count += 1
    elif cur_count > count:
        count = cur_count
    cur_count = 0
print(substr, count)