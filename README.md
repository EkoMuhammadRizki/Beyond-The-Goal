# Beyond The Goal
**Visual Novel Edukasi Sepak Bola untuk Siswa SMA**

## 📖 Tentang Game

"Beyond The Goal" adalah visual novel edukasi berbasis Ren'Py yang mengajarkan teknik dasar sepak bola melalui cerita interaktif yang menarik. Game ini menggabungkan pembelajaran teknik olahraga dengan pengembangan karakter seperti percaya diri, kerja sama tim, dan sportivitas.

### Tagline
*"Menang bukan hanya tentang mencetak gol, tapi tentang belajar, percaya diri, dan bermain bersama."*

### Filosofi Game
- Kesalahan adalah bagian dari proses belajar
- Teknik dapat dipahami dan dilatih, bukan bakat semata
- Kerja sama tim lebih penting daripada bermain egois
- Sportivitas dan keberanian membantu teman adalah inti perkembangan karakter
- Menguasai bola berarti juga belajar menguasai emosi dan rasa takut

## 🎮 Fitur Game

### Gameplay
- **3 Chapter Utama** dengan cerita berbeda
- **Branching Choices** yang mempengaruhi perkembangan karakter
- **Mini Game Interaktif** di setiap chapter
- **Sistem Skor** untuk tracking perkembangan:
  - Teknik
  - Percaya Diri
  - Sportivitas
- **Multiple Endings** berdasarkan pilihan pemain
- **Gallery Materi** untuk review pembelajaran

### Karakter
1. **Pemain Utama (Raka/Rani)** - Karakter yang dapat disesuaikan
2. **Coach Arya** - Pelatih tegas namun ramah
3. **Naya** - Teman ceria dan suportif
4. **Bima** - Pemain pemalu yang takut gagal
5. **Dimas** - Pemain kompetitif namun sportif

## 📚 Materi Pembelajaran

### Chapter 1: Umpan Pertama di Lapangan Senja
**Materi:**
- Dasar sepak bola
- Peran pemain
- Teknik menendang:
  - Kaki bagian dalam
  - Kaki bagian luar
  - Punggung kaki

**Mini Game:** Kick Selector Quiz

### Chapter 2: Bola yang Tidak Mau Diam
**Materi:**
- Kontrol bola (telapak kaki, dada, paha)
- Dribbling
- Kontrol kaki bagian dalam & luar

**Mini Game:** Control & Dribble Match

### Chapter 3: Sundulan Penentu
**Materi:**
- Teknik heading
- Permainan kecil (1v1, 2v2)
- Kerja sama tim
- Sportivitas

**Mini Game:** Final Small Match Quiz

## 🎨 Style & Presentasi

- **Visual Style:** Semi-anime modern dengan atmosfer hangat dan sporty
- **Nuansa:** Warm coming-of-age, slice-of-life sekolah
- **Target:** Siswa SMP/SMA, penggemar visual novel, pembelajaran PJOK

## 🛠️ Struktur Project

```
Beyond The Goal/
├── game/
│   ├── script.rpy              # Main script & opening
│   ├── characters.rpy          # Definisi karakter & sprites
│   ├── variables.rpy           # Game variables & helper functions
│   ├── audio.rpy               # Audio definitions
│   ├── chapter1.rpy            # Chapter 1: Teknik Menendang
│   ├── chapter2.rpy            # Chapter 2: Kontrol & Dribbling
│   ├── chapter3.rpy            # Chapter 3: Heading & Teamwork
│   ├── custom_screens.rpy     # Custom UI screens
│   ├── generate_placeholders.rpy  # Placeholder system
│   ├── images/
│   │   ├── characters/         # Character sprites
│   │   └── backgrounds/        # Background images
│   └── audio/                  # Music & sound effects
└── README.md
```

## 🚀 Cara Menjalankan

### Requirement
- Ren'Py SDK 8.0 atau lebih baru
- Windows/Mac/Linux

### Langkah-langkah
1. Download dan install Ren'Py SDK dari [renpy.org](https://www.renpy.org/)
2. Clone atau download project ini
3. Buka Ren'Py Launcher
4. Klik "Add Existing Project" dan pilih folder "Beyond The Goal"
5. Klik "Launch Project" untuk menjalankan game

## 🎯 Player Style System

Game akan menentukan style bermain pemain berdasarkan pilihan:

- **Technical Player** - Fokus pada pemahaman teknik dan strategi
- **Supportive Player** - Membuat tim menjadi lebih baik
- **Brave Learner** - Berani mencoba dan belajar dari kesalahan
- **Balanced Captain** - Seimbang dalam semua aspek

## 📝 Placeholder System

Project ini menggunakan sistem placeholder otomatis:
- **Character sprites** menggunakan Solid color dengan warna berbeda untuk setiap karakter
- **Backgrounds** menggunakan Solid color sesuai tema lokasi
- **Audio** dapat ditambahkan ke folder `game/audio/`

Semua placeholder dapat diganti dengan asset final tanpa mengubah kode.

## 🔧 Customization

### Mengganti Character Sprites
1. Buat image PNG dengan ukuran 300x600 pixels
2. Simpan di `game/images/characters/`
3. Gunakan naming convention: `[nama]_[ekspresi].png`
   - Contoh: `mc_senang.png`, `coach_neutral.png`

### Mengganti Backgrounds
1. Buat image PNG dengan ukuran 1920x1080 pixels
2. Simpan di `game/images/backgrounds/`
3. Gunakan nama sesuai definisi di `characters.rpy`

### Menambahkan Audio
1. Simpan file audio di `game/audio/`
2. Format yang didukung: MP3, OGG, WAV
3. Nama file harus sesuai dengan definisi di `audio.rpy`

## 📊 Sistem Skor

Game melacak 3 aspek perkembangan:
- **Teknik** - Pemahaman teknik sepak bola
- **Percaya Diri** - Keberanian mencoba dan mengambil keputusan
- **Sportivitas** - Kerja sama tim dan kepedulian pada teman

Skor ditampilkan di HUD pojok kanan atas dan di reflection screen setiap chapter.

## 🎓 Target Pendidikan

Game ini cocok untuk:
- Pembelajaran PJOK interaktif
- Media edukasi sepak bola untuk pemula
- Pengembangan karakter siswa
- Game edukasi sekolah

## 📜 License

Project ini dibuat untuk tujuan edukasi. Silakan modifikasi dan kembangkan sesuai kebutuhan.

## 🤝 Kontribusi

Untuk menambahkan fitur atau memperbaiki bug:
1. Fork repository ini
2. Buat branch baru untuk fitur Anda
3. Commit perubahan Anda
4. Submit pull request

## 📞 Support

Jika ada pertanyaan atau masalah, silakan buat issue di repository ini.

---

**Dibuat dengan ❤️ menggunakan Ren'Py**

*"Tidak semua pemain menjadi pencetak gol terbaik. Tapi setiap pemain bisa menjadi alasan timnya terus bermain."*
