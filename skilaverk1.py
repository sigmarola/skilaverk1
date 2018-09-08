val = str(input('Veldu forrit(1-4):'))
#aðalvalmynd
if val == '1':

    mydict = {'Finnur':7785214,
              'Nonni':6568525,
              'Samúel':4852541,
              'Siggi':7841595,
              'Jósef':6524148,
              'Jón':7774147,
              'Olli':6565565,
              'Gunnar':8475145,
              'Villi':8785487,
              'Magnús':6365256}

    nafn = ""
    nyttNafn = ""
    nyttNr = ""
    #valmynd
    def menu():
        print("1: Finna símanr.", '\n'
              "2: Bæta við númeri", '\n'
              "3: Eyða númeri", '\n'
              "4: Breyta númeri", '\n'
              "5: Hætta")
    #listi yfir nofn
    def showDict():
        for x, y in mydict.items():
            print(x, y)
        return
    #val hvort þú villt sjá lista yfir nofn
    def showDictVal():
        print("Sýna skrá?: ")
        val = input("Y/N")
        val = val.upper()
        if val == "Y":
            for x, y in mydict.items():
                print(x, y)
            return
        else:
            return
    #valmynd hefst
    while 1:
        menu()
        inpt = str(input("d:"))
        #Fynna símanr. með nafni
        if inpt == '1':
            nafn = input("Finna nr. hjá: ")
            x = mydict.get(nafn)
            if x == None:
                print("Nafn fannst ekki!")
            else:
                print(x)
        #Bæta inn nýju nafni og símanr.
        elif inpt == '2':
            nyttNafn = input("Nýtt nafn: ")
            nyttNr = int(input("Nýtt númer: "))
            mydict [nyttNafn] = nyttNr
            print('"%s" Var bætt við'%(nyttNafn))
            showDictVal()
        #Eyða nafni og símanr.
        elif inpt == '3':
            nafn = input("Hverjum villtu eyða úr skrá?")
            mydict.pop(nafn)
            showDict()
            print('"%s" Var eytt'%(nafn))
        #breyta símanr.
        elif inpt == '4':
            showDict()
            nafn = input("Breyta síma hjá: ")
            nyttNr = int(input("Nýtt númer: "))
            mydict[nafn] = nyttNr
            showDictVal()
        #Hætta
        elif inpt == '5':
            break
        else:
            print('Rangt val')
elif val == '2':
    nafnForr = 'FOR1TÖ05CU'
    nafnGso = 'GSÖ1TÖ05AU'
    #skráir nemendur í hópa
    def skraihop():
        fjoldi = int(input("Hve margir eru skráiðir í hóp: "))
        listi=[]
        nafn=""
        for x in range(fjoldi):
            nafn=input("Skrá nafn: ")
            listi.append(nafn)
            listi.sort()
        return listi
    print("skrá í FOR1TÖ05CU")
    forr = skraihop()
    print("skrá í GSÖ1TÖ05AU")
    gso = skraihop()
    #synur hópa
    def synaAfanga(afangi):
        for x in afangi:
            print(x)
        return
    #ber saman hvort nemandi sé í báðum hópum
    def beraSaman(afg1, afg2):
        listi=[]
        for x in afg1:
            if x in afg2:
                listi.append(x)
        listi.sort()
        return
    #sýna hópa
    print('Nemendur í %s: '%(nafnForr))
    synaAfanga(forr)
    print('Nemendur í %s: '%(nafnGso))
    synaAfanga(gso)
    #badir = beraSaman(forr, gso)
    print('Nemendur í báðum áföngum:')
    """if badir:
        print(beraSaman(forr, gso))
    else:
        print('Enginn')"""
    print(beraSaman(forr, gso))
    #segir hvor hópur er stærri
    def synaStærri(afg1, afg2):
        if len(afg1) > len(afg2):
            print('FOR1TÖ05CU er með fleiri nemendur')
        elif len(afg1) < len(afg2):
            print('GSÖ1TÖ05AU er með fleiri nemendur')
        else:
            print('Áfangar erum með jafn marga nemendur!')
        return

    synaStærri(forr, gso)
    #færir tvo öftustu úr hóp í annan
    def færaTvo(afg1, afg2):
        listi=[]
        listi = afg1 + afg2[:2]
        return listi
    #print(færaTvo(forr, gso))
    print('Tveir síðustu úr %s bætt í %s:'%(nafnForr, nafnGso),'\n',(færaTvo(forr, gso)))
elif val == '3':
    #nafn of lykilorð slegið inn
    user = input('Nafn: ')
    pssw = input('Lykilorð: ')

    userOK=False
    psswrdOK=False
    #les úr skrá og setur í lista
    skra = open('skra.txt' ,'r')
    innihald = skra.read()
    skra.close()
    linur = innihald.split("\n")
    #gá hvort notandi sé til, og hvort lykilorð sé rétt
    for x in linur:
        rn = x.split(';')[0]
        if rn == user:
            userOK=True
            if x.split(';')[1] == pssw:
                psswrdOK=True
                break
    if not userOK:
        print('Notandi ekki til')
    elif psswrdOK:
        print('Halló, ' + user)
    else:
        print('Rangt lykilorð')
elif val == '4':
    strengur = str(input('Sláðu inn nafn: '))
    nyr =''
    #öðrum hvejum staf er víxlað
    for x in range(0,len(strengur),2):
        if x+1 > len(strengur):
            nyr = nyr + strengur[x]
        elif x == (len(strengur)-1):
            nyr = nyr + strengur[x]
            break
        else:
            nyr = nyr + strengur[x+1] + strengur[x]
    print(nyr.upper())
    denyr=''
    #sama gert hér til að afrugla orð
    for x in range(0,len(nyr),2):
        if x+1 > len(nyr):
            denyr = denyr + nyr[x]
            print(denyr)
        elif x == (len(nyr)-1):
            denyr = denyr + nyr[x]
            break
        else:
            denyr = denyr + nyr[x+1] + nyr[x]
            print(denyr)
    print(denyr.upper())
else:
    print('rangt val')









