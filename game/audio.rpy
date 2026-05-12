# ============================================
# AUDIO DEFINITIONS
# ============================================

# ============================================
# BACKGROUND MUSIC (BGM)
# ============================================

# Main Menu Theme - Upbeat dan hangat
define audio.main_menu_theme = "audio/main_menu_theme.mp3"

# Training Theme - Energik dan motivasi
define audio.training_theme = "audio/training_theme.mp3"

# Quiz Theme - Fokus dan konsentrasi
define audio.quiz_theme = "audio/quiz_theme.mp3"

# Final Match Theme - Intense dan emosional
define audio.final_match_theme = "audio/final_match_theme.mp3"

# Reflection Theme - Tenang dan reflektif
define audio.reflection_theme = "audio/reflection_theme.mp3"

# ============================================
# SOUND EFFECTS (SFX)
# ============================================

# Peluit pelatih
define audio.whistle = "audio/whistle.wav"

# Tendangan bola
define audio.kick_ball = "audio/kick_ball.wav"

# Tendangan keras
define audio.strong_kick = "audio/strong_kick.wav"

# Suara penonton kecil
define audio.crowd_small = "audio/crowd_small.wav"

# Jawaban benar
define audio.correct = "audio/correct.wav"

# Jawaban salah
define audio.wrong = "audio/wrong.wav"

# ============================================
# AUDIO PLACEHOLDER CREATION
# ============================================

init python:
    import os
    
    # Buat folder audio jika belum ada
    audio_path = os.path.join(config.gamedir, "audio")
    if not os.path.exists(audio_path):
        try:
            os.makedirs(audio_path)
        except:
            pass
    
    # Daftar file audio yang dibutuhkan
    required_audio = [
        "main_menu_theme.mp3",
        "training_theme.mp3",
        "quiz_theme.mp3",
        "final_match_theme.mp3",
        "reflection_theme.mp3",
        "whistle.wav",
        "kick_ball.wav",
        "strong_kick.wav",
        "crowd_small.wav",
        "correct.wav",
        "wrong.wav"
    ]
    
    # Note: Placeholder audio akan menggunakan silence
    # Ganti dengan file audio asli saat production
