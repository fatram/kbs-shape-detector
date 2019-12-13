(defrule bentuksegitiga
    (jumlahsudut 3)
    =>
    (assert (bentuk_segitiga))
)

(defrule bentuksegiempat
    (jumlahsudut 4)
    =>
    (assert (bentuk_segiempat))
)

(defrule bentuklima
    (jumlahsudut 5)
    =>
    (assert (bentuk_segilima))
)

(defrule bentuksegienam
    (jumlahsudut 6)
    =>
    (assert (bentuk_segienam))
)

;;****************
;;* segitiga     *
;;****************

(defrule samakaki
    (bentuk_segitiga)
    (jumlahsudutsama 2)
    =>
    (assert (samakaki))
)

(defrule segitigasamasisi
    (bentuk_segitiga)
    (jumlahsudutsama 3)
    =>
    (assert (segitiga_samasisi))
    (halt)
)


(defrule segitigatumpulsamakaki
    (bentuk_segitiga)
    (samakaki)
    (jumlahsuduttumpul 1)
    =>
    (assert (segitiga_tumpul_samakaki))
    (halt) 
)

(defrule segitigasikusamakaki
    (bentuk_segitiga)
    (samakaki)
    (jumlahsudutsiku 1)
    =>
    (assert (segitiga_siku_samakaki))
    (halt)
)

(defrule segitigalancipsamakaki
    (bentuk_segitiga)
    (samakaki)
    (jumlahsudutlancip 1)
    =>
    (assert (segitiga_lancip_samakaki))
    (halt)
)

(defrule segitigasiku
    (bentuk_segitiga)
    (jumlahsudutsiku 1)
    =>
    (assert (segitiga_siku))
    (halt)
)

(defrule segitigalancip
    (bentuk_segitiga)
    (jumlahsudutlancip 3)
    =>
    (assert (segitiga_lancip))
    (halt)
)

(defrule segitigatumpul
    (bentuk_segitiga)
    (jumlahsuduttumpul 1)
    =>
    (assert (segitiga_tumpul))
    (halt)
)

(defrule segitigatidakberaturan
    (bentuk_segitiga)
    (jumlahsudutsama 0)
    =>
    (assert (segitiga_tidak_beraturan))
    (halt)
)


;;****************
;;* Segiempat    *
;;****************


(defrule persegi
    (bentuk_segiempat)
    (jumlahsudutsiku 4)
    (jumlahsisisama 4)
    =>
    (assert (persegi))
    (halt)
)

(defrule persegipanjang
    (bentuk_segiempat)
    (jumlahsudutsiku 4)
    (jumlahsisisama 2)
    =>
    (assert (persegi_panjang))
    (halt)
)

(defrule jajargenjangberaturan
    (bentuk_segiempat)
    (jumlahsudutsama 2)
    (jumlahsisisama 4)
    =>
    (assert (jajar_genjang_beraturan))
    (halt)
)

(defrule jajargenjanglayanglayang
    (bentuk_segiempat)
    (jumlahsudutsama 1)
    (jumlahsisisama 2)
    =>
    (assert (jajar_genjang_layang_layang))
    (halt)
)

(defrule trapesiumsamakaki
    (bentuk_segiempat)
    (jumlahsudutsama 2)
    (jumlahsisisama 1)
    =>
    (assert (trapesium_sama_kaki))
    (halt)
)

(defrule trapesiumratasisi
    (bentuk_segiempat)
    (jumlahsudutsiku 2)
    =>
    (assert (trapesium_rata_sisi))
    (halt)
)

(defrule segiempattidakberaturan
    (bentuk_segiempat)
    =>
    (assert (segiempat_tidak_beraturan))
    (halt)
)

;;****************
;;* Segilima    *
;;****************

(defrule segilimaberaturan
    (bentuk_segilima)
    (jumlahsisisama 5)
    =>
    (assert (segilima_beraturan))
    (halt)
)

(defrule segilimatidakberaturan
    (bentuk_segilima)
    =>
    (assert (segilima_tidak_beraturan))
    (halt)
)

;;****************
;;* Segienam   *
;;****************

(defrule segienamberaturan
    (bentuk_segienam)
    (jumlahsisisama 6)
    =>
    (assert (segienam_beraturan))
    (halt)
)

(defrule segienamtidakberaturan
    (bentuk_segienam)
    =>
    (assert (segienam_tidak_beraturan))
    (halt)
)