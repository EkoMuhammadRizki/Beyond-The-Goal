# ⚽ Pitching Progress Game: Beyond The Goal

Dokumen ini disusun untuk membantu Anda mempresentasikan (pitching) progress pengembangan game "Beyond The Goal" kepada dosen pembimbing atau penguji. Penjelasan dibuat terstruktur, mulai dari konsep awal hingga kondisi saat ini, serta penjelasan teknis (coding) yang mudah dipahami.

---

## 📌 1. Pendahuluan & Konsep Game

*   **Judul Game:** Beyond The Goal
*   **Genre:** Visual Novel Edukasi (Educational Visual Novel)
*   **Engine:** Ren'Py (Python-based)
*   **Target Audiens:** Siswa SMA (15-18 tahun), pecinta game naratif, dan siswa yang sedang belajar teknik dasar sepak bola.
*   **Tujuan Utama:** Menghadirkan media pembelajaran PJOK (Pendidikan Jasmani, Olahraga, dan Kesehatan) yang interaktif, menyenangkan, dan tidak membosankan melalui cerita yang menarik.

---

## 📈 2. Progress Pengembangan (Dari Awal Sampai Sekarang)

Berikut adalah ringkasan perjalanan pembuatan game ini:

### ⏱️ Tahap 1: Perencanaan & Desain (Ideasi)
*   **Penyusunan Cerita:** Membuat draft cerita yang berfokus pada perkembangan karakter (Growth Mindset) dan kerja sama tim.
*   **Integrasi Materi:** Memasukkan materi teknik dasar sepak bola (Menendang, Mengontrol, Dribbling, dan Heading) ke dalam alur cerita.
*   **Desain Sistem:** Merancang sistem skor (Teknik, Percaya Diri, Sportivitas) dan penentuan gaya bermain di akhir game.

### ⚙️ Tahap 2: Pengembangan Sistem Inti (Core System)
*   **Pembuatan Kerangka Kode:** Membagi game menjadi file-file modular agar rapi (per chapter, variabel terpisah, sistem HUD terpisah).
*   **Sistem Variabel & Skor:** Membuat logika untuk menghitung skor berdasarkan pilihan pemain.
*   **Sistem Placeholder Otomatis:** Membuat sistem yang otomatis memunculkan gambar kotak berwarna jika aset gambar asli (karakter/background) belum ada. Ini membuat game **selalu bisa dimainkan (fully playable)** tanpa takut error "file not found".

### 📝 Tahap 3: Implementasi Konten & Mini Game
*   **Chapter 1 (Teknik Menendang):** Selesai. Dilengkapi mini game "Kick Selector Quiz".
*   **Chapter 2 (Kontrol & Dribbling):** Selesai. Dilengkapi mini game "Control & Dribble Match".
*   **Chapter 3 (Heading & Teamwork):** Selesai. Dilengkapi mini game "Final Small Match".
*   **Multi Ending:** Sistem penentuan akhir cerita berdasarkan dominasi skor gaya bermain pemain.

### 🎨 Tahap 4: UI/UX & Polishing
*   **Custom UI:** Mengubah tampilan menu bawaan Ren'Py menjadi bertema sepak bola.
*   **HUD (Heads-Up Display):** Menampilkan indikator skor di pojok kanan atas secara real-time.
*   **Gallery & Chapter Select:** Menambahkan fitur untuk melihat kembali materi dan memilih bab yang ingin dimainkan.

> [!NOTE]
> **Status Saat Ini:** Game sudah **Selesai secara fungsional (Production Ready)**. Alur cerita dari awal sampai akhir beserta mini game sudah berfungsi 100%. Saat ini game menggunakan sistem placeholder untuk visual dan audio, sehingga langkah selanjutnya tinggal memasukkan aset visual (gambar karakter & background) dan audio asli.

---

## 💻 3. Penjelasan Coding (Sederhana & Mudah Dipahami)

Bagian ini menjelaskan fungsi dari file-file kode utama di dalam game agar Anda bisa menjelaskannya dengan lancar ke dosen.

### 1. `variables.rpy` (Sistem Memori & Skor)
*   **Penjelasan Sederhana:** File ini berfungsi sebagai "ingatan" game. Di sini kita membuat variabel (wadah data) untuk menyimpan skor pemain.
*   **Untuk Apa:** Setiap kali pemain memilih jawaban yang benar tentang teknik sepak bola, nilai di variabel `score_teknik` akan bertambah. Ini yang menentukan apakah pemain lulus ujian teknik atau tidak.

### 2. `hud_system.rpy` (Tampilan Informasi Layar)
*   **Penjelasan Sederhana:** File ini mengatur apa yang dilihat pemain di layar selain gambar karakter dan teks dialog.
*   **Untuk Apa:** Di sini terdapat kode `screen hud_display` yang berfungsi menampilkan kotak skor di pojok layar secara terus-menerus (HUD). Selain itu, file ini mengatur efek getar (`shake`) jika jawaban salah dan efek kilatan (`flash`) jika benar.

### 3. `chapter1.rpy`, `chapter2.rpy`, `chapter3.rpy` (Logika Cerita & Kuis)
*   **Penjelasan Sederhana:** Ini adalah file yang berisi naskah cerita dan pilihan-pilihan interaktif per bab.
*   **Untuk Apa:** Di dalam file ini kita menggunakan perintah `menu:` untuk membuat pilihan. Contohnya, saat ditanya "Bagian kaki mana untuk menendang jarak jauh?", game akan memberikan pilihan. Kode di sini akan mengecek jawaban pemain, memberikan poin jika benar, dan melanjutkan cerita sesuai pilihan tersebut (Branching Narrative).

### 4. `custom_screens.rpy` (Antarmuka Kustom)
*   **Penjelasan Sederhana:** File ini digunakan untuk merombak tampilan standar Ren'Py agar sesuai dengan tema game kita.
*   **Untuk Apa:** Kami membuat layar baru seperti *Chapter Select* (untuk memilih bab) dan *Gallery* (untuk membaca kembali materi teknik sepak bola yang sudah dipelajari).

### 5. `generate_placeholders.rpy` (Sistem Anti-Error)
*   **Penjelasan Sederhana:** Ini adalah fitur cerdas yang kami buat menggunakan bahasa Python di dalam Ren'Py.
*   **Untuk Apa:** Jika seorang artis belum selesai menggambar karakter "Raka", kode ini akan mendeteksi bahwa file gambar "Raka" tidak ada, lalu secara otomatis menggambarnya sebagai kotak berwarna dengan tulisan "Raka". Ini mencegah game *crash* atau *force close* saat diuji coba oleh dosen meskipun gambarnya belum jadi.

---

## 🎯 4. Rencana Langkah Selanjutnya (Next Steps)

Untuk menyempurnakan game ini menuju versi final, berikut adalah rencana selanjutnya:
1.  **Penggantian Aset Visual:** Mengganti gambar placeholder (kotak warna) dengan sprite karakter bergaya anime dan background lapangan sepak bola yang asli.
2.  **Pengisian Audio:** Memasukkan musik latar (BGM) dan efek suara (SFX) seperti peluit dan tendangan bola yang sesungguhnya.
3.  **Uji Coba Pengguna (User Testing):** Melakukan playtest kepada beberapa siswa SMA untuk melihat tingkat pemahaman mereka terhadap materi sepak bola yang disampaikan di dalam game.

---

*Tips untuk Pitching:* Tekankan pada dosen bahwa game ini **bukan hanya sekadar visual novel biasa**, tapi memiliki **nilai edukasi yang kuat** dan sistem kode yang sudah **modular serta siap pakai** (tinggal ganti gambar saja tanpa perlu coding ulang dari nol).*
