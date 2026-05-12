# 🧪 Testing Checklist

Gunakan checklist ini untuk memastikan game "Beyond The Goal" berfungsi dengan baik.

## ✅ Pre-Launch Testing

### Installation & Setup
- [ ] Ren'Py SDK terinstall dengan benar
- [ ] Project terbuka di Ren'Py Launcher
- [ ] Tidak ada error saat compile
- [ ] Game dapat di-launch

### Main Menu
- [ ] Main menu tampil dengan benar
- [ ] Background music playing (jika ada audio)
- [ ] Semua tombol clickable
- [ ] "Mulai Bermain" membuka opening cinematic
- [ ] "Chapter Select" membuka chapter select screen
- [ ] "Gallery Materi" membuka gallery screen
- [ ] "Load Game" membuka load screen
- [ ] "Pengaturan" membuka preferences
- [ ] "Keluar" menutup game dengan konfirmasi

## 📖 Chapter 1 Testing

### Opening & Introduction
- [ ] Opening cinematic tampil
- [ ] Narasi pembuka muncul
- [ ] Logo game tampil
- [ ] Music transition smooth
- [ ] Input nama pemain berfungsi
- [ ] Nama pemain tersimpan dan digunakan

### Dialog & Characters
- [ ] Coach Arya muncul dengan benar
- [ ] Naya muncul dengan benar
- [ ] MC (main character) muncul dengan benar
- [ ] Dialog text readable
- [ ] Character expressions berubah sesuai context
- [ ] Background berubah sesuai scene

### Choices & Branching
- [ ] Menu pilihan muncul
- [ ] Semua pilihan clickable
- [ ] Setiap pilihan mengarah ke scene yang benar
- [ ] Skor berubah sesuai pilihan
- [ ] HUD menampilkan skor yang benar

### Mini Game - Kick Selector Quiz
- [ ] Mini game intro tampil
- [ ] Music berubah ke quiz theme
- [ ] Soal 1 tampil dengan benar
- [ ] Pilihan jawaban clickable
- [ ] Jawaban benar memberi feedback positif
- [ ] Jawaban salah memberi feedback negatif
- [ ] Sound effect correct/wrong playing
- [ ] Skor dihitung dengan benar
- [ ] Semua 3 soal berfungsi
- [ ] Quiz result tampil dengan benar

### Reflection & Completion
- [ ] Reflection screen tampil
- [ ] Ringkasan pembelajaran muncul
- [ ] Score screen tampil
- [ ] Chapter 1 marked as completed
- [ ] Chapter 2 unlocked di chapter select
- [ ] Autosave berfungsi
- [ ] Gallery item unlocked

## 📖 Chapter 2 Testing

### Introduction
- [ ] Chapter 2 intro tampil
- [ ] Naya kesulitan mengontrol bola (story)
- [ ] Menu pilihan bantuan muncul
- [ ] Setiap pilihan mengarah ke scene yang tepat

### Scenes
- [ ] Scene kontrol telapak kaki berfungsi
- [ ] Scene kontrol dada berfungsi
- [ ] Scene dribbling berfungsi
- [ ] Dialog flow natural
- [ ] Character interactions make sense

### Mini Game - Control & Dribble Match
- [ ] Mini game intro tampil
- [ ] Combo system berfungsi
- [ ] Combo counter tampil
- [ ] Combo bonus dihitung
- [ ] Combo reset saat salah
- [ ] Semua 5 soal berfungsi
- [ ] Feedback untuk setiap jawaban
- [ ] Quiz result dengan combo info

### Reflection & Completion
- [ ] Reflection screen tampil
- [ ] Naya berterima kasih
- [ ] Sportivitas score bertambah
- [ ] Chapter 2 marked as completed
- [ ] Chapter 3 unlocked
- [ ] Autosave berfungsi
- [ ] Gallery item unlocked

## 📖 Chapter 3 Testing

### Introduction
- [ ] Chapter 3 intro tampil
- [ ] Bima takut heading (story)
- [ ] Menu pilihan membantu Bima muncul
- [ ] Setiap pilihan mengarah ke scene yang tepat

### Scenes
- [ ] Scene heading slow practice berfungsi
- [ ] Scene heading demonstration berfungsi
- [ ] Scene heading brave approach berfungsi
- [ ] Bima character development terlihat
- [ ] Dialog emosional tersampaikan

### Mini Game - Final Small Match
- [ ] Mini game intro tampil
- [ ] Pertandingan 2v2 setup jelas
- [ ] Situasi 1: Passing vs Shooting
- [ ] Situasi 2: Heading decision
- [ ] Situasi 3: Sportivitas (Bima jatuh)
- [ ] Situasi 4: Final goal opportunity
- [ ] Teknik score tracked
- [ ] Sportivitas score tracked separately
- [ ] Match result sesuai dengan skor

### Ending & Credits
- [ ] Match result screen tampil
- [ ] Feedback sesuai dengan performance
- [ ] Reflection screen tampil
- [ ] Game ending message tampil
- [ ] Player Growth Summary tampil
- [ ] Player style determined correctly
- [ ] Credits scene tampil
- [ ] Return to main menu

## 🎮 Gameplay Systems

### Score System
- [ ] Teknik score increases correctly
- [ ] Percaya Diri score increases correctly
- [ ] Sportivitas score increases correctly
- [ ] Scores never go negative
- [ ] HUD updates in real-time
- [ ] Score screen shows correct values

### Player Style System
- [ ] Technical points tracked
- [ ] Supportive points tracked
- [ ] Brave points tracked
- [ ] Balanced points tracked
- [ ] Player style determined correctly at end
- [ ] Style description matches gameplay

### Save/Load System
- [ ] Manual save berfungsi
- [ ] Autosave after each chapter
- [ ] Load game restores state correctly
- [ ] Chapter progress saved
- [ ] Scores saved correctly
- [ ] Gallery unlocks saved

### Gallery System
- [ ] Gallery accessible from main menu
- [ ] Locked items shown as locked
- [ ] Unlocked items show content
- [ ] Chapter 1 materi unlocks after ch1
- [ ] Chapter 2 materi unlocks after ch2
- [ ] Chapter 3 materi unlocks after ch3
- [ ] Content readable and informative

## 🎨 Visual & Audio

### Visuals
- [ ] All backgrounds load (or show placeholder)
- [ ] All character sprites load (or show placeholder)
- [ ] Transitions smooth
- [ ] No visual glitches
- [ ] Text readable on all backgrounds
- [ ] UI elements properly positioned

### Audio
- [ ] Main menu music plays (if available)
- [ ] Training theme plays in chapters
- [ ] Quiz theme plays in mini games
- [ ] Final match theme plays in chapter 3
- [ ] Reflection theme plays in reflections
- [ ] Sound effects play when triggered
- [ ] Volume controls work
- [ ] Music loops smoothly
- [ ] No audio cutting or glitches

### Effects
- [ ] Shake effect on wrong answer
- [ ] Flash effect on correct answer
- [ ] VPunch on strong kick
- [ ] Fade transitions work
- [ ] Dissolve transitions work
- [ ] Centered text displays correctly

## 🖥️ UI/UX

### HUD Display
- [ ] HUD visible during gameplay
- [ ] HUD hidden in menus
- [ ] HUD positioned correctly (top right)
- [ ] HUD readable
- [ ] HUD updates in real-time
- [ ] HUD doesn't overlap important content

### Chapter Select
- [ ] Shows all 3 chapters
- [ ] Locked chapters shown as locked
- [ ] Unlocked chapters clickable
- [ ] Chapter descriptions visible
- [ ] "Kembali" button works
- [ ] Navigation smooth

### Gallery Screen
- [ ] Opens from main menu
- [ ] Shows unlocked content
- [ ] Scrollable if content is long
- [ ] Content formatted properly
- [ ] "Kembali" button works
- [ ] No locked content accessible

### Preferences
- [ ] Volume sliders work
- [ ] Fullscreen toggle works
- [ ] Text speed adjustment works
- [ ] Auto-forward speed works
- [ ] Skip settings work
- [ ] Changes saved

## 🐛 Bug Testing

### Common Issues
- [ ] No crashes during gameplay
- [ ] No infinite loops
- [ ] No stuck states
- [ ] All choices lead somewhere
- [ ] All labels defined
- [ ] No missing images cause crashes
- [ ] No missing audio cause crashes
- [ ] Rollback works correctly
- [ ] Skip works correctly
- [ ] Quick menu accessible

### Edge Cases
- [ ] Empty name input handled
- [ ] Very long name handled
- [ ] Rapid clicking doesn't break game
- [ ] Loading during mini game works
- [ ] Saving during choices works
- [ ] Multiple playthroughs work
- [ ] Different choice paths work

## 📱 Platform Testing

### Windows
- [ ] Game launches
- [ ] All features work
- [ ] Performance smooth
- [ ] Save/load works
- [ ] Exit works properly

### Mac (if available)
- [ ] Game launches
- [ ] All features work
- [ ] Performance smooth
- [ ] Save/load works
- [ ] Exit works properly

### Linux (if available)
- [ ] Game launches
- [ ] All features work
- [ ] Performance smooth
- [ ] Save/load works
- [ ] Exit works properly

## 🎯 Educational Content

### Learning Objectives
- [ ] Teknik menendang explained clearly
- [ ] Kontrol bola explained clearly
- [ ] Dribbling explained clearly
- [ ] Heading explained clearly
- [ ] Teamwork emphasized
- [ ] Sportivitas emphasized

### Feedback Quality
- [ ] Correct answers give positive feedback
- [ ] Wrong answers give educational feedback
- [ ] Feedback explains why answer is right/wrong
- [ ] Feedback encourages learning
- [ ] No negative/discouraging messages

### Reflection Quality
- [ ] Reflections summarize learning
- [ ] Reflections connect to gameplay
- [ ] Reflections are meaningful
- [ ] Reflections encourage growth mindset

## 📊 Performance

### Loading Times
- [ ] Game starts in reasonable time
- [ ] Chapter loads quickly
- [ ] Scene transitions smooth
- [ ] No long freezes
- [ ] Image loading doesn't cause lag

### Memory Usage
- [ ] No memory leaks
- [ ] Game runs smoothly throughout
- [ ] No slowdown over time
- [ ] Multiple playthroughs stable

## ✨ Polish

### Overall Experience
- [ ] Story flows naturally
- [ ] Pacing feels right
- [ ] Choices feel meaningful
- [ ] Characters are likeable
- [ ] Educational content integrated well
- [ ] Ending is satisfying
- [ ] Replayability exists

### Consistency
- [ ] Character personalities consistent
- [ ] Art style consistent (when assets added)
- [ ] Music style consistent
- [ ] UI style consistent
- [ ] Tone consistent throughout

## 📝 Documentation

### Code Quality
- [ ] Code well-commented
- [ ] File structure logical
- [ ] Naming conventions consistent
- [ ] No unused code
- [ ] Easy to modify

### User Documentation
- [ ] README.md complete
- [ ] QUICKSTART.md helpful
- [ ] ASSET_GUIDE.md clear
- [ ] CHANGELOG.md updated
- [ ] Comments in code helpful

## 🚀 Release Readiness

### Pre-Release
- [ ] All critical bugs fixed
- [ ] All features working
- [ ] Documentation complete
- [ ] Assets finalized (or placeholders acceptable)
- [ ] Testing complete

### Build
- [ ] Windows build works
- [ ] Mac build works (if applicable)
- [ ] Linux build works (if applicable)
- [ ] Android build works (if applicable)
- [ ] File size reasonable

### Distribution
- [ ] README included
- [ ] License included
- [ ] Credits complete
- [ ] Version number set
- [ ] Build name correct

---

## 📋 Testing Notes

**Tester Name:** _______________
**Date:** _______________
**Version:** _______________
**Platform:** _______________

**Critical Issues Found:**
- 
- 
- 

**Minor Issues Found:**
- 
- 
- 

**Suggestions:**
- 
- 
- 

**Overall Rating:** ___/10

---

**Status Legend:**
- ✅ Pass
- ❌ Fail
- ⚠️ Issue (but not blocking)
- 🔄 Needs retest
- ➖ Not applicable
