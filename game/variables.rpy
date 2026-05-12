# ============================================
# GAME VARIABLES
# ============================================

# Nama pemain
default player_name = "Raka"

# Sistem Skor
default teknik_score = 0
default percaya_diri = 0
default sportivitas = 0

# Chapter Progress
default chapter_clear = 0
default current_chapter = 1

# Chapter 1 Variables
default ch1_quiz_score = 0
default ch1_completed = False

# Chapter 2 Variables
default ch2_quiz_score = 0
default ch2_combo = 0
default ch2_completed = False

# Chapter 3 Variables
default ch3_match_score = 0
default ch3_sportivitas_score = 0
default ch3_completed = False

# Player Style Tracking
default technical_points = 0
default supportive_points = 0
default brave_points = 0
default balanced_points = 0

# Gallery Unlock
default gallery_unlocked = []

# ============================================
# HELPER FUNCTIONS
# ============================================

init python:
    def add_teknik(amount):
        global teknik_score
        teknik_score += amount
        if teknik_score < 0:
            teknik_score = 0
    
    def add_percaya_diri(amount):
        global percaya_diri
        percaya_diri += amount
        if percaya_diri < 0:
            percaya_diri = 0
    
    def add_sportivitas(amount):
        global sportivitas
        sportivitas += amount
        if sportivitas < 0:
            sportivitas = 0
    
    def get_player_style():
        """Menentukan style pemain berdasarkan poin"""
        styles = {
            "technical": technical_points,
            "supportive": supportive_points,
            "brave": brave_points,
            "balanced": balanced_points
        }
        return max(styles, key=styles.get)
    
    def unlock_gallery(item):
        """Unlock item di gallery"""
        if item not in gallery_unlocked:
            gallery_unlocked.append(item)
