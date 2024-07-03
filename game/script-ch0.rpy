label ch0_main:
    stop music fadeout 2.0

    if persistent.playername == "uuddlrlrba" and persistent.monika_unlock is False: # prevents you from going back into it later
        call routeSkip
        $ persistent.skipped = True
        return

    if player == "Tabuukilla":
        call easterEggs
        $ persistent.skipped = True
        return

    
    scene bg residential_day
    with dissolve_scene_full
    play music t2

    init python:
    # testing this guy
        #saveLocked = True
        #persistent.opening_scene = False
        quick_menu = True
        #config.developer = True

    #$ config.developer = True
    $ quick_menu = True
    #$ config.developer = True
    #$ config.console = True
    $ s_name = "???" # fixes some shenanigans down the line 

    #Developer Choice:"
#    menu:
#        m "Select if you've unlocked my route!"
#        "Advance to normal route for testing":
#            m "Okay~"
#            $ persistent.monika_unlock = False
#        "I've unlocked your route.":
#            m "Thanks!"
#            $ persistent.monika_unlock = True
#        "Testing Credits":
#            call credits2

    

    # IF MONIKA UNLOCK, CHOICE HERE
    if persistent.monika_unlock is True:
        menu:
            "Sıradan bir okul günü.--"
            "--ama birşeyler farklı geliyor.":
                "Ama yine de, her zamanki gibi, etrafım okula birlikte yürüyen çiftler ve arkadaş gruplarıyla çevrili."
                $ monika_route_lock = True
                $ monika_route_position = 1
                return
            "--tıpkı diğerleri gibi.":
                "Tıpkı herzaman olacağı gibi."
                $ monika_route_lock = False


    s "Heeeeeeeyyy!!"
    "Uzaktan bana doğru koşan sinir bozucu bir kız görüyorum, dikkatleri üzerine çekebileceğinden tamamen habersizmiş gibi kollarını havada sallıyor."
    "Bu kız Sayori, komşum ve çocukluğumuzdan beri iyi arkadaşım. "
    "Bilirsin, bugün asla bir arkadaş edinmeyi düşünmediğiniz ama birbirinizi çok uzun zamandır tanıdığınız için bir şekilde yürüyen türden bir arkadaş?"
    #show sayori 1a at t11

    # IF MONIKA UNLOCK, CHOICE HERE ON WHETHER SAYORI WAKES UP ON TIME
    if persistent.monika_unlock is True:
        menu:
            "Böyle günlerde okula birlikte yürürdük.--"
            "--Hala da öyle, çünkü hep zamanında uyanıyor.":
                $ s_name = "Sayori"
                "Son zamanlarda bu alışkanlığımızı bir kez daha kazandık."
                show sayori 1a at t11
                s "[player], Benimle gurur duyuyor musun??"
                $ monika_route_lock = True
                $ monika_route_position = 2
                return
            "--ama son zamanlarda uyuyor.":
                "Lise başladığından beri giderek daha sık uyuyakalıyordu."
                "Bu yüzden beklemekten yoruldum ve sadece giderdim."
                $ monika_route_lock = False
    else: 
        "Eskiden böyle günlerde okula birlikte yürürdük ama lise yıllarından itibaren o giderek daha sık uyuyakalırdı ve ben de onu beklemekten yorulurdum."
    #$ persistent.opening_scene = False #debugging line
    "Ama peşimden böyle koşacaksa, kaçsam daha iyi olacak gibi hissediyorum.."
    "Yine de içimi çekip yaya geçidinin önünde boş boş duruyorum ve Sayori'nin bana yetişmesine izin veriyorum."
    $ s_name = "Sayori" 
    show sayori 4p at t11 zorder 2

    s 4p "Haaahhh...haaahhh..."
    s "Yine uyuyakalmışım!"
    s "Ama bu sefer sana yetiştim!"
    mc "Belki, ama sadece durup seni beklemeye karar verdiğim için."
    show sayori at s11
    s 5c "Eeehhhhh, sanki beni görmezden gelmeyi düşünüyormuşsun gibi konuşuyorsun.!"
    s "Bu çok kaba, [player]!"
    mc "Eğer insanlar garip davrandığın için sana bakarlarsa, çift olduğumuzu falan düşünmelerini istemem."
    show sayori at t11 zorder 2
    s 1a "Tamam, tamam."
    s "Ama sonuçta beni bekledin."
    s "Sanırım istesen bile kötü olmak senin içinde yok~"
    mc "Nasıl istersen, Sayori..."
    s 1q "Ehehe~"
    show sayori at thide zorder 1
    hide sayori
    "Birlikte karşıdan karşıya geçip okula gidiyoruz.."
    "Yaklaştıkça, sokaklar günlük gidip gelen diğer öğrencilerle giderek daha fazla benekleniyor."
    show sayori 3a at t11 zorder 2
    s "Bu arada, [player]..."
    

    # IF MONIKA ROUTE UNLOCK, CHOICE HERE

    if persistent.monika_unlock is True:
        menu:
            s "Katılacağın kulübe henüz karar vermedin mi?"
            "Evet, verdim.":
                s "Oooooh! Söyle!"
                $ monika_route_lock = True
                $ monika_route_position = 3
                return
            "İlgilenmiyorum.":
                "Bunu ona doğrudan söylemeye karar verdim."
                $ monika_route_lock = False
    else:
        s "Katılacağın kulübe henüz karar vermedin mi?"



    mc "Kulüp mü"
    mc "Sana daha önce de söyledim, hiçbir kulübe katılmakla ilgilenmiyorum.."
    mc "Bu yıl da kulüplere bakmadım bile."
    show sayori at s11
    s 4h "Eh? Bu doğru değil!"
    s "Bu yıl bir kulübe katılacağına söz vermiştin!"
    mc "Gerçekten mi...??"
    "Eminim ki, birçok konuşmamızdan birinde, onun bahsettiği şeylere kayıtsızca katılmışımdır."
    "Sayori, benimle ilgili biraz fazla endişeleniyor. Oysa ben, oyunlar ve anime ile vakit geçirerek sıradan bir şekilde hayatımı sürdürüyor olmaktan memnunum."
    s 4j "Uh-huh!"
    s "Üniversiteden önce sosyalleşmeyi öğrenemeyeceği ya da herhangi bir beceriye sahip olamayacağı konusunda nasıl endişelendiğimden bahsediyordum."
    s "Mutluluğun benim için gerçekten önemli, biliyorsun!"
    s "Şu anda mutlu olduğunu biliyorum ama gerçek dünyaya alışamadığın için birkaç yıl içinde NEET(Ne eğitimde ne istihdamda) olacağını düşünmek bile beni kahrediyor.!"
    s 4g "Bana güveniyorsun, değil mi?"
    s "Beni senin için endişelendirip durma..."
    mc "Pekala, tamam..."
    mc "Seni mutlu edicekse birkaç kulübe bakıcağım"
    mc "Yinede söz vermiyorum."
    s 1h "En azından biraz deneyeceğine söz verir misin?"
    mc "Evet, sanırım sana söz veriyorum."
    show sayori at t11 zorder 2
    s 4r "Yaay~!"
    "Neden böyle kaygısız bir kızın bana ders vermesine izin veriyorum?"
    "Daha da ötesi, kendimi ona teslim ettiğime bile şaşırdım.."
    "Sanırım onun benim için bu kadar endişelendiğini görmek, kafasının içindeki her şeyi abartıyor olsa bile, onu en azından biraz rahatlatmak istememe neden oluyor."

    scene bg class_day
    with wipeleft_scene

    "Okul günü her zamanki gibi sıradan geçiyor ve ben farkına bile varmadan bitiyor."
    "Eşyalarımı topladıktan sonra boş boş duvara bakıyor, bir nebze olsun motivasyon arıyorum."
    mc "Kulüpler..."
    "Sayori bazı kulüplere bakmamı istiyor.."
    "Sanırım anime kulübüyle başlamaktan başka çarem yok..."

    s "Selamm?"
    show sayori 1b at t11 zorder 2
    mc "Sayori...?"
    "Ben dalmışken Sayori sınıfa girmiş olmalı."
    "Etrafıma bakıyorum ve sınıfta kalan tek kişinin ben olduğumu fark ediyorum."
    s 1a "Seni sınıftan çıkarken yakalarım diye düşünmüştüm ama burada öylece oturduğunu ve dalgın olduğunu gördüm, ben de içeri girdim."
    s "Dürüst olmak gerekirse, bazen benden bile kötü oluyorsun... Etkilendim!"
    mc "Kendi kulübüne geç kalacaksan beni beklemene gerek yok."
    s 1y "Biraz cesaretlendirilmeye ihtiyacın olabileceğini düşündüm."
    mc "Neyi biliyor musun?"
    s 1a "İşte, kulübüme gelebilirsin!"
    mc "Sayori..."
    s 4r "Eveet??"
    mc "...Kesinlikle kulübüne gelmeyeceğim."
    show sayori at s11
    s 5d "Eeeehhhhh?! Kabasın!"
    "Sayori Edebiyat Kulübü'nün başkan yardımcısı."
    "Ama onun edebiyata ilgisi olduğunu hiç bilmiyordum."
    "Aslında, neredeyse eminim ki yeni bir kulübün başlatmak eğlenceli olacağını düşündüğü için yaptı."
    "Kulübü öneren kişiden sonra ilgi gösteren ilk kişi olduğu için, \"Vice President\" unvanını aldı."
    "Bununla birlikte, edebiyata olan ilgimin daha da azalacağı garanti."
    mc "Evet. Anime kulübüne gidiyorum."
    show sayori at t11 zorder 2
    s 1g "Hadi amaa, lütfen?"
    mc "Neden bu kadar önemsiyorsun ki??"
    s 5b "Peki..."
    s "Dün kulübe yeni bir üye getireceğimi söyledim...."
    s "Ve Natsuki kek falan yaptı...."
    s "Ehehe..."
    mc "Tutamıyacağın sözler verme!"
    "Sayori gerçekten o kadar boş kafalı mı yoksa tüm bunları planlayacak kadar kurnaz mı bilemiyorum."
    "Uzun bir iç çektim.."
    mc "Peki... Bir kapkek için uğrarım, tamam mı?"
    show sayori at h11
    s 4r "Evet! Hadi gidelim~!"

    stop music fadeout 2.0

    $ m_name = 'Kız 3'
    $ n_name = 'Kız 2'
    $ y_name = 'Kız 1'

    scene bg corridor
    with wipeleft_scene

    "Ve böylece bugün, bir kek için ruhumu sattığım gün oldu."
    "Sayori'yi kederli bir şekilde okul boyunca ve üst kata kadar takip ediyorum - okulun nadiren ziyaret ettiğim bir bölümü, genellikle üçüncü sınıf dersleri ve etkinlikleri için kullanılıyor."
    "Sayori, enerji dolu bir şekilde sınıfın kapısını açar."

    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4 at l41
    s "Millet! Yeni üyemiz burada~!"
    mc "Sana söyledim, bana 'yeni üye' deme--"
    show sayori at lhide
    hide sayori
    "Eh? Odaya bir göz attım."
    show yuri 1a at t11 zorder 2
    y "Edebiyat Kulübü'ne hoş geldiniz. Seninle tanışmak bir zevk."
    y "Sayori senin hakkında hep güzel şeyler söylüyor."
    show yuri at t22 zorder 2
    show natsuki 4c at t21 zorder 2
    n "Ciddi misin? Bir oğlan getirmişsin.?"
    n "Atmosferi öldürmenin yolu."
    show yuri at t33 zorder 2
    show natsuki at t32 zorder 2
    show monika 1k at t31 zorder 2
    m "Ah, [player]! Ne güzel bir sürpriz!"
    m "Kulübe hoş geldin!"
    show monika 1a
    mc "..."
    "Bu durumda tüm kelimeler benden kaçıyor."
    "Bu klüp..."
    "{i}...inanılmaz sevimli kızlarla dolu!!{/i}"

    show monika at thide zorder 1
    show yuri at thide zorder 1
    show natsuki at f32 zorder 3
    hide monika
    hide yuri

    n 2c "Neye bakıyorsun?"
    n "Bir şey söylemek istiyorsan söyle."
    mc "Ö-özür dilerim..."
    show natsuki at t32 zorder 2
    show yuri 2l at f33 zorder 3
    y "Natsuki..."
    $ n_name = 'Natsuki'
    show yuri at t33 zorder 2
    show natsuki at f32 zorder 3
    n 5s "Hmph."
    show natsuki at t32 zorder 2

    "Adı Natsuki olduğu anlaşılan ekşi tavırlı kız, tanımadığım biri."
    "Ufak tefek olması bana muhtemelen birinci sınıf öğrencisi olduğunu düşündürüyor.."
    "Sayori'ye göre kapkekleri yapan da oymuş."

    show sayori 2q at f31 zorder 3
    s "Huysuzlandığında onu görmezden gelebilirsin~"
    "Sayori bunu sessizce kulağıma söylüyor, sonra diğer kızlara dönüyor."
    s 1x "Her neyse! Bu Natsuki, her zaman enerji dolu."
    s "Ve bu da Yuri, kulübün en akıllısı!"
    $ y_name = 'Yuri'
    show sayori at t31 zorder 2
    show yuri at f33 zorder 3
    y 4b "Böyle şeyler söyleme..."
    "Nispeten daha olgun ve çekingen görünen Yuri, Sayori ve Natsuki gibi insanlara ayak uydurmakta zorlanıyor gibi görünüyor."
    show yuri at t33 zorder 2
    mc "Ah... İkinizle de tanıştığıma memnun oldum."
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    hide yuri
    hide natsuki
    show sayori at f31 zorder 3
    s 1a "Ve Monika'yı zaten tanıyormuşsunuz gibi görünüyor, doğru mu?"
    $ m_name = 'Monika'
    show sayori at t31 zorder 2
    show monika 2a at f32 zorder 3
    m "Bu doğru."
    m "Seni tekrar görmek çok güzel, [player]."
    show monika 5a at hop
    "Monika tatlı tatlı gülümser."
    "Birbirimizi tanıyoruz - nadiren konuşurduk ama geçen yıl aynı sınıftaydık."
    "Monika muhtemelen sınıftaki en popüler kızdı - zeki, güzel, atletik."
    "Kısacası, tamamen benim ligimin dışında."
    "O yüzden bana içtenlikle gülümsemesi biraz..."
    mc "S-sende, Monika."
    show monika at thide zorder 1
    hide monika
    show sayori at f31 zorder 3
    s 4x "Gel otur, [player]! Masada senin için yer açtık, böylece benim ya da Monika'nın yanına oturabilirsin."
    s "Ben kekleri getireyim.~"
    show sayori at t31 zorder 2
    show natsuki 1e at f32 zorder 3
    n "Hey! Onları ben yaptım, ben alırım.!"
    show natsuki at t32 zorder 2
    show sayori at f31 zorder 3
    s 5a "Özür dilerim, biraz fazla heyecanlandım~"
    show sayori at t31 zorder 2
    show yuri 1a at f33 zorder 3
    y "O zaman ben de biraz çay yapayım.?"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "Kızlar, masaya dönüştürülmüş birkaç sırayı düzenlemişler."
    "Sayori'nin bahsettiği gibi, Monika'nın yanında bir yer ve Sayori'nin yanında bir yer olacak şekilde genişletilmiş."
    "Natsuki ve Yuri, odanın köşesine doğru yürüyüp, Natsuki sarılı bir tepsi alırken Yuri dolabı açıyor."
    "Hâlâ tuhaf hissederek, Sayori'nin yanına oturuyorum."
    "Natsuki, elinde tepsiyle gururla masaya geri yürüyor."
    show natsuki 2z at t32 zorder 2
    n "Eveet, hazır mısınız?"
    n "...Ta-daa!"
    show sayori 4m at t31 zorder 2
    show monika 2d at t33 zorder 2
    s "Uwooooah!"
    "Natsuki tepsinin üzerindeki folyoyu kaldırarak küçük kediler gibi süslenmiş bir düzine beyaz, kabarık keki ortaya çıkarıyor."
    "Bıyıklar krema ile çizildi ve kulakları yapmak için küçük çikolata parçaları kullanıldı."
    show sayori at f31 zorder 3
    s 4r "Çoooooook tatlı~!"
    show sayori at t31 zorder 2
    show monika at f33 zorder 3
    m 2b "Pişirme konusunda bu kadar iyi olduğunu bilmiyordum, Natsuki!"
    show monika at t33 zorder 2
    show natsuki at f32 zorder 3
    n 2d "Ehehe. Tabi, bilirsin."
    n "Acele edin ve bir tane alın!"
    "Önce Sayori bir tane kapıyor, sonra Monika. Ben de takip ediyorum."
    show natsuki at t32 zorder 2
    show sayori at f31 zorder 3
    s 4q "Bu çok lezzetli!"
    "Sayori ağzı doluyken konuşuyor ve şimdiden yüzüne krema bulaştırmayı başardı."
    "Keki parmaklarımın arasında çeviriyor, ısırmak için en iyi açıyı arıyorum."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    hide sayori
    hide monika
    show natsuki 1c at t32 zorder 2
    "Natsuki sessiz."
    "Bana doğru sinsi bakışlarını fark etmekten kendimi alamıyorum.."
    "Acaba bir ısırık almam için bekliyor mu??"
    "Sonunda ısırdım."
    "Krema tatlı ve lezzet dolu - acaba kendisi mi yaptı?."
    mc "Bu gerçekten çok iyi.."
    mc "Teşekkür ederim, Natsuki."
    n 5h "N-neden bana teşekkür ediyorsun? Ben öyle değilim..!"
    "{i}(Bunu daha önce bir yerde duymamış mıydım...?){/i}"
    show natsuki at s32
    n 5s "...Senin için falan yapmadım."
    mc "Ne? Teknik olarak yaptığını sanıyordum. Sayori dedi ki--"
    show natsuki at t32 zorder 2
    n 12c "Şey, belki!"
    n "Ama değil, b-bilirsin, {i}sen!{/i} Aptal..."
    mc "Tamam, tamam..."
    show natsuki at thide zorder 1
    hide natsuki
    "Natsuki'nin tuhaf mantığından vazgeçiyorum ve konuşmayı kapatıyorum."
    "Yuri elinde bir çay setiyle masaya döner."
    "Çaydanlığı kek tepsisinin yanına koymadan önce her birimizin önüne dikkatlice birer çay fincanı yerleştiriyor."
    show yuri 1a at t21 zorder 2
    mc "Bütün bir çay setini bu sınıfta mı tutuyorsun?"
    y "Merak etme, öğretmenler bize izin verdi.."
    y "Sonuçta, sıcak bir fincan çay iyi bir kitabın tadını çıkarmamıza yardımcı olmaz mı??"
    mc "Ah... Sanırım..."
    show monika 4a at t22 zorder 2
    m "Ehehe, gözünün korkmasına izin verme, Yuri sadece seni etkilemeye çalışıyor."
    show yuri at h21
    y 3n "Eh?! Bu değil..."
    "Hakarete uğrayan Yuri gözlerini kaçırır."
    y 4b "Bunu kastetmemiştim, biliyorsun..."
    mc "Sana inanıyorum."
    mc "Çay ve kitap okumak benim için bir eğlence olmayabilir ama en azından çaydan keyif alıyorum."
    y 2u "Sevindim..."
    "Yuri rahatlamış bir şekilde kendi kendine gülümser."
    "Monika bir kaşını kaldırıyor, sonra bana gülümsüyor."
    show yuri at thide zorder 1
    hide yuri
    show monika at t11 zorder 2
    m 1 "Peki, Edebiyat Kulübü'nü düşünmene ne sebep oldu?"
    mc "Um..."
    "Bu sorudan korkuyordum."
    "İçimden bir ses Monika'ya Sayori tarafından buraya sürüklendiğimi söylememem gerektiğini söylüyor."
    mc "Henüz hiçbir kulübe katılmadım ve Sayori burada çok mutlu görünüyordu..."
    m 1j "Sorun değil! Utanma!"
    m 1b "Kendini evinde hissetmeni sağlayacağız, tamam mı??"
    m "Edebiyat Kulübü'nün başkanı olarak görevim, kulübü herkes için eğlenceli ve heyecan verici hale getirmektir!"
    show monika 1a
    mc "Monika, şaşırdım."
    mc "Nasıl oldu da kendi kulübünü kurmaya karar verdin?"
    mc "Muhtemelen büyük kulüplerden herhangi birinin yönetim kurulu üyesi olabilirsiniz."
    mc "Sen geçen sene münazara kulübünün lideri değil miydin?"
    m 5 "Ahaha, bilirsin işte..."
    m "Dürüst olmak gerekirse, büyük kulüplerin etrafındaki tüm politikalara katlanamıyorum."
    m "Bütçe, tanıtım ve etkinliklere nasıl hazırlanılacağı hakkında tartışmaktan başka bir şey yokmuş gibi geliyor..."
    m "Kişisel olarak keyif aldığım bir şeyi alıp ondan özel bir şey yapmayı tercih ederim."
    m 1b "Ve eğer başkalarını edebiyatla ilgilenmeye teşvik ederse, o zaman bu hayalimi gerçekleştirmiş olurum!"
    show monika 1a
    show sayori 3q at t31 zorder 2
    s "Monika gerçekten harika bir lider!"
    show yuri 1 at t33 zorder 2
    "Yuri de başını sallıyarak onaylıyor."
    show sayori at thide zorder 1
    show yuri at thide zorder 1
    hide sayori
    hide yuri
    mc "O zaman kulüpte daha fazla insan olmamasına şaşırdım.."
    mc "Yeni bir kulüp kurmak zor olsa gerek."
    m 3b "Şöyle de diyebilirsin."
    m "Pek çok insan yepyeni bir şeye başlamak için onca çaba sarf etmekle ilgilenmez..."
    m "Özellikle de edebiyat gibi ilginizi çekmeyen bir şey olduğunda."
    m "İnsanları hem eğlenceli hem de değerli olduğunuza ikna etmek için çok çalışmalısın."
    m "Ancak bu durum, festival gibi okul etkinliklerini çok daha önemli kılıyor."
    m 2k "Mezun olmadan önce hepimizin bu kulübü gerçekten büyütebileceğimize inanıyorum!"
    m "Değil mi, millet?"
    show monika 2a at t22 zorder 2
    show sayori 4r at t21 zorder 2
    s "Evet!"
    show monika at t33 zorder 2
    show sayori at t32 zorder 2
    show yuri 1a at t31 zorder 2
    y "Elimizden geleni yapıcağız."
    show monika at t44 zorder 2
    show sayori at t43 zorder 2
    show yuri at t42 zorder 2
    show natsuki 4d at t41 zorder 2
    n "Bunu biliyorsun!"
    "Herkes coşkuyla kabul ediyor."
    "Çok farklı kızlar, hepsi aynı hedefle ilgileniyor..."
    "Monika bu üçünü bulmak için gerçekten çok çalışmış olmalı."
    "Belki de bu yüzden hepsi yeni bir üyenin katılması fikrinden bu kadar memnun oldular."
    "Yine de onların edebiyat konusundaki heyecanlarına ayak uydurabilir miyim bilmiyorum..."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    show natsuki at thide zorder 1
    show yuri at t32 zorder 2
    hide sayori
    hide monika
    hide natsuki
    y "Şey, [player], ne tür şeyler okumaktan hoşlanırsınız?"
    mc "Yanii... Ah..."
    "Son birkaç yıldır ne kadar az okuduğumu düşünürsek, buna cevap vermenin iyi bir yolu yok."
    mc "...Manga..."
    "Kendi kendime sessizce mırıldanıyorum, yarı şaka."
    show natsuki 1c at t41 zorder 2
    "Natsuki'nin kafası aniden canlanır.."
    "Bir şey söylemek ister gibi görünüyor ama sessizliğini koruyor."
    show natsuki at thide zorder 1
    hide natsuki
    y 3u "Pek okuyucu değilsin sanırım...."
    mc "...Şey, bu değişebilir..."
    "Ne diyorum ben?"
    "Yuri'nin hüzünlü gülümsemesini gördükten sonra düşünmeden konuştum."
    mc "Her neyse, ya sen, Yuri?"
    y 1l "Pekala, bir bakalım..."
    "Yuri parmağıyla çay fincanının kenarının izini sürüyor."
    y 1a "Benim favorilerim genellikle derin ve karmaşık fantastik dünyalar inşa eden romanlardır."
    y "Arkalarındaki yaratıcılık ve işçilik seviyesi benim için şaşırtıcı."
    y 1f "Ve böyle yabancı bir dünyada iyi bir hikaye anlatmak da aynı derecede etkileyici."
    "Yuri devam ediyor, okuması konusunda açıkça tutkulu."
    "İçeri girdiğim andan beri çok çekingen ve çekingen görünüyordu, ama gözlerinin aydınlanma şekliyle tesellisini insanların değil kitapların dünyasında bulduğu açık."
    y 2m "Ama biliyorsun, birçok şeyi severim."
    y "Derin psikolojik unsurları olan hikayeler genellikle beni de içine çeker."
    y 2a "Bir yazarın sizi tamamen bir döngüye sokmak için kendi hayal gücünüz eksikliğinden bu kadar kasıtlı olarak yararlanabilmesi şaşırtıcı değil mi?"
    y "Her neyse, son zamanlarda çok fazla korku okuyorum..."
    mc "ha, Bir keresinde bir korku kitabı okumuştum..."
    "En az düzeyde ilişki kurabileceğim bir şeyi umutsuzca kavrıyorum."
    "Bu hızla devam ederse, Yuri neredeyse bir taşla konuşuyor gibi olacak."
    show monika 1d at f33 zorder 3
    m "Gerçekten mi? Bunu beklemezdim, Yuri."
    m "Senin kadar nazik biri için..."
    show monika at t33 zorder 2
    show yuri at f32 zorder 3
    y 1a "Sanırım öyle diyebiliriz.."
    y "Ama eğer bir hikaye beni düşündürüyorsa veya beni başka bir dünyaya götürüyorsa, o zaman gerçekten onu bırakamam."
    y "Gerçeküstü korku genellikle dünyaya bakışınızı değiştirmekte çok başarılı olabilir, en azından kısa bir süre için bile olsa."
    show yuri at t32 zorder 2
    show natsuki 5q at f31 zorder 3
    n "ha, korkudan hoşlanmıyorum..."
    show natsuki at t31 zorder 2
    show yuri at f32 zorder 3
    y 1f "Ha? Neden böyle düşünüyorsun?"
    show yuri at t32 zorder 2
    show natsuki at f31 zorder 3
    n 5c "Eh, ben sadece..."
    "Natsuki'nin gözleri bir an için bana doğru kayar."
    n 5q "Boşver..."
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 1a "Evet, genellikle sevimli şeyler hakkında yazmayı severdin, değil mi, Natsuki?"
    show monika at t33 zorder 2
    show natsuki 1o at f31 zorder 3
    n "N-Ne?"
    n "Bu fikri sana ne verdi?"
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 3b "Geçenlerde kulüp toplantısında bir parça kağıt unutmuştun."
    m "Bir şiir üzerinde çalışıyormuş gibi görünüyor, adı-"
    show monika at t33 zorder 2
    show natsuki 1p at f31 zorder 3
    n "Sesli söyleme!!"
    n "Ve onu geri ver!"
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 1j "Tamam, tamam~"
    show monika at thide zorder 1
    show yuri at thide zorder 1
    hide monika
    hide yuri
    show natsuki 1r at t42 zorder 2
    show sayori 4q at l41 behind natsuki
    s "Ehehe, kapkeklerin, şiirlerin..."
    s "Yaptığın her şey senin kadar sevimli~"
    show sayori at t21 behind natsuki
    "Sayori, Natsuki'nin arkasına yaklaşır ve omuzlarına ellerini koyar."
    show natsuki at h42
    n 1v "{i}Igh! Ben sevimli değilim!!{/i}"
    show natsuki at t11 zorder 2
    show sayori at thide zorder 1
    hide sayori
    mc "Natsuki, kendi şiirlerini mi yazıyorsun?"
    n 1c "Eh? Hm, sanırım bazen."
    n "Neden önemsiyorsun ki?"
    mc "Bence bu etkileyici."
    mc "Neden onları zaman zaman paylaşmıyorsun?"
    n 5q "Ha-Hayır!"
    "Natsuki gözlerini kaçırıyor."
    n "Onları... beğenmezsin..."
    mc "Ah... henüz kendinden emin bir yazar değil misin?"
    show yuri 2f at t31 zorder 2
    y "Natsuki'nin hissettiğini anlıyorum."
    y "O seviyede yazıyı paylaşmak sadece özgüvenle olmuyor."
    y 2k "Yazmanın en gerçek şekli, kendimize yazmaktır."
    y "Okuyuculara açılmaya, kırılganlıklarınızı ortaya koymaya ve kalbinizin en derin noktalarını dahi göstermeye istekli olmalısınız."
    show natsuki at thide zorder 1
    hide natsuki
    show monika 2a at t33 zorder 2
    m "Senin de yazma deneyimin var mı, Yuri?"
    m "Belki de birkaç eserini paylaşırsan, örnek olabilir ve Natsuki'nin de kendi eserlerini paylaşmaya cesaret etmesine yardımcı olabilirsin."
    show yuri at s31
    y 3o "..."
    mc "Sanırım Yuri için de aynı şey geçerli..."
    show sayori 2g at t32 zorder 2
    s "Ah... Herkesin şiirlerini okumak istiyordum..."
    show sayori at thide zorder 1
    show yuri at thide zorder 1
    show monika at thide zorder 1
    hide sayori
    hide yuri
    hide monika
    "Bir an için hepimiz sessizce otururuz.?"
    show monika 5a at f32 zorder 3
    m "Pekii!"
    m "Bir fikrim var, millet~"
    show yuri 3e at t31 zorder 2
    show natsuki 2k at t33 zorder 2
    ny "...?"
    "Natsuki ve Yuri, merakla Monika'ya bakar."
    m 2b "Hadi hepimiz eve gidip kendi şiirimizi yazalım!"
    m "Sonra bir dahaki buluşmamızda hepsini birbirimizle paylaşırız."
    m "Bu şekilde, hepimiz için eşit olur!"
    show monika 2a at t32 zorder 2
    show natsuki at f33 zorder 3
    n 5q "U-Um..."
    show natsuki at t33 zorder 2
    show yuri 3v at f31 zorder 3
    y "..."
    show natsuki at t44 zorder 2
    show monika at t43 zorder 2
    show yuri at t42 zorder 2
    show sayori 4r at l41
    s "Eveeet! Hadi yapalım!"
    show monika at f43 zorder 3
    m 1a "Üstelik, yeni bir üyemiz olduğuna göre, sanırım hepimizin birbirine biraz daha alışmasına ve kulübün bağlarını güçlendirmesine yardımcı olacak."
    m "Öyle değil mi, [player]?"
    show monika at t43 zorder 2
    "Monika bir kez daha sıcak bir şekilde bana gülümser."
    mc "Bir dakika... hâlâ bir sorun var."
    show monika at f43 zorder 3
    m 1d "Eh? O nedir??"
    "Kulübe katılmamızın asıl konusuna geri döndüğümüze göre, tüm bu süre boyunca aklımda olanı açıkça ifade ederim."
    show monika at t43 zorder 2
    mc "Ben hiç bu kulübe katılacağımı söylemedim!"
    mc "Sayori belki beni uğramaya ikna etmiş olabilir, ama hiçbir karar vermedim."
    mc "Hâlâ bakacağım başka kulüpler var ve... eh..."
    show monika 1g
    show sayori 1g
    show natsuki 4g
    show yuri 2e
    "Düşüncelerim dağılıyor."
    "Dört kız da üzgün gözlerle bana bakıyor."
    show monika at s43
    m 1p "A-Ama..."
    show yuri at s42
    y 2v "Üzgünüm... Düşündüm ki..."
    show natsuki at s44
    n 5s "Hmph."
    show sayori at s41
    s 1k "[player]..."
    mc "H-Hepiniz..."
    "Ben... Ben bu kızlara karşı savunmasızım."
    "Bu durumdayken nasıl net bir karar vereceğim?"
    "Eğer bu güzel kızlarla her gün geçirmek için ödemen gereken bedel şiir yazmaksa..."
    mc "...Pekala."
    mc "Tamam, kararımı verdim o zaman."
    mc "Edebiyat Kulübü'ne katılacağım."
    show monika 1e at t43 zorder 2
    show yuri 3f at t42 zorder 2
    show natsuki 1k at t44 zorder 2
    show sayori 4b at t41 zorder 2
    "Kızların gözleri tek tek parlar."
    show sayori at h41
    s 4r "Evet! Çok mutluyummm~"
    "Sayori kollarını etrafıma dolayıp zıplamaya başlar."
    mc "H-Hey--"
    show yuri at f42 zorder 3
    y 1m "Beni gerçekten bir an korkuttun..."
    show yuri at t42 zorder 2
    show natsuki at f44 zorder 3
    n 5q "Eğer gerçekten sadece cupcake'ler için geldiysen, çok sinirlenirdim."
    show natsuki at t44 zorder 2
    show monika at f43 zorder 3
    m 5 "O zaman bu işi resmileştiriyoruz!"
    m "Edebiyat Kulübü'ne hoş geldin!"
    show monika at t43 zorder 2
    mc "Ah... teşekkürler, sanırım."
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    show sayori at thide zorder 1
    show monika at t11 zorder 2
    hide yuri
    hide natsuki
    hide sayori
    m 3b "Pekala, millet!"
    m "Sanırım bu şekilde, bugünkü toplantıyı iyi bir notla resmen sonlandırabiliriz."
    m "Herkes bu akşamın ödevini hatırlasın:"
    m "Bir sonraki toplantıya getirmek için bir şiir yazın, böylece hepsini paylaşabiliriz!"
    "Monika bir kez daha bana bakar."
    m 1a "[player], Nasıl ifade edeceğini merakla bekliyorum."
    show monika 5 at hop
    m "Ehehe~"
    mc "E-Evet..."
    show monika at thide zorder 1
    hide monika
    "Monika gibi sınıfın yıldızını vasat yazma yeteneklerimle gerçekten etkileyebilir miyim?"
    "İçimdeki kaygının arttığını şimdiden hissediyorum."
    "Bu arada, kızlar sohbetlerine devam ederken, Yuri ve Natsuki yemeklerini temizler."
    show sayori 1a at t11 zorder 2
    s "Hey, [player], Zaten buradayken, birlikte eve yürümek ister misin?"
    "Doğru - Sayori ve ben artık birlikte eve yürümüyoruz çünkü o her zaman okul sonrası kulüplerde kalırdı."
    mc "Tabii ki, neden olmasın."
    s 4q "Yeeyy!~"

    scene bg residential_day
    with wipeleft_scene

    "Bu şekilde, ikimiz de kulüp odasından ayrılıp eve doğru yol alırız."
    "Tüm yol boyunca, aklım dört kız arasında gidip gelir:"
    show sayori 1 at t41 zorder 2
    "Sayori,"
    show natsuki 4 at t42 zorder 2
    "Natsuki,"
    show yuri 1 at t43 zorder 2
    "Yuri,"
    show monika 1 at t44 zorder 2
    "ve tabii ki, Monika."
    "Her gün okuldan sonra edebiyat kulübünde mi geçireceğim mutlu olacak mıyım?"
    "Belki de bu kızlardan biriyle daha yakınlaşma şansım olur..."
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "Tamamdır!"
    "Koşullarımın sunduğu imkanları en iyi şekilde değerlendirmem gerekecek ve eminim ki iyi şans beni bulacak."
    "Ve sanırım bu gece bir şiir yazmakla başlıyor..."

    return