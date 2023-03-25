#!/usr/bin/env python

import argparse
import pathlib

from lzsslib.decompress import LzssDecompressor

from .header import header_parse


def create(fin, fout):
    raise NotImplementedError


def extract(fin, fout):
    # Parse header...
    buffer = fin.read(1024)
    header = header_parse(buffer)
    
    # Set the file cursor in the begining of the content...
    fin.seek(header.content_offset)

    # Create a decompressor...
    decomp = LzssDecompressor(
        offset_width=header.offset_width,
        size_width=header.size_width,
        size_min=header.size_min)

    # Decompress
    remaining_size = header.decomp_size
    while (buffer := fin.read(1024)):
        out = decomp.decompress(buffer, remaining_size)
        remaining_size -= len(out)
        fout.write(out)
    
    fout.flush()


def main():
    parser = argparse.ArgumentParser(
                    prog='jzp',
                    description='Archive and unarchive JZP files')
    parser.add_argument('-c', '--create', action='store_true')
    parser.add_argument('-x', '--extract', action='store_true')
    parser.add_argument('-f', '--file', action='store', required=True, type=pathlib.Path)
    args = parser.parse_args()

    if args.create and args.extract:
        print("Incompatible \'create\' and \'extract\' options simultaneously set. Please specify only one of the two...")
        return 1

    if not args.create and not args.extract:
        print("Please specify a mode of operation, either \'create\' or \'extract\'...")
        return 1

    fin_mode = 'rb' if args.extract else 'wb'
    fin = args.file.open(mode=fin_mode)

    fout_mode = 'wb' if args.extract else 'rb'
    fout_ext = '.jzp' if args.create else '.bin'
    fout = args.file.with_suffix(fout_ext).open(mode=fout_mode)

    if args.create:
        create(fin, fout)
    else:
        extract(fin, fout)

    fin.close()
    fout.close()

if __name__ == "__main__":
    main()
