Proyek Django - Aplikasi Main
Tautan Aplikasi yang Sudah Dideploy
Aplikasi PWS - Main (Ganti dengan tautan yang sesuai setelah deployment).

Implementasi Checklist Secara Step-by-Step
Membuat Proyek Django Baru
Saya membuat proyek baru dengan django-admin startproject dan memastikan virtual environment aktif sebelum mulai instalasi dan pembuatan proyek.

Membuat Aplikasi 'main'
Aplikasi main dibuat dengan perintah python manage.py startapp main. Saya menambahkan aplikasi ini ke dalam INSTALLED_APPS di settings.py agar diakui oleh Django.

Routing Aplikasi ke Proyek
Pada urls.py proyek utama, saya melakukan routing menggunakan include sehingga aplikasi main dapat diakses melalui root URL proyek.

Membuat Model 'Product'
Saya membuat model Product di models.py dengan atribut name, price, dan description. Setelah itu, saya menjalankan perintah makemigrations dan migrate untuk membuat tabel di database.

Membuat Fungsi di Views untuk Menampilkan Data
Pada views.py, saya menulis fungsi show_info yang mengembalikan template HTML yang menampilkan nama aplikasi, nama saya, dan kelas saya.

Routing Fungsi di views.py
Saya menambahkan URL untuk mengakses fungsi show_info pada urls.py aplikasi main dengan menambahkan path 'info/'.

Deployment ke PWS
Saya menyiapkan aplikasi untuk deployment dengan membuat Procfile dan requirements.txt, lalu menggunakan perintah cf push untuk mengunggah aplikasi ke PWS sehingga dapat diakses oleh umum.

Bagan Request Client ke Web Aplikasi Django
Berikut adalah bagan proses request dan respon dalam aplikasi Django:

rust
Copy code
Client Request --> URLS.PY --> VIEWS.PY --> MODELS.PY --> Template HTML --> Client Response
Penjelasan Kaitan Antara urls.py, views.py, models.py, dan Template HTML:
urls.py: Menerima permintaan dari client dan memetakan URL tersebut ke fungsi yang ada di views.py.
views.py: Memproses permintaan dari client, mengambil data dari model (jika diperlukan), dan mengembalikan respon berupa template HTML.
models.py: Berfungsi sebagai penghubung antara aplikasi dan database. Dalam hal ini, model Product digunakan untuk menyimpan dan mengelola data produk.
Template HTML: Digunakan untuk menampilkan data yang telah diambil oleh views.py kepada client dalam bentuk antarmuka web.
Fungsi Git dalam Pengembangan Perangkat Lunak
Git adalah sistem kontrol versi yang sangat penting dalam pengembangan perangkat lunak. Beberapa fungsinya:

Versi dan Riwayat: Git memungkinkan pengembang untuk melacak semua perubahan kode dari waktu ke waktu. Setiap commit merupakan snapshot dari proyek.
Kolaborasi: Git memfasilitasi kerja tim, di mana beberapa pengembang bisa bekerja di bagian yang berbeda dari kode secara bersamaan tanpa saling mengganggu.
Cabang (Branching): Git memungkinkan pembuatan cabang untuk mengembangkan fitur baru atau memperbaiki bug tanpa mempengaruhi versi utama.
Revert: Jika ada kesalahan, Git memudahkan untuk kembali ke versi kode yang stabil.
Kenapa Framework Django Dipilih?
Django adalah pilihan framework yang sangat populer untuk pembelajaran pengembangan perangkat lunak karena:

Komprehensif: Django menyediakan banyak fitur bawaan seperti ORM, templating engine, dan admin interface, yang memudahkan pengembang pemula untuk belajar.
Baterai Terpasang: Django menerapkan prinsip "batteries included," artinya framework ini sudah siap pakai dengan semua fitur penting untuk mengembangkan aplikasi web tanpa harus menginstal banyak komponen tambahan.
Modular dan Terstruktur: Django memiliki arsitektur yang terorganisir (MTV: Model, Template, View), memudahkan developer untuk mengerti alur pengembangan perangkat lunak.
Mengapa Model pada Django Disebut Sebagai ORM?
Model pada Django disebut ORM (Object-Relational Mapping) karena memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek Python. Dengan ORM, kita tidak perlu menulis kueri SQL secara manual. Sebagai gantinya, kita bisa bekerja dengan model Python dan Django akan secara otomatis mengkonversi tindakan pada objek model menjadi instruksi SQL yang relevan. ORM mempermudah developer dalam mengelola database tanpa perlu mengetahui detail teknis SQL.