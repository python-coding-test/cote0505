import sys
input = sys.stdin.readline
n = int(input().strip())
options = [input().rstrip() for _ in range(n)]
shortcut = []
options2 = []
for option in options:
    words = option.split()
    shortcut_assigned = False
    word_start_index = 0
    for word in words:
        if word[0] not in shortcut and word[0] != ' ':
            shortcut.append(word[0].upper())
            shortcut.append(word[0].lower())
            char_index = option.index(word[0], word_start_index)
            a = option[:char_index] + f"[{word[0]}]" + option[char_index+1:]
            options2.append(a)
            shortcut_assigned = True
            break
        word_start_index += len(word) + 1
    if not shortcut_assigned:
        for i, char in enumerate(option):
            if char not in shortcut and char != ' ':
                shortcut.append(char.upper())
                shortcut.append(char.lower())
                options2.append(option[:i]+f"[{char}]"+option[i+1:])
                shortcut_assigned = True
                break
    if not shortcut_assigned:
        options2.append(option)

for formatted_option in options2:
    print(formatted_option)