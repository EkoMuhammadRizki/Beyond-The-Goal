# 🔧 Troubleshooting Guide

Panduan mengatasi masalah umum saat menggunakan "Beyond The Goal".

---

## 📋 Table of Contents

- [Installation Issues](#installation-issues)
- [Launch Issues](#launch-issues)
- [Gameplay Issues](#gameplay-issues)
- [Audio Issues](#audio-issues)
- [Visual Issues](#visual-issues)
- [Performance Issues](#performance-issues)
- [Save/Load Issues](#save-load-issues)
- [Development Issues](#development-issues)

---

## 🚀 Installation Issues

### Problem: Ren'Py SDK tidak bisa didownload

**Symptoms:**
- Download gagal atau terputus
- File corrupt

**Solutions:**
1. Gunakan browser berbeda
2. Coba download dari mirror site
3. Gunakan download manager
4. Check koneksi internet
5. Disable antivirus sementara

### Problem: Ren'Py tidak bisa di-extract

**Symptoms:**
- Error saat extract
- File tidak lengkap

**Solutions:**
1. Download ulang file
2. Gunakan 7-Zip atau WinRAR
3. Extract ke folder tanpa spasi di nama
4. Check disk space (minimal 1GB free)
5. Run as administrator (Windows)

### Problem: Project tidak muncul di launcher

**Symptoms:**
- Folder tidak terdeteksi
- Project list kosong

**Solutions:**
1. Pastikan folder "Beyond The Goal" ada
2. Check struktur folder (harus ada folder "game")
3. Coba "Refresh" di launcher
4. Coba "Add Existing Project" manual
5. Pastikan tidak ada karakter spesial di path

---

## 🎮 Launch Issues

### Problem: Game tidak mau launch

**Symptoms:**
- Error message saat launch
- Game crash immediately
- Black screen

**Solutions:**
1. **Check Ren'Py version**
   - Minimal version 8.0
   - Update jika perlu

2. **Check error log**
   - Buka `log.txt` di folder game
   - Cari error message
   - Google error message untuk solusi

3. **Force recompile**
   - Di launcher, klik "Force Recompile"
   - Launch ulang

4. **Check file integrity**
   - Pastikan semua file .rpy ada
   - Check tidak ada syntax error

5. **Clean cache**
   - Delete folder `game/cache`
   - Launch ulang

### Problem: "File not found" error

**Symptoms:**
- Error tentang missing file
- Game crash dengan file path error

**Solutions:**
1. **Check file path**
   - Path case-sensitive di Mac/Linux
   - Check typo di nama file

2. **For audio files**
   - Audio files optional
   - Game akan skip jika tidak ada
   - Tambahkan file atau ignore error

3. **For image files**
   - Game akan gunakan placeholder
   - Tidak perlu file image untuk testing
   - Tambahkan file atau ignore

### Problem: Syntax error di script

**Symptoms:**
- Error message tentang syntax
- Line number disebutkan

**Solutions:**
1. **Buka file yang error**
   - Check line number yang disebutkan
   - Look for:
     - Missing colon (:)
     - Wrong indentation
     - Unclosed quotes
     - Missing return statement

2. **Common syntax errors**
   ```python
   # Wrong
   label test
       "Dialog"
   
   # Correct
   label test:
       "Dialog"
       return
   ```

3. **Use text editor with syntax highlighting**
   - VS Code
   - Sublime Text
   - Atom

---

## 🎯 Gameplay Issues

### Problem: Choices tidak muncul

**Symptoms:**
- Menu pilihan tidak tampil
- Game stuck

**Solutions:**
1. **Check menu syntax**
   ```python
   menu:
       "Question?"
       
       "Choice 1":
           # code
       
       "Choice 2":
           # code
   ```

2. **Check indentation**
   - Harus 4 spaces
   - Konsisten di semua line

3. **Reload game**
   - Press Shift+R
   - Atau restart game

### Problem: Score tidak update

**Symptoms:**
- HUD tidak berubah
- Score tetap 0

**Solutions:**
1. **Check function call**
   ```python
   # Correct
   $ add_teknik(10)
   $ add_percaya_diri(5)
   $ add_sportivitas(15)
   ```

2. **Check HUD visibility**
   - HUD harus visible saat gameplay
   - Call `show screen hud_display` jika perlu

3. **Check variable names**
   - `teknik_score` (not `teknik`)
   - `percaya_diri` (not `percaya_diri_score`)
   - `sportivitas` (not `sportivitas_score`)

### Problem: Chapter tidak unlock

**Symptoms:**
- Chapter 2/3 tetap locked
- Chapter select tidak update

**Solutions:**
1. **Check chapter_clear variable**
   ```python
   # Di akhir chapter 1
   $ chapter_clear = 1
   
   # Di akhir chapter 2
   $ chapter_clear = 2
   ```

2. **Check autosave**
   - Pastikan autosave berjalan
   - Load save terbaru

3. **Manual unlock (for testing)**
   ```python
   # Press Shift+O untuk console
   $ chapter_clear = 3
   ```

### Problem: Mini game tidak berfungsi

**Symptoms:**
- Quiz tidak muncul
- Jawaban tidak respond
- Score tidak dihitung

**Solutions:**
1. **Check label call**
   ```python
   call ch1_minigame
   # not jump ch1_minigame
   ```

2. **Check menu structure**
   - Pastikan semua pilihan ada
   - Check indentation

3. **Check score calculation**
   - Pastikan variable di-update
   - Check logic benar/salah

---

## 🔊 Audio Issues

### Problem: Tidak ada suara sama sekali

**Symptoms:**
- Game silent
- No music or sound effects

**Solutions:**
1. **Check volume settings**
   - In-game preferences
   - System volume
   - Mixer volume (Windows)

2. **Check audio files**
   - Audio files optional
   - Game akan skip jika tidak ada
   - Tambahkan file ke `game/audio/`

3. **Check audio format**
   - BGM: MP3 or OGG
   - SFX: WAV
   - Check file tidak corrupt

4. **Test with sample audio**
   - Download free audio
   - Test dengan file sederhana

### Problem: Music tidak loop

**Symptoms:**
- Music berhenti setelah selesai
- Tidak repeat

**Solutions:**
1. **Check play command**
   ```python
   # Correct (will loop)
   play music "audio/training_theme.mp3"
   
   # Wrong (won't loop)
   play sound "audio/training_theme.mp3"
   ```

2. **Check audio file**
   - Pastikan file bisa loop seamlessly
   - Edit audio untuk smooth loop

### Problem: Sound effects tidak play

**Symptoms:**
- SFX tidak terdengar
- Music OK tapi SFX tidak

**Solutions:**
1. **Check play command**
   ```python
   # Correct
   play sound "audio/kick_ball.wav"
   
   # Wrong
   play music "audio/kick_ball.wav"
   ```

2. **Check channel**
   - Sound effects use "sound" channel
   - Music use "music" channel
   - Don't mix them up

---

## 👁️ Visual Issues

### Problem: Character sprites tidak muncul

**Symptoms:**
- Character tidak terlihat
- Hanya background

**Solutions:**
1. **This is normal with placeholders**
   - Placeholder = solid color
   - Might blend with background
   - Add real sprites untuk visibility

2. **Check show command**
   ```python
   # Correct
   show mc neutral at left
   
   # Wrong
   show mc_neutral at left
   ```

3. **Check image definition**
   - Check `characters.rpy`
   - Pastikan image defined

### Problem: Background tidak muncul

**Symptoms:**
- Black screen
- No background

**Solutions:**
1. **Check scene command**
   ```python
   # Correct
   scene bg_school_field
   
   # Wrong
   scene school_field
   ```

2. **Check image definition**
   - Check `characters.rpy`
   - Pastikan background defined

3. **Placeholder should work**
   - Solid color background
   - Jika hitam, mungkin color issue

### Problem: Text tidak terbaca

**Symptoms:**
- Text terlalu kecil
- Text blend dengan background
- Text terpotong

**Solutions:**
1. **Adjust text size**
   - Preferences → Text Speed
   - Edit `gui.rpy` untuk permanent change

2. **Check text box**
   - Pastikan textbox visible
   - Check opacity settings

3. **Change text color**
   - Edit `gui.rpy`
   - Adjust `gui.text_color`

### Problem: UI elements overlap

**Symptoms:**
- Buttons overlap
- HUD overlap dengan dialog
- Menu tidak rapi

**Solutions:**
1. **Check screen positioning**
   - Edit `custom_screens.rpy`
   - Adjust xalign, yalign

2. **Check zorder**
   - Higher zorder = on top
   - Adjust untuk layering

3. **Adjust screen size**
   - Check resolution settings
   - Test di berbagai resolusi

---

## ⚡ Performance Issues

### Problem: Game lag atau slow

**Symptoms:**
- Slow transitions
- Choppy animation
- Long load times

**Solutions:**
1. **Close other programs**
   - Free up RAM
   - Close browser tabs
   - Close background apps

2. **Update graphics drivers**
   - Check manufacturer website
   - Install latest drivers

3. **Lower quality settings**
   - Reduce resolution
   - Disable effects
   - Use windowed mode

4. **Check system requirements**
   - Minimal 2GB RAM
   - Integrated graphics OK
   - Check CPU usage

### Problem: High memory usage

**Symptoms:**
- RAM usage tinggi
- System slow
- Game crash after long play

**Solutions:**
1. **Restart game periodically**
   - Close dan reopen
   - Clear memory

2. **Check for memory leaks**
   - Report jika terjadi
   - Provide log file

3. **Reduce cache**
   - Delete `game/cache`
   - Restart game

---

## 💾 Save/Load Issues

### Problem: Cannot save game

**Symptoms:**
- Save button tidak work
- Error saat save

**Solutions:**
1. **Check write permissions**
   - Folder harus writable
   - Run as administrator (Windows)

2. **Check disk space**
   - Minimal 100MB free
   - Clean up disk

3. **Check save location**
   - Windows: `%APPDATA%\RenPy\`
   - Mac: `~/Library/RenPy/`
   - Linux: `~/.renpy/`

### Problem: Cannot load save

**Symptoms:**
- Load button tidak work
- Save file corrupt
- Error saat load

**Solutions:**
1. **Check save file exists**
   - Look in save folder
   - Check file not empty

2. **Try different save slot**
   - Use multiple save slots
   - Don't rely on single save

3. **Check version compatibility**
   - Save from older version might not work
   - Start new game if necessary

### Problem: Autosave tidak work

**Symptoms:**
- No autosave files
- Progress not saved

**Solutions:**
1. **Check autosave code**
   ```python
   $ renpy.save("auto-ch1")
   ```

2. **Manual save instead**
   - Use save menu
   - Save after each chapter

---

## 💻 Development Issues

### Problem: Changes tidak terlihat

**Symptoms:**
- Edit script tapi tidak berubah
- Old version masih running

**Solutions:**
1. **Reload game**
   - Press Shift+R
   - Atau restart game

2. **Force recompile**
   - Di launcher: Force Recompile
   - Launch ulang

3. **Clear cache**
   - Delete `game/cache`
   - Restart

4. **Check file saved**
   - Pastikan file di-save
   - Check timestamp file

### Problem: Syntax error setelah edit

**Symptoms:**
- Game tidak launch
- Error message

**Solutions:**
1. **Check recent changes**
   - Undo last edit
   - Test incrementally

2. **Use version control**
   - Git untuk track changes
   - Easy to revert

3. **Check indentation**
   - Use 4 spaces
   - No tabs
   - Consistent throughout

### Problem: Asset tidak terdeteksi

**Symptoms:**
- Image/audio tidak load
- File not found error

**Solutions:**
1. **Check file location**
   - `game/images/characters/`
   - `game/images/backgrounds/`
   - `game/audio/`

2. **Check file name**
   - Case-sensitive
   - No spaces (use underscore)
   - Correct extension

3. **Check file format**
   - Images: PNG or JPG
   - Audio: MP3, OGG, or WAV

4. **Reload game**
   - Shift+R after adding files

---

## 🆘 Getting Help

### Before Asking for Help

1. **Check this guide**
2. **Check README.md**
3. **Check code comments**
4. **Search existing issues**
5. **Try basic troubleshooting**

### When Asking for Help

**Include:**
- What you're trying to do
- What's happening instead
- Error messages (full text)
- Steps to reproduce
- System information
- Screenshots (if applicable)
- Log file (`log.txt`)

**Template:**
```markdown
**Problem:**
[Clear description]

**Expected:**
[What should happen]

**Actual:**
[What actually happens]

**Steps to Reproduce:**
1. 
2. 
3. 

**System Info:**
- OS: [e.g., Windows 10]
- Ren'Py Version: [e.g., 8.0.3]
- Game Version: [e.g., 1.0.0]

**Error Message:**
```
[Paste error here]
```

**Screenshots:**
[If applicable]

**Log File:**
[Attach log.txt]
```

### Where to Get Help

1. **Project Issues**
   - Create issue on GitHub
   - Tag appropriately

2. **Ren'Py Forums**
   - https://lemmasoft.renai.us/forums/
   - Active community

3. **Ren'Py Discord**
   - https://discord.gg/renpy
   - Real-time help

4. **Documentation**
   - https://www.renpy.org/doc/html/
   - Comprehensive docs

---

## 🔍 Debug Tools

### Developer Menu (Shift+D)

**Features:**
- Reload game
- Variable viewer
- Image location
- Style inspector
- Console access

### Console (Shift+O)

**Useful Commands:**
```python
# Check variable
teknik_score

# Set variable
$ teknik_score = 100

# Unlock all chapters
$ chapter_clear = 3

# Jump to label
$ renpy.jump("chapter_2")

# Show all images
$ renpy.list_images()
```

### Log File

**Location:**
- Same folder as game
- Named `log.txt`

**Contains:**
- Error messages
- Warnings
- Loading information
- Useful for debugging

---

## 📞 Emergency Fixes

### Nuclear Option: Fresh Start

If nothing works:

1. **Backup saves**
   - Copy save folder

2. **Delete game folder**
   - Remove completely

3. **Re-download/extract**
   - Fresh copy

4. **Restore saves**
   - Copy back save folder

5. **Test**
   - Should work now

### Quick Fixes

**Game won't launch:**
```bash
1. Force Recompile
2. Delete cache folder
3. Restart computer
4. Reinstall Ren'Py
```

**Weird behavior:**
```bash
1. Shift+R (reload)
2. Restart game
3. Delete cache
4. Force recompile
```

**Save issues:**
```bash
1. Manual save
2. Check permissions
3. Check disk space
4. Try different slot
```

---

## ✅ Prevention Tips

### Best Practices

1. **Save often**
   - Multiple slots
   - Before important choices

2. **Backup regularly**
   - Save folder
   - Project folder

3. **Test changes**
   - Test after each edit
   - Don't make many changes at once

4. **Use version control**
   - Git recommended
   - Easy to revert

5. **Keep documentation**
   - Note your changes
   - Document custom code

### Maintenance

1. **Update Ren'Py**
   - Check for updates
   - Test after update

2. **Clean cache**
   - Periodically delete cache
   - Especially after big changes

3. **Check logs**
   - Review log.txt
   - Look for warnings

4. **Test thoroughly**
   - Test all paths
   - Test on different systems

---

## 📚 Additional Resources

- **Ren'Py Documentation:** https://www.renpy.org/doc/html/
- **Ren'Py Cookbook:** https://www.renpy.org/wiki/renpy/doc/cookbook
- **Ren'Py Forums:** https://lemmasoft.renai.us/forums/
- **Ren'Py Discord:** https://discord.gg/renpy
- **Stack Overflow:** Tag [renpy]

---

**Still having issues? Create an issue on GitHub with details!**

*"Every problem has a solution. Keep trying!"* 🔧
