# Day 7

import pathlib
import shutil
import os

data = pathlib.Path('/tmp/data7')

def create_root():
    root = pathlib.Path('/tmp/fsroot_advent7')
    if root.exists():
        # Cleanup/start over
        shutil.rmtree(root)
        root.mkdir()
    return root


def create_fs():
    cwd = ['/']
    for line in data.read_text().splitlines():
        if not line: continue
        if line.startswith('$'):
            prompt, cmd, *args = line.split()
            args = ' '.join(args)
            if cmd == 'cd':
                if args == '/':
                    cwd = [cwd[0]]
                elif args == '..' and cwd[-1 != '/']:
                    # Remove last item
                    _ = cwd.pop()
                else:
                    # Add new item
                    cwd.append(args)
                    fld = root / '/'.join(cwd[1:])
                    if not fld.exists():
                        fld.mkdir()
            elif cmd == 'ls':
                continue
        else:
            # Use cwd to know where we are
            fld = root / '/'.join(cwd[1:])
            if cmd == 'ls':
                info, name = line.split()
                if info == 'dir':
                    folder = name
                    this_fld = fld / folder
                    if not this_fld.exists():
                        this_fld.mkdir()
                else:
                    size = int(info)
                    filename = name
                    this_file = this_fld = fld / filename
                    if not this_file.exists():
                        _ = this_file.write_bytes(bytes(size))
                        # this_file.stat().st_size

root = create_root()
create_fs()


# Part1 - Get the summed size of _all_ the folders that are upto 100,000 in size
part1 = 0
for dirpath, dirnames, filenames in os.walk(root):
    this_folder = pathlib.Path(dirpath)
    if this_folder == root: continue
    size = sum(os.path.getsize(os.path.join(dirpath, filename))
               for dirpath, dirnames, filenames in os.walk(this_folder)
               for filename in filenames)
    if size <= 100000:
        part1 += size
# part1: 1443806


# Part 2 - Find the size of the smallest folder that needs to be deleted to give us 30000000 free space
disk_size = 70000000
space_req = 30000000
size = sum(os.path.getsize(os.path.join(dirpath, filename))
               for dirpath, dirnames, filenames in os.walk(root)
               for filename in filenames)
space_avail = disk_size - size
space_to_find = space_req - space_avail

part2 = {}
for dirpath, dirnames, filenames in os.walk(root):
    this_folder = pathlib.Path(dirpath)
    if this_folder == root: continue
    size = sum(os.path.getsize(os.path.join(dirpath, filename))
               for dirpath, dirnames, filenames in os.walk(this_folder)
               for filename in filenames)
    part2[this_folder] = size


def get_folder_to_delete():
    sorted_by_size = {k: v for k, v in sorted(part2.items(), key=lambda item: item[1])}
    for folder in sorted_by_size:
        if sorted_by_size[folder] >= space_to_find:
            return folder, sorted_by_size[folder]

pth, size = get_folder_to_delete()

# Part 2 - 942298
