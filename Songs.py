albums = [
    ("Mankatha",2011,"Yuvan Shankar Raja",
     [
         (1,"Vilayadu Mankatha"),
         (2,"Nee... Naan..."),
         (3,"Machi Open The Bottle"),
         (4,"Nanbane"),
         (5,"Balle Lakka"),
         (6,"Vilayadu Mankatha")
     ]
     ),
    ("Master",2021,"Aniruth Ravichandar",
     [
         (1,"Vaathi Coming"),
         (2,"Andha kanna paathaakaa"),
         (4,"Kutti Story"),
         (5,"Quit Pannuda"),
         (6,"Polakattum para Para"),
         (6,"Pona Pogattum")
     ]
     ),
    ("Thanin Oruvan",2015,"HipHop Tamizha",
     [
         (1,"Thani Oruvan"),
         (2,"Kadhal Cricket"),
         (3,"TheemaiDhaan Vellum"),
         (4,"Aasai Peraasai")
     ]
     ),
    ("Vikram Vedha",2017,"Sam.C.S",
     [
         (1,"Karuppu Vellai"),
         (2,"Yaanji"),
         (3,"Tasakku Tasakku"),
         (4,"Pogatha Yennaivittu"),
         (5,"Gheto Chase"),
         (6,"Sangu Satham")
     ]
     ),
    ("Jil Jung Juk",2015,"Vishal Chandrshekhar",
     [
         (1,"Shoot The Kuruvi"),(2,"Red Road-U"),
         (3,"Domer-U Lord-U"),
         (4,"Casanava")
     ]
     ),
    ("Madras",2014,"Santhosh Narayanan",
     [
         (1,"Madras"),
         (2,"Kakidha Kappal"),
         (3,"Naan Nee"),
         (4,"Aagayam Theepiditha"),
         (5,"Irandhidava")
     ]
     )


]

for Index,value in enumerate(albums):
    Album,year,artist,songs=value
    print("{4})Album:{0}   Year:{1}   Artist:{2}\nSongs:{3}".format(Album,year,artist,songs,Index+1))
    print(" ")

print("Choose an album from the following:")
chosen_album=int(input())

while True:
    if 1<=chosen_album<=len(albums):
        alb=(albums[chosen_album-1])
        title,Year,Artist,Songs=alb
        print("Album:{0}   Year:{1}   Artist:{2}\nSongs:{3}".format(title,Year,Artist,Songs))

        chosen_song=int(input("Choose a Song from the album:"))
        if 1<=chosen_song<=len(Songs):
            Song=Songs[chosen_song-1]
            print("Playing",Song[1])

        break

