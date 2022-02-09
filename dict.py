mane_dict = {'46bLSJ8rqa': 'kd3YaAgW0W', '2KmK0xgWNs': 'JdsDdTEHjG', 'Ocw8e3xiYE': 'bASum7YGjX'}
main_list = list(mane_dict.values())

value = {'letters': 0, 'numbers': 0}
score = 0
for q in range(len(main_list)):
    for i in main_list[score]:
        if i.isalpha():
            value['letters'] += 1
        elif i.isdigit():
            value['numbers'] += 1
    print(value)
    value['letters'] = 0
    value['numbers'] = 0
    score += 1
