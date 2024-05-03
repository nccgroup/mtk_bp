# Mediatek BP firmware tools

File formats are defined with [Kaitai](https://kaitai.io/). Files can be interactively explored with the [Kaitai IDE](https://ide.kaitai.io/) using the `ksy` files.

Using [`XT2205-1_TESLA_TMO_12_S2STS32.71-118-4-2-6-3_subsidy-TMO_UNI_RSU_QCOM_regulatory-DEFAULT_cid50_CFC.xml.zip`](https://mirrors.lolinet.com/firmware/lenomola/tesla/official/TMO/XT2205-1_TESLA_TMO_12_S2STS32.71-118-4-2-6-3_subsidy-TMO_UNI_RSU_QCOM_regulatory-DEFAULT_cid50_CFC.xml.zip) from
<https://mirrors.lolinet.com/firmware/lenomola/tesla/official/TMO/> as an example:

## Firmware image

Extract contents of `md1img.img`:

```
$ ./md1_extract.py ../XT2205-1_TESLA_TMO_12_S2STS32.71-118-4-2-6-3_subsidy-TMO_UNI_RSU_QCOM_regulatory-DEFAULT_cid50_CFC/md1img.img --outdir ./md1img_out/
extracting files to: ./md1img_out
md1rom: addr=0x00000000, size=43084864
        extracted to 000_md1rom
cert1md: addr=0x12345678, size=1781
        extracted to 001_cert1md
cert2: addr=0x12345678, size=988
        extracted to 002_cert2
md1drdi: addr=0x00000000, size=12289536
        extracted to 003_md1drdi
cert1md: addr=0x12345678, size=1781
        extracted to 004_cert1md
cert2: addr=0x12345678, size=988
        extracted to 005_cert2
md1dsp: addr=0x00000000, size=6776460
        extracted to 006_md1dsp
cert1md: addr=0x12345678, size=1781
        extracted to 007_cert1md
cert2: addr=0x12345678, size=988
        extracted to 008_cert2
md1_filter: addr=0xffffffff, size=300
        extracted to 009_md1_filter
md1_filter_PLS_PS_ONLY: addr=0xffffffff, size=300
        extracted to 010_md1_filter_PLS_PS_ONLY
md1_filter_1_Moderate: addr=0xffffffff, size=300
        extracted to 011_md1_filter_1_Moderate
md1_filter_2_Standard: addr=0xffffffff, size=300
        extracted to 012_md1_filter_2_Standard
md1_filter_3_Slim: addr=0xffffffff, size=300
        extracted to 013_md1_filter_3_Slim
md1_filter_4_UltraSlim: addr=0xffffffff, size=300
        extracted to 014_md1_filter_4_UltraSlim
md1_filter_LowPowerMonitor: addr=0xffffffff, size=300
        extracted to 015_md1_filter_LowPowerMonitor
md1_emfilter: addr=0xffffffff, size=2252
        extracted to 016_md1_emfilter
md1_dbginfodsp: addr=0xffffffff, size=1635062
        extracted to 017_md1_dbginfodsp
md1_dbginfo: addr=0xffffffff, size=1332720
        extracted to 018_md1_dbginfo
md1_mddbmeta: addr=0xffffffff, size=899538
        extracted to 019_md1_mddbmeta
md1_mddbmetaodb: addr=0xffffffff, size=562654
        extracted to 020_md1_mddbmetaodb
md1_mddb: addr=0xffffffff, size=12280622
        extracted to 021_md1_mddb
md1_mdmlayout: addr=0xffffffff, size=8341403
        extracted to 022_md1_mdmlayout
md1_file_map: addr=0xffffffff, size=889
        extracted to 023_md1_file_map
```

Firmware is in the extracted `md1rom` file (`000_md1rom`).


## Debug symbols

Takes symbols from `md1_dbginfo` (full filename given by `md1_file_map`) and outputs them in
a text format that can be imported with Ghidra's `ImportSymbolsScript.py` script.

```console
$ ./mtk_dbg_extract.py ../XT2205-1_TESLA_TMO_12_S2ST32.71-118-4-2-6_subsidy-TMO_UNI_RSU_QCOM_regulatory-DEFAULT_cid50_R1_CFC/md1_extract/mapped_files/DbgInfo_NR16.R2.MT6879.TC2.PR1.SP_LENOVO_S0MP1_K6879V1_64_MT6879_NR16_TC2_PR1_SP_V17_P38_03_24_03R_2023_05_19_22_31 | tee debug_symbols.txt
INT_Vectors 0x0000084c l
brom_ext_main 0x00000860 l
INT_SetPLL_Gen98 0x00000866 l
PLL_Set_CLK_To_26M 0x000009a2 l
PLL_MD_Pll_Init 0x000009da l
INT_SetPLL 0x000009dc l
INT_Initialize_Phase1 0x027b5c80 l
INT_Initialize_Phase2 0x027b617c l
init_cm 0x027b6384 l
init_cm_wt 0x027b641e l
...
```
