from main import *
import re


# get which row in memory graph
def get_row(start_record, start_program):
    row = int(start_record, base=16) - int(start_program, base=16)
    row = (row / 16)
    return int(row)


def get_column_index(column_name):
    column_index = df.columns.get_loc(column_name)
    return column_index


# open sic input file
f = open('rsc\\sic.txt', 'r')
header_string = f.readline()
starting_address = hex(int(header_string[7:13], base=16))[2:].zfill(4).upper()
program_length = hex(int(header_string[14:], base=16))[2:].zfill(4).upper()
print(program_length)
if starting_address[3] != '0':
    starting_address = starting_address[:3] + '0'
# calculate addresses of memory
addresses = []
for i in range(int(starting_address, base=16), int(program_length, base=16)+int(starting_address, base=16), 16):
    addresses.append(hex(i)[2:].zfill(4))
df['Address'] = addresses
df = df.fillna('xx')

# insert into cells
for line in f.readlines():
    if line[0] == 'T':
        cells_no = len(line[9:]) / 2
        record_length = line[7:9]
        record_start = hex(int(line[1:7], base=16))[2:].zfill(4).upper()

        # slice record into tuples
        obj_codes = line[9:]
        tuples = re.findall('..', obj_codes)
        tuples_counter = 0

        which_column = record_start[3]
        which_column = get_column_index(which_column)
        which_row = get_row(record_start, addresses[0])
        flag = False
        for row in range(which_row, which_row + 3, 1):
            for column in range(which_column, 17):
                if tuples_counter < len(tuples):
                    df.iloc[row, column] = tuples[tuples_counter]
                    tuples_counter += 1
                else:
                    flag = True
                    break;
            which_column = 1
            if flag:
                break;

print(df)
