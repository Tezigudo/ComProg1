import csv


def exact_num_medal(medal_data, medal_type, threshold):
    return sum(int(data[medal_type]) > threshold for data in medal_data)


while 1:
    medal_csv = input('Enter CSV file: ')
    try:
        medal_data = []
        with open(medal_csv, 'r') as medal_file:
            data = csv.DictReader(medal_file)
            for each_data in data:
                medal_data.append(each_data)
        break
    except FileNotFoundError:
        print(f'Filename {medal_csv} does not exist. Please enter again.')

while 1:
    medal_type = input('What is the type of medal? (or [exit] to quit): ')
    if medal_type == 'exit':
        exit()
    if medal_type not in ['Gold', 'Silver', 'Bronze']:
        print(f"The key '{medal_type}' does not exist.")
        continue
    threshold = int(input(f'Print the number of teams that has {medal_type} medals over: '))
    print(f'Answer = {exact_num_medal(medal_data, medal_type, threshold)}')
