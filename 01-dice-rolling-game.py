# Ask: roll the dice?
# If user enters y
#    Generate two random numbers
#    Print the numbers
# If user enters n
#    Print "thank you"
#    Terminate
# Else
#    Print "invalid input"

# burada ilk defa random modülünü import ediyoruz
import random
# hatırlatma: modül ile fonksiyon arasındaki fark:
# modül: python kütüphanesinden bir dosya
# fonksiyon: o dosyanın içindeki bir işlev

# random modülünün amacı rastgele sayılar üretmektir

# kullanıcıdan girdi alıyoruz
# girdiyi küçük harfe çeviriyoruz
while True:  # sonsuz döngü başlat
    user_input = input("Do you want to roll the dice? (y/n): ").lower()
    if user_input == "y":  # eğer kullanıcı "y" girdiyse
        dice1 = random.randint(1, 6)  # 1 ile 6 arasında rastgele bir sayı üret
        dice2 = random.randint(1, 6)  # 1 ile 6 arasında rastgele bir sayı üret
        print(f"You rolled {dice1} and {dice2}")  # sonucu yazdır
    elif user_input == "n":  # eğer kullanıcı "n" girdiyse
        print("Thank you!")  # teşekkür mesajı yazdır
        break  # döngüyü sonlandır
    else:  # eğer kullanıcı geçersiz bir girdi girdiyse
        print("Invalid input")  # geçersiz girdi mesajı yazdır
        # program burada sona erer
# burada while kullanmamızın nedeni kullanıcı geçerli bir girdi verene kadar sormaya devam etmesidir

# for'dan farkı:
# for döngüsü genellikle belirli sayıda tekrarlama için kullanılır
# while döngüsü ise belirli bir koşul doğru olduğu sürece devam eder
# bu yüzden burada while kullanıyoruz çünkü kullanıcı geçerli bir girdi verene kadar devam etmesini istiyoruz
