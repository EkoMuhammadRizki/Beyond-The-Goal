# 🤝 Contributing to Beyond The Goal

Terima kasih atas minat Anda untuk berkontribusi pada "Beyond The Goal"! Kami menyambut kontribusi dari semua orang, baik developer, educator, artist, writer, maupun player.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Guidelines](#coding-guidelines)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Asset Contribution](#asset-contribution)
- [Educational Content](#educational-content)

---

## 📜 Code of Conduct

### Our Pledge

Kami berkomitmen untuk menjadikan partisipasi dalam project ini sebagai pengalaman yang bebas dari harassment untuk semua orang, tanpa memandang:
- Usia
- Ukuran tubuh
- Disabilitas
- Etnisitas
- Identitas dan ekspresi gender
- Level pengalaman
- Kebangsaan
- Penampilan personal
- Ras
- Agama
- Identitas dan orientasi seksual

### Our Standards

**Perilaku yang Diharapkan:**
- Menggunakan bahasa yang ramah dan inklusif
- Menghormati sudut pandang dan pengalaman yang berbeda
- Menerima kritik konstruktif dengan baik
- Fokus pada yang terbaik untuk komunitas
- Menunjukkan empati terhadap anggota komunitas lain

**Perilaku yang Tidak Dapat Diterima:**
- Penggunaan bahasa atau gambar seksual
- Trolling, komentar menghina, atau serangan personal
- Harassment publik atau privat
- Mempublikasikan informasi privat orang lain
- Perilaku tidak profesional lainnya

---

## 🎯 How Can I Contribute?

### 1. Reporting Bugs

**Before Submitting:**
- Check existing issues untuk memastikan bug belum dilaporkan
- Test di versi terbaru
- Kumpulkan informasi yang relevan

**Bug Report Should Include:**
- Deskripsi jelas tentang bug
- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots (jika applicable)
- System information (OS, Ren'Py version)
- Error messages (jika ada)

**Template:**
```markdown
**Bug Description:**
[Deskripsi singkat bug]

**Steps to Reproduce:**
1. Go to...
2. Click on...
3. See error...

**Expected Behavior:**
[Apa yang seharusnya terjadi]

**Actual Behavior:**
[Apa yang benar-benar terjadi]

**Screenshots:**
[Jika ada]

**System Info:**
- OS: [e.g., Windows 10]
- Ren'Py Version: [e.g., 8.0.3]
- Game Version: [e.g., 1.0.0]

**Additional Context:**
[Informasi tambahan]
```

### 2. Suggesting Features

**Before Suggesting:**
- Check roadmap untuk melihat apakah sudah direncanakan
- Check existing feature requests
- Pastikan feature sesuai dengan vision game

**Feature Request Should Include:**
- Clear description of the feature
- Why it would be useful
- How it should work
- Mockups or examples (jika ada)
- Potential challenges

**Template:**
```markdown
**Feature Description:**
[Deskripsi feature]

**Use Case:**
[Kapan dan mengapa feature ini berguna]

**Proposed Implementation:**
[Bagaimana feature ini bisa diimplementasikan]

**Alternatives Considered:**
[Alternatif lain yang sudah dipertimbangkan]

**Additional Context:**
[Mockups, examples, dll]
```

### 3. Code Contributions

**Areas to Contribute:**
- Bug fixes
- New features
- Performance improvements
- Code refactoring
- Documentation
- Tests

### 4. Asset Contributions

**Types of Assets:**
- Character sprites
- Background images
- Music & sound effects
- UI elements
- Icons

### 5. Content Contributions

**Types of Content:**
- Story writing
- Dialog improvements
- Educational content
- Translations
- Tutorial creation

### 6. Documentation

**Documentation Needs:**
- Code comments
- User guides
- Tutorial videos
- FAQ updates
- Translation of docs

---

## 🛠️ Development Setup

### Prerequisites

1. **Ren'Py SDK 8.0+**
   ```bash
   # Download from https://www.renpy.org/
   ```

2. **Git**
   ```bash
   # Windows: Download from https://git-scm.com/
   # Mac: brew install git
   # Linux: sudo apt-get install git
   ```

3. **Text Editor**
   - VS Code (recommended)
   - Sublime Text
   - Atom
   - Atau editor favorit Anda

### Setup Steps

1. **Fork the Repository**
   - Click "Fork" button di GitHub
   - Clone fork Anda:
   ```bash
   git clone https://github.com/YOUR_USERNAME/beyond-the-goal.git
   cd beyond-the-goal
   ```

2. **Add Upstream Remote**
   ```bash
   git remote add upstream https://github.com/ORIGINAL_OWNER/beyond-the-goal.git
   ```

3. **Create Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # atau
   git checkout -b fix/bug-description
   ```

4. **Open in Ren'Py**
   - Launch Ren'Py Launcher
   - Add existing project
   - Select your cloned folder

5. **Make Changes**
   - Edit files
   - Test thoroughly
   - Commit changes

6. **Push Changes**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Fill in the template

---

## 📝 Coding Guidelines

### Ren'Py Script Style

**File Organization:**
```python
# ============================================
# FILE DESCRIPTION
# ============================================

# Imports (if any)

# Constants
define CONSTANT_NAME = value

# Variables
default variable_name = value

# Labels
label label_name:
    # Code here
    return
```

**Naming Conventions:**
- **Labels:** `snake_case` (e.g., `ch1_intro`, `show_score_screen`)
- **Variables:** `snake_case` (e.g., `teknik_score`, `player_name`)
- **Constants:** `UPPER_SNAKE_CASE` (e.g., `MAX_SCORE`, `DEFAULT_NAME`)
- **Characters:** `lowercase` (e.g., `mc`, `coach`, `naya`)
- **Images:** `snake_case` (e.g., `mc_neutral`, `bg_school_field`)

**Comments:**
```python
# Single line comment

## Section header

# ============================================
# MAJOR SECTION
# ============================================

"""
Multi-line comment
for longer explanations
"""
```

**Dialog Format:**
```python
# Good
coach "Dialog text here."

# With expression
show coach senang
coach "Dialog with happy expression."

# With action
coach "Dialog text." with dissolve
```

**Menu Format:**
```python
menu:
    "Clear question or prompt?"
    
    "Option 1":
        # Code for option 1
        
    "Option 2":
        # Code for option 2
```

**Indentation:**
- Use 4 spaces (not tabs)
- Consistent indentation throughout

### Python Code Style

Follow PEP 8 guidelines:
```python
init python:
    def function_name(parameter1, parameter2):
        """
        Function description.
        
        Args:
            parameter1: Description
            parameter2: Description
            
        Returns:
            Description of return value
        """
        # Function code
        return result
```

### Best Practices

1. **Keep it Simple**
   - Write clear, readable code
   - Avoid unnecessary complexity
   - Use descriptive names

2. **Comment Your Code**
   - Explain why, not what
   - Document complex logic
   - Add section headers

3. **Test Thoroughly**
   - Test all code paths
   - Test edge cases
   - Test on different platforms

4. **Follow Existing Patterns**
   - Match existing code style
   - Use established conventions
   - Maintain consistency

5. **Modular Design**
   - Keep files focused
   - Separate concerns
   - Reuse code when possible

---

## 💬 Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat:** New feature
- **fix:** Bug fix
- **docs:** Documentation changes
- **style:** Code style changes (formatting, etc.)
- **refactor:** Code refactoring
- **test:** Adding or updating tests
- **chore:** Maintenance tasks

### Examples

```bash
# Good commits
feat(chapter1): add new quiz question about dribbling
fix(score): correct calculation for sportivitas points
docs(readme): update installation instructions
style(chapter2): improve dialog formatting
refactor(variables): simplify score tracking system

# Bad commits
update stuff
fix bug
changes
wip
```

### Commit Best Practices

1. **One logical change per commit**
2. **Write clear, descriptive messages**
3. **Use present tense** ("add" not "added")
4. **Keep subject line under 50 characters**
5. **Add body for complex changes**

---

## 🔄 Pull Request Process

### Before Submitting

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] Documentation updated
- [ ] Commits are clean and logical
- [ ] Branch is up to date with main

### PR Template

```markdown
## Description
[Describe your changes]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
[Describe how you tested]

## Screenshots
[If applicable]

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added/updated
- [ ] All tests pass

## Related Issues
Closes #[issue number]
```

### Review Process

1. **Automated Checks**
   - Code style validation
   - Build verification

2. **Code Review**
   - At least one maintainer review
   - Address feedback
   - Make requested changes

3. **Testing**
   - Maintainers test changes
   - Community testing (if major)

4. **Merge**
   - Approved PRs merged to main
   - Branch deleted after merge

### After Merge

- Your contribution will be credited
- Changes included in next release
- Thank you message in changelog

---

## 🎨 Asset Contribution

### Character Sprites

**Requirements:**
- Size: 300x600 pixels
- Format: PNG with transparency
- Style: Semi-anime modern
- Expressions: neutral, senang, marah, sedih, fokus, takut

**Submission:**
1. Create sprites following guidelines
2. Name files correctly (e.g., `mc_senang.png`)
3. Submit via PR or issue
4. Include license information

### Backgrounds

**Requirements:**
- Size: 1920x1080 pixels
- Format: PNG or JPG
- Style: Semi-realistic with anime feel
- Lighting: Consistent with time of day

**Submission:**
1. Create backgrounds following guidelines
2. Name files correctly
3. Submit via PR or issue
4. Include license information

### Audio

**Requirements:**
- BGM: MP3, 192kbps+, loopable
- SFX: WAV, 44.1kHz, mono/stereo
- Quality: Professional or semi-professional
- Length: As specified in ASSET_GUIDE.md

**Submission:**
1. Create audio following guidelines
2. Name files correctly
3. Submit via PR or issue
4. Include license information

### Asset License

All contributed assets must be:
- Original work or properly licensed
- Compatible with MIT License
- Free for educational use
- Properly attributed

---

## 📚 Educational Content

### Writing Guidelines

**Story Content:**
- Age-appropriate for high school students
- Positive and encouraging tone
- Culturally sensitive
- Educational value

**Dialog:**
- Natural and conversational
- Character-appropriate
- Clear and concise
- Grammatically correct

**Educational Material:**
- Accurate information
- Clear explanations
- Practical examples
- Engaging presentation

### Content Review

Educational content will be reviewed by:
- Educators
- Subject matter experts
- Community members
- Maintainers

---

## 🌍 Translation

### Translation Guidelines

1. **Accuracy**
   - Translate meaning, not just words
   - Maintain tone and style
   - Keep educational accuracy

2. **Cultural Adaptation**
   - Adapt cultural references
   - Use appropriate idioms
   - Consider local context

3. **Technical Terms**
   - Use standard football terminology
   - Be consistent with terms
   - Add glossary if needed

### Translation Process

1. Check if language is already in progress
2. Create issue to claim language
3. Translate using provided template
4. Submit for review
5. Address feedback
6. Final approval and merge

---

## ❓ Questions?

- **General Questions:** Open a discussion
- **Bug Reports:** Create an issue
- **Feature Requests:** Create an issue
- **Security Issues:** Email maintainers directly
- **Other:** Contact maintainers

---

## 🙏 Thank You!

Every contribution, no matter how small, helps make "Beyond The Goal" better for everyone. We appreciate your time and effort!

**Contributors will be credited in:**
- CHANGELOG.md
- Game credits
- README.md (for major contributions)

---

**Happy Contributing! ⚽🎮**

*"Together, we go beyond the goal."*
