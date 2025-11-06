# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Md1img(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(Md1img, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.sections = []
        i = 0
        while True:
            _ = Md1img.Section(self._io, self, self._root)
            self.sections.append(_)
            if  ((_.magic != 1485313672) or (self._io.is_eof())) :
                break
            i += 1


    def _fetch_instances(self):
        pass
        for i in range(len(self.sections)):
            pass
            self.sections[i]._fetch_instances()


    class EmptyBody(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Md1img.EmptyBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Md1img.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dsize = self._io.read_u4le()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ASCII")
            self.maddr = self._io.read_u4le()
            self.mode = self._io.read_u4le()
            self.ext_magic = self._io.read_bytes(4)
            if not self.ext_magic == b"\x89\x16\x89\x58":
                raise kaitaistruct.ValidationNotEqualError(b"\x89\x16\x89\x58", self.ext_magic, self._io, u"/types/header/seq/4")
            self.hdr_size = self._io.read_u4le()
            self.hdr_version = self._io.read_u4le()
            self.img_type = self._io.read_u4le()
            self.img_list_end = self._io.read_u4le()
            self.align_size = self._io.read_u4le()
            self.dsize_extend = self._io.read_u4le()
            self.maddr_extend = self._io.read_u4le()
            self.reserved = self._io.read_bytes(self.hdr_size - 80)


        def _fetch_instances(self):
            pass


    class Section(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Md1img.Section, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.magic = self._io.read_u4le()
            _on = self.magic
            if _on == 1485313672:
                pass
                self.body = Md1img.SectionBody(self._io, self, self._root)
            else:
                pass
                self.body = Md1img.EmptyBody(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            _on = self.magic
            if _on == 1485313672:
                pass
                self.body._fetch_instances()
            else:
                pass
                self.body._fetch_instances()


    class SectionBody(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Md1img.SectionBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.sec_hdr = Md1img.Header(self._io, self, self._root)
            self.sec_data = self._io.read_bytes(self.sec_hdr.dsize)
            self.alignment = self._io.read_bytes((self.sec_hdr.align_size - self.sec_hdr.dsize) % self.sec_hdr.align_size)


        def _fetch_instances(self):
            pass
            self.sec_hdr._fetch_instances()



