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
        s "What's going on with Natsuki, then?"
        "Try to tell the full story.":
            mc "So you know how Natsuki had been acting strange awhile back?"
            mc "Well..."
            "I try to continue, but this doesn't feel right. I'm not sure I want to get Sayori involved in something that's between Natsuki and I like this anyway."
            "Maybe I can explain it to her at a later point, but I don't know the full details of this anyway."
            mc "I don't fully know about this myself. I don't feel comfortable sharing the details, either, so let's say she needed somewhere to stay and leave it at that."
        "Be vague.":
            mc "I don't fully know about this myself. I don't feel comfortable sharing the details, either, so let's say she needed somewhere to stay and leave it at that."
    
    s "Huh. I wonder why..."
    mc "There you have it. No sneaky business or anything like that, it's me helping a friend."
    s 1r "A {i}friend{/i}?"
    mc "That's a whole different topic."
    s 1x "Mmm. Well, if you need any advice, I'm not that good at that kind of thing, but I can try to help."
    mc "Thanks, Sayori."
    hide sayori with wipeleft
    scene bg club_day with dissolve_cg
    show sayori 1a at t22
    show natsuki 1a at f21
    "We walk back into the club room, and Natsuki comes up to us."
    n 1b "[player]?"
    "I motion for Sayori to walk away."
    hide sayori with wiperight  
    show natsuki 1b at f11
    mc "I'm back now, yeah."
    n 4c "I... aghh. I hope you didn't do anything stupid."
    "It's true that she doesn't still trust me 100 percent."
    "And with her insecurities, it wouldn't surprise me if she got the wrong idea about Sayori and I, even if that wouldn't make any sense in the first place."
    mc "You're the only one I care about like this right now, Natsuki. I promise."
    m "Well, I hope you don't want to treat everyone else like dirt, at least!"
    show natsuki 4c at lhide
    hide natsuki
    show monika 1b at f22
    "I turn around and see Monika listening in."
    show monika 1a at f22
    mc "You know what I meant, Monika."
    show monika 1a at lhide
    hide monika
    show natsuki 1h at f11
    mc "But yeah, Natsuki. You're the most important person to me at the moment."
    mc "Sayori's nice, but she's only a friend when it comes down to it, you know?"
    "Natsuki looks relieved."
    n "Thank you, [player]..."
    "Man, this is complicated. That was already pretty obvious, but dang. No matter what, though, being patient and letting things happen as they do seems to work out."
    "I think."
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)

    
    scene bg flashback_home with Dissolve(2.0)
    window show
    $ o_name = "???"
    o "And just what is this you're reading?"
    n "It's mango!"
    o "Mango?"
    n "Yeah! They're like comics, but cooler."
    o "Let me see this..."
    o "So you're reading manga, hmm?"
    o "Where did you even get this? From a friend?"
    o "It doesn't matter, actually."
    o "Go do something else."
    n "But why? It makes me happy."
    o "No, it'll rot your brain!"
    o "I want you to live a fulfilling, productive life."
    o "Manga won't get you there."
    o "It can't even be considered literature, honestly..."
    window hide
    show black with Dissolve(2.0)

    
    scene bg bedroom with open_eyes 
    window show
    show natsuki 1bb at t41
    n "[player]? There's something that's been on my mind."
    "How is it that Natsuki is always awake before me, anyway? I always imagined she'd be the type to sleep in."
    mc "What is it, Natsuki?"
    show natsuki 1bu at f11
    n "I feel kinda guilty about everything that's been going on."
    n "Not that I owe you an explanation, anyway."
    "Natsuki pauses for a moment and looks into my eyes."
    play music Thoughts fadein 2.0
    n 1bh "What am I even saying? Of course I owe you an explanation."
    n "After you've let me stay here for this long..."
    n "After I kept treating you like garbage..."
    n "I wish I was stronger. Why can't I even do that?"
    show natsuki 1bs at f11
    "Tears begin to well up in Natsuki's eyes."
    mc "Calm down, Natsuki. Why don't you start from the beginning?"
    n 1bs "I can't. Not yet."
    mc "Okay. What can you tell me, then?"
    n 5be "The reason I've been so distant towards you and everyone else lately..."
    "Natsuki tries to speak but the words won't come out of her mouth."
    mc "I'll be here, Natsuki. Take as long as you need."
    n 5bc "[player], what does trust mean to you?"
    mc "Huh? That's sudden, give me a moment."
    "To me, trust means a lot of things. But if my only choice is to sum it up, then that's what I'll do."
    mc "To me, trust is the ultimate symbol of confidence. It's the basis of friendship, romance, and human interactions in general."
    mc "It's the symbol of your faith in someone. The symbol meaning that you believe they'll never hurt you."
    mc "I don't believe you can have a \'perfect\' trust in someone."
    mc "But trust doesn't have to be perfect, either. It just needs to be good enough, and then you can be satisfied."
    show natsuki 5bu at f11
    "Natsuki thinks over what I said. I probably messed up my explanation somewhere in there, but I think she got the point."
    n 5be "I was thinking of something like that too, but it's a bit different for me."
    n "I... need that perfect trust. And I don't think I'll ever show my true self unless I have perfect trust in that person."
    mc "I don't know, Natsuki. How do you get that perfect trust in the first place?"
    mc "What {i}is{/i} perfect trust?"
    n 5bb "I don't know, but I can't bring myself to agree with anything other than a perfect trust."
    mc "Is there a reason why you think that?"
    n 5bc "Maybe I'll tell you some other time."
    n "What you said about trust, I don't think it's totally wrong, though."
    n "I might have to rethink some of this after all..."
    n "If I take the first step, it might be a little easier."
    show natsuki 1bc at t44
    "Natsuki reaches for the pillows separating us and throws them off the bed."
    mc "What are you doing?"
    show natsuki 1bh at f11
    n "What's the big issue? It's not like we're doing anything dirty."
    n 5bi "Unless that's what you're insisting. If that's the case, then you can go back to sleeping on the couch."
    n "Honestly, though, that barrier was getting annoying anyway."
    n 5be "Like, you always snored into the pillows which only made your snoring even louder."
    n "It sucked."
    "There was a moment of silence as Natsuki reaches for what to say next."
    pause(1.0)
    n 1bb "But yeah."
    n "You've been so nice to me."
    n 1bq "I might not trust you, or anyone else, completely. But I trust you enough."
    n "That's what you said was important, wasn't it? Trust being good enough."
    "I wasn't really sure how to respond to this situation."
    mc "Maybe so."
    n 1bu "One day I might tell you the full story, but I hope this is enough for now."
    mc "It is, Natsuki. Thank you."
    "We spent the majority of that day lying in bed. We weren't actually doing anything, except thinking about everything leading up to this point."
    hide natsuki with dissolve_cg
    stop music fadeout 2.0
    show black with Dissolve(2.0)
    
    play music aNewDay fadein 2.0
    scene bg bedroom with open_eyes
    scene bg kitchen with Dissolve(1.5)
    scene bg class_day with Dissolve(1.5)
    scene bg club_day with Dissolve(1.5)
    show natsuki 1a at t21
    "Another breakfast, another day of school, and another day at the Literature Club."
    "Everything was normal up to the Literature Club, in fact, but it's what happened at the club that turned this into something entirely different."
    show sayori 1x at f22
    "Natsuki and I walk in, and everyone greets us as usual. We go to grab some manga, but as we do, Sayori walks up to us."
    s "You two are gonna start dating soon, right?"
    show natsuki 1p at f21
    show sayori 1q at t22
    n "Excuse me?"
    show natsuki 1p at t21
    show sayori 1r at f22
    s "Come on! It's obvious you two like each other."
    "What? I never told Sayori about that part!"
    show natsuki 1q at f21
    show sayori 1r at t22
    n "You're not entirely wrong, but..."
    show natsuki 1q at t21
    show sayori 1x at f22
    s "But what? Live a little!"
    show natsuki 1s at f21
    show sayori 1r at t22
    "Natsuki looks over at me, unsure what to do."
    "Which is awfully inconvenient, seeing as I'm unsure what to do as well."
    "I whisper to Natsuki. Sayori was probably going to listen in anyway, but there's not much I can do about that anymore."
    mc "Let's discuss this in the hallway."
    hide sayori with wipeleft
    "Natsuki nods her head. As we try going out into the hallway, we hear Monika's voice."
    show natsuki 1s at t41
    show monika 1b at f44
    m "Where are you two going?"
    show natsuki 1s at t41
    show monika 1a at t43
    show yuri 1b at f44
    y "I don't like jumping to conclusions, but from what we know about you two... hmm..."
    mc "Look, we're jus--"
    show natsuki 1q at f41
    show monika 1a at t43
    show yuri 1a at t44
    n "Stop making excuses and tell it like it is, [player]."
    n "We're going to have a private conversation. Understand?"
    hide monika with wipeleft
    hide yuri with wipeleft 
    stop music fadeout 2.0
    scene bg corridor with dissolve_cg
    play music AfterAll fadein 2.0
    "Everyone else nods their head as we make our way over to the hallway."
    show natsuki 1c at f11
    mc "...Anyway, about us dating."
    mc "I mean, I wouldn't be opposed to it, but can you really date someone you don't fully trust?"
    "Natsuki stands there for awhile."
    show natsuki 1j at f11
    "As she comes to a conclusion, she smiles and whispers back."
    n "But as long as our trust in each other is good {i}enough{/i}, then it can work. That's what you said, isn't it?"
    n 1q "Besides, I'm tired of lying to myself."
    "Well, it's now or never. I'm thinking at first that maybe this is too impulsive, but... no, I'm ready."
    mc "Okay. Natsuki, will yo--"
    stop music
    n 4e "Idiot!"
    mc "I'm not sure what you expected me to say."
    n "Not that! I'm talking about how we're still standing right outside the club room."
    mc "Ah, I see. Let's head further down the hallway, then."
    hide natsuki
    scene bg corridor with dissolve_cg
    "We move through the hallway and then stop, hoping this spot is good enough."
    play music AfterAll fadein 2.0
    show natsuki 5q at f11
    n "So? Are you going to say it or not?"
    mc "Of course."
    "...Holy crap."
    "Holy crap."
    "{i}Holy crap.{/i}"
    "It only just now sunk in what I'm doing. I mean, I knew I was doing it, but I'm {i}actually{/i} doing it."
    "I remember when I first joined the Literature Club. I liked everyone there, but Natsuki stood out to me."
    show natsuki 1q at f11
    mc "Natsuki, you're a special person to me. Seriously."
    "Natsuki is cold, yeah, but she can be sweet sometimes too. It's not as if everyone has a perfect personality anyway."
    "Plus, I think the way she acts is endearing, personally."
    mc "I've liked you from day one, and I don't know if you were in the same boat, but you still have feelings for me nonetheless."
    "Natsuki not only has similar interests as me, but she's broadened my horizons, too. And if there's anyone I want to go through something new with, it's her."
    mc "I'm not perfect, I'll admit. Not to mention this would be my first relationship, so I might not be perfect boyfriend material."
    "And we've been living together, too! How awesome is that? It's a weird set of circumstances, sure, but at least we've both got some happiness out of it."
    show natsuki 1s at f11
    mc "But that doesn't matter to me. My emotions are too strong for that to stop me."
    "It wasn't pure happiness, of course. There were some uncomfortable, sad times as well."
    "I can't even imagine how bad Natsuki must have it for her trust in me to shatter like that so hard after we built up a good friendship."
    mc "Other people might be convinced we're already dating. Which is understandable, as we do have feelings for each other."
    "What a journey this has been. When I first joined the Literature Club, I didn't think anything even close to this would be happening, but here we are."
    mc "So why not make it official? I promise to make you the happiest girl alive."
    mc "Natsuki, will you be my girlfriend?"
    "Natsuki responds immediately."
    show natsuki 4e at f11
    n "Duh, of course! Geez, you almost made that sound like a marriage proposal or something. Make your confession shorter next time."
    show natsuki 1t at f11
    n "But I'll forgive you. I've liked you since you first came to the Literature Club, after all."
    mc "Heh."
    "I said \'Heh,\' but that didn't come close to expressing the emotions I have right now. I'm so relieved, so satisfied... so happy."
    mc "Natsuki..."
    
    "We both lean in."
    show natsuki 1i at face_one(y=200) with dissolve_cg
    "Our mouths keep getting closer and closer..."
    show natsuki 1i at face_two(y=335) with dissolve_cg
    "Until..."
    show natsuki 1i at face_three(y=600) with dissolve_cg
    stop music
    play music EarlyBird
    
    s "I knew it!"
    "Oh."
    n 1p "What the heck?!"
    show natsuki 1p at t44
    show monika 5a at t41 zorder 1
    show sayori 4x at t31 zorder 2
    "We both turn around and see Sayori and Monika peeking out of the Literature Club doorway."
    hide monika with wiperight  
    hide sayori with wiperight  
    "Realizing that they've been caught, they rush back inside."
    mc "Well, we're not dying anytime soon. There'll be another chance, I'm sure."
    n 5q "Yeah."
    
    mc "I feel like leaving the Literature Club early today, honestly."
    mc "You?"
    n 5s "Yeah..."
    mc "I'll tell Monika that we need to leave the club early. I think she'll understand."
    mc "While I'm sure the club will tease us plenty tomorrow, I'm about ready to go home."
    "Man, today's been weird... but I wouldn't have it any other way."
    
    stop music fadeout 3.0
    window hide
    show black with Dissolve(2.0)
    pause(2.0)
    scene bg flashback_home with Dissolve(2.0)
    
    window show
    $ o_name = "???"
    o "Happy birthday, Natsuki."
    o "I know it's been a tough year, but here's hoping the next will be better."
    n "..."
    o "Is something wrong?"
    n "I don't want to talk about this. Not on my birthday."
    n "I think you already know what I'm talking about though, dad."
    window hide
    show black with Dissolve(2.0)
    
    
    play sound alarm 
    "{i}BEEP! BEEP!{/i}"
    scene bg bedroom with open_eyes 
    play music EarlyBird fadein 2.0
    "...That means I'm in a relationship then, right?"
    stop sound
    "I'm still processing it. Not only that I have a girlfriend, but the fact that my girlfriend is Natsuki. It's bizarre for me to even think about."
    "While it does feel a bit odd, it's great tha--"
    show natsuki 3b at f11
    n "Come on, get up already!"
    "Wait, what was going on?"
    mc "Natsuki? What time is it?"
    n 4e "Why do you use that alarm clock, anyway? It's not like you wake up to it much."
    n "Like I said, get up. It's almost time for school and I've already made your breakfast."
    mc "Alright. Thanks, Natsuki."
    hide natsuki with wipeleft
    scene bg kitchen with wipeleft_scene
    "I go into the kitchen and see not just scrambled eggs, but a few pieces of bacon as well."
    show natsuki 3q at f11
    n "Since I'm your girlfriend now, I thought the meals I make for you should be a little less crappy."
    mc "Really? That's rather nice of you, actually."
    n 4i "I can be nice sometimes! Geez. You could at least thank me or something."
    mc "Sorry. Thank you, Natsuki."
    n 1a "That's better."
    mc "Let's eat, then."
    hide natsuki with dissolve_cg
    "We each eat our breakfast (while sitting together, I'd like to mention) and head off to school soon after."
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
    "As we walk into the Literature Club once we're done with our classes, we're immediately met by Sayori."
    show sayori 1x at f22
    s "Sooooo?"
    mc "So what?"
    s "You two are dating, aren't you? You have to be at this point."
    s 1r "I was going to text you, but I had the feeling you weren't going to spill the beans that easily, ehehe."
    mc "I don't get why it's such a big deal to you, though. Did you make a bet or something?"
    s 4x "Because I've been cheering you two on, of course!"
    "Natsuki rolls her eyes."
    show natsuki 4b at f21
    show sayori 4x at t22
    n "Yeah, we're dating."
    "I expect Natsuki to follow up with something rude, but..."
    n "So what? I'm proud of it."
    show natsuki 4a at t21
    show sayori 4x at f22
    s "For sure! I didn't mean that as a bad thing."
    show natsuki 1b at f21
    show sayori 4x at t22
    n "I know, but I don't see it as a big deal."
    n 3y "I guess the fact that [player] actually got a girlfriend is surprising, though."
    "Well, she's not wrong."
    show natsuki 3y at t21
    show sayori 1r at f22
    s "Ah, well, you're not wrong, ehehe."
    "Wow, even Sayori agrees."
    s 1x "I just think it's super cool! So, congrats to you two."
    mc "Thanks, Sayori. I'm happy about it too."
    n 4q "You better be considering I'm not willing to be just anyone's girlfriend, you know!"
    hide sayori with wipeleft
    show natsuki 4q at f11
    "Sayori laughs as Natsuki and I walk further into the club room."
    mc "That reminds me, about this whole relationship thing, Natsuki."
    mc "What exactly are we supposed to do?"
    n 1b "I'm not exactly romantic, if that's what you're thinking."
    mc "Me neither, and I'd probably end up embarrassing myself if I tried to be romantic."
    mc "Guess this won't be as easy as I thought."
    show natsuki 1a at t22
    m "Not necessarily!"
    show monika 3b at l21
    "Monika walks over from her desk."
    mc "Wouldn't it work better if one of us were more romantic, though?"
    show monika 3b at f21
    m "Sometimes unconventional relationships are the ones that work best."
    m 1b "Not everyone has to follow the standard expectation of a relationship."
    m 1k "I think what's most important is that you're both happy. That's all that matters, isn't it?"
    m "At least, that's how I like to think about it."
    "I almost feel like there's something deeper to that statement, but it doesn't really matter, either."
    m 4k "Well, anyway, I wish you two the best of luck! I think you two make a cute couple, personally."
    show natsuki 4e at f22
    show monika 4k at t21
    n 1v "For the last time, I'm not cute!"
    hide monika with wipeleft
    show natsuki 4e at f11
    "Hmm."
    mc "What, does that mean I am?"
    n 4b "You're funny sometimes, I guess."
    "I feel like those two things aren't quite the same."
    mc "Anyway, I'll go get some manga, Natsuki."
    hide natsuki with wipeleft 
    scene n_cg1_bg
    show n_cg1_base
    show n_cg1_exp1
    with dissolve_cg
    "We read manga again that day, but this time it felt a lot different. It felt more... personal. I noticed that we laughed and smiled a lot more than usual."
    "Can a simple label actually change things that much? Would it have been like this if we got into a relationship earlier, too?"
    "Similar to what Monika said, though, that doesn't matter much. What matters is us being happy. I promised I'd make Natsuki happy, and that thought makes me happy, too."
    "I could try being more romantic, however."
    "I mean, what could go wrong?" 
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
    "Finally, a day where I wake up before Natsuki! Partially because I set my alarm clock 30 minutes earlier than normal, but regardless."
    mc "Hey, Natsuki! Are you going to get up?"
    "Natsuki turns over."
    show natsuki 1bh at f11
    n "Huh? What are you waking me up for?"
    mc "It's morning, isn't it? And you usually wake me up, so I thought I'd do the opposite for a change."
    n 1bb "It's too early for me to get up, dummy. I only wake you up because you oversleep."
    "Uh oh."
    "I think I might have made a mistake. Probably."
    mc "Oh! Um, I'm sorry about that. I won't do it again."
    show natsuki 1bd at f11
    "Natsuki smiles before turning over again."
    n "I think it's nice, though."
    mc "Huh?"
    n 1bq "That you care about me."
    n "You might mess up on a gigantic scale a lot, but it's nice to be cared for by someone."
    n "It's the thought that counts... or something like that, I don't know."
    n "Next time you should think first, I guess."
    n "I'm going back to sleep, now."
    hide natsuki with wipeleft
    "Since I don't feel like getting up after that, I lay back down as well. Two minutes later, though, I hear the sound of blankets rustling."
    show natsuki 1bb at f11
    n "Whew, now I'm ready to get up."
    mc "After two minutes?"
    n "I planned on getting up at this time, yeah."
    show natsuki 1ba at t11
    "I mean, that's not something for me to necessarily complain about, so I'm not sure why I brought it up."
    mc "By the way, I've got something to ask."
    show natsuki 1bb at f11
    n "Yeah?"
    mc "This might sound a bit stupid, but do you think I could make breakfast today?"
    n "I won't turn down more time to rest, but why do you want to make breakfast?"
    mc "Well, you've been making breakfast for over a month now, haven't you? I think it's only fair that I give you a break sometimes."
    n 1bk "Go ahead. I hope your cooking doesn't suck, though."
    n 1bq "Although if you made it for me, then I'd eat it anyway, but still..."
    mc "I think it's cool how much of an effort you've been making to be kinder to me, you know."
    n 5bq "W-What? It's not something I'm intentionally trying to do!"
    n "It just happens."
    n "Ugh. I wish I knew beforehand you'd embarrass me like this once we started dating."
    
    "But wait, does that mean I have to make breakfast? Like, actually {i}make{/i} breakfast? Crap. I usually tend to eat processed food, so I don't know much about homemade cooking."
    hide natsuki with wipeleft
    scene bg kitchen with Dissolve(2.0)
    "I head off to the kitchen, and think about what I want to make."
    "Natsuki likes sweet stuff, right? But this is breakfast, so it's gotta be something breakfast themed."
    "How many breakfast foods do I know how to cook, anyway? Not many, I don't think. I could try something new, but that could also end up being a disaster."
    menu:
        "I need to think about what I should cook. A simple dish would be the safe way to go, but making something bigger might be more interesting."
        "Something simple.":
            "Screw it, scrambled eggs it is."
            
            stop music fadeout 2.0
            window hide
            scene bg kitchen with Dissolve(2.0)
            play music EarlyBird fadein 2.0
            window show
            "After I finish making breakfast for both of us, I present what I made to Natsuki."
            show natsuki 1c at t41
            pause(1.0)
            show natsuki 1c at t44
            pause(1.0)
            show natsuki 1c at t41
            pause(1.0)
            show natsuki 1c at t44
            pause(1.0)
            "She stares at it from multiple angles, and proceeds to take a bite."
            "She doesn't have a look of disgust on her face, so I've got that going for it."
            show natsuki 1b at f11
            n 1b "This isn't seasoned, is it?"
            mc "Ohh, uh, was I supposed to do that?"
            n "Yeah."
            n 4b "I still think it tastes pretty good, though. Not as good as mine, of course."
            n "You did a decent job for your first time cooking."
            mc "I don't cook a lot, but this wasn't my first time cooking, either."
            n 1b "Oh."
            n "You did a decent job for however many times you cooked, then."
            mc "Thanks."
            n 4j "Plus, my scrambled eggs always taste the same, which is to say they taste perfect."
            n "This is definitely below average, so it obviously tastes different."
            n "So, it's nice to have some variety in the food I eat."
            "I'm guessing that was meant as a compliment?"
            mc "I'm glad you at least got something out of it."
            n 1a "Yup. I'm interested in seeing what you cook next."
            mc "Wait, I'm cooking again?"
            n 1b "Only if you want to."
            n "I'm saying you have potential or something like that, I dunno."
            mc "I guess it is true that it's a useful skill to practice."
            n "Yeah. Food tastes so much better when it's specially made by someone else, you know?"
            mc "Made by someone else? That's kind of broad. You mean made by someone you care about?"
            "Natsuki notices what I pointed out and speaks shyly."
            n 5q "T-That's besides the point."
            mc "I'm not so sure. I think it is the point, Natsuki."
            "Natsuki pouts."
            n 5s "You have to point out everything, don't you?"
            mc "Only if I think it's needed."
            n "Fine. Your food tastes better because I know it was you who made it, and you're an important person to me. Happy?"
            mc "A little."
            "It wouldn't hurt for me to practice cooking more often, though."
            mc "Anyway, back to eating."
        "Something complicated.":
            $ makeComplex = True
            "Natsuki's a special person, so she deserves a special meal. This might take awhile, but I'm sure it'll be worth it."
            stop music fadeout 2.0
            window hide
            scene bg kitchen with Dissolve(2.0)
            play music EarlyBird fadein 2.0
            window show
            mc "For the eggs that'd be... one, two..."
            show natsuki 3b at t44
            n "[player]?"
            show natsuki 1b at t43
            mc "Then the oatmeal..."
            show natsuki 1b at f42
            n "[player]!"
            mc "Huh?"
            show natsuki 1b at f11
            "I turn to Natsuki, who is still waiting for me to be done."
            n 4b "Are you sure you know how to cook a meal this big?"
            n "Like, are you actually sure? I'm not convinced you're sure."
            mc "What makes you say that?"
            mc "Granted, it's been nearly thirty minutes now, but that's part of the process."
            n "I just hope it tastes good if we're going to be late for school for this."
            "Oh, crap. We {i}are{/i} probably going to be late for school."
            mc "Well, with how far I am into making this, we'll probably only be about five minutes late. That's not too bad, in my opinion."
            n "Like I said, this food better be worth it."
            scene bg kitchen with wipeleft_scene
            "A few short moments pass, and the food is done."
            "It's a giant meal consisting of scrambled eggs, bacon, oatmeal, pancakes covered with syrup, french toast, and water (there wasn't a carton of orange juice, so I had to cleverly improvise)."
            show natsuki 1c at f11
            "As I bring the meal to Natsuki, she's surprised by how large it is."
            n 1b "Yeesh! I knew it was going to be big, but not {i}this{/i} big."
            "Natsuki is slightly hesitant to try my food."
            "Which is fair, since the food could look a bit more appetizing, and my plating skills aren't exactly fantastic, either. Despite that, she takes a bite of the scrambled eggs."
            "A blank expression rests on her face as she quietly mutters something to herself."
            n "So far so good..."
            show natsuki 1g at lhide
            hide natsuki
            "She tries tasting the french toast next, but before she can try to swallow, she gags and scrambles to drink some water."
            "I don't think this is supposed to be happening."
            n "[player]... you idiot..."
            "Natsuki tries speaking, but her throat is incredibly dry and she keeps coughing."
            mc "Come on! I'm not great at cooking, yeah, but it couldn't have been that bad."
            "Natsuki paces over to the cooking counter and brings something back."
            show natsuki 4e at f11
            n "What's this?"
            "She puts down the container she's holding."
            mc "That's my sugar shaker."
            n "No, it's a salt shaker."
            "Her reaction makes a lot more sense now."
            mc "I could've sworn I picked the sugar shaker, not the salt one."
            "Natsuki drinks some more water."
            n 2e "The two containers look different, too."
            n "Even I don't get how you could've mixed them up."
            "Natsuki sighs and sits down, her elbow resting on the table as she leaves her hand on her forehead. She seems to have come to some kind of realization, I'm guessing?"
            n 5i "You care too much."
            n "Sure, you only just woke up, but the main thing is that you were so caught up in making this huge meal for me that you didn't even check what ingredients you were using."
            n 5q "What did I do to deserve someone this nice?"
            mc "I'm really sorry, Natsuki. I should've made a simpler meal instead."
            n 4b "Hey, you still made a lot of food for me."
            n "I should at least try eating the other parts of it."
            mc "Ignoring the french toast thing, my cooking still isn't that good. I don't think you need to eat the rest of it."
            n "In that case, we can share it."
            n 1y "Here, you can have the french toast."
            mc "I said I was sorry, Natsuki."
            n 1j "I'm joking. But come on, you have to eat too, don't you?"
            mc "I guess so."
            "..."
            mc "...Actually, this tastes terrible. Let's eat some cereal instead."
            n 4b "That's what I thought."
            "I grab two bowls and a box of cereal for Natsuki and I, as we're on our way to forgetting I ever cooked any of that."
    hide natsuki
    window hide
    scene bg kitchen with Dissolve(2.0)
    window show
    "As we ate, I sneaked a question in the middle of it."
    mc "Since we're boyfriend and girlfriend now, we should start going on actual dates now, right?"
    "Natsuki spits out her food all over me."
    show natsuki 1p at f11
    n "Wait, what?!"
    n 4q "...Actually, that wouldn't be any different from what we've done before. Go on."
    mc "I was thinking we could have a picnic. Your thoughts?"
    n 1b "That doesn't sound so bad."
    n "You have to help make the food, though."
    n "I let you be lazy more than the average person does, but even I have my limits."
    mc "Got it. Since it's the weekend, how about we make the food tomorrow and leave that day?"
    n "You should have enough ingredients, so we might as well."
    n 1a "No backing out, either! You promised."
    "I didn't promise anything, but I get the gist anyway."
    
    stop music fadeout 2.0
    window hide
    scene bg bedroom with open_eyes
    play music aNewDay fadein 2.0
    window show
    "Finally, the weekend."
    "Guess it's time to start cooking, then."
    "Where's Natsuki, though? Did she already start making food?"
    scene bg kitchen with wipeleft_scene
    "I head to the kitchen and, as I previously guessed, there was a whole row of foods."
    mc "Whoa! I thought your specialty was baking, Natsuki!"
    show natsuki 1bd at f11
    n "It is. Which is why all the food I've made so far today is stuff that you bake."
    "I take a closer look and see several different flavors of cupcakes."
    mc "Ah, you're right."
    mc "I'm the one who has to make the non-baking stuff then?"
    n 1bb "Yup."
    mc "Okay, I'll list off the foods I know how to make."
    mc "I can make scrambled eggs, peanut butter and jelly sandwiches... that's it."
    if makeComplex is True:
        mc "Well, I can technically make more than that, but you know how that went earlier."
    n 4be "What the heck? Then what's with all these ingredients?"
    mc "That's a pretty good question, actually."
    mc "What's it gonna be, then? Scrambled eggs or peanut butter and jelly sandwiches?"
    n 3bb "Sandwiches, I guess."
    mc "These'll be the best sandwiches you've tasted, trust me."
    "Natsuki smiles. She's tired, but genuinely happy."
    show natsuki 1bj at f11
    n 1bk "I'll wait for you to prove it to me, then!"
    hide natsuki with dissolve_cg
    scene bg kitchen with wipeleft_scene
    "And so, I went on to make the best sandwiches ever."
    "Actually, that's a bit of an exaggeration. I'd like to think they were good, though, but I wouldn't be able to find out until we actually leave for the picnic."
    scene bg house_entrance with Dissolve(2.0)
    show natsuki 1bb at f11
    n "Is everything ready?"
    mc "Should be."
    n "Good. Let's get going already!"
    mc "What, are you looking forward to this or something?"
    "Natsuki's face quickly shifts to a nervous expression."
    n 4bq "N-No! Maybe a little."
    n "Gosh, you do this on purpose, don't you?"
    mc "Guess you've got me all figured out, huh?"
    n "Hmph. You shouldn't tease girls unless you really like them, you know that?"
    mc "We're dating."
    n 4bs "Oh, yeah."
    "Natsuki looks like she's about to throw out another \"But still!\" but can't bring herself to make the excuse."
    n 1bq "Fine, I'll give you that. But I'll win next time!"
    "Next time? Win what?"
    n 5bq "And when I do, you'll pay! You'll owe me a hug or something, I'm still working out the details."
    mc "Sure thing, Natsuki."
    "But for now, it was time for a picnic. A picnic where the only foods were sandwiches and cupcakes, but it wasn't the food that mattered."
    "It was about spending time with my girlfriend, Natsuki."
    
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    pause(2.0)
    scene bg flashback_home with Dissolve(2.0)
    
    window show
    o "Hey."
    o "I wanted to talk."
    n "Oh, there's plenty to talk about. Here, I'll let you start."
    o "Look, I know that things have been a bit... rough between us, but I promise you I'm trying."
    o "It's just so hard."
    n "That doesn't change anything. You still have a daughter to take care of."
    o "..."
    o "...I know. I'm trying."
    n "Whatever you say, dad."
    
    window hide
    show black with Dissolve(2.0)
    pause(2.0)
    scene bg residential_day with Dissolve(2.0)
    play music aNewDay fadein 2.0
    window show
    mc "So, where are we even going to, anyway?"
    "Natsuki and I walk out of my house and head towards... somewhere, I think."
    show natsuki 3bb at f21
    n "I thought you had that planned out already."
    n "You know, since you came up with this idea and all."
    "Whoops."
    mc "I think there's a park nearby we could sit down at."
    n "I'll let you lead the way, then."
    n 4bh "You better not get lost."
    mc "Yeah, yeah, I know."
    hide natsuki with wipeleft
    scene bg park_day with Dissolve(2.0)
    stop music fadeout 2.0
    play music NextToYou fadein 1.0
    "We wander around for a bit--I was heading in the correct direction, I swear--until we stumble upon a grassy park."
    "The weather conditions are perfect for a picnic, luckily."
    mc "Should be here, then."
    show natsuki 1ba at f21
    n "Works for me."
    hide natsuki with wipeleft
    "Natsuki sets down the blanket she's carrying and I put down the baskets of food I'm holding."
    show natsuki 1bd at s11
    "We both sit down as we get ready to eat."
    "I pull out one of Natsuki's cupcakes from the basket and take a bite. It's soft, moist, and delicious, all at the same time."
    mc "Dang, this has to be some of your best work yet."
    n 1bb "Well, considering this is... what, the second cupcake of mine you've ever had?"
    mc "Look, I'd put this in my list of Top 2 cupcakes you've made. It's a compliment."
    "Natsuki smiles and quietly laughs."
    n 1bk "Thanks, [player]."
    "Natsuki takes one of the sandwiches I made and has a bite."
    n 1bj "It's better than your breakfast cooking, I'll say that much."
    mc "Thanks, that's what I was going for."
    "Yeah, I'll go with that."
    "We didn't spend much time eating, meaning we weren't left with much to do afterwards."
    hide natsuki with dissolve_cg
    
    "So, we decided to lay down next to each other on the blanket."
    scene bg sky_day with Dissolve(2.0)
    "Maybe I can take another shot at being romantic?"
    mc "This sky certainly is... blue."
    "Actually, I'll hold off on that for now."
    n "It sure is, [player]. I'm glad you noticed?"
    mc "Cut me some slack, I'm trying to think of something to talk about."
    "Natsuki turns her head and looks into my eyes."
    n "I don't think you have to force yourself to find something to talk about."
    n "Just being together is pretty nice."
    mc "You're not wrong."
    mc "..."
    mc "Hey, Natsuki."
    n "What?"
    mc "Sorry if this is a sensitive topic, but what do you think your future's gonna be like?"
    mc "Do you have a dream job or something?"
    "Natsuki ponders for a little bit."
    n "Hmm."
    n "I've had ideas for what I'd like to do, but I haven't actually decided."
    n "There's so much I've been having to focus on these days that it's not something I can think about right now."
    "Seemingly wanting to change the subject, Natsuki asks me the same thing."
    n "What about you? What's your dream job?"
    n "You can't be a NEET forever."
    "Huh. My dream job? I love anime to death, so maybe with enough practice I could one day become the ultimate animator or something at some point?"
    "No, that's wrong. I'd be lying if I said I ever seriously thought about my future. I wouldn't turn out to be even a rookie animator."
    mc "Honestly, I've got nothing."
    n "Sucks for you."
    "Natsuki sighs."
    n "I'm gonna have to help you get a job at some point, aren't I?"
    mc "Well, I'll take all the help I can get."
    n "Ha, that's what I thought."
    n "I don't know why we're focusing on that, though."
    n "You have to learn to just shut up and enjoy your surroundings sometimes, [player]."
    mc "Yeah, that's true. I'll admit I'm not great at relaxing."
    n "I know how you feel, though. I feel like I've been carrying the weight of the world on my shoulders lately."
    mc "I can make it easier for you."
    "I move closer to Natsuki and slowly put my arms around her, which eventually turns into a hug. She looks surprised, but glad nonetheless."
    n "Y-Yeah, but you can't hug me forever!"
    mc "I can hug you for now, though. I'm sure I'll owe you one later anyway like you said before."
    n "Hmph. Fine..."
    n "I still don't get why you keep being so nice to me, though."
    n "It's not like I've been nice back."
    mc "I think you've acted a lot softer lately, actually."
    n "Really?"
    mc "Yeah. I doubt I've rubbed off on you or anything, but it's cool to see."
    n "You say weird stuff sometimes."
    mc "What, you only just noticed?"
    n "I'm not saying it's a bad thing. It could be one of the reasons why I'm attracted to you."
    n "Or maybe not. You get my point."
    mc "Mmhmm."
    "We stayed in that position for nearly an hour. Normally that seems like something that would never happen, but on a day this peaceful, things sorta came together like that."
    scene bg park_day with Dissolve(2.0)
    mc "We should probably go home, now."
    "Natsuki hugs me tighter."
    show natsuki 1bu at f11
    n "Do we have to?"
    mc "I wish I could stay but, like you said, nothing can last forever."
    mc "We've got homework to do, so..."
    n 5bg "Fine."
    stop music fadeout 2.0
    hide natsuki with wipeleft
    "Disappointed, Natsuki gets up as we start to gather up our stuff. We walk back home immediately after."
    window hide
    scene bg home_interior with Dissolve(2.0)
    window show
    "As we're back in my living room, we sit down on the couch next to each other."
    mc "Well, that happened."
    show natsuki 5bu at t22
    "I grab a leftover cupcake. I'm relaxed, but Natsuki seems to have something on her mind."
    mc "Everything okay, Natsuki?"
    "I take a bite and wait for her response."
    show natsuki 5bu at f22
    n "I've been thinking, and..."
    play music Dusk fadein 2.0
    pause(2.0)
    "Natsuki pauses for nearly a full minute."
    n "I trust you enough to tell you, but this isn't something I want you to be involved with."
    mc "What are you talking about, though?"
    n 4bu "Like I said, I don't want you involved."
    n "Don't worry about me. I've already accepted what's going on."
    "I'd like to help her, but how? She clearly doesn't want me to have anything to do with this."
    mc "If you say so."
    show natsuki 1bu at t22
    "Natsuki gets up."
    n "I'm going to watch some anime."
    mc "If you need me, just ask."
    show natsuki 1bu at lhide
    hide natsuki
    "Natsuki walks off with a worried look on her face."
    "It pains me to watch this happen, but in times like these I need to stay true to myself. As cliche as it sounds, patience is a virtue."
    "And patience has gotten me this far. It's how I managed to get into a relationship with Natsuki in the first place."
    "I think everything will work out in the end. As long as I wait and prepare for whatever might come next, I'll succeed." 
    
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    pause(2.0)
    scene bg bedroom with Dissolve(2.0)
    play music Dusk fadein 2.0
    window show
    mc "Natsuki?"
    "I wake up (before my alarm clock goes off, surprisingly) and see Natsuki nowhere in the room."
    "I didn't hear anything last night, so something bad couldn't have happened, right? I can't let my mind get the better of me for now."
    "I slowly yet confidently walk into the living room."
    mc "There you are."
    scene bg home_interior with Dissolve(2.0)
    show natsuki 12bd at s11
    "I see Natsuki sitting on the couch, with a blanket wrapped around her. I sit down next to her."
    mc "What happened?"
    show natsuki 12ba at f11
    "Natsuki looks like she wants to say something, but can't manage to do so."
    n 1bu "It was just a nightmare."
    mc "That's it? Gotta be a pretty bad dream for you to be out here."
    n "When a nightmare happens in the room you sleep in, you wouldn't want to stay in that room, would you?"
    n "Plus, I didn't want to wake you up."
    mc "You can wake me up any time, Natsuki. I'm here for you."
    n 1bu "Yeah, but it's something I don't want you to have to deal with."
    n "This isn't your fight."
    mc "I'm guessing you're not going to tell me what's going on, then."
    mc "I don't mean that to guilt trip you, but you need to think about what's best for {i}you{/i}."
    n "I know, [player]. Maybe someday I'll tell you."
    mc "It's okay, Natsuki."
    show natsuki 12bd at f11
    "I give Natsuki a hug as she closes her eyes and takes a deep breath."
    mc "Now, how about some breakfast?"
    
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    pause(2.0)
    scene bg flashback_home with Dissolve(2.0)
    
    window show
    n "I can't stand having things continue like this. I want the old \'you\' back."
    n "So what did I do wrong, dad? What did I do that's causing me to be treated like this?"
    n "What did I do to make you neglect me like this?"
    o "Sometimes that's how things go."
    o "There's no real reason for it, at least any that's intentional."
    o "Sometimes it just happens."
    o "Not that I want it to, anyway."
    n "But why?"
    o "As I said, there's not necessarily a reason!"
    o "You have to learn to accept that!"
    n "No. There has to be a reason."
    n "What happened to you?"
    n "I want things to get better."
    n "I want to see you back to normal."
    n "Is that ever going to happen?"
    o "..."
    o "..."
    o "I don't know, Natsuki. I'm trying my best." 
    
    
    window hide
    show black with Dissolve(2.0)
    pause(2.0)
    scene bg streets_day with Dissolve(2.0)
    
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