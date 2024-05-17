#!/usr/bin/env python3
import argparse
import typer
from mtk_structs.mtk_dbg_info import MtkDbgInfo
from kaitaistruct import KaitaiStream


app = typer.Typer()


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


def load_dbg_info(dbg_file):
    mtk_dbg = MtkDbgInfo(KaitaiStream(dbg_file))
    assert mtk_dbg.header.cati_type == 0x524E5443  # root container
    return mtk_dbg


@app.command()
def files(dbg_file: typer.FileBinaryRead):
    mtk_dbg = load_dbg_info(dbg_file)
    container = mtk_dbg.header.body

    for i in range(container.num_entry_info):
        info = container.entry_info[i]
        print(f'{info.unk1:#08x} {info.name} {info.unk2}')
        file_info(container.entry_stream.entries[i].body.files)


@app.command()
def symbols(dbg_file: typer.FileBinaryRead, remap: bool = False, labels: bool = False):
    mtk_dbg = load_dbg_info(dbg_file)
    container = mtk_dbg.header.body

    for i in range(container.num_entry_info):
        if container.num_entry_info > 1:
            info = container.entry_info[i]
            print(f'# {info.unk1:#08x} {info.name} {info.unk2}')
        symbol_text(container.entry_stream.entries[i].body.symbols, remap=remap, as_functions=(not labels))

    if container.num_entry_info > 1:
        print('# WARNING: output contains symbols for multiple debug info entries (separator lines begin with "#"")')


@app.command()
def info(dbg_file: typer.FileBinaryRead):
    mtk_dbg = load_dbg_info(dbg_file)

    container = mtk_dbg.header.body

    for i in range(container.num_entry_info):
        info = container.entry_info[i]        
        entry = container.entry_stream.entries[i].body

        assert entry.files[-1].filename == ''
        assert entry.symbols[-1].symbol == ''

        print(f'{info.unk1:#08x} {info.name} {info.unk2}:\t{len(entry.files) - 1} files, {len(entry.symbols) - 1} symbols')


if __name__ == '__main__':
    app()
