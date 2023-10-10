


if __name__ == '__main__':

     mark_1 = int(input('enter mark #1:'))
     mark_2 = int(input('enter mark #2:'))
     mark_3 = int(input('enter mark #3:'))
     mark_4 = int(input('enter mark #4:'))
     mark_5 = int(input('enter mark #5:'))

     highest = max(mark_1, mark_2, mark_3, mark_4, mark_5)
     lowest = min(mark_1, mark_2, mark_3, mark_4, mark_5)

     average = (mark_1 + mark_2 + mark_3 + mark_4 + mark_5) / 5

     print()
     print(f'highest mark: {highest}.')
     print(f'lowest mark: {lowest}.')
     print(f'highest mark: {average}.')

     print(f'The highest mark was {highest} the lowest mark was {lowest}'
           f'and the average as {average}.')
