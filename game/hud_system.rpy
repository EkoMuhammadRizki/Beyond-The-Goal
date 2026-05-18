# ============================================
# HUD SYSTEM - Always Show Score Display
# ============================================

# Tampilkan HUD saat gameplay (bukan di menu)
init python:
    def should_show_hud():
        """Cek apakah HUD harus ditampilkan"""
        # Tampilkan HUD hanya saat gameplay, tidak di menu
        return not renpy.context()._menu

# Auto-show HUD during gameplay
label after_load:
    # Show HUD after loading
    show screen hud_display
    return

# Show HUD at start of each chapter
label show_hud:
    show screen hud_display
    return

label hide_hud:
    hide screen hud_display
    return

# ============================================
# TRANSITIONS & EFFECTS
# ============================================

# Shake effect untuk jawaban salah (menggunakan vpunch sebagai transition)
define shake = vpunch

# Flash effect untuk jawaban benar
transform flash:
    alpha 0.0
    linear 0.1 alpha 1.0
    linear 0.1 alpha 0.0
    linear 0.1 alpha 1.0

# Centered text transform
transform truecenter:
    xalign 0.5
    yalign 0.5

# ============================================
# CUSTOM TRANSITIONS
# ============================================

# Fade transition
define fade = Fade(0.5, 0.0, 0.5)

# Dissolve transition
define dissolve = Dissolve(0.5)

# VPunch untuk efek tendangan
define vpunch = Move((0, 10), (0, 0), 0.1, bounce=True, repeat=False, delay=0.0)

# Flash untuk efek cahaya
define flash = Fade(0.1, 0.0, 0.5, color="#FFFFFF")

# ============================================
# AUDIO HELPERS
# ============================================

# Define audio variables dengan fallback
define audio.training_theme = "audio/training_theme.mp3"
define audio.quiz_theme = "audio/quiz_theme.mp3"
define audio.final_match_theme = "audio/final_match_theme.mp3"
define audio.reflection_theme = "audio/reflection_theme.mp3"

define audio.whistle = "audio/whistle.wav"
define audio.kick_ball = "audio/kick_ball.wav"
define audio.strong_kick = "audio/strong_kick.wav"
define audio.crowd_small = "audio/crowd_small.wav"
define audio.correct = "audio/correct.wav"
define audio.wrong = "audio/wrong.wav"

# ============================================
# CENTERED TEXT HELPER
# ============================================

# Helper untuk menampilkan centered text
screen centered_text(text_content):
    zorder 200
    
    frame:
        xalign 0.5
        yalign 0.5
        background None
        padding (50, 30)
        
        text text_content:
            xalign 0.5
            yalign 0.5
            size 24
            color "#FFFFFF"
            text_align 0.5

# ============================================
# NOTIFICATION SYSTEM
# ============================================

screen notification(message, color="#4CAF50"):
    zorder 150
    
    frame:
        xalign 0.5
        yalign 0.1
        background color + "DD"
        padding (30, 20)
        
        text message:
            size 20
            color "#FFFFFF"
            xalign 0.5
    
    timer 2.0 action Hide("notification")

# Helper function untuk show notification
init python:
    def show_notification(message, color="#4CAF50"):
        renpy.show_screen("notification", message=message, color=color)
