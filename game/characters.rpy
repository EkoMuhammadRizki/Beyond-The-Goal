# ============================================
# CHARACTER DEFINITIONS
# ============================================

# Karakter Utama (nama bisa dipilih)
define mc = Character("[player_name]", color="#4CAF50", who_bold=True)

# Coach Arya - Pelatih tegas namun ramah
define coach = Character("Coach Arya", color="#FF9800", who_bold=True)

# Naya - Ceria dan suportif
define naya = Character("Naya", color="#E91E63", who_bold=True)

# Bima - Pemalu dan takut gagal
define bima = Character("Bima", color="#2196F3", who_bold=True)

# Dimas - Kompetitif namun sportif
define dimas = Character("Dimas", color="#9C27B0", who_bold=True)

# Narrator untuk refleksi
define narrator = Character(None, kind=nvl)

# ============================================
# CHARACTER SPRITES
# ============================================

# Pemain Utama - Raka/Rani
image mc neutral = "images/characters/mc_neutral.png"
image mc senang = "images/characters/mc_senang.png"
image mc marah = "images/characters/mc_marah.png"
image mc sedih = "images/characters/mc_sedih.png"
image mc fokus = "images/characters/mc_fokus.png"
image mc takut = "images/characters/mc_takut.png"

# Coach Arya
image coach neutral = "images/characters/coach_neutral.png"
image coach senang = "images/characters/coach_senang.png"
image coach marah = "images/characters/coach_marah.png"
image coach fokus = "images/characters/coach_fokus.png"

# Naya
image naya neutral = "images/characters/naya_neutral.png"
image naya senang = "images/characters/naya_senang.png"
image naya sedih = "images/characters/naya_sedih.png"
image naya fokus = "images/characters/naya_fokus.png"

# Bima
image bima neutral = "images/characters/bima_neutral.png"
image bima senang = "images/characters/bima_senang.png"
image bima sedih = "images/characters/bima_sedih.png"
image bima takut = "images/characters/bima_takut.png"
image bima fokus = "images/characters/bima_fokus.png"

# Dimas
image dimas neutral = "images/characters/dimas_neutral.png"
image dimas senang = "images/characters/dimas_senang.png"
image dimas marah = "images/characters/dimas_marah.png"
image dimas fokus = "images/characters/dimas_fokus.png"

# ============================================
# BACKGROUND IMAGES
# ============================================

image bg_black = Solid("#000000")
image bg_school_field = "images/backgrounds/school_field.png"
image bg_training_cone = "images/backgrounds/training_cone.png"
image bg_wall_training = "images/backgrounds/wall_training.png"
image bg_mini_field_1v1 = "images/backgrounds/mini_field_1v1.png"
image bg_mini_field_2v2 = "images/backgrounds/mini_field_2v2.png"
image bg_reflection = "images/backgrounds/reflection_room.png"

# ============================================
# PLACEHOLDER GENERATOR
# ============================================
# Jika image tidak ditemukan, gunakan placeholder

init python:
    # Fungsi untuk membuat placeholder character
    def create_placeholder_character(name, color):
        return Solid(color, xysize=(300, 600))
    
    # Fungsi untuk membuat placeholder background
    def create_placeholder_bg(name, color):
        return Solid(color, xysize=(1920, 1080))
