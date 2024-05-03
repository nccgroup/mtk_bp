# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class MtkDbgInfo(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = MtkDbgInfo.DbgHeader(self._io, self, self._root)
        self._raw_body = self._io.read_bytes(((self.header.size - 16) - 1))
        _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
        self.body = MtkDbgInfo.DbgBody(_io__raw_body, self, self._root)

    class SymbolEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.symbol = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self.addrs = MtkDbgInfo.AddrPair(self._io, self, self._root)


    class SymbolEntries(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(MtkDbgInfo.SymbolEntry(self._io, self, self._root))
                i += 1



    class AddrPair(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.addr1 = self._io.read_u4le()
            self.addr2 = self._io.read_u4le()


    class FileEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.filename = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self.num_addr_pairs = self._io.read_u4le()
            self.addr_pairs = []
            for i in range(self.num_addr_pairs):
                self.addr_pairs.append(MtkDbgInfo.AddrPair(self._io, self, self._root))



    class DbgHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic1 = self._io.read_bytes(4)
            if not self.magic1 == b"\x43\x41\x54\x49":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x41\x54\x49", self.magic1, self._io, u"/types/dbg_header/seq/0")
            self.magic2 = self._io.read_bytes(4)
            if not self.magic2 == b"\x43\x54\x4E\x52":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x54\x4E\x52", self.magic2, self._io, u"/types/dbg_header/seq/1")
            self.unk1 = self._io.read_u4le()
            self.size = self._io.read_u4le()


    class DbgBody(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic3 = self._io.read_bytes(4)
            if not self.magic3 == b"\x43\x41\x54\x49":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x41\x54\x49", self.magic3, self._io, u"/types/dbg_body/seq/0")
            self.unk2 = self._io.read_u4le()
            self.unk3 = self._io.read_u4le()
            self.unk_str1 = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self.unk_str2 = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self.unk_str3 = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self.date_str = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self.unk4 = self._io.read_u4le()
            self.unk5 = self._io.read_u4le()
            self._raw_symbols = self._io.read_bytes(((self.unk5 - self.unk4) - 1))
            _io__raw_symbols = KaitaiStream(BytesIO(self._raw_symbols))
            self.symbols = MtkDbgInfo.SymbolEntries(_io__raw_symbols, self, self._root)
            self.separator = self._io.read_bytes(1)
            self.files = []
            i = 0
            while not self._io.is_eof():
                self.files.append(MtkDbgInfo.FileEntry(self._io, self, self._root))
                i += 1




