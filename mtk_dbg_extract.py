#!/usr/bin/env python3
import argparse
from mtk_structs.mtk_dbg_info import MtkDbgInfo
from kaitaistruct import KaitaiStream


def file_info(files):
    for file in files:
        print(file.filename)
        for addr_pair in file.addr_pairs:
            print(f'{addr_pair.addr1:#010x} - {addr_pair.addr2:#010x}')


def symbol_text(symbols):
    for sym in symbols:
        symbol = sym.symbol.replace(' ', '_')
        print(f'{symbol} {sym.addrs.addr1:#010x} l')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dbg_file', type=argparse.FileType('rb'))
    parser.add_argument('--files', action='store_true', default=False, help='show file info instead of symbols')
    args = parser.parse_args()

    mtk_dbg = MtkDbgInfo(KaitaiStream(args.dbg_file))

    if args.files:
        file_info(mtk_dbg.body.files)
    else:
        symbol_text(mtk_dbg.body.symbols.entries)


if __name__ == '__main__':
    main()
