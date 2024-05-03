meta:
  id: mtk_dbg_info
  file-extension: mtk_dbg_info
  encoding: ascii
  endian: le

seq:
  - id: header
    type: dbg_header

  - id: body
    type: dbg_body
    size: header.size - 0x10 - 1  # minus length of header


types:

  addr_pair:
    seq:
      - id: addr1
        type: u4
      - id: addr2
        type: u4

  dbg_header:
    seq:
      - id: magic1
        contents: "CATI"
      - id: magic2
        contents: "CTNR"
      - id: unk1
        type: u4
      - id: size
        type: u4

  dbg_body:
    seq:
      - id: magic3
        contents: "CATI"
      - id: unk2
        type: u4
      - id: unk3
        type: u4
      - id: unk_str1
        type: strz
      - id: unk_str2
        type: strz
      - id: unk_str3
        type: strz
      - id: date_str
        type: strz
      - id: unk4
        type: u4
      - id: unk5
        type: u4

      - id: symbols
        size: unk5 - unk4 - 1
        type: symbol_entries
        
      - id: separator
        size: 1
        
      - id: files
        type: file_entry
        repeat: eos

  symbol_entry:
    seq:
      - id: symbol
        type: strz
      - id: addrs
        type: addr_pair

  symbol_entries:
    seq:
      - id: entries
        type: symbol_entry
        repeat: eos

  file_entry:
    seq:
      - id: filename
        type: strz
      - id: num_addr_pairs
        type: u4
      - id: addr_pairs
        type: addr_pair
        repeat: expr
        repeat-expr: num_addr_pairs
  