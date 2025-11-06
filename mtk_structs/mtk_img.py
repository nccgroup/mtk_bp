# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class MtkImg(KaitaiStruct):

    class GfhType(Enum):
        gfh_type_file_info = 0
        gfh_type_bl_info = 1
        gfh_type_anti_clone = 2
        gfh_type_bl_sec_key = 3
        gfh_type_brom_cfg = 7
        gfh_type_brom_sec_cfg = 8
        gfh_type_0x200 = 512
        gfh_type_rsa_maybe = 514
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.file_info = MtkImg.GfhCommonHeader(self._io, self, self._root)
        self._raw_hdrs = self._io.read_bytes((self.file_info.body.hdr_size - self.file_info.size))
        _io__raw_hdrs = KaitaiStream(BytesIO(self._raw_hdrs))
        self.hdrs = MtkImg.HeaderEntries(_io__raw_hdrs, self, self._root)
        self.code = self._io.read_bytes_full()

    class GfhRsaMaybe(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.bleh1 = self._io.read_u4be()
            self.bleh2 = self._io.read_u4be()
            self.bleh3 = self._io.read_u4be()
            self.bleh4 = self._io.read_u4be()


    class GfhCommonHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(3)
            if not self.magic == b"\x4D\x4D\x4D":
                raise kaitaistruct.ValidationNotEqualError(b"\x4D\x4D\x4D", self.magic, self._io, u"/types/gfh_common_header/seq/0")
            self.version = self._io.read_u1()
            self.size = self._io.read_u2le()
            self.type = KaitaiStream.resolve_enum(MtkImg.GfhType, self._io.read_u2le())
            _on = self.type
            if _on == MtkImg.GfhType.gfh_type_file_info:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MtkImg.GfhFileInfo(_io__raw_body, self, self._root)
            elif _on == MtkImg.GfhType.gfh_type_0x200:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MtkImg.Gfh0x200(_io__raw_body, self, self._root)
            elif _on == MtkImg.GfhType.gfh_type_rsa_maybe:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MtkImg.GfhRsaMaybe(_io__raw_body, self, self._root)
            else:
                self.body = self._io.read_bytes((self.size - 8))


    class GfhFileInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(12), 0, False)).decode(u"ascii")
            self.unused = self._io.read_u4le()
            self.file_type = self._io.read_u2le()
            self.flash_type = self._io.read_u1()
            self.sig_type = self._io.read_u1()
            self.load_addr = self._io.read_u4le()
            self.total_size = self._io.read_u4le()
            self.max_size = self._io.read_u4le()
            self.hdr_size = self._io.read_u4le()
            self.sig_size = self._io.read_u4le()
            self.jump_offset = self._io.read_u4le()
            self.processed = self._io.read_u4le()


    class HeaderEntries(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(MtkImg.GfhCommonHeader(self._io, self, self._root))
                i += 1



    class Gfh0x200(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.filename_maybe = (KaitaiStream.bytes_terminate(self._io.read_bytes(128), 0, False)).decode(u"ascii")
            self.version_maybe = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")



