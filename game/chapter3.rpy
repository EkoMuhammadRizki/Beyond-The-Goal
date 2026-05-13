# ============================================
# CHAPTER 3: Sundulan Penentu
# ============================================
# Materi: Teknik heading, permainan kecil, kerja sama tim, sportivitas

label ch3_intro:
    $ current_chapter = 3
    
    scene bg_black with fade
    
    centered "{size=+10}{color=#4CAF50}Chapter 3{/color}{/size}\n{size=+5}Sundulan Penentu{/size}"
    
    pause 2.0
    
    play music training_theme fadein 2.0
    
    scene bg_mini_field_2v2 with dissolve
    
    show coach neutral at center with dissolve
    
    coach "Selamat datang di chapter terakhir, [player_name]!"
    
    coach "Hari ini kita akan belajar teknik heading dan bermain dalam pertandingan kecil."
    
    show mc neutral at left with dissolve
    
    mc "Heading? Menyundul bola?"
    
    show coach fokus
    
    coach "Tepat! Heading adalah teknik penting, terutama untuk bola-bola udara."
    
    show bima takut at right with dissolve
    
    bima "Coach... aku takut menyundul bola... takut sakit..."
    
    show coach senang
    
    coach "Wajar merasa takut, Bima. Tapi dengan teknik yang benar, heading itu aman."
    
    show coach neutral
    
    coach "Yang penting adalah:"
    
    centered "{b}Teknik Heading:{/b}\n\n1. Gunakan dahi, bukan ubun-ubun\n2. Mata tetap terbuka\n3. Leher kaku, gerakkan dari pinggang\n4. Timing yang tepat\n5. Jangan takut, percaya diri"
    
    # Sembunyikan karakter lain agar fokus ke Dimas dan tidak bertabrakan
    hide mc
    hide bima
    hide coach
    
    # Tampilkan Dimas di kiri jauh agar tidak tertutup Coach
    show dimas neutral at left with dissolve
    
    dimas "Aku sudah siap bertanding, Coach!"
    
    # Tampilkan Coach di kanan jauh agar mereka berdialog berhadapan
    show coach senang at right with dissolve
    
    coach "Bagus, Dimas! Tapi ingat, ini bukan hanya soal menang."
    
    coach "Ini tentang kerja sama tim dan sportivitas."
    
    # Munculkan semua karakter dalam posisi berbaris rapi tanpa tumpang tindih
    show mc fokus:
        xalign 0.0 yalign 1.0
    show dimas neutral:
        xalign 0.33 yalign 1.0
    show coach neutral:
        xalign 0.66 yalign 1.0
    show bima takut:
        xalign 1.0 yalign 1.0
    with dissolve
    
    mc "Bima, aku akan bantu kamu belajar heading."
    
    menu:
        "Bagaimana kamu membantu Bima?"
        
        "Latihan bertahap dari bola pelan":
            $ add_sportivitas(10)
            $ supportive_points += 2
            
            show mc senang
            
            mc "Kita mulai dari bola yang pelan dulu, Bima."
            
            call ch3_scene_heading_slow
        
        "Minta Bima menonton dulu":
            $ add_teknik(5)
            $ technical_points += 1
            
            show mc neutral
            
            mc "Bima, tonton dulu bagaimana aku melakukannya."
            
            call ch3_scene_heading_demo
        
        "Beri motivasi dan langsung coba":
            $ add_percaya_diri(10)
            $ brave_points += 2
            
            show mc fokus
            
            mc "Bima, kamu pasti bisa! Ayo coba sekarang!"
            
            call ch3_scene_heading_brave
    
    # Lanjut ke mini game pertandingan
    call ch3_minigame
    
    return

# ============================================
# SCENE: HEADING SLOW PRACTICE
# ============================================
label ch3_scene_heading_slow:
    scene bg_training_cone with dissolve
    
    show mc senang at left
    show bima takut at right
    
    mc "Bima, aku akan lempar bola pelan ke arahmu."
    
    show mc neutral
    
    mc "Kamu cukup menyentuh bola dengan dahi. Tidak perlu keras."
    
    show bima fokus
    
    bima "Baik... aku akan coba..."
    
    play sound kick_ball
    
    show bima senang
    
    bima "Aku... aku berhasil! Dan tidak sakit!"
    
    show mc senang
    
    mc "Lihat? Dengan teknik yang benar, heading itu aman!"
    
    $ add_sportivitas(10)
    $ add_percaya_diri(10)
    
    show coach senang at center with dissolve
    
    coach "Excellent! Kalian berdua menunjukkan kerja sama yang luar biasa!"
    
    return

# ============================================
# SCENE: HEADING DEMONSTRATION
# ============================================
label ch3_scene_heading_demo:
    scene bg_mini_field_1v1 with dissolve
    
    show mc fokus at center
    
    mc "Perhatikan, Bima. Aku akan tunjukkan teknik heading yang benar."
    
    show mc neutral
    
    mc "Mata terbuka, fokus pada bola. Gunakan dahi, bukan ubun-ubun."
    
    play sound kick_ball
    with vpunch
    
    show mc senang
    
    mc "Lihat? Gerakannya dari pinggang, bukan hanya leher."
    
    show bima fokus at right with dissolve
    
    bima "Oh, jadi seperti itu... Aku mengerti sekarang."
    
    $ add_teknik(10)
    $ add_percaya_diri(5)
    
    return

# ============================================
# SCENE: HEADING BRAVE APPROACH
# ============================================
label ch3_scene_heading_brave:
    scene bg_mini_field_1v1 with dissolve
    
    show mc fokus at left
    show bima takut at right
    
    mc "Bima, kamu pasti bisa! Percaya pada dirimu sendiri!"
    
    show bima fokus
    
    bima "Tapi... bagaimana kalau aku gagal?"
    
    show mc senang
    
    mc "Gagal itu bagian dari belajar. Yang penting kamu berani mencoba!"
    
    show bima fokus
    
    bima "Baik... aku akan coba!"
    
    play sound kick_ball
    
    show bima senang
    
    bima "Aku berhasil! Terima kasih, [player_name]!"
    
    $ add_percaya_diri(15)
    $ add_sportivitas(10)
    
    return

# ============================================
# CHAPTER 3 MINIGAME: FINAL SMALL MATCH QUIZ
# ============================================
label ch3_minigame:
    scene bg_black with fade
    
    centered "{size=+10}Mini Game: Final Small Match{/size}\n\nPertandingan 2 vs 2!\nPilih keputusan terbaik dalam setiap situasi!"
    
    pause 2.0
    
    play music final_match_theme
    
    $ ch3_match_score = 0
    $ ch3_sportivitas_score = 0
    
    scene bg_mini_field_2v2 with dissolve
    
    play sound whistle
    
    centered "PERTANDINGAN DIMULAI!\nTim: [player_name] & Bima vs Dimas & Naya"
    
    # Situasi 1
    centered "Situasi 1:\nKamu menerima bola di tengah lapangan.\nBima bebas di sayap, tapi kamu juga punya peluang shooting."
    
    menu:
        "Apa yang kamu lakukan?"
        
        "Passing ke Bima yang bebas":
            $ ch3_match_score += 10
            $ ch3_sportivitas_score += 15
            $ add_sportivitas(10)
            $ supportive_points += 1
            play sound kick_ball
            centered "{color=#4CAF50}✓ KERJA SAMA TIM!{/color}\n\nBima menerima bola dengan baik!\n+10 Teknik, +15 Sportivitas"
        
        "Shooting sendiri":
            $ ch3_match_score += 5
            $ add_teknik(5)
            $ technical_points += 1
            play sound strong_kick
            with vpunch
            centered "{color=#FFC107}△ EGOIS{/color}\n\nTendanganmu meleset. Bima terbuka tadi.\n+5 Teknik, +0 Sportivitas"
        
        "Dribble melewati lawan":
            $ ch3_match_score += 8
            $ add_teknik(8)
            $ brave_points += 1
            play sound kick_ball
            centered "{color=#4CAF50}✓ BERANI!{/color}\n\nKamu berhasil melewati satu lawan!\n+8 Teknik"
    
    # Situasi 2
    centered "Situasi 2:\nBola melayang tinggi ke arahmu.\nKamu bisa heading atau membiarkan Bima yang mengambil."
    
    menu:
        "Apa yang kamu lakukan?"
        
        "Heading dengan percaya diri":
            $ ch3_match_score += 15
            $ add_teknik(10)
            $ add_percaya_diri(10)
            $ brave_points += 1
            play sound kick_ball
            with vpunch
            centered "{color=#4CAF50}✓ SEMPURNA!{/color}\n\nHeading-mu akurat!\n+15 Teknik, +10 Percaya Diri"
        
        "Biarkan Bima yang heading":
            $ ch3_match_score += 10
            $ ch3_sportivitas_score += 15
            $ add_sportivitas(15)
            $ supportive_points += 2
            play sound kick_ball
            centered "{color=#4CAF50}✓ PERCAYA TEMAN!{/color}\n\nBima berhasil heading! Dia senang kamu percaya padanya.\n+10 Teknik, +15 Sportivitas"
        
        "Kontrol dengan dada":
            $ ch3_match_score += 8
            $ add_teknik(8)
            $ technical_points += 1
            play sound kick_ball
            show text "{color=#2196F3}○ AMAN{/color}\n\nKontrol yang baik, tapi heading lebih efektif.\n+8 Teknik" at truecenter
            pause 2.0
            hide text
    
    # Situasi 3
    show text "Situasi 3:\nBima dijatuhkan oleh Dimas (tidak sengaja).\nBima terlihat kesakitan." at truecenter
    
    pause 3.0
    
    hide text
    
    menu:
        "Apa yang kamu lakukan?"
        
        "Bantu Bima berdiri":
            $ ch3_sportivitas_score += 20
            $ add_sportivitas(20)
            $ supportive_points += 2
            show text "{color=#4CAF50}✓ SPORTIVITAS TINGGI!{/color}\n\nKamu menunjukkan kepedulian pada teman.\n+20 Sportivitas" at truecenter
            pause 2.0
            hide text
        
        "Marah pada Dimas":
            $ ch3_sportivitas_score -= 10
            centered "{color=#F44336}✗ TIDAK SPORTIF{/color}\n\nItu tidak sengaja. Kamu harus lebih tenang.\n-10 Sportivitas"
        
        "Lanjutkan permainan":
            $ ch3_match_score += 5
            centered "{color=#FFC107}△ FOKUS MENANG{/color}\n\nPermainan lanjut, tapi kamu kurang peduli teman.\n+5 Teknik, +0 Sportivitas"
    
    # Situasi 4
    centered "Situasi 4:\nSkor 0-0, waktu hampir habis.\nKamu punya peluang emas untuk mencetak gol."
    
    menu:
        "Apa yang kamu lakukan?"
        
        "Shooting dengan punggung kaki":
            $ ch3_match_score += 15
            $ add_teknik(15)
            $ add_percaya_diri(10)
            $ brave_points += 1
            play sound strong_kick
            with vpunch
            play sound crowd_small
            centered "{color=#FFD700}★ GOOOAL! ★{/color}\n\nTendangan sempurna! Tim kalian menang!\n+15 Teknik, +10 Percaya Diri"
        
        "Passing ke Bima untuk finishing":
            $ ch3_match_score += 12
            $ ch3_sportivitas_score += 20
            $ add_sportivitas(20)
            $ supportive_points += 2
            play sound kick_ball
            pause 0.5
            play sound strong_kick
            with vpunch
            play sound crowd_small
            centered "{color=#FFD700}★ GOOOAL! ★{/color}\n\nBima mencetak gol! Kerja sama yang sempurna!\n+12 Teknik, +20 Sportivitas"
        
        "Dribble dulu untuk posisi lebih baik":
            $ ch3_match_score += 8
            $ add_teknik(8)
            play sound kick_ball
            centered "{color=#FFC107}△ TERLAMBAT{/color}\n\nWaktu habis sebelum kamu shooting. Skor 0-0.\n+8 Teknik"
    
    # Hasil Match
    call ch3_match_result
    
    return

# ============================================
# MATCH RESULT
# ============================================
label ch3_match_result:
    scene bg_reflection with dissolve
    
    play sound whistle
    
    show coach neutral at center with dissolve
    
    coach "Pertandingan selesai!"
    
    if ch3_match_score >= 40 and ch3_sportivitas_score >= 40:
        show coach senang
        coach "Luar biasa, [player_name]!"
        coach "Skor Teknik: [ch3_match_score] | Sportivitas: [ch3_sportivitas_score]"
        coach "Kamu tidak hanya bermain bagus, tapi juga menunjukkan sportivitas tinggi!"
        $ add_percaya_diri(25)
        $ balanced_points += 3
        $ ending_type = "balanced"
    elif ch3_match_score >= 40:
        show coach neutral
        coach "Teknik kamu bagus: [ch3_match_score]"
        coach "Tapi Sportivitas: [ch3_sportivitas_score]"
        coach "Ingat, sepak bola bukan hanya soal menang, tapi juga bagaimana kamu bermain."
        $ add_percaya_diri(15)
        $ technical_points += 2
        $ ending_type = "technical"
    elif ch3_sportivitas_score >= 40:
        show coach senang
        coach "Sportivitas kamu luar biasa: [ch3_sportivitas_score]"
        coach "Teknik: [ch3_match_score]"
        coach "Kamu adalah pemain yang membuat tim lebih baik!"
        $ add_percaya_diri(20)
        $ supportive_points += 3
        $ ending_type = "supportive"
    else:
        show coach neutral
        coach "Teknik: [ch3_match_score] | Sportivitas: [ch3_sportivitas_score]"
        coach "Masih ada yang perlu dipelajari, tapi yang penting kamu sudah berani mencoba!"
        $ add_percaya_diri(10)
        $ brave_points += 2
        $ ending_type = "learning"
    
    show bima senang at right with dissolve
    
    bima "Terima kasih, [player_name]! Aku tidak takut lagi menyundul bola!"
    
    show naya senang at left with dissolve
    
    naya "Kalian bermain dengan bagus!"
    
    # Solusi 1: Sembunyikan karakter lain agar tidak bertabrakan dengan Coach di tengah
    hide coach
    hide bima
    hide naya
    
    show dimas senang at center with dissolve
    
    dimas "Pertandingan yang seru! Ayo main lagi kapan-kapan!"
    
    $ add_sportivitas(15)
    
    # Unlock gallery
    $ unlock_gallery("ch3_heading_teamwork")
    
    # Autosave
    $ renpy.save("auto-ch3")
    
    # Mark chapter complete
    $ ch3_completed = True
    $ chapter_clear = 3
    
    # Lanjut ke refleksi
    call ch3_reflection
    
    return

# ============================================
# CHAPTER 3 REFLECTION
# ============================================
label ch3_reflection:
    scene bg_reflection with fade
    
    play music reflection_theme fadein 2.0
    
    centered "{size=+10}Refleksi Chapter 3{/size}"
    
    pause 1.0
    
    show mc neutral at center with dissolve
    
    mc "Hari ini aku belajar bahwa sepak bola bukan hanya soal skill individu..."
    
    show mc fokus
    
    mc "Tapi tentang bagaimana kita bermain bersama sebagai tim."
    
    show mc senang
    
    mc "Membantu teman mengatasi ketakutan mereka... itu lebih berarti daripada mencetak gol."
    
    scene bg_black with fade
    
    centered "{b}Ringkasan Pembelajaran:{/b}\n\n• Heading: Gunakan dahi, mata terbuka, timing tepat\n• Kerja sama tim lebih penting dari skill individu\n• Sportivitas: Peduli pada teman dan lawan\n• Keberanian mencoba hal baru\n\n{i}Menang bukan hanya tentang skor,\ntapi tentang bagaimana kita bermain bersama.{/i}"
    
    centered "Chapter 3 Selesai!"
    
    pause 1.0
    
    # Tampilkan skor akhir
    call show_score_screen
    
    # Transisi ke ending
    scene bg_black with fade
    
    pause 1.0
    
    centered "{size=+5}Perjalanan kita hampir selesai...{/size}"
    
    pause 2.0
    
    # Lanjut ke ending
    call game_ending
    
    return

# ============================================
# GAME ENDING
# ============================================
label game_ending:
    scene bg_black with fade
    
    pause 1.0
    
    scene bg_school_field with dissolve
    
    play music reflection_theme
    
    centered "{size=+15}{color=#4CAF50}Beyond The Goal{/color}{/size}"
    
    pause 2.0
    
    show mc senang at center with dissolve
    
    mc "Perjalanan ini mengajarkan aku banyak hal..."
    
    show mc neutral
    
    mc "Bukan hanya tentang teknik sepak bola..."
    
    show mc fokus
    
    mc "Tapi tentang percaya diri, kerja sama, dan keberanian untuk terus belajar."
    
    scene bg_black with fade
    
    centered "{i}Tidak semua pemain menjadi pencetak gol terbaik.{/i}"
    
    pause 2.0
    
    centered "{i}Tapi setiap pemain bisa menjadi alasan timnya terus bermain.{/i}"
    
    pause 2.0
    
    # Player Growth Summary
    call player_growth_summary
    
    # Credits
    call credits_scene
    
    return

# ============================================
# PLAYER GROWTH SUMMARY
# ============================================
label player_growth_summary:
    scene bg_reflection with fade
    
    centered "{size=+10}Player Growth Summary{/size}"
    
    pause 1.0
    
    centered "{b}Perkembangan [player_name]:{/b}\n\n{color=#4CAF50}Teknik:{/color} [teknik_score]\n{color=#FF9800}Percaya Diri:{/color} [percaya_diri]\n{color=#2196F3}Sportivitas:{/color} [sportivitas]"
    
    # Tentukan player style
    $ player_style = get_player_style()
    
    if player_style == "technical":
        centered "{b}Player Style:{/b}\n\n{color=#4CAF50}★ Technical Player ★{/color}\n\nKamu adalah pemain yang mengandalkan\npemahaman teknik dan strategi."
    elif player_style == "supportive":
        centered "{b}Player Style:{/b}\n\n{color=#E91E63}★ Supportive Player ★{/color}\n\nKamu adalah pemain yang membuat\ntim menjadi lebih baik."
    elif player_style == "brave":
        centered "{b}Player Style:{/b}\n\n{color=#FF9800}★ Brave Learner ★{/color}\n\nKamu adalah pemain yang berani\nmencoba dan belajar dari kesalahan."
    else:
        centered "{b}Player Style:{/b}\n\n{color=#9C27B0}★ Balanced Captain ★{/color}\n\nKamu adalah pemain yang seimbang\ndalam semua aspek permainan."
    
    return

# ============================================
# CREDITS SCENE
# ============================================
label credits_scene:
    scene bg_black with fade
    
    centered "{size=+15}Credits{/size}"
    
    pause 2.0
    
    centered "{b}Beyond The Goal{/b}\n\nVisual Novel Edukasi Sepak Bola"
    
    pause 2.0
    
    centered "{size=+5}Pengembang Game{/size}\n\n{b}Kristian Jonathan{/b}"
    
    pause 3.0
    
    centered "{i}\"Menang bukan hanya tentang mencetak gol,\ntapi tentang belajar, percaya diri,\ndan bermain bersama.\"{/i}"
    
    pause 3.0
    
    centered "Dibuat dengan Ren'Py\n\nVersion 1.0.0 - May 2026"
    
    pause 2.0
    
    centered "{size=+5}Terima kasih telah bermain!{/size}"
    
    pause 2.0
    
    # Kembali ke main menu
    return
