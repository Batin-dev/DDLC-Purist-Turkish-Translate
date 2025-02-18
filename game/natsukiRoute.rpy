label natsukiRoute_FestivalDays:
    $ persistent.natsukiRouteStarted = True
    stop music
    play sound alarm
    scene bg bedroom with open_eyes
    "{i}BİP! BİP!{/i}"
    "Festival günü geldi! Alarmım çalmaya başlıyor ve esneyerek kollarımı uzatıp saate bakıyorum."
    stop sound
    "...Hımm, bu kadar geç olmamalıydı, değil mi? Alarmı doğru ayarladığımı hatırlıyorum ama."
    "Telefonuma bakıyorum, neredeyse elli tane okunmamış mesaj ve bir sürü kaçırılmış arama var, hepsi de Natsuki'den."
    "Kalbim sıkışıyor ve okulumun başladığından bir saat geç kalmış olduğumu fark ediyorum."
    "Hızla hazırlanıp mutfağa gidiyorum ve Natsuki'yle birlikte yaptığımız cupcakeleri alıp, iki tepsiyi üst üste koyarak her şeyi taşımaya başlıyorum."
    "Kapıyı hızla açıp okula doğru koşuyorum, kulübümüzün etkinliği için bu kadar geç kalmamın ne kadar kötü bir etki yaratacağı konusunda endişeliyim."
    play music Bunkasai
    scene bg corridor with wipeleft
    "Okula koşarak girip sınıfa doğru ilerliyorum, cupcakeleri düşürmemek için dikkatli oluyorum. Odaya girdiğimde, festival için gelmiş birkaç kişi zaten burada."
    scene bg club_day with wipeleft
    n "Cidden?"
    show natsuki 4e at f31
    "Yan tarafa döndüğümde Natsuki'yi, benim kadar sinirli bir şekilde beni izlerken görüyorum."
    mc "Üzgünüm! Alarmım düzgün ayarlanmamıştı. Geç kalmayı hiç planlamamıştım, gerçekten."
    hide natsuki with wipeleft
    "Cupcake tepsilerini yakındaki bir masaya koyuyorum, ve insanlar tezgaha doğru koşuyor. Belki sadece cupcakes için gelmiyorlardır, değil mi?"
    show natsuki 4e at f42
    n "Yani, sen temel teknolojiyi kullanmayı çözerken biz burada hiçbir cupcake olmasından dolayı insanları bekliyorduk!"
    n "Biliyor musun, insanların bu tür şeylerde kalmalarını sağlamak ne kadar zor?"
    "Telefonuma tekrar bakıyorum, o kadar kez mesaj attığını hatırlıyorum."
    mc "Evet, gerçekten endişelendiğini görebiliyorum. Gerçekten üzgünüm."
    mc "Ama bana ulaşmaya bayağı çaba gösterdin, sanırım. Gerçekten benim için endişelendin mi?"
    n 4h "Kulübün etkinliğinin nasıl olacağına endişelendim, aptal. Evet, biraz da olsa senin için endişelendim ama..."
    "Natsuki, bakışlarını kenara çeviriyor."
    n 4q "Bak, önemli değil."
    mc "Hey."
    "Natsuki'nin yanına biraz daha yaklaşarak konuşuyorum."
    show natsuki 4q at f32
    mc "Şu an buradayız. İnsanlar en güzel cupcakeleri yiyip biz de festivalin tadını çıkaracağız."
    mc "Söz veriyorum, eğlenceli olacak. Ne dersin?"
    n "Hmph. Beni hayal kırıklığına uğratma o zaman."
    show natsuki 5b at f32
    "Natsuki kollarını çapraz yapıyor ama hala heyecanlı ya da en azından ilgileniyor gibiydi."
    hide natsuki with wipeleft
    "Neyse ki, şiir okuma etkinliği günün ilerleyen saatlerinde yapılacaktı, bu yüzden büyük bir hata yapmadığımı düşünüyorum."
    "Kulüp ve ben biraz daha gelen herkesle selamlaşıp kulübümüz hakkında konuştuk ama pek fazla ilgi gösteren olmamıştı."
    "Birçok kişi cupcake almak için gelmişti, bu da… aslında beklediğim bir şeydi."
    "En heyecan verici şey değildi ama o kadar da sıkıcı değildi. Sonuçta, bunu kulübe yardımcı olmak için yapıyordum."
    "Bir süre sonra, Monika'nın sesini uzaklardan duyuyorum."
    show monika 4b at f32
    m "Tamam, herkes! Şiir okumaya başlayacağız! Öncelikle edebi kulüp üyelerimiz kendi harika seçkilerini okuyacak. Sayori, başlamak ister misin?"
    show monika 4b at t21
    show sayori 1x at f22
    s "Tabii! Elimden gelenin en iyisini yapacağım!"
    hide monika with wipeleft
    hide sayori with wipeleft
    scene bg class_day with dissolve_cg
    show sayori 1d at f32
    "Sayori, kürsüye çıkarken biraz gergin gözüküyor ama bir kez okumaya başladığında, şiir ilerledikçe daha rahat hale geldiği belli oluyor."
    show sayori 1r at f32
    "Şiirini bitirdikten sonra hepimiz alkışlıyoruz, Monika tekrar konuşmaya başlıyor."
    show sayori 1a at t31
    show monika 4b at f33
    m "Harika şiirin için teşekkürler Sayori! Şimdi sırada... "
    hide sayori 
    show yuri 3o at l32
    show monika 1a at t44
    "Monika bitirmeden, Yuri kürsüye doğru koşuyor, şiirini sıkıca tutarak."
    show monika 5a at f44
    m "Evet, Yuri. Başla!"
    hide monika with wipeleft
    show yuri 3o at f32
    "Yuri şiirini okumaya başlıyor. Sesindeki güven o kadar belirgin ki, bunun için gerçekten hazırlık yaptığı belli."
    show yuri 3b at f32
    "Yuri'nin şiirini bitirmesinin ardından hepimiz tekrar alkışlıyoruz, Monika sıradaki kişiyi okumaya hazır."
    show yuri 3k at t31
    show monika 3b at f22
    m "Şimdi sırada ben varım! Ahem..."
    hide yuri with wipeleft
    show monika 3b at f32
    "Monika şiirini çıkartıp okumaya başlıyor. Festival için gelen herkes onun şiirinden etkilendi… ya da belki sadece Monika'yı seviyorlar?"
    "Her halükarda, Monika'nın bu konuda uzman olduğu kesin."
    scene bg class_day with wipeleft
    show monika 5a at f32
    m "Umarım şiirimi beğenmişsinizdir. Şimdi [player] şiirini okumaya başlayacak!"
    show monika 5a at t33
    mc "Ah, tamam."
    scene bg club_day with wipeleft
    "Sonunda ben de geldim. Gerçekten sonuncu olmayı umuyordum ama bu, ya şimdi ya da hiç."
    mc "Herkese merhaba."
    "Boğazımı temizliyorum ve şiirime bir kaç kez bakarak hazırlığımı yapıyorum. Neyse ki, garip sessizlik çok uzun sürmüyor ve okumaya başlıyorum."
    show natsuki 1a at t22
    "Performansım, pratik yaptığım zamanlardan daha kötü oldu. Çoğu kişi acımasızca alkışladı, ama Natsuki'nin alkışı biraz daha güçlüydü."
    "Gerçi muhtemelen acıma yüzünden alkışlıyordu, ama yine de jesti takdir ettim. Kürsüden inip Natsuki'ye doğru yürüyorum."
    show natsuki 1c at f32
    n "Neden bu kadar üzgünsün? Belki daha kötü de olabilirdi. Aslında, hiç de şaşırmadım."
    mc "Evet, bu doğru... Ama sen bana o kadar az mı güveniyorsun?"
    n "Diyorum ki, bu kulübün dışında kimse bu kadarını yapamazdı."
    "Natsuki bana gerçek bir iltifat mı etti?"
    n 1e "Tabii ki, bu o kadar da büyük bir şey değil ama, yoktan iyidir."
    "Oh."
    "Monika'nın tekrar konuşmaya başladığını fark ediyorum."
    scene bg class_day with wipeleft
    hide natsuki
    show monika 1b at f33
    m "Son olarak Natsuki şiirini okuyacak!"
    hide monika with wipeleft
    show natsuki 4e at f32
    "Natsuki kürsüye çıkıyor ve şiirini hazırlıyor."
    n "Tabii ki ben sonuncu değilim! Bunu kanıtlayacağım, buna ihtiyacım yok."
    "Natsuki şiirini okumaya başlıyor, bu sefer kulüp üyeleriyle pratik yaptığında olduğundan çok daha hevesli."
    "Yazım tarzı yine ışıl ışıl parlıyor ve bu, oldukça eğlenceli bir deneyim oluyor."
    show natsuki 4l at f32
    "Bittiğinde hepimiz alkışlıyoruz, ama biraz dikkat çekerek, herkesin alkışı durduktan sonra birkaç saniye daha alkışlıyorum."
    "Natsuki kürsüden inip bana doğru yürüyor."
    scene bg club_day with wipeleft
    mc "Bu inanılmazdı!"
    show natsuki 4d at f32
    n "Heh, ne bekliyordun? Bunu belli etmem gerekmezdi ama."
    n "Ama yine de, iltifatını kabul etmekte bir sakınca yok. Teşekkür ederim, sanırım."
    show natsuki 1a at t33
    show monika 4b at f31
    m "Edebiyat kulübü üyeleri bittiğine göre, başka biri...?"
    show monika 1g at f31
    "Monika etrafa bakıyor ve çoğu kişinin şimdiden ayrıldığını görüyor."
    n 1c "Yani, beklediğimden daha uzun süre dikkatlerini çekmeyi başardık."
    show monika 1g at t31
    show natsuki 1a at t32
    show sayori 4x at f33
    s "Evet! Ve eğlendik, değil mi?"
    show monika 1a at t41
    show natsuki 1a at t42
    show sayori 1x at t43
    show yuri 1b at f44
    y "Sanırım bu kadar iyiydi..."
    show yuri 1a at t44
    mc "Hey, hala burada biri var!"
    show natsuki 1c at f42
    n "Son bir cupcake almak için, ama evet."
    mc "Ama festivalin bitmesine hala bir saat var. Şimdi ne yapalım?"
    "Bir kaç dakika beyin fırtınası yapıyoruz."
    show yuri 1f at f44
    y "Daha fazla insan çekmeyi deneyebiliriz."
    show yuri 1a at t44
    show sayori 1r at f43
    s "Neden olmasın? Vazgeçmek zorunda değiliz!"
    show sayori 1a at t43
    show natsuki 1c at f42
    n "Ama daha fazla cupcake'imiz yok ki."
    show natsuki 1a at t42
    show monika 1b at f41
    m "Bir şekilde daha fazla insan gelmesi için bir şeyler bulabiliriz."
    show monika 1a at t41
    show natsuki 1b at f42
    n "Bilmiyorum. Gerçekten, bunu devam ettirmenin bir anlamı yok gibi."
    show natsuki 1a at t42
    show yuri 1f at f44
    y "Bu kadar karamsar olma, Natsuki. Her zaman bu yaptıklarımızı geri getirme şansımız vardır."
    show yuri 1a at t44
    mc "Bence belki bir süre takılabiliriz. Daha fazla insan gelirse gelir ama, festivalin geri kalanını boşuna geçirmiş olmak üzülmemek olur."
    show sayori 1r at f43
    s "Bu doğru. Buradayken biraz eğlenmeye çalışmalıyız!"
    show sayori 1a at t43
    show yuri 1l at f44
    y "Eğer herkes kabul ederse..."
    show yuri 1m at t44
    show monika 1d at f41
    m "Eğer bunu yapmak istiyorsanız, sizi durdurmak benim işim değil. Ben burada kalırım, biri gelirse diye."
    hide yuri
    hide sayori 
    hide natsuki
    with wipeleft
    show monika 1k at f32
    "Monika yanıma gelip kulağıma fısıldıyor."
    m "Natsuki ile git. Sayori'yi ben hallederim, merak etme."
    show monika 1a at f41
    "Monika göz kırpıyor ve uzaklaşıyor. Bekle, bu kadar mı belli oluyor?"
    hide monika with wipeleft
    "Onun tavsiyesine uymanın bir sakıncası olmadığı için Natsuki'ye doğru ilerliyorum."
    show natsuki 1g at f32
    mc "Natsuki, festivali beraber gezmek ister misin?"
    "Natsuki etrafa bakıp herkesin bize baktığını görüyor."
    n 1j "Pekala, tabii, ama sadece yapacak başka hiçbir şeyim yok diye."
    "Natsuki, yüzündeki gülümsemeyi gizlemeye çalışıyor."
    mc "Tabii ki, Natsuki."
    scene bg corridor with dissolve_cg
    "Sınıfın dışına çıkıp koridora ilerliyoruz, koridor öğrenci gruplarıyla dolmuş."
    "Bu kaos içinde nereye gittiğimizi anlamak zor oluyor ama, fazla uzun sürmeden işin üstesinden geliyoruz."
    scene bg school_yard with wipeleft_scene
    "Sonunda okulun dışına çıkmayı başarıyoruz. Etrafımızda çok sayıda stant var, çoğu da karnaval oyunlarıyla dolu."
    show natsuki 3a at f32
    mc "Natsuki, burada ilginç bir şey var mı?"
    n 1k "Sanırım şu stantlardaki oyunlardan birini deneyebilirim."
    "Solumuza döndüğümüzde, bir standda süt şişelerini devirmek için top atılması gereken bir oyun gördük."
    "Yanımıza gelip, topu masaya koyan birinci sınıf olduğunu düşündüğüm bir kızı gördük."
    $ o_name = "Öğrenci"
    o "Bütün şişeleri devirmek için üç şansınız var! Bir deneyelim mi?"
    "Natsuki'ye döndüm."
    mc "Kim başlasın?"
    n 3b "Muhtemelen sen atarsın ve kaçırırsın, o yüzden önce sen denemelisin, ne de olsa biraz eğlenebilirsin."
    "Bu... gerçekten çok nazik, sanırım?"
    "Bir top alıp atış için hazırlanıyorum. Derin bir nefes alıyorum ve topu şişelere doğru fırlatıyorum."
    o "Dokuz şişeden üçünü devirdin! Fena değil."
    show natsuki 2g at f32 
    "Natsuki de bir top alıyor. Yüzündeki ciddi bir konsantrasyon ifadesi var, en iyi atış açısını bulmaya çalışıyor."
    "Ama on saniye geçtiği halde hala atış yapmamıştı."
    mc "Natsuki? Her şey yolunda mı?"
    n 2e "Şşş! Konsantre oluyorum!"
    "Natsuki bir süre daha şişelere bakmaya devam etti, sonra nihayet topu fırlattı."
    show natsuki 2e at f32 with hpunch
    "Direkt ve sert bir atış yaptı, aslında bu daha etkileyici olabilirdi ama top sadece şişeleri ıskalayıp, geri geri zıplayarak standın arkasına çarptı ve neredeyse bize çarpıyordu."
    mc "Vay be, dikkat et!"
    n 3i "Tamam, son atışı sana bırakıyorum."
    "Son topu alıp atıyorum, bu sefer sadece bir şişeyi devirebildim."
    o "Ayy, yazık oldu. Ama yine de teşekkürler!"
    
    scene bg school_yard with dissolve_cg
    
    show natsuki 3i at f32
    "Natsuki ile yürürken, bize yaklaşan, kapı kapı dolaşan bir satıcıyı andıran üçüncü sınıf bir öğrenciyle karşılaştık."
    o "Birbirinizle uyumunuzu ölçmek ister misiniz?"
    show natsuki 3p at f32
    n 3p "Pardon?"
    mc "Hayır, teşekkürler—"
    "Hayır demeye çalışırken, bizi ve Natsuki’yi küçük bir masaya doğru çekip götürüyor. Başka bir üçüncü sınıf öğrenci de karşıya oturuyor, diğeriyse gidiyor."
    show natsuki 1g at f32
    o "Lütfen oturun."
    show natsuki 1g at s32
    "Natsuki ve ben oturmaya çalışıyoruz, ama birbirimize çarpıyoruz ve küçük bir problem fark ediyoruz."
    show natsuki 1i at t32
    mc "Gerçekten sadece bir sandalye mi var bu uyum ölçme işiniz için?"
    o "Birlikte oturmanız lazım, bu şekilde çalışacak."
    "Natsuki'ye işaret ederek sandalyeye oturmasını söylüyorum."
    show natsuki 1g at s32
    o "Şimdi, her biriniz elinizi bana verin."
    n 1e "Gitmek isterim, teşekkürler."
    "Natsuki kalkmaya çalışmadan, üçüncü sınıf öğrenci elini alıyor."
    "Bunun yasak olduğundan eminim ama, bu tuhaf durumu yaşamak zorundayken, ben de elimle veriyorum."
    o "Hımm... evet. Bir dakika. Eğer zaten bir çiftseniz, uyumunuzu nasıl ölçeyim?"
    n 4p "Ne?!"
    mc "Hayır, öyle değil!"
    o "Bunda utanılacak bir şey yok. Ama lütfen zamanımı boşa harcamayın."
    show natsuki at lhide
    "Sinirli bir şekilde Natsuki kalkıp gitmeye başlıyor, beni de kolumdan tutarak çekiyor."

    scene bg school_yard with Dissolve(1.5)
    
    show natsuki 5h at f32
    n 5h "Vay canına, ne cesaret!"
    mc "Aslında, onun bu hatayı yapmasına biraz hak veriyorum."
    n 5e "Evet, ama insanlar böyle hemen sonuç çıkarmamalı! Hatta... eğer doğruysa..."
    show natsuki 5g at f32
    "Natsuki cümlesini ortasında kesiyor."
    mc "Natsuki?"
    n 5e "Neyse. Hadi biraz yemek yiyelim, tamam mı? Bütün gün bir şey yemedim."
    hide natsuki with wipeleft
    
    scene bg school_yard with dissolve_cg
    show natsuki 1c at f32
    "Bir standın yanına gidiyoruz ve burada hamburger satıldığını fark ediyoruz."
    mc "İki hamburger lütfen."
    "Parayı görevliye veriyorum."
    o "Maalesef, normal hamburger için ekmek kalmadı. Ama ramen ekmeğiyle yapılmış harika ramen hamburgerlerimiz var!"
    mc "Hmm, pek emin değilim. Natsuki, sen buna razı olur musun?"
    "Geri dönüp tekrar görevliye bakarken, paranın zaten alındığını görüyorum. Aslında bunun pek doğru olmadığını düşünüyorum ama zaten çok pahalı değildi, o yüzden önemli değil diye düşünüp geçiyorum."
    show natsuki 1a at s32
    "Yakındaki bir masaya gidip oturuyoruz. Bir süre oturmak gerçekten güzel, itiraf ediyorum."
    mc "Son birkaç gün ne kadar yoğun geçse de, biraz eğlenceli olduklarını kabul etmeliyim."
    n 1b "Kötü bir fırıncı değilsin, bunu kabul edebilirim."
    mc "Hadi ama, eğer sen olmasaydın, o kadar iyi sonuçlar almazdık."
    n "Evet, ama ondan başka."
    mc "Dün söylediğimi tekrar ediyorum, daha fazla vakit geçirelim diye. Eğer buluşmak istersen, bana mesaj atman yeterli."
    n 1e "Az önce sana elli mesaj gönderdim, ama yanıt vermedin, ama yine de aklımda bulundururum."
    mc "Ama sonuçta buradayım, değil mi?"
    n 1h "Evet, yanlış değilsin. Sadece korkmuştum..."
    "Natsuki hızla bir ifadeyi değiştiriyor."
    n 1s "Bir dahaki sefere fazla uyuma, tamam mı?"
    "Gerçekten Natsuki, benim cevaplarımı görmeyince bu kadar endişelenmiş olabilir mi?"
    "Bunu geçirdiğimi düşünmüştüm ama belki de benden farklı bir şekilde düşünüyor."
    mc "Çalışacağım. Yine de geç kaldığım için üzgünüm."
    "Görevli masamıza gelip, ramen ekmeğiyle yapılmış hamburgerlerden birer tane veriyor."
    "Aslında fena değil, en azından paramı boşa harcamadım."
    "Yani, bu festivalin profesyonel olduğunu iddia etmiyorum, ama sonuçta bu bir {i}okul{/i} festivali, fazla da şikayet edemem."
    hide natsuki with wipeleft
    scene bg school_yard with dissolve_cg
    
    "Biraz daha konuştuktan sonra, yemeklerimizi bitirip kalkıyoruz."
    show natsuki 1a at f32
    mc "Çok yoruldum. Ya sen?"
    n 1b "Evet, biraz yoruldum. Sanırım eve gitsek iyi olacak."
    mc "Festivalden şimdi ayrılmak fena olmaz. Seninle geçirdiğim vakit için mutluyum."
    n 4b "Ben de fena vakit geçirmedim. Muhtemelen seninle gelmeseydim, daha kötü olurdu."
    "Bir şekilde, birbirimizin gözlerinin içine bakıyoruz. Sadece kısa bir an için, ama oldu."
    "Evet, kesinlikle oldu."
    mc "Evet... Yani, yarın görüşürüz."
    n 4b "S-Sen de."
    "İşte yaptım. Festivale gittim, şiirimi okudum ve Natsuki ile vakit geçirdim. Bugün başarılıydı diyebilirim. Umarım her şey böyle devam eder."
    "Muhtemelen bunun gerçekleşmesi için bu sefer alarmımı düzgün kurmam lazım."
    
    show black with wipedown
    stop music fadeout 5.0

    pause(5.0)

    $ o_name = "???" 
    play sound alarm
    "{i}BEEP! BEEP!{/i}"
    scene bg bedroom with open_eyes 
    "Neyse ki alarmımı doğru kurmuşum, günün başı için bu bile iyi bir başlangıç."
    stop sound
    "Uyanırken, telefonumu kontrol ediyorum ve Natsuki'den bir mesaj gördüm. Bugün sabah gönderilmiş ve önemli gibi görünüyor."
    
    p "kötü haber! edebiyat kulübünde açıklayacağım"
    "Bu iyi bir şey gibi görünmüyor. Ne olmuş olabilir ki?"
    scene bg club_day with dissolve_cg
    
    show natsuki 5g at t41
    pause(1.0)
    show natsuki 5g at t44
    pause(1.0)
    show natsuki 5g at t41
    pause(1.0)
    show natsuki 5g at t44
    pause(1.0)
    "Edebiyat Kulübüne geldiğimde, içimde bir kaygı var. Natsuki, kafasını aşağı eğmiş bir şekilde etrafta yürüyüp duruyor, sanki bir şey ya da birini bekliyormuş gibi."
    mc "Natsuki?"
    show natsuki 4c at t32
    "Biraz başını kaldırıyor ve bana bakıyor."
    n 1b "[player]? Ne var?"
    mc "Bunu bana söylemeni isteyecektim."
    "Cep telefonumu cebimden çıkarıp, sabah bana gönderdiği mesajı gösteriyorum."
    n 4b "Ah, o. Evet, duydun mu?"
    "Natsuki, bana bakıyor, ben de zaten ne olduğunu bildiğimi düşünerek."
    mc "Henüz duymadığımı varsayacağım."

    stop music
    play music NatTheme
    n 1v "Parfait Girls iptal oldu! Üstelik 76. ciltte, finalden hemen önce durdurmuşlar!"
    mc "Vay be, bunu duyduğuma üzüldüm, Natsuki."
    mc "Ama bir film yapılacağı söylenmişti, değil mi? O ne olacak acaba?"
    n 4c "Buna çok para ve zaman harcadıkları için, ayrıca anime uyarlaması olmayan orijinal bir hikaye olduğu söyleniyor, hala çıkaracaklarmış."
    n "Bunu bir noktada görmek isterim ama sonuçta sadece bir film. Manga önemli olan, ve şimdi o da gitti."
    show natsuki 4g at t32
    "Parfait Girls'e Natsuki kadar bağlı olmasam da, Natsuki'nin bu kadar hayal kırıklığına uğramış olduğunu görmek üzücüydü."
    mc "Neyse ki hala başka seriler var, değil mi?"
    n 4b "Evet, ama hiçbiri Parfait Girls değil."
    mc "Doğru. O zaman... nasıl..."
    "Bir an duraklıyorum, ne söyleyeceğimi düşünmeye çalışıyorum. Aslında bu çözülmesi gereken bir şey değil, ama şimdi geri adım atmanın da anlamı yok."
    mc "Kendi manganı neden yapmıyorsun?"
    "Natsuki bana keskin bir şekilde bakıyor."
    n 4g "Çok komik."
    n "Biliyor musun, biraz daha anlayışlı olmanı beklerdim. Ben de senin en sevdiğin mangan bitse üzülürdüm."
    mc "Ciddiyim. Yardım da ederim."
    n 2e "Ciddi misin? Bir manga yaratmak düşündüğün kadar kolay değil."
    mc "Hey, kolay olacağını söylemedim ki. Hem her şeyi bir seferde yapmak zorunda değiliz."
    mc "Yavaşça da olsa üstüne çalışırsak, bence mümkün."
    mc "Bunun bir en çok satan olmasına da gerek yok. Ya da aslında satmamıza gerek yok. Sadece eğlencelik bir şey olsun."
    mc "Hem, nasıl bu kadar zor olabileceğini nereden biliyorsun? Kişisel deneyim mi?"
    show natsuki 5s at t32
    "Natsuki bir anlığa yan tarafta bakıyor."
    n "O... konu dışında."
    mc "Yalnız olmayacaksın."
    "Natsuki bir kaç saniye düşünüyor."
    n 2e "Tamam, ama sadece beni bundan bahsetmeyi kesmen için."
    mc "Tamam. O zaman nereden başlayalım?"
    n 1b "Çizebiliyor musun, [player]?"
    mc "Çizimde {i}berbat{/i} sayılmam sanırım."
    "Tabii, \"berbat\" tanımına bağlı olarak."
    n "Tamam, o zaman yazmayı ben hallederim."
    "Bir anlık garip bir sessizlik oluyor."
    mc "O zaman... manganın konusu ne olacak?"
    n 1c "Peki, senin manga zevkin ne?"
    mc "Genelde shonen manga tercih ederim, ama bazen başka türlere de göz atarım."
    n 1b "Bunu halledebiliriz sanırım. Ben zaten slice of life manganı tercih ederim ama bir yol buluruz."
    "Bir sessizlik daha."
    "Sanırım bu düşündüğüm kadar kolay olmayacak."
    mc "En iyi yazma materyali gerçek hayattan çıkar, değil mi? O zaman neden buradan ilham almayalım?"
    "Şimdi düşündüğümde, ne dediğimi bilmiyorum aslında."
    n 4b "Evet, ama buradan ne ilham alacağım? Hayatım oldukça sıkıcı zaten."
    mc "O zaman neden manganın konusunu edebiyat kulübü yapmıyoruz?"
    n 1w "Ama bu edebiyat kulübü de sıkıcı!"
    "Uzaklardan Monika'nın hayal kırıklığına uğramış sesi duyuluyor."
    show natsuki 1a at t44
    show monika 1g at f41
    m "Ah, teşekkürler..."
    hide monika
    show natsuki 1b at f32
    n "Ama başka bir fikrimiz yok, o yüzden..."
    show natsuki 1a at f32
    "Bu fikrin ne kadar iyi olduğunu hala bilmiyorum ama umarım tutar."
    n 1b "Peki, bir başlık bulmamız lazım. Fikirler?"
    mc "Hmm... \"The Doki Doki Literature Club\" koysak nasıl olur?"
    "O başlık oldukça kötüydü ama ben slice of life bir hikaye için tavsiye alacağım son kişiyim."
    n 4g "Şaka mı yapıyorsun? Bu bir aşk romanı değil! Ne düşündün de bunu söyledin?"
    mc "Hey, anında uydurdum, fikirlerimin iyi olacağını hiç söylemedim."
    show natsuki 4g at t44
    show monika 1k at f41
    "Odadan bir yerlerden gülüşmeler duyuluyor."
    n 4w "Bak, Monika bile buna gülüyor!"
    hide monika
    show natsuki 3q at f11
    n "Ama hadi, gerçekten hikayeye aşk unsuru eklemek istersen..."
    mc "Ben aslında hiç aşk unsuru istememiştim!"
    n 4d "Geç kaldın, bunu sen söyledin!"
    "Natsuki açıkça benimle dalga geçmekten eğleniyordu."
    n 2b "Ama ciddi olalım, karakterlerimizin adı ne olacak?"
    mc "Bunu edebiyat kulübümüzden mi alıyoruz? Belki herkesin ismini ters çevirebiliriz. Mesela Ikustan, Akinom, Iruy, Iroyas."

    $ playerNameBackwards = player[::-1].title()

    n 4b "Hadi ama, en azından {i}çaba{/i} göster. Ciddiye al, [playerNameBackwards]."
    "Adımı ters çevirdiğimde aslında pek de iyi çıkmadığını kabul ediyorum."
    y "Bir manga mı yapıyorsunuz?"
    show natsuki 2b at t22
    show yuri 2f at f21
    "Dönüp baktığımda Yuri'nin geçerken bize baktığını görüyorum."
    y 2a "Manga ilgimi çekmiyor aslında ama yazı konusunda iyi olduğumu bilirsin. Belki yardımcı olabilirim..."
    "Natsuki onu kesiyor."
    show yuri 4b at t21
    show natsuki 5c at f22
    n "Buna gerek yok, sağ ol."
    show yuri at lhide
    hide yuri
    "Yuri sessizce uzaklaşıyor, biraz alınmış gibi."
    show natsuki 5c at f11
    mc "Ne oldu ki şimdi?"
    n 2w "Buna odaklanırken başka hiçbir şey dikkatimi çekmesin istiyorum."
    mc "Dikkat mi? Ne demek istiyorsun?"
    n 2e "Yuri! Onunla ilgilenmene gerek yok."
    mc "Yuri'yi kıskanıyor musun, Natsuki?"
    show natsuki 1x at f11
    "Natsuki'nin ellerini biraz sıktığını, sonra derin bir nefes aldığını görebiliyorum."
    n 1b "Hayır."
    mc "Yani, o zaman Yuri'yi eklemek sorun yaratmaz, değil mi?"
    n 1e "O kadar ileri gitmem."
    "Bu konuda hiçbir yere varamayacağımı fark ettiğim için konuyu kapatmaya karar veriyorum."
    mc "Senin kararın, Natsuki. Eğer bu kadar önemliyse..."
    n 5u "Bazen biraz güvensiz hissediyorum."
    "Natsuki'nin böyle bir şeyi açıkça itiraf etmesi tuhaf. "
    
    play sound paalert
    $ o_name = "PA System"
    o "Dikkat tüm öğrencilere!"
    show natsuki 1c at f11
    "Hepimiz okulun hoparlöründen gelen sese yöneliyoruz."
    o "Dün festivalde yaşanan teknik aksaklıklar nedeniyle, okul yarın kapalı olacak."
    $ o_name = "???"
    "Hımm, acaba patlamaların neden olduğu hasarı mı fark ettiler, yoksa boğa güreşi yüzünden yıkılan duvar mı sebep oldu?"
    mc "Hı. O zaman yarın okula gitmemiz gerekmiyor. Galiba o zaman başka bir şeyler yapmam gerekecek."
    show natsuki 5i at f11
    "Natsuki, bir şey hakkında derin düşüncelere dalmış gibi görünüyor."
    n 5k "[player], yarın yiyecek alışverişine gitmem lazım. Benimle gelmek ister misin?"
    mc "Hı? Beni... çağırıyor musun?"
    "Natsuki hemen tepki veriyor."
    show natsuki 5h at hf11
    n "Yardım etmeye ihtiyacım var! Sadece o kadar."
    "Bence alışverişe gitmek için ikinci bir kişiye ihtiyacı yok, ama neyse."
    mc "O zaman uygun olmalıyım, ama önce programıma bakayım."
    show natsuki 5s at f11
    "Telefonumdan haftalık planımı kontrol ediyorum, böylece gidebileceğimden emin oluyorum."
    n 5q "Başka biriyle planın falan yok, değil mi?"
    mc "Bilmediğim kadarıyla yok."
    n "İyi."
    "Sanırım bir şeyi çözdüm. Natsuki kolayca kıskanabiliyor ama keşke bunun gerekmediğini anlasaydı. Ne korkuyor ki?"
    mc "O zaman, yarın mı?"
    n 4c "Evet. Şimdi, manga işine dönelim."
    mc "Evet. Nerede kalmıştık, tekrar?"
    
    hide natsuki
    scene bg club_day with dissolve_cg 
    "Bir saat geçti ve başardıklarımız konusunda gayet iyiyiz gibi hissediyoruz."
    mc "Oldukça ilerledik, değil mi?"
    show natsuki 3c at f11
    n "Son kontrol ettiğimde... bir sayfa bitirmiştik."
    mc "Daha fazla şey yaptığımızı yemin edebilirim."
    n 3b "Hayır. Sadece başlık sayfasını yaptık."
    "Natsuki, çizdiğim sayfayı gösteriyor. Üzerinde, Edebiyat Kulübü üyelerinin ve benim kötü çizilmiş versiyonlarımız, dramatik pozlarla yer alıyor. Üstte ise 'Edebiyat Kulübü Arkadaşları' başlığımız var."
    n "Henüz renklendirilmedi bile."
    mc "Eyvah, bu asla işe yaramayacak."
    show natsuki 3c at t22
    show sayori 1b at f21
    "Sayori geçiyor."
    s "Bu ne?"
    show natsuki 4e at f22
    show sayori 1b at t21
    n "Bir hata."
    mc "Bu saçma manga projesine çalışıyoruz."
    show natsuki 4e at t22
    show sayori 1x at f21
    s "Bence harika görünüyor!"
    show natsuki 4f at f22
    show sayori 1x at t21
    n 4f "Her şeyi şekerleştirmene gerek yok, Sayori."
    show natsuki 4f at t22
    show sayori 4c at f21
    s 4c "Ciddiyim! Sizin en iyisini yaptığınız önemli, bu da önemli. Yaptığınız şeyde stiliniz ve duygularınız olması lazım."
    s "Mükemmel yazı ve sanat içeren bir manga hoş olabilir, ama eğer ruhsuzsa ne anlamı var ki?"
    mc "Evet, sanırım haklısın."
    show natsuki 4g at t22
    s 1b "Eğer bir tavsiyede bulunabileceksem, o da başlık olurdu."
    mc "Biraz genel oldu evet."
    s "Nasıl..."
    "Sayori duraklıyor, ama hiçbir şey bulamıyor."
    n "Başlığı başka bir zaman çalışalım."
    show natsuki 4g at t33
    show sayori 1b at t32
    show monika 3d at f31
    "Monika geçiyor."
    m "Aslında, manga üzerinde çalışmaya başka bir zaman devam etmeniz gerekecek. Zaten gitme zamanı!"
    show monika 3c at t31
    show natsuki 1e at f33
    n "Ne? Daha yeni başlamıştık!"
    show natsuki 1g at s33
    "Natsuki itiraz ettikten sonra, başını eğiyor."
    mc "Evet, biraz daha kalamaz mıyız?"
    show monika 4b at f31
    m "Pekala, teknik olarak kalabilirsiniz. Ama neden daha rahat bir yerde çalışmıyorsunuz? Sonuçta bir aşk romanı üzerinde çalışıyorsunuz, değil mi?"
    show monika 1j at t31
    show natsuki 5e at f33
    "Natsuki hızlıca araya giriyor."
    n "H-Hayır! Ve 'rahat bir yerde' çalışmamıza da gerek yok. Hapsi de olsa burada çalışabiliriz."
    show monika 5a at f31
    m "Ne derseniz deyin~"
    hide monika with wipeleft   
    hide sayori with wipeleft
    "Monika, Sayori ile birlikte kapıdan çıkarken göz kırpıyor."
    show natsuki 1g at f11
    "Natsuki, odanın geri kalanına bakıyor ve kimse başka kimse kalmadığını fark ediyor."
    n 1c "Tamam, hadi senin evine gidelim."
    mc "Bekle, ne?"
    n "Manga üzerinde çalışmak için, tabii! Hadi gel, geç olmadan."
    show natsuki at lhide
    hide natsuki
    "Natsuki, beni kolumdan çekip sınıftan dışarı çıkarıyor. Demek ki, sonradan da olsa çalışmaya devam edeceğiz."
    scene bg bedroom with wipeleft_scene

    "Bir bakmışım, evime gelmişiz."
    mc "Hadi o zaman, işe geri dönelim."
    show natsuki 4c at f11
    n "Aslında, pek bir fikrim kalmadı."
    mc "O zaman buradayken ne yapıyoruz?"
    n 1e "Düşünmek için geldik! Manga için nasıl fikirler bulacağız başka? Hem, seni yalnız bırakıp bütün gün anime izlerken küçük bir ekranda NEET gibi oturmanı izleyemem."
    mc "O zaman ne öneriyorsun?"
    n 3b "NEET olmazdın, eğer animeyi tek başına izlemek yerine birisiyle izlersen, neden önce bunu yapmıyoruz?"
    mc "Hıh, anime izlediğini bilmiyordum. Ama haklısın, manga okumakla anime izlemek genelde bir arada gider."
    n 4d "Tabii ki, ve şunu bilmelisin ki anime zevkim manga zevkim kadar iyidir."
    mc "O zaman, ne izleyeceğimize sen karar ver."
    n "Harika, çünkü manga için ilham almak adına izleyeceğimiz tam şey bu."
    hide natsuki with wiperight
    "Bu hala manga hakkında mı ki?"
    "Bir süre Natsuki çantasından birkaç saniye boyunca bir şeyler aradı, derken Blu-Ray DVD'lerden bir set çıkardı. Bir an, kapağı tanıdığımı düşündüm."
    show natsuki 2a at f11
    mc "Parfait Girls anime mi? Dahası, bunu okula mı getirdin?"
    n 4b "Tabii, çoğu zaman mangayı okumanı öneririm. Ama sen zaten çoğunu okudun, bu yüzden animeyi izlemek de hoş, çünkü aradaki ince farkları görmek güzel."
    stop music fadeout 5.0
    n "Ayrıca, bu daha fazla Parfait Girls. Anime de herhangi bir gereksiz bölüme sahip değil."
    mc "Eğer senin istediğin buysa, o zaman izleyelim. Ben de ayarları yaparım."
    hide natsuki

    scene bg bedroom with Dissolve(1.5)
    play music aNewDay fadein 2.0
    "Geride kalan o öğleden sonra gerçekten eğlenceliydi. Sanırım hiç manga üzerinde çalışmadık, ama sorun değil."
    "Parfait Girls animeyi izlemek gayet güzeldi. Bu versiyonun ince detaylarını görmek gerçekten ilginçti ve hatta ben bile takdir edebildim."
    show natsuki 1c at f11
    n "Aman tanrım, gitmem gerektiğini yeni fark ettim."
    show natsuki 1c at t41
    "Natsuki, izlediğimiz şovun ardından üzerinde oturduğumuz beanbag'tan kalkıp bütün eşyalarını toplamaya başlıyor."
    n 1b "Keşke daha uzun kalabilsem, ama yarın yine birlikteyiz, değil mi?"
    mc "Evet. O zaman görüşürüz!"
    show natsuki at lhide
    hide natsuki
    "Natsuki, odama doğru yürürken elini sallayarak dışarı çıkıyor, fakat çantasının sapı kapı koluna takılıp düşmesine neden oluyor."
    n "İyiyim!"
    "Natsuki toparlanıp kalkıyor, ardından kısa sürede evimden çıkıyor ve ben, yüzümde tatmin olmuş bir gülümseme ile kalıyorum."
    "Keşke Natsuki ile böyle eğlenmeye devam edebilsem, hayatın yüklerinden hiç endişelenmeden."
    show black with wipedown
    "Keşke biz ikimiz de böyle olabilsek."
    window hide
    stop music fadeout 2.0
    pause(4.0)  

    window show

    play sound alarm
    "{i}BEEP! BEEP!{/i}"
    scene bg bedroom with open_eyes
    "Alarm saatimin çaldığını duyup uyanıyorum."
    stop sound
    "Dün alarmı kapatmayı unuttum, çünkü okul yok ama yine de, bana bugün Natsuki ile vakit geçireceğimizi hatırlattı."
    "Durumu gözden geçirdiğimde, aslında bu iş biraz daha kolay olurdu, eğer ona ne zaman gideceğimizi sormayı unutmasaydım."
    "Telefonumu alıp Natsuki'ye ne zaman gelmek istediğini yazıyorum ve neredeyse hemen mesaj atıyor."
    p "Şu an nasıl?"
    "Biraz erken olduğunu düşündüm ama beklemektense hemen gitmek, bana daha makul geldi."
    "Mesajımı onaylayıp, birazcık düzgün görünmeye çalışarak hazırlanıyorum."
    "Bir süre sonra, kapıma bir tekme duyuyorum."
    scene bg house_entrance with dissolve_cg
    show natsuki 4ba at f11
    play music aNewDay fadein 2.0
    "Kapıyı açıyorum ve Natsuki'nin orada olduğunu görüyorum, biraz sabırsız ama aynı zamanda beni gördüğüne mutlu."
    n 4bb "Yani, hazırsın değil mi?"
    show natsuki 4ba at f11
    mc "Sanırım sen hazırsın, o zaman ben de hazırım."
    n 4bb "Tamam. Umarım bu işte çok yavaş davranmazsın, bu arada."
    mc "Elimden geleni yaparım."
    "Birçok kez alışverişe çıktım, bu yüzden sorun olacağını düşünmüyorum, ama kim bilir, belki Natsuki bir profesyonel alışverişçi falandır, varsa öyle bir şey."

    scene bg streets_day with wipeleft_scene
	
    play sound crowds
	
    pause(1.5)
    scene bg grocery with dissolve_cg
    "Hiç gitmediğim büyük bir süpermarkete geliyoruz. Her yer kalabalık, bu da her şeyin nerede olduğunu görmekte biraz zorluk yaşamama neden oluyor."
    show natsuki 1ba at f32
    n 1bb "Hadi! Zamanımız var ama o kadar da değil!"
    
    "İçeri doğru ilerliyoruz ve ben, bu gezinin detaylarını bana söylemesini bekliyorum."
    n "Buradayız, KO Süpermarket. Burada şimdilik ihtiyacımız olan her şeyi bulabiliriz."
    mc "İlginç. Daha önce hiç duymamıştım burayı."
    mc "Burası hakkında özel bir şey var mı?"
    n 3bl "Bu mağazanın güzel yanı, çoğu üründe düşük fiyatlar olması. Yani burası kesinlikle doğru tercih."
    n "Sen de buraya gelmeye başlamalısın, biliyorsun. Hani, kötü bir alışveriş zevkin yoksa tabii."
    show natsuki 3bj
    "Alışveriş için kötü bir zevkin olabileceğini hiç düşünmemiştim, ama artık düşünüyorum."
    mc "Peki, ne alacağız peki?"
    n 3bl "Cupcake malzemeleri tabii! Malzemelerimizi eksiksiz almak önemli."
    mc "Anladım. Nereden başlayalım?"
    n "İlk önce un. Beni takip et, birkaç koridor ileride."
    show natsuki 3ba at t44
    mc "Daha hızlıca işimizi bitirebilmek için ayrı ayrı gitsek daha iyi olmaz mı?"
    "Natsuki birden donakaldı."
    show natsuki 5bq at t44
    n "Y-Yok, böyle iyiyiz." 
    mc "Peki, sen ne dersen."
    hide natsuki with wipeleft
    "Un ve şeker reyonuna doğru ilerliyoruz ve Natsuki unları inceliyor."
    show natsuki 3bc at t41
    pause(1.5)
    show natsuki 3bc at t33
    pause(1.5)
    show natsuki 3bc at t42
    "Aynı türden birçok çeşit var ama her biri farklı markalarda. Natsuki'nin bir şey seçmekte biraz zaman harcadığını fark ediyorum."
    mc "Markanın tat üzerinde fazla etkisi olacağını sanmıyorum."
    show natsuki 4bb at f11
    n "Marka önemli değil! Buradaki en önemli şey, her çuvalın büyüklüğüne bakıp, fiyatlarını diğerlerinden nasıl karşılaştırdığını anlamak."
    show natsuki 4ba at f11
    mc "Yani üç tane 4 kiloluk un çuvalı, bir tane 10 kiloluk çuvaldan daha ucuz oluyorsa?"
    n 3bb "Aynen öyle. Bu uzun bir işlem ve aslında vaktimiz olsa da çok dikkatli olman gerekiyor."
    mc "Anlıyorum. Bu kadar ayrıntılı düşündüğünü hiç bilmiyordum."
    n "Eğer para birikiyorsa, neden yapmayasın ki?"
    show natsuki 3ba at t44
    "Natsuki haklı bir noktaya değindi; alışveriş yaparken hiç bu tarz şeylere dikkat etmemiştim. Hatta matematik yapmayı hiç sevmedim."
    show natsuki 1bl at f44
    "Bir süre sonra, Natsuki sonunda un çuvalını seçiyor."
    n 1bb "Al, bunu tut."
    show natsuki 1bb at f11
    "Bir şey söylemeye fırsatım bile olmadan, un çuvalını bana atıyor ve ben zorla yakalıyorum, o da alışveriş listesine tekrar bakıyor."
    show natsuki 1ba at f11
    "Unu önce alışveriş sepetine koymak çok daha hızlı olurdu ama sanırım biraz aceleciydi."
    n 1bb "Tamam, sırada yumurta var."
    show natsuki 1ba at t44
    "Yumurta kutularının olduğu reyonda ilerliyoruz. Natsuki yine hangi türü alacağına karar verirken, ben de sohbete başlamak istiyorum."
    mc "Bu cupcake'leri bir etkinlik için mi yapıyorsun?"
    n 1bb "O kısmı önemli değil, güven bana."
    mc "Bilmiyorum, önemli değilse, bana söylemenin ne zararı var? Eğer biri için yapıyorsan, sır tutarım."
    n 4bq "Sonunda öğrenirsin zaten. Hadi ama, şimdi bana yardım etmelisin, değil mi?"
    "Gerçekten neye yardım etmem gerektiğinden hiç bir fikrim yok. Ama Natsuki'nin bazen garip mantıklarını anlamaya alıştım."
    mc "Yardım etmeyi isterim ama nasıl yardımcı olacağımı bilmiyorum."
    n 4bb "Hmm... listenin geri kalanına bak, belki? Sanırım alışveriş sepetinde."
    "Natsuki'nin dediği gibi, sepete bakarken listeyi buluyorum."
    mc "Sıradaki şey tereyağı olmalı."
    n "Tamam, o zaman gidelim."
    show natsuki 4ba at f11
    "Natsuki mükemmel bir yumurta kartonunu seçiyor ve yolumuza devam ediyoruz."
    mc "Bir şey soracaktım Natsuki. Bütün bu iş tamamlandıktan sonra, cupcake'leri birlikte yapmayı ister misin?"
    show natsuki 4bs at f11
    "Natsuki bir anlık olarak yanına bakıyor, sonra tekrar bana dönüyor."
    n 4bq "Normalde isterdim ama..."
    mc "Evet?"
    n "Sadece özel bir durum olduğunu söyleyeyim."
    mc "Anladım."
    show natsuki 4bs at f11
    "Bir anda ne demek istediğini anlayamıyorum ve sessizleşiyorum."
    hide natsuki with wipeleft
    "Bu bütün iş bana biraz garip geldi. Bu bir randevu muydu yoksa değildi mi? Belki yanlış anlıyorum ama aynı zamanda, Natsuki ile daha fazla vakit geçirmeyi sevmediğimi de söyleyemem."
    "Belki bir gün onu gerçekten bir randevuya davet ederim. Hani, tam olarak bir randevu diyerek, randevu olarak adlandırıp, öyle bir şey yaparız."
    "Ama sanırım bunu yapmaya cesaretim olmayacak, o yüzden şimdilik unutmalıyım."
    "Alışverişimiz devam etti, ihtiyacımız olan tüm malzemeleri alıp, self-checkout kasasına yöneldik."
    show natsuki 2ba at f11
    "Natsuki'nin burası için bir üyelik kartı çıkardığını fark ettim, demek ki düşündüğümden daha sık geliyormuş buraya."
    mc "Peki, bunların hepsi toplamda ne kadar?"
    n 1bk "Bunu... Vay, yeni bir rekor kırdım!"
    mc "Yeni rekor mu?"
    n 2bc "Evet, bu ürünleri ne kadar ucuza alabileceğimi görmek hoşuma gidiyor. Tabii kuponları saymazsak."
    mc "Biliyorsun, o kadar ucuz ki, bence ben de ödemek isterim."
    mc "Yanımda yeterince param var galiba."
    show natsuki 2bu at t11
    "Natsuki biraz tedirgin görünüyor."
    show natsuki 2bu at f11
    n "Yapmak zorunda değilsin... "
    n "...Aslında, gerçekten istersen, olur."
    mc "Tabii ki, hiç sorun değil."
    show natsuki 4bj
    "Natsuki kısa bir an için gülümsüyor."
    n "Teşekkürler. Ama unutma, sen gönüllü oldun, ben sana geri ödeme yapmam!"
    hide natsuki with wipeleft
    scene bg streets_day with wipeleft_scene
    "Her şeyi toparlayıp, birkaç alışveriş torbası taşıyarak dışarı çıkıyoruz."
    mc "Yani, ben alışveriş konusunda pek uzman değilim ama açıkçası bu eğlenceliydi."
    show natsuki 1bb at f11
    n "Genelde sıkıcıdır, ama biriyle gelmek güzeldi. O yüzden sana teşekkür ederim."
    mc "Evet."
    show natsuki 1ba at f11
    "Bir sessizlik oldu. Bir şeyler söyleme isteği duyuyordum ama ne söyleyeceğimi tam olarak anlayamadım."
    mc "Natsuki..."
    show natsuki 1bs at f11
    n "E-Evet?"
    mc "Ben... şey..."
    "Yok, bunu yapamam."
    mc "İyi şanslar cupcake'leri yaparken."
    n 1bq "Tabii ki!"
    n "Ve... şey..."
    "Natsuki de, söylemeye çalıştığı şeyi bir türlü çıkaramadı."
    n "İyi şanslar, ne yapıyorsan."
    "Ne demem gerektiğini bilmiyorum."
    mc "Teşekkürler."
    hide natsuki with dissolve_cg
    "Teşekkürler? O kadar mı?"
    "Bir gün duygularımı itiraf edeceğim. Ya da belki Natsuki, gururunu aşacak kadar güçlü hisler besliyorsa, o önce itiraf eder."
    "Ama ne olursa olsun, ben her zaman onun yanında olacağım."
    stop music fadeout 3.0
    hide window
    pause(1.0)
    scene bg bedroom with wipeleft_scene
    play music Thoughts fadein 3.0
    
    "Yatakta otururken, her şeyi biraz daha net görmeye çalışıyorum."
    "Edebiyat Kulübü'ne katılalı pek uzun sayılmaz, ama yine de yeterince uzun."
    "Yeterince uzun ki kulüp üyeleriyle, özellikle de Natsuki ile bir bağ kurduğumu hissediyorum."
    "Sayori beni kulübe davet ettiğinde, bunun bu kadarına yol açacağını düşünmemiştim."
    "Tabii, geçmişte kızlara karşı duygularım olmuştu ama sanırım Natsuki ile geçirdiğim zaman kadar güçlü değillerdi."
    "Zor birini anlamak bazen kolay olmuyor, evet, ama onun tüm güvensizliklerinin altında gerçekten bir iyilik var."
    "Ve neyse ki, sevdiğim bir kızın manga ilgimle de ortak paydada buluşması güzel."
    "Düşünüyorum da, aslında manga, birbirimize daha da yakınlaşmamıza da neden oldu. Sadece birlikte okumak değil, dün kendi manga'mızı yapmaya çalışmamız da."
    "Önemli değil, neredeyse hiçbir şey yapamadık ama belli ki o da keyif alıyordu, ben de."
    "Ne olduğunu tam olarak bilmiyorum ama telefonumu alıyorum. Düşünmeden Natsuki'ye mesaj atıyorum: \"İyi geceler!\""
    "Yaptıktan sonra inanılmaz derecede utanıyorum. Arkadaşlar böyle şeyler yapar mı? Hem biz bir ilişkide değiliz. Ne düşünüyordum ki?"
    "En kötü ihtimali beklerken, Natsuki'den cevap alıyorum."
    p "sen de! :)"
    "Zihnim biraz rahatlıyor ama sonra başka şeyler düşünmeye başlıyorum."
    hide window
    show black with Dissolve(4.0)
    window show
    "Eğer itiraf etmeye karar verirsem, ne söyleyebilirim? Ne zaman olur? Beni buna iten bir şey olur mu?"
    "Bu noktada neredeyse hiçbir şey bilmiyorum. Tek bildiğim yarının yeni bir gün olduğu ve Natsuki ile vakit geçirebileceğim, umarım o da benimle vakit geçirmekten keyif alır."
    hide window
    pause(1.0)
    stop music fadeout 3.0
    pause(2.0)
    
    
    call natsukiRoute_SchoolDaysTwo
    return

label natsukiRoute_SchoolDaysTwo:
    scene bg bedroom with open_eyes
    window show
    play music aNewDay fadein 3.0
    play sound alarm
    "{i}BEEP! BEEP!{/i}" 
    stop sound
    "Vay be, geçen gece hiç uyumadım mı acaba? Ne kadar yorgunum, bir türlü anlamıyorum."
    "Sonuçta, pek de önemli değil. Yeni bir gün, yeni bir Edebiyat Kulübü toplantısı demek, ama bu kötü bir şey değil tabii."
    "Haa, bir de, acaba Natsuki nasıl? Hani, marketten sonra biraz garip olmuştu durum."
    "...Hayır, böyle düşünmemeliyim. Eğer bu kadar gergin olursam hiçbir yere varamam. Sonuçta, ne olursa olsun olacak."
    "Şu anda, normal bir şekilde hayatıma devam etmem gerek. O yüzden alarmımı kapatıp okula gitmek için hazırlanıyorum."

    scene bg class_day with wipeleft_scene
    pause(1.5)
    scene bg club_day with wipeleft_scene
    "Dersler nihayet bitmişken (Fransızca dersini sevdiğimi hiç söyledim mi?), Edebiyat Kulübü'ne doğru ilerliyorum."
    "Odaya girdiğimde, herkes kendi işine dalmış durumda. Buna Natsuki de dahil, ama o başı öne eğilmiş bir şekilde masasında oturuyor."
    "Belki uyuyordur, ama anlamak zor."
    show monika 1a at f11
    m "Hey, [player]! Geldiğini görmek güzel."
    hide monika with wipeleft
    show natsuki 5u at t44
    "Monika, Yuri ve Sayori'ye selam verdikten sonra, Natsuki'nin yanına gidiyorum."
    show natsuki 5u at t11
    mc "Natsuki? Uyanık mısın?"
    show natsuki 1c at f11
    "Natsuki, gözünü yavaşça ovuşturuyor ve sesimi duyduğunu fark ettikten sonra başını kaldırıyor."
    "Onun başını kaldırmasının, özellikle benim sesimi duyduğunda olduğunu düşünmek isterdim, ama şu anda fazla çıkarımda bulunuyorum."
    n 1e "Hah... Sonunda geldin."
    "Natsuki kollarını esnetip esneyerek uyanıyor."
    mc "Dün gece pek uyudun mu?"
    n "Sanırım öyle diyebilirim."
    mc "Bir şey mi seni uyandırdı, yoksa?"
    n "Aslında çok düşündüğüm bir şey vardı, evet."
    show natsuki 1q at f11
    n "S-Seninle falan alakası yok yani."
    mc "Aynen, bende de öyle."
    n 1e "Hı?"
    "Belki bunu daha iyi ifade edebilirdim."
    mc "Haa, önemli değil. Ben de dün gece uyumakta zorlandım."
    n 1s "Evet."
    "Ya gerçekten çok yorgunduk ya da kafamız karışmıştı, çünkü olan biteni anlamıştık ama yine de sorgulamıyorduk."
    hide natsuki with dissolve_cg
    "Belki her ikisi de oluyordur. Ama kesinlikle son zamanlarda her şeyin biraz farklı hissettirdiğini biliyordum."
    mc "Peki, bugün ne yapalım?"
    "Natsuki yine esneyip gözlerini kapatıyor."
    
    n "Her zaman manga var. Aslında... bana okumanı isterim."
    show natsuki 4p at hf11
    "Natsuki gözlerini aniden açıp, böyle bir şey söylemesinin ne kadar tuhaf olduğunu fark ediyor."
    n 4q "Böyle demek istemedim! Gerçekten çok yorgunum, tamam mı?"
    "Natsuki'nin bu kadar sakin bir halini görmek garip, sanki gerginliği gitmiş gibi. Belli ki uykusuzluk bazı insanlarda böyle bir etki yaratıyor."
    pause(1.5)
    hide natsuki
    scene bg club_day with wipeleft_scene
    "Bir süre birlikte manga okuduk. Natsuki bana okuma isteğini yorgun olduğu için yapmıştı, ama çok geçmeden yine eski haline döndü."
    show monika 1a at f41
    m "Tamam, herkes!"
    show monika 1a at f11
    "Hepimiz Monika'ya dönüyoruz."
    play music aNewDay fadein 2.0
    m 1b "Bir süredir etkinlik yapmadık, o yüzden ne yapabileceğimizi düşündüm."
    show monika 1a at t21
    show yuri 1f at f22
    y "Okul festivaline sadece birkaç gün önce katıldık, değil mi?"
    show monika 1b at f21
    show yuri 1e at t22
    m "Dediğim gibi, birbirimizi daha iyi tanımamıza yardımcı olacak basit bir şeyler yapalım dedim."
    show monika 1b at t31
    show yuri 1e at t32
    show natsuki 3b at f33
    n "Bunu salakça bir şey yapmazsanız olur."
    show natsuki 3b at t33
    "Natsuki'nin sözü yarıda kesiliyor."
    show monika 1b at f31
    m "Evet, gösteri yapıp anlatıyoruz!"
    show monika 1a at t41
    show yuri 1e at t42
    show natsuki 1c at t43
    show sayori 1c at f44
    s "Gösteri ve anlatım? Yani, bir şey getirip hakkında konuştuğun şey mi?"
    show sayori 1a at t44
    mc "Ama bu sadece küçük çocukların yaptığı bir şey değil mi?"
    show monika 1b at f41
    m "Evet ama hâlâ çok faydalı! Birincisi, topluluk önünde konuşma becerilerimizi geliştiriyor—festivalde kötü bir iş çıkarmadınız ama her zaman gelişim alanı var."
    m "Ayrıca, birbirimizi daha iyi tanımamıza da yardımcı olur. Özellikle sen, [player], çünkü kulüpte çok yeni sayılırsın."
    show monika 1a at t41
    show natsuki 4e at f43
    n "Bu gerçekten utanç verici. Biraz daha az kötü bir şey seçmedin mi?"
    n "Buradaki yarısı çocuk gibi davranıyor diye, biz de onlara öyle davranmak zorunda değiliz."
    show monika 1b at f41
    show natsuki 4g at t43
    m "Kabulleniyorum, etkinlik için fikirlerim tükenmişti ve son aklıma gelen buydu, ama yine de."
    show monika 1a at t41
    show yuri 1f at f42
    y "O zaman aklına başka etkinlik fikirleri gelen var mı, Natsuki?"
    show yuri 1e at t42
    show natsuki 1c at f43
    "Natsuki düşünmeye başlıyor."
    n 1b "Hımm..."
    show natsuki 1b at t43
    show sayori 4c at f44
    s "Yapma, Yuri, insanları böyle sıkboğaz etme!"
    show sayori 4c at t44
    "Sanırım burada devreye girme sıram geldi."
    mc "Ne dersiniz, birlikte şiir yazsak?"
    show natsuki 4e at f43
    n "Zaten bunu yapıyoruz. Kulübün amacı bu, [player]."
    "Oh, evet."
    show yuri 1f at f42
    show natsuki 4c at t43
    y "Aslında, bir önerim var."
    show monika 1b at f41
    show yuri 1e at t42
    m "Hadi, Yuri, söyle."
    show monika 1a at t41
    show yuri 1f at f42
    y "Herkesin ismini ayrı ayrı kağıtlara yazıp bir şapkaya koyabiliriz."
    y "Çekilen ismin belirlediği etkinlik, herkesin hoşlandığı bir şey olmalı. Mesela Natsuki'nin adı çekilirse, hepimiz manga okuyabiliriz."
    y "Bu, ilgi alanlarımızı genişletmemize yardımcı olurken, seçim sürecinin tamamen adil olmasını sağlar."
    show monika 1b at f41
    show yuri 1e at t42
    m "Peki, diğerleri ne düşünüyor?"
    show monika 1a at t41
    show sayori 1c at f44
    s "Bana gayet iyi bir fikir gibi geldi."
    show sayori 1x at t44
    show natsuki 4b at f43
    n "Fena olmayabilir, ama eğer saçma bir şey çıkarsa orada olmayın."
    show natsuki 4c at t43 zorder 2
    show sayori 4q at t33 zorder 1
    s "Seni zorla götürürüm o zaman!"
    s 4r "Ehehe~"
    
    mc "Hadi o zaman, şimdiden çekilişi yapalım, ayrıntıları sonra hallederiz."
    show yuri 1b at f42
    y "Katılıyorum. Ben hallederim."
    hide monika
    hide yuri
    hide natsuki
    hide sayori 
    with wipeleft
    "Yuri herkesin ismini yazıp yanımıza gelir ve bir şey ister."
    show yuri 1b at f21
    y "Bunları koymak için bir şeyler lazım, bir şapka gibi bir şey."
    show yuri 1a at t21
    show natsuki 1b at f22
    n "Benim bir kedi bereim var, iş görür mü?"
    hide natsuki
    "Natsuki çantasından bir bere çıkarıyor. Üzerinde şirin bir gri kedi tasarımı var, bu durumun onun tarzı olduğunu düşündürür."
    hide yuri
    show natsuki 1c at f11
    mc "Bere senin, o yüzden isimleri sen çekmelisin Natsuki."
    "Bir kaç dakika içinde çekiliş bitmişti. Natsuki çekilen kağıda bakıyor ve okuyor."
    n 1b "[player]."
    mc "Hah, ne? Ben mi?"
    n 4b "Evet, sen."
    "Çekilişi kazanmayı beklemiyordum aslında. Sonuçta sadece 5'te 1 şansım vardı ama her şey şimdi bana kaldı."
    show monika 1b at f21
    show natsuki 1c at t22
    m "O zaman, ne tür bir etkinlik düşündün?"
    hide monika 
    hide natsuki
    menu:
        "Evet, etkinlik... Ne yapacağıma karar vermedim. Ama hem ben hem de Natsuki'nin keyif alacağı bir şey olmalı."
        "Bir şeyler pişirmek":
            call choiceBaking
        "Anime izlemek":
            call choiceAnime
        "Manga okumak":
            $ readManga = True
            call choiceManga
    call natsukiRoute_SchoolDaysTwo_End
    return


label choiceBaking:
    mc "Hımm, cupcake yapmayı ne dersiniz?"
    
    show natsuki 1p at f11
    "Natsuki şaşkın bir şekilde bakıyor."
    show natsuki 1p at t21
    show yuri 1f at f22
    y "Gerçekten pişirme biliyor musun?"
    hide natsuki
    hide yuri
    show sayori 1x at f11
    "Sayori kulağıma fısıldıyor."
    s "Bence Natsuki'yi etkilemeye çalıştığını görmek tatlı ama sen daha sadece bir kere pişirdin, değil mi? Sadece sarcastik bir şekilde demiyorum, aslında Natsuki'nin dikkatini çekmek için daha iyi yollar var."
    show sayori 1a at t21
    show monika 1b at f22
    m "Eğer bunu seçeceksen, en iyisi Natsuki'nin çekilişi kazanmasına izin verirken, senin için de yapmamıza gerek yok."
    hide sayori
    show monika 1a at t21
    show yuri 1b at t22
    y "Bence {i}senin{/i} gerçekten sevdiğin bir şeyi seçmelisin, [player]."
    mc "Dediğin gibi."
    hide monika 
    hide yuri
    "Yani, cupcake yapmayı sevmesem de biraz fazla belli ettim galiba."
    menu:
        mc "Tamam, o zaman ben..."
        "Anime":
            call choiceAnime
        "Manga":
            call choiceManga
    return


label choiceAnime:
    mc "Hadi gelin, birlikte biraz anime izleyelim?"
    show natsuki 1b at f11
    n "Fena fikir değil aslında."
    show natsuki 1c at t22
    show sayori 1c at f21
    s "Okulda bir A/V odamız var, sanırım oradan bir projektör alabiliriz."
    show natsuki 1c at t33
    show sayori 1a at t32
    show monika 1b at f31
    m "Karar verildi o zaman! Ben gidip kullanabileceğimiz bir şey var mı bakarım."
    hide monika
    hide sayori
    with wipeleft
    show natsuki 1b at f11
    n "Peki, ne izleyeceğiz o zaman, [player]? Umarım iyi bir şey seçersin."
    show natsuki 1a at f11
    mc "Hadi canım, zaten güzel zevkim olduğunu biliyorsun."
    n 1b "Hala tartışılır bu."
    mc "Söz veriyorum, iyi bir şey seçeceğim."
    "Derin bir nefes alıp, akıllıca bir şey söylemeye hazırlanıyorum."
    show natsuki 1q at hf11
    mc "Aslında anime önemli değil. Önemli olan seninle vakit geçirmek."
    show natsuki 1i at f11
    mc "...ve tabii ki diğer kulüp üyeleriyle!"
    "Eh, bence yarım akıllıca bir şeydi. Ama Natsuki pek ikna olmuş gibi görünmüyor."
    n "Y-Ya, kulüp işte."
    n 4w "Neyse, konuyu dağıtıyoruz."
    mc "Bekle, Monika şimdi gidiyor dedi, o zaman bugün mü yapıyoruz?"
    hide natsuki
    show monika 5a at l41
    m "Aslında hemen şimdi!"
    "Dönüp, kulüp odası kapısının önünde Monika'yı görüyorum."
   
    show monika 1a at t31
    
    hide monika
     
    with wipeleft
    hide window
    scene bg club_day with wipeleft_scene
    pause(1.0)
    window show
    "Birkaç dakika sürüyor, ama Monika ve Yuri bir laptop ve projektörle geri dönüp her şeyi kuruyor."
    "Bu arada, Sayori, Natsuki ve ben birkaç masayı itip, yerde rahatça izleyebilmek için yer açıyoruz."
    mc "Tamam, son masa da yerleştirildi..."
    "Oh."
    "Yanımda Natsuki'yi oturtmayı umuyordum, ama Yuri ve Sayori'nin zaten yanına oturduğunu görüyorum. Anında bir bahane bulup, Natsuki'yi buraya çekmeye çalışıyorum."
    mc "Natsuki, buraya gel! Orada bir parlama var, buraya gelmen daha iyi olur."
    "Evet, aslında orada hiç parlama yoktu ama..."
    
    show natsuki 5q at f44
    n "Her neyse, bunu sadece parlama yüzünden yapıyorum, o yüzden aklından başka şeyler geçirme."
    hide natsuki
    "Bir saat kadar geçti, hepimiz değişik anime türleri izledik. Natsuki ve ben yalnızca ilgilendik, ama diğerleri hala eğleniyor gibiydi, bence bu da başarılı sayılır."
    "Normalde burada bitmesi gerekirdi, ama Natsuki'ye bir bakış attım ve fark ettim ki farkında olmadan büyük bir hata yapmışım."
    "Kendi kendime mırıldanıyorum."
    mc "Aman Tanrım!"
    show natsuki 1c at f11
    n "Hmm?"
    mc "Hiçbir şey."
    hide natsuki with dissolve_cg
    "Gerçekten omzuma kolumu mu attım? Hem de herkes izlerken? Bu inanılmaz derecede garip. Gizlice, elimden geldiğince sessizce kolumu çekiyorum."
    show natsuki 1q at f11
    n "Bırak orada kalsın."
    mc "Ne?!"
    n 1i "Zaten üşüyordum."
    mc "Anladım."
    return

label choiceManga:
    mc "Hadi manga okuyalım mı?"
    show yuri 1b at f11
    y "Manga, benim tercih ettiğim okuma şekli değil ama yine de sorun değil."
    show yuri 1a at t22
    show natsuki 1b at f21
    n "Buna sıcak bakıyorum, zaten bunu tahmin etmiştin."
    show natsuki 1a at t31
    show yuri 1a at t32
    show sayori 1c at f33
    s "Peki, nasıl olacak? Hepimiz aynı kitaptan mı okuyacağız?"
    show natsuki 1a at t42
    show yuri 1a at t43
    show sayori 1a at t44
    show monika 1b at f41
    m "Biraz sıkışık olabilir, eğer öyle yaparsak."
    show monika 1a at t41
    mc "Hepimiz farklı kitaplar okuruz belki, sonra bitince düşüncelerimizi paylaşırız?"
    hide natsuki
    hide sayori
    hide yuri
    show monika 2b at f11
    m "Pek sosyal bir grup etkinliği sayılmaz, ama yine de senin kararın."
    m "Hadi yapalım o zaman."
    hide monika with wipeleft
    mc "Natsuki, herkes için bir seri seçer misin?"
    mc "Ben de sana yardım ederim, herkesin sevdiği bir şey seçmeye."
    "Herkese bir manga seçtikten sonra, hepimiz sessizce kitaplarımıza açıp okumaya başlıyoruz."
    
    "Natsuki ve ben aynı mangayı okumayı seçtik, çünkü uzun zamandır bunu yapıyoruz. Parfait Girls'in spin-off'u olan 'Ice Cream Sundae Girls'ı seçtik."
    "Bittiğinde, Natsuki'ye ne düşündüğünü soruyorum."
    show natsuki 4b at f11
    n "Fena değil. Spin-off için iyi bir deneme ama Parfait Girls'in asıl amacını kaçırmış."
    show natsuki 4a at f11
    n "Yine de keyifliydi."
    mc "Evet, katılıyorum. Fena değildi ama o kadar işte."
    show natsuki 4a at t11 zorder 2
    $ saveLocked = False
    n "Neyse, artık bunu okudun diyebilirsin, değil mi?"
    
    "Bunu okuduğumla gururlanacağım çok bir durum yok ama, kim bilir belki bir gün?"
    
    "Yine Natsuki'ye bakıyorum ve gerçekten şaşırtıcı bir şey fark ediyorum."
    "Gerçekten el ele mi tutuyoruz? Ama ne zaman oldu bu? Ben mi yoksa o mu yaptı?"
    "Şimdilik sessiz kalmalıyım. Ama Monika yaklaşırken..."
    show monika 5 at t21 zorder 1
    m "Beni gördüğünüzde eğlendiğiniz belliydi."
    "Natsuki ve ben aşağıya bakıyoruz ve bunu ilk kez gördüğünü düşünüyorum."
    show natsuki 1o at t22
    n "Ahh! Hayır!"
    show natsuki 1p at t22
    "Hızla ellerimizi çekiyoruz."
    m "Aww, eğlenmediniz mi?"
    n "Hayır, eğlendik! Ama, işte..."
    show natsuki 5q at t22
    m "Hımm?"
    n "Senin işin değil!"
    show natsuki 5s at t22
    "Natsuki, arasında bizde bir şey olup olmadığını açıkça reddetmek yerine, Monika'ya biraz geri durmasını söylüyor."
    "Bunun ilerleme sayılabileceğini merak ediyorum. Hmm..."
    return

label natsukiRoute_SchoolDaysTwo_End:
    scene bg club_day with Dissolve(2.0)
    "Gerçekten ne olduğunu anlamıyorum ama sonrasında günün geri kalanı bir şekilde geçti. Tamamen eğlendim ve yarını sabırsızlıkla bekliyorum."
    "Hayat her zamankinden daha parlak görünüyor. Artık hiçbir şey onu aşağı çekemez gibi hissediyorum."
    window hide
    stop music fadeout 2.0
    show black with Dissolve(2.0)
    pause(2.0)
    
    call natsukiRoute_Stress
    return
label natsukiRoute_Stress:
    
    scene bg bedroom with open_eyes
    play music Thoughts fadein 2.0
    window show
    "Bugün çok mutlu hissediyorum."
    "Belki Natsuki yüzünden ya da belki değil, ama gerçekten."
    "Uzun zamandır böyle iyi hissetmemiştim."
    "Neyse ki, hayat bazen mutluluğun kısa süreli olmasını sağlıyor, çünkü bu sabah Natsuki'den endişe verici bir mesaj alıyorum."
    
    p"seninle konuşmam lazım"
    "Bu, Natsuki'nin genelde kullandığı emojili ya da simgeli yazışma tarzından çok farklıydı. Bunun yerine, daha ciddi bir ton vardı."
    "Tabii ki bu, kötü bir şey olduğu anlamına gelmiyordu. Belki de hiç önemli bir şey değildir."
    "Ama bu mesajın ne anlama gelebileceğini düşünmek bile beni korkutuyor. Daha önce her şeyin yolunda gideceğini düşünürken, şimdi gerçeğe dönmüş gibiyim."
    "Ona ne olduğunu sordum, birkaç dakika geçtikten sonra bir cevap aldım."
    p "hiçbir şey"
    p "boşver"
    "O 'hiçbir şey' değil. Kesinlikle bir şeyler oluyor ama Natsuki bana söylemek istemiyorsa, o zaman yapacak bir şey yok."
    "Bu benim işim değil, değil mi? Ama keşke olsaydı. Keşke yardımcı olabilseydim. Şu an yapabileceğim tek şey, onun isteklerine saygı göstermek."
    "...Tabii ki, belki de bunu çok derin düşünüyorumdur."
    
    scene bg club_day with Dissolve(2.0)
    stop music
    show natsuki 4c at t44
    "Literatür Kulübüne girdiğimde, her zamanki tanıdık manzarayı görüyorum."
    "Sayori ve Monika şiirleri üzerinde çalışıyor."
    "Yuri köşede bir kitap okuyor."
    "Ve Natsuki tek başına bir masada oturuyor."
    show natsuki 4c at f11
    "Natsuki'nin yanına gidiyorum ve yanına oturuyorum."
    mc "Merhaba."
    
    "Natsuki monoton bir şekilde konuşuyor."
    show natsuki 4e at f11
    n "Selam."
    mc "Biraz manga okusak mı?"
    n "Ne istersen."
    
    hide natsuki with wipeleft
    "Önce bunun benim işim olmadığını söyledim ama yalan söyleyemem, en azından merak etmiyorum dersem."
    "Yine de duygularına saygı göstermeliyim. Şimdilik manga okumaya devam edeceğiz ve eğer onunla ilgili bir şey olursa, zamanla öğrenirim."
    if(readManga is True):
        "Dolaba gidip, Ice Cream Sundae Girls'ın bir sonraki cildini arıyorum. Bulduğumda masaya geri dönüyorum."
        show natsuki 4c at f11
        n "Yine Ice Cream Sundae Girls mı?"
        mc "Evet, geçen sefer okuduklarımız orta seviyedeydi ama kim der ki seri zamanla daha iyiye gitmez?"
        n "Ben. Seriyi okudum."
        n "Zamanla daha iyiye gitmez."
        mc "Ahh."
    else:
        "Dolaba gidip, Parfait Girls'ın bir sonraki cildini arıyorum. Bulduğumda masaya geri dönüyorum."
        show natsuki 4c at f11
        n "Yine Parfait Girls mı?"
        mc "Evet, bu özel arcın başlangıcı pek iyi değildi ama kim der ki zamanla daha iyiye gitmez?"
        n "Ben. Tam arcı okudum."
        n "Zamanla daha iyiye gitmez."
    show natsuki 4u at f11
    n "Yine de bana oku, tamam mı?"
    mc "Yine yorgun musun yoksa?"
    n "Evet, bir şeyler var."
    n "Bugün kendimi pek iyi hissetmiyorum."
    mc "Her zaman yardımcı olmak isterim, biliyorsun."
    n "Bakalım."
    "Bakalım mı?"
    "Bu ne demek? Yani, aslında kendimi oldukça güvenilir bir adam olarak görüyorum. Söylediğini yanlış mı anlamışım?"
    n "Hadi ama, oku zaten."
    mc "Tabii, hemen."
    hide natsuki with wipeleft
    
    "Bu... işte böyle geçti bir gün. Sonra eve geri döndüm, her zamanki gibi endişeliyim."
    window hide
    
    scene bg bedroom with Dissolve(2.0)
    window show
    "Farkına varmadan sabah oldu."
    "Natsuki'den bir mesaj daha geldi, bu defa beni daha da endişelendirdi."
    p "bunu boşver"
    "Bunu boşver mi? Ne için endişelenmemeliyim?"
    "Bunu söylemek, beni daha çok endişelendirdi. Ama neden?"
    "Natsuki hakkında çok fazla şey bilmiyorum. Biliyorum ki mükemmel bir hayatı yok ama hiçbiri bizinkiler gibi."
    "Bunun için gereksiz yere mi bu kadar endişeleniyorum? Bir hafta sonra, hatta bir ay sonra bu durum önemli olacak mı?"
    "Şu an olduğu gibi, Natsuki'nin yanındayım ve başka hiçbir şey beni daha mutlu edemez."
    "Eğer bunu yapmaya devam edebileceğimse, en azından."
    
    scene bg club_day with wipeleft_scene
    show natsuki 4c at t44
    "Literatür Kulübü'ne geri döndüm ve yine yalnız bir masada oturan Natsuki'ye yaklaştım."
    show natsuki 4c at f11
    mc "Ne var ne yok?"
    n 4e "Hiçbir şey."
    "Ama bu gerçekten hiçbir şey olduğuna inanmıyorum. Oldukça mesafeli duruyor, her zamankinden farklı."
    mc "Daha önce de söylediğim gibi, ne zaman konuşmak istersen ben buradayım."
    n 4c "Tamam."
    "Gene manga okudum ona, ama hiç o kadar keyif alıyormuş gibi görünmedi. Ama ne yapabilirim ki, değil mi?"
    hide natsuki
    scene bg bedroom with wipeleft_scene
    "Bir başka gün geçti, başka bir sabah ve başka bir mesaj."
    p "söyledim, endişelenme"
    "Bu, benim şüphelerimi doğruladı, yani büyük bir şeyin olduğunu hissediyorum. Ama ne olduğunu bilmiyorum ve kolayca bulabileceğimi de sanmıyorum."
    scene bg club_day with Dissolve(2.0)
    show natsuki 42b at t11
    "Günün geri kalanı, Natsuki'nin bana soğuk davranmasıyla geçti, yani artık buna alıştım."
    "Birkaç gün boyunca aynı şeyler tekrarlandı. Natsuki bana daha da mesafeli yaklaşmaya devam etti, ta ki bir gün..."
    hide natsuki
    show black with Dissolve(2.0)
    "Bir gün her şey farklıydı."
    scene bg bedroom with open_eyes
    "Her zamanki gibi telefonumu kontrol ederek uyandım ve Natsuki'den bir mesaj aldım."
    "Bu beni en çok endişelendiren mesaj, çünkü bu geçen hafta boyunca bir şeylerin biriktiğini hissediyorum ve sonunda ne olduğunu öğreneceğim gibi."
    
    p "bir şeyi netleştirmeliyiz. herkes gittikten sonra literatür kulübü çok iyi olur."
    scene bg club_day with wipeleft_scene
    show natsuki 4g at t44
    "Ve işte buradayım, Literatür Kulübü'nde. Hiçbir manga almayı bile düşünmeden, Natsuki bana uğraşmamamı söylüyor."
    show natsuki 4g at f11
    "Böylece oturduk. İkimiz de aynı anda hem sıkılmış hem gergindik, bugünün nereye gideceğinden habersizdik. Ama Natsuki'nin benden daha fazla bildiği kesin."
    "..."
    "..."
    "Birkaç saat gibi bir şey geçti, sonra Natsuki etrafına bakmaya başladı."
    n 4g "Tamam, herkes gitti."
    mc "Bana ne söylemek istiyordun?"
    n 4u "Nereden başlayayım?"
    n "Her şey o kadar karışık ki. Bir şeylerin doğru olup olmadığını anlamaya çalışıyorum ama sana bunu söylemek iyi bir fikir mi, ondan da emin değilim."
    n "Düşününce, aslında iyi bir fikir değilmiş. Neden sana o mesajı attım ki?"
    n 4w "Saat 2'de karar vermek doğru muydu, neden buna inandım ki?"
    n "Neyse, önemli değil."
    n 4u "Şu anda tek söylemem gereken şey..."
    show natsuki 1g at hf11
    "Natsuki, parmaklarını endişeyle ovuşturarak bir an bekledi ve sonra masaya yumruklarını vurdu, beni şaşırtarak."
    play music Dusk fadein 2.0
    n "Ne var seninle?!"
    mc "Ha?"
    n "Hadi ama, gitmeyi düşündüm. O yüzden hala buradayken ne istiyorsun?"
    mc "Ne demek istiyorsun? Biz arkadaş değil miyiz?"
    n "Sana o kadar soğuk davrandım! Senin gitmeni istedim, kendimi yalnız kalmaya zorladım."
    n "Ama neden işe yaramadı? Neden hala gitmedin?"
    n "Ne kadar kaba olursam olayım, aslında o kadar da acımasız olamam."
    show natsuki 1g at f11
    mc "Natsuki, ben..."
    stop music fadeout 3.0
    play music AfterAll fadein 3.0
    "Neyin peşinde olduğumu anladım. Natsuki'nin niyetini ya da herhangi bir şeyi çözmeye çalışmak falan değil. Sonra düşünebilirim bunları."
    "Ama şu an anlamam gereken şey şu: {i}Burası anıydı{/i}. Bu an."
    "Çünkü şimdi değilse, ne zaman?"
    "Bunu söylemem gerek."
    mc "Çünkü senin yanında olmak istiyorum."
    show natsuki 12c at f11
    mc "Çünkü sana güvenebilmeni istiyorum."
    show natsuki 12b at f11
    mc "Çünkü her durumda sana yardım etmek istiyorum."
    show natsuki 12a at f11
    "Derin bir nefes alıyorum."
    mc "En önemlisi de, seni çok seviyorum."
    "Natsuki şok olmuş durumda. Birkaç saniye boyunca orada durdu, sonra gözlerinden yaşlar süzüldü."
    show natsuki 12i at f11
    n "Bunu benim için kolaylaştırmak zorundasın, değil mi?"
    n "Bunu söylesen de ben seni seviyorum ama, mesele bu değil."
    n "Ben... böyle yaşayamam."
    hide natsuki with Dissolve(1.0)
    "Natsuki gözyaşları içinde bana sarıldı. Her şey o kadar hızlı gelişiyor ki, düşünmeye fırsatım yok."
    mc "Dediğim gibi, her zaman senin yanında olacağım. Bu bir söz, Natsuki."
    "Natsuki'nin sözleri, hıçkırıkları arasında çıktı."
    show natsuki 12g at f11
    n "Anlamıyorum. Biri neden bana bu kadar nazik davranmalı?"
    mc "Derin nefes al, Natsuki. Her şey yoluna girecek ve ben bunun garantisini veriyorum."
    show sayori 1m at t41
    "Zaman sanki donmuş gibiydi. Sayori dışında, ki o da geçtiği sırada onu kovalamak zorunda kaldım, sonuçta bunun şimdilik pek önemi yok."
    hide sayori with Dissolve(1.0)
    "Şu an tek önemli şey, Natsuki'yi rahatlatmak."
    mc "Bana güvenebilirsin, Natsuki. Ne durumda olduğunu bilmiyorum ama sana güvenebileceğinden eminim."
    "Natsuki bir şeyler söylemeye çalıştı ama o kadar yorulmuştu ki, ağzından tek kelime çıkmadı."
    mc "Sadece rahatla."
    show natsuki 4s at f11
    "Ve rahatladı. O kadar rahatladı ki, hala kollarımda uyuyakaldı."
    hide natsuki with wipeleft
    "..."
    "Evet, güzel bir duygu oldu ama sonunda bir süre ayakta durmaktan sıkıldım."
    mc "Tamam, Natsuki."
    "Natsuki yavaşça uyandı ve esnedi."
    show natsuki 1c at f11
    n "Hı? Ne oldu?"
    mc "Hiçbir şey olmadı."
    mc "Kötü bir gün geçirdin ve her şeyi dışarıya vurman gerekiyordu. Hepsi bu."
    n 2q "Ciddiyim, sana karşı duygularım var ama... karmaşık."
    mc "Evet."
    "Aklımda bir çözüm ararken, hafta sonu neredeyse geldi, belki..."
    mc "Yarın okul yok, bir fikrim var. Kabul etmek zorunda değilsin ama bence yapmalısın."
    mc "Bir gün geçirelim, tüm kötü şeyleri unutalım. Mesela bir yere yemek yemeye gidebiliriz."
    mc "Buna 'randevu' demek zorunda değiliz, sadece bir rahatlama günü. Bunun sana uygun olduğunu düşünüyor musun?"
    show natsuki 1a at f11
    "Natsuki kısa bir şekilde gülümsedi."
    n "...Tabii."
    mc "O zaman karar verildi! Detayları sana yazacağım, tamam mı?"
    n "Anladım."
    n "Sabırsızlıkla bekliyorum galiba..."
    show natsuki 1a at t41
    "Natsuki sınıftan çıkmaya başladı."
    n 1q "Ve... teşekkür ederim."
    mc "Her zaman."
    hide natsuki with wipeleft
    stop music fadeout 1.0
    play music Thoughts fadein 1.0
    window hide
    scene bg residential_day with Dissolve(2.0)
    scene bg bedroom with Dissolve(2.0)
    window show
    "Bundan kısa bir süre sonra evime doğru yürümeye başladım ama ancak yatağımda yattığımda her şey gerçekten yerleşti."
    "Cidden. {i}Natsuki'ye itiraf ettim{/i}. Gerçekten yaptım. Ve o da beni sevdiğini söyledi mi? Şaşkınım."
    "Şüphelerim vardı tabii ama bunu gerçekten duymak? Duygu inanılmaz."
    "Karmaşık olduğunu söyledi. Ne anlama geldiğini bilmiyorum ama şu an için önemli değil."
    "Şu an düşündüğüm tek şey yarın ve bunun harika bir gün olacağı."
    "Gerisi ne olursa olsun önemli değil."
    "Şu an tek düşündüğüm şey {i}şu an{/i}ki duygularım."
    stop music fadeout 3.0
    window hide
    show black with Dissolve(3.0)
    
    scene bg bedroom with open_eyes
    window show
    play music aNewDay fadein 2.0
    "Bir gün, her şeyden uzak bir şekilde. Huzurlu bir gün, hayatımızdaki boş bir gün gibi hissedilen bir gün."
    "O gün bugündü."
    "Natsuki ile akşam yemeğine gitmemize kadar daha epey vakit vardı. O zamana kadar ona saçma sapan şeyler hakkında mesaj attım."
    "O, en sevdiği animelerden bahsetti, ben de kendi favorilerimden. Böyle sohbet etmek güzel hissettirdi ve farkına bile varmadan saat neredeyse 7 olmuştu."
    stop music fadeout 2.0
    scene bg house_entrance_night with Dissolve(2.0)
    play music NatTheme fadein 2.0
    show natsuki 1ba at f11
    "Bir süre sonra kapı çaldı ve kapıyı açtığımda, Natsuki'yi, uzun bir aradan sonra ilk kez mutlu bir şekilde gördüm."
    mc "Sanırım hazırsın, öyle mi?"
    n 1bb "Evet!"
    "Ve böylece başladı."
    window hide
    scene bg streets_night with Dissolve(1.5)
    window show
    show natsuki 1bj at f11
    "Gittiğimiz restoranı seçtim. Oldukça şık bir yerdi, ya da en azından normalde gitmeyeceğim bir yerdi."
    "Ama bu özel bir gündü, değil mi? Bazen konfor alanımın dışına çıkmaktan bir sakınca yok."
    
    scene bg restaurant with wipeleft_scene
    show natsuki 1bj at f11
    "Restoranın kapısından içeri adım attık ve hemen kasanın arkasındaki görevliye yöneldim."
    mc "Dün iki kişilik rezervasyon yaptırmıştım."
    $ o_name = "Host"
    o "Tabii, efendim."
    show natsuki 1bd at f11
    "Natsuki sırıtıyor."
    n "Efendim mi?"
    mc "Bence bana oldukça yakıştı."
    n "Ne diyorsun, {i}efendim{/i}."
    $ o_name = "Host"
    o "Ahem. Adınız?"
    mc "[player]."
    o "Soyadınız?"
    "..."
    scene bg restaurant with wipeleft_scene 
    "..."
    o "...Anladım."
    hide natsuki 
    "Bize masamız gösterildikten sonra oturduk ve önümüzdeki menülere göz attık."
    show natsuki 4bp at f11
    n "Ne demek istiyorsun?!"
    "Menüden kafamı kaldırıp ona bakıyorum."
    mc "Ne oldu?"
    n 4bw "Bana çocuk menüsü verdiler!"
    mc "Gerçekten mi?"
    n "Evet! İnanabiliyor musun?"
    "Natsuki, çocuk menüsü olduğunu gösteriyor."
    mc "İyi, aslında böyle bir hata yapmaları hiç de şaşırtıcı değil."
    n 4be "Ama işte, küçük olabilirim ama bu kadar da değil. Ben hâlâ 12 yaşında değilim, çocuksu bir menüye ihtiyacım yok!"
    "Yanımızdan geçerken bir çalışan, bir şeylerin ters gittiğini fark etti ve hızla yanımıza geldi."
    $ o_name = "Employee"
    o "Bir problem mi var?"
    n 4bc "Evet, ben çocuk değilim! Neden bana çocuk menüsü verdiniz?"
    mc "Önemli değil, ama ona başka bir menü getirir misiniz lütfen?"
    o "Tabii, bir dakika."
    "Çalışan uzaklaşıyor."
    n 4be "Söylemek istediğim şey bu!"
    mc "Natsuki, lütfen..."
    n "Kısa olmamın hiçbir anlamı yok! Kısa yetişkinler de var, biliyor musun? Hem de bazıları benden çok daha çekici! Ama tabi ben onlardan daha iyi görünüyorum, hâlâ."
    "Sığ bir iç çekiş yapıp etrafa bakıyorum, birkaç kişi bize bakmaya başlamış."
    mc "Haklısın. Ama lütfen çok dikkat çekmemeye çalışalım."
    show natsuki 5bo at t11
    "Natsuki geriye yaslanıyor, kollarını kavuşturuyor ve somurtuyor."
    show natsuki 4bb at t11
    n "Ama bu gerçek, değil mi?"
    "Ve o an, o çalışan menüyü tekrar getirmeye başlıyor."
    o "İşte efendim."
    "Çalışan masadan uzaklaşırken ben bir kaşımı kaldırıyorum."
    mc "Ve sen bana 'efendim' demiştin, değil mi?"
    show natsuki 4bt at t11
    n "En azından ben unvanımı hak ediyorum."
    mc "Bana ne diyebilirim ki?"
    mc "Ama şimdi menülere bakalım."
    hide natsuki with wipeleft
    "İkimiz de menülere göz atıyoruz. Natsuki'nin yüz ifadesine bakarak, menünün arkasında bir şaşkınlık sesinin geldiğini düşünüyorum."
    show natsuki 4bc at t11
    n 4bc "Bu kadar mı pahalı? Bu kesinlikle bir yazım hatası olmalı."
    mc "Hayır. Burası lüks bir restoran, lüks fiyatlarıyla."
    n 4be "[player], ne düşünmüştün? Bu kadar para harcamanın anlamı yok, ama ben de sana bu kadar para harcatamam!"
    mc "Neden olmasın?"
    n 4bc "Bu hiç de doğru olmaz."
    mc "Bak, bu benim param. Hem, yeterince param var, o yüzden başka neyle harcayacağım ki?"
    "Tabii ki yalan söylüyorum. Neredeyse iflas etmiş durumdayım ama o an böyle söyledim."
    show natsuki 4bc at f11
    "Her neyse, yavaşça ona daha yakınlaşıyorum."
    mc "Ama sen buna değer birisin."
    show natsuki 4bs at t11
    "Natsuki şaşkın bir şekilde ne diyeceğini unutuyor."
    mc "Bir şekilde paramın karşılığını almak zorundayım. Belki sana yediririm, çünkü hatıralar, paradan çok daha değerli falan, ne bileyim."
    show natsuki 1bp at t11
    "Natsuki daha da şaşırmış görünüyor."
    n "N-Ne...?"
    mc "Şaka yapıyordum! Eğer beni beslememi istiyorsan, belki~"
    "Ne oluyor? Ne zamandan beri bu kadar özgüvenliyim? Hem de ne demek ' ~ '?!"
    show natsuki 4bs at t11
    n "O-O zaman ne istiyorsan hemen sipariş veriyorum!"
    show natsuki 4bj at t11
    "Natsuki menüsünü tekrar kaldırıyor ama bunu yapmadan önce, yüzünde bir gülümseme yakalıyorum. Demek ki pek de fena yapmamışım, sanırım."
    "Yemek siparişlerimizi verdikten sonra kendimize ait bir anımız oluyor."
    mc "Hoş bir yer, değil mi? Bulabildiğim en şık restoran burasıydı."
    n 4bb "Ama bu, seni soymalarına göz yummak anlamına gelmez."
    n "Bu arada menüdeki en ucuz şeyi sipariş ettim. O yüzden teşekkürler."
    mc "Dediğim gibi, sen buna değersin. Güzel bir yer seçmek istedim, hatırlanacak yemekler."
    n "Ya da belki yemekleri hatırlayacağız ama yanlış sebeplerle."
    mc "Hala gerginsin gibi görünüyor."
    "Ellerimi onun ellerinin yakınına koyuyorum."
    mc "Bunu yapabilir miyim?"
    "O başını sallayarak onaylıyor ve ellerimizi birbirine bağlıyoruz."
    mc "Şu anda her şeyi unut ve anın tadını çıkar."
    n 4bh "V-Vay, sen bu romantizm işini pek fena yapmıyorsun aslında."
    n "B-Bu önemli değil! Zaten biz bunun bir randevu olmadığını söyledik!"
    "Bu an mükemmeldi."
    $ o_name = "???"
    o "Siparişiniz?"
    "Neyse."
    mc "Uh, teşekkürler."
    "Arkamızda bir çalışan, her birimizin yemeklerini masaya getiriyor."
    $ o_name = "Waiter"
    o "Afiyet olsun."
    "Çalışan uzaklaşıyor, biz de yemeklerimize dalmaya hazırlanıyoruz. Ben kızarmış ıstakoz sipariş ettim, Natsuki ise makarna ve peynir."
    mc "İtiraf etmelisin, bu eğlenceli değil mi?"
    n 1bb "Evet. Hayattan biraz uzaklaşmak güzel."
    n "Ama şunu söylemeliyim ki, bu makarna ve peynir..."
    "Natsuki yemeğinden bir lokma alıyor."
    n "Eh."
    "Tabak, oldukça kusursuz. Peynirin tam olarak erimiş ve rendelenmiş miktarı var."
    "Tabii, belki de sadece sıradan bir makarna ve peynir gibi görünüyor, ama kim bilebilir?"
    mc "Bu... oldukça farklı bir makarna ve peynir, değil mi?"
    mc "Eğer istersen, biraz yemek paylaşırım seninle."
    n "Hayır, ben ıstakozdan pek hoşlanmam."
    "Natsuki parmaklarıyla oynuyor ve sessizce bir şeyler söylüyor."
    n 4bq "Ama, şey, teşekkürler... Teklifin için."
    hide natsuki with dissolve_cg
    "Vay, gerçekten harika hissettiriyor. Sanki nihayet ona ulaşabildim, ki tek istediğim buydu."
    window hide
    
    window show
    "Yemeklerimizi bitirince, bir çek yazıyorum ve çıkmaya hazırlanıyorum. Natsuki'nin utangaç bir şekilde bana baktığını fark ediyorum."
    show natsuki 1bc at f11
    mc "Bunu bir daha yapmalıyız."
    n 1bq "Düşüneceğim."
    "Bu kesinlikle bir hayırdan daha iyi, herhalde."
    n 1bl "Her şey için teşekkürler, [player]. Gerçekten seninle vakit geçirmek çok keyifliydi."
    mc "Ben de, Natsuki."
    mc "Birkaç gün sonra okulda görüşürüz, o zaman mı?"
    n "Evet."
    show natsuki 1bs at f11
    "Birbirimizin gözlerine kısa bir süre bakıyoruz, ama her ikimiz de ne yaptığımızı fark edip hemen bakışlarımızı kaçırıyoruz."
    mc "Haha, bu neden tanıdık geliyor?"
    mc "Eh, hadi bakalım. Görüşürüz."
    n "Hoşça kal."
    show natsuki at lhide
    hide natsuki
    "Ve işte, uzun bir zamandır yaşadığım en huzurlu günün sonuydu."
    stop music fadeout 2.0
    
    scene bg bedroom with Dissolve(1.5)
    play music Thoughts fadein 2.0
    "Bugünkü başarının ardından, yatağımda oturup buna dair düşünmeye karar veriyorum."
    "Bugün pek çok şey ters gidebilirdi, ama gitmedi. Bugün saf bir mutluluk gibiydi. Gerçekten böyle bir günün hatırlanabilir olması harika."
    "Birçok anıma bakınca mesela, mutlu görünüyorlar ama aslında sadece o an mutlu olmamı sağlıyordu. Geriye kalan zaman rezaletti."
    "Ama bugün her şey harikaydı. Umarım her şey böyle devam eder."
    "Muhtemelen etmez, ama bununla yarın baş ederim, eğer gelirse."
    "Ama şimdilik, uyuma zamanı."
    window hide
    $ o_name = "???" 
    stop music fadeout 2.0
    show black with Dissolve(2.0)
    
    pause(2.0)

    scene bg bedroom with Dissolve(1.5)
    window show
    play music aNewDay fadein 2.0
    "Genelde sabahları uyanıp telefonuma baktığımda, genellikle mesaj alıp almadığımı kontrol ederdim."
    "Ama şimdi, tek amacım Natsuki'den mesaj gelip gelmediğine bakmak. Zamanla her şeyin nasıl değiştiğini görmek ilginç."
    "Bu sabah bana mesaj atmadı, bu arada. Ama tabii ki ben de ona mesaj atmadım, yine de ona mesaj atmak zorunda değilim."
    "Aslında sanırım bu hafta sonu boyunca bana hiç mesaj atmadı."
    "Neyse, hafta sonu bitti ve bugün okul var, o yüzden okula gitmek zorundayım."
    
    scene bg club_day with wipeleft
    "Sonunda Edebiyat Kulübüne vardım. Her zamanki gibi aynı manzarayı bekliyordum ama bu sefer biraz farklı, çünkü Natsuki ortada yok."
    "Meraklı ve biraz endişeli bir şekilde diğer üyelere, Natsuki'nin nerede olduğunu soruyorum."
    mc "Monika, Natsuki nerede?"
    show monika 1b at f11
    m "Sanırım bilmiyorum. Yardımcı olabileceğim bir şey var mı?"
    mc "Yok, sadece merak ettim."
    hide monika with dissolve_cg
    "Tabii ki aslında bir şey vardı, ama söylemek istemedim."
    show sayori 1a at f11
    mc "Sayori, Natsuki'yi gördün mü?"
    s 1c "Hayır! Birkaç gün önce olanlardan sonra onun nerede olduğunu sanırım senin bilmen gerekiyordu..."
    "Bir iç çekiyorum."
    mc "Evet, ben de öyle düşünmüştüm."
    hide sayori with dissolve_cg
    pause(0.5)
    show yuri 1a at f11
    "Sanırım geriye sadece Yuri kaldı, ama ondan da pek bir şey alacağımı sanmıyorum."
    mc "Yuri, Natsuki'yi gördün mü?"
    y 1b "Sanırım görmedim."
    hide yuri with dissolve_cg
    pause(0.5)
    show natsuki 4c at t41
    "Sinirli bir şekilde uzaklaşırken, Natsuki'nin içeri girdiğini fark ediyorum."
    mc "Natsuki! Bugün gelmeyecek gibi düşündüm seni."
    n 4b "Biraz yalnız kalmaya ihtiyacım vardı."
    mc "Anladım. Şimdi manga okumasak mı?"
    stop music
    play music Dusk fadein 1.0
    n "Hayır."
    show natsuki 4c at t44
    "Natsuki beni reddediyor ve bir köşeye oturuyor."
    hide natsuki
    "Eee... şimdi ne yapacağım?"
    show monika 1b at t41
    m "Natsuki!"
    show monika 1a at t32 zorder 2
    show natsuki 4c at t44 zorder 1
    "Dönüp Monika'nın Natsuki'ye doğru yürüdüğünü görüyorum."
    m 1b "Nasılsın? Normalde geç kalmazsın."
    n 1g "Zaten dedim ya, biraz yalnız kalmaya ihtiyacım var."
    "Ben de yanlarına gitmeye karar veriyorum."
    mc "Unutma, her zaman konuşmak istersen buradayım--"
    show monika 1g with dissolve_cg
    hide monika
    n 4e "Evet, biliyorum. Tekrar söylemene gerek yok."
    show natsuki 4c at t44
    mc "Ben... tamam."
    "Ne oldu? Dün her şey çok iyiydi."
    "Tabii, bilmediğim çok şey var ama Natsuki'nin bu kadar gergin olması ne demek?"
    show sayori 1c at f43
    s "Hey, Natsuki!"
    "Yine dönüp bu sefer Sayori'yi görüyorum."
    s "Nasılsın--"
    show sayori 1m at t43
    show natsuki 1e at f44
    n "Bu köşede oturuyorum çünkü! Bunu, kimseyle olmak istemediğimi açıkça belli etmiyor mu?"
    show natsuki 1c at t44
    show sayori 1g at t43
    show yuri 1h at f42
    y "Bunu kaba bir şekilde söylemek istemiyorum Natsuki, ama kimseyle olmak istemiyorsan, neden bugün geldin?"
    show yuri 1g at t42
    show natsuki 1g at f44
    n "Eğer gelmeseydim, mutlaka beni aramaya başlardınız."
    "Tamamen haklı değil mi? Ben kesinlikle onu arardım."
    hide yuri 
    hide sayori 
    hide natsuki 
    with dissolve_cg
    scene bg club_day with wipeleft_scene
    
    "Günün geri kalanını pek bir şey yapmadan geçirdim. Sayori'yle bile konuşasım gelmedi."
    "Natsuki ile vakit geçirmeye o kadar alışmışım ki, bunun nasıl olacağını hiç düşünmemiştim."
    "Geçen hafta, evet, çok hevesli değildi ama yine de oradaydı. Hala manga okuduk birlikte."
    "Peki ya şimdi? Arkadaşlığımız böyle sona ermez, değil mi? Özellikle duygularımızı birbirimize açıkladıktan sonra."
    "Şu an yapabileceğim tek şey, her zaman yaptığım gibi yanında olmaya devam etmek. Ona biraz alan verebilirim ama yine de ona destek olmak istiyorum."
    "Belki bu, onun isteklerine karşı geliyor ama hiç bir şey yapmamaktan iyidir."
    "Asla ondan vazgeçmeyeceğim."
    show black with Dissolve(2.0)
    pause(2.0)
    scene bg club_day with wipeleft_scene
    "Ve böylece başka bir gündü. Okul sanki sonsuza kadar sürüyormuş gibi hissettirdi, Edebiyat Kulübüne gitmek bile buna pek iyi gelmedi."
    show natsuki 1c at t44
    "Odaya girdiğimde, Natsuki bu sefer zamanında gelmişti, yine köşede oturuyordu. Yanına gidip bir soru soruyorum."
    show natsuki 1c at t11
    mc "Bugün kendini biraz daha iyi hissediyor musun?"
    show natsuki 1e at f11
    n "Hayır ve lütfen tekrar sorma, tamam mı?"
    mc "Tamam."

    hide natsuki with dissolve_cg
    "Hızla uzaklaşıp derin bir nefes alıyorum, geleceğin ne getireceğini bilemeden."
    show sayori 1h at t41
    s "Onu kızdırmadın, değil mi?"
    show sayori 1h at t11
    "Göz ucumla Sayori'yi fark ediyorum."
    s 1j "Ne yaptıysanız, [player]?"
    mc "Durum öyle değil, sana yemin ederim. En azından öyle olduğunu sanmıyorum."
    s 1g "Sanmıyorsun {i}değil{/i} mi?"
    mc "Yani, eğer bana söylemeyecekse, o zaman asla bilemeyeceğim, değil mi?"
    s 1h "Bence bu tamamen doğru değil. Peki, son birkaç gündür ne yaptın?"
    mc "Onu kızdıracak bir şey yapmadım. İki gün önce onu restorana götürdüm, ve o da keyif almış gibiydi."
    mc "Biz ikimiz de keyif aldık."
    s 1x "Yani, aranızda bir şeyler varmış! Bunu biliyordum!"
    mc "Sayori, mesele bu değil. Hem zaten, o... yani--"
    show sayori 1x at t21
    show natsuki 1c at f44
    n "Hımm?"
    show natsuki 1c at f22
    "Natsuki'nin kalkıp yanıma ve Sayori'ye gelmeye başladığını görüyorum."
    n 1g "Beni mi konuşuyordunuz?"
    mc "Casusluk mu yapıyordun?"
    s 1k "Gerçekten de aynı odada olduğumuz için haklısın."
    s "Ehehe..."
    n 4e "Cidden, [player]. Sadece git."
    n "Böyle daha kolay olur."
    hide sayori with dissolve_cg
    hide natsuki with dissolve_cg
    "Artık hiçbir şey anlamıyorum."
    "Sadece anlamıyorum."
    "Önümüzdeki hafta boyunca, Sayori ve ben Natsuki'ye ulaşmak için çeşitli yollar düşündük."
    "Ne yazık ki, her plan bir öncekinden daha kötüydü."
    scene bg club_day with wipeleft_scene
    "İlk denememizi hatırlıyorum. Onu açmaya çalışmak için hazırladığım plan yeterince iyiydi sanırım, ama sanırım değildi."
    show natsuki 4g at f11
    n "Unuttuğunu sanmıyorum ama git, sadece bu kadar istiyorum."
    n "Zor değil."
    hide natsuki with wipeleft

    scene bg club_day with wipeleft_scene
    "Sonraki gün bir başka deneme yaptık. Bu kez her şey daha da kötü gitti."
    show natsuki 4e at f11
    n "Kaç kere söylemem gerek? Git."
    n "Git."
    n "Git."
    n "Git."
    n "Hala anlamadın mı?"
    hide natsuki with wipeleft
    "O gün sonra, Natsuki'nin telefonunu aradım ama bir çaldıktan sonra arama kapandı."
    "Böyle bir şey olduğunda, genellikle aradığın telefonun bataryası bitmiştir, ya da..."
    "Beni engellemiş olamaz, değil mi? Çünkü ona daha önce mesaj atmadım, eğer engellediyse, bu tamamen kendi isteğiyle olmuştur."
    "Belki de üçüncü kez denemek son şansımdı. Ama olmadı."
    
    scene bg club_day with wipeleft_scene
    show natsuki 5g at f11
    n "..."
    "Ama biz denemeye devam ettik. Sonuçta, {i}ben{/i} devam etmeliydim."
    "Ya da en azından, {i}ben{/i} etmek zorundaydım. Ve böylece, başka bir gün, başka bir deneme."
    n "Saçma mısın? Kaç kere deneyeceksin? Olmayacak."
    hide natsuki with wipeleft
    "Ama içimde bir umut vardı, belki hala kazanabilirim. {i}Bir gün daha{/i}."
    scene bg club_day with wipeleft_scene

    show natsuki 42c at f11
    n "Bundan gerçekten bıktım, biliyor musun?"
    "Ne kadar sürerse sürsün, kararlıydım. Sadece bir gün daha."
    n "Bir tek dileğime saygı gösteremez misin? Ya da öldüm falan ve senin benim tek basit dileğimi yerine getirmediğini düşünmek zorunda kalsaydın, geri kalan hiçbir şeyle bunu telafi edemezdin? "
    n "Bunu nasıl hissedersin, ha?"
    show natsuki 42b at t22
    show sayori 4h at t21
    s "Ben..."
    show natsuki 42b at t33
    show sayori 4g at t32
    show monika 1d at f31
    m "Natsuki? Belki kulüpten birkaç gün uzaklaşmak istersin?"
    m "Eğer bir kulüp üyemi rahatsız eden bir şey varsa, onu halletmek isterim."
    show monika 1c at t31
    show natsuki 42c at f33
    n "Defol git, Monika!"
    hide monika 
    hide natsuki
    hide sayori with dissolve_cg
    "Ama bunu yapmak zorundaydım. Kazanmak zorundaydım--"
    show sayori 4h at f11
    s "[player], dur."

    mc "Huh?"
    s "Bana ve Natsuki'ye dair bir şeyler saklıyorsun, değil mi? O, herkese karşı kaba ama özellikle sana karşı daha da sert."
    s "Yardım etmek için buradayım, ama bunu yapabilmem için her şeyi bilmem gerekiyor."
    mc "Dediğim gibi, nasıl sinirlendirdiğimi hiç anlamadım ki!"
    "Bunu kendime defalarca söyledim ama ya gerçekten onu sinirlendirecek bir şey yaptıysam? Belki de fark etmeden, ama yine de bilemedim."
    "...Hayır, önemli değil. Her ne kadar suçlu olsam da, Natsuki'ye bunu telafi edeceğimi söyledim."
    s 4g "Ona özür dilemeni öneririm ama sanmıyorum ki şu an bir fark yaratır, değil mi?"
    mc "Bunun için çok geç kaldık."
    mc "Peki ya şimdi? Denediğimiz her şeyi denedik."
    s 1b "Bilmiyorum. Ama en azından onu rahatlatmayı denemeliyim."
    s 1c "Hey, Natsuki! Buraya gelir misin?"
    show sayori 1c at t21
    show natsuki 4g at f22
    "Natsuki gözlerini devirdi ve kalktı."
    n "Bak, gerçekten buna kalkıp bir şeyler yapmayı düşünüyorsan--"
    show sayori 1b at t43
    show natsuki 4f at t22 zorder 2
    "Sayori, Natsuki'yi sarıldığında, Natsuki'nin sözünü kesildi."
    s "Sarılmak, herkese iyi gelir, değil mi?"
    "Sayori bunu söyledi ama, Natsuki'nin yüzünde derin bir öfke vardı."
    "Bunun iyi bitmeyeceği belliydi."
    show natsuki 12e at f22
    n "SENİ NEFRET EDİYORUM!"
    show sayori 4m at t21
    show natsuki 12g at f22
    "Natsuki, Sayori'nin kollarından sıyrılıp kaçtı."
    n "Hepiniz! Hiçbiriniz anlamıyorsunuz, değil mi?"
    n "Beni yalnız bırakın!"
    n "Bu kadar basit bir şey! Eğer hiçbirinizin yalnız bırakmayı öğrenmediyseniz, o da benim sorunum değil!"
    n "Bunu yapamam."
    n "Bundan bıktım."
    n "Her şeyden."
    show natsuki 12h at lhide
    hide natsuki
    "Natsuki gözyaşlarına boğulup odadan çıktı."
    hide sayori
    mc "Natsuki!"
    "Ama çok geçti."
    "Artık hiçbir şeyi düzeltme şansım yok."
    "Bitti ve biz her şeyi mahvettik."
    "Ben mahvettim. Sayori, her şeyi daha da kötüleştirdi ama sonuçta bu benim karışıktığım bir durumdu."
    scene bg class_day with Dissolve(1.5)
    "Sonrasında ne olduğuna net olarak hatırlamıyorum. Sanırım kulüpte bir masaya yaslandım."
    "Monika ve Yuri ne olduğunu sormaya çalıştı ama yanıt vermek istemedim. Hiç konuşmak istemedim."
    window hide
    stop music fadeout 4.0
    show black with Dissolve(4.0)
    pause(2.0)
    scene bg class_night with open_eyes
    play music Dusk fadein 3.0
    "Bundan birkaç saat sonra Sayori tarafından uyandırıldım."
    s "Epey geç oldu, [player]. Benim bile okul projeleri için bu saatte kütüphanede çalışmama izin vermiyorlar ve sanırım burada uyumana da izin vermezler. Üzgünüm..."
    mc "Hayır, sorun değil. Gidiyorum."
    "Hıçkırık alarak bir süre daha oturup kalkıp saate baktım."
    "Saat 7 mi olmuş?"
   
    stop music fadeout 3.0
    scene bg streets_afternoon with dissolve_cg
    "Okuldan çıktıktan sonra bir fast food restoranına gittim çünkü evde yemek yapacak halim kalmazdı."
    "Bugün gerçekten kötü bir haldeydim ama açıkçası kimse ne düşündüğüme takılmıyordu."
    "Ama orada kalamam, değil mi? Hiçbir yerde sonsuza kadar kalamam, istediğim ve denediğim kadar, bu yüzden nihayet eve gitme zamanıydı."
    
    scene bg dark_streets with dissolve_cg
    "Eve doğru yürürken mahalleme geliyorum. Evime çıkmaya çalışıyorum ama hiç beklemediğim bir şeyle karşılaşıyorum."
    "Hayır, bir şey değil. {i}Birisi{/i}."
    scene bg natsukiCG1 with dissolve_cg
    mc "Natsuki?!"
    play music Dusk fadein 3.0
    
    n "Berbat ettim, [player]."

    
    mc "Natsuki, ne oluyor burada?"
    "Bunu görmek beni şaşırttı, özellikle de her şeyin yaşandığı şu dönemde."
    "Natsuki, veranda mı? Burada ne kadar zamandır bekliyor ki?"
    n "Beni artık sevmiyorsun, biliyorum, ama kalacak bir yere ihtiyacım var."
    mc "Tabii! Ama Natsu--"
    n "Bunun bir anlamı yok. Sadece... "
    "Natsuki bir an durup düşünüyor."
    n "Önemli değil."
    mc "Tamam, o zaman sonra konuşuruz. Burada soğuk, değil mi? Gel, içeri girelim."
    
    scene bg home_interior_night with dissolve_cg
    "Kapımı açıp, birlikte oturma odamıza geçiyoruz."
    mc "Sanırım bir süre burada kalacaksın. Herhalde tahmin edebileceğin gibi, açıklamam gereken birkaç şey var."
    show natsuki 4c at f11
    n "Sofrada yatıyorsun."
    mc "Ne--"
    mc "...Yani evet, tabii. Koltuk zaten yeterince rahat."
    "Buna karşı çıkmanın anlamı yok."
    mc "O zaman odada kalırsın, değil mi?"
    n 4e "Başka bir seçenek yok sanırım?"
    "Teknik olarak, koltukta uyuyabilir, beni zor durumda bırakmayabilirdi ama sanırım bu da sorun değil."
    mc "Tamam, o zaman odada kalırsın. Ama hiçbir şeye dokunma, tamam mı?"
    n "Açıkçası, odanda sakladığın şeyler beni o kadar tiksindirebilir ki, bakmak bile istemem."
    mc "Bunu bir iltifat olarak kabul ediyorum."
    n "Değil."
    mc "Anladım."
    show natsuki 4u at t11
    "Odada garip bir sessizlik hakim. Natsuki'nin gözlerinde, sanki biraz kaba davranıp davranmadığını düşündüğü bir korku var gibi görüyorum."
    "Acaba, başına gelenlerden dolayı içindeki duygulara mı kapılıyor?"
    mc "Eee, o zaman yarın görüşürüz."
    n "Tamam."
    show natsuki 4u at lhide
    hide natsuki
    "Natsuki bir anlığına dışarı çıkıp, çalılıkların arasında bıraktığı valizini alıyor ve odama doğru yöneliyor. Ben de büyük koltuğuma oturup, uyumak için hazırlanıyorum."
    "Yatak örtüsü yoktu ama, artık çok yorgundum, gidip almaya üşendim."
    "Şu an tek istediğim uyumak. Sadece iyi bir uyku."
    stop music fadeout 2.0
    show black with Dissolve(3.0)
    
    "{i}BZZT! BZZT!{/i}"
    stop sound
    "Natsuki'nin alarm saatimle uyandırdığını görünce, telefon alarmımı kurarak sabah uyandım. Neyse ki, onu gece boyunca şarj edebileceğim bir yer bulmuştum."
    "Ve tam da uyanınca, Natsuki'nin bir şeyler pişirdiğini görüyorum."
    scene bg kitchen with wipeleft_scene
    play music NatTheme fadein 2.0
    mc "Natsuki? Çoktan kalktın mı?"
    show natsuki 3bb at f11
    n "Senin gibi her şeyi uyuyarak geçirecek değilim."
    mc "Sanırım. Ne yapıyorsun?"
    n "Çırpılmış yumurta."
    mc "Mantıklı. Ama senin uzmanlığın pastacılık değil miydi?"
    n "Evet ama yemek yapmak da önemli bir yetenek."
    n "Genelde işlenmiş gıda tüketirim."
    n 4be "Ama senin için bir şey yapmıyorum, tabii. Mutfak senin, sen yaparsın."
    hide natsuki with wipeleft
    "Sert ama haksız da sayılmaz."
    "Ben yemek yapma konusunda pek uzman değilim, o yüzden bir kase mısır gevreği alıp geçiyorum."
    "Tam ben hazır olduğumda, Natsuki yaptığı yemeği de bitiriyor. Ben mutfak masasında otururken, o oturma odasında koltukta oturuyor."
    mc "Gerçekten yemek masasında oturmak istemiyor musun?"
    n "İyiyim."
    mc "Tamam."
    "Bütün bu soğuk tavırları sürekli sürdürecek mi? Umarım etmez."
    "Yemek yedikten sonra, ikimiz de oturmaya devam ediyoruz."
    scene bg home_interior with Dissolve(1.5)
    "Bunun nasıl gideceğini bilmesem de, kalkıp Natsuki ile konuşmak için koltuğa gidiyorum."
    mc "Sıkılırsan, manga koleksiyonumdan bir şeyler okuyabilirsin."
    show natsuki 1bc at f11
    n "Tabii."
    n "..."
    "..."
    mc "Benim halletmem gereken şeyler var. Sonra görüşürüz."
    hide natsuki with wipeleft  
    scene bg bedroom with Dissolve(1.5)
    "Kalkıp odamıza gidiyorum, aslında ne yapacağımı düşünerek."
    "...Şimdi düşündüğümde hiçbir şeyim yok. O zaman anime izlerim."
    window hide
    scene bg bedroom with wipeleft_scene
    window show
    "Bir kaç saat geçiyor ve fazlasıyla anime izleyip numaralanmış hissediyorum. Tam koltukta uyumak üzereyken Natsuki'nin sesini duyuyorum."
    n "Ne?! Bunu nereden ve nasıl buldun?"
    show natsuki 1bb at t41
    "Kollarımı gererken, dönüp bakınca, Natsuki'nin manga koleksiyonuma göz attığını fark ediyorum."
    mc "Ne hakkında konuşuyorsun?"
    "Natsuki, rafımdan bir manga cildi çıkarıyor."
    n 2bb "Bunu diyorum, aptal!"
    mc "Parfait Girls? Hiç hatırlamıyorum bunu aldığımı."
    n 4be "Ama bu sadece herhangi bir Parfait Girls cildi değil. Bu, sadece Fransa'da çıkan ve sadece yüz tane basılan özel bir sayı."
    n 4bc "Bunu neden almışsın?"
    "Evet, ben de tam olarak bunu merak ediyorum."
    mc "Bilmiyorum. Sanırım başka manga kitaplarıyla birlikte bir garaj satışında almıştım, çünkü bazen böyle alışveriş yaparım."
    mc "O zaman Parfait Girls'in benim ilgimi çekecek bir şey olmadığını düşünürdüm, ama diğer manga kitapları ilgi çekiciydi. Başka bir şey hatırlamıyorum."
    mc "Ama evet, istersen oku."
    n 4be "Nasıl okuyabilirim ki, Fransızca?"
    show natsuki 4bc at t41
    mc "Tamam, haklısın."
    mc "Fransızcam {i}mükemmel{/i} olmasa da, sanırım manga'yı çevirebilirim. Okumamı ister misin?"
    show natsuki 5bs at t41
    "Natsuki biraz gergin görünüyor."
    n "Başka bir şey okurum."
    mc "İstediğin gibi."
    hide natsuki with wipeleft
    "Belki, bu sefer biraz açılmasına fırsat verebilirim. Şu an olmasa da, belki daha sonra."
    "Dur, bugün okul var mıydı? Bu biraz rastgele oldu ama... lanet olsun."
    "Neyse ki çok geç oldu."
    "Bir kaç saat daha anime izledikten sonra, midemdeki o boşluk, bunun tadını çıkarmamı zorlaştırıyor."
    "Endişelerim beni yıkmasaydı iyi olurdu ama bazen gerçekten zor oluyor, yaşanan her şeyin farkında olunca."
    "Bunu yapmak belki erken, ama bir denemek istiyorum. Belki biraz dinlenmek, beni daha iyi hissettirir..."
    window hide
    stop music fadeout 2.0
    show black with Dissolve(3.0)
    
    play sound alarm
    "{i}BZZT! BZZT!{/i}"
    scene bg bedroom with open_eyes 
    window show
    stop sound
    "Ertesi sabah uyanıyorum ve Natsuki'yi odamın kapısında dururken görüyorum."
    show natsuki 1b at t41
    n "Artık kalktın mı?"
    n "[player], dün okul var mıydı?"
    mc "Evet, aslında... "
    n 5e "Ughh. Böyle nasıl bir şeyler yapmayı başarıyorsun?"
    show natsuki at lhide
    hide natsuki
    n "Şimdi okula gidiyorum. Kendine gel, gelmek istersen gel ama seni beklemem."
    "Natsuki kapıyı çarpıp çıkarken, yalnız kalıyorum. Telefonuma bakıp saate bakınca, neredeyse geç kaldığımı fark ediyorum."
    "Alarmı düzgün kurmayı öğrenmiştim sanmıştım ama işte, neyse."
   
    stop music fadeout 2.0
    window hide
    scene bg class_day with Dissolve(1.5)
    scene bg club_day with Dissolve(1.5)
    play music aNewDay fadein 2.0
    window show 
    "Okul vardı, herhalde ama önemli değil. Okuldan sonra, nihayet Edebiyat Kulübü'ne geçiyorum ve herkes bana bakıyor."
    mc "Selam."
    show sayori 4h at f11
    s "[player]! Neredeydiniz, Natsuki?"
    mc "Bunu mu? Tesadüfen okulu kaçırdık."
    show natsuki 4g at t22
    show monika 1d at f21
    m "Tesadüfen mi?"
    mc "Evet, Natsuki evimdeydi--"
    show monika 1c at t31
    show sayori 1q at t33
    show natsuki 1o at f32
    "Natsuki hemen gelip ağzımı kapatıyor."
    m 1l "Aaa, görüyorum. Evinde mi? İlginç."
    n 5q "Yoğunluktan başka bir şey değil."
    s 1i "Evet, yoğun olduğunuzu tahmin ettim."
    "Herkes bize hayal kırıklığıyla bakıyor. Natsuki ağzımı açıyor."
    mc "Durum böyle değil, yemin ederim."
    show sayori 1i at t43
    show monika 1c at t41
    show natsuki 5q at t42
    show yuri 2r at f44
    y "Kulübe katılmak istiyorsanız, gerçekten katılmanız lazım, acil bir durum yoksa tabii."
    show yuri 2r at t44
    show monika 1i at f41
    m "Yani, {i}bunu{/i} kaçıracak kadar, çok küçük bir saygısızlık."
    show monika 1c at f41
    mc "Bunu dikkate alacağız."
    show natsuki 1q at f42
    n "Evet!"
    n 2t "O zaman... ne dersiniz? Şiirlerimiz?"
    "O günden sonra okula hiç kaçmadık."
    window hide
    stop music fadeout 2.0
    show black with Dissolve(2.0)
    
    scene bg flashback_home with Dissolve(2.0)
    window show
    $ o_name = "???"
    n "Baba? Annemle ne oluyor?"
    o "..."
    n "Baba?"
    o "O... iyi olacak."
    o "Olmak zorunda."
    window hide
    show black with Dissolve(1.5)

    scene bg kitchen with wipeleft_scene
    window show
    play music NatTheme fadein 2.0
    "En azından bugün okuldan bir gündü. Son seferdeki gibi tekrar Edebiyat Kulübü'ne yüzümü göstermek istemiyorum açıkçası."
    "Natsuki ve ben kahvaltımızı yapıyoruz. Hala ayrı odalarda olmamıza rağmen, bir şey söylüyor."
    show natsuki 1bb at t44
    n "Yani, [player]."
    show natsuki 1bc at f11
    "Natsuki kalkıp yanıma oturuyor, ama gerçekten paneli görmesi gerektiğinde bile yanımda oturacak kadar yakınlaşmıyor."
    n 1bq "O Fransız Parfait Girls cildini okuma teklifin hakkında..."
    mc "Tabii, hiç sorun değil."
    n "Evet, aslında başka sevdiğim manga türlerinden çok yok, o yüzden yani."
    mc "Kahvaltımı bitireyim, hemen alıp getireyim."
    hide natsuki with wipeleft  
    scene bg bedroom with Dissolve(1.5)
    scene bg home_interior with Dissolve(1.5)
    "Yemeklerimi bitirdikten sonra odamıza gidip, Natsuki'nin bahsettiği manga cildini alıyorum. Sonra salona geri dönüp kanepeye oturuyorum."
    "Natsuki de geliyor, ama gerçekten yanımda oturana kadar pek yaklaşmıyor."
    mc "Hazır mısın?"
    show natsuki 1bb at f11
    n "Hazırım."
    hide natsuki with wipeleft
    "Natsuki'ye okurken kafamda bir sürü düşünce dolaşıyor."
    "Geçen sefer yanıma oturmamıştı çünkü Edebiyat Kulübü'ndeki herkes bizim hakkımızda bir şeyler düşünmesin diye, ama o bile sonunda yaklaşıp oturdu."
    "Birbirimize duygularımızı itiraf ettik, ama bu sefer kimse burada değil, o zaman neden tereddüt ediyor?"
    "Beni artık güvenmiyor mu?"
    "...Yok, belki de fazla anlam yüklemiyorumdur."
    scene bg home_interior with Dissolve(1.5)
    show natsuki 1bs at f11
    "Okumayı bitirdikten sonra mangayı yerine koyuyorum. Odamdan geri dönerken Natsuki bir şeyler düşünüyor gibi görünüyor."
    mc "Her şey yolunda mı?"
    n "Evet, sadece birkaç şey hakkında düşünüyorum."
    mc "Ya, istediğin kadar burada kalabilirsin, hani evi satmadığım sürece falan."
    n 1bq "Teşekkür ederim, [player]."
    mc "Ne zaman istersen."
    window hide
    stop music fadeout 2.0
    show black with Dissolve(2.0)
    pause(2.0)
    
    play sound alarm
    "{i}BZZT! BZZT!{/i}"
    "{i}BZZT! BZZT!{/i}"
    "{i}BZZT! BZZT!{/i}"
    "{i}BZZT! BZ--{/i}"
    $ o_name = "???"
    o "Hadi ama, [player]!"
    scene bg home_interior with open_eyes
    play music NatTheme fadein 2.0
    show natsuki 5b at f11
    "Gözlerimi zorla açıyorum ve Natsuki'yi görüyorum."
    stop sound
    mc "Hıh? Ne oluyor?"
    n 5g "Alarm seni uyandırmıyordu, o yüzden ben de zorla uyandırdım."
    n "Neyse, kahvaltın soğumadan kalk hadi."
    mc "Kahvaltı?"
    n 1b "Sadece senin her gün kahvaltıda mısır gevreği yediğini kaldıramadım da ondan."
    n "Kahvaltıda, öğle yemeğinde, akşam yemeğinde mısır gevreği mi? Vay be. Böyle sağlıklı bir hayat tarzı olmaz."
    n "Ve sakın yanlış anlamalar yapma. Son zamanlarda beslenme konusu benim için önemli bir mesele, hepsi bu."
    mc "Gel, zaten biliyorsun, Natsuki, sadece mısır gevreği yemiyorum."
    mc "Yine de... bunun için şikayet etmemeliyim, teşekkür ederim."
    hide natsuki with dissolve_cg
    "Beslenme meselesi onun için önemliymiş, öyle mi..."
    scene bg kitchen with wipeleft_scene    
    "Kalkıp yemek masasına gidiyorum ve önümde sıcacık bir tabak karışık yumurta görüyorum."
    show natsuki 3b at t44
    n "Tamam, karışık yumurta yapabildiğim tek şey bu. Kusura bakma."
    mc "Sorun değil."
    hide natsuki with dissolve_cg  
    "Natsuki her zamanki gibi kanepeye geçiyor ve yaptığı yemeği yiyor."
    "Neredeyse onunla biraz daha yakınlaşıyor gibiyim, azar azar."
    scene bg home_interior with wipeleft_scene  
    show natsuki 1a at f11
    "Yemeklerimizi bitirdikten sonra aklımda olan bir şeyi soruyorum."
    mc "Ne kadar süre burada kalmayı planlıyorsun, peki?"
    mc "Dediğim gibi, burada kalmak istersen kalabilirsin ama sanırım sonsuza kadar burada kalmak istemezsin, değil mi?"
    show natsuki 1s at f11
    "Natsuki yanına bakarak sessiz kalıyor."
    n "Belki de isterim."
    mc "Neyse, çok da önemli değil. Sanırım okula gitme zamanı geldi, değil mi?"
    n "Evet."
    hide natsuki with dissolve_cg  
    scene bg class_day with Dissolve(2.0)
    scene bg club_day with Dissolve(2.0)
    stop music fadeout 2.0
    "Okul aslında pek özel bir şey değildi ya da öyle hissettirmedi. Edebiyat Kulübü'nde geçirdiğimiz zaman da pek değişmemişti, her şey yavaşça eskisi gibi olmaya başlıyordu."
    "Bütün bu sabırlı bekleyişin boşa gitmediğini düşünüyorum, başka bir şey olmasa da."

    
    "Böyle birkaç hafta geçti."
    scene bg home_interior with open_eyes
    play music NatTheme fadein 2.0
    "Natsuki'nin burada yaşamaya başlamasından neredeyse bir ay sonra, sabah uyanırken yanıma gelip bir şey konuşmak istedi."
    show natsuki 4b at f11
    n "Bundan sonra istersen kendi yatağında uyuyabilirsin."
    "Ne? Ne diyorsun?"
    mc "Bekle, ne demek istediğini düşündüm ama... doğru mu anlıyorum?"
    n 4q "Hayır! Cidden, aklın başka bir yere gitmesine şaşırmadım bile."
    n 4s "Aslında başka bir şey düşündüm. Beni takip et."
    hide natsuki with wiperight 
    scene bg bedroom with Dissolve(1.5)
    "Natsuki'yi takip edip odamın içine giriyorum ve yatağıma bakıyorum."
    show natsuki 2b at f11
    n "Bak işte."
    "Yatakta iki tarafı ayıran yastıklardan yapılmış bir bariyer var. Biraz karmaşık ama işe yaradığını görebiliyorum."
    mc "Yani, yatağın iki tarafı var ve her birimiz kendi tarafımıza mı geçiyoruz?"
    n "Evet. Yatak bir kişi için oldukça büyük ve senin kanepede yatmanı biraz garip buluyordum, o yüzden..."
    show natsuki 2a at f11
    mc "Teşekkür ederim, Natsuki. Kendi odamda uyumak gerçekten güzel olacak."
    mc "Bu arada, akşam yemeği için farklı bir şeyler yesek nasıl olur? Belki pizza yemeye çıkabiliriz?"
    "Natsuki'nin reddetmesini bekliyordum ama beklediğimin tersine bir cevap verdi."
    n 2b "Tamam. Sanırım eğlenceli olabilir."
    show black with dissolve_cg
    "O akşam, yerel bir pizzacıya gidip harika zaman geçirdik."
    "Orada, eski günlerde olduğu gibi manga ve diğer saçma şeylerden konuştuk."
    "Bunu tekrar yaşamak gerçekten güzel, ama biliyorum ki bu sonsuza kadar süremez..."
    "Hiçbir şey sonsuza kadar sürmez."
    "Yine de, o geceden sonra Natsuki ile daha fazla vakit geçirmeye başladım. Manga okuduk, anime izledik, masa oyunları oynadık falan."
    "Artık bana daha fazla güveniyor olsa da, hala küçük bir kaygı vardı içinde. Bir gün nedenini sorarım belki, ama şimdilik Natsuki ile yaşamaya devam ediyorum."
    "Huzurlu bir hayat, mükemmel olmasa da."
    "Gerçekten tek istediğim bu."
    stop music fadeout 2.0
    window hide
    scene bg bedroom with open_eyes
    window show
    play music NatTheme fadein 2.0
    "Ertesi sabah ikimiz de kalkıyoruz. Ben son dakikada ödevimi bitirip okula gitmek için hazırlanırken, Natsuki kahvaltıyı hazırlıyor."
    "Ne yazık ki, alıştığımız rutin bozuluyor ve telefonuma bir mesaj geliyor."
    "Bu mesajı bir gün alacağımı biliyordum ama açıkçası almak istemediğim bir mesaja bakıyorum."
    "Göndereni görüyorum ve tahmin ettiğim gibi, Sayori."
    p "Cidden, Natsuki ile aranızda ne var?"
    "Mesajı alıp, 'Bunu sonra konuşuruz.' diye cevap veriyorum. Sonuçta, ödevimi bitirmem gerek."
    "Ama gerçekten, bunun yüz yüze konuşulması gereken bir şey olduğunu düşünüyorum."
    stop music fadeout 2.0
    scene bg class_day with Dissolve(2.0)
    scene bg club_day with Dissolve(2.0)
    play music aNewDay fadein 2.0
    "Natsuki ve ben her zamanki gibi yemeklerimizi yedikten sonra, sıradan bir okul günü için dışarı çıkıyoruz."
    "Derslerimiz bittiğinde, birlikte Edebiyat Kulübü'ne giriyoruz ve her şeyin yine normal şekilde işlediğini görüyoruz."
    show sayori 1a at t44
    show natsuki 1c at t41
    "Natsuki'ye sessizce bir şeyler söylüyorum."
    hide natsuki with wipeleft  
    mc "Bir dakika, tamam mı?"
    show sayori 1a at f11
    "Sayori'nin yanına gidiyorum."
    mc "Evet, Natsuki hakkında. Belki biraz daha sessiz bir yer bulmalıyız?"
    s 1c "Tabii!"
    hide sayori with wipeleft
    scene bg corridor with dissolve_cg
    "Sayori ile birlikte koridora gidip konuşmamız gereken şeyi tartışmaya başlıyoruz."
    show sayori 4h at f11
    # DEVAM EDİLİCEK
    menu:
        s "Natsuki ile ne oluyor acaba?"
        "Tam hikayeyi anlatmaya çalış.":
            mc "Biliyorsun, Natsuki bir süre garip davranıyordu, değil mi?"
            mc "Pekala..."
            "Devam etmeye çalışıyorum ama bu doğru hissettirmiyor. Natsuki ile aramdaki bir şeyi Sayori'ye anlatmak istemiyorum."
            "Belki daha sonra ona açıklayabilirim ama gerçekte bunun tam detaylarını da bilmiyorum."
            mc "Ben de bu konuda pek bir şey bilmiyorum. Detayları paylaşmak konusunda rahat hissetmiyorum, o yüzden diyelim ki onun kalacak bir yere ihtiyacı vardı ve bunu burada bırakıyoruz."
        "Kısa kes.": 
            mc "Ben de bu konuda pek bir şey bilmiyorum. Detayları paylaşmak konusunda rahat hissetmiyorum, o yüzden diyelim ki onun kalacak bir yere ihtiyacı vardı ve bunu burada bırakıyoruz."
    
    s "Hımm. Neden böyle merak ediyorum..."
    mc "İşte bu kadar. Herhangi bir gizli iş yok, bu sadece bir arkadaşıma yardım etmem."
    s 1r "Bir {i}arkadaş{/i} mı?"
    mc "Bu bambaşka bir konu."
    s 1x "Mmm. Eğer herhangi bir tavsiye istersen, bu konuda çok iyi değilim ama elimden geleni yapabilirim."
    mc "Teşekkürler, Sayori."
    hide sayori with wipeleft
    scene bg club_day with dissolve_cg
    show sayori 1a at t22
    show natsuki 1a at f21
    "Kulüp odasına döndüğümüzde, Natsuki bize doğru geliyor."
    n 1b "[player]?"
    "Sayori'ye uzak durmasını işaret ediyorum."
    hide sayori with wiperight  
    show natsuki 1b at f11
    mc "Geri döndüm, evet."
    n 4c "Ahh... Umarım saçmalık yapmamışsındır."
    "Gerçekten de, onun bana tam olarak güvenmediği doğru."
    "Ve onun güvensizlikleriyle, Sayori ile aramızda yanlış bir izlenim alması sürpriz olmaz, ki bu aslında mantıklı bile değil."
    mc "Şu an beni en çok önemseyen sensin, Natsuki. Söz veriyorum."
    m "Ama umarım diğerlerine karşı kötü davranmak istemiyorsundur!"
    show natsuki 4c at lhide
    hide natsuki
    show monika 1b at f22
    "Arkamı döndüğümde Monika'nın dinlediğini görüyorum."
    show monika 1a at f22
    mc "Ne demek istediğimi biliyorsun, Monika."
    show monika 1a at lhide
    hide monika
    show natsuki 1h at f11
    mc "Ama evet, Natsuki. Şu an en önemli kişi sensin."
    mc "Sayori nazik ama sonuçta sadece bir arkadaş, biliyorsun?"
    "Natsuki rahatlamış görünüyor."
    n "Teşekkür ederim, [player]..."
    "Vay be, bu karmaşık bir durum. Zaten oldukça belirgindi ama, ah. Ne olursa olsun, sabırlı olmak ve her şeyin kendi yolunda gelişmesine izin vermek işe yarıyor gibi görünüyor."
    "Sanırım."
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)

    
    scene bg flashback_home with Dissolve(2.0)
    window show
    $ o_name = "???"
    o "Okuduğun şey bu mu?"
    n "Manga!"
    o "Manga mı?"
    n "Evet! Bunlar çizgi roman gibi ama daha havalı."
    o "Bana göster bunu..."
    o "Yani manga okuyorsun, öyle mi?"
    o "Bunu nereden buldun? Bir arkadaşından mı?"
    o "Aslında önemli değil."
    o "Başka bir şey yap."
    n "Ama neden? Bu beni mutlu ediyor."
    o "Hayır, bu beynini çürütür!"
    o "Verimli, dolu dolu bir hayat yaşamanı istiyorum."
    o "Manga bunu sağlayamaz."
    o "Açıkçası, edebiyat bile sayılmaz..."
    window hide
    show black with Dissolve(2.0)
    
    scene bg bedroom with open_eyes 
    window show
    show natsuki 1bb at t41
    n "[player]? Aklımda bir şey var."
    "Natsuki'nin benden önce her zaman uyanmasının sebebi ne acaba? Hep uyuyakalan bir tip olacağını düşünmüştüm."
    mc "Nedir, Natsuki?"
    show natsuki 1bu at f11
    n "Son zamanlarda olanlar hakkında biraz suçluluk hissediyorum."
    n "Yani, sana bir açıklama borçlu olduğumu düşünmüyorum aslında."
    "Natsuki bir an duraksıyor ve gözlerime bakıyor."
    play music Thoughts fadein 2.0
    n 1bh "Ne diyorum ben? Tabii ki sana bir açıklama borçluyum."
    n "Bu kadar uzun süre burada kalmama izin verdikten sonra..."
    n "Sana sürekli kötü davrandıktan sonra..."
    n "Daha güçlü olmayı dilerdim. Neden bunu bile yapamıyorum?"
    show natsuki 1bs at f11
    "Natsuki'nin gözlerinde yaşlar belirmeye başlıyor."
    mc "Sakin ol, Natsuki. Başlangıçtan başlayabilirsin."
    n 1bs "Yapamam. Henüz değil."
    mc "Tamam. O zaman ne söyleyebilirsin?"
    n 5be "Son zamanlarda sana ve diğerlerine neden bu kadar uzak durduğumun sebebi..."
    "Natsuki konuşmaya çalışıyor ama kelimeler ağzından çıkmıyor."
    mc "Buradayım, Natsuki. İhtiyacın olduğu kadar zaman alabilirsin."
    n 5bc "[player], senin için güven ne demek?"
    mc "Huh? Bu ani bir soru, bir dakikanı al."
    "Bana göre güven birçok şey ifade ediyor. Ama sadece özetlemem gerekirse, bunu yaparım."
    mc "Güven benim için güvenin en yüksek sembolüdür. Arkadaşlığın, romantizmin ve genel olarak insan etkileşimlerinin temelidir."
    mc "Birine olan inancının sembolüdür. Onların sana asla zarar vermeyeceklerine inandığını gösterir."
    mc "Kimseye 'mükemmel' bir güven duymanın mümkün olduğunu düşünmüyorum."
    mc "Ama güven mükemmel olmak zorunda da değil. Yeterince iyi olması yeter, sonra memnun kalabilirsin."
    show natsuki 5bu at f11
    "Natsuki söylediklerimi düşünüyor. Açıklamamda muhtemelen bir yerlerde hata yaptım ama anladığını düşünüyorum."
    n 5be "Ben de buna benzer bir şey düşünüyordum, ama benim için biraz farklı."
    n "Ben... mükemmel bir güvene ihtiyacım var. Ve bu güveni o kişiye hissettirmedikçe gerçek benliğimi gösteremeyeceğimi düşünüyorum."
    mc "Bilmiyorum, Natsuki. Peki, mükemmel güveni ilk başta nasıl elde edebilirsin?"
    mc "Mükemmel güven {i}nedir{/i}?"
    n 5bb "Bilmiyorum ama başka bir güven anlayışına katlanamıyorum."
    mc "Bunun arkasında bir sebep var mı?"
    n 5bc "Belki başka bir zaman sana söylerim."
    n "Ama söylediklerin hakkında tamamen yanlış olduğunu düşünmüyorum."
    n "Belki bunları yeniden düşünmem gerek..."
    n "İlk adımı atarsam, belki biraz daha kolay olur."
    show natsuki 1bc at t44
    "Natsuki, aramızdaki yastıkları alıp atıyor."
    mc "Ne yapıyorsun?"
    show natsuki 1bh at f11
    n "Neyin büyük bir sorunu var? Kötü bir şey yapmıyoruz sonuçta."
    n 5bi "Eğer bunu savunuyorsan, o zaman tekrar kanepeye dönersin."
    n "Ama dürüst olmak gerekirse, o engel de canımı sıkıyordu."
    n 5be "Yastıkların içine horladığın için, horlaman daha da fazlalaşıyordu."
    n "Bu kötüydü."
    "Natsuki bir şey söyleyecekmiş gibi duraksıyor."
    pause(1.0)
    n 1bb "Ama evet."
    n "Bana çok nazik davrandın."
    n 1bq "Tamamen güvenmiyor olabilirim, ama sana yeterince güveniyorum."
    n "Bu senin önem verdiğin şeydi, değil mi? Yeterince iyi bir güven."
    "Bu duruma nasıl tepki vereceğimi gerçekten bilemedim."
    mc "Belki de öyledir."
    n 1bu "Bir gün sana tam hikayeyi anlatabilirim ama umarım bu yeter."
    mc "Yeter, Natsuki. Teşekkürler."
    "O günün büyük bir kısmını yatakta uzanarak geçirdik. Aslında hiçbir şey yapmıyorduk, sadece bu ana kadar olan her şeyi düşünüyorduk."
    hide natsuki with dissolve_cg
    stop music fadeout 2.0
    show black with Dissolve(2.0)
    
    play music aNewDay fadein 2.0
    scene bg bedroom with open_eyes
    scene bg kitchen with Dissolve(1.5)
    scene bg class_day with Dissolve(1.5)
    scene bg club_day with Dissolve(1.5)
    show natsuki 1a at t21
    "Bir kahvaltı daha, bir okul günü daha ve Edebiyat Kulübü'nde bir gün daha."
    "Her şey, Edebiyat Kulübü'ne kadar normaldi. Ama kulüpte olanlar bu durumu tamamen farklı bir hale getirdi."
    show sayori 1x at f22
    "Natsuki ve ben içeri giriyoruz ve herkes her zamanki gibi bize selam veriyor. Biraz manga almak için gidiyoruz ama tam o sırada Sayori yanımıza geliyor."
    s "Siz ikiniz yakında çıkmaya başlayacaksınız, değil mi?"
    show natsuki 1p at f21
    show sayori 1q at t22
    n "Ne?!"
    show natsuki 1p at t21
    show sayori 1r at f22
    s "Hadi ama! Sizin birbirinizi sevdiğiniz çok belli."
    "Ne? Ben hiç Sayori'ye bu kısmı anlatmadım ki!"
    show natsuki 1q at f21
    show sayori 1r at t22
    n "Tamamen yanlış değilsin ama..."
    show natsuki 1q at t21
    show sayori 1x at f22
    s "Ama ne? Biraz yaşa!"
    show natsuki 1s at f21
    show sayori 1r at t22
    "Natsuki bana bakıyor, ne yapacağını bilemez halde."
    "Bu da pek uygun değil, çünkü benim de ne yapacağımı bilmiyorum."
    "Natsuki'ye fısıldıyorum. Sayori'nin dinleyeceği muhtemel ama buna artık bir şey yapamam."
    mc "Bunu koridor dışında konuşalım."
    hide sayori with wipeleft
    "Natsuki başını sallıyor. Koridora çıkmaya çalışırken Monika'nın sesini duyuyoruz."
    show natsuki 1s at t41
    show monika 1b at f44
    m "Siz ikiniz nereye gidiyorsunuz?"
    show natsuki 1s at t41
    show monika 1a at t43
    show yuri 1b at f44
    y "Sonuçlara atlamayı sevmiyorum ama siz ikiniz hakkında bildiklerimizden... hmm..."
    mc "Bak, biz sadece--"
    show natsuki 1q at f41
    show monika 1a at t43
    show yuri 1a at t44
    n "Bahaneler üretmeyi bırak ve olduğu gibi söyle, [player]."
    n "Özel bir konuşma yapacağız. Anladın mı?"
    hide monika with wipeleft
    hide yuri with wipeleft 
    stop music fadeout 2.0
    scene bg corridor with dissolve_cg
    play music AfterAll fadein 2.0
    "Diğer herkes başlarını sallayarak koridora doğru ilerliyoruz."
    show natsuki 1c at f11
    mc "...Neyse, çıkma teklifimiz hakkında."
    mc "Yani, buna karşı değilim, ama gerçekten güvendiğin birisiyle çıkabilir misin?"
    "Natsuki bir süre öylece duruyor."
    show natsuki 1j at f11
    "Bir karara varınca gülümseyip fısıldıyor."
    n "Ama aramızdaki güven {i}yeterince{/i} iyi olduğu sürece, bu işe yarar. Bu, senin söylediğin değil mi?"
    n 1q "Ayrıca, kendime yalan söylemekten de yoruldum."
    "Artık ya şimdi ya da asla. İlk başta bunun çok ani olduğunu düşünüyorum ama... hayır, hazırım."
    mc "Tamam. Natsuki, bana--"
    stop music
    n 4e "Aptal!"
    mc "Ne beklediğini bilmiyorum."
    n "Hayır! Hala kulüp odasının önünde durduğumuzdan bahsediyorum."
    mc "Ah, anladım. O zaman koridorun daha iç kısımlarına geçelim."
    hide natsuki
    scene bg corridor with dissolve_cg
    "Koridordan geçerken duruyoruz, umarım burası yeterince iyi bir yer."
    play music AfterAll fadein 2.0
    show natsuki 5q at f11
    n "Öyleyse? Söyleyecek misin yoksa?"
    mc "Tabii ki."
    "...Aman Tanrım."
    "Aman Tanrım."
    "{i}Aman Tanrım.{/i}"
    "Gerçekten şu anda ne yaptığımı kavradım. Yani, bunu yapacağımı biliyordum ama {i}gerçekten{/i} yapıyorum."
    "Edebiyat Kulübü'ne ilk katıldığım zamanı hatırlıyorum. Herkesi sevmiştim ama Natsuki dikkatimi çekmişti."
    show natsuki 1q at f11
    mc "Natsuki, benim için özel bir insansın. Cidden."
    "Natsuki soğuk biri, evet ama bazen tatlı olabiliyor. Sonuçta herkesin mükemmel bir kişiliği yok."
    "Ayrıca, onun tavırlarının benim için sempatik olduğunu düşünüyorum."
    mc "Seni ilk günden beri sevdim ve senin de aynı şekilde hissettiğini bilmiyorum ama yine de benim için hislerin var."
    "Natsuki sadece benimle benzer ilgi alanlarına sahip değil, aynı zamanda ufkumu genişletti. Ve yeni şeyler denemek istediğim kişi o."
    mc "Mükemmel değilim, kabul ediyorum. Ayrıca bu benim ilk ilişkim olacağı için mükemmel bir erkek arkadaş olamayabilirim."
    "Ve birlikte yaşıyoruz da! Ne harika bir durum değil mi? Garip bir durum, elbette ama en azından ikimiz de ondan mutluluk çıkardık."
    show natsuki 1s at f11
    mc "Ama bu benim için önemli değil. Duygularım bunun beni durdurmasına izin vermiyor."
    "Elbette saf bir mutluluk yoktu. Bazı rahatsız edici, üzücü anlar da yaşadık."
    "Natsuki'nin benimle olan güveninin bu kadar sarsılması ne kadar kötü olmalı, iyi bir dostluk kurduktan sonra."
    mc "Diğer insanlar zaten birlikte olduğumuzu düşünebilir. Bu da anlaşılabilir, sonuçta birbirimize karşı hislerimiz var."
    "Ne kadar zorlu bir yolculuktu. Edebiyat Kulübü'ne katıldığımda bunun gibi bir şeyin olacağını hiç düşünmemiştim ama buradayız."
    mc "O zaman neden resmi hale getirmiyoruz? Seni dünyanın en mutlu kızı yapmayı vaat ediyorum."
    mc "Natsuki, benim kız arkadaşım olur musun?"
    "Natsuki hemen cevap veriyor."
    show natsuki 4e at f11
    n "Tabii ki! Aman Tanrım, bunu sanki evlenme teklifi gibi yaptı. Bir sonraki sefer itirafını daha kısa yap."
    show natsuki 1t at f11
    n "Ama seni affedeceğim. Edebiyat Kulübü'ne ilk geldiğin günden beri seni seviyorum."
    mc "Heh."
    "Heh dedim ama bu anı ifade etmeye bile yetmiyor. O kadar rahatladım ki, o kadar tatmin oldum... o kadar mutluyum."
    mc "Natsuki..."
    
    "İkimiz de yanaşıyoruz."
    show natsuki 1i at face_one(y=200) with dissolve_cg
    "Ağzımız birbirine iyice yaklaşıyor..."
    show natsuki 1i at face_two(y=335) with dissolve_cg
    "Ta ki..."
    show natsuki 1i at face_three(y=600) with dissolve_cg
    stop music
    play music EarlyBird
    s "Bunu biliyordum!"
    "Oh."
    n 1p "Ne oluyor burada?!"
    show natsuki 1p at t44
    show monika 5a at t41 zorder 1
    show sayori 4x at t31 zorder 2
    "İkimiz de döndüğümüzde Sayori ve Monika'nın Edebiyat Kulübü kapısının arkasından bakmakta olduğunu görüyoruz."
    hide monika with wiperight  
    hide sayori with wiperight  
    "Yakalandıklarını anlayınca hemen içeri geri koşuyorlar."
    mc "Eh, bir sonraki şansa kadar ölmeyeceğiz. Eminim başka bir fırsatımız olur."
    n 5q "Evet."
    
    mc "Açıkçası, bugün Edebiyat Kulübü'nden erken çıkmayı düşünüyorum."
    mc "Sen ne dersin?"
    n 5s "Evet..."
    mc "Monika'ya kulüpten erken çıkmamız gerektiğini söyleyeceğim. Bence anlayışla karşılayacaktır."
    mc "Kulüp yarın bizi epeyce kızdıracak, ama ben eve gitmeye hazır hissediyorum."
    "Bugün garip geçti... ama başka türlü olmasını istemezdim."
    
    stop music fadeout 3.0
    window hide
    show black with Dissolve(2.0)
    pause(2.0)
    scene bg flashback_home with Dissolve(2.0)
    
    window show
    $ o_name = "???"
    o "Doğum günün kutlu olsun, Natsuki."
    o "Zor bir yıl geçirdiğini biliyorum, ama umarım gelecek yıl daha iyi olur."
    n "... ..."
    o "Bir şey mi var?"
    n "Bu konuda konuşmak istemiyorum. Doğum günümde değil."
    n "Ama ne demek istediğini zaten biliyorsun, baba."
    window hide
    show black with Dissolve(2.0)
    
    play sound alarm 
    "{i}BEEP! BEEP!{/i}"
    scene bg bedroom with open_eyes 
    play music EarlyBird fadein 2.0
    "...Yani, bu durumda artık bir ilişkim var, öyle değil mi?"
    stop sound
    "Bunu henüz sindirmeye çalışıyorum. Sadece bir kız arkadaşım olması değil, kız arkadaşımın Natsuki olması da garip bir düşünce."
    "Biraz tuhaf hissettirse de, harika... "
    show natsuki 3b at f11
    n "Hadi ama, artık kalk!"
    "Dur, ne oluyor?"
    mc "Natsuki? Saat kaç?"
    n 4e "Neden o alarm saatini kullanıyorsun ki? Zaten ona pek uyanmıyorsun."
    n "Dediğim gibi, kalk. Okul zamanı geliyor ve senin için kahvaltı hazırladım."
    mc "Tamam. Teşekkürler, Natsuki."
    hide natsuki with wipeleft
    scene bg kitchen with wipeleft_scene
    "Mutfağa girdiğimde sadece çırpılmış yumurtalar değil, birkaç dilim pastırma da görüyorum."
    show natsuki 3q at f11
    n "Artık kız arkadaşım olduğuma göre, senin için yaptığım yemeklerin biraz daha iyi olması gerektiğini düşündüm."
    mc "Gerçekten mi? Bu oldukça nazik bir davranış."
    n 4i "Bazen nazik olabilirim! Tamam mı? En azından bir 'teşekkürler' edebilirsin."
    mc "Üzgünüm. Teşekkürler, Natsuki."
    n 1a "İşte bu daha iyi."
    mc "O zaman yiyelim."
    hide natsuki with dissolve_cg
    "Kahvaltımızı (birlikte otururken, belirtmek isterim) yiyoruz ve kısa süre sonra okula doğru yola çıkıyoruz."
    window hide
    scene bg residential_day with wipeleft_scene
    pause(1.5)
    scene bg class_day with wipeleft_scene
    pause(1.5)
    scene bg corridor with wipeleft_scene
    pause(1.5)
    scene bg club_day with wipeleft_scene
    show natsuki 1a at t21
    show sayori 1x at t22
    stop music fadeout 2.0
    play music aNewDay fadein 2.0
    window show
    "Derslerimizi tamamladıktan sonra Edebiyat Kulübü'ne girdiğimizde, hemen Sayori ile karşılaşıyoruz."
    show sayori 1x at f22
    s "Sooooo?"
    mc "Ne var?"
    s "Siz ikiniz artık çıkıyor musunuz? Artık bunu yapmak zorundasınız."
    s 1r "Sana mesaj atmayı düşündüm, ama bu bilgiyi bu kadar kolay paylaşmayacağını düşündüm, ehehe."
    mc "Ama bunun senin için bu kadar önemli olduğunu anlamıyorum. Bir bahse mi girdin yoksa?"
    s 4x "Çünkü siz ikisini destekliyordum, tabii ki!"
    "Natsuki gözünü devirdi."
    show natsuki 4b at f21
    show sayori 4x at t22
    n "Evet, çıkıyoruz."
    "Natsuki'nin kaba bir şey eklemesini bekliyorum ama..."
    n "Peki, bu benim için bir gurur kaynağı."
    show natsuki 4a at t21
    show sayori 4x at t22
    s "Tabii ki! Bunu kötü bir şey olarak kastetmemiştim."
    show natsuki 1b at f21
    show sayori 4x at t22
    n "Biliyorum ama bunu büyük bir mesele olarak görmüyorum."
    n 3y "Sanırım [player]’ın gerçekten bir kız arkadaşı olması şaşırtıcı."
    "Eh, haklı değil mi?"
    show natsuki 3y at t21
    show sayori 1r at f22
    s "Ah, doğru söylüyorsun, ehehe."
    "Vay be, Sayori bile katılıyor."
    s 1x "Bunu süper havalı buluyorum! Yani, sizi ikinizi kutluyorum."
    mc "Teşekkürler, Sayori. Ben de bu durumdan mutluyum."
    n 4q "Beni düşüneceğinizi umarım, çünkü sıradan birinin kız arkadaşı olmayı istemiyorum, biliyorsun!"
    hide sayori with wipeleft
    show natsuki 4q at f11
    "Sayori gülerek Natsuki ile birlikte kulüp odasına doğru ilerliyoruz."
    mc "Bu ilişkiyle ilgili bir şey hatırlatıyor, Natsuki."
    mc "Tam olarak ne yapmalıyız?"
    n 1b "Romantik biri olduğumu düşünmüyorsan, bu durum hiç de öyle değil."
    mc "Ben de romantik değilim ve romantik olmaya çalışsam muhtemelen kendimi rezil ederim."
    mc "Demek ki bu iş düşündüğüm kadar kolay olmayacak."
    show natsuki 1a at t22
    m "Zorunlu değil!"
    show monika 3b at l21
    "Monika masasından kalkıp yanımıza geliyor."
    mc "Birimiz romantik olursa daha iyi olmaz mı?"
    show monika 3b at f21
    m "Bazen alışılmışın dışında olan ilişkiler en iyi şekilde işleyenlerdir."
    m 1b "Herkesin bir ilişki için standart beklentileri takip etmesi gerekmiyor."
    m 1k "En önemli şeyin, ikinizin de mutlu olması olduğunu düşünüyorum. Sonuçta tek mesele bu, değil mi?"
    m "En azından ben bunu düşünmeyi seviyorum."
    "Bu cümlenin altında daha derin bir anlam olduğunu hissetsem de, bunun pek önemi yok."
    m 4k "Neyse, her ikinize de en iyi şansları diliyorum! Bence çok tatlı bir çiftsiniz."
    show natsuki 4e at f22
    show monika 4k at t21
    n 1v "Son bir kez daha, ben tatlı değilim!"
    hide monika with wipeleft
    show natsuki 4e at f11
    "Hmm."
    mc "Yani bu benim tatlı olduğum anlamına mı geliyor?"
    n 4b "Bazen komiksin, sanırım."
    "Bu iki şeyin pek aynı olduğunu düşünmüyorum."
    mc "Neyse, ben biraz manga alacağım, Natsuki."
    hide natsuki with wipeleft 
    scene n_cg1_bg
    show n_cg1_base
    show n_cg1_exp1
    with dissolve_cg
    "O gün tekrar manga okuduk, ama bu sefer çok daha farklıydı. Daha... kişisel hissettiriyordu. Daha fazla gülüp gülmediğimizi fark ettim."
    "Basit bir etiket gerçekten bu kadar şeyi değiştirebilir mi? Daha önce bir ilişkiye girseydik de böyle mi olurdu?"
    "Ama Monika'nın dediği gibi, bunun önemi yok. Önemli olan mutlu olmamız. Natsuki'yi mutlu etmek için söz verdim ve bu düşünce beni de mutlu ediyor."
    "Daha romantik olmaya çalışabilirim, yine de."
    "Ne olabilir ki?" 
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    pause(1.5)
   
    play sound alarm
    "{i}BEEP! BEEP!{/i}"
    stop music
    stop sound
    scene bg bedroom with open_eyes 
    play music EarlyBird fadein 2.0
    "Sonunda, Natsuki'den önce uyandığım bir gün! Kısmen alarm saatimi normalden 30 dakika daha erken kurduğum için ama neyse."
    mc "Hey, Natsuki! Uyanacak mısın?"
    "Natsuki döner."
    show natsuki 1bh at f11
    n "Huh? Niye beni uyandırıyorsun?"
    mc "Sabah değil mi? Ve genelde sen beni uyandırıyorsun, bu sefer tersini yapayım dedim."
    n 1bb "Uyanmak için daha erken, aptal. Sadece sen çok uyuduğun için seni uyandırıyorum."
    "Uh oh."
    "Sanırım bir hata yaptım. Muhtemelen."
    mc "Oh! Um, bunun için üzgünüm. Bir daha yapmam."
    show natsuki 1bd at f11
    "Natsuki gülümser ve tekrar döner."
    n "Ama hoşuma gidiyor."
    mc "Huh?"
    n 1bq "Sana karşı bir şeyler hissetmen güzel."
    n "Belki büyük bir ölçekle hata yapıyorsun ama, birinin umursaması güzel."
    n "Düşünmek önemli... ya da öyle bir şey, bilmiyorum."
    n "Bir dahaki sefer önce düşünmelisin, sanırım."
    n "Şimdi uyuyacağım."
    hide natsuki with wipeleft
    "Ondan sonra kalkmak istemediğim için ben de geri yatıyorum. Ama iki dakika sonra, yastığın sesini duyuyorum."
    show natsuki 1bb at f11
    n "Uff, şimdi uyanmaya hazırım."
    mc "İki dakika mı?"
    n "Bu saatte uyanmayı planlamıştım, evet."
    show natsuki 1ba at t11
    "Bilmiyorum, bu benim şikayet etmem gereken bir şey değil, bu yüzden neden bunu açtım bilmiyorum."
    mc "Bu arada, sormak istediğim bir şey var."
    show natsuki 1bb at f11
    n "Evet?"
    mc "Bu biraz aptalca gelebilir ama, bu sabah kahvaltı yapabilir miyim?"
    n "Dinlenmek için daha fazla zaman kazanmak istemiyorum ama, neden kahvaltı yapmak istiyorsun?"
    mc "Eh, bir aydan fazla süredir kahvaltıyı sen yapıyorsun, değil mi? Bence bazen sana bir mola vermek adil."
    n 1bk "Yap gitsin. Ama umarım yemek yapma yeteneğin berbat değildir."
    n 1bq "Ama senin için yaparsam yine de yerim, yine de..."
    mc "Senin benim için nazik olmaya çalıştığın kadar çaba göstermeni çok cool buluyorum, biliyor musun?"
    n 5bq "B-Bu? Bunu kasıtlı olarak yapmıyorum ki!"
    n "Böyle oluyor."
    n "Ugh. Bunu bilseydim, sana bu şekilde utandıracağımı düşünmezdim."
    "Ama bekle, bu gerçekten kahvaltı {i}hazırlamam{/i} gerekecek mi? Ah, harika. Ben genellikle işlenmiş gıdalarla besleniyorum, bu yüzden ev yapımı yemek yapma konusunda pek bilgim yok."
    hide natsuki with wipeleft
    scene bg kitchen with Dissolve(2.0)
    "Mutfak yönünde giderken ne yapacağımı düşünüyorum."
    "Natsuki tatlı şeyleri seviyor, değil mi? Ama bu kahvaltı, o yüzden bir kahvaltı yemeği olması lazım."
    "Aslında, ne kadar kahvaltı yemeği yapmayı biliyorum? Çok fazla değil, galiba. Yeni bir şey denemek isteyebilirim ama bu bir felaket de olabilir."
    menu:
        "Ne pişireceğimi düşünmem lazım. Basit bir yemek yapmak güvenli bir yol ama biraz daha büyük bir şey yapmak daha ilginç olabilir."
        "Basit bir şey.":            
            "Boşver, omlet yapacağım."
            
            stop music fadeout 2.0
            window hide
            scene bg kitchen with Dissolve(2.0)
            play music EarlyBird fadein 2.0
            window show
            "Kahvaltıyı ikimiz için hazırladıktan sonra, yaptığım şeyi Natsuki'ye sunuyorum."
            show natsuki 1c at t41
            pause(1.0)
            show natsuki 1c at t44
            pause(1.0)
            show natsuki 1c at t41
            pause(1.0)
            show natsuki 1c at t44
            pause(1.0)
            "Birkaç açıdan bakıyor ve bir lokma alıyor."
            "Yüzünde bir iğrenme ifadesi yok, bu da iyi bir şey."
            show natsuki 1b at f11
            n 1b "Bu tuzlanmamış, değil mi?"
            mc "Oh, eh, bunu yapmak zorunda mıydım?"
            n "Evet."
            n 4b "Ama yine de bence tadı oldukça iyi. Elbette benimki kadar değil."
            n "Yani, ilk defa pişirdiğin için fena iş çıkarmadın."
            mc "Pek sık yemek yapmam, ama bu benim ilk deneyimim de değil."
            n "Oh."
            n "Yani, kaç kere pişirdiğine göre fena iş çıkarmadın."
            mc "Teşekkür ederim."
            n 4j "Üstelik, benim omletlerim her zaman aynı tadı alıyor, yani mükemmel bir tadı var."
            n "Bu kesinlikle ortalamanın altında, dolayısıyla tadı farklıdır."
            n "Yani, yediğim yiyeceklerde biraz çeşitlilik olması güzel."
            "Sanırım bu bir iltifat olarak düşünülmüştü?"
            mc "En azından sen bir şeyler çıkarabildiğin için mutluyum."
            n 1a "Evet. Bir sonraki ne pişireceğini görmek istiyorum."
            mc "Bekle, tekrar mı pişiriyorum?"
            n 1b "İstersen."
            n "Yani, potansiyelin var ya da bir şey, bilmiyorum."
            mc "Sanırım yemek yapma pratiği yapmak gerçekten faydalı bir beceri."
            n "Evet. Yiyecek, başka biri tarafından özel olarak yapıldığında çok daha güzel tadıyor, biliyor musun?"
            mc "Başka biri tarafından yapıldığını mı kast ediyorsun? Bu biraz geniş bir tanım. Yani, senin için önemli olan biri tarafından mı?"
            "Natsuki bu noktanın farkına varıyor ve utangaç bir şekilde konuşuyor."
            n 5q "O-O noktayı geçelim."
            mc "Emin değilim. Bence tam da bu nokta, Natsuki."
            "Natsuki somurtuyor."
            n 5s "Her şeyi işaretlemek zorundasın, değil mi?"
            mc "Gerekli olduğunu düşündüğümde sadece."
            n "Tamam. Yiyeceklerin daha iyi tadıyor çünkü bunun senin yaptığın olduğunu biliyorum ve sen benim için önemli birisin. Mutlu musun?"
            mc "Biraz."
            "Pratik yapmam da yararına olur, diye düşünüyorum."
            mc "Neyse, yemeye devam edelim."
        "Karmaşık bir şey.":            
            $ makeComplex = True
            "Natsuki özel biri, bu yüzden ona özel bir yemek hazırlamak istiyorum. Bu biraz zaman alacak ama buna değeceğine eminim."
            stop music fadeout 2.0
            window hide
            scene bg kitchen with Dissolve(2.0)
            play music EarlyBird fadein 2.0
            window show
            mc "Yumurtalar için... bir, iki..."
            show natsuki 3b at t44
            n "[player]?"
            show natsuki 1b at t43
            mc "Sonra yulaf ezmesi..."
            show natsuki 1b at f42
            n "[player]!"
            mc "Ne?"
            show natsuki 1b at f11
            "Natsuki'ye döndüğümde, hala bitirmemi bekliyor."
            n 4b "Bu kadar büyük bir yemeği yapmayı bildiğinden emin misin?"
            n "Yani, gerçekten emin misin? Emin olmadığım için seni pek ikna edemedim."
            mc "Bunu neden söylüyorsun?"
            mc "Doğru, yaklaşık otuz dakikadır buradayım ama bu süreçte bu var."
            n "Sadece, bu yiyecek iyi olmazsa, okula geç kalacağımızı umuyorum."
            "Aman Tanrım. Gerçekten {i}okula{/i} geç kalıyor olmalıyız."
            mc "Şu anda bunun ne kadar ilerlediğine göre, muhtemelen sadece beş dakika geç kalacağız. Bence bu çok da kötü değil."
            n "Dediğim gibi, bu yemek buna değer olmalı."
            scene bg kitchen with wipeleft_scene
            "Kısa bir süre geçtikten sonra, yemek hazır."
            "Büyük bir tabakta, omlet, pastırma, yulaf ezmesi, şurup ile kaplı pankekler, Fransız tostu ve su var (portakal suyu yoktu, bu yüzden akıllıca bir çözüm bulmak zorundaydım)."
            show natsuki 1c at f11
            "Yemeği Natsuki'ye getirdiğimde, büyüklüğünden şaşırıyor."
            n 1b "Yahu! Büyüyeceğini biliyordum ama {i}bu{/i} kadar büyük olacağını bilmiyordum."
            "Natsuki, yemeğimi denemekte biraz tereddüt ediyor."
            "Ki bu da adil, çünkü yemek biraz daha iştah açıcı görünmüyor ve sunum becerilerim de pek iyi değil. Ama yine de, omletin bir lokmasını alıyor."
            "Yüzünde boş bir ifade ile sessizce kendine bir şeyler mırıldanıyor."
            n "Şu ana kadar iyi gidiyor..."
            show natsuki 1g at lhide
            hide natsuki
            "Sonra Fransız tostunu deniyor ama yutmaya çalışmadan önce boğuluyor ve su içmek için hızla koşuyor."
            "Bu şekilde olmaması gerektiğini düşünmüyorum."
            n "[player]... aptal... "
            "Natsuki konuşmaya çalışıyor ama boğazı aşırı kuru ve sürekli öksürüyor."
            mc "Hadi ama! Yemek yapmada o kadar iyi olmadığımı kabul ediyorum ama bu kadar kötü olamazdı."
            "Natsuki mutfak tezgahına gidip bir şey getiriyor."
            show natsuki 4e at f11
            n "Bu ne?"
            "Koyduğu kabı bırakıyor."
            mc "Bu benim şekerlik."
            n "Hayır, bu bir tuzluk."
            "Tepkisi çok daha mantıklı."
            mc "Şekerliği değil, tuzlu olanı seçtiğimi yemin ederim."
            "Natsuki biraz daha su içiyor."
            n 2e "İki kap da farklı görünüyor."
            n "Bunun nasıl karıştırıldığını anlayamıyorum."
            "Natsuki içini çekiyor ve masaya oturuyor, dirseğini masanın üzerine koyarak elini alnına bırakıyor. Bir tür farkındalığa geldiğini düşünüyorum."
            n 5i "Sen çok önem veriyorsun."
            n "Tabii ki, sadece uyandın ama asıl mesele, bu kocaman yemeği bana yaparken o kadar dikkatlisin ki hangi malzemeleri kullandığını bile kontrol etmedin."
            n 5q "Benim için bu kadar nazik birini ne yaptım?"
            mc "Gerçekten özür dilerim, Natsuki. Daha basit bir yemek yapmalıydım."
            n 4b "Hey, yine de benim için çok yemek yaptın."
            n "En azından diğer kısımlarını yemeyi denemeliyim."
            mc "Fransız tostu hariç, hâlâ yemeklerim pek iyi değil. Geri kalanını yemen gerektiğini sanmıyorum."
            n "Bu durumda paylaşabiliriz."
            n 1y "Burada, Fransız tostunu sen al."
            mc "Üzgünüm, Natsuki."
            n 1j "Şaka yapıyorum. Ama hadi, sen de yemek yemelisin, değil mi?"
            mc "Sanırım öyle."
            "..."
            mc "...Aslında, bu korkunç tadıyor. Hadi biraz mısır gevreği yiyelim."
            n 4b "Ben de bunu düşündüm."
            "İki kase alıp, hem Natsuki hem de ben için mısır gevreği alarak, yaptığım her şeyi unutarak yolumuza devam ediyoruz."
    hide natsuki
    window hide
    scene bg kitchen with Dissolve(2.0)
    window show
    "Yemek yerken, ortasında bir soru sormayı başardım."
    mc "Artık kızarkadaş ve erkekarkadaş olduğumuza göre, gerçek randevulara çıkmaya başlamalıyız, değil mi?"
    # çn: sacma bi anlam karmasası var ne dicem bilemedim
    "Natsuki ağzındaki yiyeceği bana püskürtüyor."
    show natsuki 1p at f11
    n "Ne?!"
    n 4q "...Aslında, bu daha önce yaptıklarımızdan farklı olmayacak. Devam et."
    mc "Bir piknik yapmayı düşündüm. Ne dersin?"
    n 1b "Bu o kadar kötü görünmüyor."
    n "Ama yiyecek yapmaya yardım etmen gerek."
    n "Sana normalden daha fazla tembellik yapmama izin verdim ama benim de sınırlarım var."
    mc "Anlaşıldı. Haftasonu olduğuna göre, yarın yemek yapıp o gün gidelim mi?"
    n "Yeterince malzemen olduğunu düşünüyorsan, öyleyse yapalım."
    n 1a "Geri dönüş yok! Söz verdin."
    "Ben hiç söz vermedim ama durumu anladım."

    
    stop music fadeout 2.0
    window hide
    scene bg bedroom with open_eyes
    play music aNewDay fadein 2.0
    window show
    "Sonunda hafta sonu geldi."
    "Sanırım mutfakta bir şeyler yapma zamanı."
    "Ama Natsuki nerede? Yemeği çoktan yapmaya mı başladı?"
    scene bg kitchen with wipeleft_scene
    "Mutfakta, tahmin ettiğim gibi, bir dizi yiyecek vardı."
    mc "Vay canına! Biliyor musun, Natsuki, senin özel yeteneğinin fırıncılık olduğunu düşünmüştüm!"
    show natsuki 1bd at f11
    n "Evet, öyle ama bu sabah yaptığım tüm yiyecekler fırınlamaya yönelik."
    "Biraz daha yakından bakınca, birçok farklı tatta cupcake olduğunu görüyorum."
    mc "Ah, haklısın."
    mc "Yani, pişirme dışındaki yiyecekleri ben mi yapacağım?"
    n 1bb "Kesinlikle."
    mc "Tamam, o zaman yapabileceğim yiyecekleri sayayım."
    mc "Çırpılmış yumurta, fıstık ezmesi ve reçelli sandviçler... hepsi bu kadar."
    if makeComplex is True:
        mc "Aslında daha fazlasını yapabiliyorum ama, daha önce nasıl gittiğini biliyorsun."
    n 4be "Ne demek bu? O zaman tüm bu malzemeler ne için?"
    mc "Bu gerçekten iyi bir soru."
    mc "O zaman ne olacak? Çırpılmış yumurta mı, yoksa fıstık ezmeli ve reçelli sandviç mi?"
    n 3bb "Sanırım sandviçler."
    mc "Bunlar, yediğin en iyi sandviçler olacak, buna güven!"
    "Natsuki gülümsüyor. Yorgun ama gerçekten mutlu görünüyor."
    show natsuki 1bj at f11
    n 1bk "Bunu kanıtlamanı bekleyeceğim o zaman!"
    hide natsuki with dissolve_cg
    scene bg kitchen with wipeleft_scene
    "Ve böylece, en iyi sandviçleri yapmaya başladım."
    "Aslında, bu biraz abartı. İyi olduklarını düşünüyorum ama bunu, pikniğe gitmeden önce öğrenemeyeceğim."
    scene bg house_entrance with Dissolve(2.0)
    show natsuki 1bb at f11
    n "Her şey hazır mı?"
    mc "Olmalı."
    n "İyi. Hadi gidelim artık!"
    mc "Ne, bu kadar mı meraklısın?"
    "Natsuki'nin yüzü birden gergin bir ifadeye dönüşüyor."
    n 4bq "Hayır! Belki biraz."
    n "Aman tanrım, bunu bilerek yapıyorsun, değil mi?"
    mc "Beni çözmüşsün gibi görünüyor."
    n "Hmph. Kızları rahatsız etmemelisin, gerçekten hoşlandığın sürece, biliyorsun değil mi?"
    mc "Çıkıyoruz, yani ilişkideyiz."
    n 4bs "Ah, evet."
    "Natsuki, \"Ama hâlâ!\" demek üzere gibi görünüyor ama bunu dile getirmeye cesaret edemiyor."
    n 1bq "Tamam, bunu kabul ediyorum. Ama bir sonraki sefer ben kazanacağım!"
    "Sonraki sefer? Ne için kazanmak?"
    n 5bq "Ve kazandığımda, bana bir sarılmayı borçlu olacaksın ya da başka bir şey, henüz detayları çalışıyorum."
    mc "Tamam Natsuki."
    "Ama şu an, bir piknik zamanıydı. Yalnızca sandviç ve cupcake'lerin olduğu bir piknik ama önemli olan yemek değil."
    "Onunla, kız arkadaşım Natsuki ile vakit geçirmekti."
    
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    pause(2.0)
    scene bg flashback_home with Dissolve(2.0)
    
    window show
    o "Hey."
    o "Seninle konuşmak istedim."
    n "Oh, konuşacak çok şey var. Hadi, önce sen başla."
    o "Bak, aramızda bazı şeylerin biraz... zor geçtiğini biliyorum ama gerçekten çabalıyorum."
    o "Bu çok zor."
    n "Bu hiçbir şeyi değiştirmiyor. Yine de bir kızına bakman gerekiyor."
    o "... "
    o "...Biliyorum. Çabalıyorum."
    n "Ne dersen de, baba."
    
    window hide
    show black with Dissolve(2.0)
    pause(2.0)
    scene bg residential_day with Dissolve(2.0)
    play music aNewDay fadein 2.0
    window show
    mc "Peki, nereye gideceğiz aslında?"
    "Natsuki ile evimden çıkıp... bir yere doğru yürüyoruz, sanırım."
    show natsuki 3bb at f21
    n "Bunun planını sen yapmadın mı zaten?"
    n "Hani sen bu fikri ortaya atmıştın?"
    "Oooops."
    mc "Sanırım yakında oturabileceğimiz bir park var."
    n "O zaman seni takip edeceğim."
    n 4bh "Kaybolmazsan iyi olur."
    mc "Evet, evet, biliyorum."
    hide natsuki with wipeleft
    scene bg park_day with Dissolve(2.0)
    stop music fadeout 2.0
    play music NextToYou fadein 1.0
    "Bir süre etrafta dolaşıyoruz—doğru yolda ilerliyordum, yemin ederim—ve sonunda bir çimenlik parka rastlıyoruz."
    "Hava koşulları piknik yapmak için mükemmel."
    mc "Burada olmalıyız."
    show natsuki 1ba at f21
    n "Benim için sorun değil."
    hide natsuki with wipeleft
    "Natsuki, taşıdığı örtüyü yere seriyor ve ben de tutmakta olduğum yiyecek sepetlerini bırakıyorum."
    show natsuki 1bd at s11
    "İkimiz de oturup yemek yemeye hazırlanıyoruz."
    "Natsuki'nin sepetinden bir cupcake alıp bir ısırık alıyorum. Yumuşak, nemli ve bir o kadar da lezzetli."
    mc "Vay canına, bu senin en iyi işlerinden biri olmalı."
    n 1bb "Bilmiyorum, bu... kaçıncı cupcake'im senin için?"
    mc "Bak, bu, senin yaptığın en iyi ikinci cupcake'lerin arasına girecek. Bu bir iltifat."
    "Natsuki gülümsüyor ve sessizce gülüyor."
    n 1bk "Teşekkürler, [player]."
    "Natsuki, yaptığım sandviçlerden birini alıp ısırıyor."
    n 1bj "Kahvaltı yaptıklarından daha iyi, bunu kabul etmeliyim."
    mc "Teşekkürler, tam olarak bunu istiyordum."
    "Evet, bunu kabul edebilirim."
    "Yemek için fazla zaman geçirmedik, bu yüzden sonrasında yapacak pek bir şeyimiz kalmadı."
    hide natsuki with dissolve_cg
    
    "Böylece, örtünün üzerine yan yana uzanmaya karar verdik."
    scene bg sky_day with Dissolve(2.0)
    "Belki romantik bir şans daha denemeliyim?"
    mc "Bu gökyüzü kesinlikle... mavi."
    "Aslında, şimdilik bununla durayım."
    n "Gerçekten de öyle, [player]. Fark ettiğine sevindim."
    mc "Biraz hafiflet beni, konuşacak bir şeyler bulmaya çalışıyorum."
    "Natsuki başını çevirip gözlerimin içine bakıyor."
    n "Bence konuşacak bir şey bulmak zorunda değilsin."
    n "Birlikte olmak zaten oldukça güzel."
    mc "Yanlış değilsin."
    mc "..."
    mc "Hey, Natsuki."
    n "Ne var?"
    mc "Bu hassas bir konuysa özür dilerim, ama geleceğin hakkında ne düşünüyorsun?"
    mc "Bir hayal işin var mı mesela?"
    "Natsuki bir süre düşündü."
    n "Hmm."
    n "Ne yapmak istediğimle ilgili fikirlerim var ama gerçekten bir karar vermedim."
    n "Son zamanlarda odaklanmam gereken çok şey var, bu yüzden şu anda düşünemiyorum."
    "Konuyu değiştirmek isteyen Natsuki, bana da aynı soruyu soruyor."
    n "Ya sen? Hayal işin ne?"
    n "Sonsuza kadar NEET olamazsın."
    "Huh. Hayal işim mi? Animeyi çok seviyorum, bu yüzden yeterince pratik yaparsam bir gün en iyi animatörlerden biri olabilirim belki?"
    "Hayır, bu yanlış. Geleceğim hakkında ciddi olarak düşündüğümü söylersem yalan söylemiş olurum. Hatta bir çırak animatör bile olamam."
    mc "Açıkçası, hiçbir fikrim yok."
    n "Senin için kötü."
    "Natsuki iç çekiyor."
    n "Bir noktada sana iş bulmama yardım etmem gerekecek, değil mi?"
    mc "Eh, alabileceğim her türlü yardıma açığım."
    n "Ha, bunu düşündüm."
    n "Ama neden buna odaklandığımızı bilmiyorum."
    n "Bazen sadece etrafını sevmeyi ve keyfini çıkarmayı öğrenmelisin, [player]."
    mc "Evet, bu doğru. Rahatlama konusunda pek iyi değilim kabul ediyorum."
    n "Ama seninle aynı duyguları taşıdığımı biliyorum. Son zamanlarda sanki dünyanın yükünü omuzlarımda taşıyormuşum gibi hissediyorum."
    mc "Senin için bunu daha kolay hale getirebilirim."
    "Natsuki'ye daha yakınlaşıp yavaşça kollarımı etrafına sarıyorum, bu sonunda bir kucaklamaya dönüşüyor. O, şaşırmış ama yine de mutlu görünüyor."
    n "Y-Ya, ama sonsuza kadar beni kucaklayamazsın!"
    mc "Ama şu an için seni kucaklayabilirim. Zaten daha önce söylediğin gibi, bir süre sonra sana bir kucaklama borçlu olacağım."
    n "Hmph. Tamam..."
    n "Ama neden bu kadar nazik olmaya devam ettiğini hala anlamıyorum."
    n "Bana nazik davranmadım ki."
    mc "Bence son zamanlarda daha yumuşak davrandın aslında."
    n "Gerçekten mi?"
    mc "Evet. Üzerimde etkili olduğunu sanmıyorum ama bunu görmek hoş."
    n "Bazen garip şeyler söylüyorsun."
    mc "Ne, sadece şimdi mi fark ettin?"
    n "Kötü bir şey olduğunu söylemiyorum. Belki de sana çekilmemin nedenlerinden biri bu."
    n "Ya da belki değil. Ama anladın işte."
    mc "Mmhmm."
    "O pozisyonda neredeyse bir saat kaldık. Normalde böyle bir şey olacağını düşünmezdim ama bu kadar huzurlu bir günde her şey böyle bir araya geldi."
    scene bg park_day with Dissolve(2.0)
    mc "Şimdi eve gitmemiz gerekiyor."
    "Natsuki beni daha sıkı kucaklıyor."
    show natsuki 1bu at f11
    n "Gitmek zorunda mıyız?"
    mc "Keşke kalabilseydik ama, senin de dediğin gibi, hiçbir şey sonsuza kadar süremez."
    mc "Yapmamız gereken ödevlerimiz var, bu yüzden..."
    n 5bg "Tamam."
    stop music fadeout 2.0
    hide natsuki with wipeleft
    "Hayal kırıklığına uğramış Natsuki, eşyalarımızı toplamaya başladığımızda kalkıyor. Hemen eve geri yürüdük."
    window hide
    scene bg home_interior with Dissolve(2.0)
    window show
    "Salonuma döndüğümüzde, yan yana kanepede oturuyoruz."
    mc "Neyse, böyle oldu."
    show natsuki 5bu at t22
    "Artık kalan bir cupcake alıyorum. Rahatım ama Natsuki'nin aklında bir şeyler var gibi görünüyor."
    mc "Her şey yolunda mı, Natsuki?"
    "Bir ısırık alıyorum ve onun cevabını bekliyorum."
    show natsuki 5bu at f22
    n "Düşünüyorum ve..."
    play music Dusk fadein 2.0
    pause(2.0)
    "Natsuki neredeyse tam bir dakika duraksıyor."
    n "Sana yeterince güveniyorum ki bunu söyleyebilirim ama bununla ilgilenmeni istemiyorum."
    mc "Ne hakkında konuşuyorsun, peki?"
    n 4bu "Dediğim gibi, seni dahil etmek istemiyorum."
    n "Beni merak etme. Olanı kabul ettim bile."
    "Ona yardım etmek isterdim ama nasıl? Açıkça bu konuyla benim bir ilgim olmasını istemiyor."
    mc "Dediğin gibi."
    show natsuki 1bu at t22
    "Natsuki kalkıyor."
    n "Biraz anime izlemeye gidiyorum."
    mc "Eğer bana ihtiyacın olursa, sadece söyle."
    show natsuki 1bu at lhide
    hide natsuki
    "Natsuki kaygılı bir ifadeyle yanından uzaklaşıyor."
    "Bunu izlemek acı veriyor ama böyle zamanlarda kendime sadık kalmam gerekiyor. Klişe gibi gelse de, sabır bir erdemdir."
    "Ve sabır beni buraya kadar getirdi. Natsuki ile ilişki kurmamı sağladı."
    "Her şeyin sonunda yoluna gireceğini düşünüyorum. Beklediğim ve gelecek olan her şeye hazırlıklı olduğum sürece, başarılı olacağım."
    
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    pause(2.0)
    scene bg bedroom with Dissolve(2.0)
    play music Dusk fadein 2.0
    window show
    mc "Natsuki?"
    "Uyanıyorum (alarmımdan önce, şaşırtıcı bir şekilde) ve odada Natsuki'yi göremiyorum."
    "Geçen gece hiçbir şey duymadım, bu yüzden kötü bir şey olmamış olmalı, değil mi? Şu an zihnimin beni ele geçirmesine izin veremem."
    "Yavaş ama kendinden emin bir şekilde oturma odasına doğru yürüyorum."
    mc "İşte burada."
    scene bg home_interior with Dissolve(2.0)
    show natsuki 12bd at s11
    "Natsuki'nin kanepede, etrafına bir battaniye sarılı olduğunu görüyorum. Yanına oturuyorum."
    mc "Ne oldu?"
    show natsuki 12ba at f11
    "Natsuki bir şey söylemek istiyor gibi görünüyor, ama bunu başaramıyor."
    n 1bu "Sadece bir kabustu."
    mc "Hepsi bu mu? Burada olman için gerçekten kötü bir rüya olmalı."
    n "Bir kâbus, uyuduğun odada olursa, o odada kalmak istemezsin, değil mi?"
    n "Artı, seni uyandırmak istemedim."
    mc "Beni istediğin zaman uyandırabilirsin, Natsuki. Ben buradayım senin için."
    n 1bu "Evet ama, bununla başa çıkmanı istemiyorum."
    n "Bu senin savaşın değil."
    mc "O zaman neler olduğunu bana söylemeyecek gibisin."
    mc "Bunu bir suçluluk hissi yaratmak için demiyorum ama {i}sen{/i} için en iyisini düşünmelisin."
    n "Biliyorum, [player]. Belki bir gün sana anlatırım."
    mc "Tamam, Natsuki."
    show natsuki 12bd at f11
    "Natsuki'ye sarılıyorum, gözlerini kapatıyor ve derin bir nefes alıyor."
    mc "Şimdi, kahvaltı yapalım mı?"

    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    pause(2.0)
    scene bg flashback_home with Dissolve(2.0)

    window show
    n "Bunun böyle devam etmesini istemiyorum. Eski \'sen\'i geri istiyorum."
    n "Peki, neyi yanlış yaptım baba? Neden böyle muamele görüyorum?"
    n "Beni neden bu şekilde ihmal ettin?"
    o "Bazen işler böyle olur."
    o "Gerçekten bunun için bir sebep yok, en azından kasıtlı olan bir sebep."
    o "Bazen sadece olur."
    o "Zaten olmasını istemiyorum."
    n "Ama neden?"
    o "Dediğim gibi, mutlaka bir sebep yok!"
    o "Bunu kabul etmeyi öğrenmelisin!"
    n "Hayır. Bir sebep olmalı."
    n "Sana ne oldu?"
    n "Her şeyin daha iyiye gitmesini istiyorum."
    n "Seni normal görmeyi istiyorum."
    n "Bu asla olacak mı?"
    o "... "
    o "... "
    o "Bilmiyorum, Natsuki. Elimden gelenin en iyisini yapmaya çalışıyorum." 

    window hide
    show black with Dissolve(2.0)
    pause(2.0)
    scene bg streets_day with Dissolve(2.0)
    
    # Devam ederim kanzi
    window show
    "We continued to go on dates for at least over a month."
    "Things were pretty normal, but on some occasions I noticed a tall man that Natsuki would glare at for a few moments; she never told me who he was."
    "Not until today."
    "Natsuki and I were about go on a date at the time. We had picked a fast food restaurant to go to, but just before we walked in, Natsuki saw that man again."
    show natsuki 1bu at f11
    n "Let's go somewhere else."
    show natsuki 1bu at f41
    play music Dusk fadein 2.0
    " Before I could object, she grabbed me by the arm and tried to drag me away. That is, until {i}he{/i} spoke up."
    o "You, over there. I need to ask you something."
    "I froze, not even Natsuki being able to move me."
    show natsuki 12bb at f41
    mc "Y-Yeah?"
    "I had no idea what to think at the time. Who was this guy? Am I about to be dead?"
    o "Are you dating Natsuki?"
    "I gulped."
    mc "Y-Yes."
    o "That's all I wanted to know. Thank you."
    "And then he just... walked away. Leading me to right now, where I'm left extremely confused."
    "Anxiety clouded my thoughts. Yeah, I was definitely about to be dead."
    mc "What did he even want with me? What did he want with {i}you{/i}?"
    show natsuki 1bc at f11
    n "Calm down, [player]."
    "Natsuki grabs my shoulder, but I'm still shaking."
    mc "How am I supposed to calm down? This reeks of creepiness."
    "Natsuki looks down at the ground."
    n 2bu  "...He's my dad."
    mc "What?!"
    n 1bc "I said I don't want you to get involved."
    n 42bc "If it comes down to it, then I'll handle it."
    "Natsuki has a determined look on her face. Just what am I missing here?"
    mc "Are you sure you can handle it, though?"
    mc "I'm not trying to downplay your strengths, but I feel like there's something deeper going on here that I'm not being told about."
    n "You care too much, [player]."
    n 1bi "You really do."
    "Natsuki clenches her fist, her face being a mixture of irritated and sad."
    mc "Let's go home, Natsuki."
    n "Yeah..."
    hide natsuki
    scene bg home_interior with Dissolve(2.0)
    stop music fadeout 2.0
    play music Thoughts fadein 2.0
    show natsuki 1bc at f11
    "We head home, as Natsuki sighs and walks towards my room."
    show natsuki 1bc at lhide
    hide natsuki 
    "Maybe I should do something for her. Is there something nice I could surprise her with?"
    "As I sit down on my couch, I notice a flyer sitting on the coffee table in front."
    "Parfait Girls: The Movie, huh? In theaters tomorrow, too. Natsuki did tell me about it awhile ago, I think. This was supposed to be an original story not in the manga or anime, right?"
    mc "Hey, Natsuki?"
    scene bg bedroom with wipeleft_scene
    "I shout as I walk into my room. She's laying on my bed, still seeming conflicted."
    show natsuki 1bu at t44
    n "Hmm?"
    show natsuki 1bb at f11
    mc "Are you free tomorrow?"
    n "Am I ever not free?"
    "Thinking about it... I don't think I've ever run into a situation where she was \'too busy\' or something like that."
    mc "Well, I'm taking a nap. I promise tomorrow will be good."
    "I lay down on the bed and close my eyes."
    stop music fadeout 2.0
    show black with dissolve_cg
    pause(1.5)
    scene bg bedroom_night with open_eyes
    "I soon fall into a deep sleep, and find myself waking up in the middle of the night."
    "Why wasn't Natsuki next to me, though?"
    show black with wipeleft
    "I slowly walk into the living room."
    scene bg kitchen_night with wipeleft_scene  
    show natsuki 1bu at t44
    "I turn over to the kitchen and see Natsuki getting something out of the fridge."
    mc "Natsuki? Why are you up so late?"
    show natsuki 1bp at h44
    "Natsuki, shocked to hear someone awake, drops the food she's holding. Luckily nothing breaks."
    show natsuki 1bg at t44
    n "I could ask you the same thing!"
    mc "Hey, I woke up a few minutes ago. I don't think you went to sleep the same time I did, though."
    n 12bc "I'm probably stressing you out with this, aren't I?"
    play music Dusk fadein 2.0
    show natsuki 12bd at lhide
    hide natsuki
    "Natsuki rushes back to my room, ashamed."
    mc "Natsuki!"
    scene bg bedroom_night with wipeleft_scene  
    "I planned on going back to sleep anyway, so I head back to my room and see Natsuki laying on my bed, her face buried in a pillow."
    mc "You're not stressing me at all, Natsuki. I might get a bit concerned, sure, but nothing I can't deal with."
    
    n "You know, I've actually recently been thinking about telling you."
    mc "Telling me what?"
    n "You already know, [player]."
    "Is this about her dad?"
    n "But I can't bring myself to do it. I don't know if I ever will."
    "Even though I can't see her face, it sounds like she's crying."
    mc "One step at a time, Natsuki."
    "I get into bed with her."
    mc "Now, hold my hand."
    "Natsuki tightly grips my hand."
    mc "There. Feel a bit calmer?"
    mc "Get some rest. I said I had something planned for tomorrow, didn't I?"
    mc "You'll like it, believe me."
    "Natsuki stops making noise, which leads me to assume that she's fallen asleep. I should probably do the same."
    
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    scene bg bedroom with open_eyes 
    window show
    "As I wake up the next morning, I notice that Natsuki is sound asleep. One of the first times I've ever woke up before her, now that I think about it."
    play music Thoughts fadein 2.0
    scene bg kitchen with wipeleft_scene
    "While I leave my room to make breakfast, I feel a tinge of anxiety. I ignore it for now, but how long can I keep this up? How long until I break?"
    "Certainly not something I want to think about while making scrambled eggs, so I don't."
    "Instead, once I'm done making breakfast, I go back to my room and use my time to order tickets online for the Parfait Girls movie I plan on taking Natsuki to."
    scene bg bedroom with wipeleft_scene    
    "I check back in my room and see that Natsuki is awake. Still concerned for her, I ask her how she's doing."
    mc "Feeling any better?"
    show natsuki 1bc at f44
    n "A little."
    mc "Good. Remember, I've got something neat in store for later today."
    n "Wake me up when it happens, then."
    hide natsuki with wipeleft  
    "Natsuki turns over and tries going back to sleep."
    "My mind starts to drift towards worrying again, but I don't want to keep worrying like this."
    "Not yet again."
    window hide
    scene bg bedroom with wipeleft_scene
    window show
    "A few hours pass, and it's almost time for us to go."
    mc "Ready, Natsuki?"
    stop music fadeout 2.0
    show natsuki 1bw at t44
    play music NatTheme fadein 2.0
    "Natsuki groggily responds."
    n "For what?"
    mc "You already forgot?"
    n "You never even told me what we're doing yet."
    "Natsuki gets out of bed."
    mc "Ah, that's true. Well, how about you find out now?"
    "I hold up the tickets I printed earlier."
    n 1bc "Ahh!"
    n 1bb "Actually, it's not that surprising. I already knew you were getting the tickets."
    mc "Oh."
    n "Yesterday I would've asked if we could go, but you know how tired I was."
    n "Earlier today, though, I was going to try to ask, but I caught a glimpse of when you were printing the tickets, so..."
    "Huh. I guess she must've gotten a glass of water or something, and I didn't notice with the printer drowning the sound out."
    mc "Anyway, it's not long until it starts. Let's go!"
    hide natsuki with wipeleft  
    scene bg streets_day with wipeleft_scene
    "Shortly after, we head outside as I lead Natsuki to a movie theater."
    show natsuki 1bc at f11
    n "Why are you doing this, anyway? Not that I'm upset or anything."
    mc "I dunno, you seemed to be having a hard time lately, so I thought I'd do something to take your mind off of it."
    "Natsuki doesn't look grateful that often, but when she does, it's unbelievably satisfying."
    n 1bq "Thank you. Seriously, I don't deserve any of this."
    n "...Well, I deserve some of it, but still."
    "If nothing else, at least Natsuki seems to be going back to being her old self."
    "We walk up to the man at the ticket counter."
    mc "Two seats for the 3:30 PM screening of Parfait Girls, please."
    $o_name = "Employee"
    o "Go ahead."
    $o_name = "???"
    hide natsuki with dissolve_cg
    show black with dissolve_cg
    "Natsuki and I walk into the theater. The lobby is gigantic, containing more than enough space for a place like this."
    "The snack vendor is full of delicious treats, filled with traditional movie theater snacks from around the world."
    "That, of course, wasn't the main attraction. We head into the cinema room where the movie is supposed to play, only to find out we were the only people who showed up."
    n "Did we arrive on time?"
    mc "It's 3:30 now, isn't it?"
    mc "But hey, we do have front row seats!"
    mc "...Not that it matters."
    stop music fadeout 2.0
    "We sit down next to each other as the movie begins."
    "..."
    "..."
    "..."
    pause(1.5)
    
    play music NatTheme fadein 2.0
    mc "So what did you think of it, Natsuki?"
    show natsuki 4bb at f11
    n "I don't know if it lived up to the hype, but I thought it was decent."
    mc "Same here. I was unsure about how well they could adapt the series into a movie, but they did a pretty good job."
    "I pull away my arm that was wrapped around Natsuki's shoulders and stand up."
    mc "Time to go home."
    n "Hey, [player], there's something I want to say first."
    "Natsuki looks off to the side, like she always does when she's nervous."
    mc "What is it?"
    n 4bq "Um... thanks."
    n "I've never had a boyfriend like you... or a boyfriend at all..."
    n "Or even a friend like you... or anyone at all like you."
    n "You're the only one who takes me to movies I want to watch, or makes food with me."
    n "You're the only one who's been this nice to me... so if I'm ever mean towards you, you know part of the reason why."
    n "I'm shocked by how kind you are, so I don't always know how to react."
    n "And I think a lot about how other people see me, since I want to be the best. So that's also part of it."
    n "..."
    n "..."
    n 12bc "...This is stupid. Sorry for wasting your time."
    show natsuki 12bc at lhide
    hide natsuki
    "Natsuki's head droops as she gets up and heads towards the exit."
    "What is going on, Natsuki? What's the final piece of this puzzle I'm missing?"
    
    
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    pause(2.0)
    scene bg flashback_home with Dissolve(2.0)
    
    window show
    o "Natsuki, we need to talk about your grades."
    n "Yeah, so, what about them?"
    o "You know what I'm referring to."
    n "My grades suck, there you go. What else is new?"
    o "This has to change. I don't know if you'll need a tutor or something, but we can't let things keep going like this."
    o "We can't let you be held back a second time, Natsuki."
    n "So what if I am? Is it really that big of a deal?"
    o "We both know that your education is important."
    n "Even then, how are my grades supposed to change if the situation that I live in won't change? How are my grades supposed to get better if living here doesn't get better?"
    n "Going through all this... I can only do so much."
    o "What are you going to do if you get held back again, then? What will you tell your friends? Will you lie about your age to the people you meet?"
    n "Were you listening to anything I even said?"
    o "I did, but you're missing my point."
    n "No. I get your point, but you don't seem to get mine."
    n "But if that's how you want to go about this, then fine."
    n "It's not like I can do anything about this anyway."
    n "It's not like I was ever able to do anything about the things going on in my life."
    
    window hide
    show black with Dissolve(2.0)
    pause(2.0)
    
    
    window show
    
    "Things continued as normal for the next few days."
    "Actually, I don't know if I'd consider it \"normal\". Something definitely felt off, and in the middle of one night, I would learn why."
    scene bg bedroom_night with open_eyes   
    "It had to have been around 3 AM at the time. Natsuki and I were asleep, until I heard a loud noise along the lines of a thud."
    "I turned towards Natsuki's side and saw that she rolled off the bed."
    "I didn't think much of it initially. I thought she had another nightmare or something and it happened because of her tossing and turning."
    "To some degree, that was true, but it was what I found when I looked at her after she fell that I discovered a horrifying fact."
    play music Excuses fadein 2.0
    "When she fell, her shirt shifted in a way that her right shoulder became visible, and the final puzzle piece I had been looking for had finally appeared."
    show natsuki 12bb at t41
    "She looked up at me, albeit groggily. She had just woken up, after all."
    mc "Natsuki?! What's with that bruise? Natsuki!"
    "And here I am now. Shocked and furious to see such a thing."
    "I could spend time coming up with a bunch of other possibilities explaining why she has that bruise, but there was no point. Everything already fit together."
    "The thoughts rush through my head."
    "The reason why she has a bruise..."
    "The reason she came to live with me..."
    "The reason she acts the way she does towards her dad..."
    "There is no other explanation. Maybe I'm just jumping the gun, but this is the conclusion I have come to: Natsuki was hit by her dad."
    "If that isn't bad enough, the potential implications could be even worse."
    "I feel dizzy. Now what? Now how do I handle this? It's not like I can ignore this."
    "I was able to ignore it before, but that was because I didn't realize what was going on; I didn't realize the seriousness of the situation."
    "But now that I do, I have to do something."
    n 12be "[player]... This bruise, uh..."
    mc "Don't bother."
    mc "I already know."
    "Natsuki has a guilty expression on her face."
    n 12bd "Are you mad at me, [player]?"
    n "I don't have any excuses anymore. Before, I hid it from you since I thought I was doing the right thing by keeping you out of this, but..."
    mc "I'm not mad at you."
    mc "I wish I didn't have to find out like this, but it's not you I'm upset with, Natsuki."
    mc "I'd say that we should discuss this tomorrow, but I don't think either of us feel like going back to sleep."
    "I motion for Natsuki to get up and she gets back in bed."
    show natsuki 12bd at f11
    mc "Do you want anything to drink? Are you hungry?"
    n "No."
    n 12be "Just... I want to get this over with."
    "Natsuki's face is a continuous whirlwind of emotion. Fear, regret, and sadness all cycle through at the same time."
    mc "When did this happen, Natsuki?"
    "As I talk, I get back into bed as well. The comfort I got from laying down covered in blankets was gone now."
    n "Remember that day when I snapped at you and said I hated everyone?"
    mc "It's not a good memory to go back to, but yes."
    n "After I ran out of the classroom, I headed home right after. Then, I was having an argument with my dad as usual, and--"
    "I stop her right there."
    mc "Hold up, \'as usual\'? Does this happen often or something?"
    n "Err, I'd have to go back a bit further to expla--"
    "I feel bad for interrupting again, but I need to get the bruise out of the way first."
    mc "Sorry, go back to the story. We can talk about the rest later."
    n "Yeah. So I was arguing with my dad, and then it escalated, and then..."
    "Natsuki shows me her bruise again."
    mc "Then you ran to my house, didn't you?"
    n 12bd "Yeah."
    mc "..."
    mc "Sorry, I haven't fully processed this yet. It's been over a month since then, though."
    mc "Shouldn't your bruise have faded out at this point?"
    n 12be "I don't know. I thought about that too, but I didn't want to tell anyone, so..."
    mc "Again, we can focus on that later. I think I understand everything now, but I need to ask you more about the situation with your dad. Was it always like this?"
    "Natsuki takes a deep breath."
    n "My home life used to be fine, or at least better."
    n "It wasn't amazing or anything, which has to do a lot with how tight our money situation was."
    n "My mom passed away early into my childhood, so my dad took care of me from that point on."
    n "He wasn't the worst father ever or anything. He got mad a lot, but not nearly as mad as he's gotten over these past few years."
    mc "Did something happen to make him more upset like that?"
    n 12bc "I don't know. Maybe he just couldn't deal with everything put together."
    n "Him and my mom were apparently married for fifteen years before they had me. I think raising a child with his wife was too important for him to put into words."
    n "Our money situation has gotten worse recently too. We haven't totally sunk yet, although it has to be tough for him."
    mc "That doesn't justify what he did."
    n 12bc "I didn't say it does! I'm mad about this too."
    "I sigh. This is so much to take in all at once. Maybe I really should've waited until tomorrow to talk about this, but it's too late for that now."
    n 12bc "As the years went by, my dad started to distance himself from me."
    n "Well, it's more like he distanced himself from {i}everyone{/i}."
    n "He can do that if he wants, but he still has a daughter to take care of. Occasionally making dinner isn't enough."
    n "I felt neglected because of it. It was like I did something wrong, but I couldn't figure out what it was."
    mc "Does he drink, Natsuki?"
    n "No, I don't think so."
    n "I never saw him drink, anyway."
    mc "Hmm."
    n "As I was saying, I would argue with him a lot about how I was treated. It wasn't only neglect that was the problem, it was how he acted towards other things, too."
    n "He had this perfect idea of what he wanted his daughter to be like. He was willing to give some leeway, but not enough to let me do things like keep my manga collection at home."
    mc "He wanted to have that much control over your life when he could barely take care of himself?"
    n "Basically."
    "Wow. The more of this I hear, the more I feel bad for Natsuki."
    "What she had been going through is not how someone should have to live."
    n "Because he wanted me to be the best daughter ever, that's what he taught me for years to do."
    n "He wanted me to rise above everyone else."
    n 12be "And, yeah, wanting me to be successful is one thing, but..."
    mc "He didn't have to push it onto you as hard as he did, right?"
    n "Yeah. And it wasn't exactly him focusing on only my grades, either."
    n "I've never been good enough at school to be a straight A student anyway."
    n "He told me to be the best socially, too, and to have the most friends."
    n "That even though it might not always work out, to make sure to try to talk to people."
    n "I never figured out what to do. I never wanted to figure out if I should take advice from him of all people."
    n "It didn't really matter, though. In the end, I had a hard time making friends, because I had trouble trusting people thanks to him."
    "..."
    "I can't even think right now. My mind is frozen."
    "..."
    n "Like I said, I didn't want to end up the way I did."
    n "Things just happened that way. Sometimes I'd be try to be nice, but a lot of times I didn't want to show any weakness."
    n "I don't get why it happened that way, but it did."
    "Natsuki pauses, taking a deep breath. Remembering all this can't be easy."
    n "I think the reason why he was so obsessed with me being successful is because of himself."
    n 12bd "I think he didn't want me to turn out the way he did."
    "Natsuki looks like she's about to break down. Regardless, there's something I need to know."
    mc "Natsuki."
    mc "Do you still care for him?"
    "Natsuki thought long and hard about that question, as we sat in complete silence."
    n "A part of me does."
    mc "Okay, let me make sure we're on the same page here."
    mc "What your dad did to you is abuse."
    mc "I need to make something clear. Another one of his actions was undeniable, unjustifiable neglect towards you."
    mc "How do you fully feel about him? Just, think of everything, Natsuki."
    "I give Natsuki a few minutes while I wait for her to come up with an answer."
    "Learning all this is so surreal. It's like when you know something's wrong, but only later realize the extent of how awful it is."
    "I think it's funny how this turned out. Not that kind of funny, but I'm talking more about how I came to find out about this."
    "Natsuki seemed bent on not letting me find out about this situation. She didn't always do a great job, but she continued to try hiding it."
    "But then there's tonight. Because my bed is up against the wall, you can only fall off of it if you lay down on the left side."
    "I was the first one to get into bed that night, and I laid down on the right side."
    "So, the only option was for Natsuki to lay down on the left side."
    "If that didn't happen, she wouldn't have fallen off the bed, I wouldn't have seen her bruise, and I never would've learned the truth behind all this."
    "I know I was trying to give Natsuki time to think, but a thought crossed my mind."
    mc "Did your dad ever try to take his life?"
    n 12bc "Huh?"
    mc "I asked if your dad tried committing suicide at any point."
    n "He hasn't."
    mc "I'm trying to figure something out."
    mc "You said that he distanced himself from everyone, and that you think it was because he was sick of life piling up on him, right?"
    mc "He lost his wife, his financial situation was rough, and so on."
    n "I think so."
    mc "Would he have tried to take his life?"
    mc "I'm sorry if that sounds random, but it's something I was thinking about."
    mc "He had to have some reason to live, wouldn't he?"
    n "Or you're looking too deep into it."
    mc "No, I think I'm onto something."
    mc "Otherwise it leaves only two possibilities: there was another reason he distanced himself from everyone, or he had no reason to live."
    mc "There's nothing pointing to the first possibility and I don't think it'd make sense if there was, either. As for the second possibility, he hadn't even attempted suicide, right?"
    n 12bg "Again, you're looking way too deep into it."
    n "You can't tell how someone is feeling when you don't know them well enough."
    n "It's just not possible."
    mc "I also remember you suggesting that it was possible the reason your dad was so obsessed with you being successful was because he didn't want to see you end up like himself."
    mc "What if he kept living for you?"
    mc "If it were true then it would be a twisted, sick way to convey love when you look at how he treated you."
    mc "But even with how angry I am at him, I can't totally ignore that maybe that was the situation."
    "I'm even more conflicted now. There is absolutely no justifying his actions, and violence is never the answer, but maybe I really am looking at this from the wrong perspective."
    "Perhaps there is no {i}right{/i} perspective to this, either."
    "Again, what he did was despicable, but I do wonder..."
    mc "I can't believe I forgot to mention this, but this is the first time he hit you, right? That's what I had been getting from what you said."
    n "This is the first time he had hit me, yes."
    n "Back when he and my mom first got married, they agreed they would never use violence to get a point across if they ever had kids."
    n 12bf "I wonder how s-she would feel about all this..."
    "Natsuki finally breaks into tears."
    mc "It's been a long night, Natsuki."
    mc "I'm proud of you for telling me all this."
    "Natsuki struggles to speak."
    n 12bi "I-It's not like I had a choice!"
    mc "Maybe, but that doesn't make it any less difficult."
    n "How much longer is this going to l-last?"
    "Natsuki cries harder."
    mc "Hey, I'm your boyfriend. One of the things I'm supposed to do when you're having a hard time is to comfort you."
    mc "So let me do that. Let me comfort you."
    hide natsuki with wipeleft
    "We both lay down and hug each other. It was the most personal, emotional hug I had experienced."
    "...I think even I cried a little."
    window hide
    stop music fadeout 2.0
    show black with Dissolve(2.0)
    
    play music alarm 
    window show
    "{i}BEE--{/i}"
    scene bg bedroom with open_eyes 
    play music Thoughts fadein 2.0
    "There was no point to the alarm clock today."
    "I didn't care what the Literature Club was going to think or say, but we weren't going to school today."
    "Looking at Natsuki, seeing that she's still hugging me even while she's asleep... there's no way I could make her go to school."
    "I don't want to leave her alone, either, so that's just how it is."
    "I'll admit I'm not totally sure about everything that was said last night."
    "There's still many questions that haven't been answered (plus ones that haven't been asked) and we haven't figured out what to do about Natsuki's dad if we do end up making a decision, either."
    "Regardless, I said that Natsuki could stay with me as long as she'd like. It's not like I'd break that promise after this long."
    "I think about getting up to make breakfast, but I can wait. I want to keep Natsuki company for as long as possible."
    "Dozens of thoughts continuing to swirl through my head, roughly ten minutes pass. But before I can drift back to sleep, Natsuki wakes up."
    show natsuki 1bh at f11
    n "Huh?"
    "Natsuki panics."
    n "[player]! We're about to be late for school!"
    mc "You didn't forget about what happened last night, right?"
    n 1bu "Yeah, but..."
    hide natsuki with wipedown
    mc "Even now, you're still pushing yourself."
    mc "You have to rest, Natsuki."
    "Natsuki looks as if she's about to fight back only for her head to land back on the pillow."
    n "Fine."
    n "..."
    n "I like you, you know."
    "A smile comes across Natsuki's face, which surprises me a little. I didn't think she'd be smiling in this situation."
    mc "I like you too, Natsuki."
    mc "We are dating for a reason, after all."
    n "Yeah, but I don't feel like I say it enough. I'm kinda crappy sometimes."
    n "But with you, I feel like I can do anything."
    "Natsuki pulls me closer and hugs me tighter."
    n "So... stay with me, okay?"
    n "Please..."
    "I don't know if she's acting like this because she's sleep deprived or exhausted or something, but I-I'm not complaining or anything."
    mc "I'll stay with you for as long as you want, Natsuki."
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    
    window show
    scene bg bedroom_night with open_eyes
    play music Dusk fadein 2.0
    "Ugh... what time is it?"
    "Unaware of what's going on around me, I check my phone to see the time."
    "Almost 7 PM already? We really slept that long?"
    mc "Natsuki? Are you awake?"
    "It doesn't seem like it, the way she's still been holding me."
    show natsuki 1bb at t11
    n "...Huh?"
    show natsuki 1ba at t11
    "Natsuki wakes up and rubs her eyes."
    mc "It's almost 7 PM."
    n "Okay."
    hide natsuki with dissolve_cg
    "Natsuki tries going back to sleep. Which is one thing, but can things be swept under the rug this easily?"
    "What am I even thinking? Natsuki's been through more than enough; it'd be selfish to try to get her to wake up when she's fine with sleeping."
    "It does make me think about how I'm handling this situation in general."
    "I've had no experience with what she's been going through or anything similar, either. Am I really qualified to give advice for this?"
    "And if not me, then who? I haven't asked Natsuki about her thoughts on counseling or anything yet, but I'm the person she trusts the most right now, aren't I?"
    "It might seem like I'm overthinking this a bit, but I think this is important enough for that not to matter."
    "What I say from this point forward could potentially change her life forever."
    "Maybe it could change mine, too."
    
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    window show
    scene bg bedroom_night with open_eyes
    "I continued to sleep and woke up at around 11 PM. I don't think I've ever slept this long before, actually."
    show natsuki 1bu at t41
    "Natsuki is up this time too, though, as I turn over and see her reading some manga."
    show natsuki 1bu at t11
    mc "Hey."
    "She turns her face to me with a sliver of nervousness in her expression."
    n 12be "What?"
    mc "Can we talk?"
    "Natsuki looks as if she wants to put it off, which I can't blame her for."
    n "You're probably gonna bug me until I say yes, so..."
    "Natsuki puts the manga down and pulls the bed's blankets closer to her."
    mc "Both of us are on the same page about the situation with your dad, right?"
    mc "But that creates another issue, which is figuring out what to do about it."
    n 1bu "Why do we need to do anything about it?"
    mc "What do you mean?"
    n "Like I said, why do we have to try to fix it in the first place?"
    "Is she even wrong? Does there need to {i}be{/i} a solution?"
    mc "Well, do you still care for your dad?"
    n 1bc "I do, but I'm happy living the way I am at the moment."
    "Am I getting myself into something that ultimately isn't for me to try to change?"
    mc "Do you think you'd be happier if things were patched up?"
    n "Maybe I would be, but I don't want to take the risk to find out."
    "Am I going in circles thinking about this?"
    "I want to help Natsuki. She's so, so important to me and I love her so much, but I have to question if this is okay for me to do. I don't think she's ever actually asked for my help with this, has she?"
    n 12be "Can we at least talk about this later?"
    mc "I don't know if we should."
    mc "I'll be honest, I'm extremely unsure about what I'm saying right now."
    mc "But would things be the same if we let this go?"
    mc "Would things be the same the next time we go on a date?"
    mc "Like I said, I don't know what we should do about your dad."
    mc "I just think it's gonna feel weird if we don't do something."
    n 3bu "I used to think the same thing, you know."
    n "I thought about it a lot when I first came to live with you. Remember how tense I was back then?"
    n "Then I learned to... let it go, I guess."
    n "Eventually I started dating you, and here we are now."
    n "There's no problem with us living like this, is there?"
    n 4bu "My dad doesn't seem to care enough to talk with me anyway."
    "I was thinking about that, actually. What's up with the times we found her dad in public? He didn't speak to Natsuki, but he did ask at one point if I was dating her."
    mc "If that's what you want, Natsuki, then I'll respect your wishes."
    mc "I'll admit that I'm still curious about a lot of things, but as you said, there's no harm in the way we're living."
    mc "If you want to put this aside for now, then that's okay."
    show natsuki 12bd at f11
    "Natsuki hugs me."
    n 12be "Thank you, [player]."
    "Natsuki has been so sweet lately. That's probably because she's speaking to her boyfriend, but living in a healthier environment is probably influencing her, too."
    "Maybe it is okay to end things here. We're both happy now, so maybe it's fine to leave it at this, since I don't think anything bad will come out of it."
    "Right?"
    
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    window show
    "I know things won't stay like this."
    "I know something is going to happen."
    "I know there's no way this is over."
    "But until then, I'm going to enjoy whatever happens next. There's no point in being anxious about something that hasn't happened yet."
    "In other words, it's time to relax."
    
    
    window hide
    show black with Dissolve(2.0)
    window show
    "It's been awhile since I learned what was going on with Natsuki and her dad. As it turns out, it was easier to let go of than I thought it'd be."
    "In fact, I've been looking forward to today."
    n "[player]! Wake up!"
    scene bg bedroom with open_eyes
    play music aNewDay fadein 2.0
    mc "I'm awake."
    show natsuki 1bd at f11
    n "Good. Happy Valentine's Day!"
    "Natsuki pushes a tray of homemade chocolates towards me."
    mc "Thanks, Natsuki."
    "The chocolates all have a different shape, as if they were made with uniqueness in mind. I pick one up and take a bite, experiencing one of the best chocolates I've eaten in a long time."
    mc "Wow, this tastes great! Nice job."
    n 1bh "Y-Yeah, I tried."
    "Natsuki tries gathering her courage to say something."
    n 1bq "So, um..."
    mc "Yeah?"
    n "Since it's Valentine's Day, shouldn't we... uh, go on a date or something, too?"
    mc "Sure, I don't see why not."
    n 1bb "Duh!"
    n 1bc "...That's as far as I got, actually. Where should we go?"
    mc "That's a good question."
    "We sit there for a few moments, having no idea where to go from here."
    mc "You know that place we go to on picnics sometimes? There's a lake near there that would be a nice place to relax at."
    n 1bq "Yeah, I know where you're talking about."
    n "Um... I-I'll be waiting, then, I guess."
    hide natsuki with wipeleft
    
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    window show
    scene bg home_interior_night with Dissolve(2.0)
    "We spend the rest of our day normally until night time, at which point it's time to go."
    mc "Well, I'm finished getting ready. What about you, Natsuki?"
    show natsuki 1ba at f11
    n "I'm ready. Are we gonna get going or what?"
    mc "Yeah, let's go."
    hide natsuki
    scene bg residential_night with wipeleft_scene
    pause(1.5)
    scene bg park_night with wipeleft_scene
    play music NatTheme fadein 2.0
    "Natsuki and I walk out the door and meet the cold air of the night, along with the light breeze complimenting it. From there, we head to the place I have in mind."
    "Once we get there, we realize that maybe my idea for a date location that I came up with on the spot wasn't so bad after all."
    "The water is gorgeous. The moon shines down on the lake, giving an amazing amount of light considering what time it is."
    "We both sit down on the edge, arms wrapped around each other as we stare into the moonlight."
    mc "Man, this place is beautiful."
    mc "Not as beautiful as you, of course."
    show natsuki 5bq at f11
    "Natsuki looks disappointed."
    n "You're just looking for cheesy stuff to say."
    "To be fair, she's not entirely wrong."
    mc "Yeah, but that doesn't stop it from being true, does it?"
    n 4bj  "Well, I'll accept the compliment."
    n "Just because I complain doesn't mean those are my only feelings. You already know that."
    n "It wasn't a serious complaint anyway."
    show natsuki 1ba
    "Natsuki goes back to a small smile, which I'll take."
    n "It's pretty cold, though."
    "Natsuki puts both of her arms around me instead of only one."
    mc "Yeah, sorry about that. I should've brought a blanket or picked an earlier time."
    n 1bb "Guess there's not much we can do about it now."
    n 1bt "Guess you'll have to warm me up as punishment."
    mc "I'm cold too, Natsuki. You're not going to get much warmer with what you're doing."
    mc "You're just looking for excuses to hug me."
    n 1bq "N-No I'm not!"
    "I grin."
    mc "Whatever you say, Natsuki."
    "We stay like this for a couple minutes until I bring up something I remembered."
    mc "Hey, Natsuki."
    n 1bb "What is it? I'm trying to concentrate on warming up."
    show natsuki 1ba at f11
    mc "Yeah, sure. Anyway, those chocolates you baked were pretty good."
    mc "It got me thinking, though."
    mc "Remember that time when we first went grocery shopping?"
    n 1bb "It's been a long time since then, [player]. You don't have to think about all our previous dates when I'm right here."
    mc "I know, but I was thinking about {i}why{/i} we went shopping."
    n "For food, probably. I think that's why people go to grocery stores."
    mc "I believe we bought cupcake supplies, though."
    mc "When I asked you what or who they were for, you said I'd find out soon enough."
    mc "But I don't think I ever found out what they were for."
    n 1bq "Oh, that."
    "Natsuki sounds embarrassed."
    n "Didn't you already figure it out?"
    n "I thought it was obvious."
    n 1be "Are you trying to get me to call you an idiot on purpose or something?"
    n "You already know I usually don't mean it. I don't get what's so attractive about saying it."
    "Wait, usually?"
    mc "I genuinely don't know. I don't like jumping to conclusions like that."
    n "You're going to make me say it, aren't you?"
    n 1bq "If it makes you happy, I was going to make them for you, idiot."
    mc "Ahh."
    "Okay, in hindsight I should've figured that out a long time ago."
    mc "How come I never got them, then?"
    n 1bc "You already forgot? The whole \'terrible home life kinda ruins your desire to do anything for anyone\' thing?"
    "Gah, I'm dumb."
    mc "Oh! I'm so sorry, I didn't mean to bring that up."
    n 1bb "Yeah, yeah, I'm used to it at this point."
    n "I used to say that you said weird stuff sometimes, but I'm starting to think you're weird in general."
    mc "What's that supposed to mean?"
    n "As I've said before, it's not a bad thing."
    show natsuki 1ba at t11
    "Natsuki quits hugging me and looks at the lake again."
    n 1ba "At least your taste in date locations is okay."
    mc "Well, I've been able to get some practice, after all."
    "..."
    n "[player]."
    mc "Yeah?"
    n 1bb "I wonder what life would've been like if I had never met you."
    n "Actually, I don't want to think about what life would've been like if I never found you. I know it'd be bad, though."
    "Putting it into perspective, Natsuki's right."
    "If she never met me, she wouldn't have had any place to stay after her dad hit her, and I don't want to think about what life after that would've been like, either."
    "Would she have had the courage to ask any of the other club members for a place to stay?"
    "I don't think it matters now, anyway."
    mc "I'm so glad I'm dating you."
    mc "Would it be annoying if I said that for the thousandth time? Maybe it would be, but it wouldn't change anything."
    n "I still don't get why you're dating me."
    n "But I can't deny that I've had a good time dating you, too."
    n 1bq "A great time, even. Whatever makes you feel better or something."
    mc "I think it's kinda cute how you add \"or something\" or \"I guess\" whenever you're saying something nice to me."
    n 1bb "Well, you know what?"
    n 1bi  "..."
    "Even Natsuki doesn't have any comebacks for that."
    menu:
        "It wouldn't hurt to start another conversation to break the silence, would it?"
        "Ask about her favorite date.":
            $ askAboutDate = True
            mc "By the way, Natsuki, what's your favorite date we've had?"
            n 1bb "Huh? I never really thought about that, honestly."
            n "They're all pretty okay."
            mc "Yeah, I've enjoyed all of them too."
            mc "Kinda makes me wonder what would be the \'perfect date,\' though."
            n "I might have something in mind for that."
            mc "Wait, really?"
            n "Later, maybe. Something I've kind of wanted to do for awhile, but we'll see."
            "What's that supposed to mean? Oh well."
        "Ask how she's doing.":
            mc "How are you doing, Natsuki? Like, in general?"
            mc "As your boyfriend, I need to make sure that you're okay and all that."
            n 1bb "I'm fine, I guess."
            n "I've been stressed sometimes for obvious reasons, but it isn't so bad when you're there."
            mc "Glad I could help. I'd do anything to make you feel better."
            n "Thanks, [player]. I'm glad we're dating."
            n 1bq "I've... liked you from the start, as weird as that is for me to admit."
            n "I know I've said that before, but it didn't really sink in until now."
        "Don't say anything.":
            "On second thought, I don't need to say anything, because the mood speaks for itself."
            "Natsuki and I will keep sitting together like this, because we don't need words to convey how we feel about each other."
    hide natsuki
    stop music fadeout 2.0
    scene bg park_night with wipeleft_scene
    "And so, the night continues like this until I check my phone and realize how late it's gotten."
    mc "I hate to say this, but we should get back home now."
    play music NextToYou fadein 2.0
    "Natsuki stares into my eyes."
    show natsuki 4bs at t11
    n "Do we have to?"
    "I stare back."
    mc "We can stay for a little longer, I guess."
    "Okay, this is getting really romantic. We're not going to be interrupted, are we? Please don't tell me we're about to be interrupted."
    "You know what? Screw even bringing that up. I'm going to enjoy the moment and nobody's going to stop me."
    "..."
    "OH! Right, Natsuki's still here."
    n 4bq "Good."
    mc "I can always make time for us to be together, you know."
    n "Yeah, that makes me happy."
    show natsuki 1bh at face_one(y=200) with dissolve_cg 
    "Our faces lean in closer."
    mc "I love you so much, Natsuki."
    show natsuki 1bh at face_two(y=335) with dissolve_cg 
    
    n "So do I, [player]."
    "She starts leaning in. Our faces are so close..."
    "C-Could this be...?" 
    "She suddenly stops leaning in." 
    
    if askAboutDate is True:
        n "Hey, about earlier when I said there's something I've been wanting to do... there's something I need to ask."
        n "Have you ever been kissed before?"
    else:
        n "How many times have you been kissed, by the way?"
    mc "At the moment, not even once." 
    mc "You?"
    n "It's the same here."
    
    "Our faces are even closer now."
    "Natsuki blushes."
    n "Would you like to change that?"
    mc "I don't see why not."
    show black with close_eyes
    "Eventually our faces can't get any closer. Suddenly, we're kissing. Nobody to interrupt us, nothing to bring us down."
    "And man, does it feel good."
    "I keep thinking the moment's going to be ruined by something, but it never does. All that happens is pure bliss."
    "Once we're done, we both have a look of shock on our face."
    scene bg park_night 
    show natsuki 1bn at face_three(y=600) with open_eyes
    n "Did we actually...?"
    mc "I think so."
    n "Okay, I'm just checking."
    n "We should do this more often."
    n 1bs "I liked it."
    "Natsuki seems like she's trying to stop blushing but can't do it."
    mc "I agree."
    "I'll admit, I had a bit of trouble figuring out what to say, but whatever."
    "My first kiss was great, though. I think this was a good day overall."
    
    stop music fadeout 2.0
    hide natsuki with dissolve_cg
    window hide
    show black with Dissolve(2.0)
    window show
    
    "More time passed. Much, much more time."
    n "Wake up! You know what day it is, don't you?"
    scene bg bedroom with open_eyes
    play music aNewDay fadein 2.0
    "I struggle to sit up, still not fully awake."
    mc "I think?"
    show natsuki 5c at f11
    n "So you have no idea, then."
    mc "I didn't say that!"
    mc "It is true, though, I will give you that."
    n 4b "I'm not surprised you'd forget seeing as you were never good at remembering, but lucky for you, I am."
    mc "I still don't know what today is."
    n "It's been half a year since we first started dating, duh!"
    "I raise an eyebrow."
    mc "Already?"
    n 1b "Yup! Doesn't feel like it's been this long, though."
    mc "Same here."
    mc "..."
    mc "So, like, it's actually been six months, right?"
    n 2c "Yeah."
    n 5b "I know you're probably shocked that you had a girlfriend for more than a week, but you know I'd never leave you."
    mc "I'm guessing we should celebrate later tonight, then?"
    n "You're getting better at this."
    n "Took you long enough."
    mc "I try."
    n "You do?"
    mc "Very funny, Natsuki. I'll think of the details later, but I'm tired."
    n 1a "You're always tired. We have to get to school anyway."
    mc "Yeah, yeah."
    hide natsuki with dissolve_cg
    scene bg club_day with wipeleft_scene
    show natsuki 1a at f11
    "It'd be redundant if I said school was boring as usual, so I won't. We did, of course, go to the Literature Club, though."
    show natsuki 1a at t21
    show sayori 4r at f22
    "As we walk in while holding hands, Sayori greets us."
    s "You two look happy today!"
    show natsuki 1a at t31
    show sayori 4a at t32
    show monika 1b at f33
    m "They always look happy, Sayori."
    m 5a "Not saying that's a bad thing~"
    mc "Well, it's been half a year since we started dating, so..."
    show natsuki 1a at t41
    show sayori 4a at t42
    show monika 1a at t43
    show yuri 4b at f44
    "Yuri peeks up from the book she's reading."
    y "Congratulations."
    mc "Ah, it's no big deal."
    hide yuri with wipeleft
    show natsuki 4e at f31
    show sayori 4a at t32
    show monika 1a at t33
    "Natsuki looks disappointed in me."
    n "I think it's a big deal."
    n 3t  "The fact that [player] had a girlfriend for longer than a week is impressive!"
    mc "Yes, Natsuki, you made that joke at home, too."
    n 3c "That was a joke?"
    "Dang it, Natsuki."
    show natsuki 3a at t31
    show sayori 4c at f32
    show monika 1a at t33
    s "Anyway, I think that's pretty cool. Congrats to both of you!"
    show natsuki 3a at t31
    show sayori 4c at t32
    show monika 4b at f33
    m "I remember when you two first met."
    m "I saw this coming, to be honest."
    mc "Did you, Monika? I didn't think it was obvious we had feelings for each other at the time."
    show natsuki 3a at t31
    show sayori 4x at f32
    show monika 4b at t33
    s "It was obvious."
    "Huh."
    mc "Anyway, we're going to read some manga now."
    show natsuki 3a at t31
    show sayori 4x at t32
    show monika 5a at f33
    m "I see. Have fun!"
    hide sayori with dissolve_cg
    hide monika with dissolve_cg
    hide natsuki with dissolve_cg
    stop music fadeout 2.0
    window hide
    
    scene bg residential_day with wipeleft_scene
    window show
    
    show natsuki 1a at f11
    
    "Once all was said and done, Natsuki and I head back home. On our way back by my house, I see the silhouette of a tall figure dart across the bushes."
    show natsuki 4u at f11
    "At least, it tries to dart across the bushes. Once it realizes our eyes are on it, it stops."
    "It walks a little bit forward, enough for us to see who it is: Natsuki's dad."
    "I've seen him multiple times before while I was with Natsuki, and he never interacted with us much."
    "She would glare at him, and that seemed to get her thoughts across just fine."
    "This time, though, I noticed something about his hand. He was clenching his fist, which wasn't a fantastic sign."
    "It was quite a terrible sign, actually, but I feel that speaks for itself and I'm kinda panicking at this point."
    menu:
        "So, is he gonna punch me? Am I about to be killed or something?"
        "Confront him!":
            $ confrontDad = True
            "I can't run away from this forever."
            mc "Hey, you! What you are doing?"
            "It didn't matter, though, because he runs away anyway."
            n 1b "You're not going to go after him, are you?"
            mc "I don't think there's any point in chasing him. It's clear he doesn't want to talk."
            "Which is nice, since it benefits my health in the sense that I don't get killed."
            n 1u "Yeah."
            scene bg house_entrance with wipeleft_scene
            pause(1.5)
            scene bg home_interior with wipeleft_scene
            "Well, may as well head home. I walk through the front door and take a deep breath as I sit on the living room couch."
        "Run away!":
            scene bg house_entrance with wipeleft_scene
            pause(1.5)
            scene bg home_interior with wipeleft_scene
            "Luckily I'll be able to live a little longer, as I hastily rush into my home with Natsuki, as I slam the front door behind me."
    mc "Did your dad seem a bit, uh..."
    n 1b "Angry?"
    mc "That's a word for it, yeah."
    mc "I'm not really sure what to do about this."
    n 3b "I doubt he's actually going to murder you or anything, [player]."
    mc "I know, but..."
    n 4b "But nothing."
    "Well, this situation is a bit tense right now."
    n 1c "Besides, it's a special day."
    n "Shouldn't you take me out on a date, since that's the point of dating and all?"
    mc "Of course."
    mc "Should we get something to eat?"
    n 1b "If it's at a place that doesn't rip you off like that one time."
    mc "Fast food it is."
    
    play music NatTheme fadein 2.0
    "For most people, going to a fast food restaurant wouldn't be romantic."
    "Sorry, scratch that. For basically {i}anyone{/i}, going to a fast food restaurant wouldn't be romantic. Luckily, Natsuki wasn't just anyone."
    hide natsuki with wipeleft
    
    
    scene bg fastfood with wipeleft_scene
    mc "Well, we're here."
    "We walk into the restaurant."
    "There's a certain modern atmosphere to it, although it doesn't necessarily mask the fact that this is a fast food place, and the fact that we're going on a date at a fast food place."
    show natsuki 1a at s11
    "Once we order our food, we sit down next to each other at an empty table."
    mc "I know this place is a bit weird for a date, but we've gone here before, haven't we?"
    n 1b "Yeah. I don't think you have to be worried, [player]. I'd rather be somewhere comfortable than somewhere super romantic, and this place is comfortable for me, so..."
    "We eventually receive our food. As Natsuki unwraps her hamburger, I notice that she seems unsure about something."
    mc "Is everything alright?"
    n 1s "There's something I've been wanting to try."
    mc "Hmm?"
    "I start to drink some water."
    stop music
    play music EarlyBird
    n "Um..."
    menu:
        n "W-Would you feed me?"
        "Spit out the water you're drinking":
            mc "W-What? Natsu--"
        "Spit out the water you're drinking":
            mc "W-What? Natsu--"
        "Spit out the water you're drinking":
            mc "W-What? Natsu--"
    n 4q "I'm just curious, okay!"
    n "I've seen so many other couples do it, and..."
    mc "Let me get this straight. You want me to feed you?"
    n 5e "Don't make me say it again!"
    "I'd be lying if I said I wasn't the least bit curious about what it was like, too."
    mc "Sure, I guess."
    hide natsuki with wipeleft
    "I get up and walk over to the utensils center to grab a fork, and then sit back down in my chair."
    show natsuki 5s at d11
    mc "So, Natsuki, we're really doing this?"
    n 5s "Like I said, it's one of those things you have to do at least once."
    "According to who?"
    mc "Alright, so then I take the fork and stick it in the burger, right?"
    n 4b  "I guess? Wait, you eat burgers with a fork?"
    mc "It's a lifestyle, Natsuki."
    mc "Anyway, next you open your mouth."
    n 4w "Actually, I changed my mind."
    mc "What?!"
    n 4q "This is too embarrassing."
    mc "Natsuki, we are in a fast food restaurant. Not a single person is going to judge."
    mc "Sure, feeding someone a hamburger isn't how it's usually done if you want to be romantic. Actually, nobody does that."
    mc "Now that I think about it, it wouldn't be weird for someone to judge us."
    mc "Still! I had to get up and grab a fork.."
    mc "You don't want to waste the ten seconds I spent to get us a fork, do you?"
    "I think what I'm saying is very convincing, personally."
    n "Fine!"
    show natsuki 1w at f11
    "Natsuki opens her mouth as I put the fork into it. She bites down and quickly chews, filled with embarrassment."
    show natsuki 1s at t11
    mc "Well?"
    "She swallows, and tries to think of something to respond with."
    n 1q "...That was a thing."
    n "Yep, that was definitely a thing."
    mc "I'm glad we can both agree on that."
    n 4b "Can we also agree to never do that again? At least not in a fast food restaurant?"
    mc "Sure, because I wasn't going to do it again anyway."
    n 4q "N-Not for now, at least."
    mc "Yeah."
    "That was weird."
    hide natsuki with wipeleft
    window hide
    stop music fadeout 2.0
    
    
    window show
    "...And so, we finish up our food and leave the restaurant."
    scene bg residential_night with wipeleft
    pause(1.5)
    scene bg home_interior_night with wipeleft
    "Once we head home, things go back to normal. Not \'things {i}seemed{/i} like they went back to normal,\' I mean that we didn't even think about Natsuki's dad once."
    "Or rather, we thought about it but didn't want to admit it had been on our minds."
    "The rest of the night goes well enough. There was no other drama, at least. Tomorrow, though? I doubt it'll be as peaceful as I'm hoping for."
    "I don't know why, but it feels like something's about to happen."
    window hide
    
    
    
    show black with Dissolve(2.0)
    window show
    scene bg flashback_home with Dissolve(2.0)
    $ o_name = "???"
    n "I'm tired of this."
    o "Not now, Natsuki."
    n "Not now? If not now, then when?"
    n "How much longer is this going to be put off?"
    o "I'm serious. We will discuss this later."
    n "Like I said, you keep saying \"we'll talk about it later\" but nothing ever actually happens!"
    n "I don't want to keep living like this, and I don't think you do either."
    o "Go to your room, Natsuki. We will discuss this later, and that is final!"
    n "No! We have to do something!"
    n "Part of the reason I'm doing this is because I still care about you."
    n "You don't know what I'd give for things to go back to the way they used to be."
    o "But it's not that easy!"
    o "None of this is."
    o "Do you not understand, Natsuki?"
    n "I understand, but it doesn't change anything."
    o "I asked you to leave."
    o "How many times do I have to say it?"
    o "Leave."
    n "I won't."
    o "Leave."
    n "We have to settle this."
    o "Leave."
    n "Never."
    o "LEAVE!"
    n "{i}NO!{/i}"
    n "{i}Not until you at least try to change!{/i}"
    n "{i}Not until we live a better life!{/i}"
    o "You..."
    o "Will you never get it?!"
    n "No. You're the one who doesn't get it."
    n "You've never got it."
    o "{i}ENOUGH!{/i}"
    o "{i}NATSUKIIII!{/i}"
    "..."
    "..."
    "..."
    "..."
    "..."
    o "Oh, my dear Itsuko..."
    o "You have no idea how much I wish you were still with us..."
    window hide
    show black with Dissolve(2.0)
    window show
    
    scene bg house_entrance_night 
    o "I just don't know what to do."
    play music Dusk fadein 2.0
    "I freeze in place."
    "It's {i}him.{/i}"
    "It was the night after mine and Natsuki's anniversary. She had gone to bed and I was about to join her, when I heard a knock on the door."
    "So, I went to open it up, and there he was. I was face to face with Natsuki's dad, and by myself this time."
    "As I was saying, back to where I left off."
    $ d_name = "Nat's Dad"
    d "I just don't know what to do."
    mc "Uhh, hi. Um..."
    "What do I even do here?"
    scene bg home_interior_night with wipeleft_scene
    mc "You see, well, uh..."
    "He plops onto the couch in the living room."
    d "I hope you don't mind."
    "Well, it's not like I can do anything about it anyway."
    mc "What are you here for? Y-You looked kinda upset yesterday."
    if confrontDad is True:
        d "Hmm? Oh, that. Sorry about running away when you tried speaking to me, but I didn't feel like discussing anything at the time. I was upset, after all."
        d "What happened yesterday is unrelated to what I need to ask you, though."
    else:
        d "Hmm? I was upset, yes, but that's unrelated to what I need to ask you."
    d "From my understanding, Natsuki has been living with you, correct?"
    mc "Y-Yes."
    d "For half a year, then."
    "A pained expression rests on his face."
    d "I'm not here to criticize you, or tell you how to live your life."
    d "It seems I've lost the right to even give advice for my own daughter's life."
    d "I wanted to see things for myself, though."
    "I hear the door to my room open."
    n "[player]? Who's there? I think I recognize that voice."
    mc "It's nobody, Natsuki!"
    "That was the worst lie I could've come up with. The absolute worst lie possible. It's clear I wasn't at the top of my game right now."
    d "I'm talking to your boyfriend."
    
    "As soon as Natsuki hears that, she slams the door shut. That's one problem solved, I guess?"
    "Ha, what am I saying? I'm panicking to no end, and that was probably the worst solution in history. We're actually going to talk about this right here?"
    mc "Aren't there better places to talk about this?"
    d "It's not going to change anything at this point."
    "I sigh, and ask another question."
    mc "You've seen Natsuki and I go on dates multiple times. How come you never did anything other than ask me a question once?"
    "He looks off to the side."
    d "I guess I accepted it early on."
    d "My daughter didn't want to live with me anymore. She cut ties."
    d "It pains me to realize that, but what was I supposed to do?"
    d "You and I both know she wouldn't have come back to me."
    d "Certainly not if I approached you two in the middle of something."
    d "I was stuck. Done. She's gone."
    "I feel slightly more comfortable about speaking to him at this point, partially because he wasn't going to murder me."
    "Not totally comfortable, but that made it a little better."
    mc "That sums it up, yeah."
    d "What a shame."
    "Unlike what I expected, he doesn't have a hint of anger in his voice. Only regret."
    mc "You seem rather calm about all this."
    stop music fadeout 2.0
    play music Dawn fadein 2.0
    d "Of course. Like I said, I accepted it."
    d "There's nobody to be angry at except myself."
    d "I know this is my fault."
    d "I know I've made the biggest mistake of my life."
    d "I already hated myself before all this happened."
    d "But ever since Natsuki left, I've been worse."
    d "I loathed myself more each day."
    d "Wondering how I could've lost my temper like that."
    d "Wondering how I could've broken a promise I made to my own wife."
    "He pauses."
    d "But I doubt you want to hear about that."
    d "And I understand."
    d "I know you must think I'm a terrible excuse for a parent."
    d "I'm not trying to gain any sympathy from you."
    "Good, because I wasn't going to give him any."
    "But at last, I finally feel brave enough to talk a bit more."
    mc "Acknowledging your awful actions doesn't excuse them from being awful."
    "I thought I had gone too far with that, but Natsuki's dad takes a deep breath and speaks again, as surprisingly calm as ever."
    d "I'm aware."
    d "There's no redeeming myself for what I did."
    d "Believe me, I'm not trying to deny that."
    d "I'm just trying to think about what to do next."
    "He pauses again, this time for even longer."
    d "Natsuki probably told you about me distancing myself from everyone, didn't she?"
    mc "She did."
    d "Yes, after I lost my wife..."
    "I notice a tear roll down his cheek. He stops yet again."
    d "I'm sorry. Just... after I lost my wife, I became a recluse."
    d "I tried to provide for Natsuki, but I didn't provide nearly enough. Even with our financial situation, there is still so much more I could've done."
    d "I could've cared for her so much more."
    d "There's a reason she's so skinny, you know."
    d "I digress. My point is, nobody should have to be raised by a parent like myself."
    d "Nobody should have to be raised by someone who won't give full attention to their kid."
    "Another tear rolls down his cheek. Then another, and another. They don't stop coming."
    d "It's such a horrible situation. Now I've lost everything."
    d "After Natsuki was born, if I told my past self that I would eventually... do {i}that{/i} to her, I don't think I would've been able to take it."
    d "But that's selfish too, isn't it? I wanted to be there for my daughter, no matter what."
    d "But I couldn't do it. There's no excuse."
    "He's sobbing at this point, his face buried in his hands."
    mc "Wow, I..."
    d "I'm sorry for dragging you into this. It's utterly unacceptable for me to barge into your house like this."
    d "Like many things, I wish I could take it back, but I needed someone to vent to."
    "We sit there, unsure what to say next. After several moments of silence, he speaks up again."
    d "I lived for Natsuki, you know."
    d "Even after my wife was gone, things kept getting worse. I lost my job at some point... I don't think I ever told Natsuki that, but I wouldn't be shocked if she figured it out."
    d "I barely managed to get any money period, but that's another story."
    d "Natsuki was all I had left."
    d "Living the way I did was torture. It absolutely does not excuse my behavior, but simply getting out of bed was a seemingly impossible challenge sometimes."
    d "The main reason I was so strict towards her was because I didn't want her to experience the life I was living. Even my strictness was misguided, though."
    d "I've said it more than enough times, but my life was terrible. But..."
    d "At least I still had my daughter."
    d "We argued a lot, though."
    d "A lot of times it was about my failure as a parent."
    d "I took things too personally. I shouldn't have taken anything personally in the first place."
    d "She was my daughter, and she was right."
    d "One time I was disappointed in myself. Frustrated, upset, defeated, and ultimately, regretful."
    d "I should've left the room right there. But I kept talking. I kept deflecting."
    
    d "Looking back, everything I said during that conversation is a joke."
    d "I kept going. I wasn't even mad at her, I was mad at myself and didn't want to admit it."
    d "Living itself was painful. I couldn't take it anymore, so I did something I agreed I would never do at any point in my life as a parent."
    d "I hit her."
    d "And it was then I lost her, too."
    d "I was left with truly nothing."
    "He takes some more time to collect his thoughts."
    d "I don't go outside much. But during the times I did, I would often spot you and her together."
    d "I'm not mad at you, to clarify. She deserves someone better than me anyway."
    d "As I was saying, I kept watching you two. Thinking about what could've been. Thinking about how I could've prevented this."
    d "For much of my life, I blamed everyone else, yet I wouldn't blame the person that was actually responsible for any of this."
    d "I didn't blame myself. Not until it was too late."
    "I want to think more about this. I want to react somehow. But thoughts are going through my mind so fast that I'm having to push them away entirely, and all I can do for now is listen."
    d "I think it's meant to be this way, though."
    d "I'm frankly {i}glad{/i} it's this way."
    d "As I said, Natsuki doesn't deserve me."
    d "She doesn't deserve to live the way she did in my house."
    d "I still know nothing about you."
    d "I don't even know your name."
    d "But whenever you and Natsuki were together, she looked so happy, and that's all I ever wanted."
    "I keep searching for words yet can't find them."
    d "Again, I'm sorry to put you through this."
    d "This is my responsibility and mine alone."
    "Finally, I bring myself to say something."
    mc "What do you plan on doing, then?"
    d "That's a good question."
    d "I don't want to take my own life at this point."
    d "Not because I feel my actions are justified--they're absolutely not--but because I feel so defeated that I can't even bring myself to do that."
    d "That only leaves one option left."
    "I... think I know what he's getting at."
    d "As you might be able to guess, I plan to turn myself in to the police."
    d "Not that it matters. I'm about to get out of your life as quickly as I entered it."
    stop music fadeout 2.0
    play music Thoughts fadein 2.0
    "Turn himself in to the police? Is this really where it ends?"
    "I need to think hard about this one. Obviously, he is a terrible parent and not exactly a great person either."
    "But I do wonder if he was always like this. If things went downhill after his wife passed, what about before that?"
    "Although Natsuki was probably too young at the time before that all happened to describe what her dad was like then."
    "Is it worth it to try to bring him back to what he used to possibly be? Natsuki did say she still cares for him."
    "Actually, has he tried family counseling? I don't think he ever brought it up, and Natsuki never mentioned it, either."
    "I'll always be there, so I guess it's not like they'd be alone. Natsuki doesn't have to stop living with me unless she wants to."
    "At the very least, I don't think the violence incident will happen again."
    "Natsuki's dad is so much different than I expected him to be."
    "His calm demeanor is the opposite of how I thought he'd behave, and that obviously doesn't clear him of what he did, but I find it interesting."
    "I've never seen someone as lost in life as he is."
    "Which is more worth it? Trying to work towards a better life or blissfully living in the one we already have?"
    mc "I'll admit that I'm not even close to being an expert on this."
    mc "However, I want the happiest ending we can get to this situation."
    mc "Maybe it won't actually be that happy, but I want to make the decision that I think will lead us to the brightest future."
    mc "I'll give my advice on what I think is the solution that will be best for all of us in the end."
    menu:
        mc "You should..."
        "Try reaching out one last time.":
            call natsukiRoute_GoodEnd
        "Turn yourself in.":
            call natsukiRoute_BadEnd
    return

label natsukiRoute_GoodEnd:
    $ natsukiGoodEnd = True
    "Natsuki's dad has made mistakes. Awful, irredeemable mistakes. But both Natsuki and her dad care for each other."
    "I don't want this to end with her dad turning himself in. I think we can do better than that."
    "I still believe it's possible to recover. I still believe that giving him a second chance could work. And if it doesn't, oh well. At least we can say that we tried."
    "Natsuki's dad is a broken man. A man shattered into thousands of pieces. But something that is broken can also be repaired."
    "I don't want this to end with her dad giving up. I think we can do better than that."
    "I still believe it's possible to turn this around. I still believe it's not all over. And if things don't work out, oh well. Sometimes that just happens."
    "Natsuki's dad will never be able to fix everything that he did wrong. But we don't need to fix everything, we need to fix {i}enough{/i}, and that much is possible."
    "I don't want this to end knowing that this could've been so much more. I think we can do better than that."
    "I still believe we haven't lost everything. I still believe we have the chance to gain. And if we don't gain anything, oh well. We aren't going to lose anything either."
    "I can work with Natsuki and her dad, and they can work with a therapist. We can all work together to get their lives back."
    "I'm a regular person."
    "I can't force anything to happen. I can't force things to get better. I can't have all the answers."
    "But if there's one thing I am sure of, it's that we can make this work. And if we don't at least try... I think that'd be a real shame."
    stop music fadeout 2.0
    play music AfterAll fadein 2.0
    mc "You need to try to reconnect with Natsuki."
    "Natsuki's dad looks shocked. I'd be surprised if I were in that situation, too."
    d "Why? There's no way she'd let me back into her life."
    mc "I don't know. She might be scared of you, and the idea of changing how she lives right now might terrify her more."
    mc "But deep down, I think she still cares about you."
    mc "She even told me as much."
    d "What if she didn't really mean it? She does that often."
    mc "I don't think so. I think she was serious."
    mc "I've been dating her for half a year now. I can tell when she's not being genuine."
    mc "When I talked to her about you, though, she said that she still cared about you, but she didn't want to change her current lifestyle."
    mc "That seems like an odd time to lie."
    mc "I think she would've said something like \'It doesn't matter if I care about him,\' or \'I'm fine the way I am now\' if she didn't want to be fully honest, or something like that."
    mc "It'd be strange for her to go out of her way to lie in the first place."
    mc "My point is, I think we should at least try. We can get you and Natsuki a counselor, and I'd be there the whole way to help out when needed."
    mc "If you really want to, you can try to turn yourself in at another point. But for now, will you at least try to connect again with Natsuki with my help?"
    "He thinks for awhile. This talk has been lasting so long I wouldn't be surprised if it were midnight at this point."
    "Then, he raises his head and gives his answer. Everything we've talked about, all the anxiety, fear, and sadness we've gone through... all of it was leading up to this."
    d "Sure."
    d "I've got nothing to lose at this point anyway."
    
    d "Let's try, then. I want both me and my daughter to be able to get our lives back."
    mc "Alright, I'll try setting up an appointment with a counselor for you two--after I check with Natsuki, of course."
    d "Can you even do that?"
    "In hindsight, it's probably not that simple to register someone into counseling like that..."
    mc "I can get started on it."
    d "If you say so."
    d "Should I come back tomorrow so we can talk again?"
    mc "That sounds like a good idea, yeah."
    
    play sound closet_open
    play sound closet_close
    "Natsuki's dad walks over to the front door, walks out, and slowly shuts it. I think I caught a smile on his face as he was going out, but I couldn't tell for sure."
    play sound closet_open
    "Suddenly, I hear the door to my room creak."
    mc "He's gone, Natsuki."
    show natsuki 4bu at t11
    "She walks out into the living room and takes a deep breath."
    n "Okay."
    mc "I have a question for you, Natsuki."
    mc "Would you be interested in going to family counseling?"
    "I expected her to take awhile to think about it, but she responds immediately."
    show natsuki 4bu at f11
    n "Yes."
    mc "Really? You seemed against the idea of change before."
    n 5bc "So, I may or may not have just heard the whole conversation you had with my dad."
    n "You'd be a good car salesman, honestly."
    mc "Oh."
    "It is true I never decided on a dream jo--err, anyway."
    mc "You're up for it, then?"
    n 42ba "I can't keep running forever."
    n "I've been thinking about it for a long time, honestly."
    n "I did say I still cared for him."
    mc "To clarify, you're absolutely sure you want to do this? Like, it'd be okay if I tried setting up an appointment?"
    n "You're still going to be there to help, right?"
    mc "You're my girlfriend, so of course I'm going to do all I can."
    n "Good."
    n 12ba "...I'm being casual about this and all but I'm still scared, you know."
    n "It's thanks to you I can take this step forward."
    n "I'm doing this only because I trust you this much, and because you haven't broken that."
    n "So, thanks."
    show natsuki 1ba at face_three(y=600)
    "Natsuki gives me a peck on the cheek and heads back to my room. I should probably get to bed soon, too."
    hide natsuki with wipeleft
    "It's amazing how much Natsuki has grown. I don't think she'd have agreed this easily if I offered the choice half a year ago."
    "What a ride this has been. To think that we're finally going to get some closure on this feels unbelievably satisfying."
    "Now, it's only a matter of how tomorrow goes."
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    scene bg kitchen with wipeleft_scene
    play music AfterAll fadein 2.0
    window show
    
    "Here it is."
    "The day where we experience the moment of truth."
    "As I eat breakfast, I hear a knock on the front door. Natsuki's dad isn't here already, is he?"
    mc "I'll get it."
    scene bg house_entrance with wipeleft_scene
    play sound closet_open
    "I open up the front door and, as it turns out, it was him after all, filled with exhaustion."
    d "Sorry for coming so early, but I had trouble sleeping."
    mc "That's fine."
    scene bg home_interior with wipeleft_scene
    "I motion for him to sit on the couch. I look over and see Natsuki turn her head away at the breakfast table."
    "Which is fine; she doesn't need to talk right now, and I don't want to make her uncomfortable."
    play sound closet_close
    mc "So, I talked to Natsuki an--"
    d "I'm turning myself in."
    stop music
    play music Dusk
    "...That's not where I thought this conversation was supposed to go."
    mc "Wait, why?"
    d "I'm filled with too much guilt. Nothing can change that."
    mc "But we're so close to patching things up! Don't you want to connect with your daughter again?"
    d "I do, but I've messed up too many times now. I made a decision, and I'm turning myself in."
    d "I'm sorry to say that your attempts at convincing me otherwise likely won't affect me."
    "No! It wasn't supposed to be like this!"
    mc "Come on! At least give this a chance!"
    d "Sorry, but I've made up my mind."
    mc "Are you sure you want to throw all this away? You're so, so close to making this right."
    d "As I said, that changes nothing."
    "Why does it have to be like this? I don't think things will ever be the same if he quits now, but there's nothing I can do, either!"
    show natsuki 4be at t41
    n "If what [player] says won't change your mind, maybe what I say will."
    mc "Natsuki?!"
    show natsuki 4bc at t42
    pause(1.0)
    show natsuki 4bc at s42
    "Natsuki gets up and sits down next to her dad. Is she really about to say what I think she's going to?"
    n 1bg "This is hard for me to do, after everything you did to me."
    n "After you neglected me for so long."
    n 12be "After you hit me."
    n "After... actually, we'd be here awhile if I gave a full list, so I'll get to the point."
    n "You're a terrible parent. Sorry if that hurts your feelings, but it's kinda true."
    n 12bb "But you're still my dad, you know?"
    n "We still made some good memories over the years."
    n "Maybe not as many as most families, but those memories are important to me."
    n "I think it'll be a long time before I can trust you again, but I want to at least try."
    n "I'm not entirely sure why. Maybe [player] has rubbed off on me more than I thought."
    d "Natsuki, you've... You've changed."
    d "It's hard for me to judge when it's been so long since I talked to you, but..."
    n 5bc "I guess, but that doesn't matter right now."
    n "Maybe you aren't willing to reconnect with me, but I want to reconnect with {i}you{/i}."
    n "I'd feel awful if I felt like I missed a huge opportunity."
    "Natsuki's dad is shocked. Nothing else, just shocked."
    "Natsuki turns towards me."
    n 1ba "I have someone to thank for that."
    n 1bc "Someone who actually supports me, but that's a different story."
    "Natsuki still seems annoyed, which is understandable. I'm just proud that she's doing this right now."
    n "Please don't turn yourself in. I want to at least {i}try{/i} to get things back to normal."
    n 1bu "Please..."
    "Natsuki's dad thinks it over, as we all anxiously wait for his answer."
    "Years of conflicts, years of ups and downs, years of mistakes, years of decisions, and years of emotions are all coming together."
    "All for one of the biggest decisions in their lives."
    d "..."
    d "Fair enough."
    d "We're starting family counseling, then, are we?"
    "He did it."
    "I was unsure down to the last second, but he did it."
    mc "That's the plan."
    "None of us knew what to say after that. We're all so relieved that nothing comes to mind."
    "And so begins the journey towards recovery."
    
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    play music Brick fadein 2.0
    window show
    "It's been a few months since Natsuki and her dad first started attending counseling."
    "It hasn't been totally easy, but we've been managing, especially thanks to me being there to act as a pillar for the two."
    "She doesn't fully trust him, of course, but we're slowly making progress."
    "Her dad's been a lot happier lately, too. He's started job hunting, which is already a great sign."
    "I was somewhat unsure about this being the best way for things to go, but I think it is now."
    n "Morning, [player]!"
    scene bg bedroom with open_eyes
    "Natsuki gives me a hug and leaves the room to make breakfast."
    "It's nice to see her showing her sweeter side all the time, as cute as her previous personality may have been. The word for that was tsundere, right?"
    "Doesn't matter, I like the new Natsuki better than the old one."
    "I notice that she left behind a poem right next to me. Let's see what it says..."
    
    call showpoem(poem_natGood, music=False)
    "...Good. This is what I was hoping for. I made my decision on what felt right, and I believe it led me on the correct path."
    "As I get up myself, I hear a knock at the front door and go over to open it up."
    scene bg house_entrance with wipeleft_scene
    play sound closet_open
    mc "Oh, hey!"
    d "Hello! Just came to check up on you two."
    mc "I see. We're doing great! Would you like a seat?"
    "I signal for Natsuki's dad to sit on the couch."
    play sound closet_close
    scene bg home_interior with wipeleft_scene
    d "I dislike bringing this stuff up, but you two seem pretty happy, and... Natsuki doesn't want to move in with me again. Is that correct?"
    mc "Well, she does trust me more."
    d "Yes, and I doubt it's going to reach a point where she trusts me more than she trusts you."
    "He has a good point."
    "I turn over to Natsuki, who's making a full breakfast meal."
    mc "Well, Natsuki?"
    "Natsuki responds as she cooks."
    n "I'd have to think about it. I could try, maybe."
    n "Hmph. What, you don't want me to stay here?"
    "Well, maybe she didn't have her sweet side out {i}all{/i} the time."
    mc "It doesn't have to be a permanent thing. If we get far enough into our relationship, then maybe we could... you know, and then you'd be able to move back here."
    n "That's not a bad idea."
    n "You'd better not keep me waiting!"
    "And from that point forward, Natsuki tried visiting her dad more often."
    "She hadn't slept there overnight yet, but it was nice to see that she was spending more time with him."
    
    window hide
    show black with Dissolve(2.0)
    scene bg house_entrance with Dissolve(2.0)
    window show
    "More time passes. How many times have the seasons changed? I've lost count."
    mc "You sure you're ready for this, Natsuki?"
    show natsuki 1bb at f11
    n "I'm ready to stay overnight at my dad's, yeah."
    mc "Man, that means you're gonna move out eventually. I'll miss you."
    n 4bb "You already know I'm going to keep visiting you."
    mc "I know, it just still feels kind of weird."
    n 1bq "Like you said before, if we ever got married we wouldn't have to worry about that anymore, would we?"
    mc "That's true."
    n "Anyway, enough about that. I'll see you tomorrow, [player]!"
    hide natsuki with wipeleft
    scene bg home_interior with wipeleft_scene
    "And then I was alone, and would be for the rest of the night."
    "Every day since I had first met Natsuki has been an incredible journey for me."
    "I remember being worried if we both liked each other, despite that it was obvious we did. I remember being worried about how I would confess, when there was nothing to worry about in the first place."
    "Then Natsuki started living with me. That's pretty neat, if you ask me. The circumstances surrounding it were a bit weird, yeah, but it was fun. Then we started dating, and it got even better."
    "I had no idea I was capable of holding a relationship for as long as I have, let alone holding a relationship at all."
    "I certainly didn't think I'd be helping Natsuki and her dad like this, but here we are now."
    "I remember all those times I said \'things are going so great\' and \'everything is shining so bright right now\' and all that stuff, but things soon became sadder."
    "Now, though, I can say with confidence that I'm glad with how things are going. I can truly say that nothing will bring me down."
    "And I don't think anything {i}could{/i} bring me down, either. I've gone through so much, after all, that I feel like I can tackle anything."
    "I guess this is it, then. This seems like a good place to say that I'm at the end of this journey."
    "It's been a lot of fun."
    "..."
    "..."
    "..."
    scene bg home_interior_night with wipeleft_scene
    "Before I know it, it's been two hours as I sit and read some manga on the living room couch."
    scene bg house_entrance_night with wipeleft_scene
    play sound closet_open
    show natsuki 1bc at f11
    "I hear a sound at the front door, and see none other than my girlfriend."
    mc "What's up?"
    n 1bb "I got bored."
    "I kinda expected this, honestly."
    mc "Ah."
    n 1bq "So, uh, you know those cupcakes I promised you over a year ago?"
    n 1bk "I'm kinda late with this, but we have to make them someday, don't we?"
    n "So how about now?"
    mc "Sure, why not."
    mc "I love you, Natsuki."
    n 1bj "I love you too, [player]."
    
    n 1bj "Thank you for everything."
    
    
    
    $ persistent.natsukiCompletedGood = True
    window hide
    show white_end with Dissolve(5.0)
    show white with Dissolve(2.0)
    pause(5.0)
    return

label natsukiRoute_BadEnd:
    $ natsukiGoodEnd = False
    "You can apologize for your mistakes."
    "You can regret your sins."
    "You can try to make things better."
    "But that doesn't change your actions in life. Nothing will."
    "Natsuki's dad committed abuse and neglect and the fact that he feels terrible changes nothing."
    "Nor does the fact--it's not even a fact, it's a possibility--that he could potentially reconnect with Natsuki. It doesn't change anything."
    "There is no way to undo what he did. He cannot run from this forever. He committed a crime, and must deal with the consequences."
    mc "You need to turn yourself in."
    d "..."
    d "..."
    d "So be it."
    
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    scene bg home_interior_night with dissolve_cg
    play music Dusk fadein 2.0
    window show
    d "I'll turn myself in, then."
    "We were still sitting in my living room. The air is incredibly heavy, with a hint of sorrow flowing throughout."
    mc "Yeah."
    d "..."
    d "Can I ask you a favor?"
    mc "Depends what it is."
    d "It was my idea to turn myself in, but you did encourage me to do so."
    d "So, that does make you involved to some degree."
    d "But I don't want you to have to be involved with this."
    d "If Natsuki asks where I went, tell her that after I came over here to vent, I felt bad about what I did and turned myself in to the police."
    "He takes a moment to think about how to word this."
    d "Actually, scratch that. Just say you don't know where I went."
    d "She'll probably find out what happened to me on her own."
    "I feel unsure about this, but I suppose it is the best option."
    mc "I can try to do that, then."
    d "Thank you."
    "He gets up and paces towards the door. A look of sadness rests on his face."
    d "One more thing."
    d "Please take care of my daughter."
    d "I don't care what happens to me anymore."
    d "But I still care about her."
    "Before I can respond, he walks out and shuts the front door."
    "This is it, then. This is how it ends."
    "Is this the best way things could've ended? Maybe not, but it's the ending I wanted."
    "That's what counts, right? This is the ending {i}I{/i} thought was best, and that's all that matters."
    "I hear the door to my room open, and Natsuki steps out. I guess I have some explaining to do."
    
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    
    play music LettingGo fadein 2.0
    window show
    "It's been a month since that day. Natsuki eventually found out that her dad turned himself in, although I'm not sure how."
    "I'd like to say that things went back to normal, and to some level they did, but something still felt off."
    "Something felt empty. Both of us felt that way, but especially Natsuki. Sometimes she'd just stare into space; I think she felt lost."
    "She did seem slightly less stressed, but that was outweighed by her frequently seeming as if she wondered if she missed an opportunity."
    "This was the best way things could've gone, though. Natsuki's dad is gone and we'll never have to worry about him again."
    "It's over. All our problems are over."
    "At least, that's what I told myself at the start of each day..."
    scene bg bedroom with open_eyes
    show natsuki 4b at f11
    n "It's time to go to school, [player]."
    hide natsuki with dissolve_cg
    scene bg residential_day with wipeleft_scene
    pause(1.0)
    scene bg club_day with wipeleft_scene
    "I'm woken up by Natsuki. Soon afterwards, we go to school and then the Literature Club, just like we do every day. We sit and read manga, just like we do every day."
    "But at one point, things change."
    show natsuki 5u at f11
    n "[player]. Can we go into the hallway?"
    mc "Huh? Sure."
    hide natsuki with dissolve_cg
    scene bg corridor with wipeleft_scene
    show natsuki 5u at f11
    "We head into the hallway, as a deep pit is stuck in my stomach."
    mc "What is it?"
    show natsuki 12f at f11
    "I look at Natsuki, afraid. After about ten seconds, she bursts into tears."
    mc "Whoa! What's wrong?"
    "I asked her what was wrong, but I don't think any words needed to be said. I think it speaks for itself."
    n 12h "I-I feel so alone! My parents... n-now both of them..."
    mc "Hey, you've got me now."
    n "I-I love you, but it's not the same."
    "That is true. I don't think Natsuki mentioned any other family, either."
    "Maybe I really am all she has left."
    mc "It's hard to move on from something like this."
    mc "But it is possible, I can guarantee that."
    n 5e "And how would you know?!"
    "..."
    n "W-We could've fixed things! Ever since he turned himself in I haven't been as stressed, but it's caused even more problems!"
    "..."
    n 12i "I-It... didn't have to be like this..."
    "..."
    n "Why?! This isn't going back to normal, and I don't think it ever will!"
    "..."
    menu:
        n "W-Was it worth it? Was it {i}really{/i} worth it?"
        "...":
            "..."
        "...":
            "..."
    "..."
    "..."
    hide natsuki with wipeleft
    "Natsuki walks away and leaves a poem behind."
    
    call showpoem(poem_natBad, music=False)
    "This... isn't what I was hoping to read."
    "But on the other hand, nobody said this was going to be easy. I certainly didn't."
    "Life is hard, but you have to keep going. You have to keep moving. You have to keep making decisions."
    "Otherwise, can you really say you're living?"
    "I don't care if this was worth it or not anymore, because the past can't be changed."
    "I care about Natsuki and I moving forward with our life and recovering from all this."
    "It'll be long, and it'll be hard, but we can do it. I'm sure of that."
    window hide
    show black with Dissolve(2.0)
    scene bg residential_day with dissolve_cg
    
    window show
    "Another month passes. Things feel less tense than before, but still not totally normal."
    "One day after coming back from school, we sit down to have a talk."
    show natsuki 1c at f11
    n "I wonder how my dad is doing."
    n "I hope he's okay."
    "Natsuki looks down at the ground, unable to shake a feeling of uncomfortableness."
    mc "I'm sure he's continuing to serve the time he deserves."
    n "Yeah."
    n 5g "...But why did you lie?"
    "Natsuki glares at me. What is she talking about?"
    mc "What do you mean? I don't remember lying."
    n 5e "The day my dad came over to your house."
    n "Did you already forget? I came out and mentioned hearing a voice I recognized."
    "Crap."
    n "I heard every word of that conversation. Why did you not tell me that you told him to turn himself in?"
    n "Because he told you not to? Aren't my wishes the ones you should be prioritizing here?"
    mc "Natsuki, I..."
    n 4u "There's nothing you can say right now."
    n "You betrayed my trust. That's all there is to it."
    "What a disaster this has been."
    n "I'm not mad at you, if that's what you're thinking."
    n "Actually, I am mad."
    n "Not mad enough to leave you or anything."
    n "You believed you were making the right choice, weren't you?"
    n "I guess I can't give you that much crap for it."
    n "..."
    n "..."
    n "After all..."
    n 12a "If I left you, I'd really have nowhere to go this time."
    
    
    window hide
    show black with Dissolve(2.0)
    scene bg flashback_home with dissolve_cg
    
    window show
    d "Natsuki? Wait! Where are you going?!"
    n "I'm leaving, dad."
    n "I have nothing else to say to you."
    "It feels weird doing this, but I can't live here anymore. I have to get away from my current home."
    "[player]... he's my last hope."
    "I'm still unsure about going to live with him, but I'm not sure I have any other choice."
    "I want to trust [player], but it's hard. It's hard to trust anyone, even the people I love."
    "Still, he's been with me up to this point. I'll be cautious, of course, but..."
    "I don't know. There's a small part of me that thinks maybe he can make this right."
    "There's a small part of me that thinks that maybe one day things will go back to normal with my dad and I."
    "Then again, putting that much faith into another person is a dangerous thing. I've already seen where it's gotten me up to this point."
    "Please, [player]. I'm sorry for how I'm about to treat you, but it's something I have to do, just in case."
    "But please... please make my wish come true one day."
    window hide
    stop music fadeout 5.0
    show end with Dissolve(5.0)
    show black with Dissolve(2.0)
    pause(5.0)
    return