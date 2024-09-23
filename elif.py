student_exp = input('Enter spanish experience: ')

if student_exp == '':
    print('You should taking 101.')
elif student_exp == 'Spanish 101':
    print('You should taking 102.')
elif student_exp == 'Spanish 102':
    print('You should taking 201.')
elif student_exp == 'Spanish 201':
    print('You should taking 202.')
elif student_exp == 'Spanish 202':
    print('You should move to advanced courses.')
else:
    print("Sorry, I didn't recognize what you entered.")
    print("Please give me one of these experience levels: none, 101, 102, 201, or 202.")