zhanr = int(input("Zhanr Soalat Khod Ra Entekhab Konid(Englisi(1) , Joghrafia(2) , Kar ba Kampioter(3) , Olom(4): "))
match zhanr:
    case 1:
        SE = input("MOALEM BE ENGLISI CHI MISHE? (1.TEVER) (2.TEACHER) (3.MODIR) (4.MOAVEN): ")
        if SE == "2": 
            print("DOROST")
        else:
            print("NADOROST")
        SE1 = input("BOOK CASE BE CHE MANAST? (1.KETAB KHAANE) (2.GHAFAS) (3.GHAFASEYE KETAB) (4.KOMOD): ")
        if SE1 == "3":
            print("DOROST")
        else:
            print("NADOROST")
    case 2:
        SJ = input("BOZORGTARIN GHARE JAHAN KODAM AST? (1.AFRIGHA) (2.AMRIKA) (3.OROPA) (4.ASIA): ")
        if SJ == "4":
            print("DOROST")
        else:
            print("NADOROST")
        SJ1 = input("BOZORG TARIN KESHVARE GHAREYE ASIA KODAM AST? (1.ROSIE) (2.IRAN) (3.CHIN) (4.TORKIE): ")
        if SJ1 == "1":
            print("DOROST")
        else:
            print("NADOROST")
    case 3:
        SK = input("BISHTAR AZ KODAM WINDOS ESTEFADE MISHAVAD? (1.WINDOS 7) (2.WINDOS 11) (3.WINDOS 10) (4.WINDOS xp): ")
        if SK == "3":
            print("DOROST")
        else:
            print("NADOROST")
        SK1 = input("KELID HAYE TARKIBI (windos+i) SHOMARA BE KOJA MIBARAND? (1.DESKTOP) (2.SETENG) (3.DOWNLOADS) (4.CONTOROL PANEL)")
        if SK1 == "2":
            print("DOROST")
        else:
            print("NADOROST")
    case 4:
        SO = input("AB AZ CHE ATOM HAYI TASHKILL SHODE AST? (1.HIDROZHEN/OKSIZHEN) (2.HIDROZHEN/SODIOM) (3.OKSIZHEN/MANYAZIOM) (4.SODIOM/MANYAZIOM): ")
        if SO == "1":
            print("DOROST")
        else:
            print("NADOROST")
        SO1 = input("SANG [OBSIDIAN] AZ CHE TARKIBI BE VOJOD MI AYAD? (1.AB VA ASID) (2.AB VA MAVAD MOZAB) (3.MAVAD MOZAB VA ASID) (4.ASID VA SANG) :")
        if SO1 == "2":
            print("DOROST")
        else:
            print("NADOROST")
    case _:
        print("zhanr peyda nashod")

        