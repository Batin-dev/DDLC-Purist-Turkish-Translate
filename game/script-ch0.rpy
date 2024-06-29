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
    s "Mutluluğunuz benim için gerçekten önemli, biliyorsun!"
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
    s 5d "Eeeehhhhh?! Kaba!"
    "Sayori Edebiyat Kulübü'nün başkan yardımcısı."
    "Ama onun edebiyata ilgisi olduğunu hiç bilmiyordum."
    "Aslında, %99 eminim ki yeni bir kulübün başlatmak eğlenceli olacağını düşündüğü için yaptı."
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
    m 1 "So, what made you consider the Literature Club?"
    mc "Um..."
    "I was afraid of this question."
    "Something tells me I shouldn't tell Monika that I was practically dragged here by Sayori."
    mc "Well, I haven't joined any clubs yet, and Sayori seemed really happy here, so..."
    m 1j "That's okay! Don't be embarrassed!"
    m 1b "We'll make sure you feel right at home, okay?"
    m "As president of the Literature Club, it's my duty to make the club fun and exciting for everyone!"
    show monika 1a
    mc "Monika, I'm surprised."
    mc "How come you decided to start your own club?"
    mc "You could probably be a board member for any of the major clubs."
    mc "Weren't you a leader of the debate club last year?"
    m 5 "Ahaha, well, you know..."
    m "To be honest, I can't stand all of the politics around the major clubs."
    m "It feels like nothing but arguing about the budget and publicity and how to prepare for events..."
    m "I'd much rather take something I personally enjoy and make something special out of it."
    m 1b "And if it encourages others to get into literature, then I'm fulfilling that dream!"
    show monika 1a
    show sayori 3q at t31 zorder 2
    s "Monika really is a great leader!"
    show yuri 1 at t33 zorder 2
    "Yuri also nods in agreement."
    show sayori at thide zorder 1
    show yuri at thide zorder 1
    hide sayori
    hide yuri
    mc "Then I'm surprised there aren't more people in the club yet."
    mc "It must be hard to start a new club."
    m 3b "You could put it that way."
    m "Not many people are very interested in putting out all the effort to start something brand new..."
    m "Especially when it's something that doesn't grab your attention, like literature."
    m "You have to work hard to convince people that you're both fun and worthwhile."
    m "But it makes school events, like the festival, that much more important."
    m 2k "I'm confident that we can all really grow this club before we graduate!"
    m "Right, everyone?"
    show monika 2a at t22 zorder 2
    show sayori 4r at t21 zorder 2
    s "Yeah!"
    show monika at t33 zorder 2
    show sayori at t32 zorder 2
    show yuri 1a at t31 zorder 2
    y "We'll do our best."
    show monika at t44 zorder 2
    show sayori at t43 zorder 2
    show yuri at t42 zorder 2
    show natsuki 4d at t41 zorder 2
    n "You know it!"
    "Everyone enthusiastically agrees."
    "Such different girls, all interested in the same goal..."
    "Monika must have worked really hard just to find these three."
    "Maybe that's why they were all so delighted by the idea of a new member joining."
    "Though I still don't really know if I can keep up with their level of enthusiasm about literature..."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    show natsuki at thide zorder 1
    show yuri at t32 zorder 2
    hide sayori
    hide monika
    hide natsuki
    y "So, [player], what kinds of things do you like to read?"
    mc "Well... Ah..."
    "Considering how little I've read these past few years, I don't really have a good way of answering that."
    mc "...Manga..."
    "I mutter quietly to myself, half-joking."
    show natsuki 1c at t41 zorder 2
    "Natsuki's head suddenly perks up."
    "It looks like she wants to say something, but she keeps quiet."
    show natsuki at thide zorder 1
    hide natsuki
    y 3u "N-Not much of a reader, I guess..."
    mc "...Well, that can change..."
    "What am I saying?"
    "I spoke without thinking after seeing Yuri's sad smile."
    mc "Anyway, what about you, Yuri?"
    y 1l "Well, let's see..."
    "Yuri traces the rim of her teacup with her finger."
    y 1a "My favorites are usually novels that build deep and complex fantasy worlds."
    y "The level of creativity and craftsmanship behind them is amazing to me."
    y 1f "And telling a good story in such a foreign world is equally impressive."
    "Yuri goes on, clearly passionate about her reading."
    "She seemed so reserved and timid since the moment I walked in, but it's obvious by the way her eyes light up that she finds her comfort in the world of books, not people."
    y 2m "But you know, I like a lot of things."
    y "Stories with deep psychological elements usually immerse me as well."
    y 2a "Isn't it amazing how a writer can so deliberately take advantage of your own lack of imagination to completely throw you for a loop?"
    y "Anyway, I've been reading a lot of horror lately..."
    mc "Ah, I read a horror book once..."
    "I desperately grasp something I can relate to at the minimal level."
    "At this rate, Yuri might as well be having a conversation with a rock."
    show monika 1d at f33 zorder 3
    m "Really? I wouldn't have expected that, Yuri."
    m "For someone as gentle as you..."
    show monika at t33 zorder 2
    show yuri at f32 zorder 3
    y 1a "I guess you could say that."
    y "But if a story makes me think, or takes me to another world, then I really can't put it down."
    y "Surreal horror is often very successful at changing the way you look at the world, if only for a brief moment."
    show yuri at t32 zorder 2
    show natsuki 5q at f31 zorder 3
    n "Ugh, I hate horror..."
    show natsuki at t31 zorder 2
    show yuri at f32 zorder 3
    y 1f "Oh? Why's that?"
    show yuri at t32 zorder 2
    show natsuki at f31 zorder 3
    n 5c "Well, I just..."
    "Natsuki's eyes dart over to me for a split second."
    n 5q "Never mind."
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 1a "That's right, you usually like to write about cute things, don't you, Natsuki?"
    show monika at t33 zorder 2
    show natsuki 1o at f31 zorder 3
    n "W-What?"
    n "What gives you that idea?"
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 3b "You left a piece of scrap paper behind last club meeting."
    m "It looked like you were working on a poem called--"
    show monika at t33 zorder 2
    show natsuki 1p at f31 zorder 3
    n "Don't say it out loud!!"
    n "And give that back!"
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 1j "Fine, fine~"
    show monika at thide zorder 1
    show yuri at thide zorder 1
    hide monika
    hide yuri
    show natsuki 1r at t42 zorder 2
    show sayori 4q at l41 behind natsuki
    s "Ehehe, your cupcakes, your poems..."
    s "Everything you do is just as cute as you are~"
    show sayori at t21 behind natsuki
    "Sayori sidles up behind Natsuki and puts her hands on her shoulders."
    show natsuki at h42
    n 1v "{i}I'm not cute!!{/i}"
    show natsuki at t11 zorder 2
    show sayori at thide zorder 1
    hide sayori
    mc "Natsuki, you write your own poems?"
    n 1c "Eh? Well, I guess sometimes."
    n "Why do you care?"
    mc "I think that's impressive."
    mc "Why don't you share them sometime?"
    n 5q "N-No!"
    "Natsuki averts her eyes."
    n "You wouldn't...like them..."
    mc "Ah...not a very confident writer yet?"
    show yuri 2f at t31 zorder 2
    y "I understand how Natsuki feels."
    y "Sharing that level of writing takes more than just confidence."
    y 2k "The truest form of writing is writing to oneself."
    y "You must be willing to open up to your readers, exposing your vulnerabilities and showing even the deepest reaches of your heart."
    show natsuki at thide zorder 1
    hide natsuki
    show monika 2a at t33 zorder 2
    m "Do you have writing experience too, Yuri?"
    m "Maybe if you share some of your work, you can set an example and help Natsuki feel comfortable enough to share hers."
    show yuri at s31
    y 3o "..."
    mc "I guess it's the same for Yuri..."
    show sayori 2g at t32 zorder 2
    s "Aww... I wanted to read everyone's poems..."
    show sayori at thide zorder 1
    show yuri at thide zorder 1
    show monika at thide zorder 1
    hide sayori
    hide yuri
    hide monika
    "We all sit in silence for a moment."
    show monika 5a at f32 zorder 3
    m "Okay!"
    m "I have an idea, everyone~"
    show yuri 3e at t31 zorder 2
    show natsuki 2k at t33 zorder 2
    ny "...?"
    "Natsuki and Yuri look quizzically at Monika."
    m 2b "Let's all go home and write a poem of our own!"
    m "Then, next time we meet, we'll all share them with each other."
    m "That way, everyone is even!"
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
    s "Yeaaah! Let's do it!"
    show monika at f43 zorder 3
    m 1a "Plus, now that we have a new member, I think it will help us all get a little more comfortable with each other, and strengthen the bond of the club."
    m "Isn't that right, [player]?"
    show monika at t43 zorder 2
    "Monika smiles warmly at me once again."
    mc "Hold on...there's still one problem."
    show monika at f43 zorder 3
    m 1d "Eh? What's that?"
    "Now that we're back to the original topic of me joining the club, I bluntly come forth with what's been on my mind the entire time."
    show monika at t43 zorder 2
    mc "I never said I would join this club!"
    mc "Sayori may have convinced me to stop by, but I never made any decision."
    mc "I still have other clubs to look at, and...um..."
    show monika 1g
    show sayori 1g
    show natsuki 4g
    show yuri 2e
    "I lose my train of thought."
    "All four girls stare back at me with dejected eyes."
    show monika at s43
    m 1p "B-But..."
    show yuri at s42
    y 2v "I'm sorry, I thought..."
    show natsuki at s44
    n 5s "Hmph."
    show sayori at s41
    s 1k "[player]..."
    mc "Y-You all..."
    "I...I'm defenseless against these girls."
    "How am I supposed to make a clear-headed decision when it's like this?"
    "That is, if writing poems is the price I need to pay in order to spend every day with these beautiful girls..."
    mc "...Right."
    mc "Okay, I've decided, then."
    mc "I'll join the Literature Club."
    show monika 1e at t43 zorder 2
    show yuri 3f at t42 zorder 2
    show natsuki 1k at t44 zorder 2
    show sayori 4b at t41 zorder 2
    "One by one, the girls' eyes light up."
    show sayori at h41
    s 4r "Yesss! I'm so happyyy~"
    "Sayori wraps her arms around me, jumping up and down."
    mc "H-Hey--"
    show yuri at f42 zorder 3
    y 1m "You really did scare me for a moment..."
    show yuri at t42 zorder 2
    show natsuki at f44 zorder 3
    n 5q "If you really just came for the cupcakes, I would be super pissed."
    show natsuki at t44 zorder 2
    show monika at f43 zorder 3
    m 5 "Then that makes it official!"
    m "Welcome to the Literature Club!"
    show monika at t43 zorder 2
    mc "Ah...thanks, I guess."
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    show sayori at thide zorder 1
    show monika at t11 zorder 2
    hide yuri
    hide natsuki
    hide sayori
    m 3b "Okay, everyone!"
    m "I think with that, we can officially end today's meeting on a good note."
    m "Everyone remember tonight's assignment:"
    m "Write a poem to bring to the next meeting, so we can all share!"
    "Monika looks over at me once more."
    m 1a "[player], I look forward to seeing how you express yourself."
    show monika 5 at hop
    m "Ehehe~"
    mc "Y-Yeah..."
    show monika at thide zorder 1
    hide monika
    "Can I really impress the class star Monika with my mediocre writing skills?"
    "I already feel the anxiety welling up inside me."
    "Meanwhile, the girls continue to chit-chat as Yuri and Natsuki clean up their food."
    show sayori 1a at t11 zorder 2
    s "Hey, [player], since we're already here, do you want to walk home together?"
    "That's right - Sayori and I never walk home together anymore because she always stayed after school for clubs."
    mc "Sure, might as well."
    s 4q "Yaay~"

    scene bg residential_day
    with wipeleft_scene

    "With that, the two of us depart the clubroom and make our way home."
    "The whole way, my mind wanders back and forth between the four girls:"
    show sayori 1 at t41 zorder 2
    "Sayori,"
    show natsuki 4 at t42 zorder 2
    "Natsuki,"
    show yuri 1 at t43 zorder 2
    "Yuri,"
    show monika 1 at t44 zorder 2
    "and, of course, Monika."
    "Will I really be happy spending every day after school in a literature club?"
    "Perhaps I'll have the chance to grow closer to one of these girls..."
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "Alright!"
    "I'll just need to make the most of my circumstances, and I'm sure good fortune will find me."
    "And I guess that starts with writing a poem tonight..."

    return