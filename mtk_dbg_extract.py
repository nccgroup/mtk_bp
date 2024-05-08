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


def symbol_text(symbols):
    for sym in symbols:
        # terminator entry
        if sym.symbol == '':
            break

        symbol = sym.symbol.replace(' ', '_')
        print(f'{symbol} {sym.body.addrs.addr1:#010x} l')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dbg_file', type=argparse.FileType('rb'))
    parser.add_argument('--files', action='store_true', default=False, help='show file info instead of symbols')
    args = parser.parse_args()

    mtk_dbg = MtkDbgInfo(KaitaiStream(args.dbg_file))

    assert mtk_dbg.header.cati_type == 0x524E5443  # root container

    container = mtk_dbg.header.body

    if args.files:
        for i in range(container.num_entry_info):
            info = container.entry_info[i]
            print(f'{info.unk1:#08x} {info.name} {info.unk2}')
            file_info(container.entry_stream.entries[i].body.files)
    else:
        for i in range(container.num_entry_info):
            if container.num_entry_info > 1:
                info = container.entry_info[i]
                print(f'# {info.unk1:#08x} {info.name} {info.unk2}')
            symbol_text(container.entry_stream.entries[i].body.symbols)

        if container.num_entry_info > 1:
            print('# WARNING: output contains symbols for multiple debug info entries (separator lines begin with "#"")')


if __name__ == '__main__':
    main()
