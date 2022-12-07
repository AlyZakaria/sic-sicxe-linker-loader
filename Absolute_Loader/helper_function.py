
# get address in decimal
def address_in_decimal(address):
    return int(address, base=16)


# get address as string
def hex_to_string(address):
    string = hex(int(address, base=16))
    return string[2:].zfill(4).upper()

# get which row in memory graph
def get_row(start_record, start_program):
    row = address_in_decimal(start_record) - address_in_decimal(start_program)
    row = (row / 16)
    return int(row)


# get which column in memory graph
def get_column_index(column_name, df):
    column_index = df.columns.get_loc(column_name)
    return column_index


# get th specific cell in memory graph
def get_cell(start_record, start_program, column_name, df):
    row = get_row(start_record, start_program)
    column = get_column_index(column_name, df)
    return [row, column]



# do memoryGraph
def getMemoryGraph(starting_address, program_length, addresses, df):
    if starting_address[3] != '0':
        starting_address = starting_address[:3] + '0'
    # size = address_in_decimal(program_length) + address_in_decimal(starting_address)
    for i in range(address_in_decimal(starting_address), program_length, 16):
        addresses.append(hex(i)[2:].zfill(4))
    df['Address'] = addresses
    df = df.fillna('xx')
    return df

