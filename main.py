movie = "Dr. Strange"
rating: int = 3
popularity: float = 72.65

if rating >= 4 and popularity > 80:
    print("Highly recommended")

elif rating >= 3 and popularity > 70:
    print("i recommend it. it is good")
    
elif rating <= 2 and popularity > 60:
    print("you should check it out")

else:
    print("Don't watch it. it's a waste of time")
    