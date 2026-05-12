# 🚀 Quick Start Guide

Panduan cepat untuk menjalankan dan mengembangkan game "Beyond The Goal".

## 📋 Prerequisites

- **Ren'Py SDK 8.0+** - [Download di sini](https://www.renpy.org/latest.html)
- **Windows/Mac/Linux** - Game support semua platform
- **Minimal 2GB RAM** - Untuk menjalankan Ren'Py SDK
- **500MB Free Space** - Untuk project dan SDK

## ⚡ Quick Start (5 Menit)

### 1. Install Ren'Py SDK

```bash
# Download Ren'Py SDK dari renpy.org
# Extract ke folder pilihan Anda
# Jalankan renpy.exe (Windows) atau renpy.sh (Mac/Linux)
```

### 2. Load Project

1. Buka **Ren'Py Launcher**
2. Klik **"+ Add Existing Project"** atau **"Projects"** > **"Add Existing Project"**
3. Navigate ke folder **"Beyond The Goal"**
4. Klik **"Select Folder"**

### 3. Launch Game

1. Pilih project **"Beyond The Goal"** di launcher
2. Klik **"Launch Project"**
3. Game akan terbuka dan siap dimainkan!

## 🎮 Cara Bermain

### Controls
- **Left Click / Enter** - Advance dialog
- **Right Click / Esc** - Open menu
- **Scroll Up** - Rollback (lihat dialog sebelumnya)
- **Ctrl** - Skip dialog
- **Tab** - Toggle skip mode
- **S** - Screenshot
- **H** - Hide UI

### Menu Utama
- **Mulai Bermain** - Mulai game dari awal
- **Chapter Select** - Pilih chapter (unlock setelah selesai)
- **Gallery Materi** - Review materi pembelajaran
- **Load Game** - Load saved game
- **Pengaturan** - Settings (volume, fullscreen, dll)
- **Keluar** - Exit game

### Gameplay Tips
1. **Baca dengan teliti** - Setiap pilihan mempengaruhi skor
2. **Perhatikan HUD** - Lihat perkembangan skor di pojok kanan atas
3. **Coba berbagai pilihan** - Setiap pilihan memberi pengalaman berbeda
4. **Selesaikan mini game** - Untuk unlock materi di gallery
5. **Refleksi di akhir chapter** - Pelajari ringkasan pembelajaran

## 🛠️ Development Mode

### Edit Script

1. Buka Ren'Py Launcher
2. Pilih project "Beyond The Goal"
3. Klik **"script.rpy"** atau file lain di daftar
4. Edit menggunakan text editor favorit Anda
5. Save file
6. Klik **"Reload"** di game (Shift+R) atau restart game

### File Structure

```
game/
├── script.rpy              # Main entry point
├── chapter1.rpy            # Chapter 1 content
├── chapter2.rpy            # Chapter 2 content
├── chapter3.rpy            # Chapter 3 content
├── characters.rpy          # Character definitions
├── variables.rpy           # Game variables
├── custom_screens.rpy     # UI screens
└── ...
```

### Modifikasi Mudah

#### Ubah Dialog
Edit file `chapter1.rpy`, `chapter2.rpy`, atau `chapter3.rpy`:
```python
coach "Dialog baru di sini"
```

#### Tambah Pilihan
```python
menu:
    "Pilihan baru 1":
        # Code untuk pilihan 1
        
    "Pilihan baru 2":
        # Code untuk pilihan 2
```

#### Ubah Skor
```python
$ add_teknik(10)        # Tambah teknik +10
$ add_percaya_diri(5)   # Tambah percaya diri +5
$ add_sportivitas(15)   # Tambah sportivitas +15
```

## 🎨 Mengganti Asset

### Character Sprites

1. Buat PNG 300x600 pixels
2. Simpan di `game/images/characters/`
3. Nama file: `[karakter]_[ekspresi].png`
   - Contoh: `mc_senang.png`, `coach_neutral.png`

### Backgrounds

1. Buat PNG/JPG 1920x1080 pixels
2. Simpan di `game/images/backgrounds/`
3. Nama file sesuai definisi di code
   - Contoh: `school_field.png`, `training_cone.png`

### Audio

1. Siapkan file MP3/OGG/WAV
2. Simpan di `game/audio/`
3. Nama file sesuai definisi di `audio.rpy`

**Lihat ASSET_GUIDE.md untuk detail lengkap**

## 🐛 Troubleshooting

### Game Tidak Mau Launch

**Problem:** Error saat launch game

**Solution:**
1. Pastikan Ren'Py SDK versi 8.0+
2. Check console error di Ren'Py Launcher
3. Pastikan semua file .rpy tidak ada syntax error
4. Coba "Force Recompile" di launcher

### Audio Tidak Terdengar

**Problem:** Tidak ada suara

**Solution:**
1. Check volume di preferences game
2. Check volume system
3. Audio files optional - game tetap jalan tanpa audio
4. Tambahkan file audio ke `game/audio/` jika ingin ada suara

### Image Tidak Muncul

**Problem:** Character atau background tidak tampil

**Solution:**
1. Ini normal - game menggunakan placeholder
2. Placeholder = solid color
3. Untuk image asli, tambahkan ke folder `game/images/`
4. Check nama file sesuai dengan definisi di code

### Error "File Not Found"

**Problem:** Error file tidak ditemukan

**Solution:**
1. Check path file (case-sensitive di Mac/Linux)
2. Pastikan file ada di lokasi yang benar
3. Untuk audio/image, game akan fallback ke placeholder
4. Check typo di nama file

## 📚 Learning Resources

### Ren'Py Documentation
- [Official Ren'Py Documentation](https://www.renpy.org/doc/html/)
- [Ren'Py Quickstart](https://www.renpy.org/doc/html/quickstart.html)
- [Ren'Py Tutorial](https://www.renpy.org/doc/html/tutorial.html)

### Community
- [Ren'Py Forums](https://lemmasoft.renai.us/forums/)
- [Ren'Py Discord](https://discord.gg/renpy)
- [r/RenPy Reddit](https://www.reddit.com/r/RenPy/)

### Tutorials
- [Ren'Py Cookbook](https://www.renpy.org/wiki/renpy/doc/cookbook)
- [Visual Novel Design](https://vndb.org/)

## 🔧 Advanced Features

### Build Distribution

1. Buka Ren'Py Launcher
2. Pilih project "Beyond The Goal"
3. Klik **"Build Distributions"**
4. Pilih platform (Windows, Mac, Linux, Android)
5. Klik **"Build"**
6. File distribusi akan ada di folder `Beyond The Goal-dists/`

### Add New Chapter

1. Buat file baru: `game/chapter4.rpy`
2. Tambahkan label:
```python
label ch4_intro:
    # Chapter 4 content
    return
```
3. Update `script.rpy` untuk link ke chapter baru
4. Update `custom_screens.rpy` untuk chapter select

### Custom Mini Game

1. Buat label baru di chapter file
2. Gunakan menu untuk choices
3. Track score dengan variables
4. Berikan feedback dengan text/sound

Contoh:
```python
label custom_minigame:
    $ score = 0
    
    menu:
        "Pilihan 1":
            $ score += 10
        "Pilihan 2":
            $ score += 5
    
    if score >= 10:
        "Bagus!"
    else:
        "Coba lagi!"
    
    return
```

## 💡 Tips & Tricks

### Development
1. **Use Shift+R** untuk reload script tanpa restart
2. **Use Shift+D** untuk developer menu
3. **Use Shift+O** untuk console (debug)
4. **Save often** saat edit script
5. **Test setiap perubahan** sebelum commit

### Writing
1. **Keep dialog natural** - Tulis seperti orang berbicara
2. **Show, don't tell** - Gunakan action dan emotion
3. **Vary sentence length** - Mix pendek dan panjang
4. **Use character voice** - Setiap karakter punya style
5. **Test choices** - Pastikan semua path masuk akal

### Design
1. **Consistent style** - Semua asset harus matching
2. **Readable text** - Pastikan text mudah dibaca
3. **Clear choices** - Pilihan harus jelas maksudnya
4. **Feedback** - Berikan feedback untuk setiap action
5. **Pacing** - Jangan terlalu cepat atau lambat

## 🎯 Next Steps

1. ✅ **Play the game** - Mainkan semua chapter
2. ✅ **Read the code** - Pelajari struktur script
3. ✅ **Modify dialog** - Coba edit beberapa dialog
4. ✅ **Add choices** - Tambahkan pilihan baru
5. ✅ **Replace assets** - Ganti placeholder dengan asset asli
6. ✅ **Build distribution** - Buat executable untuk share

## 📞 Need Help?

- **Check README.md** - Dokumentasi lengkap
- **Check ASSET_GUIDE.md** - Panduan asset
- **Check code comments** - Inline documentation
- **Ren'Py Forums** - Community support
- **Create Issue** - Report bugs atau request features

---

**Selamat mengembangkan! 🎮⚽**

*"Beyond The Goal - Menang bukan hanya tentang mencetak gol"*
