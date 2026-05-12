# ============================================
# BAB 2: Bola yang Tidak Mau Diam
# ============================================
# Materi: Kontrol bola, dribbling, kontrol telapak kaki/dada/paha

label ch2_intro:
    $ current_chapter = 2
    
    scene bg_black with fade
    
    centered "{size=+10}{color=#4CAF50}Bab 2{/color}{/size}\n{size=+5}Bola yang Tidak Mau Diam{/size}"
    
    pause 2.0
    
    play music training_theme fadein 2.0
    
    scene bg_training_cone with dissolve
    
    show coach neutral at center with dissolve
    
    coach "Selamat datang kembali, [player_name]!"
    
    coach "Hari ini kita akan belajar sesuatu yang sangat penting: kontrol bola."
    
    show mc neutral at left with dissolve
    
    mc "Kontrol bola, Coach?"
    
    show coach fokus
    
    coach "Ya. Menendang bola itu penting, tapi menghentikan dan menguasai bola juga sama pentingnya."
    
    show naya sedih at right with dissolve
    
    naya "Coach... aku kesulitan mengontrol bola yang datang cepat..."
    
    show coach senang
    
    coach "Tidak apa-apa, Naya. Hari ini kita akan belajar bersama."
    
    coach "Ada beberapa teknik kontrol bola yang perlu kalian kuasai:"
    
    show text "{b}Teknik Kontrol Bola:{/b}\n\n1. Telapak Kaki (bola datar)\n2. Dada (bola melayang tinggi)\n3. Paha (bola melayang sedang)\n4. Kaki Bagian Dalam (bola bergulir)" at truecenter with dissolve
    
    pause 3.0
    
    hide text with dissolve
    
    show coach neutral
    
    coach "Setelah menguasai kontrol, kita akan belajar dribbling."
    
    show mc fokus
    
    mc "Dribbling? Seperti menggiring bola melewati lawan?"
    
    show coach senang
    
    coach "Tepat sekali! Dribbling adalah seni menguasai bola sambil bergerak."
    
    show naya neutral
    
    naya "[player_name], mau bantu aku latihan?"
    
    menu:
        "Bagaimana kamu membantu Naya?"
        
        "Latih kontrol telapak kaki dulu":
            $ add_teknik(5)
            $ technical_points += 1
            
            show mc senang
            
            mc "Ayo kita mulai dari yang paling dasar, Naya."
            
            call ch2_scene_control_basic
        
        "Latih kontrol dada untuk bola tinggi":
            $ add_percaya_diri(5)
            $ brave_points += 1
            
            show mc fokus
            
            mc "Kita coba yang lebih menantang, Naya!"
            
            call ch2_scene_control_chest
        
        "Langsung coba dribbling":
            $ add_sportivitas(5)
            $ supportive_points += 1
            
            show mc senang
            
            mc "Ayo kita langsung praktik dribbling bareng!"
            
            call ch2_scene_dribbling
    
    # Lanjut ke mini game
    call ch2_minigame
    
    return

# ============================================
# SCENE: BASIC CONTROL
# ============================================
label ch2_scene_control_basic:
    scene bg_wall_training with dissolve
    
    show mc fokus at left
    show naya neutral at right
    
    mc "Naya, untuk bola datar, gunakan telapak kaki."
    
    show mc neutral
    
    mc "Posisi kaki di atas bola, tekan perlahan saat bola datang."
    
    show naya fokus
    
    naya "Seperti ini?"
    
    play sound kick_ball
    
    show naya senang
    
    naya "Wah! Bolanya berhenti sempurna!"
    
    show mc senang
    
    mc "Bagus, Naya!"
    
    $ add_teknik(10)
    $ add_sportivitas(5)
    
    show coach senang at center with dissolve
    
    coach "Excellent! Kalian berdua bekerja sama dengan baik."
    
    return

# ============================================
# SCENE: CHEST CONTROL
# ============================================
label ch2_scene_control_chest:
    scene bg_training_cone with dissolve
    
    show naya takut at right
    
    naya "Bola tinggi... aku takut kena wajah..."
    
    show mc neutral at left with dissolve
    
    mc "Tenang, Naya. Aku akan tunjukkan caranya."
    
    show mc fokus
    
    mc "Saat bola datang, buka dada, lalu tarik ke belakang untuk meredam kecepatan bola."
    
    play sound kick_ball
    
    show mc senang
    
    mc "Lihat? Bolanya jatuh tepat di depan kaki."
    
    show naya fokus
    
    naya "Aku akan coba!"
    
    play sound kick_ball
    
    show naya senang
    
    naya "Aku berhasil!"
    
    $ add_percaya_diri(10)
    $ add_sportivitas(5)
    
    return

# ============================================
# SCENE: DRIBBLING
# ============================================
label ch2_scene_dribbling:
    scene bg_training_cone with dissolve
    
    show coach fokus at center
    
    coach "Dribbling membutuhkan kontrol dan irama."
    
    show coach neutral
    
    coach "Gunakan kaki bagian dalam dan luar secara bergantian."
    
    show mc fokus at left with dissolve
    show naya fokus at right with dissolve
    
    coach "Sentuhan harus lembut, jangan terlalu keras."
    
    play sound kick_ball
    pause 0.3
    play sound kick_ball
    pause 0.3
    play sound kick_ball
    
    show mc senang
    show naya senang
    
    mc "Ini seru!"
    
    naya "Aku mulai merasakan iramanya!"
    
    $ add_teknik(10)
    $ add_percaya_diri(5)
    
    return

# ============================================
# BAB 2 MINI GAME: CONTROL & DRIBBLE MATCH
# ============================================
label ch2_minigame:
    scene bg_black with fade
    
    centered "{size=+10}Mini Game: Control & Dribble Match{/size}\n\nCocokkan teknik dengan situasi bola yang tepat!"
    
    pause 2.0
    
    play music quiz_theme
    
    $ ch2_quiz_score = 0
    $ ch2_combo = 0
    
    # Soal 1
    scene bg_training_cone with dissolve
    
    show text "Situasi 1:\nBola bergulir datar ke arahmu dengan kecepatan sedang." at truecenter
    
    pause 2.0
    
    hide text
    
    menu:
        "Teknik kontrol apa yang kamu gunakan?"
        
        "Telapak kaki":
            $ ch2_quiz_score += 15
            $ ch2_combo += 1
            $ add_teknik(10)
            play sound correct
            show text "{color=#4CAF50}✓ BENAR!{/color}\n\nTelapak kaki sempurna untuk bola datar.\nCombo: [ch2_combo]" at truecenter
            pause 2.0
            hide text
        
        "Dada":
            $ ch2_combo = 0
            play sound wrong
            with shake
            show text "{color=#F44336}✗ SALAH{/color}\n\nDada untuk bola melayang tinggi, bukan bola datar.\nCombo reset!" at truecenter
            pause 2.0
            hide text
        
        "Paha":
            $ ch2_combo = 0
            play sound wrong
            with shake
            show text "{color=#F44336}✗ SALAH{/color}\n\nPaha untuk bola melayang sedang.\nCombo reset!" at truecenter
            pause 2.0
            hide text
    
    # Soal 2
    show text "Situasi 2:\nBola melayang tinggi menuju dadamu." at truecenter
    
    pause 2.0
    
    hide text
    
    menu:
        "Teknik kontrol apa yang kamu gunakan?"
        
        "Telapak kaki":
            $ ch2_combo = 0
            play sound wrong
            with shake
            show text "{color=#F44336}✗ SALAH{/color}\n\nTelapak kaki tidak bisa menjangkau bola tinggi.\nCombo reset!" at truecenter
            pause 2.0
            hide text
        
        "Dada":
            $ ch2_quiz_score += 15
            $ ch2_combo += 1
            $ add_teknik(10)
            play sound correct
            
            if ch2_combo >= 2:
                show text "{color=#4CAF50}✓ BENAR!{/color}\n\n{color=#FFD700}★ COMBO BONUS! ★{/color}\nDada sempurna untuk bola melayang tinggi.\nCombo: [ch2_combo]" at truecenter
                $ ch2_quiz_score += 10
            else:
                show text "{color=#4CAF50}✓ BENAR!{/color}\n\nDada sempurna untuk bola melayang tinggi.\nCombo: [ch2_combo]" at truecenter
            
            pause 2.0
            hide text
        
        "Paha":
            $ ch2_combo = 0
            play sound wrong
            with shake
            show text "{color=#F44336}✗ SALAH{/color}\n\nPaha untuk bola melayang sedang, bukan tinggi.\nCombo reset!" at truecenter
            pause 2.0
            hide text
    
    # Soal 3
    show text "Situasi 3:\nBola melayang setinggi pinggang." at truecenter
    
    pause 2.0
    
    hide text
    
    menu:
        "Teknik kontrol apa yang kamu gunakan?"
        
        "Telapak kaki":
            $ ch2_combo = 0
            play sound wrong
            with shake
            show text "{color=#F44336}✗ SALAH{/color}\n\nTelapak kaki untuk bola datar.\nCombo reset!" at truecenter
            pause 2.0
            hide text
        
        "Dada":
            $ ch2_combo = 0
            play sound wrong
            with shake
            show text "{color=#F44336}✗ SALAH{/color}\n\nDada untuk bola lebih tinggi.\nCombo reset!" at truecenter
            pause 2.0
            hide text
        
        "Paha":
            $ ch2_quiz_score += 15
            $ ch2_combo += 1
            $ add_teknik(10)
            play sound correct
            
            if ch2_combo >= 3:
                show text "{color=#4CAF50}✓ BENAR!{/color}\n\n{color=#FFD700}★★ PERFECT COMBO! ★★{/color}\nPaha sempurna untuk bola setinggi pinggang.\nCombo: [ch2_combo]" at truecenter
                $ ch2_quiz_score += 20
            else:
                show text "{color=#4CAF50}✓ BENAR!{/color}\n\nPaha sempurna untuk bola setinggi pinggang.\nCombo: [ch2_combo]" at truecenter
            
            pause 2.0
            hide text
    
    # Soal 4 - Dribbling
    show text "Situasi 4:\nAda 3 cone di depanmu. Kamu harus melewatinya dengan dribbling." at truecenter
    
    pause 2.0
    
    hide text
    
    menu:
        "Teknik dribbling apa yang kamu gunakan?"
        
        "Kaki bagian dalam dan luar bergantian":
            $ ch2_quiz_score += 15
            $ ch2_combo += 1
            $ add_teknik(10)
            play sound correct
            show text "{color=#4CAF50}✓ BENAR!{/color}\n\nDribbling dengan kaki dalam-luar memberikan kontrol terbaik.\nCombo: [ch2_combo]" at truecenter
            pause 2.0
            hide text
        
        "Tendangan keras lurus":
            $ ch2_combo = 0
            play sound wrong
            with shake
            show text "{color=#F44336}✗ SALAH{/color}\n\nTendangan keras akan membuat bola lepas kontrol.\nCombo reset!" at truecenter
            pause 2.0
            hide text
        
        "Hanya kaki kanan saja":
            $ ch2_quiz_score += 5
            $ ch2_combo = 0
            play sound wrong
            show text "{color=#FFC107}△ KURANG EFEKTIF{/color}\n\nBisa, tapi kurang fleksibel. Gunakan kedua kaki.\nCombo reset!" at truecenter
            pause 2.0
            hide text
    
    # Soal 5
    show text "Situasi 5:\nBola datang cepat ke arahmu, kamu harus segera mengontrol dan dribble." at truecenter
    
    pause 2.0
    
    hide text
    
    menu:
        "Apa yang kamu lakukan?"
        
        "Kontrol dengan telapak kaki, lalu dribble":
            $ ch2_quiz_score += 15
            $ ch2_combo += 1
            $ add_teknik(10)
            play sound correct
            show text "{color=#4CAF50}✓ BENAR!{/color}\n\nKontrol dulu, baru dribble. Urutan yang tepat!\nCombo: [ch2_combo]" at truecenter
            pause 2.0
            hide text
        
        "Langsung dribble tanpa kontrol":
            $ ch2_combo = 0
            play sound wrong
            with shake
            show text "{color=#F44336}✗ SALAH{/color}\n\nBola cepat harus dikontrol dulu sebelum dribble.\nCombo reset!" at truecenter
            pause 2.0
            hide text
        
        "Tendang jauh ke depan":
            $ ch2_combo = 0
            play sound wrong
            with shake
            show text "{color=#F44336}✗ SALAH{/color}\n\nItu bukan dribbling, bola akan lepas dari kontrolmu.\nCombo reset!" at truecenter
            pause 2.0
            hide text
    
    # Hasil Quiz
    call ch2_quiz_result
    
    return

# ============================================
# QUIZ RESULT
# ============================================
label ch2_quiz_result:
    scene bg_reflection with dissolve
    
    show coach neutral at center with dissolve
    
    if ch2_quiz_score >= 60:
        show coach senang
        coach "Luar biasa, [player_name]! Skor kamu: [ch2_quiz_score]"
        coach "Kamu menguasai kontrol dan dribbling dengan sempurna!"
        $ add_percaya_diri(20)
        $ technical_points += 2
    elif ch2_quiz_score >= 40:
        show coach senang
        coach "Bagus, [player_name]! Skor kamu: [ch2_quiz_score]"
        coach "Kamu sudah memahami dasar kontrol dan dribbling."
        $ add_percaya_diri(15)
        $ technical_points += 1
    else:
        show coach neutral
        coach "Skor kamu: [ch2_quiz_score]. Terus berlatih, [player_name]."
        coach "Kontrol bola butuh latihan berulang. Jangan menyerah!"
        $ add_percaya_diri(10)
        $ brave_points += 1
    
    show naya senang at right with dissolve
    
    naya "Terima kasih sudah membantu aku, [player_name]!"
    
    $ add_sportivitas(10)
    
    # Unlock gallery
    $ unlock_gallery("ch2_kontrol_dribbling")
    
    # Autosave
    $ renpy.save("auto-ch2")
    
    # Mark chapter complete
    $ ch2_completed = True
    $ chapter_clear = 2
    
    # Lanjut ke refleksi
    call ch2_reflection
    
    return

# ============================================
# BAB 2 REFLEKSI
# ============================================
label ch2_reflection:
    scene bg_reflection with fade
    
    play music reflection_theme fadein 2.0
    
    centered "{size=+10}Refleksi Bab 2{/size}"
    
    pause 1.0
    
    show mc neutral at center with dissolve
    
    mc "Hari ini aku belajar bahwa menguasai bola bukan hanya soal kekuatan..."
    
    show mc fokus
    
    mc "Tapi juga tentang ketenangan dan kontrol."
    
    show mc senang
    
    mc "Dan yang paling penting, membantu teman belajar membuat aku juga semakin paham."
    
    scene bg_black with fade
    
    show text "{b}Ringkasan Pembelajaran:{/b}\n\n• Telapak kaki: Kontrol bola datar\n• Dada: Kontrol bola melayang tinggi\n• Paha: Kontrol bola melayang sedang\n• Dribbling: Sentuhan lembut, irama teratur\n\n{i}Ketenangan dan fokus adalah kunci kontrol bola.{/i}" at truecenter
    
    pause 5.0
    
    hide text with dissolve
    
    centered "Chapter 2 Selesai!"
    
    pause 1.0
    
    # Tampilkan skor
    call show_score_screen
    
    # Transisi ke bab berikutnya
    scene bg_black with fade
    
    pause 1.0
    
    centered "{size=+5}Bab 2 Selesai!{/size}\n\nLanjut ke Bab 3..."
    
    pause 2.0
    
    # Lanjut ke bab berikutnya
    return
