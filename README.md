Tautan Aplikasi
Aplikasi PWS yang sudah di-deploy dapat diakses melalui tautan berikut: Tautan Aplikasi PWS

Implementasi Checklist
Berikut adalah langkah-langkah implementasi checklist secara step-by-step:

Persiapan Lingkungan Pengembangan

Install Python dan pip (Package Installer for Python).
Buat dan aktifkan virtual environment untuk mengisolasi dependensi proyek.
Install Django menggunakan pip: pip install django.
Membuat Proyek Django

Buat proyek baru dengan perintah: django-admin startproject nama_proyek.
Masuk ke direktori proyek dengan cd nama_proyek.
Membuat Aplikasi Django

Buat aplikasi baru dalam proyek dengan perintah: python manage.py startapp nama_aplikasi.
Daftarkan aplikasi di settings.py proyek dengan menambahkannya ke INSTALLED_APPS.
Membuat Model

Definisikan model di models.py dalam aplikasi, misalnya:
'''
<from django.db import models

<class Artikel(models.Model):
    judul = models.CharField(max_length=100)
    isi = models.TextField()
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)>
'''
<from django.db import models

<class Artikel(models.Model):
    judul = models.CharField(max_length=100)
    isi = models.TextField()
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)>
'''
Migrasi Database

Jalankan perintah python manage.py makemigrations untuk membuat file migrasi.
Terapkan migrasi dengan python manage.py migrate untuk membuat tabel di database.
Membuat View dan URL

Definisikan view di views.py, misalnya:

'''
<from django.shortcuts import render
from .models import Artikel

<def daftar_artikel(request):
    artikel_list = Artikel.objects.all()
    return render(request, 'daftar_artikel.html', {'artikel_list': artikel_list})>
'''
Daftarkan URL di urls.py aplikasi:
'''
<from django.urls import path
from . import views

<urlpatterns = [
    path('artikel/', views.daftar_artikel, name='daftar_artikel'),
]>
'''

Buat template HTML di direktori templates, misalnya daftar_artikel.html:

'''
<!DOCTYPE html>
<html>
<head>
    <title>Daftar Artikel</title>
</head>
<body>
    <h1>Daftar Artikel</h1>
    <ul>
    {% for artikel in artikel_list %}
        <li>{{ artikel.judul }} - {{ artikel.isi }}</li>
    {% endfor %}
    </ul>
</body>
</html>

'''

Pengujian dan Deploy

Jalankan server pengembangan dengan python manage.py runserver dan uji aplikasi di browser.
Untuk deployment, gunakan platform seperti Heroku, DigitalOcean, atau lainnya.
*Bagan Arsitektur Web Django*
Berikut adalah bagan sederhana dari request client ke web aplikasi berbasis Django:

'''<Client Request --> <URLs (urls.py) --> <Views (views.py) --> <Models (models.py) --> <HTML (templates)>'''

Penjelasan:

*urls.py:* Menyediakan rute URL yang mengarahkan request client ke view yang sesuai.
*views.py:* Menangani logika aplikasi, memproses data menggunakan model, dan mengembalikan response dalam bentuk template HTML.
*models.py:* Mengelola data dan interaksi dengan database.
*Templates (HTML):* Menyajikan data yang dikirimkan oleh view dalam format HTML kepada client.
Fungsi Git dalam Pengembangan Perangkat Lunak
Git adalah sistem kontrol versi yang digunakan untuk melacak perubahan dalam kode sumber proyek. Fungsinya mencakup:

*Versi Kontrol:* Mengelola dan menyimpan versi kode yang berbeda.
*Kolaborasi:* Memungkinkan banyak developer bekerja pada proyek yang sama secara bersamaan.
*Branching dan Merging:* Membantu membuat cabang pengembangan terpisah dan menggabungkannya kembali setelah selesai.
*Histori Perubahan:* Menyimpan riwayat perubahan kode untuk referensi dan pemulihan di masa depan.
Mengapa Memulai Dengan Django?
Django adalah framework yang ideal untuk pemula karena:

*Dokumentasi Lengkap:* Menyediakan panduan yang komprehensif dan mudah dipahami.
*Batteries Included:* Menyediakan banyak fitur bawaan seperti admin panel, autentikasi, dan ORM yang mempermudah pengembangan.
*Struktur Proyek Jelas:* Mengikuti prinsip desain yang memudahkan pemahaman alur kerja dan pengembangan aplikasi web.

Mengapa Model pada Django Disebut ORM?
Model pada Django disebut ORM (Object-Relational Mapping) karena:

*Abstraksi Database:* Menghubungkan objek Python dengan tabel database, sehingga developer tidak perlu menulis SQL langsung.
*Pengelolaan Data:* Memudahkan operasi CRUD (Create, Read, Update, Delete) dengan menggunakan metode Python standar.
*Pemetaan Objek:* Mengonversi data antara format database dan objek Python dengan cara yang transparan.
