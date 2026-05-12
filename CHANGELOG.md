# Changelog

Semua perubahan penting pada project "Beyond The Goal" akan didokumentasikan di file ini.

## [1.0.0] - 2026-05-12

### ✨ Fitur Utama
- **3 Chapter Lengkap** dengan cerita interaktif
  - Chapter 1: Umpan Pertama di Lapangan Senja (Teknik Menendang)
  - Chapter 2: Bola yang Tidak Mau Diam (Kontrol & Dribbling)
  - Chapter 3: Sundulan Penentu (Heading & Teamwork)

- **Sistem Karakter**
  - 5 karakter dengan multiple expressions
  - Nama pemain dapat disesuaikan (Raka/Rani)
  - Dialog interaktif dengan branching choices

- **Mini Game Interaktif**
  - Chapter 1: Kick Selector Quiz
  - Chapter 2: Control & Dribble Match (dengan combo system)
  - Chapter 3: Final Small Match Quiz

- **Sistem Skor & Perkembangan**
  - Tracking Teknik, Percaya Diri, dan Sportivitas
  - HUD display di pojok kanan atas
  - Player Style System (Technical, Supportive, Brave, Balanced)
  - Reflection screen di akhir setiap chapter

- **UI/UX Custom**
  - Main Menu dengan tema sepak bola
  - Chapter Select Screen (unlock progressive)
  - Gallery Materi untuk review pembelajaran
  - Custom color scheme (hijau lapangan)

- **Placeholder System**
  - Auto-fallback untuk missing images
  - Solid color placeholders untuk character sprites
  - Solid color placeholders untuk backgrounds
  - Game tetap playable tanpa asset final

### 📚 Materi Edukasi
- Teknik menendang bola (kaki dalam, luar, punggung)
- Kontrol bola (telapak kaki, dada, paha)
- Dribbling dengan kontrol
- Teknik heading yang aman
- Kerja sama tim dan sportivitas

### 🎮 Gameplay Features
- Branching narrative dengan multiple choices
- Consequence system yang mempengaruhi skor
- Autosave setelah setiap chapter
- Multiple endings berdasarkan player style
- Gallery unlock system

### 🎨 Visual & Audio
- Character sprite system dengan 6 expressions
- 6 background locations
- Background music system (5 tracks)
- Sound effects (6 SFX)
- Custom transitions dan effects

### 📖 Dokumentasi
- README.md lengkap dengan panduan
- ASSET_GUIDE.md untuk replacement asset
- Inline comments di semua script files
- Struktur modular dan mudah dikembangkan

### 🔧 Technical
- Ren'Py 8.0+ compatible
- Modular file structure
- Clean code dengan comments
- Error handling untuk missing assets
- Cross-platform support (Windows/Mac/Linux)

### 📁 File Structure
```
game/
├── script.rpy              # Main script & opening
├── characters.rpy          # Character definitions
├── variables.rpy           # Game variables
├── audio.rpy               # Audio definitions
├── chapter1.rpy            # Chapter 1 content
├── chapter2.rpy            # Chapter 2 content
├── chapter3.rpy            # Chapter 3 content
├── custom_screens.rpy     # Custom UI screens
├── generate_placeholders.rpy  # Placeholder system
├── hud_system.rpy          # HUD & effects
├── gui.rpy                 # GUI configuration
└── options.rpy             # Game options
```

## Rencana Pengembangan

### [1.1.0] - Future
- [ ] Tambahan chapter bonus
- [ ] Achievement system
- [ ] Leaderboard untuk mini game scores
- [ ] More character interactions
- [ ] Voice acting support

### [1.2.0] - Future
- [ ] Multiplayer quiz mode
- [ ] Custom character creator
- [ ] More mini games
- [ ] Mobile optimization
- [ ] Translation support (English, etc.)

## Known Issues

### Current Version
- Audio files belum tersedia (menggunakan placeholder)
- Character sprites menggunakan solid color placeholder
- Backgrounds menggunakan solid color placeholder

### Workarounds
- Game tetap fully playable tanpa asset
- Placeholder system memastikan no crashes
- Asset dapat ditambahkan kapan saja tanpa code changes

## Credits

**Game Design & Development**
- Visual Novel Engine: Ren'Py
- Game Concept: Educational Football/Soccer Training
- Target Audience: High School Students (SMA)

**Educational Content**
- Football/Soccer basic techniques
- Character development themes
- Teamwork and sportsmanship values

---

**Format:** [Version] - Date
**Types of Changes:**
- ✨ Added - New features
- 🔧 Changed - Changes in existing functionality
- 🐛 Fixed - Bug fixes
- 🗑️ Removed - Removed features
- 📚 Documentation - Documentation changes
