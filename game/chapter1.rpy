# ============================================
# BAB 1: Umpan Pertama di Lapangan Senja
# ============================================
# Materi: Dasar sepak bola, peran pemain, teknik menendang

label ch1_intro:
    $ current_chapter = 1
    
    scene bg_black with fade
    
    centered "{size=+10}{color=#4CAF50}Bab 1{/color}{/size}\n{size=+5}Umpan Pertama di Lapangan Senja{/size}"
    
    pause 2.0
    
    play music training_theme fadein 2.0
    
    scene bg_school_field with dissolve
    
    show coach neutral at center with dissolve
    
    coach "Selamat datang di latihan sepak bola!"
    
    coach "Sebelum kita mulai, siapa nama kamu?"
    
    $ player_name = renpy.input("Masukkan nama kamu:", default="Raka", length=20)
    $ player_name = player_name.strip() or "Raka"
    
    show coach senang
    
    coach "Baik, [player_name]! Senang bertemu denganmu."
    
    show coach neutral
    
    coach "Hari ini kita akan belajar teknik dasar menendang bola."
    
    show mc neutral at left with dissolve
    
    mc "Teknik menendang? Bukankah itu mudah, Coach?"
    
    show coach fokus
    
    coach "Banyak yang berpikir begitu. Tapi menendang bola dengan benar adalah fondasi dari semua permainan."
    
    coach "Ada tiga teknik dasar menendang yang harus kamu kuasai:"
    
    show text "1. Kaki Bagian Dalam\n2. Kaki Bagian Luar\n3. Punggung Kaki" at truecenter with dissolve
    
    pause 2.0
    
    hide text with dissolve
    
    coach "Setiap teknik punya fungsi berbeda dalam permainan."
    
    show naya senang at right with dissolve
    
    naya "Hai [player_name]! Aku Naya. Ayo kita latihan bareng!"
    
    mc "Hai Naya!"
    
    show coach neutral
    
    coach "Baik, sekarang kita akan mulai latihan. [player_name], apa yang ingin kamu lakukan dulu?"
    
    menu:
        "Apa yang ingin kamu lakukan?"
        
        "Latih umpan pendek dengan Naya":
            $ add_sportivitas(5)
            $ supportive_points += 1
            
            show mc senang
            
            mc "Aku ingin latihan umpan pendek dulu, Coach."
            
            show coach senang
            
            coach "Pilihan bagus! Umpan pendek adalah dasar kerja sama tim."
            
            call ch1_scene_passing
        
        "Coba tendangan keras ke gawang":
            $ add_percaya_diri(5)
            $ brave_points += 1
            
            show mc fokus
            
            mc "Aku ingin coba tendangan keras, Coach!"
            
            show coach neutral
            
            coach "Berani mencoba! Tapi ingat, kekuatan tanpa teknik hanya akan sia-sia."
            
            call ch1_scene_shooting
        
        "Tanya teori dulu sebelum praktik":
            $ add_teknik(5)
            $ technical_points += 1
            
            show mc fokus
            
            mc "Coach, boleh jelaskan teorinya dulu?"
            
            show coach senang
            
            coach "Bagus! Memahami teori akan membuat praktikmu lebih efektif."
            
            call ch1_scene_theory
    
    # Lanjut ke mini game
    call ch1_minigame
    
    return

# ============================================
# SCENE: PASSING PRACTICE
# ============================================
label ch1_scene_passing:
    scene bg_training_cone with dissolve
    
    show naya senang at right
    show mc neutral at left
    
    naya "Oke [player_name], untuk umpan pendek kita pakai kaki bagian dalam."
    
    show naya fokus
    
    naya "Posisi kaki tumpu di samping bola, kaki tendang mengayun dari samping."
    
    show mc fokus
    
    mc "Seperti ini?"
    
    play sound kick_ball
    
    show naya senang
    
    naya "Bagus! Bolanya akurat!"
    
    $ add_teknik(10)
    
    show coach senang at center with dissolve
    
    coach "Excellent! Umpan pendek yang baik adalah kunci permainan tim."
    
    return

# ============================================
# SCENE: SHOOTING PRACTICE
# ============================================
label ch1_scene_shooting:
    scene bg_mini_field_1v1 with dissolve
    
    show mc fokus at center
    
    mc "Aku akan coba tendangan keras!"
    
    play sound strong_kick
    with vpunch
    
    show mc sedih
    
    mc "Ah! Meleset jauh..."
    
    show coach neutral at right with dissolve
    
    coach "Lihat? Kekuatan tanpa kontrol tidak berguna."
    
    coach "Untuk tendangan keras, gunakan punggung kaki. Tapi yang penting adalah akurasi."
    
    show mc fokus
    
    mc "Baik Coach, aku akan coba lagi dengan lebih fokus."
    
    $ add_percaya_diri(5)
    $ add_teknik(5)
    
    return

# ============================================
# SCENE: THEORY LESSON
# ============================================
label ch1_scene_theory:
    scene bg_reflection with dissolve
    
    show coach fokus at center
    
    coach "Mari kita bahas teori menendang bola."
    
    show text "{b}Teknik Menendang Bola:{/b}\n\n{color=#4CAF50}1. Kaki Bagian Dalam{/color}\n- Untuk umpan pendek akurat\n- Kontrol tinggi\n\n{color=#FF9800}2. Kaki Bagian Luar{/color}\n- Untuk umpan melengkung\n- Mengecoh lawan\n\n{color=#2196F3}3. Punggung Kaki{/color}\n- Untuk tendangan keras\n- Jarak jauh" at truecenter with dissolve
    
    pause 5.0
    
    hide text with dissolve
    
    show coach senang
    
    coach "Memahami teori akan membantumu memilih teknik yang tepat saat bermain."
    
    $ add_teknik(15)
    
    return

# ============================================
# BAB 1 MINI GAME: KICK SELECTOR QUIZ
# ============================================
label ch1_minigame:
    scene bg_black with fade
    
    centered "{size=+10}Mini Game: Kick Selector Quiz{/size}\n\nPilih teknik tendangan yang tepat untuk setiap situasi!"
    
    pause 2.0
    
    play music quiz_theme
    
    $ ch1_quiz_score = 0
    
    # Soal 1
    scene bg_training_cone with dissolve
    
    show text "Situasi 1:\nTeman berada 5 meter di depanmu.\nKamu ingin memberikan umpan akurat." at truecenter
    
    pause 2.0
    
    hide text
    
    menu:
        "Teknik apa yang kamu gunakan?"
        
        "Kaki bagian dalam":
            $ ch1_quiz_score += 10
            $ add_teknik(10)
            play sound correct
            show text "{color=#4CAF50}✓ BENAR!{/color}\n\nKaki bagian dalam memberikan kontrol dan akurasi terbaik untuk umpan pendek." at truecenter
            pause 2.0
            hide text
        
        "Kaki bagian luar":
            $ ch1_quiz_score -= 3
            play sound wrong
            with shake
            show text "{color=#F44336}✗ KURANG TEPAT{/color}\n\nKaki bagian luar lebih cocok untuk umpan melengkung atau mengecoh lawan." at truecenter
            pause 2.0
            hide text
        
        "Punggung kaki":
            $ ch1_quiz_score -= 3
            play sound wrong
            with shake
            show text "{color=#F44336}✗ KURANG TEPAT{/color}\n\nPunggung kaki untuk tendangan keras jarak jauh, bukan umpan pendek." at truecenter
            pause 2.0
            hide text
    
    # Soal 2
    scene bg_mini_field_1v1 with dissolve
    
    show text "Situasi 2:\nKamu berada 20 meter dari gawang.\nIngin menendang keras ke gawang." at truecenter
    
    pause 2.0
    
    hide text
    
    menu:
        "Teknik apa yang kamu gunakan?"
        
        "Kaki bagian dalam":
            $ ch1_quiz_score -= 3
            play sound wrong
            with shake
            show text "{color=#F44336}✗ KURANG TEPAT{/color}\n\nKaki bagian dalam kurang kuat untuk jarak jauh." at truecenter
            pause 2.0
            hide text
        
        "Kaki bagian luar":
            $ ch1_quiz_score += 5
            $ add_teknik(5)
            play sound correct
            show text "{color=#FFC107}△ CUKUP BAIK{/color}\n\nBisa digunakan, tapi punggung kaki lebih kuat untuk tendangan jarak jauh." at truecenter
            pause 2.0
            hide text
        
        "Punggung kaki":
            $ ch1_quiz_score += 10
            $ add_teknik(10)
            play sound correct
            show text "{color=#4CAF50}✓ BENAR!{/color}\n\nPunggung kaki memberikan kekuatan maksimal untuk tendangan jarak jauh." at truecenter
            pause 2.0
            hide text
    
    # Soal 3
    scene bg_training_cone with dissolve
    
    show text "Situasi 3:\nAda lawan di depanmu.\nKamu ingin mengoper bola melengkung ke teman di samping." at truecenter
    
    pause 2.0
    
    hide text
    
    menu:
        "Teknik apa yang kamu gunakan?"
        
        "Kaki bagian dalam":
            $ ch1_quiz_score += 5
            $ add_teknik(5)
            play sound correct
            show text "{color=#FFC107}△ CUKUP BAIK{/color}\n\nBisa digunakan, tapi kaki luar lebih efektif untuk umpan melengkung." at truecenter
            pause 2.0
            hide text
        
        "Kaki bagian luar":
            $ ch1_quiz_score += 10
            $ add_teknik(10)
            play sound correct
            show text "{color=#4CAF50}✓ BENAR!{/color}\n\nKaki bagian luar sempurna untuk umpan melengkung dan mengecoh lawan." at truecenter
            pause 2.0
            hide text
        
        "Punggung kaki":
            $ ch1_quiz_score -= 3
            play sound wrong
            with shake
            show text "{color=#F44336}✗ KURANG TEPAT{/color}\n\nPunggung kaki sulit untuk membuat bola melengkung." at truecenter
            pause 2.0
            hide text
    
    # Hasil Quiz
    call ch1_quiz_result
    
    return

# ============================================
# QUIZ RESULT
# ============================================
label ch1_quiz_result:
    scene bg_reflection with dissolve
    
    show coach neutral at center with dissolve
    
    if ch1_quiz_score >= 25:
        show coach senang
        coach "Luar biasa, [player_name]! Skor kamu: [ch1_quiz_score]"
        coach "Kamu benar-benar memahami kapan menggunakan setiap teknik!"
        $ add_percaya_diri(15)
        $ technical_points += 2
    elif ch1_quiz_score >= 15:
        show coach senang
        coach "Bagus, [player_name]! Skor kamu: [ch1_quiz_score]"
        coach "Kamu sudah memahami dasar-dasarnya. Terus berlatih!"
        $ add_percaya_diri(10)
        $ technical_points += 1
    else:
        show coach neutral
        coach "Skor kamu: [ch1_quiz_score]. Tidak apa-apa, [player_name]."
        coach "Belajar itu proses. Yang penting kamu mau mencoba dan belajar dari kesalahan."
        $ add_percaya_diri(5)
        $ brave_points += 1
    
    # Unlock gallery
    $ unlock_gallery("ch1_teknik_menendang")
    
    # Autosave
    $ renpy.save("auto-ch1")
    
    # Mark chapter complete
    $ ch1_completed = True
    $ chapter_clear = 1
    
    # Lanjut ke refleksi
    call ch1_reflection
    
    return

# ============================================
# BAB 1 REFLEKSI
# ============================================
label ch1_reflection:
    scene bg_reflection with fade
    
    play music reflection_theme fadein 2.0
    
    centered "{size=+10}Refleksi Bab 1{/size}"
    
    pause 1.0
    
    show mc neutral at center with dissolve
    
    mc "Hari ini aku belajar banyak tentang teknik menendang..."
    
    show mc fokus
    
    mc "Ternyata setiap teknik punya fungsinya masing-masing."
    
    show mc senang
    
    mc "Bukan hanya soal tendangan keras, tapi juga akurasi dan situasi yang tepat."
    
    scene bg_black with fade
    
    show text "{b}Ringkasan Pembelajaran:{/b}\n\n• Kaki bagian dalam: Umpan pendek akurat\n• Kaki bagian luar: Umpan melengkung\n• Punggung kaki: Tendangan keras jarak jauh\n\n{i}Kesalahan adalah bagian dari proses belajar.{/i}" at truecenter
    
    pause 5.0
    
    hide text with dissolve
    
    centered "Chapter 1 Selesai!"
    
    pause 1.0
    
    # Tampilkan skor
    call show_score_screen
    
    # Transisi ke bab berikutnya
    scene bg_black with fade
    
    pause 1.0
    
    centered "{size=+5}Bab 1 Selesai!{/size}\n\nLanjut ke Bab 2..."
    
    pause 2.0
    
    # Lanjut ke bab berikutnya
    return

# ============================================
# SHOW SCORE SCREEN
# ============================================
label show_score_screen:
    scene bg_black
    
    show text "{size=+10}Status Perkembangan{/size}\n\n{color=#4CAF50}Teknik:{/color} [teknik_score]\n{color=#FF9800}Percaya Diri:{/color} [percaya_diri]\n{color=#2196F3}Sportivitas:{/color} [sportivitas]" at truecenter
    
    pause 3.0
    
    hide text
    
    return
