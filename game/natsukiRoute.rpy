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
    "Her şey gayet normal ilerliyordu, ama bazen Natsuki'nin kısa süreliğine dik dik baktığı uzun boylu bir adamı fark ediyordum. Kim olduğunu hiç söylememişti."
    "Ta ki bugüne kadar."

    "Natsuki’yle buluşup bir yere gitmeye hazırlanıyorduk. Fast food restoranına gitmeye karar vermiştik ama içeri girmeden hemen önce Natsuki yine o adamı gördü."

    show natsuki 1bu at f11
    n "Başka bir yere gidelim."
    show natsuki 1bu at f41
    play music Dusk fadein 2.0
    "İtiraz etmeme fırsat kalmadan kolumu tuttu ve beni oradan götürmeye çalıştı. Ta ki {i}o{/i} konuşana kadar."
    o "Hey, sen. Bir şey sormam lazım."
    "Donakaldım, Natsuki bile beni hareket ettiremedi."
    show natsuki 12bb at f41
    mc "Ş-Şey... Evet?"
    "Aklımdan bin bir düşünce geçiyordu. Bu adam da kimdi? Yoksa başım büyük belada mı?"
    o "Natsuki ile çıkıyor musun?"
    "Yutkundum."
    mc "E-Evet."
    o "Öğrenmek istediğim tek şey buydu. Teşekkürler."
    "Ve sonra hiçbir şey olmamış gibi yürüyüp gitti. Şu anda tamamen kafam karışmış durumda."
    "İçimdeki endişe gittikçe büyüyordu. Evet, kesinlikle başım belada."

    mc "Ne istiyordu benden? Ya da asıl {i}senden{/i} ne istiyordu?"
    show natsuki 1bc at f11
    n "Sakin ol, [player]."
    "Natsuki omzuma dokundu ama hala titriyordum."
    mc "Nasıl sakin olayım? Bu bayağı ürkütücü bir durum."
    "Natsuki yere bakarak iç çekti."
    n 2bu "...O benim babam."
    mc "Ne?!"
    n 1bc "Sana bulaşmasını istemiyorum."
    n 42bc "Eğer bir şey olursa, ben hallederim."
    "Natsuki’nin yüzü ciddileşti. Benden saklanan şey tam olarak neydi?"
    mc "Emin misin? Yani, seni küçümsemek gibi olmasın ama bana söylenmeyen bir şeyler varmış gibi hissediyorum."
    n "Çok düşünüyorsun, [player]."
    n 1bi "Hem de fazlasıyla."
    "Natsuki elini yumruk yaptı, yüzünde sinirle hüznün karıştığı bir ifade vardı."
    mc "Hadi eve gidelim, Natsuki."
    n "Evet..."

    hide natsuki
    scene bg home_interior with Dissolve(2.0)
    stop music fadeout 2.0
    play music Thoughts fadein 2.0
    show natsuki 1bc at f11
    "Eve döndüğümüzde Natsuki iç geçirerek odama doğru yürüdü."
    show natsuki 1bc at lhide
    hide natsuki 
    "Ona bir şey yapmalı mıyım? Onu mutlu edecek bir sürpriz bulabilir miyim?"
    "Kanepeme oturduğumda, sehpanın üstünde duran bir broşür gözüme çarptı."
    "Parfait Girls: The Movie, ha? Yarın vizyona giriyormuş. Natsuki bundan bahsetmişti, değil mi? Sanırım bu, manganın ya da animenin bir parçası olmayan tamamen orijinal bir hikayeydi."
    
    mc "Hey, Natsuki?"
    
    scene bg bedroom with wipeleft_scene
    "Seslenerek odama girdim. Yatağımda uzanmış, düşüncelere dalmış görünüyordu."
    show natsuki 1bu at t44
    n "Hmm?"
    show natsuki 1bb at f11
    mc "Yarın boş musun?"
    n "Sence ben ne zaman meşgul oldum ki?"
    "Düşününce... Gerçekten de hiç 'Çok meşgulüm.' falan dediğini hatırlamıyorum."
    mc "Neyse, ben biraz uyuyacağım. Yarın güzel bir gün olacak, söz veriyorum."
    "Yatağa uzandım ve gözlerimi kapattım."

    stop music fadeout 2.0
    show black with dissolve_cg
    pause(1.5)
    scene bg bedroom_night with open_eyes
    "Derin bir uykuya daldım ama gece yarısı aniden uyandım."
    "Natsuki neden yanımda değil?"

    show black with wipeleft
    "Yavaşça salona doğru ilerledim."
    scene bg kitchen_night with wipeleft_scene  
    show natsuki 1bu at t44
    "Mutfak tarafına dönüp baktığımda, Natsuki’nin buzdolabından bir şeyler aldığını gördüm."
    mc "Natsuki? Bu saatte ne yapıyorsun?"
    show natsuki 1bp at h44
    "Natsuki, birinin uyanık olduğunu duyunca elindekini düşürdü. Neyse ki kırılan bir şey olmadı."
    show natsuki 1bg at t44
    n "Aynı şeyi ben de sana sorabilirim!"
    mc "Ben az önce uyandım ama senin benimle aynı saatte yatmadığını düşünüyorum."
    n 12bc "Bunu düşündüğünü bile görmek istemiyorum, ama sanırım seni bayağı strese sokuyorum, değil mi?"
    play music Dusk fadein 2.0
    show natsuki 12bd at lhide
    hide natsuki
    "Natsuki başını eğdi ve utanarak hızla odama geri döndü."
    
    mc "Natsuki!"

    scene bg bedroom_night with wipeleft_scene  
    "Zaten tekrar uyumayı planlıyordum, bu yüzden odama döndüm. Natsuki yatağımda yüzünü yastığa gömmüş bir halde yatıyordu."
    
    mc "Beni hiç strese sokmuyorsun, Natsuki. Sadece endişeleniyorum, ama bunun üstesinden gelebilirim."

    n "Biliyor musun, aslında sana anlatmayı düşünüyordum."
    mc "Neyi anlatmayı?"
    n "Sen zaten biliyorsun, [player]."
    "Babasından mı bahsediyordu?"
    n "Ama bunu yapmaya cesaret edemiyorum. Belki de hiç edemeyeceğim."
    "Yüzünü göremesem de sesinden ağladığını hissediyordum."

    mc "Adım adım, Natsuki."
    "Yatağa girip yanına uzandım."
    
    mc "Şimdi, elimi tut."
    "Natsuki elimi sıkıca kavradı."
    
    mc "İşte, biraz daha iyi hissettin mi?"
    mc "Hadi uyu artık. Sana yarın için bir planım olduğunu söyledim, değil mi?"
    mc "Hoşuna gidecek, inan bana."
    "Natsuki sessizleşti. Uyuduğunu düşündüm. Benim de uyumam en iyisi olurdu."
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    scene bg bedroom with open_eyes 
    window show
    "Ertesi sabah uyandığımda, Natsuki'nin hâlâ derin bir uykuda olduğunu fark ediyorum. Sanırım ilk kez ondan önce uyanıyorum, şimdi düşününce."
    play music Thoughts fadein 2.0
    scene bg kitchen with wipeleft_scene
    "Kahvaltı yapmak için odamdan çıkarken içimde hafif bir endişe hissediyorum. Şimdilik görmezden geliyorum ama bunu ne kadar sürdürebilirim? Ne zaman pes ederim?"
    "Çırpılmış yumurta yaparken düşünmek isteyeceğim bir şey değil bu, o yüzden düşünmüyorum."
    "Bunun yerine, kahvaltıyı hazırladıktan sonra odama dönüp vaktimi Natsuki'yi götürmeyi planladığım Parfait Girls filminin biletlerini almakla değerlendiriyorum."
    scene bg bedroom with wipeleft_scene    
    "Odaya döndüğümde, Natsuki'nin uyanmış olduğunu görüyorum. Onun için hâlâ endişeliyim, bu yüzden nasıl hissettiğini soruyorum."
    mc "Biraz daha iyi hissediyor musun?"
    show natsuki 1bc at f44
    n "Birazcık."
    mc "Güzel. Unutma, bugün için güzel bir sürprizim var."
    n "O zaman geldiğinde beni uyandır."
    hide natsuki with wipeleft  
    "Natsuki arkasını dönüp tekrar uyumaya çalışıyor."
    "Aklım tekrar endişelere kaymaya başlıyor, ama sürekli böyle düşünmek istemiyorum."
    "En azından şimdilik..."
    window hide
    scene bg bedroom with wipeleft_scene
    window show
    "Birkaç saat geçiyor ve artık çıkma vakti yaklaşıyor."
    mc "Hazır mısın, Natsuki?"
    stop music fadeout 2.0
    show natsuki 1bw at t44
    play music NatTheme fadein 2.0
    "Natsuki mahmur bir şekilde cevap veriyor."
    n "Ne için?"
    mc "Gerçekten unuttun mu?"
    n "Bana ne yapacağımızı bile söylemedin ki."
    "Natsuki yataktan kalkıyor."
    mc "Ah, doğru ya. O zaman şimdi öğrenme vaktin geldi!"
    "Sabah bastırdığım biletleri gösteriyorum."
    n 1bc "Aaa!"
    n 1bb "Aslında o kadar da şaşırtıcı değil. Zaten biletleri alacağını tahmin etmiştim."
    mc "Öyle mi?"
    n "Dün sana bilet alıp alamayacağımızı soracaktım ama ne kadar yorgun olduğumu biliyorsun."
    n "Bugün ise sormaya çalıştım ama sen biletleri bastırırken fark ettim, yani..."
    "Hah. Muhtemelen su almaya falan kalktı ve yazıcının sesi yüzünden fark etmedim."
    mc "Her neyse, film başlamak üzere. Hadi gidelim!"
    hide natsuki with wipeleft  
    scene bg streets_day with wipeleft_scene
    "Kısa bir süre sonra dışarı çıkıp sinema salonuna doğru yola koyuluyoruz."
    show natsuki 1bc at f11
    n "Bunu neden yapıyorsun ki? Yanlış anlama, şikayet etmiyorum."
    mc "Bilmiyorum, son zamanlarda biraz zorlandığını hissettim. Düşüncelerini dağıtmak için güzel bir şey yapmak istedim."
    "Natsuki'nin minnettar olduğu anlar nadirdir ama öyle olduğu zaman gerçekten çok hoşuma gidiyor."
    n 1bq "Teşekkür ederim. Gerçekten, bunu hak etmiyorum."
    n "...Ya da, tamam, birazını hak ediyorum ama yine de."
    "En azından, Natsuki eski haline dönmeye başlıyor gibi görünüyor."
    "Bilet gişesindeki adama yaklaşıyoruz."
    mc "Saat 15:30 Parfait Girls seansı için iki bilet lütfen."
    $o_name = "Çalışan"
    o "Buyurun, geçebilirsiniz."
    $o_name = "???"
    hide natsuki with dissolve_cg
    show black with dissolve_cg
    "Natsuki ile sinema salonuna giriyoruz. Lobi devasa, böyle bir yer için fazlasıyla geniş."
    "Atıştırmalık standı, dünyanın dört bir yanından gelen sinema salonu ikramlarıyla dolu."
    "Ama tabii ki asıl önemli olan bu değil. Salonumuza yöneliyoruz ve fark ediyoruz ki burada yalnızca biz varız."
    n "Doğru saatte geldik, değil mi?"
    mc "Saat 15:30 oldu işte?"
    mc "Ama bak, en önden oturacağız!"
    mc "...Gerçi pek bir önemi yok."
    stop music fadeout 2.0
    "Yan yana oturuyoruz ve film başlıyor."
    "..."
    "..."
    "..."
    pause(1.5)
    
    play music NatTheme fadein 2.0
    mc "Ne düşünüyorsun, Natsuki?"
    show natsuki 4bb at f11
    n "Bilemiyorum, abartıldığı kadar iyi mi emin değilim ama fena değildi."
    mc "Aynen. Seriyi filme uyarlayacaklarını duyduğumda biraz şüpheliydim ama bence iyi iş çıkarmışlar."
    "Natsuki'nin omzuna doladığım kolumu geri çekip ayağa kalkıyorum."
    mc "Hadi eve dönelim."
    n "Bir dakika, [player], söylemek istediğim bir şey var."
    "Natsuki, her zamanki gibi, gergin olduğunda yaptığı gibi yana bakıyor."
    mc "Ne oldu?"
    n 4bq "Şey... teşekkür ederim."
    n "Beni gerçekten önemseyen bir sevgilim hiç olmadı... hatta bir sevgilim bile olmadı..."
    n "Beni böyle düşünen bir arkadaşım bile olmadı... Senin gibi biri hiç olmadı."
    n "Benimle birlikte yemek yapan, benim istediğim filmlere götüren tek kişi sensin."
    n "Bana bu kadar iyi davranan tek kişi sensin... O yüzden bazen sana kaba davranırsam, bunun nedenlerinden biri olduğunu bil."
    n "Böylesine iyi birine alışık değilim, nasıl tepki vereceğimi bile bilmiyorum."
    n "Bir de, başkalarının beni nasıl gördüğünü çok düşünüyorum, en iyi olmak istiyorum. O yüzden biraz da öyle davranıyorum."
    n "..."
    n "..."
    n 12bc "...Bu çok saçma. Zamanını boşa harcadım, özür dilerim."
    show natsuki 12bc at lhide
    hide natsuki
    "Natsuki başını öne eğerek ayağa kalkıyor ve çıkışa yöneliyor."
    "Ne oluyor, Natsuki? Bu bulmacanın eksik kalan parçası ne?"
    
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    pause(2.0)
    scene bg flashback_home with Dissolve(2.0)
    
    window show
    o "Natsuki, notların hakkında konuşmamız lazım."
    n "Evet, ne var yani?"
    o "Neden bahsettiğimi biliyorsun."
    n "Notlarım berbat, işte bu kadar. Başka ne var?"
    o "Bu böyle devam edemez. Özel ders mi alırsın, başka bir yol mu buluruz bilmiyorum ama bu şekilde gitmesine izin veremeyiz."
    o "İkinci kez sınıfta kalmana göz yumamayız, Natsuki."
    n "Ee, kalsam ne olacak ki? Gerçekten bu kadar büyük bir mesele mi?"
    o "Eğitiminin önemli olduğunu biliyorsun."
    n "Ama nasıl düzelecek ki? Hayatım bu haldeyken notlarım nasıl düzelebilir? Burada yaşadığım sürece nasıl daha iyi olabilir ki?"
    n "Bütün bunlarla uğraşırken elimden gelenin en iyisini yapıyorum."
    o "Peki tekrar sınıfta kalırsan ne yapacaksın? Arkadaşlarına ne söyleyeceksin? Tanıştığın insanlara yaşını mı saklayacaksın?"
    n "Beni dinliyor musun gerçekten?"
    o "Evet, ama esas noktayı kaçırıyorsun."
    n "Hayır. Ben senin noktanı anladım ama sen benimkini anlamıyorsun."
    n "Ama madem böyle olsun istiyorsun, tamam."
    n "Zaten elimden bir şey gelmiyor ki."
    n "Hayatımda olup biten hiçbir şeyi değiştiremedim, bunu da değiştiremem."  

    
    window hide
    show black with Dissolve(2.0)
    pause(2.0)
    
    
    window show
    
    "Her şey birkaç gün boyunca normal seyrinde devam etti."
    "Aslında, buna 'normal' der miydim bilmiyorum. İçimde garip bir his vardı ve bir gece, nedenini öğrenecektim."
    scene bg bedroom_night with open_eyes   
    "Saat sabaha karşı 3 civarı olmalıydı. Natsuki ve ben uyuyorduk, ta ki aniden gelen bir 'güm' sesiyle uyanana kadar."
    "Sesin geldiği yöne döndüğümde, Natsuki’nin yataktan düştüğünü gördüm."
    "Başta pek önemsemedim. Muhtemelen yine bir kabus görmüştü ve uykusunda dönerken düşmüştü diye düşündüm."
    "Kısmen doğruydu ama yere düştüğünde, kıyafeti hafifçe kayarak sağ omzunu açığa çıkardığında, uzun zamandır eksik kalan o son parçayı nihayet görmüş oldum."
    play music Excuses fadein 2.0
    show natsuki 12bb at t41
    "Natsuki gözlerini açıp bana baktı. Uykulu görünüyordu, sonuçta yeni uyanmıştı."
    mc "Natsuki?! O morluk da ne? Natsuki!"
    "Ve işte buradayım. Şok olmuş, öfkeli ve ne yapacağımı bilemez halde."
    "Başka bir açıklama bulmaya çalışsam da, buna hiç gerek yoktu. Zaten her şey yerine oturmuştu."
    "Düşünceler beynimde yankılanıyor..."
    "O morluğun sebebi..."
    "Beni neden terk edip benimle yaşamaya geldiği..."
    "Babası hakkında neden hep böyle davrandığı..."
    "Başka bir ihtimal yoktu. Belki de hemen sonuca varıyorum ama düşündüğüm tek bir şey vardı: Natsuki, babası tarafından vurulmuştu."
    "Ve eğer bu yeterince kötü değilse, olası sonuçları çok daha korkunç olabilirdi."
    "Başım dönüyor. Peki şimdi? Şimdi ne yapacağım? Bunu görmezden gelmem mümkün değil."
    "Daha önce göz ardı edebiliyordum çünkü durumun ciddiyetini bilmiyordum. Ama artık biliyorum."
    "Bildiğime göre, bir şeyler yapmalıyım."
    n 12be "[player]... O şey, yani bu morluk..."
    mc "Boşuna uğraşma."
    mc "Biliyorum zaten."
    "Natsuki’nin yüzünde suçluluk dolu bir ifade vardı."
    n 12bd "Bana kızgın mısın, [player]?"
    n "Bunu daha fazla saklayamam. Daha önce sana söylemedim çünkü seni bu işin dışında tutmanın doğru olduğuna inanıyordum ama..."
    mc "Sana kızgın değilim."
    mc "Bunu böyle öğrenmek istemezdim ama kızgın olduğum kişi sen değilsin, Natsuki."
    mc "Bunu yarına bırakabiliriz diyebilirdim ama sanırım ikimiz de tekrar uyuyacak gibi değiliz."
    "Natsuki'ye yatağa geri dönmesi için işaret ettim ve o da yavaşça yatağa çıktı."
    show natsuki 12bd at f11
    mc "Bir şey içer misin? Aç mısın?"
    n "Hayır."
    n 12be "Sadece... bunu halledelim artık."
    "Natsuki’nin yüzündeki ifadeler sürekli değişiyordu. Korku, pişmanlık ve üzüntü, hepsi bir aradaydı."
    mc "Bu ne zaman oldu, Natsuki?"
    "Konuşurken ben de yatağa geri girdim ama artık battaniyelerin sıcaklığı bile bana bir rahatlık vermiyordu."
    n "Hani bir gün sana bağırıp herkesten nefret ettiğimi söylemiştim ya?"
    mc "Hatırlamak istemediğim bir anı ama, evet."
    n "O gün sınıftan çıkıp doğrudan eve gittim. Babamla yine tartışmaya başladık ve..."
    "Onu orada durdurdum."
    mc "Dur bir dakika, 'yine mi' dedin? Yani bu sık sık olan bir şey mi?"
    n "Ee, bunu açıklamak için biraz daha geriye gitmem gerek ama—"
    "Tekrar bölmek istemiyordum ama önce şu morluk meselesini netleştirmem gerekiyordu."
    mc "Özür dilerim, hikâyeye devam et. Diğer şeyleri sonra konuşuruz."
    n "Tamam. Tartışma büyüdü ve... sonra..."
    "Natsuki, morluğunu tekrar gösterdi."
    mc "Ve sonra doğrudan benim evime geldin, değil mi?"
    n 12bd "Evet."
    mc "..."
    mc "Üzgünüm, bunu hala tam olarak kafamda oturtamadım. Ama o olayın üzerinden bir aydan fazla zaman geçti."
    mc "Bu morartının şimdiye kadar geçmesi gerekmiyor muydu?"
    n 12be "Bilmiyorum. Ben de düşündüm bunu ama kimseye söylemek istemedim, o yüzden..."
    mc "Bunu sonra konuşuruz. Şu an her şeyi biraz daha iyi anladığımı düşünüyorum ama babanla ilgili durumu daha iyi kavrayabilmem için birkaç şey sormam lazım. Hep böyle miydi?"
    "Natsuki derin bir nefes aldı."
    n "Eskiden evde her şey daha iyiydi, ya da en azından daha normaldi."
    n "Harika olduğu söylenemezdi, ama bu da biraz maddi durumumuzun zorluğuyla alakalıydı."
    n "Annem ben daha küçükken vefat etti, o yüzden o zamandan beri babam büyüttü beni."
    n "Berbat bir baba değildi aslında. Kolay sinirlenirdi ama son birkaç yılda olduğu kadar değil."
    mc "Peki, onu bu kadar öfkelendiren şey ne oldu?"
    n 12bc "Bilmiyorum. Belki de her şey üst üste gelince baş edemedi."
    n "Annemle on beş yıl evli kaldıktan sonra beni dünyaya getirmişler. Sanırım onun için ailesini bir arada tutmak kelimelere dökemeyeceği kadar önemliydi."
    n "Son zamanlarda maddi durumumuz daha da kötüleşti. Henüz tamamen batmadık ama onun için zor olduğu kesin."
    mc "Bu, yaptıklarını haklı çıkarmaz."
    n 12bc "Ben de öyle bir şey söylemedim zaten! Ben de buna öfkeliyim."
    "İç çektim. Bir anda bu kadar fazla şey öğrenmek gerçekten ağır geliyordu. Belki de bunu konuşmak için sabaha kadar beklemeliydim ama artık geri dönüş yoktu."
    n 12bc "Yıllar geçtikçe babam benden uzaklaşmaya başladı."
    n "Yani, aslında {i}herkesten{/i} uzaklaştı."
    n "Bunu yapmak istiyorsa yapabilir ama sonuçta onun bakmakla yükümlü olduğu bir kızı var. Ara sıra yemek yapmak yeterli değil."
    n "İhmal edilmiş gibi hissediyordum. Sanki bir hata yapmışım da ceza çekiyormuşum gibi ama neyi yanlış yaptığımı bilmiyordum."
    mc "İçiyor mu, Natsuki?"
    n "Hayır, sanmıyorum."
    n "En azından hiç içtiğini görmedim."
    mc "Hmm."
    n "Dediğim gibi, ona nasıl davrandığı konusunda sık sık tartışıyorduk. Sadece ihmal değil, başka şeyler de vardı."
    n "Kafasında mükemmel bir kız çocuğu imajı vardı. Bana biraz esneklik tanıyordu ama kendi evimde manga koleksiyonu bulundurmama bile izin vermeyecek kadar değil."
    mc "Kendi hayatına bile doğru düzgün bakamazken senin hayatını bu kadar kontrol etmeye mi çalışıyordu?"
    n "Aynen öyle."
    "Ne kadar çok şey duyarsam duyayım, Natsuki için içim daha da kötü oluyordu."
    "Kimsenin böyle bir hayat yaşamak zorunda kalmaması gerekir."
    n "Beni en iyi kızı olmaya zorladığı için yıllarca bana da bunu öğretti."
    n "Beni herkesten üstün olmam için eğitti."
    n 12be "Ve evet, başarılı olmamı istemesi bir şey ama..."
    mc "Bunu sana bu kadar baskı yaparak dikte etmesine gerek yoktu, değil mi?"
    n "Evet. Ama olay sadece dersler de değildi."
    n "Zaten hiçbir zaman mükemmel bir öğrenci olmadım."
    n "Sosyal olarak da en iyisi olmamı istiyordu, en fazla arkadaşa benim sahip olmamı..."
    n "Her zaman işe yaramayacağını bilsem de insanlarla konuşmayı denememi öğütlüyordu."
    n "Ne yapacağımı hiç bilemedim. Onun gibi birinden tavsiye almak istiyor muydum, onu bile anlamaya çalışmadım."
    n "Ama zaten bir noktada önemi de kalmadı. Çünkü ona olan güvensizliğim yüzünden insanlarla arkadaşlık kurmakta hep zorlandım."
    "..."
    "Şu an düşünemiyorum bile. Aklım tamamen durmuş gibi."
    "..."
    n "Dediğim gibi, böyle biri olmak istemedim."
    n "Ama olaylar böyle gelişti. Bazen insanlara karşı nazik olmaya çalıştım, ama çoğu zaman zayıflık göstermemek için kendimi sert tuttum."
    n "Neden böyle oldu bilmiyorum ama oldu işte."
    "Natsuki bir an duraksadı, derin bir nefes aldı. Bütün bunları hatırlamak hiç de kolay olmasa gerek."
    n "Sanırım onu bu kadar başarı takıntılı yapan şey kendisiydi."
    n 12bd "Bence, benim onun gibi olmamı istemedi."
    "Natsuki, her an gözyaşlarına boğulacak gibi duruyordu. Ama sormam gereken bir şey vardı."
    mc "Natsuki."
    mc "Babanı hala önemsiyor musun?"
    "Natsuki uzun uzun düşündü. Odada sessizlik hâkimdi."
    n "Bunun bir kısmı hâlâ içimde var."
    mc "Tamam, aynı fikirde olduğumuzdan emin olmak istiyorum."  
    mc "Babanın sana yaptıkları... istismardı, Natsuki."  
    mc "Ve bir şeyin altını çizmem lazım. Yaptığı başka bir şey daha vardı; seni açıkça ve kesinlikle ihmal etti, bunu hiçbir şey haklı çıkaramaz."  
    mc "Ona karşı gerçekten ne hissediyorsun? Her şeyi düşün, Natsuki."  

    "Natsuki'nin cevap vermesini beklerken ona biraz zaman tanıyorum."  
    "Bütün bunları öğrenmek tuhaf hissettiriyor. Sanki bir şeylerin yanlış olduğunu hep biliyordun ama ancak şimdi, olayın ne kadar korkunç olduğunu gerçekten kavrıyorsun."  
    "Bunun bu şekilde ortaya çıkması bana garip geliyor. Komik değil, ama düşündükçe ironik bir tarafı da var."  
    "Natsuki, bunu benden saklamak için elinden geleni yaptı. Her zaman iyi başaramasa da saklamaya devam etti."  
    "Ama sonra bu gece oldu. Çünkü yatağım duvara dayalı olduğu için sadece sol tarafta yatarsan düşebilirsin."  
    "Bu gece yatağa ilk giren bendim ve sağ tarafa uzandım."  
    "Yani Natsuki'nin sol tarafta yatmaktan başka şansı yoktu."  
    "Eğer bu olmasaydı, düşmeyecek, ben de morartısını görmeyecek ve bütün bunları asla öğrenmeyecektim."  

    "Natsuki'ye düşünmesi için zaman tanıyordum ama aklıma bir şey takıldı."  
    mc "Baban hiç... kendine zarar vermeye çalıştı mı?"  
    n 12bc "Ne?"  
    mc "Yani... intihara teşebbüs etti mi hiç?"  
    n "Hayır, etmedi."  
    mc "Sadece bir şeyi çözmeye çalışıyorum."  
    mc "Bana herkesten uzaklaştığını söyledin. Hayatın üstüne üstüne geldiğinden sıkıldığını düşündüğünü söylemiştin, değil mi?"  
    mc "Eşini kaybetti, maddi durumu kötüydü... her şey üst üste geldi."  
    n "Sanırım öyle."  
    mc "Peki, hiç... intihara kalkışmış olabilir mi?"  
    mc "Biliyorum, biraz alakasız gelebilir ama aklıma takıldı."  
    mc "Yaşamak için bir sebebi olmalıydı, değil mi?"  
    n "Ya da sen fazla derin düşünüyorsun."  
    mc "Hayır, bence burada bir şey var."  
    mc "Yoksa geriye sadece iki ihtimal kalıyor: Ya herkesten uzaklaşmasının başka bir sebebi vardı ya da yaşamak için hiçbir sebebi yoktu."  
    mc "İlk ihtimali destekleyecek hiçbir şey yok, olsa bile mantıklı olur muydu bilmiyorum. İkinci ihtimale gelirsek, eğer gerçekten yaşamak için sebebi olmasaydı, en azından bir kez denemez miydi?"  
    n 12bg "Gerçekten, bunu fazla kuruyorsun."  
    n "Birini tam olarak tanımıyorsan ne hissettiğini anlayamazsın."  
    n "Bu kadar basit."
    mc "Babanın senin başarılı olman konusunda bu kadar takıntılı olmasının sebebinin, senin de onun gibi olmanı istememesi olabileceğini söylemiştin, hatırlıyorum."  
    mc "Peki ya sırf senin için yaşamaya devam ettiyse?"  
    mc "Eğer gerçekten öyleyse, yaptığı şeyler düşünüldüğünde bu çok garip, hastalıklı bir sevgi gösterme şekli olurdu."  
    mc "Ama ona ne kadar kızgın olsam da, belki de durum gerçekten buydu diye düşünmeden edemiyorum."  
    "Aklım iyice karıştı. Onun yaptıklarını haklı çıkaracak hiçbir şey yok, şiddet asla bir çözüm olamaz. Ama belki de olaya tamamen yanlış açıdan bakıyorumdur."  
    "Belki de bu durumun {i}doğru{/i} bir bakış açısı bile yoktur."  
    "Yaptıkları affedilemez ama yine de düşünüyorum..."  
    mc "Bunu sormayı unuttuğuma inanamıyorum ama... Bu, onun sana vurduğu ilk sefer değil mi? Anlattıklarından çıkardığım buydu."  
    n "Evet, bana vurduğu ilk seferdi."  
    n "Annemle evlendiklerinde, eğer bir gün çocukları olursa, asla şiddete başvurmayacaklarına dair söz vermişlerdi."  
    n 12bf "Acaba annem bunu öğrense ne hissederdi..."  
    "Natsuki sonunda gözyaşlarını tutamıyor."  
    mc "Uzun bir gece oldu, Natsuki."  
    mc "Bana bunları anlatabildiğin için seninle gurur duyuyorum."  
    "Natsuki konuşmakta zorlanıyor."  
    n 12bi "B-bunun bir seçenek olduğunu mu sanıyorsun!?"  
    mc "Belki, ama bu, bunu yapmanın kolay olduğu anlamına gelmez."  
    n "Daha ne kadar böyle sürecek?"  
    "Natsuki daha da hıçkırarak ağlıyor."  
    mc "Hey, ben senin sevgilinim. Zor zamanlarında yanımda olup seni rahatlatmam gerekmez mi?"  
    mc "Bırak bunu yapayım. Bırak seni rahatlatayım."  
    hide natsuki with wipeleft  
    "İkimiz de yatağa uzanıp birbirimize sarılıyoruz. Hayatımda hissettiğim en içten, en duygusal sarılmaydı bu."  
    "...Sanırım ben bile biraz ağladım."  
    window hide  
    stop music fadeout 2.0  
    show black with Dissolve(2.0)  
    play music alarm  
    window show  
    "{i}BEE--{/i}"  
    scene bg bedroom with open_eyes  
    play music Thoughts fadein 2.0  
    "Bugün alarm çalmasının hiçbir anlamı yoktu."  
    "Edebiyat Kulübü ne düşünecek, ne söyleyecek umurumda değildi. Bugün okula gitmeyecektik."  
    "Natsuki'ye bakıyorum. Uyurken bile hâlâ bana sarılıyor... Onu böyleyken okula göndermem mümkün değildi."  
    "Onu yalnız bırakmak da istemiyorum. O yüzden durum bu."  
    "Dün gece konuşulan her şeyden tam olarak emin olamasam da..."  
    "Hâlâ cevaplanmamış birçok soru var. Hatta sorulmamış olanlar da... Ve Natsuki'nin babasıyla ilgili ne yapacağımız konusunda bir karara varmış da değiliz."  
    "Ama Natsuki'ye ne kadar isterse burada kalabileceğini söylemiştim. Şimdi o sözü tutmamak olmaz."  
    "Kalkıp kahvaltı hazırlamayı düşünüyorum ama bekleyebilirim. Natsuki'nin yanında biraz daha kalmak istiyorum."  
    "Zihnimde dönen onlarca düşünceyle on dakika kadar geçiyor. Tam yeniden uykuya dalacakken, Natsuki uyanıyor."  

    show natsuki 1bh at f11  

    n "Huh?"  
    "Natsuki panikle irkilir."  
    n "[player]! Okula geç kalmak üzereyiz!"  
    mc "Dün gece olanları unuttun mu yoksa?"  
    n 1bu "Unutmadım ama..."  
    hide natsuki with wipedown  
    mc "Bunca şey yaşanmışken bile kendini zorluyorsun."  
    mc "Dinlenmen gerekiyor, Natsuki."  
    "Natsuki bir şeyler söyleyecek gibi duruyor ama başı yastığa düşüyor."  
    n "Peki..."  
    n "..."  
    n "Seni seviyorum, biliyor musun?"  

    "Natsuki'nin yüzüne bir gülümseme yayılıyor. Bu beni biraz şaşırtıyor. Böyle bir durumda gülümsemesini beklemiyordum."  
    mc "Ben de seni seviyorum, Natsuki."  
    mc "Sonuçta, biz boşuna sevgili olmadık."  
    n "Evet ama... Bunu yeterince söylemiyor gibiyim."  
    n "Bazen biraz kötü biri olabiliyorum."  
    n "Ama seninleyken her şeyi yapabilecek gibi hissediyorum."  

    "Natsuki beni kendine doğru çekip daha sıkı sarılıyor."  
    n "O yüzden... benimle kal, olur mu?"  
    n "Lütfen..."  
    "Onun bunu uykusuzluktan mı, yorgunluktan mı yoksa başka bir sebepten mi yaptığını bilmiyorum ama... şikayet edecek halim yok."  
    mc "Ne kadar istersen seninle kalacağım, Natsuki."  
    stop music fadeout 2.0  
    window hide  
    show black with Dissolve(2.0)  
    window show  
    scene bg bedroom_night with open_eyes  
    play music Dusk fadein 2.0  
    "Ugh... saat kaç oldu?"  
    "Etrafımda neler olup bittiğini pek fark etmeden telefonuma bakıyorum."  
    "Neredeyse akşam 7 mi olmuş? Bu kadar mı uzun uyuduk?"  
    mc "Natsuki? Uyanık mısın?"  
    "Hâlâ bana sarıldığına göre uyanık gibi durmuyor."  
    show natsuki 1bb at t11  
    n "...Huh?"  
    show natsuki 1ba at t11  
    "Natsuki uyanıyor ve gözlerini ovuşturuyor."  
    mc "Saat neredeyse akşam 7."  
    n "Tamam."  
    hide natsuki with dissolve_cg  
    "Natsuki tekrar uyumaya çalışıyor. Bunu anlıyorum ama... her şey gerçekten bu kadar kolay unutulabilir mi?"  
    "Aslında ben ne düşünüyorum? Natsuki zaten fazlasıyla şey yaşadı; onu uyandırmaya çalışmak bencilce olurdu."  
    "Ama bu durumla nasıl başa çıktığım hakkında beni düşündürüyor."  
    "Onun yaşadıklarına dair hiçbir deneyimim yok. Benim bile yaşamadığım bir konuda gerçekten ona yol gösterebilir miyim?"  
    "Peki ya ben değilsem, kim?"  
    "Natsuki'ye danışmanlık alıp almak istemediğini henüz sormadım ama şu an bana en çok güvenen kişi benim, değil mi?"  
    "Belki fazla düşünüyorum ama bunun önemli bir konu olduğuna eminim."  
    "Şu andan itibaren söyleyeceğim her şey onun hayatını sonsuza dek değiştirebilir."  
    "Belki benimkini de..."  
    stop music fadeout 2.0  
    window hide  
    show black with Dissolve(2.0)  
    window show  
    scene bg bedroom_night with open_eyes  

    "Uyumaya devam ettim ve gece 11 civarında uyandım. Sanırım daha önce hiç bu kadar uzun uyumamıştım."  

    show natsuki 1bu at t41  
    "Ama bu sefer Natsuki de uyanık. Yana dönüp baktığımda elinde bir manga tuttuğunu görüyorum."  

    show natsuki 1bu at t11  
    mc "Hey."  

    "Natsuki bana hafif gergin bir ifadeyle bakıyor."  

    n 12be "Ne var?"  
    mc "Konuşabilir miyiz?"  

    "Natsuki, sanki bunu ertelemek istiyormuş gibi görünüyor. Onu suçlayamam."  

    n "Zaten 'evet' dememi bekleyeceksin, değil mi?"  

    "Natsuki mangayı kenara koyup battaniyeyi kendine doğru çekiyor."  

    mc "Babanla olan durum hakkında ikimiz de aynı fikirdeyiz, değil mi?"  
    mc "Ama bu, başka bir sorunu da beraberinde getiriyor: Bu durumu nasıl ele alacağımızı bulmak."  

    n 1bu "Neden bir şey yapmak zorundayız ki?"  
    mc "Ne demek istiyorsun?"  
    n "Yani, neden bunu çözmeye çalışmak zorundayız?"  
    "Aslında haksız mı? Bu duruma illa bir çözüm bulmamız mı gerekiyor?"  
    mc "Peki, hâlâ baban için bir şeyler hissediyor musun?"  
    n 1bc "Evet, ama şu an yaşadığım hayattan memnunum."  
    "Acaba benim değiştirmem gereken bir şey mi bu? Yoksa gerçekten bu benim işim değil mi?"  
    mc "Sence, her şey yoluna girseydi daha mutlu olur muydun?"  
    n "Belki olurdum, ama bunu öğrenmek için riske girmek istemiyorum."  
    "Bu konuda düşünerek kendi içimde kısır döngüye mi giriyorum?"  
    "Natsuki’ye yardım etmek istiyorum. O benim için çok önemli ve onu çok seviyorum, ama bunu yapmamın doğru olup olmadığını da sorguluyorum."  
    "O bana gerçekten bu konuda yardım etmemi söyledi mi?"  
    n 12be "Bunu sonra konuşabilir miyiz?"  
    mc "Bilmiyorum, konuşmalı mıyız ki?"  
    mc "Açıkçası, şu an söylediklerimden pek emin değilim."  
    mc "Ama bu konuyu kapatırsak her şey eskisi gibi mi olacak?"  
    mc "Bir dahaki sefere birlikte dışarı çıktığımızda her şey aynı mı olacak?"  
    mc "Dediğim gibi, baban hakkında ne yapmamız gerektiğini bilmiyorum."  
    mc "Sadece, bir şey yapmazsak içimde bir şeylerin eksik kalacağını hissediyorum."  
    n 3bu "Biliyor musun, eskiden ben de böyle düşünürdüm."  
    n "Seninle yaşamaya başladığım ilk zamanlar hep bunu düşünürdüm. O zamanlar ne kadar gergin olduğumu hatırlıyor musun?"  
    n "Ama sonra... bırakmayı öğrendim sanırım."  
    n "Sonunda seninle çıkmaya başladım ve işte buradayız."  
    n "Böyle yaşamamızda bir sorun yok, değil mi?"  
    n 4bu "Babam zaten benimle konuşacak kadar bile umursamıyor gibi görünüyor."  
    "Bunu ben de düşünmüştüm aslında. Daha önce Natsuki'nin babasını dışarıda gördüğümüzde neden hiç konuşmadı? Ama bir keresinde benim onunla çıkıp çıkmadığımı sormuştu."  
    mc "Eğer senin istediğin buysa, Natsuki, o zaman senin kararına saygı duyarım."  
    mc "Hâlâ merak ettiğim pek çok şey var ama dediğin gibi, yaşadığımız şekilde bir sorun yok."  
    mc "Eğer bunu şimdilik bir kenara koymak istiyorsan, bu da sorun değil."  
    show natsuki 12bd at f11  
    "Natsuki bana sarılıyor."  
    n 12be "Teşekkür ederim, [player]."  
    "Natsuki son zamanlarda çok tatlı davranıyor. Bunda sevgilisiyle konuşmasının etkisi olduğu kadar, daha sağlıklı bir ortamda yaşamasının da etkisi var bence."  
    "Belki de bu noktada durmak doğrudur. Şu an ikimiz de mutluyuz, o yüzden her şeyi olduğu gibi bırakmakta yanlış bir şey yoktur belki de."  
    "Öyle değil mi?"  

    
    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    window show
    "Biliyorum, her şey böyle kalmayacak."  
    "Biliyorum, bir şeyler olacak."  
    "Biliyorum, bunun burada bitmesi mümkün değil."  
    "Ama o zamana kadar, olacakları olduğu gibi kabul edeceğim. Henüz gerçekleşmemiş bir şey için endişelenmenin bir anlamı yok."  
    "Başka bir deyişle, artık biraz rahatlama zamanı."
    
    
    window hide
    show black with Dissolve(2.0)
    window show
    "Natsuki ve babasıyla ilgili durumu öğrendiğimden bu yana biraz zaman geçti. Görünüşe göre, düşündüğümden daha kolay kabullenebiliyormuşum."  
    "Aslında, bugünü heyecanla bekliyordum."  
    n "[player]! Uyan artık!"  
    scene bg bedroom with open_eyes  
    play music aNewDay fadein 2.0  
    mc "Uyandım, uyandım."  
    show natsuki 1bd at f11  
    n "Güzel! Mutlu Sevgililer Günü!"  
    "Natsuki, elinde tuttuğu bir tepsiyi bana doğru itiyor. Üzerinde bir sürü ev yapımı çikolata var."  
    mc "Teşekkür ederim, Natsuki."  
    "Çikolataların her biri farklı bir şekilde yapılmış. Sanki hepsi özel olarak düşünülmüş gibi. Bir tanesini alıp ısırıyorum ve uzun zamandır yediğim en iyi çikolatayı tattığımı hissediyorum."  
    mc "Vay, bu harika olmuş! Gerçekten güzel iş çıkarmışsın."  
    n 1bh "Şey... Elimden geleni yaptım."  
    "Natsuki, bir şey söylemeye çalışıyor gibi görünüyor."  
    n 1bq "Şey, şey... Yani..."  
    mc "Evet?"  
    n "Bugün Sevgililer Günü olduğuna göre... şey, bir randevuya falan gitmemiz gerekmiyor mu?"  
    mc "Tabii ki, neden olmasın?"  
    n 1bb "Tabii ki gitmeliyiz!"  
    n 1bc "Ama... nereye gideceğimiz hakkında hiç düşünmedim."  
    mc "Güzel soru."  
    "Bir süre sessizlik oluyor, ikimiz de nereye gideceğimizi bilemiyoruz."  
    mc "Hani bazen piknik yaptığımız o yer var ya? Orada bir göl var. Gayet güzel bir yer."  
    n 1bq "Evet, orayı hatırlıyorum."  
    n "Şey... O zaman hazırlanıp seni bekleyeceğim."  
    hide natsuki with wipeleft  

    stop music fadeout 2.0  
    window hide  
    show black with Dissolve(2.0)  
    window show  
    scene bg home_interior_night with Dissolve(2.0)  
    "Günümüzü her zamanki gibi geçiriyoruz, ta ki akşam olup dışarı çıkma vakti gelene kadar."  
    mc "Ben hazırım. Ya sen, Natsuki?"  
    show natsuki 1ba at f11  
    n "Ben de hazırım. Hadi gidelim mi artık?"  
    mc "Evet, çıkalım."  
    hide natsuki  
    scene bg residential_night with wipeleft_scene  
    pause(1.5)  
    scene bg park_night with wipeleft_scene  
    play music NatTheme fadein 2.0  
    "Kapıdan çıkar çıkmaz gecenin soğuk havasıyla karşılaşıyoruz. Hafif bir rüzgâr da esiyor. Ardından, aklıma gelen yere doğru ilerliyoruz."  
    "Vardığımızda, son anda aklıma gelen bu mekânın aslında kötü bir seçim olmadığını fark ediyoruz."  
    "Su muhteşem görünüyor. Ay, gölün üzerine parlak bir ışık saçıyor. Saat kaç olursa olsun, gölün yüzeyinde yankılanan bu ışık gerçekten etkileyici."  
    "İkimiz de göl kenarına oturuyor, birbirimize sarılarak ay ışığını izliyoruz."  
    mc "Burası gerçekten çok güzel."  
    mc "Ama senin kadar güzel değil, tabii ki."  
    show natsuki 5bq at f11  
    "Natsuki bana hayal kırıklığı içinde bakıyor."  
    n "Bu sadece klişe bir laf arayışı."  
    "Haksız da sayılmaz aslında."  
    mc "Belki öyle, ama doğru olduğu gerçeğini değiştirmez, değil mi?"  
    n 4bj "Pekâlâ, iltifatı kabul ediyorum."  
    n "Şikâyet ettiğime bakma, hissettiklerim sadece bundan ibaret değil. Bunu zaten biliyorsun."  
    n "Ayrıca o kadar da ciddi bir şikâyet değildi."  
    show natsuki 1ba  
    "Natsuki hafifçe gülümsüyor. Bunu kabul ederim."  
    n "Ama hava epey soğuk."  
    "Natsuki, kollarını tamamen bana doluyor."  
    mc "Evet, kusura bakma. Keşke bir battaniye getirseydim ya da biraz daha erken gelseydik."  
    n 1bb "Artık yapacak bir şey yok."  
    n 1bt "O zaman beni ısıtmak zorundasın, ceza olarak!"  
    mc "Natsuki, ben de üşüyorum. Bu şekilde pek ısınamazsın."  
    mc "Bana sarılmak için bahane arıyorsun, değil mi?"  
    n 1bq "H-Hayır! Öyle bir şey yok!"  
    "Gülümsüyorum."  
    mc "Her ne dersen de, Natsuki."  
    "Birkaç dakika boyunca öylece kalıyoruz, ta ki aklıma bir şey gelene kadar."  
    mc "Hey, Natsuki."  
    n 1bb "Ne var? Isınmaya odaklanmaya çalışıyorum."  
    show natsuki 1ba at f11  
    mc "Evet, evet, tabii. Neyse, yaptığın çikolatalar gerçekten harikaydı."  
    mc "Ama bir şeyi hatırlattı bana."  
    mc "İlk kez markete birlikte gittiğimiz zamanı hatırlıyor musun?"  
    n 1bb "O kadar zaman geçti ki, [player]. Şu an buradayken eski buluşmalarımızı düşünmek zorunda değilsin."  
    mc "Biliyorum, ama {i}neden{/i} markete gittiğimizi düşündüm."  
    n "Muhtemelen yemek almak içindir. İnsanlar genelde bu yüzden markete gider."  
    mc "Ama cupcake malzemeleri almıştık, değil mi?"  
    mc "Sana kimin ya da ne için olduğunu sorduğumda, yakında öğreneceğimi söylemiştin."  
    mc "Ama sanırım asla gerçekten öğrenemedim."  
    n 1bq "Ah, o şey mi?"  
    "Natsuki biraz utanmış gibi görünüyor."  
    n "Bunu zaten anlamadın mı?"  
    n "Bence yeterince açıktı."  
    n 1be "Beni bilerek 'aptal' demeye zorluyorsun, değil mi?"  
    n "Bunu genelde ciddi söylemediğimi zaten biliyorsun. Ama neden hoşuna gidiyor anlamıyorum."  
    "Bekle, genelde mi?"  
    mc "Gerçekten bilmiyorum. Öyle şeyleri varsaymayı pek sevmem."  
    n "Beni bunu söylemeye zorlayacaksın, değil mi?"  
    n 1bq "Eğer bu seni mutlu edecekse… Onları senin için yapacaktım, aptal."  
    mc "Ahh."  
    "Şimdi düşününce, bunu çok daha önce anlamam gerekirdi."  
    mc "Peki neden hiç bana vermedin?"  
    n 1bc "Cidden unuttun mu? Şu 'berbat bir ev hayatı insanın başkaları için bir şey yapma isteğini öldürüyor' meselesi?"  
    "Gah, ben gerçekten aptalım."  
    mc "Ah! Çok üzgünüm, bunu açmak istememiştim."  
    n 1bb "Evet, evet, artık alıştım."  
    n "Eskiden bazen garip şeyler söylediğini düşünürdüm, ama şimdi genel olarak tuhaf olduğunu düşünmeye başlıyorum."  
    mc "Bu ne anlama geliyor şimdi?"  
    n "Daha önce de söylediğim gibi, bu kötü bir şey değil."  
    show natsuki 1ba at t11  
    "Natsuki kollarını benden çekip tekrar göle bakıyor."  
    n 1ba "En azından buluşma mekanlarını seçme konusunda fena değilsin."  
    mc "Eh, biraz pratik yapma şansım oldu sonuçta."  
    "..."  
    n "[player]."  
    mc "Evet?"  
    n 1bb "Seni hiç tanımasaydım hayatım nasıl olurdu diye merak ediyorum."  
    n "Aslında, bunu düşünmek istemiyorum. Ama kötü olacağını biliyorum."  
    "Gerçekten düşündüğümde, Natsuki haklı."  
    "Eğer beni hiç tanımasaydı, babası onu dövdüğünde kalacak bir yeri olmazdı ve sonrası nasıl olurdu, düşünmek bile istemiyorum."  
    "Diğer kulüp üyelerinden birine kalacak yer isteyecek cesareti olur muydu?"  
    "Sanırım artık bunun bir önemi yok."  
    mc "Seninle birlikte olduğum için gerçekten mutluyum."  
    mc "Bunu bininci kez söylersem sinir olur musun? Belki olursun ama bu hiçbir şeyi değiştirmez."  
    n "Hâlâ neden benimle çıktığını anlayamıyorum."  
    n "Ama inkar edemem ki seninle harika vakit geçirdim."  
    n 1bq "Hatta muhteşem bir vakit. Eğer bu seni daha iyi hissettirecekse ya da bir şey..."  
    mc "Güzel bir şey söylediğinde cümlenin sonuna 'ya da bir şey' ya da 'sanırım' eklemen çok tatlı geliyor bana."  
    n 1bb "Şey, bil bakalım ne var?"  
    n 1bi "..."

    "Buna Natsuki'nin bile bir cevabı yok gibi görünüyor."
    menu:
        "Sessizliği bozmak için yeni bir konu açmak kötü bir fikir olmazdı, değil mi?"
        "Ona en sevdiği randevuyu sor.":
            $ askAboutDate = True
            mc "Bu arada, Natsuki, en sevdiğin randevumuz hangisiydi?"
            n 1bb "Huh? Açıkçası hiç düşünmemiştim."
            n "Hepsi gayet güzel bence."
            mc "Evet, ben de hepsinden keyif aldım."
            mc "Ama insan merak ediyor, 'mükemmel randevu' nasıl olurdu acaba?"
            n "Bununla ilgili bir fikrim olabilir."
            mc "Cidden mi?"
            n "Belki sonra. Uzun zamandır yapmak istediğim bir şey ama bakalım."
            "Bu da ne demek şimdi? Neyse, sonra anlarız."
        "Nasıl olduğunu sor.":
            mc "Nasılsın, Natsuki? Genel olarak?"
            mc "Sonuçta ben senin erkek arkadaşınım, iyi olup olmadığını bilmem lazım."
            n 1bb "İyiyim, sanırım."
            n "Bazen stresli oluyorum, malum sebeplerden, ama sen yanımdayken o kadar kötü gelmiyor."
            mc "Yardımcı olabildiğime sevindim. Seni mutlu etmek için her şeyi yaparım."
            n "Teşekkürler, [player]. Seninle birlikte olmaktan mutluyum."
            n 1bq "Başından beri senden hoşlanıyordum aslında, bunu itiraf etmek benim için biraz garip olsa da."
            n "Bunu daha önce de söyledim ama ancak şimdi tam anlamıyla fark ediyorum."
        "Hiçbir şey söyleme.":
            "Aslında hiçbir şey söylememe gerek yok, çünkü içinde bulunduğumuz an zaten her şeyi anlatıyor."
            "Natsuki'yle böylece oturmaya devam ediyoruz, çünkü bazen kelimelere ihtiyaç duymadan da her şeyi hissedebiliyorsun."
    hide natsuki
    stop music fadeout 2.0
    scene bg park_night with wipeleft_scene
    "Ve gece böylece devam ediyor, ta ki telefonuma bakıp saatin ne kadar geç olduğunu fark edene kadar."
    mc "Bunu söylemek istemem ama sanırım eve dönmemiz lazım."
    play music NextToYou fadein 2.0
    "Natsuki gözlerimin içine bakıyor."
    show natsuki 4bs at t11
    n "Gerçekten mi?"
    "Ben de ona bakıyorum."
    mc "Biraz daha kalabiliriz, sanırım."
    "Tamam, şu an gerçekten romantik bir an yaşıyoruz. Sakın biri gelip bozmasın, lütfen."
    "Hatta bunu düşünmeyi bile bırakıyorum. Sadece anın tadını çıkaracağım ve kimse bunu mahvedemeyecek."
    "..."
    "AH! Doğru ya, Natsuki hâlâ burada."
    n 4bq "Güzel."
    mc "Seninle vakit geçirmek için her zaman zaman ayırabilirim, biliyorsun."
    n "Bunu duymak beni mutlu ediyor."
    show natsuki 1bh at face_one(y=200) with dissolve_cg 
    "Yüzlerimiz birbirine daha da yaklaşıyor."
    mc "Seni çok seviyorum, Natsuki."
    show natsuki 1bh at face_two(y=335) with dissolve_cg 
    
    n "Ben de seni seviyorum, [player]."
    "Yavaşça bana doğru eğiliyor. Yüzlerimiz neredeyse birleşmek üzere..."
    "B-Bu gerçekten oluyor mu?" 
    "Tam o anda duruyor." 
    
    if askAboutDate is True:
        n "Bu arada, az önce bahsettiğim şey var ya... Sana bir şey sormam lazım."
        n "Hiç öpüştün mü?"
    else:
        n "Bu zamana kadar kaç kere öpüldün?"
    mc "Şu an itibarıyla? Hiç."
    mc "Ya sen?"
    n "Aynı şekilde."
    
    "Aramızdaki mesafe neredeyse yok gibi artık."
    "Natsuki'nin yanakları kızarıyor."
    n "Bunu değiştirmek ister misin?"
    mc "Bence neden olmasın?"
    show black with close_eyes
    "Ve sonunda, yüzlerimiz tamamen birleşiyor. Öpüşüyoruz. Ne bizi durduracak biri var, ne de bu anı mahvedecek bir şey."
    "Ve bu, gerçekten harika hissettiriyor."
    "Her an bir şey olacakmış gibi hissediyorum ama olmuyor. Tek hissettiğim şey saf mutluluk."
    "Öpüşmemiz bittiğinde, ikimiz de şaşkınlıkla birbirimize bakıyoruz."
    scene bg park_night 
    show natsuki 1bn at face_three(y=600) with open_eyes
    n "Gerçekten mi..?"
    mc "Sanırım evet."
    n "Tamam, sadece emin olmak istedim."
    n "Bunu daha sık yapmalıyız."
    n 1bs "Hoşuma gitti."
    "Natsuki'nin yanakları hala kıpkırmızı ve bunu gizlemeye çalışıyor ama pek başarılı olamıyor."
    mc "Aynı fikirdeyim."
    "Açıkçası, ne diyeceğimi tam olarak bilemedim ama boşver."
    "İlk öpücüğüm mükemmeldi. Bugün gerçekten güzel bir gündü."

    
    stop music fadeout 2.0
    hide natsuki with dissolve_cg
    window hide
    show black with Dissolve(2.0)
    window show
    
    "Zaman geçti. Hem de çok, çok fazla zaman."
    n "Uyan artık! Bugünün ne günü olduğunu bilmiyor musun?"
    scene bg bedroom with open_eyes
    play music aNewDay fadein 2.0
    "Henüz tam uyanamamış halde doğrulmaya çalışıyorum."
    mc "Sanırım?"
    show natsuki 5c at f11
    n "Yani, hiçbir fikrin yok."
    mc "Öyle demedim!"
    mc "Ama haklısın, pek hatırlamıyorum."
    n 4b "Senin hiçbir şeyi aklında tutamadığını düşününce pek şaşırmadım. Neyse ki ben iyiyim bu konuda."
    mc "Bugün ne günü, hala bilmiyorum."
    n "Altı ay oldu işte, biz çıkmaya başlayalı!"
    "Kaşlarımı kaldırıyorum."
    mc "Şimdiden mi?"
    n 1b "Evet! Ama o kadar uzun zaman geçmiş gibi gelmiyor."
    mc "Aynen."
    mc "... "
    mc "Yani, gerçekten altı ay oldu, değil mi?"
    n 2c "Evet."
    n 5b "Bir haftadan uzun süredir sevgilin olduğuna şaşırmış olabilirsin ama ben seni bırakmam, biliyorsun."
    mc "O zaman bu akşam kutlamamız mı gerekiyor?"
    n "Aferin, öğreniyorsun."
    n "Gerçi biraz zaman aldı."
    mc "Çabalıyorum işte."
    n "Öyle mi dersin?"
    mc "Çok komiksin, Natsuki. Ayrıntıları sonra düşünürüm ama şu an uykuluyum."
    n 1a "Her zaman uykuluyorsun. Ayrıca okula gitmemiz gerekiyor."
    mc "Evet, evet."
    hide natsuki with dissolve_cg
    scene bg club_day with wipeleft_scene
    show natsuki 1a at f11
    "Okulun her zamanki gibi sıkıcı olduğunu söylemek gereksiz olurdu. Ama tabii ki Edebiyat Kulübü’ne gittik."
    show natsuki 1a at t21
    show sayori 4r at f22
    "El ele tutuşarak içeri girerken Sayori bizi karşılıyor."
    s "Siz bugün çok mutlu görünüyorsunuz!"
    show natsuki 1a at t31
    show sayori 4a at t32
    show monika 1b at f33
    m "Zaten hep mutlu görünüyorlar, Sayori."
    m 5a "Tabii, bu kötü bir şey değil~"
    mc "Yani, bugün çıkmaya başlayalı altı ay oldu da..."
    show natsuki 1a at t41
    show sayori 4a at t42
    show monika 1a at t43
    show yuri 4b at f44
    "Yuri, okuduğu kitaptan başını kaldırıyor."
    y "Tebrikler."
    mc "Ah, o kadar da büyük bir olay değil aslında."
    hide yuri with wipeleft
    show natsuki 4e at f31
    show sayori 4a at t32
    show monika 1a at t33
    "Natsuki, bana hayal kırıklığına uğramış gibi bakıyor."
    n "Bence büyük bir olay."
    n 3t "Sonuçta [player] bir hafta boyunca sevgiliyi elde tutabildi, bu bile etkileyici!"
    mc "Evet, Natsuki, bunu evde de söyledin."
    n 3c "Şaka mı yapmıştım yani?"
    "Lanet olsun, Natsuki."
    show natsuki 3a at t31
    show sayori 4c at f32
    show monika 1a at t33
    s "Neyse, bence harika bir şey bu. İkinizi de tebrik ederim!"
    show natsuki 3a at t31
    show sayori 4c at t32
    show monika 4b at f33
    m "İlk tanıştığınız günü hatırlıyorum."
    m "Böyle olacağını tahmin etmiştim, açıkçası."
    mc "Gerçekten mi Monika? O zamanlar birbirimizden hoşlandığımız bu kadar belli miydi?"
    show natsuki 3a at t31
    show sayori 4x at f32
    show monika 4b at t33
    s "Kesinlikle belliydi."
    "Huh."
    mc "Neyse, biz biraz manga okuyacağız."
    show natsuki 3a at t31
    show sayori 4x at t32
    show monika 5a at f33
    m "Anladım. İyi eğlenceler!"
    hide sayori with dissolve_cg
    hide monika with dissolve_cg
    hide natsuki with dissolve_cg
    stop music fadeout 2.0
    window hide
    
    scene bg residential_day with wipeleft_scene
    window show
    
    show natsuki 1a at f11
    
    "Her şey olup bittikten sonra, Natsuki ve ben eve doğru yola koyulduk. Evime yaklaştığımızda, çalıların arasından hızla geçen uzun bir silüet fark ettim."
    show natsuki 4u at f11
    "En azından çalıların arasından hızla geçmeye çalıştı. Gözlerimizin üzerinde olduğunu fark edince durdu."
    "Biraz daha ilerledi, öyle ki artık kim olduğunu görebiliyorduk: Natsuki’nin babası."
    "Daha önce onu Natsuki ile beraberken birkaç kez görmüştüm, ama bizimle pek ilgilenmemişti."
    "Natsuki ona her seferinde sert bir bakış atardı ve bu da düşüncelerini yeterince açık şekilde ifade ediyordu."
    "Ama bu sefer, elinde bir şey fark ettim. Yumruğunu sıkıyordu ve bu hiç de iyiye işaret değildi."
    "Aslında, oldukça kötü bir işaretti ama bunu söylememe bile gerek yok. Şu an biraz panikliyorum."
    menu:
        "Peki, şimdi bana yumruk mu atacak? Ölecek miyim yoksa?"
        "Onunla yüzleş!":
            $ confrontDad = True
            "Bundan sonsuza kadar kaçamam."
            mc "Hey, sen! Ne yapıyorsun orada?"
            "Ama bu pek bir şey değiştirmedi, çünkü o zaten kaçmaya başladı."
            n 1b "Onun peşinden gitmeyeceksin, değil mi?"
            mc "Sanırım onu kovalamamın pek anlamı yok. Açıkça konuşmak istemiyor."
            "Bu da iyi, çünkü en azından sağlığım açısından daha faydalı oluyor—ölmemiş oluyorum."
            n 1u "Evet."
            scene bg house_entrance with wipeleft_scene
            pause(1.5)
            scene bg home_interior with wipeleft_scene
            "Pekâlâ, o zaman eve girelim bari. Ön kapıdan içeri girip derin bir nefes alarak oturma odasındaki kanepeye oturdum."
        "Kaç!":
            scene bg house_entrance with wipeleft_scene
            pause(1.5)
            scene bg home_interior with wipeleft_scene
            "Neyse ki biraz daha uzun yaşayabileceğim. Natsuki ile birlikte aceleyle eve girip kapıyı hızla arkamdan kapattım."
    mc "Baban biraz, şey... sana da öyle geldi mi?"
    n 1b "Öfkeli mi?"
    mc "Evet, sanırım bu doğru bir kelime."
    mc "Bu konuda ne yapmam gerektiğini pek bilmiyorum."
    n 3b "Seni gerçekten öldürecek falan değil, [player]."
    mc "Biliyorum ama..."
    n 4b "Ama'sı yok."
    "Şu an durum biraz gergin."
    n 1c "Ayrıca, bugün özel bir gün."
    n "Beni bir randevuya çıkarman gerekmiyor mu? Sonuçta çıkıyor olmamızın amacı bu değil mi?"
    mc "Tabii ki."
    mc "Bir şeyler mi yiyelim?"
    n 1b "Ama geçen seferki gibi kazık atan bir yer olmasın."
    mc "O zaman fast food alalım."

    play music NatTheme fadein 2.0
    "Çoğu insan için fast food restoranına gitmek romantik sayılmaz."
    "Pardon, düzelteyim. {i}Kimse{/i} için fast food restoranına gitmek romantik sayılmaz. Neyse ki Natsuki, sıradan biri değildi."
    hide natsuki with wipeleft
    
    
    scene bg fastfood with wipeleft_scene
    mc "Evet, geldik."
    "Restorana giriyoruz."
    "Burası modern bir atmosfere sahip, ama buranın hala bir fast food restoranı olduğu gerçeğini gizlemiyor. Ve bizim bir randevu için fast food restoranına geldiğimiz gerçeğini de..."
    show natsuki 1a at s11
    "Siparişlerimizi verdikten sonra boş bir masaya geçip yan yana oturuyoruz."
    mc "Biliyorum, burası randevu için biraz garip gelebilir ama daha önce de buraya gelmiştik, değil mi?"
    n 1b "Evet. Bence bu konuda endişelenmene gerek yok, [player]. Benim için önemli olan rahat hissetmek. Aşırı romantik bir yer olmasına gerek yok. Ve burası benim için rahatlatıcı, yani..."
    "Bir süre sonra siparişlerimiz geliyor. Natsuki hamburgerinin kağıdını açarken bir şey hakkında kararsız gibi görünüyor."
    mc "Bir şey mi oldu?"
    n 1s "Aslında... denemek istediğim bir şey var."
    mc "Hımm?"
    "Suyumdan bir yudum almaya başlıyorum."
    stop music
    play music EarlyBird
    n "Şey..."
    menu:
        n "B-Beni besler misin?"
        "İçtiğin suyu püskürt":
            mc "N-N-Ne?! Natsu--"
        "İçtiğin suyu püskürt":
            mc "N-N-Ne?! Natsu--"
        "İçtiğin suyu püskürt":
            mc "N-N-Ne?! Natsu--"
    n 4q "Sadece meraktan sordum, tamam mı!"
    n "Bunu yapan çiftleri çok gördüm ve..."
    mc "Dur bir dakika. Yani istiyorsun ki... ben seni besleyeyim?"
    n 5e "Bunu bir daha söyletme bana!"
    "Yalan söyleyemem, ben de nasıl bir his olacağını biraz merak etmiyor değilim."
    mc "Pekâlâ, tamam o zaman."
    hide natsuki with wipeleft
    "Kalkıp çatal almak için mutfak alanına gidiyorum, sonra tekrar oturuyorum."
    show natsuki 5s at d11
    mc "Yani, Natsuki, gerçekten yapıyoruz bunu?"
    n 5s "Dedim ya, insanın en az bir kere yapması gereken şeylerden biri bu."
    "Kim demiş?"
    mc "Tamam, yani çatalı alıp hamburgerin içine batırıyorum, öyle mi?"
    n 4b "Sanırım? Ama sen hamburgeri çatalla mı yiyorsun?"
    mc "Bu bir yaşam tarzı, Natsuki."
    mc "Neyse, şimdi ağzını açıyorsun."
    n 4w "Aslında... vazgeçtim."
    mc "Ne?!"
    n 4q "Çok utanç verici."
    mc "Natsuki, şu an bir fast food restoranındayız. Kimse bizi umursamayacak."
    mc "Tamam, kabul ediyorum, birini hamburgerle beslemek romantizm açısından pek ideal değil. Aslında, kimse bunu yapmaz."
    mc "Şimdi düşününce, belki de insanlar bize garip garip bakabilir."
    mc "Ama yine de! Çatal almak için kalkıp gittim..."
    mc "Harcadığım on saniyeyi boşa harcamak istemezsin, değil mi?"
    "Bence söylediklerim gayet ikna edici."
    n "Peki, tamam!"
    show natsuki 1w at f11
    "Natsuki ağzını açıyor, ben de çatalı ona uzatıyorum. Isırıyor ve hızla çiğnemeye başlıyor, tamamen utanç içinde."
    show natsuki 1s at t11
    mc "Ee, nasıl?"
    "Yutkunuyor, sonra cevap vermek için kelimeleri toparlamaya çalışıyor."
    n 1q "...Bu bir şeydi."
    n "Evet, kesinlikle bir şeydi."
    mc "Bari ikimiz de aynı fikirdeyiz."
    n 4b "Aynı fikirde olacağımız bir başka konu da, bunu bir daha yapmamak olabilir mi? En azından fast food restoranında?"
    mc "Tabii, zaten tekrar yapmayı düşünmüyordum."
    n 4q "Ş-Şimdilik en azından."
    mc "Aynen."
    "Garipti."
    hide natsuki with wipeleft
    window hide
    stop music fadeout 2.0

    
    window show
    "...Ve böylece yemeğimizi bitirip restorandan ayrılıyoruz."
    scene bg residential_night with wipeleft
    pause(1.5)
    scene bg home_interior_night with wipeleft
    "Eve döndüğümüzde her şey normale dönüyor. Yani, 'her şey {i}sanki{/i} normale dönmüş gibi oldu' demiyorum, gerçekten de Natsuki’nin babasını bir an bile düşünmedik."
    "Ya da... düşündük ama bunun aklımızda olduğunu kendimize bile itiraf etmek istemedik."
    "Gecenin geri kalanı gayet sakin geçiyor. En azından başka bir olay yaşanmadı. Ama yarın mı? O kadar huzurlu geçeceğini sanmıyorum."
    "Neden bilmiyorum ama sanki bir şey olacakmış gibi hissediyorum."
    window hide

    
    
    
        show black with Dissolve(2.0)
    window show
    scene bg flashback_home with Dissolve(2.0)
    $ o_name = "???"
    n "Artık bıktım bundan."
    o "Şimdi sırası değil, Natsuki."
    n "Şimdi değil mi? Peki ne zaman?"
    n "Daha ne kadar ertelenecek bu?"
    o "Ciddiyim. Bunu sonra konuşacağız."
    n "Sonra mı? Hep \"sonra konuşuruz\" diyorsun ama hiçbir şey değişmiyor!"
    n "Ben böyle yaşamaya devam etmek istemiyorum, ve sanırım sen de istemiyorsun."
    o "Odana git, Natsuki. Bu konuyu sonra konuşacağız. Konu kapanmıştır!"
    n "Hayır! Bir şeyler yapmalıyız!"
    n "Bunu yapmamın sebebi hâlâ seni umursamam."
    n "Eskisi gibi olabilmek için neler vermezdim..."
    o "Ama bu o kadar kolay değil!"
    o "Hiçbiri kolay değil."
    o "Bunu anlamıyor musun, Natsuki?"
    n "Anlıyorum ama bu hiçbir şeyi değiştirmiyor."
    o "Sana odana git dedim."
    o "Kaç kere söylemem gerekiyor?"
    o "Git."
    n "Gitmeyeceğim."
    o "Git dedim."
    n "Bunu çözmek zorundayız."
    o "Git."
    n "Asla."
    o "{i}GİT DEDİM!{/i}"
    n "{i}HAYIR!{/i}"
    n "{i}Sen en azından değişmeye çalışana kadar hayır!{/i}"
    n "{i}Daha iyi bir hayatımız olana kadar hayır!{/i}"
    o "Sen..."
    o "Hiç mi anlamayacaksın?!"
    n "Hayır. Asıl anlamayan sensin."
    n "Asla anlamadın."
    o "{i}YETER ARTIK!{/i}"
    o "{i}NATSUKİİİ!{/i}"
    "..."
    "..."
    "..."
    "..."
    "..."
    o "Ah... Sevgili Itsuko'm..."
    o "Keşke hâlâ bizimle olsaydın, bunu ne kadar isterdim bir bilsen..."
    window hide
    show black with Dissolve(2.0)
    window show
    
    scene bg house_entrance_night 
    o "Bilmiyorum... Gerçekten ne yapacağımı bilmiyorum."
    play music Dusk fadein 2.0
    "Olduğum yerde donup kalıyorum."
    "Bu {i}o.{/i}"
    "Natsuki’yle yıl dönümümüzün ertesi gecesiydi. O çoktan yatağa geçmişti, ben de birazdan yanına gidecektim ki kapıya birinin vurduğunu duydum."
    "Kapıyı açmak için gittim ve işte oradaydı. Natsuki’nin babasıyla burun buruna gelmiştim—hem de bu sefer tamamen yalnızdım."
    "En son kaldığım yerden devam edecek olursam..."
    $ d_name = "Nat’ın Babası"
    d "Gerçekten ne yapacağımı bilmiyorum."
    mc "Uh, merhaba. Şey..."
    "Şu an ne yapmam gerektiği hakkında hiçbir fikrim yok."
    scene bg home_interior_night with wipeleft_scene
    mc "Şey, yani... Uh..."
    "Salonun kanepesine kendini bırakıyor."
    d "Umarım sakıncası yoktur."
    "Zaten bunu engelleyebilecek bir konumda değilim."
    mc "Buraya neden geldiniz? D-Dün biraz üzgün görünüyordunuz."
    if confrontDad is True:
        d "Hı? Ah, o mesele mi? Sen benimle konuşmaya çalışırken çekip gitmem için kusura bakma ama o an hiçbir şey hakkında konuşacak havada değildim. Sonuçta üzgündüm."
        d "Ama dünkü olayın şu an sormak istediğim şeyle bir ilgisi yok."
    else:
        d "Hı? Üzgündüm, evet, ama şu an sormam gereken şeyle ilgisi yok."
    d "Bildiğim kadarıyla Natsuki bir süredir seninle yaşıyor, doğru mu?"
    mc "E-Evet."
    d "Yani altı aydır."
    "Yüzüne acı dolu bir ifade yerleşiyor."
    d "Seni eleştirmeye, hayatına karışmaya gelmedim."
    d "Zaten kendi kızıma bile yol gösterecek bir hakkım kaldığını sanmıyorum."
    d "Ama her şeyin nasıl olduğunu kendi gözlerimle görmek istedim."
    "Tam o sırada odamın kapısının açıldığını duyuyorum."
    n "[player]? Kim var orada? Sanırım sesi tanıyorum."
    mc "Kimse değil, Natsuki!"
    "Bu, uydurabileceğim en kötü yalandı. Hayır, düzeltiyorum—tarihte söylenmiş en kötü yalan. Şu an hiç de formda olmadığım çok belli."
    d "Erkek arkadaşınla konuşuyorum."
    
    "Bunu duyar duymaz Natsuki kapıyı hızla kapatıyor. Sanırım bir sorunu çözmüş oldum?"
    "Ha, ben ne saçmalıyorum? Şu an içim içime sığmıyor panikten ve az önce belki de tarihin en kötü çözümünü ürettim. Bunu burada, şimdi mi konuşacağız gerçekten?"
    mc "Bunu konuşmak için daha uygun bir yer yok mu?"
    d "Bu saatten sonra değişen bir şey olmaz."
    "İç çekiyorum ve başka bir soru soruyorum."
    mc "Bizi birlikte dışarıda gördüğünüz zamanlar oldu. Ama o zamanlarda sadece bir kere bana soru sormaktan başka bir şey yapmadınız. Neden?"
    "Gözlerini hafifçe yana çeviriyor."
    d "Sanırım baştan kabullendim."
    d "Kızım benimle yaşamak istemiyordu artık. Bütün bağları kopardı."
    d "Bunu fark etmek acı verici ama başka ne yapabilirdim?"
    d "Sen de ben de biliyoruz ki ne olursa olsun geri dönmezdi."
    d "Özellikle de sizin yanınıza, öyle ortada çıkıp gelirsem hiç."
    d "Sıkışıp kaldım. Bitti. O artık yok."
    "Bu noktada onunla konuşmak konusunda biraz daha rahat hissediyorum. Kısmen de olsa."
    "En azından beni öldürmeyeceğini anlamış oldum, bu da bir şeydir."
    "Tam anlamıyla rahat değilim ama biraz daha iyi hissettiriyor."
    mc "Özetlemek gerekirse, evet."
    d "Ne büyük bir kayıp."
    "Beklediğimin aksine, sesinde en ufak bir öfke yok. Sadece pişmanlık."
    mc "Oldukça sakin görünüyorsunuz."
    stop music fadeout 2.0
    play music Dawn fadein 2.0
    d "Tabii ki. Dediğim gibi, kabullendim."
    d "Öfkelenebileceğim tek kişi kendimim."
    d "Bunun tamamen benim hatam olduğunu biliyorum."
    d "Hayatımın en büyük hatasını yaptığımı biliyorum."
    d "Zaten her şey olmadan önce bile kendimden nefret ediyordum."
    d "Ama Natsuki gittiğinden beri daha da kötüleştim."
    d "Her geçen gün kendimden biraz daha nefret ettim."
    d "Nasıl olup da kendimi kaybedebildiğimi düşündüm."
    d "Nasıl olup da kendi karıma verdiğim bir sözü bozabildiğimi..."
    "Bir an duraksıyor."
    d "Ama bunları dinlemek isteyeceğini sanmıyorum."  
    d "Ve anlıyorum."  
    d "Beni berbat bir ebeveyn olarak gördüğünü biliyorum."  
    d "Senden sempati beklediğim falan yok."  
    "İyi, çünkü ona verecek değildim zaten."  
    "Ama en azından sonunda biraz daha konuşacak cesareti kendimde buluyorum."  
    mc "Yaptıklarının korkunç olduğunu kabul etmen, onları daha az korkunç yapmaz."  
    "Bunu söyleyerek fazla ileri gitmiş olabileceğimi düşündüm ama Natsuki’nin babası derin bir nefes alıp konuşmaya devam etti, hem de şaşırtıcı bir şekilde hala sakin."  
    d "Farkındayım."  
    d "Ne yaparsam yapayım, yaptıklarımı telafi edemem."  
    d "İnan bana, bunu inkâr etmeye çalışmıyorum."  
    d "Sadece bundan sonra ne yapacağımı düşünmeye çalışıyorum."  
    "Yine sustu, bu sefer daha uzun bir süre."  
    d "Natsuki muhtemelen sana insanlardan nasıl uzaklaştığımı anlatmıştır, değil mi?"  
    mc "Evet, anlattı."  
    d "Evet... eşimi kaybettikten sonra..."  
    "Yanaklarından bir damla yaş süzüldüğünü fark ettim. Tekrar duraksadı."  
    d "Özür dilerim. Sadece... onu kaybettikten sonra tamamen içime kapandım."  
    d "Natsuki’ye bir şekilde bakmaya çalıştım ama asla yeterince yapamadım. Maddi durumumuz ne olursa olsun, çok daha fazlasını yapabilirdim."  
    d "Ona çok daha fazla ilgi gösterebilirdim."  
    d "Bu kadar zayıf olmasının bir sebebi var, biliyorsun."  
    d "Neyse... demek istediğim şu ki, kimse benim gibi bir ebeveyn tarafından büyütülmeyi hak etmiyor."  
    d "Kimse, çocuğuna tam anlamıyla ilgi göstermeyen biri tarafından büyütülmemeli."  
    "Bir damla daha süzüldü yanağından. Sonra bir tane daha... ve bir tane daha. Durmaksızın akıyordu artık."  
    d "Bu gerçekten korkunç bir durum. Şimdi her şeyimi kaybettim."  
    d "Natsuki doğduğunda, eğer o zamanki halime bir gün gelip ona... {i}bunu{/i} yapacağımı söyleseydin, muhtemelen kendimi bile kaldıramazdım."  
    d "Ama bu da bencilce, değil mi? Kızımın yanında olmak istedim, ne olursa olsun."  
    d "Ama yapamadım. Bunun bahanesi yok."  
    "Şimdi hıçkıra hıçkıra ağlıyordu, elleriyle yüzünü kapatmıştı."  
    mc "Wow, ben..."  
    d "Seni buna dahil ettiğim için üzgünüm. Hiç de kabul edilebilir bir şey değil, böyle pat diye evine dalmak."  
    d "Keşke birçok şeyi geri alabilseydim ama... birine içimi dökmeye ihtiyacım vardı."  
    "Öylece oturduk, ne diyeceğimizi bilemeden. Uzunca bir sessizliğin ardından tekrar konuştu."  
    d "Ben Natsuki için yaşıyordum, biliyor musun?"  
    d "Eşim gittikten sonra her şey daha da kötüleşti. Bir noktada işimi kaybettim... Sanırım bunu Natsuki'ye hiç söylemedim ama muhtemelen anlamıştır."  
    d "Zar zor geçinecek kadar para bulabiliyordum, ama o da ayrı bir mesele."  
    d "Natsuki elimde kalan tek şeydi."  
    d "Böyle yaşamak tam anlamıyla işkenceydi. Bu, yaptıklarımı asla haklı çıkarmaz ama yataktan çıkmak bile bazen imkansız gibi geliyordu."  
    d "Ona bu kadar katı davranmamın en büyük sebebi, benim yaşadığım hayatı yaşamasını istemememdi. Ama bu katılığım da yanlış yönlendirilmişti."  
    d "Bunu defalarca söyledim, hayatım berbattı. Ama..."  
    d "En azından hâlâ bir kızım vardı."  
    d "Ama çok tartışırdık."  
    d "Çoğu zaman benim bir ebeveyn olarak ne kadar yetersiz olduğum üzerine olurdu."  
    d "Her şeyi fazlasıyla kişisel alıyordum. Oysa hiçbir şeyi kişisel almamam gerekirdi."  
    d "O benim kızımdı ve haklıydı."  
    d "Bir keresinde kendime çok kızmıştım. Hayal kırıklığı, öfke, yenilmişlik ve en sonunda pişmanlık içinde boğuluyordum."  
    d "O anda odadan çıkmalıydım. Ama çıkmadım. Konuşmaya devam ettim. Savunmaya geçtim."  
    d "Şimdi dönüp baktığımda, o konuşmada söylediğim her şey saçmalıkmış."  
    d "Devam ettim, devam ettim... Aslında ona kızgın bile değildim, kendime kızıyordum ama bunu kabul etmek istemiyordum."  
    d "Yaşamak bile acı vericiydi. Artık dayanamıyordum ve hayatım boyunca bir ebeveyn olarak asla yapmam dediğim şeyi yaptım."  
    d "Ona vurduğumda..."  
    d "Onu da kaybettim."  
    d "Ve gerçekten elimde hiçbir şey kalmadı."  

    "Düşüncelerini toparlamak için biraz daha zaman ayırıyor."
    d "Dışarı pek çıkmam. Ama çıktığım zamanlarda seni ve onu birlikte görüyordum."
    d "Yanlış anlama, sana kızgın değilim. Zaten benden çok daha iyisini hak ediyor."
    d "Ama işte, sizi izlemeye devam ettim. Neler olabileceğini düşündüm. Bütün bunları nasıl önleyebileceğimi düşündüm."
    d "Hayatımın büyük bir kısmında başkalarını suçladım ama bu durumdan asıl sorumlu olan kişiyi suçlamayı hiç düşünmedim."
    d "Kendimi suçlamadım. Ta ki iş işten geçene kadar."
    "Bu konu hakkında daha fazla düşünmek istiyorum. Bir tepki vermek istiyorum. Ama aklımdan o kadar hızlı düşünceler geçiyor ki hepsini itmek zorunda kalıyorum ve şu an yapabildiğim tek şey dinlemek."
    d "Sanırım böyle olması gerekiyor."
    d "Dürüst olmak gerekirse, {i}böyle olmasına seviniyorum{/i}."
    d "Dediğim gibi, Natsuki beni hak etmiyor."
    d "Benim evimde yaşadığı hayatı hak etmiyor."
    d "Senin hakkında hâlâ hiçbir şey bilmiyorum."
    d "Adını bile bilmiyorum."
    d "Ama ne zaman seninle olsa, çok mutlu görünüyordu. Ve benim tek istediğim de buydu."
    "Aklımda bir şeyler söylemek için kelimeler arıyorum ama bulamıyorum."
    d "Tekrar söylüyorum, seni bunun içine sürüklediğim için üzgünüm."
    d "Bu tamamen benim sorumluluğum."
    "Sonunda kendimi bir şey söylemeye zorluyorum."
    mc "Peki şimdi ne yapmayı planlıyorsun?"
    d "Güzel soru."
    d "Kendi hayatıma son vermek istemiyorum."
    d "Bunu, yaptıklarımın affedilir olduğunu düşündüğüm için değil—kesinlikle değil—ama kendimi o kadar yenilmiş hissediyorum ki onu bile yapacak gücü bulamıyorum."
    d "Bu da geriye tek bir seçenek bırakıyor."
    "Sanırım ne demek istediğini anladım."
    d "Muhtemelen tahmin edebileceğin gibi, polise teslim olmayı planlıyorum."
    d "Ama bunun bir önemi yok. Hayatına ne kadar hızlı girdiysem, o kadar hızlı çıkacağım."
    stop music fadeout 2.0
    play music Thoughts fadein 2.0
    "Polise mi teslim olacak? Gerçekten böyle mi bitecek?"
    "Bu konuyu ciddi şekilde düşünmem gerekiyor. Bariz bir şekilde o korkunç bir ebeveyn ve harika bir insan olduğu da söylenemez."
    "Ama acaba her zaman böyle miydi? Eşi ölmeden önce nasıldı? Eğer her şey ondan sonra kötüleştiyse, öncesinde nasıl biriydi?"
    "Gerçi Natsuki o zamanlar muhtemelen çok küçük olduğu için babasının o zamanlar nasıl biri olduğunu anlatamaz."
    "Onu eski haline döndürmeye çalışmak buna değer mi? Natsuki hâlâ ondan nefret etmiyor, ona önem verdiğini söylemişti."
    "Peki ya aile terapisi almayı denedi mi? Hiç bahsettiğini hatırlamıyorum, Natsuki de bundan hiç söz etmemişti."
    "Ben her zaman burada olacağım, yani yalnız kalmaları gibi bir durum da olmaz. Natsuki, istemediği sürece benimle yaşamayı bırakmak zorunda değil."
    "En azından şunu söyleyebilirim ki, şiddet olayı bir daha tekrarlanmaz."
    "Natsuki'nin babası, beklediğimden çok farklı biri çıktı."
    "Onun bu kadar sakin olması, düşündüğüm kişinin tam tersi. Bu, yaptıklarını affettirmese de oldukça ilginç buluyorum."
    "Şimdiye kadar bu kadar kaybolmuş bir insan daha görmedim."
    "Asıl değerli olan şey ne? Daha iyi bir hayata ulaşmak için çabalamak mı, yoksa sahip olduğumuz hayatın içinde mutlu mesut yaşamak mı?"
    mc "Kabul etmeliyim ki bu konuda hiçbir uzmanlığım yok."
    mc "Ama bu durumdan en mutlu sonu çıkarmak istiyorum."
    mc "Belki gerçekten mutlu bir son olmayacak, ama bizi en parlak geleceğe götürecek olan kararı vermek istiyorum."
    mc "Bu yüzden, hepimiz için en iyi çözümün ne olacağını düşündüğümü söyleyeceğim."
    "{i} Ç.N : çok saçma bir cümle farkındayım, ingilizcesi de saçma aynı oranda :d{i}"
    menu:
        mc "Bence sen..."
        "Son bir kez uzlaşmayı denemelisin.":
            call natsukiRoute_GoodEnd
        "Teslim olmalısın.":
            call natsukiRoute_BadEnd
    return


label natsukiRoute_GoodEnd:
    $ natsukiGoodEnd = True
    "Natsuki'nin babası büyük hatalar yaptı. Hem de affedilmesi zor, korkunç hatalar. Ama ne olursa olsun, ikisi de birbirini önemsiyor."
    "Bunun, babasının kendini ihbar etmesiyle bitmesini istemiyorum. Bundan daha iyisini yapabiliriz."
    "İyileşmenin hâlâ mümkün olduğuna inanıyorum. Ona ikinci bir şans vermenin işe yarayabileceğine inanıyorum. Eğer işe yaramazsa, olsun. En azından denediğimizi söyleyebiliriz."
    "Natsuki'nin babası paramparça olmuş bir adam. Ama kırılan bir şey tamir edilebilir."
    "Onun pes etmesiyle bitmesini istemiyorum. Bundan daha iyisini yapabiliriz."
    "Bunun düzelebileceğine inanıyorum. Her şeyin bitmediğine inanıyorum. Eğer işler yolunda gitmezse... Olsun. Bazen böyle olur."
    "Natsuki'nin babası, geçmişte yaptığı tüm hataları düzeltemeyecek. Ama her şeyi değil, sadece {i}yeterince{/i} düzeltmemiz gerekiyor. Ve bu mümkün."
    "Bu hikâyenin, çok daha fazlası olabileceğini bilerek bitmesini istemiyorum. Bundan daha iyisini yapabiliriz."
    "Her şeyi kaybetmediğimize inanıyorum. Hâlâ kazanma şansımız olduğuna inanıyorum. Eğer hiçbir şey kazanamazsak... Olsun. En azından kaybedecek bir şeyimiz de yok."
    "Natsuki ve babasıyla birlikte çalışabilirim, onlar da bir terapistten destek alabilir. Hep birlikte hayatlarını düzene sokabiliriz."
    "Ben sıradan bir insanım."
    "Her şeyi düzeltemem. Her şeyin yoluna girmesini sağlayamam. Tüm cevaplara sahip değilim."
    "Ama bildiğim tek bir şey var: Bu işi başarabiliriz. Eğer denemezsek... İşte asıl kayıp bu olur."
    stop music fadeout 2.0
    play music AfterAll fadein 2.0
    mc "Natsuki ile yeniden iletişim kurmayı denemelisin."
    "Natsuki'nin babası şaşkınlık içinde bakıyor. Ben olsam ben de şaşırırdım."
    d "Neden? Beni hayatına geri alacağına hiç ihtimal vermiyorum."
    mc "Bilmiyorum. Senden korkuyor olabilir, şu anki hayatının değişme ihtimali onu daha çok ürkütüyordur belki."
    mc "Ama derinlerde bir yerde, bence hâlâ seni önemsiyor."
    mc "Bana bunu kendisi söyledi."
    d "Ya öyle demek istemediyse? Bazen öyle yapıyor."
    mc "Sanmıyorum. Ciddiydi bence."
    mc "Onunla altı aydır birlikteyim. Ne zaman içten olup olmadığını anlayabiliyorum."
    mc "Senin hakkında konuşurken, seni hâlâ önemsediğini ama hayatını değiştirmek istemediğini söyledi."
    mc "Eğer yalan söyleyecek olsaydı, bu çok garip bir zaman olurdu."
    mc "Eğer tam anlamıyla dürüst olmak istemeseydi, ‘Onu önemsememin bir anlamı yok ki’ ya da ‘Şu anki halim gayet iyi’ gibi bir şeyler söylerdi."
    mc "Durduk yere böyle bir konuda yalan söylemesi mantıklı olmazdı."
    mc "Demek istediğim şu: En azından bir şans verelim. Seni ve Natsuki’yi bir terapiste yönlendirebiliriz. Ben de her adımda yanınızda olurum."
    mc "Eğer gerçekten istiyorsan, kendini sonra da ihbar edebilirsin. Ama şimdilik, benim yardımımla Natsuki’yle yeniden iletişim kurmayı dener misin?"
    "Bir süre düşünüyor. Konuşmamız o kadar uzun sürdü ki, gece yarısını geçmiş olabilir."
    "Sonra başını kaldırıyor ve kararını veriyor. Konuştuğumuz her şey, hissettiğimiz tüm endişe, korku ve üzüntü… Hepsi bu ana gelmek içindi."
    d "Peki."
    d "Zaten kaybedecek bir şeyim kalmadı."

    
    d "O halde deneyelim. Hem kendim hem de kızım için her şeyi yoluna koymak istiyorum."
    mc "Tamam, o zaman ikiniz için bir danışmanla görüşme ayarlamaya çalışırım—tabii önce Natsuki'ye soracağım."
    d "Bunu gerçekten yapabilir misin?"
    "Gerçekçi düşününce, birini öylece danışmanlık sürecine sokmak pek de kolay olmasa gerek..."
    mc "En azından bir başlangıç yapabilirim."
    d "Sen öyle diyorsan."
    d "Yarın tekrar gelip konuşalım mı?"
    mc "Bence iyi bir fikir olur, evet."

    play sound closet_open
    play sound closet_close
    "Natsuki'nin babası kapıya yönelip dışarı çıkıyor ve kapıyı yavaşça kapatıyor. Çıkarken yüzünde hafif bir gülümseme yakaladığımı sanıyorum, ama emin olamıyorum."
    play sound closet_open
    "Tam o anda, odamın kapısının gıcırdadığını duyuyorum."
    mc "Gitti, Natsuki."
    show natsuki 4bu at t11
    "Natsuki yavaşça salona çıkıp derin bir nefes alıyor."
    n "Tamam."
    mc "Sana bir şey soracağım, Natsuki."
    mc "Aile danışmanlığına gitmek ister misin?"
    "Bunu düşünmesi biraz zaman alır diye bekliyordum ama neredeyse anında cevap veriyor."
    show natsuki 4bu at f11
    n "Evet."
    mc "Gerçekten mi? Daha önce değişime karşıydın gibi geliyordu."
    n 5bc "Şey... Babamla yaptığın konuşmanın tamamını dinlemiş olabilirim de, olmayabilirim de."
    n "İyi bir araba satıcısı olabilirmişsin, açıkçası."
    mc "Ah."
    "Gerçi hiçbir zaman ne olmak istediğime karar veremedim—neyse, neyse."
    mc "Yani, gerçekten gitmek istiyorsun?"
    n 42ba "Sonsuza kadar kaçamam."
    n "Uzun zamandır bunu düşünüyordum, aslında."
    n "Babamı hala önemsediğimi söylemiştim."
    mc "Netleştirmek için soruyorum, yani tamamen emin misin? Randevu ayarlamamı gerçekten istiyor musun?"
    n "Sen benim yanımda olmaya devam edeceksin, değil mi?"
    mc "Sen benim sevgilimsin, tabii ki her şeyin en iyisi için elimden geleni yapacağım."
    n "Güzel."
    n 12ba "...Bu konuda rahat davranıyorum gibi görünsem de, hala korkuyorum, biliyor musun?"
    n "Ama senin sayende bu adımı atabiliyorum."
    n "Bunu yapmaya yalnızca sana bu kadar güvendiğim için cesaret edebiliyorum. Ve sen bu güveni hiç kırmadın."
    n "O yüzden... teşekkür ederim."
    show natsuki 1ba at face_three(y=600)
    "Natsuki yanağıma hafif bir öpücük konduruyor ve odama geri dönüyor. Benim de yakında yatmam lazım."
    hide natsuki with wipeleft
    "Natsuki'nin ne kadar değiştiğini görmek inanılmaz. Yarım yıl önce bu teklifi sunsaydım, kabul edeceğini hiç sanmıyorum."
    "Şimdiye kadar yaşadığımız her şey... Nihayet bunun bir şekilde sonuca ulaşacağını bilmek inanılmaz tatmin edici hissettiriyor."
    "Şimdi tek mesele, yarının nasıl geçeceği."

    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    scene bg kitchen with wipeleft_scene
    play music AfterAll fadein 2.0
    window show

    
    "İşte geldik."
    "Gerçeklerle yüzleşeceğimiz gün nihayet geldi."
    "Kahvaltımı ederken kapının çaldığını duydum. Yoksa Natsuki’nin babası şimdiden mi geldi?"
    mc "Ben açarım."
    scene bg house_entrance with wipeleft_scene
    play sound closet_open
    "Kapıyı açtığımda, tahmin ettiğim gibi oydu. Üzerinde yorgunluk vardı."
    d "Bu kadar erken geldiğim için üzgünüm ama gece pek uyuyamadım."
    mc "Sorun değil."
    scene bg home_interior with wipeleft_scene
    "Oturması için kanepeyi işaret ettim. Natsuki’ye göz ucuyla baktığımda, başını çevirerek görmezden geldiğini fark ettim."
    "Bu önemli değil, şu an konuşmak zorunda değil. Onu rahatsız etmek istemem."
    play sound closet_close
    mc "Şey, Natsuki’yle konuştum ve--"
    d "Teslim oluyorum."
    stop music
    play music Dusk
    "...Bu konuşmanın gidişatı böyle olmalı değildi."
    mc "Ne?! Neden?"
    d "Çok fazla suçluluk hissediyorum. Bunun değişmesi mümkün değil."
    mc "Ama çok az kaldı! Kızınla yeniden bağ kurmak istemiyor musun?"
    d "İstiyorum, ama artık çok fazla hata yaptım. Bir karar verdim ve kendimi ihbar edeceğim."
    d "Üzgünüm, ama beni vazgeçirmeye çalışman bir şeyi değiştirmeyecek."
    "Hayır! Böyle olmaması gerekiyordu!"
    mc "Lütfen, en azından bir şans ver!"
    d "Üzgünüm ama kararımı verdim."
    mc "Gerçekten her şeyi böylece silip atmak mı istiyorsun? Onarmaya bu kadar yaklaşmışken?"
    d "Dediğim gibi, bu hiçbir şeyi değiştirmez."
    "Neden böyle olmak zorunda ki? Şu noktada ne yaparsam yapayım bir anlamı olmayacak gibi hissediyorum!"
    show natsuki 4be at t41
    n "Eğer [player]'ın söyledikleri seni ikna etmeye yetmiyorsa, belki benim söylediklerim yeter."
    mc "Natsuki?!"
    show natsuki 4bc at t42
    pause(1.0)
    show natsuki 4bc at s42
    "Natsuki ayağa kalktı ve babasının yanına oturdu. Gerçekten düşündüğüm şeyi mi yapacak?"
    n 1bg "Bunu söylemek benim için hiç kolay değil, özellikle yaşattıklarından sonra."
    n "Beni yıllarca görmezden geldikten sonra."
    n 12be "Beni dövdükten sonra."
    n "Beni... Neyse, bütün yaptıklarını saysam sabaha kadar buradayız. O yüzden sadede geleyim."
    n "Sen berbat bir babasın. Üzgünüm ama gerçek bu."
    n 12bb "Ama hala benim babamsın, biliyor musun?"
    n "Yıllar boyunca yaşadığımız güzel anlar da var."
    n "Belki çoğu aile kadar fazla değil, ama benim için önemli olan anılar bunlar."
    n "Sana yeniden güvenebilmem uzun sürecek ama en azından denemek istiyorum."
    n "Neden bilmiyorum. Belki de [player] bana tahmin ettiğimden fazla etki etti."
    d "Natsuki, sen... Sen değişmişsin."
    d "Seni en son gördüğümden beri çok zaman geçtiği için anlamam zor ama..."
    n 5bc "Öyle olabilir, ama şu an önemli olan bu değil."
    n "Belki sen benimle yeniden bağ kurmak istemiyorsun ama ben {i}seninle{/i} kurmak istiyorum."
    n "Eğer bunu deneme şansını kaçırırsam, kendimi affedemem."
    "Natsuki'nin babası şok içinde. Başka hiçbir şey değil, sadece şok."
    "Natsuki bana dönüyor."
    n 1ba "Bunu yapabilmemi sağlayan biri var."
    n 1bc "Gerçekten arkamda duran biri, ama bu başka bir konu."
    "Natsuki hâlâ biraz sinirli gibi görünüyor, ki bu tamamen anlaşılır bir şey. Ama şu an burada oturup bunları söylemesiyle gurur duyuyorum."
    n "Lütfen kendini ihbar etme. En azından {i}denemek{/i} istiyorum."
    n 1bu "Lütfen..."
    "Natsuki'nin babası düşündü, biz ise cevabını beklerken nefesimizi tuttuk."
    "Yıllarca süren çatışmalar, iniş çıkışlar, hatalar, kararlar ve duygular..."
    "Hepsi tek bir kararda birleşiyor."
    d "..."
    d "Peki, yeterince adil."
    d "Aile terapisine başlıyoruz, öyle mi?"
    "Başardı."
    "Son ana kadar emin olamamıştım ama gerçekten başardı."
    mc "Aynen öyle."
    "Hiçbirimiz bir şey diyemedik. Hepimiz o kadar rahatlamıştık ki, kelimeler aklımıza gelmedi."
    "Ve böylece iyileşme yolculuğumuz başlıyor."

    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    play music Brick fadein 2.0
    window show
    "Natsuki ve babasının danışmanlığa başlamasının üzerinden birkaç ay geçti."
    "Her şey tamamen yolunda demek zor olur, ama en azından idare ediyoruz. Özellikle de benim ikisi için bir dayanak olmam sayesinde."
    "Natsuki hâlâ ona tam olarak güveniyor diyemem, ama adım adım ilerliyoruz."
    "Babası da eskisine göre çok daha mutlu. İş aramaya bile başladı, ki bu bile başlı başına büyük bir gelişme."
    "En başta bu sürecin en iyi yol olup olmadığından emin değildim ama artık doğru seçim olduğunu düşünüyorum."
    n "Günaydın, [player]!"
    scene bg bedroom with open_eyes
    "Natsuki bana sıkıca sarılıyor, ardından kahvaltı hazırlamak için odadan çıkıyor."
    "Onun bu kadar sık tatlı yanını göstermesi hoşuma gidiyor, eski hâli de kendine has bir sevimliliğe sahipti tabii. Bunun için bir kelime vardı, değil mi? Tsundere?"
    "Ama ne fark eder ki, ben şu anki Natsuki'yi eskisinden daha çok seviyorum."
    "Odasından ayrılırken yatağımın kenarında bir şiir bıraktığını fark ediyorum. Bakalım ne yazmış..."
    
    call showpoem(poem_natGood, music=False)
    "...Güzel. İşte tam da görmek istediğim şey buydu. İçgüdülerime güvenerek doğru olanı seçtim ve bunun en iyi yol olduğuna inanıyorum."
    "Ayağa kalkmaya hazırlanırken kapının çalındığını duyuyorum ve gidip açıyorum."
    scene bg house_entrance with wipeleft_scene
    play sound closet_open
    mc "Ah, merhaba!"
    d "Selam! Sadece siz ikinizi bir kontrol etmek istedim."
    mc "Anladım. Biz iyiyiz! İçeri buyurmak ister misin?"
    "Natsuki'nin babasına kanepeye oturmasını işaret ediyorum."
    play sound closet_close
    scene bg home_interior with wipeleft_scene
    d "Bunu açmak istemem ama... Görünen o ki gayet mutlusunuz ve... Natsuki benimle yeniden yaşamaya sıcak bakmıyor. Doğru mu?"
    mc "Eh, bana daha çok güveniyor diyebilirim."
    d "Evet, ve onun bana senden daha fazla güveneceği bir noktaya gelmemiz zor gibi görünüyor."
    "Adamın söylediklerinde haklılık payı var."
    "Natsuki'ye dönüp bakıyorum. O sırada mutfakta tam bir kahvaltı sofrası hazırlamakla meşgul."
    mc "Peki, Natsuki? Ne diyorsun?"
    "Natsuki yemek yapmaya devam ederken cevap veriyor."
    n "Bunu bir düşünmem lazım. Belki deneyebilirim."
    n "Hmph. Ne yani, burada kalmamı istemiyor musun?"
    "Eh, belki de tatlı yanını {i}her zaman{/i} göstermiyordur."
    mc "Bu kalıcı bir karar olmak zorunda değil. Eğer ilişkimiz belli bir noktaya ulaşırsa, o zaman belki... Senin tekrar buraya taşınman mümkün olabilir."
    n "Fena fikir değil."
    n "Ama beni bekletmeye kalkma sakın!"
    "Ve o günden sonra, Natsuki babasını daha sık ziyaret etmeye başladı."
    "Henüz orada geceyi geçirmemişti ama yine de onunla daha fazla vakit geçirmesi güzel bir gelişmeydi."

    window hide
    show black with Dissolve(2.0)
    scene bg house_entrance with Dissolve(2.0)
    window show
    "Zaman geçmeye devam ediyor. Mevsimler kaç kez değişti, hatırlamıyorum bile."
    mc "Buna gerçekten hazır mısın, Natsuki?"
    show natsuki 1bb at f11
    n "Babamın evinde geceyi geçirmeye hazırım, evet."
    mc "Bu, er ya da geç taşınacağın anlamına geliyor... Seni özleyeceğim."
    n 4bb "Beni sürekli görmeye devam edeceğini zaten biliyorsun."
    mc "Biliyorum ama yine de garip hissettiriyor."
    n 1bq "Senin de dediğin gibi, eğer bir gün evlenirsek, böyle şeyleri düşünmek zorunda kalmayız, değil mi?"
    mc "Haklısın."
    n "Neyse, fazla uzatmayalım. Yarın görüşürüz, [player]!"
    hide natsuki with wipeleft
    scene bg home_interior with wipeleft_scene
    "Ve sonra yalnız kaldım... Geceyi tek başıma geçirecektim."
    "Natsuki ile tanıştığım ilk günden beri, her gün benim için inanılmaz bir yolculuk oldu."
    "Birbirimizden hoşlanıp hoşlanmadığımızı düşündüğüm günleri hatırlıyorum, oysa ki bu zaten apaçık ortadaydı. Hislerimi nasıl itiraf edeceğimi düşünerek endişelendiğim zamanları hatırlıyorum, halbuki endişelenecek bir şey yoktu."
    "Sonra Natsuki benimle yaşamaya başladı. Eğer bana sorarsan, bu gerçekten harika bir şeydi. Şartlar biraz tuhaftı, evet, ama yine de çok eğlenceliydi. Sonrasında çıkmaya başladık ve her şey daha da güzelleşti."
    "Bu kadar uzun süre bir ilişkiyi yürütebileceğimi hiç düşünmezdim. Hatta bir ilişkiyi sürdürebileceğimi bile sanmıyordum."
    "Natsuki ve babasına bu şekilde yardımcı olabileceğimi de hayal etmezdim ama işte buradayız."
    "Daha önce defalarca 'her şey harika gidiyor' ve 'şu an her şey ışıl ışıl parlıyor' gibi şeyler söyledim, ama sonra bazı şeyler üzücü hâle geldi."
    "Şimdi ise, tüm içtenliğimle her şeyin yolunda olduğunu söyleyebilirim. Gerçekten de artık hiçbir şeyin beni üzebileceğini sanmıyorum."
    "Ve sanırım {i}hiçbir şey{/i} gerçekten beni üzemez de. Sonuçta, o kadar çok şey yaşadım ki, artık her şeyle baş edebileceğimi hissediyorum."
    "Sanırım buraya kadar. Bu yolculuğun sonuna geldiğimi söylemek için en doğru yer burası gibi görünüyor."
    "Gerçekten çok eğlenceliydi."
    "..."
    "..."
    "..."
    scene bg home_interior_night with wipeleft_scene
    "Farkına varmadan, iki saat geçmiş bile. Oturma odasındaki kanepede oturmuş manga okuyorum."
    scene bg house_entrance_night with wipeleft_scene
    play sound closet_open
    show natsuki 1bc at f11
    "Ön kapıdan gelen bir ses duyuyorum ve tahmin ettiğim gibi gelen kişi sevgilimden başkası değil."
    mc "Ne oldu?"
    n 1bb "Sıkıldım."
    "Açıkçası, bunu bekliyordum."
    mc "Ah."
    n 1bq "Şey, hani sana bir yıl önce söz verdiğim cupcake’ler vardı ya?"
    n 1bk "Birazcık geciktim, kabul ediyorum, ama bir gün yapmamız gerekmiyor mu?"
    n "Ne dersin, şimdi yapalım mı?"
    mc "Tabii, neden olmasın."
    mc "Seni seviyorum, Natsuki."
    n 1bj "Ben de seni seviyorum, [player]."
    
    n 1bj "Her şey için teşekkür ederim."
    # olm ağlanır la ..
    
    
    $ persistent.natsukiCompletedGood = True
    window hide
    show white_end with Dissolve(5.0)
    show white with Dissolve(2.0)
    pause(5.0)
    return

label natsukiRoute_BadEnd:
    $ natsukiGoodEnd = False
    "Hataların için özür dileyebilirsin."
    "Günahlarından pişman olabilirsin."
    "Düzeltmeye çalışabilirsin."
    "Ama bu, geçmişte yaptıklarını değiştirmez. Hiçbir şey değiştirmez."
    "Natsuki'nin babası ona kötü davrandı, onu ihmal etti. Şimdi ne kadar pişman olsa da bu gerçeği değiştirmiyor."
    "Tıpkı onun Natsuki ile yeniden bağ kurabileceği ihtimalinin hiçbir şeyi değiştirmeyeceği gibi."
    "Yaptıklarını geri almanın bir yolu yok. Bundan sonsuza kadar kaçamaz. Bir suç işledi ve bunun sonuçlarıyla yüzleşmek zorunda."
    mc "Teslim olmalısın."
    d "..."
    d "..."
    d "Öyle olsun."

    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    scene bg home_interior_night with dissolve_cg
    play music Dusk fadein 2.0
    window show
    d "Gidip teslim olacağım."
    "Hâlâ oturma odamdaydık. Hava inanılmaz ağırdı, içinde derin bir keder barındırıyordu."
    mc "Evet."
    d "..."
    d "Bir şey rica edebilir miyim?"
    mc "Ne olduğuna bağlı."
    d "Teslim olma kararı tamamen benim fikrimdi ama sen de beni cesaretlendirdin."
    d "Bu durumda, bir şekilde işin içine sen de girmiş oluyorsun."
    d "Ama bunun seni ilgilendiren bir mesele olmasını istemiyorum."
    d "Eğer Natsuki bana ne olduğunu sorarsa, ona buraya gelip içimi döktüğümü, sonra da yaptıklarımın ağırlığını hissedip polise teslim olduğumu söyle."
    "Bir an düşünüp cümlelerini tartıyor."
    d "Aslında, boş ver. Ona nereye gittiğimi bilmediğini söyle."
    d "Ne olduğunu eninde sonunda kendi öğrenir zaten."
    "Bu konuda emin değilim ama galiba en mantıklı seçenek bu."
    mc "Pekâlâ, elimden geleni yaparım."
    d "Teşekkür ederim."
    "Ayağa kalkıp kapıya doğru ilerliyor. Yüzündeki hüzünlü ifadeyi saklamıyor."
    d "Bir şey daha."
    d "Lütfen kızıma iyi bak."
    d "Benim başıma ne gelirse gelsin umurumda değil artık."
    d "Ama onu hâlâ önemsiyorum."
    "Cevap vermeme fırsat bile vermeden kapıyı açıp çıkıyor ve ardından kapıyı kapatıyor."
    "İşte bu kadar. Hikâyenin sonu böyle geliyor."
    "Bundan daha iyi bir son mümkün müydü? Belki."
    "Ama istediğim son buydu."
    "Önemli olan da bu, değil mi? {i}Benim{/i} en doğru bulduğum son bu ve gerisi umurumda değil."
    "Odamın kapısının açıldığını duyuyorum. Natsuki dışarı çıkıyor."
    "Sanırım biraz açıklama yapmam gerekecek."

    stop music fadeout 2.0
    window hide
    show black with Dissolve(2.0)
    
    play music LettingGo fadein 2.0
    window show
    "O günden bu yana bir ay geçti. Natsuki, babasının teslim olduğunu bir şekilde öğrendi, ama nasıl öğrendiğinden pek emin değilim."
    "Her şeyin normale döndüğünü söylemek isterdim ve bir noktada döndü de, ama yine de bir şeyler eksik gibi hissettirdi."
    "Bir boşluk vardı. İkimiz de bunu hissediyorduk ama en çok Natsuki hissediyordu. Bazen öylece boşluğa dalıp gidiyordu; sanki kaybolmuş gibiydi."
    "Daha az stresli görünüyor ama sanki kaçırdığı bir fırsat olup olmadığını düşünüyormuş gibi hissettiği anlar bunu gölgede bırakıyordu."
    "Ama yine de bu, işlerin gidebileceği en iyi yoldu. Natsuki'nin babası artık yok ve bir daha onun için endişelenmek zorunda kalmayacağız."
    "Her şey bitti. Tüm sorunlarımız sona erdi."
    "En azından, her güne başlarken kendime bunu söyleyip durdum..."

    scene bg bedroom with open_eyes
    show natsuki 4b at f11
    n "Hadi ama, okula gitme vakti, [player]."
    hide natsuki with dissolve_cg
    scene bg residential_day with wipeleft_scene
    pause(1.0)
    scene bg club_day with wipeleft_scene
    "Natsuki'nin sesiyle uyanıyorum. Birkaç dakika sonra birlikte okula gidiyoruz ve her zamanki gibi Edebiyat Kulübü'nde buluşuyoruz. Yine her zamanki gibi oturup manga okuyoruz."
    "Ama bir noktada, bir şeyler değişiyor."
    
    show natsuki 5u at f11
    n "[player]. Koridora çıkabilir miyiz?"
    mc "Ha? Tabii."
    
    hide natsuki with dissolve_cg
    scene bg corridor with wipeleft_scene
    show natsuki 5u at f11
    "Koridora doğru ilerliyoruz, ama içimde garip bir sıkıntı hissediyorum."
    mc "Ne oldu?"
    
    show natsuki 12f at f11
    "Natsuki'ye bakıyorum, içimde bir korku var. Yaklaşık on saniye boyunca sessizlik oluyor, sonra bir anda gözyaşlarına boğuluyor."
    mc "Hey! Ne oldu?!"
    "Ona ne olduğunu sordum, ama aslında cevap ortadaydı. Bunu söylemesine bile gerek yoktu."
    
    n 12h "Çok... çok yalnız hissediyorum! Annem... ve şimdi babam da..."
    mc "Hey, artık ben varım yanında."
    
    n "Seni seviyorum, ama bu aynı şey değil."
    "Bu doğru. Natsuki bana başka bir aile üyesinden bahsetmemişti."
    "Belki de gerçekten tek kalan kişi benim onun için."
    
    mc "Böyle bir şeyin üstesinden gelmek kolay değil."
    mc "Ama imkânsız da değil, sana bunu garanti edebilirim."
    
    n 5e "Bunu nereden bilebilirsin ki?!"
    "..."
    
    n "Her şeyi düzeltebilirdik! Babam teslim olduğundan beri daha az stresliyim, ama bu başka sorunlara yol açtı!"
    "..."
    
    n 12i "Böyle olmak zorunda değildi..."
    "..."
    
    n "Neden?! Her şey eskisi gibi olmayacak. Hiçbir zaman da olmayacak!"
    "..."
    
    menu:
        n "Buna değer miydi? {i}Gerçekten{/i} buna değer miydi?"
        "...":
            "..."
        "...":
            "..."
    
    "..."
    "..."
    
    hide natsuki with wipeleft
    "Natsuki arkasını dönüp gidiyor ve geride bir şiir bırakıyor."

    call showpoem(poem_natBad, music=False)
    "Bu... okumayı umduğum şey değildi."
    "Ama diğer yandan, kimse bunun kolay olacağını söylememişti. Ben de söylemedim."
    "Hayat zor, ama devam etmek zorundasın. İlerlemeye devam etmek, kararlar almaya devam etmek zorundasın."
    "Aksi halde, gerçekten yaşıyor sayılır mısın?"
    "Bunun değip değmediğini artık umursamıyorum. Çünkü geçmiş değiştirilemez."
    "Tek önemsediğim şey, Natsuki'yle birlikte ilerleyip tüm bunların üstesinden gelebilmek."
    "Uzun sürecek, zor olacak... ama başarabiliriz. Buna inanıyorum."
    window hide
    show black with Dissolve(2.0)
    scene bg residential_day with dissolve_cg
    
    window show
    "Bir ay daha geçiyor. Öncekine kıyasla her şey biraz daha sakin, ama hâlâ tam anlamıyla normale dönmüş sayılmaz."
    "Bir gün okuldan döndükten sonra, oturup konuşmaya karar veriyoruz."
    show natsuki 1c at f11
    n "Babamın nasıl olduğunu merak ediyorum."
    n "Umarım iyidir."
    "Natsuki gözlerini yere dikiyor, içinde hala atamadığı bir huzursuzluk var."
    mc "Hak ettiği cezayı çekmeye devam ediyordur, eminim."
    n "Evet..."
    n 5g "...Ama neden bana yalan söyledin?"
    "Natsuki bana sert bir bakış atıyor. Ne demek istiyor?"
    mc "Ne demek istiyorsun? Ne zaman yalan söyledim ki?"
    n 5e "Babam senin evine geldiği gün."
    n "Unuttun mu? Odaya geldiğimde tanıdık bir ses duyduğumu söylemiştim."
    "Lanet olsun."
    n "O konuşmanın her kelimesini duydum. Babama teslim olmasını sen söyledin, değil mi?"
    n "Peki neden bana söylemedin? Sırf o sana söylememeni istedi diye mi? Burada asıl önemli olan benim ne düşündüğüm değil miydi?"
    mc "Natsuki, ben..."
    n 4u "Şu an söyleyebileceğin hiçbir şey yok."
    n "Güvenimi kırdın. Tek söyleyebileceğim bu."
    "Bu tam bir felaket oldu."
    n "Eğer bunu düşündüysen... hayır, sana kızgın değilim."
    n "Aslında, kızgınım."
    n "Ama seni terk edecek kadar değil."
    n "Sen doğru olanı yaptığını düşünüyordun, değil mi?"
    n "Bunu düşündüğünü bildiğim için seni çok fazla suçlayamam."
    n "..."
    n "..."
    n "Sonuçta..."
    n 12a "Seni terk edersem... bu sefer gidecek hiçbir yerim kalmaz."

    
    
    window hide
    show black with Dissolve(2.0)
    scene bg flashback_home with dissolve_cg
    
    window show
    d "Natsuki? Bekle! Nereye gidiyorsun?!"
    
    n "Gidiyorum, baba."
    n "Sana söyleyecek başka hiçbir şeyim yok."
    
    "Bunu yapmak garip hissettiriyor, ama burada artık kalamam. Bu evden uzaklaşmalıyım."
    
    "[player]... o benim son umudum."

    "Onunla yaşamaya gitmek konusunda hala kararsızım, ama başka bir seçeneğim var mı, ondan bile emin değilim."
    "Ona güvenmek istiyorum, ama bu zor. Sevdiğim insanlara bile güvenmek zor geliyor."
    "Yine de, buraya kadar benim yanımda oldu. Elbette dikkatli olacağım, ama..."
    "Bilmiyorum. İçimde küçük bir his var, belki o her şeyi düzeltebilir."
    "Belki bir gün babamla aramız her zamanki gibi olur."
    "Ama bir insana bu kadar güvenmek tehlikeli. Bunun beni nereye götürdüğünü çoktan gördüm."
    "Lütfen, [player]. Az sonra sana nasıl davranacağım için üzgünüm, ama bunu yapmam gerekiyor... ne olur ne olmaz."
    "Ama lütfen... lütfen bir gün dileğimi gerçekleştir."
    window hide
    stop music fadeout 5.0
    show end with Dissolve(5.0)
    show black with Dissolve(2.0)
    pause(5.0)
    return

# hayat cok sıkıcı