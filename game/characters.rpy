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
# CHARACTER SPRITE TRANSFORMS
# ============================================
# Transform untuk menyeimbangkan ukuran visual karakter

transform mc_sprite:
    yalign 1.0
    zoom 1.0

transform coach_sprite:
    yalign 1.0
    zoom 1.08

transform naya_sprite:
    yalign 1.0
    zoom 0.92

transform bima_sprite:
    yalign 1.0
    zoom 0.95

transform dimas_sprite:
    yalign 1.0
    zoom 1.0

# ============================================
# CHARACTER SPRITES
# ============================================

# Pemain Utama - Raka/Rani
image mc neutral = At("images/characters/mc_neutral.png", mc_sprite)
image mc senang = At("images/characters/mc_senang.png", mc_sprite)
image mc marah = At("images/characters/mc_marah.png", mc_sprite)
image mc sedih = At("images/characters/mc_sedih.png", mc_sprite)
image mc fokus = At("images/characters/mc_fokus.png", mc_sprite)
image mc takut = At("images/characters/mc_takut.png", mc_sprite)

# Coach Arya
image coach neutral = At("images/characters/coach_neutral.png", coach_sprite)
image coach senang = At("images/characters/coach_senang.png", coach_sprite)
image coach marah = At("images/characters/coach_marah.png", coach_sprite)
image coach fokus = At("images/characters/coach_fokus.png", coach_sprite)

# Naya
image naya neutral = At("images/characters/naya_neutral.png", naya_sprite)
image naya senang = At("images/characters/naya_senang.png", naya_sprite)
image naya sedih = At("images/characters/naya_sedih.png", naya_sprite)
image naya fokus = At("images/characters/naya_fokus.png", naya_sprite)
image naya takut = At("images/characters/naya_takut.png", naya_sprite)

# Bima
image bima neutral = At("images/characters/bima_neutral.png", bima_sprite)
image bima senang = At("images/characters/bima_senang.png", bima_sprite)
image bima sedih = At("images/characters/bima_sedih.png", bima_sprite)
image bima takut = At("images/characters/bima_takut.png", bima_sprite)
image bima fokus = At("images/characters/bima_fokus.png", bima_sprite)

# Dimas
image dimas neutral = At("images/characters/dimas_neutral.png", dimas_sprite)
image dimas senang = At("images/characters/dimas_senang.png", dimas_sprite)
image dimas marah = At("images/characters/dimas_marah.png", dimas_sprite)
image dimas fokus = At("images/characters/dimas_fokus.png", dimas_sprite)

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
