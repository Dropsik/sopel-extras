"""
zbluzgaj.py
Author: Drops

Bluzgator
"""

from __future__ import unicode_literals
import time
import random
from sopel.module import rule

messages = [
"Masz łeb jak sklep , tylko półki puste!",
"Twoja stara jest jak wózek w supermarkecie - wrzucasz 2 złote i pchasz ile chcesz.",
"Twoja twarz wygląda jakby Cię w dzieciństwie z procy karmili.",
"Zamknij gębę , bo muchy się zlatują.",
"pozdrów ojca i gołębie.",
"Jak byłeś mały, to matka nosiła Cię w siatce na psie odchody i napierdalała po krawężnikach - dlatego teraz taki trochę ignorant jesteś.",
"Jak byłaś mała, to matka nosiła Cię w siatce na psie odchody i napierdalała po krawężnikach - dlatego teraz taka trochę ignorantka jesteś.",
"synu Peta i Pojary.",
"córko Peta i Pojary.",
"Zamknij się synu kręconej baby z nosa.",
"Zamknij się córko kręconej baby z nosa.",
"Nie dłub w nosie bo Cię górnik opierdoli.",
"kiedy miałeś ten wypadek? Bo nie wierzę, że masz taką twarz od urodzenia ;-)",
"kiedy miałaś ten wypadek? Bo nie wierzę, że masz taką twarz od urodzenia ;-)",
"Kąsasz schemat?",
"Kąsacie schemat?",
"Ssij mi zwieracz zmutowany mastodoncie, walony przez jednonogą peruwiańską dziwke.",
"Ty koński zwisie źrebaka.",
"spierdolino matki Czesia.",
"Róże są czerwone, fiołki fioletowe, Frankenstain jest paskudny, ale co do cholery stalo sie Tobie !?",
"umyj zęby bo sanepid sie dopierdoli :/.",
"Mów proszę do dupy bo moje uszy są na urlopie.",
"Widziałem Twoich rodziców. Fajni panowie.",
"Twoja matka była przy porodzie?!",
"gdy na Ciebie patrzę to jestem za aborcją.",
"Badania genetyczne wykazały, że kiedy kobieta i mężczyzna podczas stosunku się śmieją - to urodzi się ładne i mądre dziecko. Szkoda że Twoi rodzice tego nie wiedzieli...",
"Twoja dupa jest tak rozepchana że zmieściliby tam szklanego tulipana!",
"Zrobię Ci z dupy Jesień średniowiecza, Ty owsinogi niedopałku krematoryjny!",
"Ty wale spuszczony przez magiczne bobry i wyłomotany przez hinduskiego szamana.",
"Jak byłeś mały, to byłeś tak brzydkim dzieckiem, że Cię psy w piaskownicy piaskiem zasypywały.",
"Jak byłaś mała, to byłaś tak brzydkim dzieckiem, że Cię psy w piaskownicy piaskiem zasypywały.",
"Wiesz jak Cię spłodzono ? Twój stary spuścił się na buta i kopał Twoją starą po piździe.",
"Twoja matka klaszcze u Rubika.",
"Twoja stara pije wode z grzejnika.",
"Wiesz , ostatnio widziałem Cię w sklepie rowerowym na półcę z pedałami.",
"Wiesz dlaczego jesteś taki brzydki? Bo jak byłeś mały, to Ci się kołyska zapaliła i stary gasił Cię łopatą.",
"Wiesz dlaczego jesteś taka brzydka? Bo jak byłeś mała, to Ci się kołyska zapaliła i stary gasił Cię łopatą.",
"Twoja stara pierze w rzece.",
"Twoja siostra kreci kołem fortuny.",
"Twój stary złamał sobie kutasa jak ruchał twoją starą, a Ty jesteś bazarowym chujopijcą.",
"Twój stary złamał sobie kutasa jak ruchał twoją starą, a Ty jesteś bazarową spermo-pijczynią.",
"Pies Cię trącał, a Twoja stara rodziła Cię w kojcu porodowym dla świń.",
"Jesteś wymerdanym przez psy z osiedla sromowałem.",
"Wydupiaj ruchać się z pawianem.",
"Zamiast matczynej miłości w dzieciństwie, doznałeś ojcowskiej miłości z penetracją dupy Ty obrośnięty łopaciarzu.",
"Ty komunistyczny, zarzygany przez stolca rumuńskiego żula betonie.",
"Masz nos jak ogórek kiszony, jesteś jebakiem leśnym, a Twoja mama to całkiem przystojna mężczyzna.",
"Jesteś spuszczonym przez każdego chętnego penera, indoktrynowym śmieciarzem co tańczy z eunuchami.",
"jesteś chujowy fchuj.",
"Twoi starzy zrobili Cię na raty cwelu pomidorowy.",
"Idioto masz ryja jak grzybiarz ty spłodzony w miejscu publicznym, gdzie psy chujami wodę pompują, walcu drogowy z Mozambiku.",
"Twoje dupsko stanie sie moim trofeum myśliwskim!",
"Wąchaj pałe kałożerny stolcu Stalina.",
"Zrobie Ci z jaj druty telegraficzne, Ty zryty wypierdku mamuta.",
"wyglądasz jakby Cię cyganka w biegu wysrała Ty stary ośle!",
"wyglądasz jakby Cię cyganka w biegu wysrała Ty stara proco!",
"Czochraj bobra i ciąg drąg rozepchany kurwiczepku.",
"Zrobię Ci z ryja parking dla ciężarówek ty trędowaty, brudny rzepie.",
"Skrob kabla i przetrzyj chuja ścierą do mycia spalin eustachiasza ciulaty mastodoncie.",
"Masz w dupie bank spermy Ty skutasiony ciulu.",
"Masz w dupie bank spermy Ty skutasiona cipo.",
"ty zropiały cebularzu, masz popierdolone w deklu przerżnięty spermosiorbaczu.",
"ty zropiała cebularo, masz popierdolone w deklu przerżnięta spermosiorbaczko.",
"Jesteś pojebanym debilem, chrumkaj trznadla zamarznięty tamponie na patyku.",
"Azbestowy skwarze na cycku rumuńskiej suki, zerżnięty w dupe przez papużki nierozłączki.",
"Wyglądasz jakbyś wsadzał sobie palce w dupsko Ty sfilcowany, kwadratowy hujogłowcu.",
"Wyglądasz jakbyś wsadzała sobie palce w dupsko Ty sfilcowana, kwadratowa cipo.",
"Wyglądasz jakbyś wsadzał sobie palec w dupsko Ty zapyziały strusi klopsie.",
"jesteś skurwysyńskim, psim odbytem.",
"jesteś skurwiałą, psią kupą.",
"Masz rozjebaną dupę na wszystkie cztery strony świata.",
"Masz rozjebaną dupę na wszystkie cztery strony świata, masz klapczącą pizdolinę.",
"Chapaj dzidę i bierz do pyska póki tryska wygrzmocony świniopasie!",
"Masz dupę zamiast głowy.",
"Jesteś zapiździałym cebulakiem, kąsaj ogóra matkojebco!",
"Wyglądasz jak Hugo w Dolinie Paproci",
"Spadaj na drzewo prostować banany!",
"Spadaj na drzewo liście pompować!",
"Kim Ty  będziesz w przyszłości?! Chyba owocem w Jogobelli",
"Biedny ten Twój mózg ",
"Jak Cię walnę w ten poniemiecki łeb , to Ci się okupacja przypomni.",
"Milcz jak do mnie mówisz! ",
"Wiesz, jak utrzymać idiotę w niepewności? … Powiem Ci później.",
"Wiesz, jak utrzymać idiotkę w niepewności? … Powiem Ci później.",
"Stworzył mnie Bóg, bo lubi piękno, Ciebie, bo ma poczucie humoru.",
"Nie podskakuj, bo nabijesz sobie guza o sufit.",
"Słyszałem, że jak byłeś mały to Cię dotykali patykami, bo nie wiedzieli co to jest.",
"Słyszałem, że jak byłaś mała to Cię dotykali patykami, bo nie wiedzieli co to jest.",
"Słyszałam, że jak byłaś mała to Cię dotykali patykami, bo nie wiedzieli co to jest.",
"Słyszałam, że jak byłeś mały to Cię dotykali patykami, bo nie wiedzieli co to jest.",
"Lubię kolor złoty, ale Twoje zęby  to już przesada.",
"Daj mi swoje zdjęcie , bo chcę sobie zrobić kanapkę z pasztetem.",
"Kochaj deszcz, tylko on na Ciebie leci.",
"Rozbiegnij się i w ściane jebnij ;-).",
"Matka Cię pod latanią poczeła . Dlatego nie masz mózgu.",
"Gdy Cię widzę  szukam zasłony dymnej.",
"Twoi rodzice muszą mieć duże pole... Skoro wyhodowali takiego buraka jak Ty .",
"Masz ryj jak sprzęgło od żuka.",
"Twoja stara wędzi maslo.",
"Twoja stara wie gdzie jest nemo.",
"Daj mi swoje zdjęcie , bo zbieram pokemony.",
"Jak patrze na Ciebie , to nie wiem czy zostałeś poczęty w Hiroszimie czy w Czarnobylu.",
"Smyraj larwę.",
"Gryź koper.",
"Masz kopalnie złota w gębie .",
"Woźny nie posprzątał wszystkiego!",
"Twoja matka zasługiwała na lepsze .",
"Twoja stara bije Cię kablem bezprzewodowym .",
"Gównem ci się odbija .",
"Podobno jak przechodziłeś obok siłowni to zakwasów dostałeś?",
"Masz twarz  jak Pinokio po inwazji Termitów.",
"Mam taki interes ... wyliż mi grzyba.",
"Wyżej srasz niż dupę masz .",
"Połknij język i powiedz jakie to uczucie.",
"Masz mordę jak dzik torbę.",
"Wali Ci z pyska, jak z dupy tygryska.",
"Twoja stara zapierdala.",
"Ty spaczony, nieudany falsyfikacie homo sapiens - wybywaj ze swoją pustą łepetyną na Kamczatkę.",
"Nic dziwnego, że brak Ci części mózgu jeśli przez pierwsze miesiące wisiałeś w kondomie za oknem.",
"Jesteś na poziomie intelektualnym telewizji śniadaniowej!",
"Wszystko z Tobą  ok? Wyglądasz jakby Cię za dzieciństwa w betoniarce kołysano.",
"Niektórym Bóg dał rozum, innym urodę. Tobie  poskąpił jednego i drugiego.",
"Gdyby z głupoty można było produkować prąd, to zasiliłbyś nie jedno miasto , wiesz?",
"Gdyby z głupoty można było produkować prąd, to zasiliłabyś nie jedno miasto , wiesz?",
"Twoja uroda  razi moje poczucie estetyki.",
"Masz szczęście , że oddychanie to odruch bezwarunkowy, sam byś go nie opanował.",
"Jesteś chodzącym dowodem na to , że ewolucja może przebiegać wstecz.",
"Jeśli w reinkarnacji ma znaczenie inteligencja, to będziesz papierem toaletowym.",
"Nasza dalsza konwersacja nie ma najmniejszego sensu merytorycznego, albowiem egzystujesz w zbyt płytkim brodziku intelektualnym, a Twoja elokwencja, nie jest adekwatna do mojej erudycji - co koliduje z moimi imperatywami",
"Ty senarze jambiczny! Zwersyfikuj sobie średniówkę, bo Ci się metrum rozpada, amfimakrze niedorobiony!",
"Weź swoje widełki replikacyjne i idź się bawić do innej duplikacji!",
"Gdyby głupota umiała latać - latałbyś 10 km nad ziemią .",
"Gdyby głupota umiała latać - latałabyś 10 km nad ziemią .",
"Gdyby wsadzić Twój mózg do łebka od szpilki - to byłaby grzechotka.",
"Jesteś tak głupi, czy na prawdę oszukałeś przeznaczenie ?",
"Jesteś tak głupi, czy na prawdę oszukałaś przeznaczenie ?",
"Lepiej idź na łąkę komary doić.",
"Jak się nauczysz klaskać czołem to pogadamy.",
"Mózg na gówno zamieniłeś?",
"Mózg na gówno zamieniłaś?",
"Jak mówisz do mnie to zęby na baczność a nie co drugi wystąp!",
"Ty podjednostko aspołeczna.",
"Ty władco kurzu tzw. tumanie!",
"Jak patrzę na Ciebie  to tracę wiarę w ludzką inteligencję.",
"Ja na ogół unikam takich konfrontacji, ale wiadomo, że czasem sytuacja tego wymaga.",
"Uważam że poprostu jesteś nieszkodliwym idiotą, ale nie każdy ma o tobie tak dobre zdanie jak ja.",
"Ogol pięty!",
"matka Ci jajowody na kokardke zawiązała.",
"Wyglądasz jak kwit na węgiel.",
"Coś ci się zassało w mózgu.",
"Urwałeś się z choinki wielkanocnej?",
"Urwałaś się z choinki wielkanocnej?",
"Brzęczysz jak stary tramwaj.",
"Wszystko w porządku porozrzucane?",
"Nie słupa to wina, ze ślepy go nie widzi.",
"Jesteś dowcipny jak taczka gnoju.",
"Jesteś błyskotliwy jak salceson ",
"Bywają przypadki, ze są dzieci bez matki.",
"Wyglądasz jak siódme dziecko baby jagi.",
"Będą z Ciebie ludzie, jak Cię mrówki z cukrem zjedzą.",
"Masz czoło jak skocznia narciarska.",
"Gdyby za powierzchnie mózgu pobierali podatek, to byś dostał rabat!",
"Gdyby za powierzchnie mózgu pobierali podatek, to byś dostała rabat!",
"Masz gębę jak pęknięta deska klozetowa.",
"Jesteś szybki jak rakieta radzieckiej konstrukcji.",
"Nie przychodź do mnie do domu bo mi pies ucieknie.",
"Daj mi swoje zdjęcie, bo mi krowa nie chce zdechnąć.",
"Masz nawalone jak cyganka w tobołku.",
"Masz gębę jak tłuczek do ziemniaków.",
"Jesteś rozwinięty jak papier toaletowy.",
"Jesteś rozwinięta jak papier toaletowy.",
"Wyrobiłeś się jak gumka w gaciach.",
"Wyrobiłaś się jak gumka w gaciach.",
"Masz łeb z tego materiału co kangur torbę!",
"Masz oczy jak wejście AUDIO-VIDEO.",
"Wyrobiłeś się jak majtki w kroku.",
"Wyrobiłaś się jak majtki w kroku.",
"Jestem onieśmielony Twoim głupim wyrazem twarzy .",
"Jestem onieśmielona Twoim głupim wyrazem twarzy .",
"Jesteś genialny jak szczur doświadczalny.",
"Jesteś czarująca jak futro z zaskrońca.",
"Jesteś ciemny jak dwunasta w nocy!",
"Jesteś czuła jak klisza fotograficzna",
"Gdybym miął gębę jak Ty , to bym codziennie chodził pod parasolem.",
"Gdybym miąła gębę jak Ty , to bym codziennie chodził pod parasolem.",
"Masz cycki jak ser Tylżycki.",
"Zamknij gębę, bo muchy się zlatują.",
"Twoja stara nie ma dzieci.",
"Twoja stara nurkuje w studni.",
"Ale z ciebie  cipka niewydymka.",
"Masz ryj jakby Cię łopatą gasili.",
"Ty koci zwisie w gumofilcu.",
"Ty odtylcowy wujkojebco",
"Ty kawale chama w odcieniach Yellow Bahama.",
"Twoja Stara zamiata pustynie.",
"Czy istniejesz również w wersji z mózgiem?",
"Twoje zęby są jak gwiazdy na niebie - żółte i daleko od siebie.",
"Miałem zostać Twoim ojcem , ale mnie kundel wyprzedził.",
"Byłeś w Laponii? Dlaczego Ci mózg zamarzł?",
"Byłaś w Laponii? Dlaczego Ci mózg zamarzł?",
"Twoja stara jest taka gruba, że zjdęcie do paszportu robili jej satelitą.",
"Twoja stara to twój stary.",
"Twój stary to teletubiś.",
"Wyglądasz  jakby Cię cyrklem strugali.",
"masz mordę jak chodnik.",
"Nie przeżywaj bo gaci nie dopierzesz!",
"Wkładasz nogi do wody i mówisz że to grzybowa.",
"Twój stary jest saperem? Bo masz morde jak niewypał.",
"Twoja stara przewija pasek w TVN24.",
"Twoja metryka urodzin jest listem z przeprosinami do producenta kondomów.",
"masz morde jak akumulator, tylko ładować.",
"Ty kurwo bez szkoły!",
"Masz ryj jak spłuczka klozetowa tylko zpuścić w nim gówno.",
"Przeczochrany rodzynie z dupy, masz ryj jak trolejbus.",
"Jesteś gównogębnym chujem, połknij gluta próchnico!",
"Mlaskaj pytonga i czep sie tramwaju zafajdany stolcu rumuńskiego żula Alberta.",
"Masz pryszcza między uszami ty przydupasie.",
"Zrobię Ci  z dupska chińską czapę, Ty pedofilski stolcu Hitlera.",
"Masz wrzody na chuju , wysadzony w dupe gównożerco.",
"Wyglądasz jakbyś spierdolił z wiadra podczas skrobanki, Ty molestowany wieprzu.",
"Wyglądasz jakbyś spierdoliła z wiadra podczas skrobanki, Ty molestowana świnio.",
"Wyglądasz jakbyś codziennie żarł parujące kloce, Ty capiący psi napletku.",
"Męcz tatara zakurwiały jak kurwa worku po nawozach.",
"Stary gdzie taka żyzna gleba jest, że takie dorodne buraki rosną?!",
"Pełzaj flaka i pchaj wibrator zachujały szmaciarzu.",
"Jesteś zgrzybiałym lumpem, pieprz gówno przez rure ryju.",
"Ty pojebańcu z Wólki Tatrzańskiej",
"Jesteś pojebany jak lato z radiem.",
"Jesteś pojebana jak lato z radiem.",
"Jebany przez stado goryli czereśniaku, skrzyżuj nogi bo Ci z grzyba bucha stolcolubny rodzynie bengalskiej świni!",
"Masz zgrzybiałego fiuta Ty srakojebny zjebie genetyczny.",
"Twarzowe zapłaciłeś, że z taką mordą popierdalasz?",
"Twarzowe zapłaciłaś, że z taką mordą popierdalasz?",
"Zrobię Ci z mordy origami Ty azbestowy łamago.",
"Kulaj smara zryty chujcu.",
"Zrobie Ci z dupy szafke na buty, Ty pedalski wielbłądzi naplecie utarzany w piasku.",
"Ty wykastrowany koguci prąciu, pizgany w oko przez stolca rumuńskiego żula.",
"Zrobie Ci z dupy chińską porcelane Ty trabanci tłoku.",
"Jesteś zwykła pała, wyglądasz mi na pedała.",
"Stara Cię w betoniarce kołysała.",
"Jesteś zakutasionym capem ze spuchniętymi jajami, powyrywaj sobie włosy z dupy włosie łonowy orangutana.",
"Masz zęby jak płot po wiejskiej zabawie ty pomiocie chińskiego taksówkarza!",
"Widzialem Twoją starą na balkonie, jak sobie goliła dupe trójwidłową, samobieżną kosiarką do betonu.",
"Wyglądasz jakbyś językiem czyścił chodniki z psich gówien.",
"Wyglądasz jakbyś językiem czyściła chodniki z psich gówien.",
"Ty kurewski zoofilu, masz zgrzybiałego fiuta toporem jebany lachociagu pawiana na wielbłądzim garbie.",
"Zrobie Ci tornado na twarzy Ty toporem jebany liszaju.",
"Zapierdala Ci z ryja jak cyganowi z rozpora.",
"Pełzaj flaka i pchaj wibrator zachujały szmaciarzu.",
"Ty łysy wytrysku kojota.",
"Stolcolubny kutafonie, walony w kakę przez sparaliżowaną, azerbejdżańską kurwe.",
"jesteś jebanym w dupę kocmołuchem z Tasmanii, wyruchanym przez jeżozwierza.",
"czemu liżesz jajka swojego przyjaciela? Przecież mówiłeś, że lubisz jak Cię gwałci nogą i robi drenaż odbytu środkami spożywczymi.",
"z ryja Ci kapie sperma żula.",
"podobno lubisz lizać bezdomnych pod pachami i po podjajczu, zwłaszcza takich nieumytych kocmołuchów, którzy koczują na centralnym.",
"widziano Cię jak tasujesz się w ZOO patrząc na goryla i jednocześnie szamiesz banana.",
"masz w dupie stolec kolegi. Po ostatniej imprezie wymieniliście się między sobą gówienkiem. Jak Ci się je nosi?",
"jesteś chory na spermatogenezę i wycieka Ci sperma z dupska.",
"jesteś chora na spermatogenezę i wycieka Ci sperma z dupska.",
"moczysz się w nocy kiedy gwałci Cię tata w związku, zalecam Ci wizytę u lekarza odbytnika.",
"masz ochlapnięte uszy od trzaskania minet starym babom.",
"Są słuchy, że Twoja stara kisi w dupie nielegalne ogóry.",
"Siedziałem sobie ostatnio przebrany za księdza i jak mi sie przyszła spowiadać Twoja stara,  wiesz, że ona Ci w dupie grzebie jak spisz, a potem Ci palcem rysuje na plecach pentagramy?",
"Starzy wydłubali Cie z kinder niespodzianki.",
"W sumie nie ma co dymać psa w chorą dupę.",
"Wyglądasz jak skrzyżowanie wagonu z węglem z funkcjonariuszem Chińskiej Armii Ludowej.",
"śmierdzi Ci z usta bąkiem starej baby.",
"słyszałem, że lubisz spijać ropę z pękających na dupie ropni.",
"rośnie Ci huba na dupie i mech na stopie. Liż kalosz.",
"jak to się dzieje, że szamiesz rzygi i sam nie rzygasz?",
"chłeptaj piździsko psie zapinany w ucho, kmiocie odbytniczy.",
"Twoja dupa robi za stację dokującą dla murzyńskich kutasów.",
"słyszałam, że zarabiasz dając dupy małpom z ZOO?",
"Twoje ulubione jedzenie to kał z dodatkiem spermy, łoniaków i kóz z nosa.",
"wyglądasz jak zrolowana koza z nosa.",
"czemu lubisz pić mocz króliczy i wąchać bąki krowie?",
"podobno w przedszkolu byłeś bity głową o pisuar i zjebał Ci się baniak.",
"podobno w przedszkolu byłaś bita głową o pisuar i zjebał Ci się baniak.",
"jesteś wynikiem kaziroctwa.",
"Ty debilu skończony mówiłem Ci, że kału się nie szamie, teraz jebie Ci z ryja jak z TOI TOI'A!",
"słyszałem również, że lubisz trzymać własne palce w swojej dupie oglądając telewizję?",
"weź się odśwież bo jebiesz jak odchody wielkiej dupy leżące na słońcu.",
"ruchałeś się z własnym kuzynem i zostałeś zalany po pachy jebany stworze.",
"ruchałaś się z własnym kuzynem i zostałaś zalana po pachy jebana łajzo.",
"Ty gruby, jebany skurwysynu z plamą ze spermy na poliku.",
"Ty gruba, jebana rusałko z plamą ze spermy na poliku.",
"słyszałem, że lubisz jak Ci wsadzają jądra do buzi.",
"wyleciałeś z kleksem swojej starej podczas sranka zafajdany debilu.",
"wyleciałaś z kleksem swojej starej podczas sranka zafajdany stonko.",
"słoiku zajebany, co wpierdala pączki ze Społem.",
"jesteś szambonurkiem pracującym za złotówkę, który jest gwałcony w TOI TOI'u.",
"w Twoim ryju można puszczać statki tyle masz tam spermy końskiej.",
"zapyziały koczkodanie, czemu w oczodołach zamiast gałek ocznych masz jądra?",
"słyszałem, że lubisz jak Cię walą w zad jednocześnie waląc konia.",
"słyszałam, że lubisz jak Cię walą w zad jednocześnie waląc konia.",
"jesteś ssaczostolcem lubiącym napar z odchodów woźnego ze szkoły podstawowej.",
"masz nos rozjebany od kutasów i wyglądasz jak Eskimos.",
"słyszałem, że na kolację opierdalasz śmieci segregowane z wywarem z siura żula.",
"słyszałam, że na kolację opierdalasz śmieci segregowane z wywarem z siura żula.",
"Biorąc pod uwagę wszystkie czynniki wpływające na Twój wygląd , muszę rzec, iż wyglądasz jak niegodziwa, drylowana w anusa obstrukcja.",
"Wyglądasz jakbyś spierdolił z wiadra podczas skrobanki Ty przerżnięty walcu drogowy z Ukrainy.",
"Wyglądasz jakbyś spierdoliła z wiadra podczas skrobanki Ty przerżnięta suko drogowa z Ukrainy.",
"Szczerze mówiąc, jestem zmuszony stwierdzić, iż wyglądasz mi na nielubianego przez księdza Jankowskiego, niecnego koprofila z peweksu.",
"Szczerze mówiąc, jestem zmuszona stwierdzić, iż wyglądasz mi na nielubianego przez księdza Jankowskiego, niecnego koprofila z peweksu.",
"Szczerze mówiąc, jestem zmuszona stwierdzić, iż wyglądasz mi na nielubianą przez księdza Jankowskiego, niecnego koprofila z peweksu.",
"Szczerze mówiąc, jestem zmuszony stwierdzić, iż wyglądasz mi na nielubianą przez księdza Jankowskiego, niecnego koprofila z peweksu.",
"wyglądasz jak wydrylowany przez mongolskich uchodźców, niewdzięczny jurny wał.",
"Jesteś majestatycznym, niewymrożonym w katalońskim kanale naleśnikiem.",
"... na dodatek jesteś despiralizowanym przez hordę genetycznie zmutowanych murzynów pyrem co robi kupę na dworze, a Twój stary to strusi klops.",
"Generalizując, konstatuję, iż wyglądasz mi na mielonego przez kosiarkę spalinową, stolcolubnego ipsacjonistę.",
"Masz dupsko jak słonicy po zalotach słonia Ty paszczurze.",
"Pedofilski kapciu, masz morde jak tatarskie siodło.",
"Tarzaj banana zapiździały zmazie nocny nietoperza.",
"Wyglądasz jakby Ci stary codziennie kutasem kakao w dupie mieszał.",
"Ty zryty stulejarzu, wypatroszony przez stado spoconych murzynów i stado goryli chorych na raka macicy.",
"Jesteś zwykłym spermosiorbarczem, przyjmij pozycję zbierania ryżu capie ze spuchniętymi jajcami.",
"Zrobię Ci z ryja składowisko odpadów toksycznych, Ty owsinogi mapecie.",
"Miękkim chujem jesteś robiony okurwieńcu pierdolony.",
"Wyglądasz jak pomidor z wrodzoną wadą mózgu Ty azbestowy fiucie z rozjebanej chaty szmaciarza z Uzbekistanu.",
"Wyglądasz jak pomidor z wrodzoną wadą mózgu Ty azbestowa cipo z rozjebanej chaty szmaciarza z Uzbekistanu.",
"Wyglądasz jakby Twoja stara podczas ciąży miała kurwicę macicy, Ty sfilcowany wypierdku mamuta z faludży.",
"Wyglądasz jakby Twój stary spuścil się na gnój i słonce Cie wychodowało, Ty zafajdany wielbłądzi naplecie utarzany w piasku.",
"Wyglądasz jakbyś z pizdy na nartach wyjechał, wykastrowany rodzynie bengalskiej świni!",
"Masz grzywkę jak Hanka Bielicka pod pachami.",
"Co sie tak szczerzysz jak szczerbaty na suchary?",
"Ty przerżnięty bułgarski wymiocie z muszli klozetowej.",
"Twój stary był piekarzem, dlatego masz ryj jak rozjebany naleśnik.",
"Wyglądasz jak kwazimodo po trepanacji czaszki, Ty stolcu rumuńskiego żula!",
"Ty pampersie używany przez stado knurów na zmianę.",
"Co ci się stało? ...a sorry Ty  tak wyglądasz.",
"Masz ryj jak boisko do krykieta, Ty toporem jebany rurociągu z Mongolii!",
"Masz ryj jak boisko do krykieta, Ty toporem jebana spermopijczynio z Mongolii!",
"Wysadzony w dupe kurwiczepku, walony w kakao przez ojca Rydzyka.",
"Wysadzona w dupe kurwiczepku, walona w kakao przez ojca Rydzyka.",
"Zajebie Ci w ten kurwa głupi ryj, aż się porzygasz komunijnym bigosem.",
"masz ryj jak dupsko orangutana, Ty niedopałku krematoryjny.",
"Wyglądasz jakbyś zjadł stęchłe łożyska brudnych cyganek, Ty ryju z dworca w Zazibarze!",
"Wyglądasz jakbyś zjadła stęchłe czopy brudnych cyganów, Ty lumpiaro z dworca w Zazibarze!",
"Masz na głowie gówno krowie Ty spruchniały włosie z przepoconej dupy.",
"zrobie Ci z głowy spust na fekalia, Ty toporem jebany wymiocie czeczeńskiego partyzanta z kreciej nory!",
"Twoja stara to pancerna rebeka.",
"Jesteś zakutasionym liszajem, śsij druta mudżachedinie.",
"Zaraz Twoje  genitalia zmienią sie w bezkształtną masę krwi i kości.",
"Masz kurewsko niewyjściowy ryj.",
"Wyglądasz jakby robili Cię przez telefon i zabrakło impulsów.",
"Wyglądasz jakby Ci ojciec zaorał ryj kutasem Ty spruchniały szczochu.",
"Wyglądasz jakby Ci ojciec zaorał ryj kutasem Ty spruchniała szczyno.",
"Ty zmutowany odprysku nocnika, wąchaj krecika cienki jak zupa więzienna mutancie z Ukrainy.",
"Jakby Twoja matka wiedziała co urodzi, to by sobie sama skrobane zrobiła łyżką stołową.",
"Wyjebany łamago, jebany w odbyt przez bażanty z Mongolii.",
"Mój Tata chce żebyś nas odwiedził , bo naprawia rower i nie wie jak wygląda pedał.",
"ile trzeba było Twojej starej śniegu w pizde napchać żeby ulepić takiego bałwana?",
"Cała Polska jebie Twoją starą.",
"Masz pytę jak niemowle ty skurwysynu.",
"Zafajdany koguci prąciu, masz morde jak radziecki poligon zezowaty pierdolcu.",
"Gryź batona scyborgizowany zjebie genetyczny.",
"Kąp się w kale jebany pedale, cofnięty w rozwoju dropsie, wyruchany przez syna grabarza.",
"Wiesz czemu Twoja stara nie jeździ na rowerze? bo jej dzyndzel w łancuch wchodzi i budzi całe osiedle.",
"Jak byłeś mały to na gówno mówiłeś papu.",
"Targaj dzbana i ślizgaj mikołaja wygrzmocony bagiecie z czarnobyla.",
"Generalnie rzecz biorąc to ostentacyjnie pierdzę w Twoim kierunku.",
"masz rozjechaną autostrade zamiast dupy, Ty jebany przez stado goryli, szczotkuj zęby pastą stolcową.",
"masz rozjechaną autostrade zamiast dupy, Ty jebana przez stado goryli, szczotkuj zęby pastą stolcową.",
"Zapierdalaj TIK TAK'a ciulaty psi wentylu cyrklem w dupe ładowany przez psa sąsiada.",
"Ty zawszony bezmózgowcu, pocałuj mnie w dupę, przeczochrany wytrysku kojota.",
"Ty scyborgizowany cipolągu z Sierra Leone.",
"Masz takiego garba, że sznurówki zawiązujesz na stojąco, Ty śmierdzący rodzynie z dupy.",
"Wyglądasz jakby Ci stary codziennie kutasem kakao w dupie mieszał, Ty chujcu z Burkina Faso.",
"Jesteś pedofilskim fletem komunistycznym, grzebaj w rowie obciągańcu.",
"Ubierasz sie jak szczór na otwarcie kanału.",
"Lubię żółty kolor, ale Twoje zęby to przesada.",
"Twój dziadek dzwonił, żebyś mu oddała ubrania.",
"Twoja mama mówi, że Cię kocha? Robi Cię w chuja!",
"Twój stary kocha Cię tylko w nocy.",
"Ty ofiaro przemmysłu gumowego.",
"Podniecasz się jak murzynek bateryjką.",
"Wyglądasz jakby Cię w nocy stado murzynów ruchało.",
"Człowieku, czy Twoja matka ćpała jak była w ciąży?!",
"Odpierwiastkuj się ode mnie Ty ilorazie nieparzysty, bo jak Cię zlogarytmuję, to Ci zbiór zębów wyjdzie poza nawias.",
"Spadaj na drzewo, dokończ ewolucję.",
"Błysnąłeś jak chrząstka w salcesonie!",
"Jakbym miała taką twarz jak Ty , to bym się nauczyła na niej siadać.",
"Jakbym miał taką twarz jak Ty , to bym się nauczył na niej siadać.",
"Widzę, że twoja latarnia intelektu nie świeci zbyt jasno.",
"Twoje wypowiedzi nie przekraczają poziomu glonów, żyjących kilometr pod powierzchnią wody.",
"Jestem chirurgiem plastycznym i szukam takiego wyzwania jak Twoja twarz .",
"Twoi rodzice chyba do dziś rzucają kamieniami w bociany.",
"Gdy Cię wiedzę mam chęć wysłać sms-a o treści pomagam",
"Wiesz co zgasiła bym cię ale gówn* się nie pali.",
"Generalnie rzecz biorąc, myślę, że wyglądasz na pierdopędnego, ospermionego przez stado knurów kabana.",
"Generalnie rzecz biorąc, myślę, że wyglądasz na pierdopędną, ospermioną przez stado knurów kabanicą.",
"Niech Ci kał da popalić, Ty zmutowany wytrzeszczu.",
"Wyglądasz jak szynka w siatce - tłuszczyk Ci się wylewa.",
"Jesteś łasuchem owczych odchodów, a Twój stary to prawiczek.",
"Eh, muszę orzec, iż zachowujesz się jak ospermiony przez nieślubne dziecko Frankensteina, bezpański kaktus.",
"Masz mordę jak papier ścierny, jesteś wymiętoszonym przez stado słoni z puszczy międzyrównikowej wytryskiem kojota bez ubrania.",
"Twoja stara jest taka gruba, że maluje paznokcie u lakiernika.",
"Wiesz co, jestem zmuszony stwierdzić, że wyglądasz na zardzewiałego, nieoświeconego wykałaczką przez bezdomne świstaki odchoda.",
"Wiesz co, jestem zmuszona stwierdzić, że wyglądasz na zardzewiałego, nieoświeconego wykałaczką przez bezdomne świstaki odchoda.",
"Jesteś zapyziałym kaczym pipkiem, co się kąpie w odchodach.",
"Ty pokurczony pampersojadzie, nafaszerowany nazistowskimi ideami żęchole nieoświecony przez stado knurów.",
"Heh, muszę stwierdzić, że zachowujesz się jak wściekły, spłodzony w miejscu gdzie psy chujami wodę pompują psi szczoch.",
"Twoja stara robi zdjęcia aparatem słuchowym",
"Jesteś zakręcony jak słoik po ogórkach na zimę",
"Jesteś zakręcona jak słoik po ogórkach na zimę",
"Ulałeś się staremu z fiuta, niechcący wpadłeś do pępka, a stara głupia kurwa wtarła Cię w pizdę, bo myślała, że to krem na odleżyny, jebany kurwa ciapaty śmieciu.",
"Ta przerwa między zębami to na rzetony?",
"Twoja stara pracuje w bankomacie",
"Twoja stara jest taka tępa, że nie da się jej naostrzyć",
"Jestes tak przyjebany jak papa do dachu.",
"Jak byłeś mały to miałeś spięcie w inkubatorze.",
"Jak byłaś mała to miałaś spięcie w inkubatorze.",
"Słodzisz gorzkie żale",
"Zabierz matkę bo mi pod oknem szczeka",
"Twoja stara opala się przy słoneczku z Gadu Gadu.",
"Twoja stara obciągała Konia Trojańskiego",
"Twoja stara jest zakręcona jak dziwka na róże",
"Jesteś taki biedny, że jesz bigos bez kapusty.",
"Jesteś taka biedna, że jesz bigos bez kapusty.",
"Twoja stara myje gary szczotką do kibla",
"Do chrztu Cię na widłach podawali?",
"Twoja stara wymyśla teksty do Tymbarka.",
            ]

@rule('(?i)$nickname\:\s+.*(zbluzgaj|opierdol)(.*)')
def zbluzgaj(bot, trigger):
    """
    Użycie: nick_bota zbluzgaj nick
    """

    text = trigger.group().split()
    answer = random.choice(messages)
    bot.say(text[2] + ": " + answer)
