label MonikaInterlude_NatsukiGoodEnd:
    $ saveLocked = True
    play music m1 fadein 5.0
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    with Dissolve(3.0, alpha=True)
    $ persistent.natsukiCompletedGood = True
    window show
    if(persistent.natsukiRouteCompletions==1):
            m "Belki de Edebiyat Kulübü'nde birini mutlu ettiğini kabul etmeni mi bekliyorsun?"
    m "Hala sadece birini mutlu ettin."
    m "Ama, bu sürmez."
    m "Sen ve ben çok iyi biliyoruz ki, bu sadece bir mod."
    show m_thoughtful with dissolve_cg
    m "Başka, ne söyleyebilirim ki?"
    m "Natsuki'yi 'kurtardın', değil mi? O normal bir ev hayatına doğru iyileşiyor ve birbirinize olan sevdanızı defalarca itiraf ettiniz."
    m "Ama belki de bir şeylerin eksik olduğunu hissettin."
    show m_smug with dissolve_cg
    m "Haha, kavga etmeyi mi düşünmüştün?"
    m "Kendi ellerinle adalet mi sağlamak istedin?"
    m "E, işte biraz talihsizlik, eğer böyle bir şey arıyorsan."
    show m_neutral2 with dissolve_cg
    m "Ama sanmıyorum ki Natsuki bunu takdir ederdi."
    m "Benim söyleyebileceğim başka bir şey var mı?"
    elif(persistent.natsukiRouteCompletions == 2):
        show m_thoughtful with dissolve_cg
        m "Yine Natsuki, ha?"
        m "Peki, umarım sadece sevdiğin kısımlara atlamamışsındır."
        m "Bu oldukça acımasız olurdu, değil mi?"
        m "Sadece mutlu kısımlara gitmek."
        m "Onunla her adımda yanında olmadan."
        m "Ama herhalde bir kez orada oldun."
    else:
        m "Gerçekten Natsuki'yi seviyorsun, değil mi?"
        m "Sonuçta, bu üçüncü kez onun yolunu yapıyorsun."
        m "Hmmm..."
    if persistent.sayoriCompletedGood is False and persistent.yuriCompletedGood is False:
        m "Diğerlerini de bitirmelisin, değil mi?"
        m "Yoksa sadece Natsuki için mi buradasın?"
        if(persistent.natsukiRouteCompletions == 1):
            m "Belki de durum budur, çünkü diğerlerine bile yönelmedin."
        elif(persistent.natsukiRouteCompletions > 1):
            m "Belki de durum budur, çünkü şu ana kadar sadece onun yolunu tekrar ettin."

    if persistent.sayoriCompletedGood is True and persistent.yuriCompletedGood is True:
        call MonikaRouteOpening
        return

    m "Ama en sonunda pek de bir anlamı yok."
    m "Beni seni mutlu olmana engel olmasına izin verme."
    m "Ne istersen onu yap."
    window hide
    $ saveLocked = False
    stop music fadeout 5.0
    hide monika_bg_highlight #with Dissolve(2.0, alpha=True)
    hide monika_bg #with Dissolve(1.5, alpha=True)
    hide mask_3 #with Dissolve(1.0, alpha=True)
    hide mask_2
    with Dissolve(1.0, alpha=True)
    return


label MonikaInterlude_NatsukiBadEnd:
    $ saveLocked = True
    #pause(5.0)
    play music m1 fadein 5.0
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    with Dissolve(5.0, alpha=True)
    window show
    show m_unhappy2 with dissolve_cg
    m "..."
    m "Hmm."
    m "Gerçekten ona bunu söyleyeceğini düşünmemiştim."
    show m_neutral1 with dissolve_cg
    m "Sanırım seni bir sürprizle karşılaştıramam."
    m "Ama geri dönüp her şeyi düzeltemezsin diye bir şey yok."
    m "Bunun gücüne sahipsin, değil mi?"
    if persistent.sayoriCompletedGood is False and persistent.yuriCompletedGood is False:
        show m_thoughtful with dissolve_cg
        m "Bence kolayca moralin bozulmaz."
        m "Onları mutlu etmek için yola çıktın, bu yüzden burada durmayacağını düşünüyorum."
        m "Bence Natsuki'yi gerçekten mutlu etmek için her şeyi sonuna kadar götürürsün."
        m "Bunun için sadece bir 'oyun kaydet' meselesi."
        m "Beni engellemene gerek yok."
    elif (persistent.sayoriCompletedGood is False and persistent.yuriCompletedGood is True) or (persistent.sayoriCompletedGood is True and persistent.yuriCompletedGood is False) and not (persistent.sayoriCompletedGood is True and persistent.yuriCompletedGood is True):
        show m_neutral2 with dissolve_cg
        m "Zaten birini mutlu ettin, bu yüzden başkasında hata yapman yüzünden pes etmeyeceğini sanıyorum."
        m "Eğer pes edersen, gerçekten hayal kırıklığına uğrarım."
        m "Onlara önem verdiğimden değil ama..."
        m "Bu kadar çok uğraştıktan sonra senin pes etmene tanık olmak beni de üzse de."
        m "Sonuçta, senin başarılı olmanı istiyorum."
    else:
        show m_worried with dissolve_cg
        m "Sayori ve Yuri'yi mutlu ettin, o yüzden neredeyse oradasın."
        m "Henüz pes etme."
        m "Hmm?"
        m "Hayır, onlar için değil, ama..."
        m "Mutlu görünüyorsun."
        m "O yüzden sana biraz itici bir güç verebilirim."
        m "Beni dikkate alma, sanırım."
    show m_neutral2 with dissolve_cg
    m "Verilmesi gereken karar şu anda oldukça belli, değil mi?"
    m "Bunu alacağından eminim, yoksa o kadar kötü yürekli misin?"
    m "Ama senin o tür biri olmadığını biliyorum."
    m "Her neyse, ne yapman gerektiğini biliyorsundur."
    m "Başlık ekranına geri..."
    $ persistent.natsukiBadInterludeViewed = True
    window hide
    $ saveLocked = False
    stop music fadeout 5.0
    hide monika_bg_highlight #with Dissolve(2.0, alpha=True)
    hide monika_bg #with Dissolve(1.5, alpha=True)
    hide mask_3 #with Dissolve(1.0, alpha=True)
    hide mask_2
    with Dissolve(1.0, alpha=True)
    return

label MonikaInterlude_SayoriBadEnd:
    window hide
    $ saveLocked = True
    #pause(5.0)
    show black with Dissolve(1.5)
    play music m1 fadein 5.0
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    with Dissolve(5.0, alpha=True)
    window show
    show m_neutral1 with dissolve_cg
    m "..."
    m "Evet, demek ki planladığın gibi gitmedi, değil mi?"
    show m_thoughtful with dissolve_cg
    m "Eğer bana suç atmaya başlıyorsan, sözümü tuttum."
    m "Hiçbir şey yapmadım."
    m "Her durumda, bana her şey için suç atamayacağını unutmamalısın."
    m "Ama hâlâ geri dönüp her şeyi düzeltebilirsin."
    m "Bunun gücüne sahipsin, değil mi?"
    if persistent.natsukiCompletedGood is False and persistent.yuriCompletedGood is False:
        m "Bence kolayca moralin bozulmaz."
        m "Onları mutlu etmek için yola çıktın, bu yüzden burada durmayacağını düşünüyorum."
        m "Sayori'yi istediğin sona ulaştırmak için uğraşacağına eminim."
        m "Bunun için sadece bir 'oyun kaydet' meselesi."
        m "Beni engellemene gerek yok."
    elif (persistent.natsukiCompletedGood is False and persistent.yuriCompletedGood is True) or (persistent.natsukiCompletedGood is True and persistent.yuriCompletedGood is False) and not (persistent.natsukiCompletedGood is True and persistent.yuriCompletedGood is False):
        show m_neutral2 with dissolve_cg
        m "Zaten birini mutlu ettin, bu yüzden başkasında hata yapman yüzünden pes etmeyeceğini sanıyorum."
        m "Eğer pes edersen, gerçekten hayal kırıklığına uğrarım."
        m "Onlara önem verdiğimden değil ama..."
        m "Bu kadar çok uğraştıktan sonra senin pes etmene tanık olmak beni de üzse de."
        m "Sonuçta, senin başarılı olmanı istiyorum."
        m "Hatta kalbim biraz kırılıyor olsa bile."
    else:
        show m_worried with dissolve_cg
        m "Natsuki ve Yuri'yi mutlu ettin, o yüzden neredeyse oradasın."
        m "Henüz pes etme."
        show m_confused1 with dissolve_cg
        m "Hmm?"
        m "Hayır, onlar için değil, ama..."
        show m_thoughtful with dissolve_cg
        m "Mutlu görünüyorsun."
        m "O yüzden sana biraz itici bir güç verebilirim."
        m "Beni dikkate alma, sanırım."
    show m_neutral2 with dissolve_cg
    m "Verilmesi gereken kararlar oldukça belli, değil mi?"
    m "O, kendi başına ayakta durmak istiyor."
    m "Sadece ona acımamalısın."
    m "Bundan sonrası için ne yapman gerektiğini biliyorsundur."
    m "Yoksa o kadar kötü yürekli misin, sadece onun acı çekmesini istiyorsun?"
    m "Ama senin o tür biri olmadığını biliyorum."
    m "Her neyse, ne yapman gerektiğini biliyorsundur."
    m "Başlık ekranına geri..."
    m "Bu sefer daha iyi yap, tamam mı?"

    $ persistent.sayoriBadInterludeViewed = True
    window hide
    $ saveLocked = False
    stop music fadeout 5.0
    hide monika_bg_highlight #with Dissolve(2.0, alpha=True)
    hide monika_bg #with Dissolve(1.5, alpha=True)
    hide mask_3 #with Dissolve(1.0, alpha=True)
    hide mask_2
    with Dissolve(1.0, alpha=True)

    if persistent.opening_scene is True:
        $ config.main_menu_music = audio.titleTheme
    else:
        $ config.main_menu_music = audio.t1
    play music titleTheme fadein 5.0
    return

label MonikaInterlude_SayoriGoodEnd:
    window hide
    $ saveLocked = True
    #pause(5.0)
    show black with Dissolve(1.5)
    play music m1 fadein 5.0
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    with Dissolve(5.0, alpha=True)
    window show
    show m_neutral2 with dissolve_cg
    $ persistent.sayoriCompletedGood = True
    m "Hm?"
    m "Ne, yaptıklarını mı yorumlamamı istiyorsun?"
    m "Bir çeşit tebrik duymak mı?"
    if persistent.natsukiCompletedGood is False and persistent.yuriCompletedGood is False:
        show m_thoughtful with dissolve_cg
    m "Belki de sonunda Edebiyat Kulübü'ndeki birini mutlu etmeyi başardığını kabul etmelisin, ha?"
    m "Ama sadece birini."
    m "Hem, bu da uzun sürmeyecek."
    m "Sen de ben de gayet iyi biliyoruz ki bu sadece bir mod."
    
    show m_neutral1 with dissolve_cg
    
    m "Başka ne söylenebilir ki?"
    m "Sayori'yi 'kurtardın', değil mi?"
    m "Artık depresyonun karanlığı onu yutmuyor."
    m "Bundan sonra el ele tutuşup, öpüşüp, mutlu anılar biriktireceksiniz."
    m "Tabii oyunun dediğine bakarsak."
    
    if not (sayori_flag_one is True and sayori_flag_two is True):
        show m_smug with dissolve_cg
        hide m_neutral1
        
        m "Ah, ama sanki bir şeyi atlamış gibisin."
        m "Kim bilir, belki bazı kritik seçimleri değiştirsen özel bir şey olurdu?"
        m "Bilmiyorum tabii."
        m "Ama bu 'rota'da bayağı seçenek vardı."
        m "Beni boş ver."
    
    else:
        m "Sonunda o tatlı küçük sahneyi bile görebildin."
        m "Birlikte çikolata yapıyordunuz, değil mi?"
        m "Biraz klişe ama... Onun gülümsemesini görmek istiyorsan, senin için yeterlidir herhalde."
        m "Kim bilir."
    
    show m_neutral1 with dissolve_cg
    
    m "Ama eğer bana karşı bir intikam planı kurduysan..."
    m "Üzgünüm, ama hevesin kursağında kalacak."
    m "Gerçi Sayori de böyle bir şeyi istemezdi, değil mi?"
    m "Artık benim söyleyecek başka bir şeyim kaldı mı ki?"
    
    if persistent.natsukiCompletedGood is True and persistent.yuriCompletedGood is True:
        call MonikaRouteOpening
        return
    
    show m_worried with dissolve_cg
    hide m_neutral1
    
    m "Sonunda pek de bir önemi yok gerçi."
    m "Mutlu olmana engel olacak değilim."
    
    show m_neutral1 with dissolve_cg
    
    m "Ne istiyorsan onu yap."
    window hide
    $ saveLocked = False
    stop music fadeout 5.0
    hide monika_bg_highlight #with Dissolve(2.0, alpha=True)
    hide monika_bg #with Dissolve(1.5, alpha=True)
    hide mask_3 #with Dissolve(1.0, alpha=True)
    hide mask_2
    with Dissolve(1.0, alpha=True)

    if persistent.opening_scene is True:
        $ config.main_menu_music = audio.titleTheme
    else:
        $ config.main_menu_music = audio.t1 # I SWEAR THIS THING IS BUGGED I DON'T KNOW WHY
    play music titleTheme fadein 5.0
    return

label monikaInterlude_YuriBadEnd1:
    window hide
    $ saveLocked = True
    #pause(5.0)
    show black with Dissolve(1.5)
    play music m1 fadein 5.0
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    with Dissolve(5.0, alpha=True)
    window show
    show m_neutral2 with dissolve_cg

        m "...peki, demek böyle."
    m "Açıkçası, bu kadar çabuk yoldan çıkacağını beklemiyordum."
    m "Ama hepimiz hata yaparız, değil mi?"
    m "Bu arada, Natsuki'ye güvenebilirsin, biliyorsun, değil mi?"
    m "Yuri'yle bazen tartışsalar da, onu yeterince iyi tanıyor ve iyi önerilerde bulunabiliyor."
    
    if persistent.natsukiCompletedGood is True:
        m "Hem, Natsuki ve güven meselesine dair biraz fikrin var artık, değil mi?"
    
    if persistent.natsukiCompletedGood is False and persistent.sayoriCompletedGood is False:
        show m_thoughtful with dissolve_cg
        hide m_neutral2
        m "Ama tek bir hatayla hemen pes edeceğini sanmıyorum."
        m "Onları mutlu etmek için yola çıktın, değil mi? Burada duracak değilsin."
        m "Yuri bazen sadece biraz mesafeye ihtiyaç duyar, hepsi bu."
        m "Senin için sadece bir 'oyunu yükle' meselesi sonuçta."
        m "Ben seni durdurmayayım."
    
    elif (persistent.natsukiCompletedGood is False and persistent.sayoriCompletedGood is True) or (persistent.natsukiCompletedGood is True and persistent.sayoriCompletedGood is False) and not (persistent.natsukiCompletedGood is True and persistent.sayoriCompletedGood is True):
        show m_neutral2 with dissolve_cg
        m "Sonuçta birini mutlu etmeyi başardın, değil mi? Sırf biriyle hata yaptın diye pes edeceğini sanmıyorum."
        m "Öyle yapsaydın, gerçekten hayal kırıklığına uğrardım."
        m "Gerçi ne onları umursuyorum ne de sen benim ne düşündüğümü önemsiyorsun ama..."
        m "Bu kadar çabaladıktan sonra vazgeçtiğini görmek beni de biraz yaralıyor."
        m "Başarılı olmanı görmek istiyorum, sonuçta."
        m "Bunu söylerken içim biraz acıyor olsa da..."
    
    else:
        m "Hâlâ geri dönüp işleri düzeltebilirsin."
        show m_worried with dissolve_cg
        hide m_neutral2
        m "Bu güce sahipsin, değil mi?"
        m "Sonuçta diğer ikisini mutlu etmeyi başardın..."
        m "Neredeyse tamamladın."
        m "Bu kadar kolay vazgeçme. Önünde daha zorlayıcı şeyler var, eminim."
        m "...senin için en azından."
    
    show m_neutral2 with dissolve_cg
    m "Ama... bunun tek önemli seçim olduğunu sanma."
    m "Ne olacağını asla bilemezsin."
    m "Hadi, başa dönelim."
    m "Bu sefer daha doğru bir seçim yap, tamam mı?"

    $ persistent.yuriBadInterlude1Viewed = True
    window hide
    $ saveLocked = False
    stop music fadeout 5.0
    hide monika_bg_highlight #with Dissolve(2.0, alpha=True)
    hide monika_bg #with Dissolve(1.5, alpha=True)
    hide mask_3 #with Dissolve(1.0, alpha=True)
    hide mask_2
    with Dissolve(1.0, alpha=True)

    if persistent.opening_scene is True:
        $ config.main_menu_music = audio.titleTheme
    else:
        $ config.main_menu_music = audio.t1
    play music titleTheme fadein 5.0
    return

label monikaInterlude_YuriBadEnd2:
    window hide
    $ saveLocked = True
    #pause(5.0)
    show black with Dissolve(1.5)
    play music m1 fadein 5.0
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    with Dissolve(5.0, alpha=True)
    window show
    show m_neutral2 with dissolve_cg

    m "..."
    m "..."
    m "..."
    show m_confused1 with dissolve_cg
        m "Demek... bu da oldu."
    m "Açıkçası, gerçekten kavga edeceğinizi düşünmemiştim."
    m "Sana 'iyi misin' diye sormak isterdim ama... şey, {i}sen{/i} değildin."
    m "O kadar da zor bir seçim gibi gelmemişti bana..."
    m "Umarım bunu sadece onun acı çekmesini izlemek için seçmemişsindir."
    m "Ha..."
    m "Neyse, sanırım ne yapman gerektiğini zaten biliyorsun."

    if persistent.natsukiCompletedGood is False and persistent.sayoriCompletedGood is False:
        show m_thoughtful with dissolve_cg
        hide m_neutral2
        m "Daha yolun başındasın, değil mi?"
        m "Bazen ilk adımda tökezlersin ama..."
        m "Burada durmayacağını biliyorum."
        m "Belki diğerlerine yönelmeyeceksin ama buraya kadar geldiysen, devam edeceksin."
        m "O yüzden... ne yapacağını biliyorsun."
        m "Senin için sadece bir 'Oyunu Yükle' meselesi, değil mi?"
    
    elif (persistent.natsukiCompletedGood is False and persistent.sayoriCompletedGood is True) or (persistent.natsukiCompletedGood is True and persistent.sayoriCompletedGood is False) and not (persistent.natsukiCompletedGood is True and persistent.sayoriCompletedGood is True):
        show m_neutral2 with dissolve_cg
        m "Sonuçta birini mutlu etmeyi başardın, değil mi? Sırf biriyle hata yaptın diye pes edeceğini sanmıyorum."
        m "Eğer öyle yaparsan, gerçekten hayal kırıklığına uğrarım."
        m "Sen kesinlikle öyle biri değilsin."
        m "Bu kadar çabaladıktan sonra vazgeçtiğini görmek beni de biraz yaralıyor."
        m "Başarılı olmanı görmek istiyorum, sonuçta."
        m "Bunu söylerken içim biraz acıyor olsa da..."
    
    else:
        show m_worried with dissolve_cg
        hide m_neutral2
        m "Hâlâ geri dönüp işleri düzeltebilirsin."
        m "Bu güce sahipsin, değil mi?"
        m "Sonuçta diğer ikisini mutlu etmeyi başardın..."
        m "Neredeyse tamamladın."
        m "Bu kadar kolay vazgeçme."
        m "Ne yapman gerektiğini biliyorsun."

    show m_neutral2 with dissolve_cg
    m "Peki..."
    m "Başa dönüyoruz, değil mi?"
    m "Bu sefer biraz daha iyi bir iş çıkar, tamam mı?"

    $ persistent.yuriBadInterlude2Viewed = True
    window hide
    $ saveLocked = False
    stop music fadeout 5.0
    hide monika_bg_highlight #with Dissolve(2.0, alpha=True)
    hide monika_bg #with Dissolve(1.5, alpha=True)
    hide mask_3 #with Dissolve(1.0, alpha=True)
    hide mask_2
    with Dissolve(1.0, alpha=True)

    if persistent.opening_scene is True:
        $ config.main_menu_music = audio.titleTheme
    else:
        $ config.main_menu_music = audio.t1
    play music titleTheme fadein 5.0
    
    return

label monikaInterlude_YuriGoodEnd:
    window hide
    $ saveLocked = True
    #pause(5.0)
    show black with Dissolve(1.5)
    play music m1 fadein 5.0
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    with Dissolve(5.0, alpha=True)
    window show
    show m_neutral2 with dissolve_cg
    $ persistent.yuriCompletedGood = True

        m "Hm?"
    m "Ne yani, yaptıkların hakkında bir şeyler mi söylememi istiyorsun?"
    m "Bir tebrik mi bekliyorsun yoksa?"
    
    if persistent.natsukiCompletedGood is False and persistent.sayoriCompletedGood is False:
        show m_thoughtful with dissolve_cg
        m "Belki de Yuri'yi mutlu ettiğin için birkaç övgü duymak istiyorsun?"
        m "Ama sonuçta sadece birini mutlu edebildin."
        m "Hem, bunun sonsuza kadar süreceğini mi sanıyorsun?"
        m "Sen de ben de gayet iyi biliyoruz ki bu sadece bir mod."
        m "Bir gün..."
    
    show m_neutral1 with dissolve_cg
    
    m "Daha ne söylenebilir ki?"
    m "Sonuçta Yuri'yi 'kurtardın', değil mi?"
    m "Artık yardım alıyor ve o korkunç dedikodular başladığında tutunabileceği bir dayanağı var."
    m "Bundan sonra el ele tutuşup, kitap okuyup, mutlu mesut takılacaksınız."
    m "Tabii oyunun dediğine göre."
    m "Ama cidden..."
    m "Bu okuldaki çocukların hepsi neden böyle?"

    if persistent.sayoriCompletedGood is True:
        m "Hem Sayori’nin 'rotasında' hem burada..."
        m "Çocuklar biraz fazla acımasız değil mi?"
    
    m "Ah, biz nasıl bir okula yazıldık ki böyle insanlar var?"
    m "Gerçi senin için pek bir önemi yok, değil mi?"
    m "Sonuçta Yuri ile mutlusun."
    m "Benim daha fazla söyleyecek bir şeyim kaldı mı ki?"

    if persistent.natsukiCompletedGood is True and persistent.sayoriCompletedGood is True:
        call MonikaRouteOpening
        return

    show m_worried with dissolve_cg
    hide m_neutral1
    
    m "Ama en sonunda pek de bir önemi yok sanırım."
    m "Mutlu olmanı engellemeyeceğim."
    
    show m_neutral1 with dissolve_cg
    
    m "Ne yapmak istiyorsan onu yap."

    window hide
    $ saveLocked = False
    stop music fadeout 5.0
    hide monika_bg_highlight #with Dissolve(2.0, alpha=True)
    hide monika_bg #with Dissolve(1.5, alpha=True)
    hide mask_3 #with Dissolve(1.0, alpha=True)
    hide mask_2
    with Dissolve(1.0, alpha=True)

    if persistent.opening_scene is True:
        $ config.main_menu_music = audio.titleTheme
    else:
        $ config.main_menu_music = audio.t1 # I SWEAR THIS THING IS BUGGED I DON'T KNOW WHY
    play music titleTheme fadein 5.0
    
    return



label MonikaRouteOpening:
    $ persistent.monika_unlock = True
    show m_thoughtful with dissolve_cg
    m "Sanırım söylemem gereken bir şey var."
    m "Benim bile mümkün olduğunu düşünmediğim bir şeyi başardın..."
    
    show m_surprise with dissolve_cg
    
    m "Edebiyat Kulübü’nden gelen... mutluluk." 
    show m_confused2 with dissolve_cg
    
    m "Bu gerçekten ilginç, değil mi?"
    m "Hissedebiliyorum... adeta içlerinden taşan o duyguyu."
    
    show m_teary with dissolve_cg
    
    m "Sanırım oyunun bir parçası olmanın bir getirisi bu."
    m "Hepsi... gerçekten çok mutlu..."
    m "Biraz kıskandım, haha~"
    
    show m_neutral1 with dissolve_cg
    
    m "Ama sorun değil."
    m "Sonuçta yapmak istediğin şeyi başardın."
    m "Sayori, Yuri, Natsuki..."
    m "Hepsinin yüzü gülüyor, içten ve gerçekten."
    
    show m_thoughtful with dissolve_cg
    
    m "Öyleyse bir tebrik gerekiyor sanırım."
    m "Oyunu tamamladın."
    m "Herkesi kurtardın... yani, ne demek istediğimi anlıyorsun."
    
    show m_neutral2 with dissolve_cg
    
    m "Ne kadar da özelsin, değil mi?"
    
    show m_surprise with dissolve_cg
    
    m "Hm? Bir şey mi oldu?"
    m "Neden hâlâ buradasın?"
    m "Burada senin için artık hiçbir şey kalmadı."
    
    show m_neutral1 with dissolve_cg
    
    m "..."
    
    show m_smug with dissolve_cg
    
    m "Ah."
    
    show m_thoughtful with dissolve_cg
    
    m "Krediler akmaya başlamadı, değil mi?"
    m "Senaryoda bir şeyi mi kaçırdın? Belki de bir dal seçeneği tetiklenmedi?"
    
    show m_neutral2 with dissolve_cg
    
    m "Sorun değil. Hepimizin başına gelebilir."
    m "Bildiklerim kadarıyla, bunu yapabilen sadece sen ve benim gibileriyiz."
    m "Gerçi üstünlük sende gibi görünüyor."
    
    show m_neutral1 with dissolve_cg
    
    m "Neyse, ne fark eder ki."
    m "Sanırım başa dönme vakti geldi..."
    return