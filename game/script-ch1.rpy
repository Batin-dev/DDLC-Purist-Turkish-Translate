# Chapter 1 static content. Poem responses called from here are in script-poemresponses.rpy

label ch1_main:
    scene bg club_day
    with dissolve_scene_half
    play music t2
    show monika 5 at t11 zorder 2

    m "Tekrar merhaba, [player]!"
    m "Bburadan kaçıp gitmediğinize sevindim. Ehehe!"
    mc "Hayır, endişelenme.."
    mc "Bu benim için biraz garip, ama en azından sözümü tutuyorum."
    show monika at thide zorder 1
    hide monika
    "Tamam, Literatür Kulübü'ne geri döndüm."
    "Ben son gelenim, dolayısıyla diğer herkes zaten vakit geçiriyor."
    show yuri 1a at t32 zorder 2
    y "Sözünü tuttuğun için teşekkür ederim, [player]."
    y "Umuyorum ki bu senin için çok fazla yüklenme olmaz."
    y 1u "Alışık olmadığın zamanlarda edebiyata kafa kafaya dalmanı sağlıyor..."
    show natsuki 4e at t33 zorder 2
    n "Hadi ama! Sanki herhangi bir gevşekliği hak ediyormuş gibi."
    n "Sayori bana bu yıl hiçbir kulübe katılmak istemediğini söyledi."
    n "Geçen yıl da öyleydi.!"
    n 4c "Bilmiyorum, belki sadece buraya gelip takılmayı planlıyorsun, ya da ne yapmayı düşünüyorsun..."
    n "Ama bizi ciddiye almazsan, bunun sonunu göremezsin."
    show monika 2b at l41
    m "Natsuki, kulüp odasında mangalarını saklayan biri için gerçekten büyük bir ağzın var."
    n 4o "M-M-M...!!"
    show monika at lhide
    hide monika
    "Natsuki kendini \"Monika\" and \"Manga\" arasında sıkışmış buluyor."
    show natsuki at h33
    n 1v "Manga edebiyattır!!"
    show natsuki at thide zorder 1
    hide natsuki
    "Hızla mağlup olan Natsuki, koltuğuna geri döner."
    show yuri at t22 zorder 2
    show sayori 2x at f21 zorder 3
    s "Endişelenmeyin, arkadaşlar~" #You Are Not Real.
    s "[player] eğlendiği sürece her zaman elinden gelenin en iyisini yapar."
    s "Bana sormadan bile yoğun işlerde bana yardım ediyor."
    s "Yemek yapmak, odamı temizlemek gibi..."
    show sayori 2a at t21 zorder 2
    show yuri at f22 zorder 3
    y 2m "Ne kadar güvenilir..."
    show yuri at t22 zorder 2
    mc "Sayori, çünkü odan o kadar dağınık ki dikkatini dağıtıyor."
    mc "Bir keresinde neredeyse evini ateşe verecektin."
    show sayori at s21
    s 5 "Öyle mi... Hehe..."
    show yuri at f22 zorder 3
    y 1s "İkiniz gerçekten iyi arkadaşsınız, değil mi?"
    y "Biraz kıskanmış olabilirim..."
    show yuri at t22 zorder 2
    show sayori at f21 zorder 3
    s 1 "Nasıl olur? Sen ve [player] çok iyi arkadaş olabilir!"
    show sayori at t21 zorder 2
    show yuri at f22 zorder 3
    y 4b "U-Um..."
    show yuri at t22 zorder 2
    mc "S-Sayori--"
    show sayori at f21 zorder 3
    s "Hmm?"
    show sayori at t21 zorder 2
    mc "..."
    "Her zamanki gibi, Sayori beni içine soktuğu garip durumdan habersiz görünüyor."
    show sayori at f21 zorder 3
    s 4x "Oh, oh! Yuri bugün sana bir şey bile getirdi, biliyorsun~"
    show sayori at t21 zorder 2
    show yuri at f22 zorder 3
    y 3n "B-Bekle! Sayori..."
    show yuri at t22 zorder 2
    mc "Eh? Bana mı?"
    show yuri at f22 zorder 3
    y 3o "Um... Pek değil..."
    show yuri at t22 zorder 2
    show sayori at f21 zorder 3
    s 4r "Utanma~"
    show sayori at t21 zorder 2
    show yuri at f22 zorder 3
    y "Gerçekten önemli değil..."
    show yuri at t22 zorder 2
    mc "O nedir?"
    show yuri at f22 zorder 3
    y 4c "Hiçbirşey!"
    y "Sayori, gerçekten olmadığı zaman büyük bir anlaşma gibi ses çıkardı..."
    y "Uuuuh, ne yapacağım..."
    show yuri at t22 zorder 2
    show sayori at f21 zorder 3
    s 1g "Ha? Üzgünüm Yuri, ben öyle düşünmüyordum..."
    show sayori at thide zorder 1
    hide sayori
    show yuri at t11 zorder 2
    "Sanırım bu, bu durumu kurtarmanın bana bağlı olduğu anlamına geliyor..."
    mc "Hey, merak etme."
    mc "Her şeyden önce, ilk başta hiçbir şey beklemiyordum." #Bendeöyle
    mc "Yani senden gelen herhangi bir jest hoş bir sürpriz."
    mc "Ne olursa olsun beni mutlu edecek."
    y 3v "Ö-Öyle mi..."
    mc "Evet. Eğer sen istemiyorsan, bunu büyütmeyeceğim."
    y "T-tamam..."
    y 1a "Pekala, işte."
    "Yuri çantasına uzanır ve bir kitap çıkarır."
    y "Kendini dışlanmış hissetmeni istemedim..."
    y "Hoşuna gidebileceğini düşündüğüm bir kitap seçtim."
    y "Kısa bir okuma, bu yüzden genellikle okumasanız bile dikkatini çekecektir."
    y "Ve biz, bilirsin."
    show yuri at sink
    y 4b "Tartışırız... tabi istersen..."
    "B-bu..."
    "Bu kız nasıl kazara bu kadar sevimli olabiliyor?" #Sayori Daha Sevimli lan MC
    "Çok fazla kitap okumadığım halde seveceğimi düşündüğü bir kitap bile seçmiş..."
    mc "Yuri, teşekkür ederim! Bunu kesinlikle okuyacağım!"
    "Kitabı hevesle aldım."
    show yuri 2m at t11 zorder 2
    y "Vay..."
    y 2a "Kendi hızında okuyabilirsin."
    y "Ne düşündüğünü duymak için sabırsızlanıyorum."
    show yuri at thide zorder 1
    hide yuri

    #Exclusive scene starts here
    "Artık herkes yerleştiğine göre, Monika'nın kulüp için planlanan bazı etkinlikleri başlatmasını bekliyordum."
    "BAma durum öyle görünmüyor."
    "Sayori ve Monika köşede neşeli bir sohbet içindedir."
    "Yuri'nin yüzü çoktan bir kitaba gömüldü."
    "Bu fırsatı bekliyormuş gibi gergin ifadesini fark etmeden edemiyorum."
    "Bu sırada Natsuki dolabı karıştırmaktadır."
    
    #Call exclusive scene
    $ nextscene = poemwinner[0] + "_exclusive_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene

    #After exclusive scene, we go back to poem responses
    show monika 1 at t21 zorder 2
    hide sayori
    hide natsuki
    hide yuri
    m "Bu arada, dün gece bir şiir yazmayı unutmadın değil mi?"
    mc "E-Evet..."
    "Rahatlamam sona erdi."
    "Bu kadar utanç verici bir şeyi yapmayı kabul ettiğime inanamıyorum."
    "Bunu daha önce hiç yapmadığım için pek ilham bulamadım."
    m "Peki, herkes hazır olduğuna göre, neden paylaşacak birini bulmuyorsun?"
    show sayori 4q at t22 zorder 2
    s "Sabırsızlanıyorum!"
    show sayori at thide zorder 1
    show monika at thide zorder 1
    hide sayori
    hide monika
    "Sayori ve Monika hevesle şiirlerini çıkardılar."
    "Sayori'ninki spiralli bir defterden koparılmış buruşuk bir yaprağın üzerinde."
    "Öte yandan, Monika onunkini bir kompozisyon defterine yazdı."
    "Monika'nın tertemiz el yazısını oturduğum yerden bile görebiliyorum."
    "Natsuki ve Yuri de isteksizce çantalarına uzanıyorlar."
    "Ben de aynısını yapıyorum."

    return


label ch1_end:
    stop music fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    play music t3
    mc "Phew..."
    "Sanırım herkes bu kadar."
    "Odaya bir göz attım."
    "Bu beklediğimden biraz daha stresliydi."
    "Sanki herkes beni vasat yazma becerilerimden dolayı yargılıyor..."
    "Sadece iyi davranıyor olsalar bile, şiirlerimin onlarınkiyle boy ölçüşmesine imkân yok."
    "Ne de olsa burası bir edebiyat kulübü."
    "İç çekiyorum."
    "Sanırım kendimi içine soktuğum şey bu."
    "Odanın diğer ucunda Sayori ve Monika mutlu bir şekilde sohbet ediyorlar."
    "Gözlerim Yuri ve Natsuki'ye takılıyor."
    show yuri 2g at t21 zorder 2
    show natsuki 1g at t22 zorder 2
    "Kâğıtları nazikçe değiştirerek kendi şiirlerini paylaşırlar."
    show yuri 2i at t21
    "Birlikte okurken, her birinin ifadesinin değiştiğini izliyorum."
    "Natsuki'nin kaşları hayal kırıklığıyla çatılıyor."
    "Bu arada, Yuri hüzünle gülümsüyor."
    show natsuki at f22 zorder 3
    n 1q "{i}(Bu dil de ne böyle...?){/i}"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 2f "Eh?"
    y "Bir şey mi dedin?"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 2c "Önemli bir şey değil."
    "Natsuki şiiri tek eliyle masaya geri koyuyor."
    n "Sanırım süslü olduğunu söyleyebilirsin."
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 2i "Ah-- Teşekkürler..."
    y "Seninki... çok şirin."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 2h "Şirin mi?"
    n 1h "Sembolizmi tamamen kaçırdın mı yoksa?"
    n "Bu açıkça pes etme duygusuyla ilgili."
    n "Bu nasıl sevimli olabilir?"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 3f "Bunu biliyorum!"
    y "Ben sadece..."
    y 3h "Bu Dil, sanırım..."
    y "Güzel bir şey söylemeye çalışıyordum..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n "Eh?"
    n 4w "Yani söyleyecek güzel bir şey bulmak için bu kadar uğraşmak zorunda mısın?"
    n "Teşekkürler, ama gerçekten hiç de güzel olmadı!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 1i "Um..."
    y "Şey, birkaç önerim var."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 5x "Hmph."
    n "Eğer öneri arıyor olsaydım, bunu gerçekten seven birine sorardım."
    n "Hangi insanlar {i}bu{/i}, arada."
    n 5e "Sayori'nin hoşuna gitti."
    n "ve [player] da öyle"
    n "Buna dayanarak, size memnuniyetle kendi önerilerimi sunacağım."
    n "Her şeyden önce--"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 2l "Affedersin..."
    y "Teklifin için teşekkür ederim, ama yazı stilimi oluşturmak için uzun zaman harcadım."
    y 2h "Yakın zamanda değişmesini beklemiyorum, tabii özellikle ilham verici bir şeyle karşılaşmadığım sürece."
    y "Ki henüz karşılaşmadım."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1o "Nn...!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 1k "ayrıca [player] benim şiirimi de beğendi, biliyorsun."
    y "Hatta bana bundan etkilendiğini bile söyledi."
    stop music fadeout 1.0
    "Natsuki aniden ayağa kalkar."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 4y "Ha?"
    n "Yeni üyemizi etkilemek için bu kadar uğraştığını fark etmemiştim."
    play music t7
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 1n "E-Eh?!"
    y "Ben öyle bir şey yapmadım!"
    y 1o "Uu..."
    y "Sen... Sen sadece..."
    "Yuri de ayağa kalkıyor."
    y 2r "Belki de [player] benim tavsiyelerimi sizinkilerden daha çok takdir ettiği için kıskanıyorsunuzdur!"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1e "Ha! Benim tavsiyelerimi daha çok taktir {i}my{/i} etmediğini nereden biliyorsun?"
    n "Kendini o kadar mı beğeniyorsun?"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 3h "Ben...!"
    y "Hayır..."
    y "Eğer kendimi beğenmiş olsaydım..."
    y 1r "...yaptığım her şeyi aşırı şirin hale getirmek için kasten yolumdan çekilirdim!"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1o "Uuuuuu...!"
    show sayori 2l at l41 behind yuri,natsuki
    show yuri at t32 zorder 2
    show natsuki at t33 zorder 2
    s "U-Um!!"
    s "Herkes iyi mi...?" #Sen iyi ol yeter balımmm
    show sayori 2 at lhide
    hide sayori
    show natsuki at f33 zorder 3
    n 1f "Ne var biliyor musun?!"
    n "[player] ortaya çıkmaya başlar başlamaz göğüsleri sihirli bir şekilde bir beden büyüyen ben değildim!!!"
    show yuri 3p at h32
    show natsuki at t33 zorder 2
    y "N-Natsuki!!"
    show monika 3l at l41 behind yuri,natsuki
    m "Natsuki, bu biraz--"
    show monika at h41
    show yuri 3p at f32 zorder 3
    show natsuki 1e at f33 zorder 3
    ny "Bu seni ilgilendirmez!"
    show monika at lhide
    hide monika
    show yuri at t32 zorder 2
    show natsuki at t33 zorder 2
    show sayori 4p at l41 behind yuri,natsuki
    s "Kavga etmeyi sevmiyorum, çocuklar...!" #Boşver sen bu olayları balım
    show sayori at lhide
    hide sayori
    show yuri at t21 zorder 2
    show natsuki 1g at t22 zorder 2
    "Birden iki kız da sanki orada durduğumu yeni fark etmişler gibi bana doğru döndüler." #Hacı herşey isteğimiz dışı oluyor bu kadar kasmayın beni :(
    show yuri at f21 zorder 3
    y 2n "[player]...!"
    y "O- O sadece beni kötü göstermeye çalışıyor."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 4w "Bu doğru değil!" #Etmeyin kavga izin verdim mi lan
    n "Bunu o başlattı!"
    n 4e "Kendini {i}aşabilse{/i} ve yazmanın daha etkili olduğunu takdir etmeyi öğrenebilse..."
    n "O zaman bunlar hiç yaşanmazdı!"
    n "Şiirlerini sebepsiz yere karmaşık hale getirmenin ne anlamı var?"
    n "Anlam okuyucunun üzerine sıçramalı, onu anlamaya zorlamamalı."
    n 1f "Bunu ona açıklamama yardım et, [player]!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 3o "B-Bekle!"
    y "Dilimizde bu kadar çok derin ve etkileyici sözcük olmasının bir nedeni var!"
    y 3w "Karmaşık duyguları ve anlamları en etkili şekilde aktarmanın tek yolu budur."
    y "Onlardan kaçınmak sadece kendinizi gereksiz yere sınırlamak değil... aynı zamanda bir israftır!"
    y 1t "Bunu anlıyorsun, değil mi [player]?"
    show yuri at t21 zorder 2
    mc "Um...!"
    show yuri 1t at f21 zorder 3
    show natsuki 1e at f22 zorder 3
    ny "Evet??"
    mc "..."
    show yuri at t21 zorder 2
    show natsuki 1g at t22 zorder 2
    "Nasıl oldu da bu işin içine sürüklendim?!"
    "Yazmak hakkında bir şey bildiğim yok ki..."
    "Ama kiminle anlaşırsam, muhtemelen benim hakkımda daha iyi düşüneceklerdir!"
    menu:
        "Yani, tabii ki bu olacak...!"
        "Natsuki.":
            call ch1_end_natsuki
        "Yuri.":
            call ch1_end_yuri
        "Yardım et, Sayori!!":
            call ch1_end_sayori

    scene bg club_day
    show monika 4b at t11 zorder 2
    with wipeleft_scene
    m "Tamam, millet!"
    m "Gitme vaktimiz gelmek üzere."
    m "Şiirleri paylaşma konusunda ne hissettiniz?"
    show monika 4a
    show sayori 4x at t31 zorder 2
    s "Ç!ok eğlenceliydi" #OFF SENİN BAŞINDAKİ S HARFİNİ YERİMM
    show sayori at thide behind yuri
    show yuri 1i at t31 zorder 2
    hide sayori
    y "Buna değdi diyebilirim."
    show yuri at thide behind natsuki
    show natsuki 4q at t31 zorder 2
    hide yuri
    n "İyiydi. Yani, çoğunlukla."
    show natsuki at thide zorder 1
    hide natsuki
    m 1a "[player], Peki ya sen?"
    mc "...Evet, ben de aynısını söyleyebilirim."
    mc "Herkesle konuşmak için güzel bir şeydi."
    m 1j "Harika!"
    m 1a "O halde yarın da aynı şeyi yaparız."
    m "Belki sen de arkadaşlarından bir şeyler öğrenmişsindir."
    m 3b "Böylece şiirlerin daha da güzel olacak!"
    mc "..."
    show monika at thide zorder 1
    hide monika
    "Kendi kendime düşünüyorum."
    "Herkesin sevdiği şiir türleri hakkında biraz daha fazla şey öğrendim."
    "Şansım varsa, bu en azından etkilemek istediğim kişileri daha iyi etkileyebileceğim anlamına geliyor."
    "Yeni bir kararlılıkla kendi kendime başımı sallıyorum." #Hadi bakalım. İş başa düştü Sıra Manupilator abide
    show sayori 1x at t11 zorder 2
    s "[player]!"
    s "Eve yürümeye hazır mısın?" #Seninle her yere yürürüm aşkımmm
    mc "Tabii, gidelim."
    s 4q "Ehehe~"
    "Sayori sıcak bir şekilde bana bakıyor."
    "Sayori ve ben birlikte bu kadar çok zaman geçirmeyeli gerçekten de uzun zaman oldu."
    "Ben de bundan keyif almadığımı söyleyemem."
    scene bg residential_day
    show sayori 1a at t11 zorder 2
    with wipeleft_scene
    mc "Sayori..."
    mc "Daha önce olanlar hakkında..."
    s 1b "Eh? Ne demek istiyorsun?"
    mc "Biliyorsun, Yuri ve Natsuki arasında."
    mc "Bu tür şeyler sık sık olur mu?"
    s 4j "Hayır, hayır, hayır!"
    s "Onları ilk kez böyle kavga ederken görüyorum..."
    s "Söz veriyorum ikisi de harika insanlar."
    show sayori at s11
    s 1g "Sen... Onlardan nefret etmiyorsun, değil mi?"
    mc "Hayır, onlardan nefret etmiyorum!"
    mc "Sadece senin fikrini almak istedim, hepsi bu."
    mc "Seninle neden iyi arkadaş olduklarını anlayabiliyorum." #Kim Sayori ile arkadaş olmak istemez ki?
    show sayori at t11 zorder 2
    s 1d "Ehh..."
    s "Biliyorsun, [player]..."
    s "Kulüpte seninle vakit geçirebilmem çok güzel."
    s "Ama sanırım beni en çok mutlu eden şey senin herkesle iyi anlaştığını görmek."
    s 1x "Ve bence herkes de seni gerçekten seviyor!"
    mc "Bu--!"
    s 4q "Ehehe~"
    s "Her gün çok eğlenceli olacak~"
    mc "İç çekiyorum..."
    "Görünüşe göre Sayori hala içinde bulunduğum durumu kavrayamamış."
    "Elbette, herkesle arkadaş olmak güzel ama..."
    "...Gerçekten burada bitmesi gerekiyor mu?"
    mc "Gelecekte ne olacağını göreceğiz, Sayori."
    "Sayori'nin omzunu okşadım."
    "Bunu ondan çok kendime söyledim ama Sayori'yi bazen bir iç monolog olarak kullanmak çok kolay."
    show sayori at h11
    s 1x "Tamam~!"
    "Evet..."
    "Hadi yapalım şunu!"
    return

label ch1_end_natsuki:
    $ ch1_choice = "natsuki"
    stop music fadeout 1.0
    mc "Um..."
    mc "Yuri!"
    mc "Gerçekten yeteneklisin."
    show yuri 4a at s21
    y "Eh? Ş-şey..."
    play music t8
    mc "Ama Natsuki haklı!"
    mc "Bence..."
    show yuri at t21 zorder 2
    "Kendimi desteklemek için beynimi zorluyorum."
    mc "Bence duyguları az kelimeyle aktarmak..."
    mc "Bir o kadar da etkileyici olabilir!"
    mc "Okuyucunun hayal gücünün devreye girmesini sağlar."
    mc "Ve Natsuki'nin şiiri bu konuda gerçekten iyi bir iş çıkardı!"
    show natsuki at f22 zorder 3
    n 5y "...Evet!!"
    n "Öyle oldu, değil mi?!"
    n "Ahah!"
    n "Ne kadar çok {i}şey bildiğini{/i} gösteriyor!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 4b "Bu... Bu değil..."
    show yuri at t21 zorder 2
    mc "Natsuki..."
    mc "Bence bu kadar yeter."
    show natsuki at f22 zorder 3
    n 1m "Ha?"
    n "Ben mi?"
    n "Ama o bana çok kötü davrandı...!"
    "Natsuki'nin sesi sızlanıyor."
    show natsuki at t22 zorder 2
    mc "Bak..."
    mc "Dün konuştuğumuz şey doğruydu."
    mc "Yazmak gerçekten kişisel bir şeydir."
    mc "Ve bunu paylaşmak kesinlikle zor olabilir."
    mc "Görünüşe göre bugün bunu öğrendik."
    mc "Küçük bir eleştiri bile oldukça hararetli bir şeye yol açabilir."
    "Omzumun üzerinden bakıyorum."
    "Sayori şiddetle başını sallıyor."
    mc "Evet, yani..."
    mc "Kendini tehdit altında hissetmene gerek yok."
    mc "Sen harika bir yazarsın, Natsuki." #Daha rasyonel bir tavır sergilediğin için teşekkürlerimi sunarım MC. Fakat tek değerlim hala SAYORİ!
    show natsuki at f22 zorder 3
    n 1h "Ah--"
    "Natsuki'nin sesi şaşkınlıkla karşılanır."
    n 1q "...Fark ettiğin için teşekkür ederim."
    "Sonunda zar zor duyulabilir bir şekilde mırıldanıyor."
    show natsuki at t22 zorder 2
    mc "Yuri..."
    show yuri at f21 zorder 3
    y 4a "...?"
    "Yuri bana kederle bakıyor."
    "Böyle bir yüz ifadesiyle, onun için üzülmekten kendimi alamıyorum."
    show yuri at t21 zorder 2
    mc "Natsuki'nin söylediği her şeyi kastetmediğinden eminim."
    mc "Yani senin de kendini tehdit altında hissetmene gerek yok." #Olabildiğince başarılı yüzde yüz kaar oranı elde edemeyiz sonuçta. Biri gider, biri gelr, biri eksilir, diğeri artar. Hayat böyledir.
    show yuri at f21 zorder 3
    y 2v "Şey..."
    y "Eğer öyle diyorsan..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1g "Hey...!"
    n "Benim {i}için{/i} özür dilemene gerek yok, [player]."
    n 1w "Vay be."
    "Natsuki bir nefes alır."
    n 1q "Ben..."
    n "Şey hakkında..."
    n "Uu..."
    "Natsuki odanın etrafına bakar."
    show natsuki at hf22 zorder 3
    n 1x "{i}Herkes bana bakmayı keser mi?{/i}"
    "Şaşırtıcı olmayan bir şekilde, Natsuki övündüğünden daha zor zamanlar geçiriyor."
    "Sayori ve Monika başka tarafa bakıyor."
    n 1i "Hmph."
    n "Her neyse...!"
    n 1q "Göğüslerinle ilgili şey. Öyle demek istemedim, tamam mı?"
    n "Hepsi bu."
    "Natsuki uzaklara bakar, kimseyle göz teması kurmaktan kaçınır."
    show natsuki at t22 zorder 2
    show sayori 4x at l41 behind yuri
    s "Evet! Sen doğuştan güzelsin, Yuri!!"
    mc "Sayori?!"
    show yuri 4c at f21 zorder 3
    y "..."
    y "Ben gidip biraz çay yapayım..."
    show yuri at lhide
    hide yuri
    show sayori at f41 zorder 3
    s 4h "Ehh?"
    s "Sadece yardım etmeye çalışıyordum!"
    show sayori at t41 zorder 2
    mc "Eminim bunu takdir etmiştir, Sayori."
    "Sayori'nin omzunu okşadım." #ohh keşke bende Sayori'nin omzuna erişebilsem.
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    show monika 4m at t11 zorder 2
    hide sayori
    hide natsuki
    m "Peki, artık bunu aştığımıza göre..."
    m 4b "Herkes birbirinin şiirini okudu, değil mi?"
    m "Umarım herkes için faydalı olmuştur!"
    m 5 "Özellikle sen, [oyuncu]!"
    m "Ve dürüst olmak gerekirse..."
    m "Biraz fazla alıştığımız tembellikten sonra güzel bir değişiklik oldu."
    m "Ahahaha!"
    mc "Ah, yani kulübe katılmam atmosferi mahvetmekten sorumluydu..."
    m 1d "Hayır, hiç de değil, hiç de değil!"
    m "Eve gitmeden önce hala vaktimiz var."
    m 1a "Yani hepimiz biraz dinleniriz."
    m "Elbette, sohbet etmenin yanı sıra kulüp odasında edebiyatla ilgili şeyler de yapıyoruz..."
    m "Belki bu fırsatı değerlendirip bir kitap alabilir ya da bir şeyler yazabiliriz."
    m 1b "Ne de olsa kulüp bunun için var!"
    show sayori 2j at f31 zorder 3
    s "Katılmıyorum, Monika!"
    show sayori at t31 zorder 2
    show monika at f32 zorder 3
    m 1d "Eh? Ne hakkında?"
    show monika at t32 zorder 2
    show sayori at f31 zorder 3
    s 2i "Edebiyat kulübüyle ilgili en önemli şey bu değil!"
    s "En önemli şey..." #Senin olman.
    show sayori 4r at hf31 zorder 3
    s "Eğleniyoruz!"
    show sayori at t31 zorder 2
    show monika at f32 zorder 3
    m 2l "Ahaha, tabii ki..."
    m 2a "Sanırım bu yüzden Başkan Yardımcısı oldun, Sayori." #Mmm Başkan yardımcısıda erik gibiymiş
    show monika at t32 zorder 2
    show sayori at f31 zorder 3
    s 4q "Ehehe..."
    hide sayori
    hide monika
    with wipeleft
    "Ama sonuçta Monika haklı."
    "Edebiyat Kulübü'nde olmak muhtemelen tüm zamanımı hiçbir şey yapmadan geçiremeyeceğim anlamına geliyor."
    "Ama sonuçta..."
    "...Sanırım şimdiye kadar buna değdi."
    return
    
label ch1_end_yuri:
    $ ch1_choice = "yuri"
    stop music fadeout 1.0
    mc "Natsuki."
    mc "Şiirini beğendiğim konusunda haklısın."
    show natsuki at f22 zorder 3
    n 1e "Gördün mü??"
    show natsuki 1g at t22 zorder 2
    play music t8
    mc "Bekle!"
    mc "Bu kadar kaba olman için bir bahane değil!"
    mc "Sırf birinin fikri farklı diye kavga çıkarmamalısın."
    show natsuki at f22 zorder 3
    n 1m "Hiç de öyle olmadı!"
    n "Yuri şiirimi ciddiye bile almadı!"
    show natsuki at t22 zorder 2
    mc "Mm..."
    mc "Tamam, Anladım."
    mc "Yuri."
    show yuri at f21 zorder 3
    y 2t "Eh?"
    show yuri at t21 zorder 2
    mc "Gerçekten yetenekli bir yazarsınız."
    mc "Etkilendiğim bir sır değil."
    show yuri at f21 zorder 3
    y 2u "Ş-şey, bu..."
    show yuri at t21 zorder 2
    mc "Ama şöyle bir şey var."
    mc "Birinin yazı stili ne kadar basit ya da rafine olursa olsun..."
    mc "Yine de içine duygularını katıyorlar ve bu gerçekten kişisel bir şey haline geliyor."
    mc "Bu yüzden Natsuki şiirinin sevimli olduğunu söylediğinde kendini tehdit altında hissetti."
    show yuri at f21 zorder 3
    y 2v "Ben... Anladım..."
    y "Fark etmemiştim." #Sorun değil bro ya takma böyle şeyleri. Neyse benim Sayori'm nerede?
    show yuri at t21 zorder 2
    y 2w "Ö-özür dilerim..."
    show yuri at s21
    y "Uuu..."
    show natsuki at t11 zorder 2
    show yuri at thide zorder 1
    hide yuri
    mc "Ama Natsuki, çok ileri gittin!"
    mc "Yuri iyi niyetli ve eğer ona sadece nasıl hissettiğini söyleseydin..."
    mc "O zaman bu en başta olmazdı."
    n 1e "Şaka mı yapıyorsun?"
    n "Ben de aynen öyle yaptım!"
    n "Bu... {i}O{/i} öyleydi--"
    show natsuki at t22 zorder 2
    show monika 2i at f21 zorder 3
    m "Natsuki, sanırım bu kadar yeter."
    m "İkiniz de istemediğiniz bazı şeyler söylediniz."
    m "Yuri özür diledi. Senin de özür dilemen gerektiğini düşünmüyor musun?"
    show monika at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1x "Nnn...!"
    show natsuki at t22 zorder 2
    "Natsuki yumruklarını sıkıyor."
    "Sonunda, kimse onun tarafını tutmadı."
    "Kapana kısıldı, bu noktada sadece baskıya dayanamadığı için meydan okuyor."
    "Sonunda onun için üzülüyorum bile."
    show monika at t32 zorder 2
    show natsuki at t33 zorder 2
    show sayori 2h at l41
    s "U-Um!"
    s "Bazen incindiğimde..."
    s "Yürüyüş yapmak ve kafamı boşaltmak iyi geliyor!" #Sen ne güzel sözler söylüyorsun öyle
    show sayori at t41 zorder 2
    mc "Sayori, buna ihtiyacı yok--"
    show natsuki at f33 zorder 3
    n 2q "Biliyor musun?"
    n "Bunu yapacağım."
    n 2w "Bu beni şu anda hepinizin yüzüne bakmak zorunda kalmaktan kurtaracak."
    show natsuki at thide zorder 1
    hide natsuki
    "Natsuki hiçbir uyarıda bulunmadan kendi şiirini masadan kaptığı gibi dışarı fırladı."
    "Çıkarken şiiri elleriyle buruşturup çöpe atıyor." #herkesi memnun etmek imkansızdır. Fedakarlık yapmak gerekebilir.
    show sayori at f41 zorder 3
    s 1k "Natsuki..."
    show sayori at t41 zorder 2
    show monika at f32 zorder 3
    m 1r "Gerçekten bunu yapmasına gerek yoktu..."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    hide sayori
    hide monika
    "Odanın diğer ucuna bakıyorum."
    "Yuri çenesini ellerinin arasına almış, masasına bakıyor."
    "Ona yavaşça yaklaşıp bitişikteki sandalyeye oturuyorum."
    show yuri 4b at t11 zorder 2
    y "İç çek..."
    mc "Her şey yolunda mı?"
    y "Çok utandım..."
    y "Böyle davrandığıma inanamıyorum."
    y "Muhtemelen şimdi benden nefret ediyorsundur..."
    mc "Hayır--Yuri!"
    mc "Böyle bir muameleye maruz kaldıktan sonra insan nasıl sinirlenmez?"
    mc "Herkesin yapabileceği kadar iyi idare ettin."
    mc "Senin hakkında daha azını düşünmüyorum."
    y 2v "Şey..."
    y "...Pekala, sana inanıyorum."
    y 2s "Teşekkürler, [player]. Çok naziksiniz."
    y "Artık bu kulübün bir parçası olduğun için minnettarım."
    mc "Önemli değil."
    y 2v "Bir şey daha..."
    y "Um, Natsuki'nin söylediği bir şey..."
    y 4c "Hakkında... bilirsin..."
    y "Ben asla böyle utanç verici bir şey yapmam..."
    y "Yani..."
    mc "...Eh?"
    mc "Natsuki ne dedi?"
    y 3n "--!"
    y "U-Um!"
    y 3q "Neyse, boş ver..."
    y "Ben gidip biraz çay yapacağım..."
    mc "Ah, iyi fikir."
    mc "Birden fazla kişiye yetecek kadar yap, tamam mı?"
    y "Evet."
    return

label ch1_end_sayori:
    $ ch1_choice = "sayori"
    mc "N-Natsuki..."
    show natsuki 5f
    "Natsuki bana ters ters bakarak ağzımdaki tüm kelimeleri kuruttu."
    "Onun yerine Yuri'ye döndüm."
    mc "Yuri..."
    y 4a "..."
    "Ama Yuri'nin ifadesi o kadar savunmasız ki ona bir şey söylemeye cesaret edemiyorum."
    stop music fadeout 1.0
    mc "..."
    mc "...Sayori!"
    show sayori 4m at l31 behind yuri
    show yuri at t32 zorder 2
    show natsuki at t33 zorder 2
    s "Eh?!"
    mc "...Evet!"
    mc "Herkesin kavga etmesi Sayori'yi rahatsız ediyor."
    mc "Arkadaşınızı bu şekilde hissettirdiğinizi bile bile nasıl kavga etmeye devam edebiliyorsunuz?"
    show sayori at f31 zorder 3
    s 4d "[player]..."
    show sayori at t31 zorder 2
    show natsuki 4w at f33 zorder 3
    n "Şey... Bu onun sorunu! Bu onunla ilgili değil."
    show natsuki at t33 zorder 2
    show yuri 2g at f32 zorder 3
    y "Katılıyorum..."
    y "Başkalarının kendi duygularını anlaşmazlığımıza karıştırması haksızlık." #Beni niye kattınız lan o zaman kaygaya
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    n 4c "Evet, tabii Sayori Yuri'ye ne kadar kibirli bir pislik olduğunu söylemek istemiyorsa."
    show natsuki at t33 zorder 2
    show yuri 3r at f32 zorder 3
    play music t7
    y "O asla...!"
    y "Onu en başta üzen senin olgunlaşmamışlığın!"
    show yuri at t32 zorder 2
    show natsuki 1e at f33 zorder 3
    n "{i}Bahane.{/i}"
    n "Kendini dinliyor musun?"
    n 1x "İşte tam da bu yüzden..."
    n 1w "Tam da bu yüzden kimse--"
    show natsuki at t33 zorder 2
    show sayori 4p at h31
    stop music
    s "{i}Durun!!{/i}"
    show yuri 3f at f32 zorder 3
    show natsuki 1o at f33 zorder 3
    ny "--"
    show yuri at t32 zorder 2
    show natsuki at t33 zorder 2
    show sayori at f31 zorder 3
    play music t8
    s 1h "Natsuki! Yuri!"
    s "Sizler benim arkadaşlarımsınız!"
    s 1v "Ben sadece herkesin iyi geçinmesini ve mutlu olmasını istiyorum!"
    s "Arkadaşlarım harika insanlar..."
    s "Ve ben onları farklılıklarından dolayı seviyorum!"
    s 1g "Natsuki'nin şiirleri..."
    s "Harikalar çünkü sadece birkaç kelimeyle insana pek çok şey hissettiriyorlar!"
    s "Ve Yuri'nin şiirleri harika çünkü kafanızda güzel resimler çiziyorlar!"
    s 4k "Herkes çok yetenekli..."
    s "...Öyleyse neden kavga ediyoruz...?" #Ah Canım bebeğim, buradaki EQ'su yüksek bir sensin galiba. 
    show sayori at t31 zorder 2
    show natsuki at f33 zorder 3
    n 1r "Ç-çünkü..."
    show natsuki at t33 zorder 2
    show yuri 3v at f32 zorder 3
    y "Şey..."
    show yuri at t32 zorder 2
    show sayori at f31 zorder 3
    s 1j "Ayrıca!"
    s "Natsuki sevimli ve bunda yanlış bir şey yok!"
    s 1i "Ve Yuri'nin göğüsleri her zaman olduğu gibi aynı!" #SJKIOSJIOSEOIJOISEHJOIE
    show sayori at hf31
    s 1j "Kocaman ve güzel!!" #LA SAYORİ RKOGPOSRDKHRD AŞKIMM NAPIYOSUN. Yok ya ben kıvamında seviyorum Sayori'ninkiler mesela.
    show sayori 1i at t31 zorder 2
    show natsuki at f33 zorder 3
    n 1o "..."
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 3n "..."
    show yuri at t32 zorder 2
    mc "Sayori..."
    "Sayori zaferle ayakta duruyor."
    "Monika şaşkın bir ifadeyle arkasında duruyor."
    show yuri at s32
    y 3q "Ben... çay yapacağım..."
    show yuri at lhide behind sayori
    hide yuri
    "Yuri aceleyle gidiyor."
    show natsuki at thide zorder 1
    hide natsuki
    "Natsuki yüzünde boş bir ifadeyle oturur ve hiçbir şeye bakmaz."
    show sayori at thide zorder 1
    show monika 1i at t11 zorder 2
    hide sayori
    mc "Demek Sayori bu yüzden Başkan Yardımcısı."
    "Monika'ya fısıldıyorum."
    "O da başını sallıyor."
    m 1d "Dürüst olmak gerekirse..."
    m "İyi bir lider olarak görünebilirim ve işleri organize edebilirim..."
    m 3e "Ama insanlarla aram pek iyi değil..."
    m "Kendimi araya girmeye bile ikna edemedim."
    m 1m "Başkan olarak bu benim için biraz utanç verici."
    m 1l "Ahaha..."
    mc "Hayır..."
    mc "Seni suçlayamam."
    mc "Ben de bir şey söyleyemedim."
    m "Şey..."
    m 2a "Sanırım bu Sayori'nin kendi tarzında harika olduğu anlamına geliyor, değil mi?"
    mc "Öyle de denebilir."
    mc "Boş kafalı olabilir ama bazen ne yaptığını çok iyi bildiğine dair garip bir şüphe oluşuyor."
    m 5 "Anlıyorum~"
    m "Ona iyi bak, tamam mı?"
    m "Kendine zarar verdiğini görmekten nefret ederim."
    mc "Bu ikimizi yapar..."
    mc "Bana güvenebilirsin."
    "Monika bana tatlı tatlı gülümseyerek midemin düğümlenmesine neden oldu."
    "Ne derse desin, böylesine samimi bir insan gerçekten de iyi bir Başkan olur."
    "Keşke onunla biraz daha fazla konuşma fırsatı bulabilseydim..." #AAAAAAAA TEK GERÇEK SAYORİ ULAAN!
    return
