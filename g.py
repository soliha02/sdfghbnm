# QWERTY Bankga Hush kelibsiz!

language = '''
1: uzbek
2: english
'''

print(language)
a = int(input('til: '))

if a == 1:
    print('Uzbek')
    parol = int(input('parol: '))
    print('Menyu ga hush kelibsiz!')
    menyu = 'Funksiya tanlang'
    print(menyu)

  

funksiyadir = '''

1:balans
2:pul yechish
3: pul qo'shish
4: tel raqam to'ldirish
'''
print(funksiyadir)

mamajon = int(input('Menyuda tanlang: '))

print(mamajon)

if mamajon == 1:
  print('Balansiz: 100000.00 som')

  if mamajon == 2:
      
   print('Pul yeching: ')

   if mamajon == 3:
          
     print('Pul qoshing: ')

     if mamajon == 4:

       print('Tel raqam toldirildi: ')

     else:

       print('telefonizni togri kiriting: ')

   else:
          
     print('xato, pul qoshing')

  else:
      
     print('togri pul yeching')
 

else:

 print('xato, balansizni toldiring')




if a == 2:
    print('english')
    Password = int(input('Password: '))
    print('Welcome to menu')
    menu = 'Choose options bellow'
    print(menu)
    print(Password)
    function = '''

1:balance
2:withdaraw money
3: add money
4: add money to phone
'''
print(function)


mama = int(input('Choose menu options: '))

print(mama)

if mama == 1:
  print('Out of balance: 100000.00 som')

  if mama == 2:
      
   print('Withdraw money: ')

   if mama == 3:
          
     print('Add money: ')

     if mama == 4:

       print('Phone number entered: ')

     else:

       print('enter your correct phone: ')

   else:
          
     print('error, add money: ')

  else:
      
    print('pay correct: ')
 

else:
  
 print('error, top up your balance: ')






