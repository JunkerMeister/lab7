def find_max_substring(word):
    max_count = 0
    max_substring = ""

    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            substring = word[i:j]
            count = word.count(substring)
            if count > max_count or (count >= max_count and len(substring) > len(max_substring)):
                max_count = count
                max_substring = substring

    return max_substring

def find_end_count(wr):
    substr = find_max_substring(wr)
    ans = list(wr.replace(substr, '*'))
    end_count = 0
    cur_count = 0
    for h in ans:
        if h == '*':
            cur_count += 1
            end_count = max(end_count, cur_count)
        else:
            cur_count = 0
    return end_count

wr = input('Введите запос: ')


print(f"Подстрока '{find_max_substring(wr)}' {find_end_count(wr)} раза.")

