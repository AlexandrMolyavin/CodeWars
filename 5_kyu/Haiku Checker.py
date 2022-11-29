https://www.codewars.com/kata/5c765a4f29e50e391e1414d4
def is_haiku(text):
    vowel = ['a','e','i','o','u','y']
    syllabus = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    lines = text.split('\n')
    count_list = []
    for line_num, line in enumerate(lines):
        count = 0
        for word in line.split(' '):
            curr_count = 0
            prev_letter = ''
            prev_prev_letter = ''
            for letter in word.lower():
                if letter in vowel or letter in syllabus:
                    if letter in vowel:    
                        if prev_letter in syllabus or prev_letter == '':
                            curr_count += 1
                    prev_prev_letter = prev_letter
                    prev_letter = letter
            if prev_prev_letter in syllabus and curr_count > 1 and prev_letter == 'e':
                curr_count -= 1
            count += curr_count
        count_list.append(count)
    if count_list == [5, 7, 5]:
        return True
    else:
        return False
