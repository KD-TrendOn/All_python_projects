import os
nazv = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for i in os.listdir(r'/sou'):
    if 'b' in i:
        try:
            kuk = nazv[nazv.index(i[0]) - 1] + '#' + i[2] + '.aiff'
        except BaseException:
            kuk = nazv[-1] + '#' + i[2] + '.aiff'
        os.rename(i, kuk, src_dir_fd=None, dst_dir_fd=None)