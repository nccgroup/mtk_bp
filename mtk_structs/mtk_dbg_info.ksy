meta:
  id: mtk_dbg_info
  file-extension: mtk_dbg_info
  encoding: ascii
  endian: le

seq:
  - id: header
    type: cati_header

types:

  empty_body: {}
  
  container_entry_info:
    seq:
      - id: unk1
        type: u4
      - id: name
        type: strz
      - id: unk2
        type: strz

  cati_header:
    seq:
      - id: magic
        contents: "CATI"
      - id: cati_type
        type: u4

      - id: body
        type:
          switch-on: cati_type
          cases:
            0x524E5443: cati_container  # "CTNR"
            1: cati_debug
            2: cati_debug_dsp
            
  cati_headers:
    seq:
      - id: entries
        type: cati_header
        repeat: eos

  cati_container:
    seq:
      - id: unk1
        type: u4
      - id: size
        type: u4
      - id: entry_stream
        type: cati_headers
        size: size - 0x10
      - id: num_entry_info
        type: u4
      - id: entry_info
        type: container_entry_info
        repeat: expr
        repeat-expr: num_entry_info

  cati_debug:
    seq:
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
      - id: symbols_start
        type: u4
      - id: files_start
        type: u4

      - id: symbols
        type: symbol_entry
        repeat: until
        repeat-until: _.symbol == ""
        
      - id: files
        type: file_entry
        repeat: until
        repeat-until: _.filename == ""

  cati_debug_dsp:
    seq:
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
      - id: symbols_start
        type: u4
      - id: files_start
        type: u4

      - id: symbols
        type: symbol_entry
        repeat: until
        repeat-until: _.symbol == ""
        
      - id: files
        type: file_entry_dsp
        repeat: until
        repeat-until: _.filename == ""

  addr_pair:
    seq:
      - id: addr1
        type: u4
      - id: addr2
        type: u4
  
  addr_triplet:
    seq:
      - id: addr1
        type: u4
      - id: addr2
        type: u4
      - id: addr3
        type: u4

  symbol_entry_body:
    seq:
      - id: addrs
        type: addr_pair

  symbol_entry:
    seq:
      - id: symbol
        type: strz
      - id: body
        type:
          switch-on: symbol
          cases:
            '""': empty_body
            _: symbol_entry_body

  file_entry_body:
    seq:
      - id: num_addr_pairs
        type: u4
      - id: addr_pairs
        type: addr_pair
        repeat: expr
        repeat-expr: num_addr_pairs

  file_entry:
    seq:
      - id: filename
        type: strz
      - id: body
        type:
          switch-on: filename
          cases:
            '""': empty_body
            _: file_entry_body

  file_entry_dsp_body:
    seq:
      - id: num_addr_pairs
        type: u4
      - id: addr_pairs
        type: addr_triplet
        repeat: expr
        repeat-expr: num_addr_pairs

  file_entry_dsp:
    seq:
      - id: filename
        type: strz
      - id: body
        type:
          switch-on: filename
          cases:
            '""': empty_body
            _: file_entry_dsp_body
