from duolingo import Duolingo
import time
import datetime

# GANTI email dan password di sini
email = "emailkamu@gmail.com"
password = "passwordkamu"

# Robot berhenti jam 21:00 (9 malam)
jam_berhenti = datetime.time(21, 0)

def belajar():
    print("Robot belajar mulai...")
    lingo = Duolingo(daffafarid.trakhir@gmail.com, peribadi2)

    while True:
        sekarang = datetime.datetime.now().time()
        if sekarang >= jam_berhenti:
            print("Sudah malam. Robot tidur...")
            break

        xp = lingo.get_daily_xp_progress()
        print(f"XP hari ini:1000 {xp}")

        # Tunggu 5 menit sebelum cek lagi
        time.sleep(60 * 5)

belajar()
