# Chapter 2 static content. Poem responses called from here are in script-poemresponses.rpy

label ch2_main:
    scene bg club_day
    with dissolve_scene_half
    play music t2
    "Bir gün daha geçti ve kulüp toplantısı zamanı geldi bile."
    "Son birkaç gündür burada biraz daha rahatım."
    "Kulüp odasına girdiğimde beni her zamanki manzara karşılıyor."
    show sayori 2x at t11 zorder 2
    s "Selamunaleyküm [player]~"
    mc "Aleykümselam, Sayori."
    mc "Bugün keyfin yerinde gibi görünüyor."
    s 1q "Ehehe~"
    s "Sadece hala kulüpte olmana alışamadım, hepsi bu."
    mc "Anlıyorum..."
    mc "...Bu seni iyi bir ruh haline sokmak için oldukça basit bir şey."
    mc "Ama sanırım sende her zaman basit şeyler oluyor."
    s 1d "Lafı açılmışken..."
    s "Biraz acıktım..."
    s "Atıştırmalık bir şeyler almak için benimle gelir misin?"
    mc "Hayır, teşekkürler."
    s 4h "Eh?"
    s "Bu hiç sana göre değil!!"
    mc "Kendimce sebeplerim var."
    mc "Neden çantana bir göz atmıyoruz, Sayori?"
    s 4l "E-Eh?"
    show sayori at s11
    "Neden... birdenbire?"
    mc "Sebebi yok, gerçekten."
    mc "Sadece bakmak istedim."
    s 1l "A-Ah..."
    show sayori at t11 zorder 2
    "Sayori sinirli bir şekilde bozuk para cüzdanını alıyor."
    "Mandalını kurcalıyor ve açıyor."
    "Sonra, ters çevirdi ve içindekilerin masanın üzerine dökülmesine izin verdi."
    "Sadece iki küçük bozuk para düşer." #Ben öderim aşkım
    s 5a "A-Ahaha..."
    mc "Biliyordum..."
    mc "Senin içini görebiliyorum, Sayori."
    s 5c "Bu hiç adil değil!"
    s "Nereden bildin ki?"
    mc "Çok basit."
    mc "Yeterince paran olsaydı, kulüp odasına gelmeden önce atıştırmalık bir şeyler alırdın."
    mc "Yani, ya aç değilsiniz ve yürüyüş yapmak için bir bahane aradınız..."
    mc "Ya da tüm paranı harcadığını unutup sana biraz borç vermemi planladın!"
    mc "Ama bir şey daha var..."
    mc "...Sen her zaman açsın!"
    mc "Ve böylece geriye tek bir seçenek kalıyor!"
    s 4p "Uwaaa~!"
    s "Pes ediyorum!"
    s "Beni suçlu hissettirme!"
    mc "Suçlu hissediyorsan, suçlu hissetmeyi hak ediyorsun demektir..." #Eueueueu
    show yuri 1c at t33 zorder 2
    y "Ahaha."
    "Yuri aniden kıkırdadı."
    show sayori 4g
    mc "Eh?"
    "Dinlediğini fark etmedim."
    "Yüzü her zamanki gibi kitabının içinde."
    show yuri 3n at h33
    y "A-Ah!"
    y "Dinlemiyordum ya da başka bir şey--!"
    y 3o "Sadece... kitabımdaki bir şeydi..."
    show sayori at f32 zorder 3
    s 1h "Yuriiii..."
    s "Söyle [player] bana biraz para ödünç versin..."
    show sayori at t32 zorder 2
    show yuri at f33 zorder 3
    y 3h "Bu--!"
    y "Beni bu işe bulaştırma, Sayori..."
    y "Ayrıca..."
    y 1k "Sadece karşılayabileceğin şeyleri satın almalısın..."
    y "Ve açıkçası, böyle küçük bir yaramazlık yaptıktan sonra, çektiğin acı yeterince adil bir ceza."
    show sayori 1b
    mc "..."
    y 3n "Ah--!"
    y "Ben az önce..."
    y 4c "Öyle demek istemedim!!"
    y "Kitabıma çok dalmışım..."
    y "Uu..."
    show yuri at t33 zorder 2
    show sayori at f32 zorder 3
    s 1r "Ahaha!"
    s 3x "Aklından geçenleri söylemeni gerçekten seviyorum, Yuri..."
    s "Çok fazla olmuyor ama bu senin eğlenceli bir yönün!"
    show sayori at t32 zorder 2
    show yuri at f33 zorder 3
    y 3v "Bu..."
    y "Bunu düşünebilmenin imkanı yok..."
    show yuri at t33 zorder 2
    show sayori at f32 zorder 3
    s 1x "Yinede haklısın..."
    s "Kötü bir şey yaptım ve şimdi devrimi kabul etmek zorundayım."
    show sayori at t32 zorder 2
    show yuri at f33 zorder 3
    y 3h "Cezalandırma."
    show yuri at t33 zorder 2
    show sayori at f32 zorder 3
    s 1l "Bu!"
    show sayori at t32 zorder 2
    show yuri at f33 zorder 3
    y "Hala, senden geliyor, Sayori..."
    y 1a "Sanırım hepimizin içinde küçük bir şeytan var, değil mi?"
    show yuri at t33 zorder 2
    show sayori at f32 zorder 3
    s 1q "Ehehe..."
    show sayori at t32 zorder 2
    mc "Sizi kandırmasına izin vermeyin."
    mc "Sayori ne yaptığını çok iyi biliyor."
    mc "Ne de olsa daha bana söylemeden beni kulübe getireceğini size söylemişti..." #KIZMA LAN KÜÇÜK ŞEYTANIMA
    show sayori at f32 zorder 3
    s 1h "Ama...!"
    s "Kekler olmasaydı gelmezdin..."
    s "Bu yüzden Natsuki'yi onları yapması için kandırmak zorunda kaldım!"
    show sayori at t32 zorder 2
    mc "Hadi ama, bana bundan daha fazla kredi ver, Sayori."
    show sayori at f32 zorder 3
    s 1l "Ehehe..."
    play sound "sfx/slap.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show sayori 4p at hf32 zorder 3
    "{i}TAK!{/i}"
    hide white
    s 4p "Kyaa--!"
    "Birdenbire Sayori'nin yüzüne bir şey çarptı ve masanın üzerine yuvarlandı."
    s 4j "Ow..."
    s "Neydi--"
    s 4n "Eh?"
    s "Bir kurabiye!"
    "Elbette, plastiğe sarılmış dev bir kurabiye."
    "Sayori etrafına bakar."
    s 4m "Bu bir mucize mi?"
    s "tazminatımı ödedim!"
    show sayori at t32 zorder 2
    mc "Ceza..."
    show sayori 4n
    show yuri at f33 zorder 3
    y 1u "Aslında bu neredeyse işe yarıyordu..."
    show yuri at t33 zorder 2
    show natsuki 3z at f31 zorder 3
    n "Ahahaha!"
    n "Sadece {i}sana{/i} verecektim."
    n 3d "Ama sonra keklerle ilgili gevezelik ettiğini duydum."
    n "Yine de tepkini görmeye değerdi. Ahaha!"
    show natsuki at t31 zorder 2
    show sayori at f32 zorder 3
    s 4m "N-Natsuki!"
    s "Çok naziksin!"
    s 4s "Çok mutluyum..."
    "Sayori kurabiyeyi kucaklıyor."
    show sayori at t32 zorder 2
    mc "Tanrım, ye şunu..."
    "Sayori ambalajı hızla yırtar ve büyük bir ısırık alır."
    show sayori at f32 zorder 3
    s 4q "Coh güvel..."
    show sayori at hf32 zorder 3
    s 4o "Mmf--!"
    "Sayori aniden elleriyle ağzına kapatır."
    s 4p "Dilimi ısırdım."
    show sayori at t32 zorder 2
    show natsuki at f31 zorder 3
    n 3a "Ehehe."
    n "Sadece bir kurabiye için çok şey yaşıyorsun."
    "Natsuki kendi kurabiyesinden bir ısırık aldı."
    show natsuki at t31 zorder 2
    show sayori at f32 zorder 3
    s 1c "Ah, seninki de gerçekten güzel görünüyor, Natsuki!"
    s "Deneyebilir miyim?"
    show sayori at t32 zorder 2
    show natsuki at f31 zorder 3
    n 4e "Tanrım..."
    n "Dilenciler seçici olamaz!"
    show natsuki at t31 zorder 2
    show sayori at f32 zorder 3
    s 1h "Ama seninki çikolatalı..."
    show sayori at t32 zorder 2
    show natsuki at f31 zorder 3
    n 4c "Evet, neden sana bunu verdiğimi sanıyorsun?"
    show natsuki at t31 zorder 2
    show sayori at f32 zorder 3
    s 1g "İyi..."
    s 1q "Yine de bunu benimle paylaştığın için çok mutluyum."
    s "Ehehe~"
    show sayori at t21 zorder 2 behind natsuki
    "Sayori oturduğu yerden kalkıp Natsuki'nin arkasına geçti ve kollarını ona doladı."
    n 12c "Ah-- Tanrım..."
    n "Anladım, anladım."
    "Kurabiye hala elinde, Natsuki Sayori'yi itmek için uzanıyor."
    show sayori 1n at h21
    s "...{i}Om.{/i}"
    "Sayori aniden eğilir ve Natsuki'nin kurabiyesinden bir ısırık alır."
    n 1p "{i}H-Hey!!{/i}"
    n "Bunu cidden yaptın mı?!"
    s 1q "Uhuhuhu!"
    show sayori at lhide
    hide sayori
    "Ağzı dolu olan Sayori güvenli bir yere doğru koşar." #KJGIRHIORH KOLLARIMA MI???
    show yuri 1c
    "Yuri ve ben de gülüyoruz."
    show yuri 1a
    show natsuki at f31 zorder 3
    n 1w "Tanrım! Bazen tam bir çocuk oluyorsun!"
    n 1h "Monika! Sayori'ye söyler misin-"
    n 1c "--Eh?"
    "Natsuki etrafına bakar."
    "Monika kulüp odasında değil."
    n 4q "Ugh..."
    n "Monika nerede bu arada?"
    show natsuki at t31 zorder 2
    show yuri 2f at f33 zorder 3
    y "Güzel soru..."
    y "Bugün geç kalmasıyla ilgili herhangi bir şey duydunuz mu?"
    show sayori 1b at f32 zorder 3
    show yuri at t33 zorder 2
    s "Ben Hayır..."
    show sayori at t32 zorder 2
    mc "Evet, ben de görmedim."
    show yuri at f33 zorder 3
    y 2l "Hm..."
    y "Bu biraz alışılmadık."
    show yuri at t33 zorder 2
    show sayori at f32 zorder 3
    s 1g "Umarım iyidir."
    show sayori at t32 zorder 2
    show natsuki 3k at f31 zorder 3
    n "Tabii ki iyi."
    n "Muhtemelen bugün yapacak bir işi vardı."
    n 3t "Ne de olsa oldukça popüler..."
    show natsuki at t31 zorder 2
    show sayori 4m at f32 zorder 3
    s "Eh?"
    s "Sence o..."
    s "Onun bir...!"
    show sayori at t32 zorder 2
    show yuri 1a at f33 zorder 3
    y "Ahaha. Şaşırmazdım."
    y "Muhtemelen hepimizin toplamından daha çekici."
    show yuri at t33 zorder 2
    show sayori 1r at f32 zorder 3
    s "Ehehe, bu doğru..." #ahahaha yanlış birşeye doğru dediğin için çok tatlısın Sayori. EN ÇEKİCİ SENSİN KİM OLUCAK?!
    show sayori at t32 zorder 2
    show natsuki 1p at f31 zorder 3
    n "Affedersin?!"
    hide natsuki
    hide sayori
    hide yuri
    with wipeleft
    "Aniden kapı açılır."
    show monika 1g at l41
    m "Özür dilerim! Çok özür dilerim!"
    mc "Ah, işte buradasın..."
    m "Geç kalmak istememiştim..."
    m "Umarım endişelenmemişsinizdir!"
    show sayori 4n at f42 zorder 3
    s "Ne?"
    s "Monika erkek arkadaşı yerine kulübü seçti!"
    s "Çok iradeli birisin!"
    show sayori at t42 zorder 2
    show monika at f41 zorder 3
    m 1l "Erkek arkadaş...?"
    m "Sen neden bahsediyorsun?"
    "Monika şaşkınlıkla bana bakıyor."
    show monika at t41 zorder 2
    mc "Ah, boş ver onu..." #eğer boş vericekseniz bana verebilirmisiniz? Sayori'yi?
    mc "Seni tutan neydi?"
    show monika at f41 zorder 3
    m 1e "Ah..."
    m "Bugün son dersim etüt salonuydu."
    m "Dürüst olmak gerekirse, zamanın nasıl geçtiğini anlamadım..."
    m "Ahaha..."
    show monika at t41 zorder 2
    show natsuki 2c at f43 zorder 3
    n "Yine de bu hiç mantıklı değil."
    n "En azından zilin çaldığını duyardınız."
    show natsuki at t43 zorder 2
    show monika at f41 zorder 3
    m 1m "Piyano çalıştığım için duymamış olmalıyım..."
    show monika at t41 zorder 2
    show yuri 1e at f44 zorder 3
    y "Piyano...?"
    y "Senin müzikle uğraştığını bilmiyordum, Monika."
    show yuri at t44 zorder 2
    show monika at f41 zorder 3
    m 1l "Ah, bilmiyorum, gerçekten...!"
    m "Daha yeni başladım sayılır."
    m 1m "Her zaman piyano öğrenmek istemişimdir."
    show monika at t41 zorder 2
    show sayori 4x at f42 zorder 3
    s "Bu çok havalı!"
    s "Bizim için bir şeyler çalmalısın, Monika!"
    show sayori at t42 zorder 2
    show monika at f41 zorder 3
    m "Bu..."
    "Monika bana bakıyor." #Yeterla
    m 1a "Belki biraz daha iyi olduğumda bunu yaparım."
    show monika at t41 zorder 2
    show sayori at f42 zorder 3
    s 4q "Yay~!"
    show sayori at t42 zorder 2
    mc "Kulağa hoş geliyor."
    mc "Ben de dört gözle bekliyorum."
    show monika at f41 zorder 3
    m 1b "Öyle mi?"
    m "Bu durumda..."
    m "Seni hayal kırıklığına uğratmayacağım, [player]."
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    show yuri at thide zorder 1
    show monika 5 at t11 zorder 2
    hide sayori
    hide natsuki
    hide yuri
    "Monika tatlı tatlı gülümser."
    mc "Ah..."
    mc "Baskı falan yapmak istememiştim!"
    m 1a "Ahaha, endişelenme."
    m "Son zamanlarda çok fazla pratik yapıyorum."
    m "Ve hazır olduğumda paylaşma şansını gerçekten çok isterim."
    mc "Anlıyorum..."
    mc "Bu durumda, iyi şanslar."
    m 1j "Teşekkürler~!"
    m 1a "Yani, bir şey kaçırmadım, değil mi?"
    mc "Hayır... pek sayılmaz."
    show monika at thide zorder 1
    hide monika
    "Sayori'nin yaramaz kaçışını atlamayı tercih ediyorum."
    "Natsuki'nin sonunda onu şikayet edeceğinden eminim."
    "Görünüşe göre herkes çoktan yerleşmiş."
    "Sayori bir şekilde tüm kurabiyesini bitirdi bile."
    "Yuri kitabına geri döndü ve Natsuki dolabın içinde kayboldu."
    
    #Call exclusive scene
    $ nextscene = poemwinner[1] + "_exclusive_" + str(eval(poemwinner[1][0] + "_appeal"))
    call expression nextscene

    #After exclusive scene, we go back to poem responses

    return


label ch2_end:
    stop music fadeout 1.0
    scene bg club_day
    show monika 4b at t32 zorder 2
    with wipeleft_scene
    play music t3
    m "Tamam, millet!"
    m "Hepimiz birbirimizin şiirlerini okumayı bitirdik, değil mi?"
    m "Bugün için ekstra bir planım var, o yüzden herkes gelip odanın ön tarafına oturabilirse..."
    show natsuki 3c at f31 zorder 3
    n "Festivalle mi ilgili?"
    show natsuki at t31 zorder 2
    show monika 1j at f32 zorder 3
    m "Şey, sayılır~"
    show monika 1a at t32 zorder 2
    show natsuki 1m at f31 zorder 3
    n "Ugh. Festival için gerçekten bir şeyler yapmak zorunda mıyız?"
    n "Sadece birkaç gün içinde iyi bir şey hazırlayabileceğimiz yok."
    n "Yeni üyeler kazanmak yerine kendimizi utandıracağız."
    show yuri 2g at f33 zorder 3
    show natsuki at t31 zorder 2
    y "Bu benim de endişelerimden biri."
    y "Son dakika hazırlıklarıyla aram pek iyi değildir..."
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 1b "Bu kadar endişelenme!"
    m "Basit tutacağız, tamam mı?"
    m 1a "Birkaç süslemeden fazlasına ihtiyacımız olmayacak."
    m "Sayori posterler üzerinde çalışıyor ve ben de etkinlik sırasında dağıtabileceğimiz bazı broşürler tasarladım."
    show monika at t32 zorder 2
    show natsuki 3c at f31 zorder 3
    n "Tamam, bu harika ve hepsi..."
    n "Ama bu bize etkinlik için gerçekte ne yapacağımızı söylemiyor."
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 1d "Ah, sorry! I thought you heard about it already."
    m 1b "Gösteri yapacağız!"
    show monika at t32 zorder 2
    show natsuki at f31 zorder 3
    n 3h "Gösteri?"
    show natsuki at t31 zorder 2
    show yuri at f33 zorder 3
    y 3n "P..."
    y 3o "Um, Monika..."
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 1k "Evet! Bir şiir gösterisi gerçekleştireceğiz."
    m 1b "Her birimiz etkinlik sırasında okumak üzere bir şiir seçeceğiz."
    m "Ama işin güzel yanı, başkalarının da gelip şiir okumasına izin vereceğiz!"
    m 1a "Sayori, önceden hazırlanmak isteyen olursa diye tüm afişlere bunu yazıyor."
    show yuri at t44 zorder 2
    show monika at t43 zorder 2
    show natsuki at t42 zorder 2
    show sayori 4q at l41
    s "Ehehe~"
    "Bir posteri boyamakta olan Sayori, görmemiz için posteri havada tutuyor."
    show natsuki 4w at f42 zorder 3
    n "Benimle dalga mı geçiyorsun, Monika?"
    n "Sen... sen o posterleri asmaya başlamadın, değil mi?"
    show natsuki at t42 zorder 2
    show monika at f43 zorder 3
    m 1d "Eh? Şey, ben yaptım..."
    m "Bunun gerçekten o kadar kötü bir fikir olduğunu mu düşünüyorsun...?"
    show monika at t43 zorder 2
    show natsuki 1s at f42 zorder 3
    n "Şey, hayır."
    n "Kötü bir fikir değil."
    n 1w "Ama ben bunun için kaydolmadım, biliyorsun!"
    n 1x "Böyle bir grup insanın önünde sahne almamın {i}hiç{/i}bir yolu yok!"
    show natsuki at t42 zorder 2
    show yuri at f44 zorder 3
    y 3r "Ben...Natsuki'ye katılıyorum!"
    y 3w "Ben asla... hayatımda... böyle bir şey yapamam..."
    "Bunu hayal eden Yuri korku içinde başını sallar."
    show yuri at t44 zorder 2
    show sayori 1g at f41 zorder 3
    s "Millet..." #Sayori...
    show sayori at t41 zorder 2
    show monika at f43 zorder 3
    m 1g "Hayır, Sayori..."
    m "Nereden geldiklerini anlıyorum."
    m "Natsuki ve Yuri'nin birkaç gün öncesine kadar şiirlerini hiç kimseyle paylaşmadıklarını unutmayın..."
    m "Onlardan şiirlerini bir oda dolusu insana yüksek sesle okumalarını istemek çok fazla."
    m 1r "Sanırım bunu gözden kaçırmışım."
    m "O yüzden özür dilerim."
    show monika at t43 zorder 2
    show natsuki 5g at f42 zorder 3
    n "..."
    show natsuki at t42 zorder 2
    show monika at f43 zorder 3
    m 1i "...Ama!"
    m "Ben hala elimizden gelenin en iyisini yapmamız gerektiğini düşünüyorum!"
    m 1d "Bu kulübün kaderinden sadece biz sorumluyuz."
    m "Eğer etkinliğe başlarsak ve her birimiz iyi bir performans sergilersek..."
    m 3a "O zaman bu diğerlerine de aynı şeyi yapmaları için ilham verecektir!"
    m "Ve ne kadar çok kişi performans sergilerse, edebiyatın ne demek olduğunu herkese o kadar iyi gösterebiliriz!"
    show monika at t43 zorder 2
    show sayori 1r at f41 zorder 3
    s "Evet!"
    s 1x "Bu duygularınızı ifade etmekle ilgili..."
    s "Kendinle samimi olmak..."
    s "Yeni ufuklar bulmak..."
    s "Ve eğlenmek!" #Eğlenmek ha? Eğlenmeyi cidden çok seviyorsun Sayori. Bütün hepsinin sonucunda Eğlenmeyen sen olsan bile.
    show sayori at t41 zorder 2
    show monika at f43 zorder 3
    m 4b "Bu doğru!"
    m "İşte bu nedenlerle bugün hepimiz bu kulüpteyiz."
    m 4e "Bunu başkalarıyla paylaşmak istemez misiniz?"
    m "Sizi buraya getiren duyguların aynısını bulmaları için onlara ilham vermek?"
    m 1e "İstediğini biliyorum."
    m "Hepimizin istediğini biliyorum."
    m 1b "Ve eğer tek gereken odanın önünde iki dakika durup bir şiir okumaksa..."
    m "...O zaman bunu yapabileceğini biliyorum!"
    show monika 1a at t43 zorder 2
    show natsuki 5s at f42 zorder 3
    n "..."
    show natsuki at t42 zorder 2
    show yuri 4b at f44 zorder 3
    y "..."
    show yuri at t44 zorder 2
    show sayori 1g
    "Natsuki ve Yuri sessizliğini koruyor."
    "Sayori endişeli görünüyor."
    "Sanırım bu bana başka seçenek bırakmıyor..."
    mc "Katılıyorum..."
    mc "Çok şey istediğimi sanmıyorum."
    mc "Sayori ve Monika'nın yeni üyeler kazanmak için gerçekten çok uğraştıklarını düşünüyorum."
    mc "En azından onlara biraz yardımcı olabiliriz."
    show natsuki at f42 zorder 3
    n 5h "Şey... belki, ama..."
    n "..."
    "Görünüşe göre Natsuki'nin hiç argümanı kalmamış."
    n "Uu..."
    n 1q "...Tamam, iyi!"
    n "Sanırım bu işi halletmem gerekecek."
    show natsuki at t42 zorder 2
    show sayori at f41 zorder 3
    s 4r "Pekala~!"
    show sayori 4a at t41 zorder 2
    show monika at f43 zorder 3
    m 1e "Phew..."
    m "Teşekkürler, Natsuki."
    m "Peki ya sen, Yuri...?"
    show monika at t43 zorder 2
    show yuri at f44 zorder 3
    y "..."
    "Yuri kederli bir ifadeyle etrafına, diğer herkesin beklenti içindeki yüzlerine bakar."
    y "Ah..."
    y "Sanırım başka seçeneğim yok..."
    show yuri at t44 zorder 2
    show sayori at f41 zorder 3
    s 4r "Ahaha! işte bu kadar!"
    "Sen en iyisisin, Yuri.~"
    show sayori 4a at t41 zorder 2
    show yuri at f44 zorder 3
    y "Bu kulüp cidden beni öldürecek..."
    show yuri at t44 zorder 2
    show monika at f43 zorder 3
    m 1l "Tanrım..."
    m 1n "İyi olacaksın, Yuri."
    m "Ama her neyse..."
    m 1b "Asıl etkinliğe geçelim!"
    m "Her birinizden bir şiir seçmenizi istiyorum."
    m "Birbirimizin önünde okuyarak pratik yapacağız."
    show monika 1a at t43 zorder 2
    show natsuki at f42 zorder 3
    n 1p "Hayatta olmaz!!"
    show natsuki at t42 zorder 2
    show yuri 3n at f44 zorder 3
    y "Monika...!"
    y "Bu çok ani oldu...!"
    show yuri at t44 zorder 2
    show monika at f43 zorder 3
    m 2a "Kulübün önünde şiirinizi okuyamıyorsanız, yabancıların önünde bunu nasıl yapmayı bekliyorsunuz?"
    show monika at t43 zorder 2
    show yuri 4c at f44 zorder 3
    show natsuki 1o
    y "ah olamaz..."
    show yuri at t44 zorder 2
    show monika at f43 zorder 3
    m 2a "Merak etmeyin."
    m "Herkesin biraz daha rahat hissetmesine yardımcı olmak için başlayacağım."
    show monika at t43 zorder 2
    show sayori 1r at f41 zorder 3
    s "Sıradaki ben olabilir miyim?"
    show sayori at t41 zorder 2
    show monika at f43 zorder 3
    m "Ahaha. Elbette."
    m 2d "Şimdi, bakalım..."
    "Monika defterini karıştırarak kendisi için düşündüğü özel şiire ulaşır."
    "Sonra podyumun arkasında durur."
    show monika at t11 zorder 2
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    show yuri at thide zorder 1
    hide sayori
    hide natsuki
    hide yuri
    m 1a "Bu şiirin başlığı {i}Uçtukları Yol{/i}."
    m 1r "Ahem..."
    show monika 1a
    "Monika şiirini okumaya başladı."
    "Berrak, kendinden emin sesi odayı dolduruyor."
    "Dahası, ses tonu kusursuz."
    "Okuduğu her satırın ardındaki duyguyu nasıl kullanacağını çok iyi biliyor ve kelimelere hayat veriyor."
    "Bu daha önce yaptığı bir şey mi, yoksa doğal mı?"
    "Etrafıma bakıyorum."
    "Herkesin gözü Monika'da."
    "Sayori şaşırmış görünüyor."
    "Yuri'nin yüzünde anlam veremediğim yoğun bir ifade var."
    show monika 1j
    "Sonunda Monika okumayı bitirdi."
    "Dördümüz alkışlıyoruz."
    "Monika nefes alır ve gülümser."
    show monika 1a
    show sayori 4m at f33 zorder 3
    s "Bu... bu çok iyiydi, Monika!"
    show sayori at t33 zorder 2
    show monika at f32 zorder 3
    m 1j "Ahaha, çok teşekkür ederim."
    m 1a "Sadece iyi bir örnek olmayı umuyordum."
    m "Sıradaki için hazır mısın, Sayori?"
    show monika at t32 zorder 2
    show yuri 2r at l31
    y "Ben... Sıradaki benim!!"
    show sayori at h33
    s 1n "Uwah! Yuri aniden ateşlendi!"
    "Yuri ellerinin arasında bir kağıt tutuyor ve ayağa kalkıyor."
    "Başını eğerek, hızla podyuma doğru yürüyor."
    show monika at thide zorder 1
    show sayori at thide zorder 1
    show yuri at t11 zorder 2
    hide monika
    hide sayori
    y 2v "Bu şiirin adı--!"
    "Yuri endişeyle her birimize bakıyor."
    s "Yapabilirsin, Yuri..."
    y "Adı...{i}Kızıl Gözün Ardıl Görüntüsü{/i}."
    "Yuri şiiri okumaya başlarken sesi titriyor."
    "Daha bir dakika önce bunu yapmayı neredeyse reddediyordu."
    "Neden birden bu kadar çaba sarf etmeye başladı?"
    show yuri 2l
    "Yuri ilk birkaç satırı geçtikçe sesi değişiyor."
    "Neredeyse Yuri kitaplarına daldığında olanlara benziyor."
    "Titreyen sözcükleri sert ve kendinden emin bir kadının keskin hecelerine dönüşüyor."
    "Şiirin yapısı, mükemmel bir zamanlamayla telaffuz ettiği kıvrımlar ve dönüşlerle dolu."
    "Bu, Yuri'nin kafasının içinde sakladığı dönen ateşe nadir bir bakış olmalı...!"
    show yuri 2t
    "Birdenbire işi bitti."
    "Herkes şaşkına döndü."
    "Yuri gerçekliğe geri döner ve sanki kendisi bile şaşırmış gibi etrafına bakar."
    y 3o "Ben..."
    "...Bu durumu kurtarmak bana bağlı."
    "Alkışlamaya ilk ben başlıyorum."
    "Daha sonra herkes bana katıldı ve Yuri'ye hak ettiği takdiri verdik."
    "Onu alkışlamak istemediğimizden değil."
    "Ama o kadar hazırlıksız yakalandık ki unutmuş olmalıyız."
    "Biz alkışlarken Yuri şiiri göğsüne bastırdı ve aceleyle koltuğuna geri döndü."
    show yuri at lhide
    hide yuri
    show monika 1a at t11 zorder 2
    m "Yuri, bu gerçekten çok iyiydi."
    m "Paylaştığın için teşekkürler."
    y "..."
    "Görünüşe göre Yuri sayım için düştü..."
    show sayori 1q at t31 zorder 2
    s "Okaay~"
    "Sanırım sırada ben varım!"
    "Sayori sandalyesinden zıplar ve neşeyle podyuma doğru yürür."
    show sayori at t11 zorder 2
    show monika at thide zorder 1
    hide monika
    s 1x "Bunun adı...{i}Benim Çayırım{/i}."
    s "Ah..."
    s 1s "...Ahaha!"
    s 4s "Üzgünüm, kıkırdadım..."
    s 4q "Ehehe..."
    mc "Sayori..."
    s 1l "Düşündüğümden çok daha zormuş!"
    s "Nasıl bu kadar kolay yaptınız?"
    show monika 3a at t31 zorder 2
    show sayori 1b
    m "Ah..."
    m "Bunu başkalarına okuyormuş gibi düşünmemeye çalış."
    m "Kendinize okuduğunuzu hayal edin, bir aynanın karşısında ya da kendi kafanızın içinde."
    m "Bu senin şiirin, o yüzden en iyisi bu şekilde ortaya çıkacak."
    show sayori 1i
    s "Anladım, Anladım..."
    s "Tamam, o zaman..."
    show monika at thide zorder 1
    hide monika
    show sayori 1c
    "Sayori şiirine başlıyor."
    "Bir şekilde, yumuşak sesi mükemmel bir eşleşme olarak yapılmış gibi hissettiriyor."
    "Şiir, Sayori gibi amaçsızca neşeli değil."
    "Dingin ve acı tatlı."
    "Eğer bunu kağıt üzerinde okusaydım, muhtemelen pek bir şey düşünmezdim..."
    "Ama Sayori'nin sesinden duymak ona yepyeni bir anlam katıyor." #OFFF DÜŞTÜM AŞKA
    "Belki de Sayori şiirlerimi sevdiğini söylerken bunu kastediyordu."
    "Sanki baştan sona tanıdığımı sandığım birinin daha derinlerine inebiliyorum."
    "Sayori bitirir ve biz de alkışlarız."
    s 3q "Başardım~!"
    mc "İyi iş, Sayori."
    s "Ehehe, [player] bile beğendi."
    s "Sanırım bu iyiye işaret~"
    mc "Bu da ne demek oluyor...?"
    show monika 2b at f31 zorder 3
    m "Çok güzel oldu, Sayori."
    m "Şiirin atmosferi sana çok yakışmış."
    m "Ama başka şiirler bu tür bir anlatımla bu kadar iyi sonuç vermeyebilir..."
    show monika at t31 zorder 2
    show sayori at f32 zorder 3
    s 1g "Ne? Gerçekten anlamıyorum." #Senin o güzel yüzü suyu hürmetine
    show sayori at t32 zorder 2
    show monika at f31 zorder 3
    m 1a "Başka bir deyişle, bu tür nazik anlatımların pek işe yaramayacağı şiirlerini gördüm."
    m "Ne okuduğuna bağlı olarak arkalarında biraz daha güç olması gerekebilir..."
    show monika at t31 zorder 2
    show sayori at f32 zorder 3
    s 1x "Ne demek istediğini anlıyorum!"
    s "Bu... şey, bu tür şeyler üzerinde çalışıyorum..."
    s 5 "Herkesin önünde yapmak utanç verici..."
    s "Ehehe..."
    show sayori at t32 zorder 2
    show monika at f31 zorder 3
    m 4a "Bir dahaki sefere seni biraz daha zorlayacak bir şiir seçmeni isteyeceğim."
    m "Festivalden önce fazla zamanımız yok, biliyorsun değil mi?"
    show monika at t31 zorder 2
    show sayori at f32 zorder 3
    s 1q "Taamaammm."
    show sayori at t32 zorder 2
    show monika at f31 zorder 3
    m 1a "Şimdi, sırada kim var...?"
    m "Natsuki?"
    show natsuki 5s at f33 zorder 3
    show monika at t31 zorder 2
    n "Hmph."
    n "Beni [player]'dan önce gitmeye zorlama."
    n "Sizinle kıyaslanabilecek gibi değilim zaten..."
    n "Bunu yapmak zorunda kalmadan önce [player]'nun herkesin standartlarını biraz düşürmesine izin verebilirim."
    show natsuki at t33 zorder 2
    show sayori at f32 zorder 3
    s 1g "Natsuki..."
    show sayori at t32 zorder 2
    mc "Sorun yok, sorun yok."
    mc "Bir an önce bitirsem iyi olacak."
    mc "Ama ne okuyacağıma dair pek bir seçeneğim yok gibi..."
    mc "Bugün için yazdıklarımla yetinmek zorundayım."
    "Ayağa kalktım ve podyumun önüne geldim."
    show natsuki 2c at t44 zorder 2
    show sayori 1a at t43 zorder 2
    show monika 1a at t42 zorder 2
    show yuri 1e at t41 zorder 2
    "Herkesin gözü üzerimde, bu da kendimi çok garip hissetmeme neden oluyor."
    "Şiirimi okuyorum."
    "Kendi yazdıklarıma tam olarak güvenmediğim için, enerji harcamak zor oluyor."
    "Buna rağmen, bitirdiğimde yine de alkış alıyorum."
    mc "Üzgünüm, herkes kadar iyi değilim..."
    show monika at f42 zorder 3
    m 1a "Bu kadar endişelenme."
    m "Bence bu senin yeteneklerinden çok, yazdıklarına olan güvensizliğinle ilgili."
    m "Yine de bu zamanla gelişecek bir şey."
    show monika at t42 zorder 2
    mc "Evet... Olabilir."
    show monika at f42 zorder 3
    m 1j "Tamam o zaman!"
    m 1a "Geriye sadece sen kalıyorsun, Natsuki."
    show monika at t42 zorder 2
    show natsuki at f44 zorder 3
    n 2g "Evet, evet."
    n "Ben gidiyorum."
    "Natsuki isteksizce koltuğundan kalkar ve podyuma doğru ilerler."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    show yuri at thide zorder 1
    show natsuki at t11 zorder 2
    hide sayori
    hide monika
    hide yuri
    n 2c "Şiirin adı..."
    n 2q "Adı..."
    n 1x "Neden hepiniz bana bakıyorsunuz?!"
    m "Çünkü sen sunuyorsun..."
    n 2x "Hmph..."
    n 2h "Her neyse... şiirin adı {i}Zıplamak{/i}."
    "Natsuki nefes alıyor."
    show natsuki 2c
    "Şiiri okumaya başladıktan sonra somurtkan tavrı biraz kayboluyor."
    "Hâlâ biraz heyecansız olsa da, şiirinin bir ritmi ve kafiyesi var."
    "Bu Natsuki'nin alametifarikası olan bir tarz ve yüksek sesle okunduğunda şaşırtıcı derecede işe yarıyor."
    "Kelimeler sanki şiire hayat veriyormuş gibi aşağı yukarı zıplıyorlar."
    show natsuki 2s
    "Natsuki bitirir ve herkes alkışlar."
    "Oflaya puflaya koltuğuna geri döndü."
    show monika 2a at f31 zorder 3
    m "O kadar da kötü değildi, değil mi?"
    show monika at t31 zorder 2
    show natsuki 5w at f32 zorder 3
    n "Senin için söylemesi kolay..."
    n "Bunu bana tekrar yaptırmasan iyi edersin."
    show natsuki at t32 zorder 2
    show monika 1d at f31 zorder 3
    m "Ah, pekala..."
    m "En azından başkalarının önünde bir şiir okuyacak kadar hazır hissediyor musun?"
    show monika at t31 zorder 2
    show natsuki 2c at f32 zorder 3
    n "Yani, bunu başkalarının önünde yapmak çok daha kolay olacak!"
    n "Diğer insanlar için istediğim yüzü takınabilirim."
    n 2q "Ama sadece arkadaşlarım olduğunda..."
    n "Bu sadece... utanç verici."
    show natsuki at t32 zorder 2
    show sayori 1b at f33 zorder 3
    s "Bu bir sürpriz, Natsuki..."
    "Sanırım benim için tam tersi olurdu."
    show sayori at t33 zorder 2
    show natsuki at f32 zorder 3
    n "Bu işler böyledir, o yüzden..."
    show natsuki at t32 zorder 2
    show monika at f31 zorder 3
    m 1a "Sanırım bu durumda..."
    m "Festival için endişelenmenizi gerektirecek pek bir şey yok."
    m 2b "Bununla birlikte, herkese geldikleri için teşekkür etmek istiyorum."
    m "Zor olabilir ama umarım artık nasıl bir şey olduğu hakkında bir fikriniz vardır."
    m 4b "Festivalden önce bir şiir seçtiğinizden ve yeterince pratik yaptığınızdan emin olun, tamam mı?"
    m "Broşürler hazırlayacağım, bu yüzden ne okuyacağınızı önceden bana söyleyin."
    show monika at t31 zorder 2
    mc "Tanrım..."
    mc "Bunun yerine okuyacak başka bir şiir bulmalıyım."
    show monika at f31 zorder 3
    m 1j "Bu da iyi!"
    m 1a "Kendine ait olmak zorunda değil."
    m "Kulüp için bu kadar çaba harcamanıza şimdiden çok şaşırdım."
    m 5 "Bu beni gerçekten mutlu ediyor."
    show monika at t31 zorder 2
    mc "Ah... Evet, sorun değil..." #Uykum geldi yahu.
    play music t8 fadeout 1.0
    show monika at t11 zorder 2
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    hide sayori
    hide natsuki
    m 4b "Tamam, millet!"
    m "Sanırım bugünlük bu kadar."
    m "Festivalin yaklaştığını biliyorum ama yarın için de şiirler yazmaya çalışalım."
    m "Şu ana kadar çok iyi gidiyor, bu yüzden devam etmek istiyorum."
    m "Festivale gelince, yarın planlamayı bitireceğiz ve sonra hazırlanmak için hafta sonumuz olacak."
    m "Pazartesi büyük gün!" #Kanka bide sen niye buraları okuyon onuda anlamış değilim. Neyse kitap gibi, Nostanjik mi her neyse o.
    show sayori 4r at t31 zorder 2
    s "Sabırsızlanıyorum~!" #Bir tarihi eser havası veriyor gibi aynı zamanda.
    show yuri 4b at t33 zorder 2
    y "Bunu yapabilirim... Bunu yapabilirim..."
    mc "Tamam--"
    hide sayori
    hide monika
    hide yuri
    with wipeleft
    "Ayağa kalkıyorum."
    "Sayori ve Monika ile aynı coşkuyu bulmam mümkün değil ama üstesinden gelmek için elimden geleni yapacağım."
    "Eğer kulübün iyiliği içinse..."
    "Ve Monika'yı etkilemek için..."
    "O zaman elimden gelenin en iyisini yapmalıyım."
    show sayori 1a at t32 zorder 2
    mc "Gitmeye hazır mısın, Sayori?"
    show sayori at h32
    s 1x "Evet!"
    show natsuki 2d at f33 zorder 3
    n "Şu halinize bakın, eve hep böyle birlikte gidiyorsunuz."
    show monika 5 at f31 zorder 3
    show natsuki at t33 zorder 2
    m "Çok sevimli, değil mi?"
    show monika at t31 zorder 2
    show sayori at f32 zorder 3
    s 1q "Ehehe~"
    show sayori at t32 zorder 2
    mc "Tanrım, çocuklar..."
    mc "Bu kadar büyütmeyin."
    show natsuki at t44 zorder 2
    show sayori at t43 zorder 2
    show monika at t42 zorder 2
    show yuri 1u at f41 zorder 3
    y "Yine de biraz hoş olmalı..."
    show yuri at t41 zorder 2
    mc "Şey..."
    mc "Ah..."
    "Buna nasıl cevap vermem gerekiyor?"
    show sayori at f43 zorder 3
    s 1d "Sorun değil [player], söylemek zorunda değilsin."
    show sayori at t43 zorder 2
    mc "...Whatever. Let's go already."
    scene bg residential_day
    with wipeleft_scene
    $ ch2_winner = poemwinner[1].capitalize()
    if ch2_winner == "Sayori":
        $ ch2_winner = "Yuri"
    "Sayori ile bir kez daha eve yürüyorum."
    "Sadece birkaç gün geçmiş olmasına rağmen, pek çok şey çoktan değişti."
    "Ama bugün Sayori eve dönerken her zamankinden biraz daha sessiz."
    mc "Hey, Sayori..."
    show sayori 1k at t11
    s "..."
    s 1n "...Özür dilerim! Dalmışım!"
    mc "Ah, şaşılacak bir şey yok..."
    s 1d "Um..."
    s "Ben... daha önceki bir şey hakkında düşünüyordum."
    s "Nasıl ulaştığımızı seviyorum..."
    s 1y "Yani..."
    "Sayori kelimeleri karıştırıyor."
    s 1a "Diyelim ki bir gün [ch2_winner] seninle eve yürümek istedi..."
    mc "Huh?!"
    s "Ne yapardın?"
    mc "Bu nasıl bir soru...?"
    mc "Beni biraz zor durumda bırakıyorsun.."
    s 1y "Ehehe..."
    menu:
        "Yani..."
        "Eve[ch2_winner] ile yürümek isterim.":
            if ch2_winner == "Natsuki":
                call ch2_end_natsuki
            else:
                call ch2_end_yuri
        "Eve hala sayori ile yürümek isterim.":
            call ch2_end_sayori

    "Öte yandan, festivale sadece birkaç gün kaldı..."
    "Bu süre içinde neler olacağını kim bilebilir?"
    return
label ch2_end_sayori:
    $sayoriRoutePoints = sayoriRoutePoints + 1
    mc "Sayori..."
    mc "Gerçekten [ch2_winner] için seni terk edeceğimi mi düşünüyorsun?"
    s 1e "Eh?!"
    s "A-ama..."
    if ch2_winner == "Natsuki":
        s "Çok tatlı ve etrafta olması eğlenceli..."
    else:
        s "O çok güzel ve akıllı..."
    mc "Tanrım..."
    mc "Onu zaten her gün kulüpte görüyorum."
    mc "Ayrıca, eve birlikte gitmekten her zaman çok hoşlanıyor gibisiniz..."
    mc "Bunu senin için mahvetmek istemem."
    s 1y "Çok aptalsın, [player]..."
    s "Bazen beni çok fazla düşünüyorsun."
    s "[ch2_winner] isteseydi bunu hak ederdi, o yüzden..."
    mc "Sayori, ben kararımı çoktan verdim."
    mc "Bazen seni gerçekten anlayamıyorum..."
    s "Üzgünüm..."
    mc "Ayrıca, asla gerçekleşmeyecek bir şey hakkında spekülasyon yapmanın ne anlamı var?"
    s 1k "Hm..."
    show sayori at thide
    hide sayori
    "Konuşma kesildi."
    "Sayori'nin bu kadar önemsemesi biraz garip bir şey..."
    "Ama ben de ona saygı duymak ve onu mutlu etmek istiyorum."
    return

label ch2_end_natsuki:
    $natsukiRoutePoints = natsukiRoutePoints + 1
    mc "Natsuki ile eve yürümek, ha..."
    "Bunu düşünmek neden kalbimi çarptırıyor...?"
    mc "Yani..."
    mc "Sanırım onu geri çevirirsem bana yapacaklarından korkardım..."
    s 1x "Etrafında olması çok tatlı ve eğlenceli değil mi?"
    jump ch2_end_shared

label ch2_end_yuri:
    $yuriRoutePoints = yuriRoutePoints + 1
    mc "Yuri ile eve yürümek, ha..."
    "Bunu düşünmek neden kalbimi çarptırıyor...?"
    mc "Yani..."
    mc "Onun için sosyalleşmenin ne kadar zor olduğunu düşünürsek, onu geri çevirmek çok kötü olurdu, bu yüzden..."
    s 1x "Çok güzel ve akıllı değil mi?"
    jump ch2_end_shared

label ch2_end_shared:
    mc "Bunun az önce söylediğim şeyle hiçbir alakası yok!"
    s 4s "Ahaha! İtiraf ettin!"
    mc "Tanrım..."
    mc "Asla gerçekleşmeyecek bir şey hakkında spekülasyon yapmanın anlamı bile yok."
    s 1d "Şey, belki..."
    s "Ama ben sadece düşünmeyi seviyorum."
    s 1y "Çok geçmeden bana ihtiyacın kalmayacak, biliyorsun değil mi?"
    mc "Sana ihtiyacım...?"
    mc "Sayori..."
    mc "Şu anda kafanda olayları nasıl gördüğünü anlayamıyorum."
    s "Üzgünüm..."
    mc "Herkes farklıdır..."
    mc "Kulüpteki hiç kimse senin yerine geçemez."
    s 1k "Hmm..."
    s "Sen öyle diyorsan..." #SONSUZA KADAR SANA İHTİYACIM VAR.
    show sayori at thide
    hide sayori
    "Konuşma kesildi ve ben kendimi garip hissettim."
    "Ama beni böyle tuhaf bir soruyla tuzağa düşürmesi biraz da onun suçuydu..."
    "Ona yalan söyleyemem."
    "Ama onu mutlu eden bir şey varsa, bunu ondan almaktan nefret ederim."
    "Bu yüzden spekülasyon yapmanın bir anlamı olmadığını söyledim."
    return