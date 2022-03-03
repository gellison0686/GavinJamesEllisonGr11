notDone = True
allCharacters = []
while notDone:
    charList =[]
    name = input("Release Date: ")
    charList.append(name)
    profession = input("Genre: ")
    charList.append(profession)
    level = input("Insanity Level: ")
    charList.append(level)
    allCharacters.append(charList)
    print(f"""
    Release Date: {name }
    Genre: {profession }
    Insanity Level: {level }""")


    answer = input("Ghost Rider? ")
    if answer == "Y":
         print("Too Bad (Cool Emoji With Sunglasses)")
    else:
        print("Pig? ")

    answer2 = input("National Treasure? ")
    if answer2 == "Y":
        print("Too Bad (Cool Emoji With Sunglasses)")
    else:
        print("Face Off? ")

    answer3 = input("Willys Wonderland? ")
    if answer3 == "Y":
        print("Too Bad (Cool Emoji With Sunglasses)")
    else:
        print("Knowing? ")
        
        answer4 = input("Con Air? ")
    if answer4 == "Y":
        print("Too Bad (Cool Emoji With Sunglasses)")
    else:
        print("The Family Man? ")

        answer5 = input("Lord Of War? ")
    if answer5 == "Y":
        print("Too Bad (Cool Emoji With Sunglasses)")
    else:
        print("Gone In 60 Seconds? ")

        answer6 = input("The Rock? ")
    if answer6 == "Y":
        print("Too Bad (Cool Emoji With Sunglasses)")
    else:
        print("Prisoner Of The Ghostland? ")

        answer7 = input("Next? ")
    if answer7 == "Y":
        print("Too Bad (Cool Emoji With Sunglasses)")
    else:
        print("The Unbearable Weight Of Massive Talent? ")

        answer8 = input("Ghost Rider Spirit Of Vengance? ")
    if answer8 == "Y":
        print("Too Bad (Cool Emoji With Sunglasses)")
    else:
        print("Leaving Las Vegas? ")

        answer9 = input("Spider Man Into The Spider Verse? ")
    if answer9 == "Y":
        print("Too Bad (Cool Emoji With Sunglasses)")
    else:
        print("Drive Angry? ")

        answera = input("Mandy? ")
    if answera == "Y":
        print("Too Bad (Cool Emoji With Sunglasses)")
    else:
        print("The Sourcerer's Stone? ")
