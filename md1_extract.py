#!/usr/bin/env python3
import argparse
import os.path
from mtk_structs.md1img import Md1img
from kaitaistruct import KaitaiStream


def ensure_dir(path):
    if os.path.isfile(path):
        raise FileExistsError()

    return os.makedirs(path, exist_ok=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('img', type=argparse.FileType('rb'))
    parser.add_argument('--outdir', type=str, default=None)
    args = parser.parse_args()

    # make sure output directory exists or create it
    if args.outdir is not None:
        args.outdir = os.path.abspath(args.outdir)
        ensure_dir(args.outdir)
        print(f'extracting files to: {args.outdir}')

    md_img = Md1img(KaitaiStream(args.img))

    # simple name deduplication
    file_num = 0

    for section in md_img.sections:
        if type(section.body) is Md1img.EmptyBody:
            continue

        sec_hdr = section.body.sec_hdr
        fname = sec_hdr.name

        print(f'{fname}: addr={sec_hdr.maddr:#010x}, size={sec_hdr.dsize}')

        if args.outdir is not None:
            out_path = os.path.join(args.outdir, f'{file_num:03}_{os.path.basename(fname)}')
            file_num += 1
            with open(out_path, 'wb') as out_file:
                out_file.write(section.body.sec_data)
                print(f'\textracted to {os.path.basename(out_path)}')


if __name__ == '__main__':
    main()
