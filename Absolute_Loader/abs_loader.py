import re
from Absolute_Loader import helper_function as hf



# get The Absolute loader
def get_absolute_loader(df):
    # open sic input file
    f = open('rsc\\sic.txt', 'r')

    # get the starting address & program length
    header_string = f.readline()
    starting_address = hf.hex_to_string(header_string[7:13])
    program_length = hf.hex_to_string(header_string[14:])
    
    # calculate addresses of memory
    addresses = []
    df = hf.getMemoryGraph(starting_address, program_length, addresses, df)

    # insert into cells
    for line in f.readlines():
        if line[0] == 'T':
            record_start = hf.hex_to_string(line[1:7])
            # slice record into tuples
            obj_codes = line[9:]
            tuples = re.findall('..', obj_codes)
            tuples_counter = 0
            # get the index of starting cell
            [which_row, which_column] = hf.get_cell(record_start, addresses[0], record_start[3], df)
            flag = False
            for row in range(which_row, which_row + 3, 1):
                for column in range(which_column, 17):
                    if tuples_counter < len(tuples):
                        df.iloc[row, column] = tuples[tuples_counter]
                        tuples_counter += 1
                    # if we exceed the size of tuples(records) break
                    else:
                        flag = True
                        break;
                which_column = 1
                if flag:
                    break;
    return df


