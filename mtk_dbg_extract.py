#!/usr/bin/env python3
import argparse
from mtk_structs.mtk_dbg_info import MtkDbgInfo
from kaitaistruct import KaitaiStream


def file_info(files):
    for file in files:
        # terminator entry
        if file.filename == '':
            break

        print(file.filename)
        for addr_pair in file.body.addr_pairs:
            print(f'{addr_pair.addr1:#010x} - {addr_pair.addr2:#010x}')


def symbol_text(symbols, remap=False, as_functions=False):
    for sym in symbols:
        # terminator entry
        if sym.symbol == '':
            break

        symbol = sym.symbol.replace(' ', '_')
        addr = sym.body.addrs.addr1
        if remap and addr < 0x90000000:
            addr += 0x90000000

        def_type = 'f' if as_functions else 'l'

        print(f'{symbol} {addr:#010x} {def_type}')


def show_file_info(mtk_dbg):
    container = mtk_dbg.header.body

    for i in range(container.num_entry_info):
        info = container.entry_info[i]
        print(f'{info.unk1:#08x} {info.name} {info.unk2}')
        file_info(container.entry_stream.entries[i].body.files)


def show_symbol_info(mtk_dbg, remap=False, as_functions=False):
    container = mtk_dbg.header.body

    for i in range(container.num_entry_info):
        if container.num_entry_info > 1:
            info = container.entry_info[i]
            print(f'# {info.unk1:#08x} {info.name} {info.unk2}')
        symbol_text(container.entry_stream.entries[i].body.symbols, remap=remap, as_functions=as_functions)

    if container.num_entry_info > 1:
        print('# WARNING: output contains symbols for multiple debug info entries (separator lines begin with "#"")')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dbg_file', type=argparse.FileType('rb'))
    parser.add_argument('--files', action='store_true', default=False, help='show file info instead of symbols')
    parser.add_argument('--remap', action='store_true', default=False, help='remap 0x0 addrs to 0x90000000 addrs')
    parser.add_argument('--labels', action='store_true', default=False, help='output labels rather than function definitions')
    args = parser.parse_args()

    mtk_dbg = MtkDbgInfo(KaitaiStream(args.dbg_file))

    assert mtk_dbg.header.cati_type == 0x524E5443  # root container

    if args.files:
        show_file_info(mtk_dbg)
    else:
        show_symbol_info(mtk_dbg, remap=args.remap, as_functions=(not args.labels))


if __name__ == '__main__':
    main()
