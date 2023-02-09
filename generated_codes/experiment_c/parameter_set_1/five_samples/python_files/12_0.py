'''

https://www.codechef.com/problems/COLCHEF
'''


def get_number_of_houses_to_paint(room_colors):
    rooms_to_paint_count = len(room_colors)
    for color_idx in range(1, len(room_colors)):
        if room_colors[color_idx] == room_colors[color_idx-1]:
            continue
        rooms_to_paint_count -= 1
    return rooms_to_paint_count


def main():
    room_colors = input()
    print(get_number_of_houses_to_paint(room_colors))


if __name__ == '__main__':
    main()