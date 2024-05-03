# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Md1img(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.sections = []
        i = 0
        while not self._io.is_eof():
            self.sections.append(Md1img.Section(self._io, self, self._root))
            i += 1


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\x88\x16\x88\x58":
                raise kaitaistruct.ValidationNotEqualError(b"\x88\x16\x88\x58", self.magic, self._io, u"/types/header/seq/0")
            self.dsize = self._io.read_u4le()
            self.name = (self._io.read_bytes(32)).decode(u"ascii")
            self.maddr = self._io.read_u4le()
            self.mode = self._io.read_u4le()
            self.ext_magic = self._io.read_bytes(4)
            if not self.ext_magic == b"\x89\x16\x89\x58":
                raise kaitaistruct.ValidationNotEqualError(b"\x89\x16\x89\x58", self.ext_magic, self._io, u"/types/header/seq/5")
            self.hdr_size = self._io.read_u4le()
            self.hdr_version = self._io.read_u4le()
            self.img_type = self._io.read_u4le()
            self.img_list_end = self._io.read_u4le()
            self.align_size = self._io.read_u4le()
            self.dsize_extend = self._io.read_u4le()
            self.maddr_extend = self._io.read_u4le()
            self.reserved = self._io.read_bytes((self.hdr_size - 80))


    class Section(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sec_hdr = Md1img.Header(self._io, self, self._root)
            self.sec_data = self._io.read_bytes(self.sec_hdr.dsize)
            self.alignment = self._io.read_bytes(((self.sec_hdr.align_size - self.sec_hdr.dsize) % self.sec_hdr.align_size))



