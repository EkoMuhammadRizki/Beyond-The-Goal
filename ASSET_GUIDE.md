# 🎨 Panduan Mengganti Asset

Dokumen ini menjelaskan cara mengganti placeholder asset dengan asset final untuk game "Beyond The Goal".

## 📁 Struktur Asset

```
game/
├── images/
│   ├── characters/          # Character sprites (300x600px)
│   └── backgrounds/         # Background images (1920x1080px)
└── audio/                   # Music & sound effects
```

---

## 🎭 Character Sprites

### Spesifikasi
- **Ukuran:** 300 x 600 pixels
- **Format:** PNG dengan transparansi
- **Style:** Semi-anime modern

### Daftar Character Sprites yang Dibutuhkan

#### 1. Main Character (MC) - Pemain Utama
- `mc_neutral.png` - Ekspresi netral
- `mc_senang.png` - Ekspresi senang/tersenyum
- `mc_marah.png` - Ekspresi marah/kesal
- `mc_sedih.png` - Ekspresi sedih/kecewa
- `mc_fokus.png` - Ekspresi fokus/serius
- `mc_takut.png` - Ekspresi takut/khawatir

**Warna tema:** Hijau (#4CAF50)

#### 2. Coach Arya - Pelatih
- `coach_neutral.png` - Ekspresi netral
- `coach_senang.png` - Ekspresi senang/bangga
- `coach_marah.png` - Ekspresi marah/tegas
- `coach_fokus.png` - Ekspresi fokus/mengajar

**Warna tema:** Orange (#FF9800)
**Karakteristik:** Pria dewasa, tegas tapi ramah, memakai pakaian olahraga

#### 3. Naya - Teman Ceria
- `naya_neutral.png` - Ekspresi netral
- `naya_senang.png` - Ekspresi senang/ceria
- `naya_sedih.png` - Ekspresi sedih
- `naya_fokus.png` - Ekspresi fokus

**Warna tema:** Pink (#E91E63)
**Karakteristik:** Perempuan, ceria, energik, suportif

#### 4. Bima - Pemain Pemalu
- `bima_neutral.png` - Ekspresi netral
- `bima_senang.png` - Ekspresi senang
- `bima_sedih.png` - Ekspresi sedih
- `bima_takut.png` - Ekspresi takut/ragu
- `bima_fokus.png` - Ekspresi fokus/berani

**Warna tema:** Biru (#2196F3)
**Karakteristik:** Laki-laki, pemalu, takut gagal, berkembang menjadi berani

#### 5. Dimas - Pemain Kompetitif
- `dimas_neutral.png` - Ekspresi netral
- `dimas_senang.png` - Ekspresi senang/percaya diri
- `dimas_marah.png` - Ekspresi marah/kompetitif
- `dimas_fokus.png` - Ekspresi fokus/serius

**Warna tema:** Ungu (#9C27B0)
**Karakteristik:** Laki-laki, kompetitif, sportif, percaya diri

### Cara Mengganti
1. Buat atau siapkan sprite sesuai spesifikasi
2. Simpan dengan nama file yang sesuai
3. Letakkan di folder `game/images/characters/`
4. Game akan otomatis menggunakan sprite baru

---

## 🏞️ Background Images

### Spesifikasi
- **Ukuran:** 1920 x 1080 pixels (Full HD)
- **Format:** PNG atau JPG
- **Style:** Semi-realistis dengan nuansa anime

### Daftar Background yang Dibutuhkan

#### 1. `school_field.png`
**Deskripsi:** Lapangan sekolah sore hari
- Lapangan rumput hijau
- Gawang di kejauhan
- Langit sore (orange/kuning)
- Nuansa hangat dan nostalgia
- **Warna dominan:** Hijau (#7CB342)

#### 2. `training_cone.png`
**Deskripsi:** Area latihan dengan cone
- Lapangan dengan cone latihan tersusun
- Peralatan latihan terlihat
- Suasana siang hari
- **Warna dominan:** Hijau muda (#9CCC65)

#### 3. `wall_training.png`
**Deskripsi:** Dinding pantul untuk latihan
- Dinding beton/tembok sekolah
- Lapangan di depan dinding
- Marking untuk target latihan
- **Warna dominan:** Coklat (#8D6E63)

#### 4. `mini_field_1v1.png`
**Deskripsi:** Lapangan mini untuk 1 vs 1
- Lapangan kecil dengan garis batas
- Gawang mini di kedua sisi
- Suasana latihan
- **Warna dominan:** Hijau terang (#66BB6A)

#### 5. `mini_field_2v2.png`
**Deskripsi:** Lapangan untuk pertandingan 2 vs 2
- Lapangan lebih luas dari 1v1
- Gawang standar mini
- Suasana pertandingan
- **Warna dominan:** Hijau (#4CAF50)

#### 6. `reflection_room.png`
**Deskripsi:** Ruang refleksi/scoreboard
- Ruangan indoor atau area tenang
- Bisa berupa ruang kelas atau tribun
- Nuansa tenang untuk refleksi
- **Warna dominan:** Abu-abu biru (#455A64)

### Cara Mengganti
1. Buat atau siapkan background sesuai spesifikasi
2. Simpan dengan nama file yang sesuai
3. Letakkan di folder `game/images/backgrounds/`
4. Game akan otomatis menggunakan background baru

---

## 🎵 Audio Files

### Background Music (BGM)

#### 1. `main_menu_theme.mp3`
**Deskripsi:** Musik menu utama
- Tempo: Upbeat, hangat
- Mood: Motivasi, welcome
- Durasi: 2-3 menit (looping)
- **Genre:** Pop instrumental, acoustic

#### 2. `training_theme.mp3`
**Deskripsi:** Musik saat latihan
- Tempo: Energik, medium-fast
- Mood: Semangat, fokus
- Durasi: 2-3 menit (looping)
- **Genre:** Upbeat instrumental

#### 3. `quiz_theme.mp3`
**Deskripsi:** Musik saat mini game/quiz
- Tempo: Medium, steady
- Mood: Fokus, konsentrasi
- Durasi: 2-3 menit (looping)
- **Genre:** Electronic, puzzle music

#### 4. `final_match_theme.mp3`
**Deskripsi:** Musik pertandingan final
- Tempo: Fast, intense
- Mood: Emosional, epic
- Durasi: 2-3 menit (looping)
- **Genre:** Orchestral, sports anthem

#### 5. `reflection_theme.mp3`
**Deskripsi:** Musik refleksi
- Tempo: Slow, calm
- Mood: Tenang, reflektif, inspiratif
- Durasi: 2-3 menit (looping)
- **Genre:** Piano, ambient

### Sound Effects (SFX)

#### 1. `whistle.wav`
**Deskripsi:** Suara peluit pelatih
- Durasi: 1-2 detik
- Volume: Medium-loud

#### 2. `kick_ball.wav`
**Deskripsi:** Suara tendangan bola normal
- Durasi: 0.5-1 detik
- Volume: Medium

#### 3. `strong_kick.wav`
**Deskripsi:** Suara tendangan keras
- Durasi: 0.5-1 detik
- Volume: Loud
- Efek: Lebih powerful dari kick_ball

#### 4. `crowd_small.wav`
**Deskripsi:** Suara penonton kecil bersorak
- Durasi: 2-3 detik
- Volume: Medium
- Mood: Celebratory

#### 5. `correct.wav`
**Deskripsi:** Suara jawaban benar
- Durasi: 0.5-1 detik
- Volume: Medium
- Mood: Positive, success

#### 6. `wrong.wav`
**Deskripsi:** Suara jawaban salah
- Durasi: 0.5-1 detik
- Volume: Medium
- Mood: Negative, mistake

### Format Audio yang Didukung
- **MP3** - Untuk background music (ukuran file lebih kecil)
- **OGG** - Alternatif untuk background music
- **WAV** - Untuk sound effects (kualitas lebih baik)

### Cara Mengganti
1. Siapkan file audio sesuai spesifikasi
2. Simpan dengan nama file yang sesuai
3. Letakkan di folder `game/audio/`
4. Game akan otomatis menggunakan audio baru

---

## ✅ Checklist Asset

Gunakan checklist ini untuk memastikan semua asset sudah lengkap:

### Character Sprites
- [ ] mc_neutral.png
- [ ] mc_senang.png
- [ ] mc_marah.png
- [ ] mc_sedih.png
- [ ] mc_fokus.png
- [ ] mc_takut.png
- [ ] coach_neutral.png
- [ ] coach_senang.png
- [ ] coach_marah.png
- [ ] coach_fokus.png
- [ ] naya_neutral.png
- [ ] naya_senang.png
- [ ] naya_sedih.png
- [ ] naya_fokus.png
- [ ] bima_neutral.png
- [ ] bima_senang.png
- [ ] bima_sedih.png
- [ ] bima_takut.png
- [ ] bima_fokus.png
- [ ] dimas_neutral.png
- [ ] dimas_senang.png
- [ ] dimas_marah.png
- [ ] dimas_fokus.png

### Backgrounds
- [ ] school_field.png
- [ ] training_cone.png
- [ ] wall_training.png
- [ ] mini_field_1v1.png
- [ ] mini_field_2v2.png
- [ ] reflection_room.png

### Background Music
- [ ] main_menu_theme.mp3
- [ ] training_theme.mp3
- [ ] quiz_theme.mp3
- [ ] final_match_theme.mp3
- [ ] reflection_theme.mp3

### Sound Effects
- [ ] whistle.wav
- [ ] kick_ball.wav
- [ ] strong_kick.wav
- [ ] crowd_small.wav
- [ ] correct.wav
- [ ] wrong.wav

---

## 🎨 Tips Desain

### Character Sprites
1. **Konsistensi Style:** Pastikan semua karakter memiliki style art yang konsisten
2. **Ekspresi Jelas:** Ekspresi harus mudah dibedakan dari jarak jauh
3. **Pose Netral:** Pose netral harus bisa dikombinasikan dengan berbagai background
4. **Transparansi:** Gunakan background transparan untuk fleksibilitas

### Backgrounds
1. **Depth of Field:** Gunakan blur ringan di background untuk fokus pada karakter
2. **Lighting:** Perhatikan konsistensi lighting antar scene
3. **Color Palette:** Gunakan warna hangat untuk suasana friendly dan motivational
4. **Detail:** Jangan terlalu detail agar tidak mengalihkan perhatian dari dialog

### Audio
1. **Looping:** Pastikan BGM bisa loop seamlessly
2. **Volume Balance:** Seimbangkan volume antar track
3. **Fade In/Out:** Gunakan fade untuk transisi yang smooth
4. **Quality:** Gunakan bitrate minimal 192kbps untuk MP3

---

## 🔧 Testing Asset

Setelah mengganti asset:

1. **Jalankan Game:** Launch game dari Ren'Py Launcher
2. **Cek Visual:** Pastikan semua sprite dan background muncul dengan benar
3. **Cek Audio:** Test semua BGM dan SFX
4. **Cek Transisi:** Pastikan transisi antar scene smooth
5. **Cek Ekspresi:** Test semua ekspresi karakter di berbagai scene

---

## 📞 Troubleshooting

### Sprite Tidak Muncul
- Cek nama file (case-sensitive)
- Cek format file (harus PNG)
- Cek lokasi file (harus di `game/images/characters/`)

### Background Tidak Muncul
- Cek nama file sesuai dengan definisi di code
- Cek ukuran file (jangan terlalu besar, max 5MB)
- Cek format file (PNG atau JPG)

### Audio Tidak Terdengar
- Cek format file (MP3, OGG, atau WAV)
- Cek nama file sesuai dengan definisi di `audio.rpy`
- Cek volume di preferences game
- Cek lokasi file (harus di `game/audio/`)

---

## 📚 Resource Rekomendasi

### Free Asset Resources
- **Character Sprites:** Vroid Studio, Character Creator
- **Backgrounds:** Unsplash, Pexels (dengan editing)
- **Music:** Incompetech, Purple Planet Music
- **Sound Effects:** Freesound.org, Zapsplat

### Paid Asset Resources
- **Character Sprites:** Fiverr, ArtStation
- **Backgrounds:** Shutterstock, Adobe Stock
- **Music:** AudioJungle, Epidemic Sound
- **Sound Effects:** AudioJungle, Soundsnap

---

**Selamat berkarya! 🎨🎵**
