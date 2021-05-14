print('\nRequirement 1')

print('\nThis is Program 3.')

print('\nRequirement 2')

print('\nThis program records votes for the best soccer players in the world.')

print('\nRequirement 3')

print('\nEnter three soccer player names.')

first_player = input('\nEnter first soccer player: ')
second_player = input('\nEnter second soccer player: ')
third_player = input('\nEnter third soccer player: ')

print('\nRequirement 4')

print('\nPlease enter total vote number for each soccer player.\n')

one_vote = int(input('\nEnter total votes for first_player: '))
two_vote = int(input('\nEnter total votes for second_player: '))
three_vote = int(input('\nEnter total votes for third_player: '))

print('\nRequirement 5 & 6')

if one_vote > two_vote and one_vote > three_vote:
    print("\n{} is the winner with {} votes.\n".format(first_player, one_vote))

elif two_vote > one_vote and two_vote > three_vote:
    print('\n{} is the winner with {} votes.\n'.format(second_player, two_vote))

elif three_vote > one_vote or three_vote > two_vote:
    print('\n{} is the winner with {} votes.\n'.format(third_player, three_vote))

print('\nRequirement 7')

print('\nEnter three basketball player names.')

fourth_player = input('\nEnter first basketball player: ')
fifth_player = input('\nEnter second basketball player: ')
sixth_player = input('\nEnter third basketball player: ')

print('\nRequirement 8')

print('\nPlease enter vote number for each basketball player.\n')

four_vote = int(input('\nEnter votes for first basketball player: '))
five_vote = int(input('\nEnter votes for second basketball player: '))
six_vote = int(input('\nEnter votes for third basketball player: '))

print('\nRequirement 9 & 10')

if four_vote > five_vote and four_vote > six_vote:
    print("\n{} is the winner with {} votes.\n".format(fourth_player, four_vote))

elif five_vote > four_vote and five_vote > six_vote:
    print("\n{} is the winner with {} votes.\n".format(fifth_player, five_vote))

elif six_vote > four_vote or six_vote > five_vote:
    print("\n{} is the winner with {} votes.\n".format(sixth_player, six_vote))

print('\nRequirement 11')

print("\nI enjoyed program 3, it was interesting.\n")
