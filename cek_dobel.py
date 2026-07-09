import json

# 1. Baca file json
with open('whitelist.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

password = data['password']
allowed_ids = data['allowed_ids']

print(f"Total ID sebelum: {len(allowed_ids)}")

# 2. Cari ID dobel
seen = set()
dobel = []
for id in allowed_ids:
    if id in seen:
        dobel.append(id)
    else:
        seen.add(id)

if dobel:
    print(f"Ada {len(set(dobel))} ID dobel: {list(set(dobel))}")
else:
    print("Tidak ada ID dobel ✅")

# 3. Buat list baru tanpa dobel, urutan tetap dijaga
allowed_ids_bersih = list(dict.fromkeys(allowed_ids))

print(f"Total ID sesudah: {len(allowed_ids_bersih)}")

# 4. Simpan ke file baru
data_baru = {
    "password": password,
    "allowed_ids": allowed_ids_bersih
}

with open('whitelist_bersih.json', 'w', encoding='utf-8') as f:
    json.dump(data_baru, f, indent=2)

print("Selesai! File disimpan sebagai: whitelist_bersih.json")