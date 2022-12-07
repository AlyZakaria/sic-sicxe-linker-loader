from main import *
from Absolute_Loader import helper_functions as hf
import re

# open sic input file
f = open('rsc\\sic.txt', 'r')
header_string = f.readline()
starting_address = hf.hex_to_string(header_string[7:13])
program_length = hf.hex_to_string(header_string[14:])
if starting_address[3] != '0':
    starting_address = starting_address[:3] + '0'

# calculate addresses of memory
addresses = []
for i in range(hf.address_in_decimal(starting_address),
               hf.address_in_decimal(program_length) + hf.address_in_decimal(starting_address), 16):
    addresses.append(hex(i)[2:].zfill(4))
df['Address'] = addresses
df = df.fillna('xx')

# insert into cells
for line in f.readlines():
    if line[0] == 'T':
        cells_no = len(line[9:]) / 2
        record_length = line[7:9]
        record_start = hf.hex_to_string(line[1:7])

        # slice record into tuples
        obj_codes = line[9:]
        tuples = re.findall('..', obj_codes)
        tuples_counter = 0

        which_column = record_start[3]
        which_column = hf.get_column_index(which_column)
        which_row = hf.get_row(record_start, addresses[0])
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
