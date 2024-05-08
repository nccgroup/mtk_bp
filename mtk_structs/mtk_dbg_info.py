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
        self.header = MtkDbgInfo.CatiHeader(self._io, self, self._root)

    class EmptyBody(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass


    class CatiDebugDsp(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unk3 = self._io.read_u4le()
            self.unk_str1 = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self.unk_str2 = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self.unk_str3 = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self.date_str = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self.symbols_start = self._io.read_u4le()
            self.files_start = self._io.read_u4le()
            self.symbols = []
            i = 0
            while True:
                _ = MtkDbgInfo.SymbolEntry(self._io, self, self._root)
                self.symbols.append(_)
                if _.symbol == u"":
                    break
                i += 1
            self.files = []
            i = 0
            while True:
                _ = MtkDbgInfo.FileEntryDsp(self._io, self, self._root)
                self.files.append(_)
                if _.filename == u"":
                    break
                i += 1


    class FileEntryDsp(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.filename = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            _on = self.filename
            if _on == u"":
                self.body = MtkDbgInfo.EmptyBody(self._io, self, self._root)
            else:
                self.body = MtkDbgInfo.FileEntryDspBody(self._io, self, self._root)


    class SymbolEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.symbol = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            _on = self.symbol
            if _on == u"":
                self.body = MtkDbgInfo.EmptyBody(self._io, self, self._root)
            else:
                self.body = MtkDbgInfo.SymbolEntryBody(self._io, self, self._root)


    class FileEntryDspBody(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_addr_pairs = self._io.read_u4le()
            self.addr_pairs = []
            for i in range(self.num_addr_pairs):
                self.addr_pairs.append(MtkDbgInfo.AddrTriplet(self._io, self, self._root))



    class ContainerEntryInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unk1 = self._io.read_u4le()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self.unk2 = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")


    class CatiContainer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unk1 = self._io.read_u4le()
            self.size = self._io.read_u4le()
            self._raw_entry_stream = self._io.read_bytes((self.size - 16))
            _io__raw_entry_stream = KaitaiStream(BytesIO(self._raw_entry_stream))
            self.entry_stream = MtkDbgInfo.CatiHeaders(_io__raw_entry_stream, self, self._root)
            self.num_entry_info = self._io.read_u4le()
            self.entry_info = []
            for i in range(self.num_entry_info):
                self.entry_info.append(MtkDbgInfo.ContainerEntryInfo(self._io, self, self._root))



    class FileEntryBody(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_addr_pairs = self._io.read_u4le()
            self.addr_pairs = []
            for i in range(self.num_addr_pairs):
                self.addr_pairs.append(MtkDbgInfo.AddrPair(self._io, self, self._root))



    class CatiHeaders(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(MtkDbgInfo.CatiHeader(self._io, self, self._root))
                i += 1



    class AddrTriplet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.addr1 = self._io.read_u4le()
            self.addr2 = self._io.read_u4le()
            self.addr3 = self._io.read_u4le()


    class CatiHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\x43\x41\x54\x49":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x41\x54\x49", self.magic, self._io, u"/types/cati_header/seq/0")
            self.cati_type = self._io.read_u4le()
            _on = self.cati_type
            if _on == 1380865091:
                self.body = MtkDbgInfo.CatiContainer(self._io, self, self._root)
            elif _on == 1:
                self.body = MtkDbgInfo.CatiDebug(self._io, self, self._root)
            elif _on == 2:
                self.body = MtkDbgInfo.CatiDebugDsp(self._io, self, self._root)


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
            _on = self.filename
            if _on == u"":
                self.body = MtkDbgInfo.EmptyBody(self._io, self, self._root)
            else:
                self.body = MtkDbgInfo.FileEntryBody(self._io, self, self._root)


    class SymbolEntryBody(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.addrs = MtkDbgInfo.AddrPair(self._io, self, self._root)


    class CatiDebug(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unk3 = self._io.read_u4le()
            self.unk_str1 = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self.unk_str2 = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self.unk_str3 = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self.date_str = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self.symbols_start = self._io.read_u4le()
            self.files_start = self._io.read_u4le()
            self.symbols = []
            i = 0
            while True:
                _ = MtkDbgInfo.SymbolEntry(self._io, self, self._root)
                self.symbols.append(_)
                if _.symbol == u"":
                    break
                i += 1
            self.files = []
            i = 0
            while True:
                _ = MtkDbgInfo.FileEntry(self._io, self, self._root)
                self.files.append(_)
                if _.filename == u"":
                    break
                i += 1



