#this is a simple mad lib
print("   /|\ ")
print("  / | \ ")
print(" /  |  \ ")
print("/___|___\ ")

class Format:
    end = '\033[0m'
    underline = '\033[4m'
    
print(Format.underline + "My Favorite All Time Player".upper() + Format.end)
print("''' .\
.\
.\
. '''")
Name = input("Enter Your Name: ").upper()
country = input("Enter your country: ").capitalize()
favorite_player = input("Enter favorite player: ").capitalize()
favorite_club = input("Enter your favorite club: ").capitalize()

print("There has been a major talk of the best player of \
all time. Names like Maradona, Ronaldo de Lima, Zidane, Ronaldhinho, Christiano Ronaldo and Messi. \
My name is " + Name + " from " + country + " and as for \
me, my greatest player is " + favorite_player + " and  my favorite club is " + favorite_club  )