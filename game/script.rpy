# ============================================
# BEYOND THE GOAL - Main Script
# Visual Novel Edukasi Sepak Bola
# ============================================

# Game dimulai disini
label start:
    # Opening Cinematic
    call opening_cinematic
    
    # Langsung mulai Chapter 1
    call chapter_1
    
    # Setelah Chapter 1, lanjut ke Chapter 2
    call chapter_2
    
    # Setelah Chapter 2, lanjut ke Chapter 3
    call chapter_3
    
    # Setelah semua chapter selesai, kembali ke main menu
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
