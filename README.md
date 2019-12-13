# KBS Shape Detector

## Dibuat Oleh

 - Ignatius Timothy Manullang - 13517044 
 - Fatur Rahman - 13517056

## Tahapan yang dilakukan saat membuat aplikasi adalah:
 - Membuat rule dan fact untuk bentuk dasar yang bisa terdeteksi sistem
 - Membuat mesin inferensi untuk menelusuri fact dari sistem
 - Menyusun GUI 
 - Menggabungkan mesin inferensi, GUI serta rule dan fact untuk bentuk dasar yang bisa terdeteksi sistem.

## Repository yang memiliki dokumentasi lengkap
https://github.com/fatram/kbs-shape-detector

## User Manual
- Bahasa pemrograman yang digunakan adalah python 3
- Module yang digunakan adalah tkinter,opencv, pillow and clipspy 
### Installing program dependencies
 - Install python 3 
 - Install module opencv python dengan menjalankan
   command di terminal atau cmd
	 - `pip install opencv-python` 
 - Install module pillow dengan menjalankan command di terminal atau cmd
	 - `pip install pillow`
 - Install module clipspy dengan menjalankan command di terminal atau cmd
	 - `pip install clipspy`

### Running program
 - Run main.py dengan python 
### Operating program
 - Tekan tombol Open Image untuk memilih image bentuk yang akan
   dideteksi 
 - Tekan tombol Open Rule Editor untuk mengedit rule secara
   manual 
 - Tekan tombol Show Rules untuk melihat list semua rules
 - Tekan tombol Show Facts untuk melihat list semua facts
 - Di bagian “What shape do you want” anda dapat mengekspan all shapes untuk melihat semua shape yang bisa diinferensikan, setelah itu anda dapat memilih salah satu opsi shape yang ingin diinferensikan 
 - Setelah itu anda dapat klik run untuk melihat hasilnya
## Proses updating dan inferencing atas fakta yang terlibat adalah
 - Memanfaatkan CLIPS dengan menghitung sisi dari gambar yang disediakan
 - Melalui sisi, akan terdeteksi salah satu bentuk. Misalnya, jika sisinya 3, maka bentuknya segitiga. 
 - Setelah itu, akan diteruskan rule-rule yang berkaitan dengan segitiga, dengan urutan depth-first, yaitu rule yang baru diaktifkan akan dijalankan terlebih dahulu.
 - Contohnya, setelah mengecek sisi, maka program akan mengecek sudut dari bentuk yang dimasukkan, jika ditemukan 2 sudut yang ukurannya sama maka akan terdeteksi segitiga sama kaki 
 - Seterusnya jika bentuk yang dimasukkan memiliki ukuran semua sudut lebih kecil dibandingkan 90 maka akan terdeteksi segitiga sama kaki lancip
