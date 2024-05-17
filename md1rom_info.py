#!/usr/bin/env python3
import argparse
from mtk_structs.mtk_img import MtkImg
from kaitaistruct import KaitaiStream
from hexdump import hexdump


def print_attrs(obj):
    keys = list(filter(lambda x: not x.startswith('_'), obj.__dict__))

    for key in keys:
        value = getattr(obj, key)

        if type(value) is int:
            value = f'{value:#x}'

        print(f'{key}: {value}')


def print_gfh_info(gfh):
    print(f'header type {gfh.type}, version {gfh.version}')

    if type(gfh.body) is bytes:
        hexdump(gfh.body)
    else:
        print_attrs(gfh.body)

    print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('md1rom', type=argparse.FileType('rb'), help='path to md1rom')
    args = parser.parse_args()

    mtk_img = MtkImg(KaitaiStream(args.md1rom))

    print_gfh_info(mtk_img.file_info)

    for hdr in mtk_img.hdrs.entries:
        print_gfh_info(hdr)


if __name__ == '__main__':
    main()
