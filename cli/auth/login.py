def login(name,password):
    sukses = False
    file = open("logindatabase.txt","r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if(a==name and b==password):
            sukses = True
            break
    file.close()
    if(sukses):
        print("-"*40)
        print("  | Login Berhasil, silahkan masuk  | ")
        print("-"*40)
    else:
        print("-"*50)
        print("   | Anda belum terdaftar, silahan register  | ")
        print("-"*50)
        
def register(name,password):
    file = open("./cli/data/logindatabase.txt","a")
    file.write("\n"+name+","+password)
def access(option):
    global name
    if(option=="iya"):
        name = input("Masukkan ID: ")
        password = input("Masukkan Password: ")
        login(name,password)
    else:
        print(" | Masukkan ID dan Password baru anda! | ")
        name = input("Masukkan ID : ")
        password = input("Masukkan password anda: ")
        register(name,password)
        print(" | Register anda berhasil, silahkan masuk | ")

def begin():
    global option
    print("─"*45)
    print("│       Selamat datang di Taman Biru        │")
    print("─"*45)
    option = input(" apakah sudah memiliki akun? (iya/tidak): ")
    if(option!="iya" and option!="tidak"):
        begin()
begin()
access(option)
