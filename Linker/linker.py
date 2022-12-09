from Absolute_Loader import helper_function as hf
import re

starting_mem_address = ''

# to get linker
def get_linker(df , stAddress):
    # get starting address from user
    global starting_mem_address
    starting_mem_address = stAddress
       
    # open sicxe program
    f = open('rsc\\sicxe.txt', 'r')
    # get all starting addresses and lengths of all programs
    list_lengths = []
    list_starts = []
    for line in f.readlines():
        if line[0] == 'H':
            program_length = hf.hex_to_string(line[14:])
            starting_address = hf.hex_to_string(line[7:13])
            if len(list_starts) == 0:
                starting_address = hex(
                    hf.address_in_decimal(starting_mem_address))[2:].upper()
                list_starts.append(starting_address)
            else:
                starting_address = hex(
                    hf.address_in_decimal(list_starts[-1]) + hf.address_in_decimal(list_lengths[-1]))[2:].upper()
                list_starts.append(starting_address)
            list_lengths.append(program_length)
    programs_map = dict(zip(list_starts, list_lengths))
    # print(programs_map)
    # calculate addresses of memory
    addresses = []
    size = hf.address_in_decimal(list_starts[-1]) + hf.address_in_decimal(list_lengths[-1]) + 1
    df = hf.getMemoryGraph(list_starts[0], size, addresses, df)
    f.close()

    # insert into cells

    f = open('rsc\\sicxe.txt', 'r')
    counter = 0
    for line in f.readlines():
        if line[0] == 'T':
            record_start = hf.hex_to_string(hex(hf.address_in_decimal(line[1:7])+hf.address_in_decimal(list_starts[counter])))
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
                        break
                which_column = 1
                if flag:
                    break
        if line[0] == 'E':
            counter+=1
    return df