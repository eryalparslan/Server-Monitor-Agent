#gerekli kutuphaneleri import et
import os
import subprocess
import mysql.connector
import logging
import time


#renkleri tanimla
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#ekrani temizle ve karsilama ekrani goster
os.system("clear")
print
os.system("figlet -f smblock ORTA DOGU TEKNIK UNIVERSITESI")
print bcolors.WARNING + ("#############################################################################") + bcolors.ENDC
os.system("cat asd.txt")
print
print bcolors.WARNING + ("Bu yazilim sistem verilerini toplar ve veritabanina yazar.") + bcolors.ENDC
print bcolors.WARNING + ("Program basliyor...") + bcolors.ENDC
os.system("date")                                                              
print

#veritabani degiskenlerini tanimla [CONSTANTS]
DATABASE_NAME = 'metu_db'
TABLE_NAME    = 'makine'
#veritabani bilgilerini ayarla
db_config = {	
			'user':'muser',
			'password':'mpass',
			'host':'localhost',
			'database': DATABASE_NAME,
}

#veritabanina baglan
try:
	cnx = mysql.connector.connect(**db_config)
	cursor = cnx.cursor(buffered=True)
except BaseException as e:
	print bcolors.FAIL + ("veritabani baglantisi saglanamadi.") + bcolors.ENDC
print bcolors.BOLD + DATABASE_NAME + bcolors.OKGREEN + " veritabanina baglanildi." + bcolors.ENDC

#veritabanina veri ekleyecek fonksiyon
def commit_db(parm, val):
	#Eklenecek veriler icin tablo yapisini belirle
	query = ("INSERT INTO makine "
				"(parametre, deger) "
				"VALUES (%(parametre)s, %(deger)s)")


	data = {
			'parametre':parm,
			'deger':val,
		   }

	cursor.execute(query,data)
	cnx.commit()




#parametre isimlerini belirt
par1="Sunucu ismi"
par2="Isletim Sistemi"
par3="Kernel"
par4="IP"
par5="DNS"
par6="HedefCanlimi"
par7="HddKapasite"
par8="HddKullanilmis"
par9="HddBosta"
par10="HddKullanimYuzdesi"
par11="RamToplam"
par12="RamKullanilmis"
par13="RamBosta"
par14="RamOnbellek"
par15="RamKullanilabilir"
par16="CPU Model"
par17="Cekirdek Sayisi"
par18="CpuKullanimYuzdesi"
par19="UptimeSuresi"
par20="OturumAcanKulSayisi"
par21="SunucuID"
par22="Zaman"
target="localhost"

#parametrenin degerlerini belirt
try:
	val1=os.popen("hostname").read().strip()
	val2=os.popen("lsb_release -a | head -n3 | tail -n1 | awk '{print $2,$3}'").read().strip()
	val3=os.popen("uname -r").read().strip()
	val4=os.popen("hostname -I | awk '{print $1}'").read().strip()
	val5=os.popen("cat /etc/resolv.conf | grep 'nameserver ' | awk '{print $2}'").read().strip()
	val61=os.popen("ping -c 1 " + target + "| grep icmp* | wc -l").read().strip()
	# val6 belirtilen hedefin orada olup olmadigini kontrol ediyor ve evet/hayir donuyor.
	if val61 == "0":
	    val6="Hayir"
	else:
	    val6="Evet"
	#hdd kapasite (GB cinsinden)
	val7=os.popen("df -h | grep sda1 | awk '{print $2}' | sed 's/[^0-9]*//g'").read().strip()
	#hdd kullanilmis (GB cinsinden)
	val8=os.popen("df -h | grep sda1 | awk '{print $3}' | sed 's/[^0-9]*//g'").read().strip()
	#hdd bosta (GB cinsinden)
	val9=os.popen("df -h | grep sda1 | awk '{print $4}' | sed 's/[^0-9]*//g'").read().strip()
	#hdd kullanim yuzdesi (GB cinsinden)
	val10=os.popen("df -h | grep sda1 | awk '{print $5}' | sed 's/[^0-9]*//g'").read().strip()
	#ram toplam (gb)
	val11=os.popen("free -h | grep Mem | awk '{print $2}' | sed 's/G//g'").read().strip()
	#ram kullanilmis (gb)
	val12=os.popen("free -h | grep Mem | awk '{print $3}' | sed 's/G//g'").read().strip()
	#ram bosta (gb)
	val13=os.popen("free -h | grep Mem | awk '{print $4}' | sed 's/G//g'").read().strip()
	#ram onbellek (gb)
	val14=os.popen("free -h | grep Mem | awk '{print $6}' | sed 's/G//g'").read().strip()
	#ram kullanilabilir (gb)
	val15=os.popen("free -h | grep Mem | awk '{print $7}' | sed 's/G//g'").read().strip()
	#cpu model
	val16=os.popen("cat /proc/cpuinfo | grep -i 'model name' | head -n1 | awk '{print $4,$5,$6,$7,$8}'").read().strip()
	#cekirdek sayisi
	val17=os.popen("cat /proc/cpuinfo | grep processor | wc -l").read().strip()
	#islemci kullanim yuzdesi
	val18=os.popen("mpstat | awk '$3 ~ /CPU/ { for(i=1;i<=NF;i++) { if ($i ~ /%idle/) field=i } } $3 ~ /all/ { print 100 - $field }'").read().strip()
	#uptime suresi
	val19_saat=os.popen("uptime -p | awk '{print $2}'").read().strip()
	val19_dakika = os.popen("uptime -p | awk '{print $4}'").read().strip()
	val19= val19_saat + " Saat " + val19_dakika + " Dakika"
	#oturum acan kullanici sayisi
	val20=os.popen("uptime | awk '{print $4}'").read().strip()
	val21=1 ##buraya sunucu ID si gelecek degeri integer...
	val22=time.strftime("%c")
except BaseException as e:
	print bcolors.FAIL + ("bash komutlari duzgun calismadi.") + bcolors.ENDC
print bcolors.OKGREEN + ("bash komutlari calistirildi.") + bcolors.ENDC

#degiskenleri bir array a at
pars = []
vals = []
try:
	for i in [par1, par2, par3, par4, par5, par6, par7, par8, par9, par10,
			  par11, par12, par13, par14, par15, par16, par17, par18, par19, par20, par21, par22]:
		pars.append(i)

	for i in [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10,
			  val11, val12, val13, val14, val15, val16, val17, val18, val19, val20, val21, val22]:
		vals.append(i)
except BaseException as e:
	print bcolors.FAIL + ("degiskenler array e yuklenemedi.") + bcolors.ENDC


#Once tablo icerisindekileri bosaltki eski veriler silinsin, yenileri eklensin.
try:
	truncate_table = ("truncate table makine")
	cursor.execute(truncate_table)
except BaseException as e:
	bcolors.FAIL + ("tablo icerisi bosaltilamadi.") + bcolors.ENDC
print bcolors.OKGREEN + ("tablodaki eski degerler temizlendi.") + bcolors.ENDC



#verileri veritabanina yaz
try:
	for i in xrange(0,22):
		commit_db(pars[i],vals[i])
except BaseException as e:
	bcolors.FAIL + ("veriler veritabanina yazilamadi.") + bcolors.ENDC
print bcolors.OKGREEN + ("sistem verileri " + bcolors.ENDC + bcolors.BOLD + TABLE_NAME + bcolors.OKGREEN + " tablosuna yazildi." ) + bcolors.ENDC


#baglantiyi kapat
try:
	cursor.close()
	cnx.close()
except BaseException as e:
	print ("veritabani baglantisi duzgun kapatilamadi.")
print bcolors.OKGREEN + ("veri tabani baglantisi kapatildi.") + bcolors.ENDC
