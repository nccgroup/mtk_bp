meta:
  id: md1img
  file-extension: md1img
  endian: le

seq:
  - id: sections
    type: section
    repeat: until
    repeat-until: _.magic != 0x58881688

types:

  empty_body: {}

  header:
    seq:
      - id: dsize
        type: u4
      - id: name
        type: strz
        encoding: ASCII
        size: 32
      - id: maddr
        type: u4
      - id: mode
        type: u4
      - id: ext_magic
        # 0x58891689
        contents: [0x89, 0x16, 0x89, 0x58]
      - id: hdr_size
        type: u4
      - id: hdr_version
        type: u4
      - id: img_type
        type: u4
      - id: img_list_end
        type: u4
      - id: align_size
        type: u4
      - id: dsize_extend
        type: u4
      - id: maddr_extend
        type: u4
      - id: reserved
        size: hdr_size - 0x50

  section:
    seq:
      - id: magic
        type: u4
      - id: body
        type:
          switch-on: magic
          cases:
            0x58881688: section_body
            _: empty_body

  section_body:
    seq:
      - id: sec_hdr
        type: header
      - id: sec_data
        size: sec_hdr.dsize
      - id: alignment
        size: (sec_hdr.align_size - sec_hdr.dsize) % sec_hdr.align_size
