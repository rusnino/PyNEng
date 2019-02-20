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

def strip_list(output_list):
    if not output_list[-1]:
        output_list.pop(-1)
    return(output_list)

def parse_cdp_neighbors(string):
    output_list = strip_list(string.split('\n'))
    dictinored_tuples = {}
    local_host = output_list[0].split('>')[0]
    for string in output_list[6:]:
        left_tuple = (local_host, string.split()[1]+string.split()[2])
        right_tuple = (string.split()[0], string.split()[-2]+string.split()[-1])
        dictinored_tuples[left_tuple] = right_tuple
    return(dictinored_tuples)