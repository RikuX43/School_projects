print('\nThis is Program 1\n')

print('\nRequirement 1\n')
print('Please enter the information requested.\n')
name = input('Last name: ')
hometown = input('Hometown: ')
occupation = input('Occupation: ')
hobby = input('Hobby: ')

print('\nRequirement 2\n')
print('Hello {}!'.format(name))
print('From {}.'.format(hometown))
print('I hope you like being a(n) {}.'.format(occupation))
print('{} sounds like an interesting hobby.'.format(hobby))

print('\nReqirement 3\n')
print('Alternative Output\n')
print('Hello',name,'!')
print('From ' + hometown + '.')
print('I hope you like being a(n)',occupation)
print(hobby + ' sounds like an interesting hobby.')

print('\nReqirement 4\n')
print('More Options\n')
print('Hello ', 	name,	'!')
print('Hello ',name,'!', sep='')
print('Hello ',name,'! ', end='', sep='')
print('Hello ',name,'! ', end='', sep='')
print('Hello ',name,'! ', end='', sep='')
