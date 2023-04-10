print("   Selamat Datang Di Program Bangun Datar  ")
print("============================================")
print('pilih bangun datar : ')
print()
print('1. segitiga')
print('2. lingkaran')
print('3. persegi')
print('4. persegi panjang')
print()
choice = input('masukkan pillihan : ')
print()
if choice == '1':
    print('1.luas segitiga')
    print('2.keliling segitiga')
    print()
    choice = input('pilih salah satu : ')
    print()
    if choice == '1':
     a = int(input('masukkan alas :'))
     b = int(input('masukkan tinggi : '))
     luas = 1/2 * a * b
     print('luas segitiga dari alas ', a , 'tinggi',b , 'adalah', float(luas))
     print('terimakasih telah menggunakan program saya :)')
    elif choice == '2':
      a = int(input('masukkan alas : '))
      b = int(input('masukkan tinggi : '))
      c = int(input('masukkan sisi miring : '))
      kel = a + b + c
      print('keliling segitiga dari alas', a, 'tinggi' , b, 'sisi miring' , c, 'adalah', float(kel))
      print('terimakasih telah menggunakan program saya :)')
    else:
       print('maaf duar')

elif choice == '2':
    print('1.luas lingkaran')
    print('2.keliling lingkaran')
    print()
    choice = input('pilih salah satu : ')
    print()
    if choice == '1':
       r = int(input('masukkan jari-jari : '))
       luas = 3.14 * r * r
       print('jari-jari lingkaran dari luas' , r, 'adalah' ,float(luas))
       print('terimakasih telah menggunakan program saya :)')
    elif choice == '2':
       r = int(input('masukkan jari jari : '))
       kel = 2 * 3.14 * r
       print('jari-jari lingkaran dari keliling', r, 'adalah', float(kel))
       print('terimakasih telah menggunakan program saya :)')
    else:
       print('maaf duar')

elif choice == '3':
   print('1.luas persegi')
   print('2.keliling persegi')
   print()
   choice = input('pilih salah satu : ')
   print()
   if choice == '1':
      s = int(input('masukkan sisi : '))
      luas = s * s
      print('luas persegi dari sisi ', s, 'adalah ',float(luas))
      print('terimakasih telah menggunakan program saya :)')
   elif choice == '2':
      s = int(input('masukkan sisi : '))
      kel = 4 * s
      print('keliling persegi dari sisi ', s, 'adalah', float(kel))
      print('terimakasih telah menggunakan program saya :)')
   else:
       print('maaf duar')

elif choice == '4':
    print('1.luas persegi panjang')
    print('2.keliling persegi panjang')
    print()
    choice = input('pilih salah satu : ')
    print()
    if choice == '1':
        p = int(input('masukkan panjang : '))
        l = int(input('masukkan lebar : '))
        luas = p * l
        print('luas persegi panjang dari panjang ', p, 'dan lebar', l, 'adalah', float(luas))
        print('terimakasih telah menggunakan program saya :)')
    elif choice == '2':
        p = int(input('masukkan panjang : '))
        l = int(input('masukkan lebar : '))
        luas = 2 * (p+l)
        print('luas persegi panjang dari panjang ', p, 'dan lebar', l, 'adalah', float(luas))
        print('terima kasih telah menggunakan program saya :)')
    else:
       print('maaf duar')