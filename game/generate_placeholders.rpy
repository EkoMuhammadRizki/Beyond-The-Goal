# ============================================
# PLACEHOLDER IMAGE GENERATOR
# ============================================
# Script ini akan membuat placeholder images otomatis

init python:
    import os
    
    def create_placeholder_images():
        """Generate placeholder images untuk character dan background"""
        
        # Definisi warna untuk setiap karakter
        character_colors = {
            "mc": "#4CAF50",      # Hijau
            "coach": "#FF9800",   # Orange
            "naya": "#E91E63",    # Pink
            "bima": "#2196F3",    # Biru
            "dimas": "#9C27B0"    # Ungu
        }
        
        # Definisi warna untuk background
        background_colors = {
            "school_field": "#7CB342",      # Hijau lapangan
            "training_cone": "#9CCC65",     # Hijau muda
            "wall_training": "#8D6E63",     # Coklat
            "mini_field_1v1": "#66BB6A",    # Hijau terang
            "mini_field_2v2": "#4CAF50",    # Hijau
            "reflection_room": "#455A64"    # Abu-abu biru
        }
        
        # Path untuk menyimpan images
        char_path = os.path.join(config.gamedir, "images", "characters")
        bg_path = os.path.join(config.gamedir, "images", "backgrounds")
        
        # Buat folder jika belum ada
        for path in [char_path, bg_path]:
            if not os.path.exists(path):
                try:
                    os.makedirs(path)
                except:
                    pass
        
        # Note: Placeholder akan menggunakan Solid color dari Ren'Py
        # Tidak perlu membuat file PNG karena akan menggunakan displayable
        
        return True

# Jalankan saat game dimulai
init:
    $ create_placeholder_images()

# ============================================
# DEFINE PLACEHOLDER IMAGES USING SOLID
# ============================================

# Character Placeholders (300x600)
image mc_neutral_placeholder = Solid("#4CAF50", xysize=(300, 600))
image mc_senang_placeholder = Solid("#66BB6A", xysize=(300, 600))
image mc_marah_placeholder = Solid("#2E7D32", xysize=(300, 600))
image mc_sedih_placeholder = Solid("#388E3C", xysize=(300, 600))
image mc_fokus_placeholder = Solid("#43A047", xysize=(300, 600))
image mc_takut_placeholder = Solid("#1B5E20", xysize=(300, 600))

image coach_neutral_placeholder = Solid("#FF9800", xysize=(300, 600))
image coach_senang_placeholder = Solid("#FFB74D", xysize=(300, 600))
image coach_marah_placeholder = Solid("#F57C00", xysize=(300, 600))
image coach_fokus_placeholder = Solid("#FB8C00", xysize=(300, 600))

image naya_neutral_placeholder = Solid("#E91E63", xysize=(300, 600))
image naya_senang_placeholder = Solid("#F06292", xysize=(300, 600))
image naya_sedih_placeholder = Solid("#C2185B", xysize=(300, 600))
image naya_fokus_placeholder = Solid("#D81B60", xysize=(300, 600))

image bima_neutral_placeholder = Solid("#2196F3", xysize=(300, 600))
image bima_senang_placeholder = Solid("#64B5F6", xysize=(300, 600))
image bima_sedih_placeholder = Solid("#1976D2", xysize=(300, 600))
image bima_takut_placeholder = Solid("#0D47A1", xysize=(300, 600))
image bima_fokus_placeholder = Solid("#1E88E5", xysize=(300, 600))

image dimas_neutral_placeholder = Solid("#9C27B0", xysize=(300, 600))
image dimas_senang_placeholder = Solid("#BA68C8", xysize=(300, 600))
image dimas_marah_placeholder = Solid("#7B1FA2", xysize=(300, 600))
image dimas_fokus_placeholder = Solid("#8E24AA", xysize=(300, 600))

# Background Placeholders (1920x1080)
image bg_school_field_placeholder = Solid("#7CB342", xysize=(1920, 1080))
image bg_training_cone_placeholder = Solid("#9CCC65", xysize=(1920, 1080))
image bg_wall_training_placeholder = Solid("#8D6E63", xysize=(1920, 1080))
image bg_mini_field_1v1_placeholder = Solid("#66BB6A", xysize=(1920, 1080))
image bg_mini_field_2v2_placeholder = Solid("#4CAF50", xysize=(1920, 1080))
image bg_reflection_placeholder = Solid("#455A64", xysize=(1920, 1080))

# ============================================
# FALLBACK SYSTEM
# ============================================
# Jika image asli tidak ditemukan, gunakan placeholder

init python:
    def get_image_or_placeholder(image_name, placeholder_name):
        """Return image asli atau placeholder jika tidak ditemukan"""
        try:
            renpy.has_image(image_name)
            return image_name
        except:
            return placeholder_name

# Override image definitions dengan fallback
image mc neutral = ConditionSwitch(
    "renpy.loadable('images/characters/mc_neutral.png')", "images/characters/mc_neutral.png",
    "True", "mc_neutral_placeholder"
)

image mc senang = ConditionSwitch(
    "renpy.loadable('images/characters/mc_senang.png')", "images/characters/mc_senang.png",
    "True", "mc_senang_placeholder"
)

image mc marah = ConditionSwitch(
    "renpy.loadable('images/characters/mc_marah.png')", "images/characters/mc_marah.png",
    "True", "mc_marah_placeholder"
)

image mc sedih = ConditionSwitch(
    "renpy.loadable('images/characters/mc_sedih.png')", "images/characters/mc_sedih.png",
    "True", "mc_sedih_placeholder"
)

image mc fokus = ConditionSwitch(
    "renpy.loadable('images/characters/mc_fokus.png')", "images/characters/mc_fokus.png",
    "True", "mc_fokus_placeholder"
)

image mc takut = ConditionSwitch(
    "renpy.loadable('images/characters/mc_takut.png')", "images/characters/mc_takut.png",
    "True", "mc_takut_placeholder"
)

# Coach
image coach neutral = ConditionSwitch(
    "renpy.loadable('images/characters/coach_neutral.png')", "images/characters/coach_neutral.png",
    "True", "coach_neutral_placeholder"
)

image coach senang = ConditionSwitch(
    "renpy.loadable('images/characters/coach_senang.png')", "images/characters/coach_senang.png",
    "True", "coach_senang_placeholder"
)

image coach marah = ConditionSwitch(
    "renpy.loadable('images/characters/coach_marah.png')", "images/characters/coach_marah.png",
    "True", "coach_marah_placeholder"
)

image coach fokus = ConditionSwitch(
    "renpy.loadable('images/characters/coach_fokus.png')", "images/characters/coach_fokus.png",
    "True", "coach_fokus_placeholder"
)

# Naya
image naya neutral = ConditionSwitch(
    "renpy.loadable('images/characters/naya_neutral.png')", "images/characters/naya_neutral.png",
    "True", "naya_neutral_placeholder"
)

image naya senang = ConditionSwitch(
    "renpy.loadable('images/characters/naya_senang.png')", "images/characters/naya_senang.png",
    "True", "naya_senang_placeholder"
)

image naya sedih = ConditionSwitch(
    "renpy.loadable('images/characters/naya_sedih.png')", "images/characters/naya_sedih.png",
    "True", "naya_sedih_placeholder"
)

image naya fokus = ConditionSwitch(
    "renpy.loadable('images/characters/naya_fokus.png')", "images/characters/naya_fokus.png",
    "True", "naya_fokus_placeholder"
)

# Bima
image bima neutral = ConditionSwitch(
    "renpy.loadable('images/characters/bima_neutral.png')", "images/characters/bima_neutral.png",
    "True", "bima_neutral_placeholder"
)

image bima senang = ConditionSwitch(
    "renpy.loadable('images/characters/bima_senang.png')", "images/characters/bima_senang.png",
    "True", "bima_senang_placeholder"
)

image bima sedih = ConditionSwitch(
    "renpy.loadable('images/characters/bima_sedih.png')", "images/characters/bima_sedih.png",
    "True", "bima_sedih_placeholder"
)

image bima takut = ConditionSwitch(
    "renpy.loadable('images/characters/bima_takut.png')", "images/characters/bima_takut.png",
    "True", "bima_takut_placeholder"
)

image bima fokus = ConditionSwitch(
    "renpy.loadable('images/characters/bima_fokus.png')", "images/characters/bima_fokus.png",
    "True", "bima_fokus_placeholder"
)

# Dimas
image dimas neutral = ConditionSwitch(
    "renpy.loadable('images/characters/dimas_neutral.png')", "images/characters/dimas_neutral.png",
    "True", "dimas_neutral_placeholder"
)

image dimas senang = ConditionSwitch(
    "renpy.loadable('images/characters/dimas_senang.png')", "images/characters/dimas_senang.png",
    "True", "dimas_senang_placeholder"
)

image dimas marah = ConditionSwitch(
    "renpy.loadable('images/characters/dimas_marah.png')", "images/characters/dimas_marah.png",
    "True", "dimas_marah_placeholder"
)

image dimas fokus = ConditionSwitch(
    "renpy.loadable('images/characters/dimas_fokus.png')", "images/characters/dimas_fokus.png",
    "True", "dimas_fokus_placeholder"
)

# Backgrounds
image bg_school_field = ConditionSwitch(
    "renpy.loadable('images/backgrounds/school_field.png')", "images/backgrounds/school_field.png",
    "True", "bg_school_field_placeholder"
)

image bg_training_cone = ConditionSwitch(
    "renpy.loadable('images/backgrounds/training_cone.png')", "images/backgrounds/training_cone.png",
    "True", "bg_training_cone_placeholder"
)

image bg_wall_training = ConditionSwitch(
    "renpy.loadable('images/backgrounds/wall_training.png')", "images/backgrounds/wall_training.png",
    "True", "bg_wall_training_placeholder"
)

image bg_mini_field_1v1 = ConditionSwitch(
    "renpy.loadable('images/backgrounds/mini_field_1v1.png')", "images/backgrounds/mini_field_1v1.png",
    "True", "bg_mini_field_1v1_placeholder"
)

image bg_mini_field_2v2 = ConditionSwitch(
    "renpy.loadable('images/backgrounds/mini_field_2v2.png')", "images/backgrounds/mini_field_2v2.png",
    "True", "bg_mini_field_2v2_placeholder"
)

image bg_reflection = ConditionSwitch(
    "renpy.loadable('images/backgrounds/reflection_room.png')", "images/backgrounds/reflection_room.png",
    "True", "bg_reflection_placeholder"
)
