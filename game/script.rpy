# ============================================
# BEYOND THE GOAL - Main Script
# Visual Novel Edukasi Sepak Bola
# ============================================

# Game dimulai disini
label start:
    # Opening Cinematic
    call opening_cinematic
    
    # Main Menu akan muncul otomatis
    return

# ============================================
# OPENING CINEMATIC
# ============================================
label opening_cinematic:
    scene bg_black with fade
    
    # Narasi pembuka
    centered "{size=+10}Matahari sore di lapangan sekolah...{/size}"
    
    play sound "audio/whistle.wav"
    
    scene bg_school_field with dissolve
    
    pause 1.0
    
    centered "{i}Dulu aku pikir sepak bola cuma soal menang dan kalah.{/i}"
    
    pause 0.5
    
    centered "{i}Ternyata, setiap operan, setiap kesalahan, dan setiap latihan...{/i}"
    
    pause 0.5
    
    centered "{i}mengajarkanku sesuatu tentang diriku sendiri.{/i}"
    
    pause 1.0
    
    scene bg_black with fade
    
    # Logo Game
    show text "{size=+20}{color=#4CAF50}Beyond The Goal{/color}{/size}\n{size=-5}Menang bukan hanya tentang mencetak gol{/size}" at truecenter with dissolve
    
    play music "audio/main_menu_theme.mp3" fadein 2.0
    
    pause 3.0
    
    hide text with dissolve
    
    return

# ============================================
# CHAPTER SELECTION HUB
# ============================================
label chapter_select:
    scene bg_school_field with fade
    
    menu:
        "Pilih Chapter:"
        
        "Chapter 1: Umpan Pertama di Lapangan Senja":
            jump chapter_1
        
        "Chapter 2: Bola yang Tidak Mau Diam" if chapter_clear >= 1:
            jump chapter_2
        
        "Chapter 3: Sundulan Penentu" if chapter_clear >= 2:
            jump chapter_3
        
        "Kembali ke Menu":
            return

# ============================================
# LOAD CHAPTER FILES
# ============================================
# Chapter 1
label chapter_1:
    call ch1_intro
    return

# Chapter 2
label chapter_2:
    call ch2_intro
    return

# Chapter 3
label chapter_3:
    call ch3_intro
    return
