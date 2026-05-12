# ============================================
# CUSTOM SCREENS FOR BEYOND THE GOAL
# ============================================

# ============================================
# HUD SCORE DISPLAY
# ============================================
screen hud_display():
    zorder 100
    
    frame:
        xalign 0.98
        yalign 0.02
        xsize 200
        ysize 150
        background "#00000080"
        
        vbox:
            spacing 5
            xalign 0.5
            yalign 0.5
            
            text "{b}Status{/b}" size 18 xalign 0.5 color "#FFFFFF"
            
            hbox:
                spacing 5
                text "⚽" size 16
                text "Teknik:" size 14 color "#4CAF50"
                text "[teknik_score]" size 14 color "#FFFFFF"
            
            hbox:
                spacing 5
                text "💪" size 16
                text "Percaya Diri:" size 14 color "#FF9800"
                text "[percaya_diri]" size 14 color "#FFFFFF"
            
            hbox:
                spacing 5
                text "🤝" size 16
                text "Sportivitas:" size 14 color "#2196F3"
                text "[sportivitas]" size 14 color "#FFFFFF"

# ============================================
# MAIN MENU CUSTOM
# ============================================
screen main_menu():
    tag menu
    
    # Background
    add "bg_school_field"
    
    # Overlay gelap
    add Solid("#00000060")
    
    # Logo Game
    frame:
        xalign 0.5
        yalign 0.25
        background None
        
        vbox:
            spacing 10
            xalign 0.5
            
            text "{size=+20}{color=#4CAF50}Beyond The Goal{/color}{/size}" xalign 0.5
            text "{size=-2}Menang bukan hanya tentang mencetak gol{/size}" xalign 0.5 color "#FFFFFF"
    
    # Menu Buttons
    frame:
        xalign 0.5
        yalign 0.65
        background "#00000080"
        padding (40, 30)
        
        vbox:
            spacing 15
            xalign 0.5
            
            textbutton "Mulai Bermain" action Start() xsize 300 ysize 50
            textbutton "Chapter Select" action Show("chapter_select_screen") xsize 300 ysize 50
            textbutton "Gallery Materi" action Show("gallery_screen") xsize 300 ysize 50
            textbutton "Load Game" action ShowMenu("load") xsize 300 ysize 50
            textbutton "Pengaturan" action ShowMenu("preferences") xsize 300 ysize 50
            textbutton "Kredit" action Show("credits_screen") xsize 300 ysize 50
            textbutton "Keluar" action Quit(confirm=True) xsize 300 ysize 50

# ============================================
# CHAPTER SELECT SCREEN
# ============================================
screen chapter_select_screen():
    tag menu
    modal True
    
    add "bg_school_field"
    add Solid("#00000080")
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600
        background "#1a1a1a"
        
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            
            text "{size=+10}Pilih Bab{/size}" xalign 0.5 color "#4CAF50"
            
            null height 20
            
            # Chapter 1
            frame:
                xsize 700
                ysize 100
                background "#2a2a2a"
                
                hbox:
                    spacing 20
                    xalign 0.5
                    yalign 0.5
                    
                    text "1" size 40 color "#4CAF50"
                    
                    vbox:
                        spacing 5
                        text "Umpan Pertama di Lapangan Senja" size 18 color "#FFFFFF"
                        text "Materi: Teknik Menendang Bola" size 14 color "#AAAAAA"
                    
                    textbutton "Mulai" action [Hide("chapter_select_screen"), Jump("chapter_1")] xsize 100
            
            # Chapter 2
            if chapter_clear >= 1:
                frame:
                    xsize 700
                    ysize 100
                    background "#2a2a2a"
                    
                    hbox:
                        spacing 20
                        xalign 0.5
                        yalign 0.5
                        
                        text "2" size 40 color "#4CAF50"
                        
                        vbox:
                            spacing 5
                            text "Bola yang Tidak Mau Diam" size 18 color "#FFFFFF"
                            text "Materi: Kontrol Bola & Dribbling" size 14 color "#AAAAAA"
                        
                        textbutton "Mulai" action [Hide("chapter_select_screen"), Jump("chapter_2")] xsize 100
            else:
                frame:
                    xsize 700
                    ysize 100
                    background "#1a1a1a"
                    
                    hbox:
                        spacing 20
                        xalign 0.5
                        yalign 0.5
                        
                        text "2" size 40 color "#666666"
                        
                        vbox:
                            spacing 5
                            text "Bola yang Tidak Mau Diam" size 18 color "#666666"
                            text "Selesaikan Bab 1 terlebih dahulu" size 14 color "#666666"
            
            # Chapter 3
            if chapter_clear >= 2:
                frame:
                    xsize 700
                    ysize 100
                    background "#2a2a2a"
                    
                    hbox:
                        spacing 20
                        xalign 0.5
                        yalign 0.5
                        
                        text "3" size 40 color "#4CAF50"
                        
                        vbox:
                            spacing 5
                            text "Sundulan Penentu" size 18 color "#FFFFFF"
                            text "Materi: Heading & Kerja Sama Tim" size 14 color "#AAAAAA"
                        
                        textbutton "Mulai" action [Hide("chapter_select_screen"), Jump("chapter_3")] xsize 100
            else:
                frame:
                    xsize 700
                    ysize 100
                    background "#1a1a1a"
                    
                    hbox:
                        spacing 20
                        xalign 0.5
                        yalign 0.5
                        
                        text "3" size 40 color "#666666"
                        
                        vbox:
                            spacing 5
                            text "Sundulan Penentu" size 18 color "#666666"
                            text "Selesaikan Bab 2 terlebih dahulu" size 14 color "#666666"
            
            null height 20
            
            textbutton "Kembali" action [Hide("chapter_select_screen"), ShowMenu("main_menu")] xalign 0.5 xsize 200

# ============================================
# GALLERY MATERI SCREEN
# ============================================
screen gallery_screen():
    tag menu
    modal True
    
    add "bg_reflection"
    add Solid("#00000080")
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 700
        background "#1a1a1a"
        
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            
            text "{size=+10}Materi Pembelajaran{/size}" xalign 0.5 color "#4CAF50"
            
            null height 10
            
            viewport:
                scrollbars "vertical"
                mousewheel True
                xsize 850
                ysize 550
                
                vbox:
                    spacing 15
                    
                    # Materi 1
                    if "ch1_teknik_menendang" in gallery_unlocked:
                        frame:
                            xsize 800
                            background "#2a2a2a"
                            padding (20, 20)
                            
                            vbox:
                                spacing 10
                                text "{b}Teknik Menendang Bola{/b}" size 18 color "#4CAF50"
                                text "• Kaki Bagian Dalam: Untuk umpan pendek akurat" size 14
                                text "• Kaki Bagian Luar: Untuk umpan melengkung" size 14
                                text "• Punggung Kaki: Untuk tendangan keras jarak jauh" size 14
                    
                    # Materi 2
                    if "ch2_kontrol_dribbling" in gallery_unlocked:
                        frame:
                            xsize 800
                            background "#2a2a2a"
                            padding (20, 20)
                            
                            vbox:
                                spacing 10
                                text "{b}Kontrol Bola & Dribbling{/b}" size 18 color "#4CAF50"
                                text "• Telapak Kaki: Kontrol bola datar" size 14
                                text "• Dada: Kontrol bola melayang tinggi" size 14
                                text "• Paha: Kontrol bola melayang sedang" size 14
                                text "• Dribbling: Sentuhan lembut, irama teratur" size 14
                    
                    # Materi 3
                    if "ch3_heading_teamwork" in gallery_unlocked:
                        frame:
                            xsize 800
                            background "#2a2a2a"
                            padding (20, 20)
                            
                            vbox:
                                spacing 10
                                text "{b}Heading & Kerja Sama Tim{/b}" size 18 color "#4CAF50"
                                text "• Gunakan dahi, bukan ubun-ubun" size 14
                                text "• Mata tetap terbuka" size 14
                                text "• Leher kaku, gerakkan dari pinggang" size 14
                                text "• Timing yang tepat" size 14
                                text "• Kerja sama tim lebih penting dari skill individu" size 14
                    
                    if len(gallery_unlocked) == 0:
                        text "Belum ada materi yang terbuka.\nSelesaikan bab untuk membuka materi." xalign 0.5 size 16 color "#AAAAAA"
            
            textbutton "Kembali" action [Hide("gallery_screen"), ShowMenu("main_menu")] xalign 0.5 xsize 200

# ============================================
# STYLE CUSTOMIZATION
# ============================================
style button:
    background "#4CAF50"
    hover_background "#66BB6A"
    xalign 0.5
    yalign 0.5

style button_text:
    size 18
    color "#FFFFFF"
    hover_color "#FFFFFF"
    xalign 0.5
    yalign 0.5


# ============================================
# CREDITS SCREEN
# ============================================
screen credits_screen():
    tag menu
    modal True
    
    add "bg_school_field"
    add Solid("#00000090")
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 800
        background "#1a1a1a"
        
        viewport:
            scrollbars "vertical"
            mousewheel True
            xsize 950
            ysize 750
            
            vbox:
                spacing 30
                xalign 0.5
                
                # Header
                null height 20
                
                text "{size=+15}{color=#4CAF50}Beyond The Goal{/color}{/size}" xalign 0.5
                text "{size=-2}{color=#AAAAAA}Menang bukan hanya tentang mencetak gol{/color}{/size}" xalign 0.5
                
                null height 30
                
                # Pengembang
                frame:
                    xsize 900
                    background "#2a2a2a"
                    padding (30, 20)
                    
                    vbox:
                        spacing 10
                        text "{b}{size=+5}{color=#4CAF50}Pengembang Game{/color}{/size}{/b}"
                        null height 5
                        text "{size=+2}{color=#FFFFFF}Kristian Jonathan{/color}{/size}"
                
                # Tujuan Game
                frame:
                    xsize 900
                    background "#2a2a2a"
                    padding (30, 20)
                    
                    vbox:
                        spacing 10
                        text "{b}{size=+5}{color=#FF9800}Tujuan Game{/color}{/size}{/b}"
                        null height 5
                        text "{size=18}{color=#FFFFFF}Game ini dibuat sebagai media pembelajaran interaktif untuk mengajarkan teknik dasar sepak bola kepada siswa SMA. Melalui pendekatan visual novel, pemain tidak hanya belajar teknik olahraga, tetapi juga nilai-nilai penting seperti kerja sama tim, sportivitas, percaya diri, dan keberanian untuk terus belajar dari kesalahan.{/color}{/size}"
                
                # Alasan Dibuat
                frame:
                    xsize 900
                    background "#2a2a2a"
                    padding (30, 20)
                    
                    vbox:
                        spacing 10
                        text "{b}{size=+5}{color=#2196F3}Alasan Pembuatan Game{/color}{/size}{/b}"
                        null height 5
                        text "{size=18}{color=#FFFFFF}Pembelajaran olahraga, khususnya sepak bola, seringkali hanya fokus pada aspek fisik dan teknik semata. Padahal, ada nilai-nilai karakter yang sangat penting untuk dikembangkan. Game ini hadir untuk mengisi kekosongan tersebut dengan menyajikan pembelajaran yang holistik - menggabungkan teknik sepak bola dengan pengembangan karakter melalui cerita yang menarik dan interaktif.{/color}{/size}"
                        null height 10
                        text "{size=18}{color=#FFFFFF}Dengan format visual novel, siswa dapat belajar dalam suasana yang menyenangkan, tidak tertekan, dan dapat mengeksplorasi berbagai pilihan serta konsekuensinya dalam lingkungan yang aman.{/color}{/size}"
                
                # Makna Judul
                frame:
                    xsize 900
                    background "#2a2a2a"
                    padding (30, 20)
                    
                    vbox:
                        spacing 10
                        text "{b}{size=+5}{color=#9C27B0}Makna Judul \"Beyond The Goal\"{/color}{/size}{/b}"
                        null height 5
                        text "{size=18}{color=#FFFFFF}{i}\"Beyond The Goal\"{/i} memiliki makna ganda yang mendalam:{/color}{/size}"
                        null height 10
                        
                        text "{size=18}{color=#FFD700}1. {b}Melampaui Gawang{/b}{/color}{/size}"
                        text "{size=16}{color=#CCCCCC}   Sepak bola bukan hanya tentang mencetak gol ke gawang lawan. Ada proses pembelajaran, latihan, kerja sama, dan perjuangan yang terjadi sebelum gol itu tercipta. Judul ini mengajak kita melihat lebih jauh dari sekadar hasil akhir.{/color}{/size}"
                        
                        null height 10
                        
                        text "{size=18}{color=#FFD700}2. {b}Melampaui Tujuan{/b}{/color}{/size}"
                        text "{size=16}{color=#CCCCCC}   Tujuan bermain sepak bola bukan hanya untuk menang, tetapi untuk berkembang sebagai individu dan tim. Kemenangan sejati adalah ketika kita belajar sesuatu yang berharga, menjadi lebih percaya diri, dan membantu orang lain tumbuh bersama kita.{/color}{/size}"
                        
                        null height 10
                        
                        text "{size=18}{color=#FFD700}3. {b}Perjalanan Lebih Penting dari Destinasi{/b}{/color}{/size}"
                        text "{size=16}{color=#CCCCCC}   Judul ini menekankan bahwa proses pembelajaran, usaha, dan pengalaman yang kita dapatkan jauh lebih berharga daripada sekadar hasil akhir. Setiap kesalahan adalah pelajaran, setiap latihan adalah kemajuan, dan setiap teman adalah bagian dari perjalanan kita.{/color}{/size}"
                
                # Filosofi Game
                frame:
                    xsize 900
                    background "#2a2a2a"
                    padding (30, 20)
                    
                    vbox:
                        spacing 10
                        text "{b}{size=+5}{color=#E91E63}Filosofi Game{/color}{/size}{/b}"
                        null height 5
                        text "{size=18}{color=#FFFFFF}• Kesalahan adalah bagian dari proses belajar{/color}{/size}"
                        text "{size=18}{color=#FFFFFF}• Teknik dapat dipahami dan dilatih, bukan bakat semata{/color}{/size}"
                        text "{size=18}{color=#FFFFFF}• Kerja sama tim lebih penting daripada bermain egois{/color}{/size}"
                        text "{size=18}{color=#FFFFFF}• Sportivitas dan keberanian membantu teman adalah inti perkembangan karakter{/color}{/size}"
                        text "{size=18}{color=#FFFFFF}• Menguasai bola berarti juga belajar menguasai emosi dan rasa takut{/color}{/size}"
                
                # Pesan Penutup
                null height 20
                
                text "{size=18}{color=#FFD700}{i}\"Tidak semua pemain menjadi pencetak gol terbaik.{/i}{/color}{/size}" xalign 0.5
                text "{size=18}{color=#FFD700}{i}Tapi setiap pemain bisa menjadi alasan timnya terus bermain.\"{/i}{/color}{/size}" xalign 0.5
                
                null height 20
                
                # Teknologi
                frame:
                    xsize 900
                    background "#2a2a2a"
                    padding (30, 20)
                    
                    vbox:
                        spacing 10
                        text "{b}{color=#4CAF50}Dibuat dengan:{/color}{/b}"
                        text "{size=16}{color=#CCCCCC}Ren'Py Visual Novel Engine{/color}{/size}"
                        text "{size=16}{color=#CCCCCC}Version 1.0.0 - May 2026{/color}{/size}"
                
                null height 30
                
                text "{size=-2}{color=#AAAAAA}Terima kasih telah bermain!{/color}{/size}" xalign 0.5
                
                null height 30
        
        # Tombol Kembali
        textbutton "Kembali" action [Hide("credits_screen"), ShowMenu("main_menu")] xalign 0.5 yalign 0.95 xsize 200
