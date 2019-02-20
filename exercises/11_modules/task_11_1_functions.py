# --------------------------
# Program by Ruslan F.
#
#
# Version   Date    Info
# 1.0       2019    Initial Version
#
# --------------------------


def read_file_to_string(filename):
    output_string = []
    with open(filename, 'r') as f:
        for line in f:
            output_string.append(line)
        output_string = ''.join(output_string)
    return(output_string)

def strip_list(output_string):
    if not output_string[-1]:
        output_string.pop(-1)
    return(output_string)

def parse_cdp_neighbors(output_string):
    dictinored_tuples = {}
    local_host = output_string[0].split('>')[0]
    for string in output_string[6:]:
        left_tuple = (local_host, string.split()[1]+string.split()[2])
        right_tuple = (string.split()[0], string.split()[-2]+string.split()[-1])
        dictinored_tuples[left_tuple] = right_tuple
    return(dictinored_tuples)


