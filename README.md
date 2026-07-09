# Password Whitelist Checker

Script Python buat ngecek dan hapus ID dobel di file `member.json`.

## Cara Pakai
1. `python cek_dobel.py`
2. Hasilnya ada di `whitelist_bersih.json`

## Struktur member.json
{
  "password": "cimangcuvip",
  "allowed_ids": ["id1", "id2"]
}

## Fitur
- Cek ID dobel
- Hapus otomatis ID dobel
- Urutan ID tetap
