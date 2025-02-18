label yuriRoute_voxPopuli:
    play music aNewDay fadein 3.0
    scene bg residential_day with wipeleft_scene
    "Festivalin ertesi günü."
    scene bg class_day with dissolve_cg
    "Açıkçası, nasıl ya da ne zaman uyuduğumu pek hatırlamıyorum ama bir şekilde kendimi okula zorla getirdim."
    "Sanırım ders… kimya? Hımm."
    "Biraz uyumamda sorun olmazdı aslında…"
    play sound slap
    "{i}Thwick.{/i}"
    "Sanırım bir şey başıma çarptı…"
    "Bir an için o nesneyi bulmam biraz zaman aldı, sandalyemin bacağının yanında yatıyordu. Bir buruşturulmuş kağıt. Harika."
    "Notu açıyorum, yazıyı çözmeye çalışarak gözlerimi kısıyorum."
    $ o_name = "Not"
    o "Ders sonrası dışarıda buluşalım."
    "Bu kadar mı? Gerçekten?"
    "Onu geri fırlatmayı düşünsem de bir şey beni tutuyor. Bunu görmezden gelmemeliyim gibi hissediyorum."
    
    stop music fadeout 3.0
    scene bg class_day with wipeleft_scene
    "Teknik olarak, boş bir not yüzünden edebiyat kulübünü kaçırıyorum. Ama yine de, festivalde yaşananlardan sonra, onu tekrar görmeden önce kendi hislerimi bir düzene koymam gerekebilir."
    "Yaklaşık beş, on dakika sonra, biraz dağınık görünen bir üst sınıf öğrencisi geliyor."
    $ o_name = "Üst Sınıf"
    o "Hey, gerçekten geldin."
    mc "Bu ne demek oluyor?"
    o "Yani, kafana rastgele bir notun çarpmasıyla kaç kez insan bir şeyler yapmıştır ki?"
    mc "Şey… Merak ettim. O zaman, bana neden buraya getirdin?"
    "Adam, bir anlaşma yapıyormuş gibi diplomatik bir gülümseme takınıyor."
    o "Bunu kolayca söylemem yok ama…"
    o "Yuri ile çıkmamalısın."
    mc "Hı? Ne demek istiyorsun?"
    mc "Yani, biz zaten--"
    "Adam ellerini 'Biliyorum, biliyorum' der gibi kaldırıyor."
    o "Bak, sadece söylüyorum, onunla takılmaman senin için daha iyi olur. İnsanlar seni festivalde gördü ve…"
    "Omuzlarını silkiyor."
    o "Yuri'den, gerçekten, her kimse ondan daha iyi bir seçenek."
    o "Bu sert gelebilir ama, hımm… bazı olaylar oldu. Evet, olaylar."
    mc "Olaylar?"
    
    
    
    
    
menu:
    o "Bak, yardımcı olmaya çalışıyorum. Ondan uzak dur. Bu kadarını söyleyeceğim."
    "Sen bir korkaksın.":
        $ yuri_gPoints += 1
        $ yuri_coward = True
        "Sadece sessiz kalamıyorum."
        mc "Bir korkaksın, bunu biliyor musun?"
        "Gözleri kocaman açılıyor, tamamen şaşkın."
        o "Pardon?"
        "Göz göze bakıyorum ona."
        mc "Kimle takılıp takılmayacağımı bana söylemeni ne ben isterim ne de ihtiyacım var."
        mc "Ve bunu onun arkasından yapmaya çalışman…"
        mc "Sana ait olan hiçbir şeyi istemiyorum."
        "Çantamı omzuma atarak, ağzı açık şekilde onu arkada bırakıyorum. Zihnimde bir sürü soru var."
        "Neden bizimle ilgilensin ki?"
        "Yuri ne yaptı ki?"
        "Kendini kim sanıyor?"
    "Tamam, tabii ki.":
        $ yuri_gPoints += 1
        $ yuri_bPoints += 1
        "‘Evet’ gibi bir şey mırıldanıyorum, ama kafam bambaşka bir yerde."
        o "Aynı fikirde olmamız güzel. Dediğim gibi, sert olacak ama ikinizin de iyiliği için."
        "Onun yapmacık nezaketine neredeyse kusacağım."
        "Neden bizimle ilgilensin ki?"
        "Yuri ne yaptı ki?"
        "Kendini kim sanıyor?"

scene bg corridor with wipeleft
"Gitmem gerek. Muhtemelen edebiyat kulübünün geri kalan kısmının bir kısmını yakalarım."
"Yuri ile bu sonrasında nasıl karşılaşacağımı bilmiyorum ama o köprüyü geçerken düşünürüm."
call yuriRoute_return
return

label yuriRoute_return:
    play music aNewDay fadein 3.0
    scene bg club_day with wipeleft_scene
    "Edebiyat kulübü kapısını aralayıp içeri giriyorum. Natsuki de yanımda yürüyerek, koltuğunun altına yerleştirilmiş kocaman bir dergiyle geliyor."
    "Yuri hakkında ona bir şeyler sormalıyım."
    "Bunların birbirlerine karşı gösterdikleri nefretle dolu davranışlarına rağmen, son zamanlarda biraz daha toleranslı olduklarını görebiliyorum."
    "Natsuki’nin bir şeyler duymuş olma ihtimali olmasa da, yine de ona sormak zararıma olmaz."
    mc "Hey, Natsuki, bir dakika dışarıda konuşabilir miyiz?"
    hide natsuki with wipeleft
    show sayori 2m at t21
    show monika 3c at t22
    stop music fadeout 3.0
    "Sayori ve Monika bana kafalarını karıştırmış bir şekilde bakıyorlar, ama ben hafifçe başımı sallayıp dışarıya çıkıyorum."
    scene bg corridor with wipeleft 
    show natsuki 4e at t11
    "Birkaç saniye sonra, Natsuki de koridora çıkıyor."
    n "Vay canına, bu da neyin nesi--"
    show natsuki 4c at t11
    "Natsuki, yüzümdeki ifadeyi görünce aniden duruyor."
    n 2c "Sen… bir şeyler düşünüyorsun gibi görünüyorsun. Ne oldu?"
    "Ben de gizlemiyorum. Her şeyi anlatıyorum."
    mc "Bir adam, geçen dersten sonra beni kenara çekti. 'Kendi iyiliğim için' dedi, Yuri’den uzak durmam gerektiğini söyledi."
    mc "Bu ne demek oluyor ki?"
    mc "Kimse onun hakkında böyle bir şey diyebilir mi?"
    show natsuki 2u at t11
    "Natsuki alt dudağını çiğniyor, yere bakarak bir noktaya odaklanmış."
    n "Sanırım sonunda duydun, [player]."
    n "Yuri hakkında zaman zaman dedikodular çıkıyor, evet."
    n "Ama biliyorsun, bunlar sadece dedikodu, değil mi?"
    mc "O zaman başka bir şey bilmiyorsun, değil mi?"
    mc "Peki, dedikodular ne hakkında? Bahseden adam bayağı belirsizdi."
    n "Dedikoduların ne olduğunun önemi olmamalı, [player]."
    n "Yani, uzun zamandır okula gidiyorum ve dedikoduların hiçbiri sonunda doğru çıkmaz."
    n "Neden senin için farklı olsun ki?"
    n "Ayrıca, dedikodular o kadar yaygın değil."
    n "Eğer yaygın olsaydı, sanırım Monika zaten duymuş olurdu ve bir şeyler yapardı. Ya da belki zaten denedi ve işe yaramadı, ama ne demek istediğimi anlıyorsun, değil mi?"
    n "Yuri, senin o dedikodulara karışmanı istemezdi zaten."
show natsuki 1c at t11

    "Natsuki gözlerini bana doğru kaldırıyor."
    n "Beni gerçekten çok seviyor, biliyor musun?"
    "Biraz kırmızılaşmaya başladığımı hissediyorum."
    mc "E-evet. Sanırım öyle."
    n "Belki de--"
    m "Tamam, herkes~!"
    m "Şiirlerinizi paylaşma zamanı!"
    show natsuki 4c at t11
    pause(1.5)
    show natsuki at thide 
    hide natsuki 
    "Natsuki, blazerını düzelterek hırlayarak şiirini almak için yürüdü."
    "Sanırım ben de şiirimi almak için gitmeliyim..."
    
    show black with dissolve_cg
    "Geldim, gördüm, şiirimi paylaştım."
    "Ama Yuri bile orada değildi."
    call yuriRoute_amberHeart
    return
    

label yuriRoute_amberHeart:
    scene bg residential_day with wipeleft_scene
    
    show sayori 1k at t11
    s "Hey, [player]?"
    "Sayori'ye bir bakış attım. Başını eğmiş, yolumuzdaki çakıllara boş boş tekme atıyordu."
    s "Ben biraz meraklı olabilirim ama... Natsuki ile ne konuştunuz?"
    "Ah--demek ki buymuş."
    "Gerçekten hiç konuşmadık ve ben onun unutmuş olacağını düşünmüştüm. Galiba ona yeterince güvenmiyorum."
    s 1l "[player]?"
    play music Thoughts fadein 3.0
    mc "Ah, ı-ıh..."
    mc "Şey..."
    mc "Sanırım sen de Yuri ile aramızı biliyorsundur, değil mi?"
    "Sayori, dikkatlice bana bakarak başını salladı."
    s 1h "Evet...?"
    mc "Şey, yani... bazı dedikodular vardı."
    s "Dedikodular?"
    mc "Birisi bana Yuri'den uzak durmamı söyledi."
    show sayori 2g at t11
    "Sayori, benim gibi kafası karışmış ve endişeli bir şekilde tepki veriyor."
    s "Bu çok kötü..."
    mc "Biliyorum. Ama ne yapabilirim? Nedenini söylemedi."
    show sayori 2u at t11
    "Sayori, küçük bir baş sallayarak onayladı."
    mc "Natsuki'nin neden bu kadar içine kapanık olduğunu belki o biliyordur diye düşündüm ama o da konuya girmedi."
    mc "Sen biliyor musun?"
    s "Bilmiyorum... Üzgünüm, [player]."
    show sayori 2g at h11
    "Elimi uzatıp yanaklarına hafifçe dokundum, o da çığlık atarak sıçradı."
    mc "Merak etme. Bu benim sorunum, tamam mı?"
    show sayori 1u at t11
    "Sayori başını sallayarak sırt çantasını omzuna aldı."
    s 1g "[player]."
    mc "Evet?"
    s "Senin anlayışını istiyorum. {i}Biz{/i} senin için buradayız."
    mc "Biliyorum."
    s "Ama ya gerçekten biliyor musun? Sanki sadece bizlere güvenmediğin için geri duruyorsun gibi hissediyorum."
    "Sayori, bana dikkatlice bakarken, o neşeli hali yerine ciddi bir tavır takındı."
    stop music fadeout 3.0
    mc "Şey... Eğer bir fikrin varsa, duymaya açığım."
    "Sayori başını sallayarak parmak uçlarını birbirine yaklaştırdı."
    play music aNewDay fadein 3.0
    s 1x "Neden onu dışarı davet etmiyorsun? Orada konuşabilirsiniz."
    mc "Aslında bunu planlıyordum, evet."
    show sayori 1x at h11
    "Sayori ellerini birbirine çarparak başını salladı."
    s "Bu işe yarar! Sadece güzel bir yere götürdüğünden emin ol!"
    mc "Güzel mi?"
    s 2c "Yani, onu her yere götüremezsin, biliyorsun?"
    mc "E-evet, biliyorum."
    "Sayori, evimin önünde zıp zıp durarak durdu."
    s 4x "İyi bir izlenim bırakmalısın. Ben izleyeceğim!"
    "Küçük bir kahkaha atarak el salladım."
    mc "Beni dürüst tut, tamam mı?"
    stop music fadeout 2.0
    show black with close_eyes
    "Sayori geri cevap vermedi."
    call yuriRoute_tasseography
    return

label yuriRoute_tasseography:
    "Bir kitapçı. Bu kolay olmalı, değil mi?"
    "Tabii, eğer ben olmasam, ne olursa olsun uyku saatlerimi, teknik olarak 'ilk buluşmamız' olabilecek yerin en iyi yerini araştırarak geçirmiş olsam."
    "O zaman, sanki kendi dişini çekiyormuşsun gibi hissettiriyor."
    s "Kesinlikle bayılacak, buna eminim!"
    scene bg residential_day
    show sayori 4x at t11
    with open_eyes
    play music aNewDay fadein 3.0
    "Sayori, gülümsedi ve benimle birlikte okula doğru zıp zıp atarak yürüdü. Bu organizasyonu yapmamda bana yardımcı olan oydu, o yüzden belki de haklıdır."
    "Ve zaten onu daha uzun zamandır tanıyor."
    show sayori 4m at h11
    s "Aah!"
    "Sayori, birden durakladı, gözleri kocaman açılmış. Ben ne olduğunu anlamaya çalışırken, bana itti."
    s 1c "İşte Yuri! Bu fırsatın!"
    show sayori 1a at t44
    show yuri 1a at t41
    "Evet, gerçekten de o, sokak köşesinde yaslanmış duruyor."
    "Beni mi bekliyor?"
    "Belki?"
    "Sadece umarım."
    show sayori 1c at f44
    "Blazerımın önünü düzelterek, ağzım aniden kuru bir hale geldi. Sayori yine beni itti."
    s "Hadi! Bu planladığın şey değil miydi?"
    show sayori at thide
    hide sayori
    show yuri 1b at t11
    "İleriye doğru sendeleyerek, bir selamlaşma pratiği yaparken, Yuri bana döndü."
    
    $ firstThreeChars = player[:3]
    $ o_name = "[firstThreeChars]+Yuri"
    o "Merhaba!"
    "Aynı anda biz de bunu söyledik. Şu an yerin dibine girmek istesem de, en azından Yuri de tıpkı ben gibi utanmış görünüyor."
    y 2j "Sayori, şey... Sayori bana senin buradan geçtiğini söyledi."
    "Hızla omuzumun üzerinden baktım."
    play music EarlyBird fadein 3.0
    "Bahsedilen kişi çoktan sahneden kaçmış. Pek de fena olmadı sanırım."
    mc "Neyse ki ben buradayım. Hadi gidelim mi?"
    show yuri 1a at t11
    "Yuri hızla başını salladı ve hızlıca yan yana yürümeye başladık."
    "Endişeyle boğazımı temizledim."
    mc "Festivalde eğlendin mi? İlk defa bir kulübe stant kurmasına yardımcı oldum."
    show yuri 1m at t11
    "Yuri başını sallayarak, yüzünde bir gülümseme belirdi."
    y "Evet! Öğrencilerin şiirimize ilgi göstermesi çok moral vericiydi."
    mc "Demek istediğin, {i}senin şiirlerin{/i}, değil mi?"
    "Yuri, belirgin bir şekilde pembeye döndü."
    y 3v "O doğru değil. En azından senin şiirlerin bana ilham veriyor..."
    show yuri 3g at t11
    "Gülümseyerek kahkaha attım, bu da onu bana doğru döndürdü, yüzünde somurtkan bir ifade."
    mc "Ben sadece kelimeleri yazıp, tutmalarını umarım. O tamamen senin eserindi ve gerçekten çok güzeldi."
    y 3h "Ben..."
    y 3j "Şey... teşekkür ederim."
    show yuri 2a at t11
    "Sessizlik içinde yürümeye devam ettik ama bu daha çok huzurlu bir sessizlikti, garip bir sessizliktense."
    "Okul kapılarına yaklaştığımızda, yavaşça durdum."
    mc "Ve... bir şey daha?"
    y 2f "Hı?"
    mc "Okuldan sonra buluşmaya hala tamam mısın?"
    y 1m "Ah! E-evet! Kesinlikle!"
    "Yuri, bir anda heyecanlanarak daha dikkatli bir hale geldi."
    mc "Tamam, harika. Burada buluşalım mı?"
    "Yuri hızlıca başını sallayarak, hala gülümsüyordu."
    y 1b "Sanırım dersime gitmeliyim."
    mc "Evet, evet."
    show yuri 1c at lhide
    hide yuri 
    stop music fadeout 3.0
    "O, yavaşça uzaklaşarak beni kendi sınıfıma gitmeye bırakıyor."
    "Şu an okuluma odaklanamayacağımı biliyorum."
    "Bazı şeyler kazanılır, bazıları kaybedilir, sanırım."
    scene bg residential_day with wipeleft_scene
    
    "Sonuçta, 'Yuri ile buluşmamız' demek, edebiyat kulübünden çıkmamızı sağladı ve Yuri’nin yüzü ilginç bir bordo rengine büründü."
    show yuri 2v at t11
    y "B-bunu yapmana gerek yoktu, [player]."
    mc "Evet, ama ben hiç uyarı yapmadan kaybolmak istemedim."
    show yuri 1c at t11
    "Yuri başını sallayarak hafifçe gülümsedi."
    mc "Neyse, kitapçı gerçekten çok yakın. Belki daha önce gitmişsindir, aslında..."
    y 1d "Evet, belki gitmişimdir ama... Yanımda birisiyle değil."
    "Beni, istemsizce gülümsedim, omzumla onu hafifçe dürttüm."
    mc "Her şeyin bir ilki vardır, değil mi?"
    scene bg streets_day
    show yuri 1c at t11
    with wipeleft_scene
    pause(1.0)
    scene bg bookstore
    show yuri 1a at t11
    with wipeleft_scene
    play music YurTheme fadein 3.0
    "Yuri ve ben, buluşmamız için seçtiğim kitapçıya doğru yürürken, vücudumda bir kaygı dalgası yayılıyor, çünkü her şeyin yolunda gitmeme ihtimali beni korkutuyor."
    "Neyse ki, şu anda burada oldukça az insan var, bu da burayı bir buluşma yeri olarak mükemmel kılıyor."
    "En azından, umarım öyledir."
    mc "Yani... şey, işte buradayız."
    "Yuri bana bakıyor, göz teması kurmakta zorlanıyor."
    y 2o "E-evet, buradayız..."
    "O da en az benim kadar, belki daha da fazla, gergin görünüyor."
    "Ne yapmalıyım ki burada? İnsanlar kitapçılara kitap almak için gider, değil mi? Ama nereden başlamalıyım?"
    "Sanırım, sadece bakınıp, ilginç bir şeyler görmeye çalışmak kolay olur."
    mc "Horror (korku) türünü seviyorsun, değil mi Yuri?"
    "Yuri, bana bir kez daha bakıp başını salladı."
    y 1a "Evet, doğru. Korku severim."
    mc "O zaman, korku bölümüne göz atmak ister misin?"
    "Yuri’nin yüzündeki gergin ifade geri dönüyor."
    y 2o "Sadece sen istersen..."
    "Sanırım Yuri, ne demek istediğimi tam olarak anlamadı ama önemli değil."
    hide yuri with wipeleft
    "Korku kitabı bölümüne yöneliyoruz ve tam oraya vardığımızda donakaldım."
    "Vay canına... Şimdi ne yapacağım? Kitaplar hakkında hiçbir şey bilmiyorum! Yuri zaten bir uzman, peki ben ne yapmalıyım ki aptal gibi gözükmeyeyim?"
    "Şimdilik, farklı başlıklara göz atıyorum. En azından, iyi çizilmiş kapak sanatını takdir edebilirim."
    show yuri 1b at t11
    y "İlginç bir kitap buldun mu, [player]?"
    "Yuri, beni hazırlıksız yakaladı ve biraz geri sıçradım."
    mc "Ah! Sadece göz gezdiriyordum..."
    "Yanımda ne varsa, ona hızla sarıldım, ne olduğunu kontrol etmeye vakit bulamadan."
    y 1f "Deliliğin Dağlarında mı?"
    mc "Evet! Yani, kapak resmi gerçekten çok havalı görünüyor... Sanırım. O boş, karlı manzara biraz korku veriyor, değil mi?"
    y 1c "Uhuhu."
    y 1d "Yani, bu kitabın muazzam olduğunu söylemek zor, ama kapak gerçekten bir izlenim bırakıyor."
    mc "Buna mı inanıyorsun?"
    y "Evet. Bir kitabın kapak sanatının, yazı ortalama olsa bile, en ikonik şey haline gelmesi ilginç."
    "Hala kitaplar ve yazılar hakkında nasıl yorum yapmam gerektiğini pek anlayamıyorum ama Yuri, her zamanki gibi ne hakkında konuştuğunu biliyor gibi görünüyor."
    mc "O zaman, bu kitabı alacağım."
    mc "Peki, senin burada ilgini çeken bir şey var mı, Yuri?"
    y 2o "Ah, şey... Ben bu kitapçıya her zaman geliyorum ve yeni bir stok görünmüyor, bu yüzden..."
    "Yuri, gözlerini kaçırarak sinirli bir şekilde bakıyor."
    y 2p "Buraya her zaman geldiğimi sana söylemeliydim, böylece farklı bir yer seçebilirdin. İlk buluşmamızı bile mahvediyorum…"
    "Yuri'nin yüzü daha da düşüyor."
    mc "Hayır, mahvolmuş değil! Mekânın önemi yok. Seninle birlikte olmaktan hâlâ keyif alıyorum, kitaplar hakkında hiçbir şey bilmesem de."
    y 2f "Gerçekten mi?"
    "Yuri biraz daha neşeleniyor."
    mc "Evet! Bu buluşmaya seninle vakit geçirmek için geldim."
    mc "Tabii ki, keşke senin zaten geçtiğin kitapların olduğu bir kitapçı seçmeseydim ama kimin umurunda?"
    mc "Bu, seninle vakit geçirme zevkimi engellemeyecek."
    mc "Daha önce de bunun olabileceğini konuştuk ve buna tamamen hazırlıklıydım."
    mc "Ayrıca, buluşmamızın tam yerini sana hiç söylemedim."
    mc "Kendini suçlaman için hiçbir nedenin yok."
    y 3p "Ah… Şey, böyle hissediyorsan…"
    y 3c "Teşekkür ederim, [player]."
    y 3b "Ben de seninle olmaktan keyif alıyorum."
    "Biraz garip bir sessizlik havayı dolduruyor. Şimdi ne yapacağız?"
    mc "Şey, uh..."
    "İkimiz de yere bakıyoruz."
    mc "Hadi oturalım! Yani, bu kitabı aldıktan sonra."
    scene bg bookstore with wipeleft_scene
    show yuri 1a at s11
    "Kitabı hızlıca satın aldıktan sonra, yakındaki bir masaya geçiyoruz ve yan yana oturuyoruz."
    y 1b "Tekrar birlikte mi okuruz, o zaman?"
    mc "Belki sonra, ama önce biraz sohbet etmek istiyorum."
    y "Anlıyorum. Bu anlaşılabilir."
    
    mc "Peki, nasılsın?"
    
    y "Oldukça iyiyim."
    y "..."
    "Önceden gelen garip sessizlik, şimdi tekrar bütün gücüyle geri dönüyor. Yuri, kafasını masaya koyuyor, kollarının üstüne yaslanarak."
    y 1o "Ne yapmalıyım, [player]?"
    y "Buluşmaların nasıl olması gerektiğini hiç bilmiyorum. Sadece zamanını boşa harcıyorum…"
    
    mc "Hayır, asla!"
    mc "Dediğim gibi, sadece senin yanında olmak harika."
    mc "Sözler her şey değildir her zaman."
    "Yuri, bu yorumumdan sonra biraz daha sakinleşiyor."
    y 1b "Sanırım öyle…"
    "Konu değiştirmeye karar veriyorum."
        mc "Şey, biliyorum ki sen şiirle ilgileniyorsun ama hiç kendi kitabını yazmayı denedin mi?"
    y 1f "Hı?"
    y 1b "Aslında, bir tür hikaye yazmayı denedim diyebilirim."
    y 1o "Ama bir kitap yayınlamak, yazdıklarımı başkalarına göstermek anlamına gelir ve, açıkçası… kimse okuma zahmetine girmezdi."
    mc "Ama, Yuri, kendini fazla küçümsüyorsun."
    y "Gerçekten de öyle."
    mc "Hayır, bence senin şiirlerin harika. Eğer bir roman yazmayı deneseydin, o da çok güzel olurdu."
    y "Bunu o kadar kolay bir şekilde karşılaştırmak doğru değil. Şiir yazmakla geleneksel bir hikaye yazmak çok farklı."
    y "Bir hikaye yapısı kurmak, ilgi çekici karakterler yaratmak ve diğer yazınsal unsurlar…"
    y "Gerçekten büyük bir iş, ve şiir yazmanın zorluklarından farklı zorlukları var."
    y "Bana kalırsa, bir roman denemelerimi okusan hayal kırıklığına uğrardın."
    mc "Buna inanmıyorum. Belki bir gün birlikte senin yazdıklarını okuruz."
    y 1a "Eğer gerçekten istersen… belki bir gün."
    "Yuri’nin dudaklarında hafif bir gülümseme beliriyor."
    mc "Neyse, az önce aldığım kitaba ne dersin? Hadi bakalım, ne gibi bir şeymiş."
    y "Evet, bakalım."
    show black with close_eyes
    "Yuri ve ben kitabı birkaç saat okuduk, yarısına kadar gelene kadar."
    hide black with open_eyes
    mc "Peki ya sen, nasıl buldun?"
    y 1b "İzlenimlerim mi? Henüz tam olarak hikayeyi bitirmedim ama şu ana kadar oldukça keyif aldım."
    mc "Evet, ben de aslında korku türü hakkında pek bilgim yok ama eğlenceli olduğunu düşündüm. Bu Lovecraft adamının gerçekten karanlık bir aklı var…"
    mc "Biraz korkutucuydu, galiba türüne uygun bir şey. Ama bana oldukça farklı bir deneyim oldu."
    mc "Ama senin yanımda olman her şeyi çok daha rahat hale getirdi."
    "Yuri’nin yanakları hızla kızarıyor."
    y 4a "Teşekkür ederim…"
    mc "Kalanını bir ara birlikte okuruz, ne dersin?"
        y 1d "Bunu çok isterim."
    mc "Bu randevuyu gerçekten çok sevdim, Yuri."
    y 1b "Ah… doğru, bu bir randevu olduğunu unutmuşum."
    y 1b "Ben de çok keyif aldım."
    "Birbirimizin gözlerinin içine bakıyoruz, ta ki Yuri, sinirlenerek bakışlarını kaçırana kadar."
    y 1o "Üzgünüm… hala buna alışmaya çalışıyorum."
    mc "Sorun değil, Yuri. Ne kadar yavaş ya da hızlı olursak, sen nasıl istersen öyle."
    y "Gerçekten beni seviyorsun, değil mi?"
    y "Yani, benimle vakit geçirmekten hoşlanıp, birlikte bir kitabevine gitmeye katlanabiliyorsun…"
    y "Böyle insan çok az."
    y "Senin bana karşı hissettiklerini düşündüğüm için minnettarım."
    mc "Hey, eminim ki seninle bir ilişkisi olmayı isteyecek pek çok insan vardır. Benim seni beğeniyor olamam bile beni şaşırtıyor, tabii ki iyi anlamda!"
    y "Düşündüğünden daha az insan, [player]."
    stop music fadeout 3.0
    y "…çok daha az."
    "Yuri, bu konuşmadan dolayı biraz üzülmüş gibi görünüyor. Bunu telafi etmenin bir yolunu bulmalıyım."
    mc "Şey… şu an seninleyim, değil mi? Ve diğer edebiyat kulübü üyeleri de var. Kaç kişi seni seviyor olursa olsun, önemli olan seni sevenlerin olması."
    mc "Başka neye ihtiyacın var?"
    y 1j "E… sanırım bunu böyle söylemek de bir yol."
    show yuri 1c at t11
    "Yuri, bunu duyduktan sonra biraz daha mutlu olmuş gibi görünüyor, kendine hafifçe gülümseyerek."
    mc "Bugün seninle daha fazla vakit geçirmek isterdim ama akşam olmak üzere, değil mi?"
    mc "Sanırım şimdi hazırlanıp çıkmamız gerek."
    "Yuri'nin yüzüne hayal kırıklığı ifadesi geliyor."
    y 1k "Doğru. Keşke daha uzun süre birlikte olabilseydik, ama galiba bu kadar oluyor."
    mc "Evet, maalesef öyle…"
    "Birlikte el ele tutuşarak mağazadan çıkıyoruz."
    scene bg streets_afternoon
    show yuri 1c at t11
    with wipeleft_scene
        "Yürürken, kaldırımda tanıdık birini fark ediyorum."
    
    "O çocuk… okuldan biri, değil mi? Beni uyaran kişi. Ona bakmak için durduğumda, o da bizi fark ediyor. Yüzünde küçük bir sinsi gülümseme beliriyor ve aynı anda birbirimizi tanıyoruz."
    y 1f "[player]?"
    "Gözlerimi ondan kaçırıp tekrar yürümeye başlıyorum."
    mc "Üzgünüm! Hiçbir şey değil."
    "Evet, onu şehirde zaman zaman görmek mantıklı olurdu, sanırım."
    "Ama bu sefer neden bu kadar korkutucu hissettirdi? Bir önsezi mi? Belki de o sinsi gülümseme… Evet, o gerçekten biraz ürkütücüydü."
    
    
        "Neyse, sanırım önemi yok."
    "Ve, Yuri hakkında duyduğum dedikoduları konuşmam gerekmiyor muydu?"
    show black with close_eyes
    "Hıh… herhalde bir sonraki sefere kadar beklemem gerekecek."
    call yuriRoute_interlude
    return

label yuriRoute_interlude:
    scene bg bedroom with open_eyes
    play music aNewDay fadein 3.0
    "Son buluşmamdan beri bir hafta falan geçti."
    "Ondan önce duyduğum dedikoduları ona anlatmayı planlamıştım ama bir türlü cesaret edemedim."
    "Bunun gerçekten ağır bir konu olduğunu hissediyorum ve bunu berbat etmek istemiyorum."
    "Ama o dedikodulardan dolayı pek bir şey de olmadı aslında."
    "Keşke sonsuza kadar cahil kalabilsem ama bir noktada buna Yuri ile konuşmam gerekecek, o yüzden galiba bunu bir an önce halletsem iyi olacak."
    "Uykulu bir şekilde yataktan kalkarken, birkaç dakika önce Yuri'den bir mesaj aldığımı fark ediyorum."
    $ o_name = "Telefon"
    o "{i}Günaydın, [player].{/i}"
    "En azından Yuri hâlâ bana güveniyor… buna biraz kötü hissediyorum. En azından bunu açığa kavuşturmak daha iyi olur."
    "Mesajına cevap verdikten sonra, okula hazırlanıp evden çıkıyorum."
    
    scene bg club_day with wipeleft_scene
    "Derslerim bitince, bir yandan midenin içinde kaygı büyürken, Edebiyat Kulübüne doğru ilerliyorum."
    show yuri 1a at t44
    "Her zamanki gibi, Yuri bir masada kitap okuyor."
    show monika 1b at t41
    show sayori 1c at t42
    "Monika ve Sayori beni selamlamaya çalışıyorlar ama, bu sözler kulağımdan girip diğerinden çıkıyor çünkü ben Yuri'ye doğru yürümeye devam ediyorum."
    show monika at thide 
    show sayori at thide
    hide monika 
    hide sayori 
    show yuri 1a at t11
    mc "Selam."
    "Yuri dönüp beni fark ediyor. Okuduğu kitabı hızlıca kapatıyor, parmağı kitabın arasında kaldığı için sayfa, adeta bir yer işareti gibi kalıyor."
    y 1b "Ah! Merhaba, [player]. Geldiğini fark etmediğim için özür dilerim."
    mc "Sorun değil, endişelenme."
    mc "Ama aslında seninle konuşmam gereken bir şey vardı…"
    show yuri 3o at t11
    "Yuri'nin yüzüne hafif bir gerginlik yerleşiyor."
    y "Hımm?"
    mc "Yani, aslında…"
    "Bunu nasıl söylesem?"
    mc "Temelde, şey…"
    "Şu an bir kelime dahi çıkaramıyorum."
    y 1n "Acele etme, [player]."
    "Sonunda aklımdan geçenleri lafı ağzımdan çıkarıyorum."
    stop music
    mc "Bizim hakkımızda dedikodular var!"
    y 2r "Ne?!"
    "Harika, işte bu oldu."
    mc "Bir sınıf arkadaşım bana geldi."
    mc "Bana, seninle ilgili ‘olaylar’ olduğunu ve benim seninle ilişki kurmamam gerektiğini söyledi."
    mc "Ama ben biliyorum, bu doğru değil!"
    mc "Kesinlikle doğru değil. Ama ne yapacağız, Yuri?"
    mc "Biliyorsun, dedikodular nasıl yayılır, değil mi? Giderek daha kötüleşir, ta ki… yani…"
    show yuri 1u at t11
    play music Amber fadein 3.0
    "Yüzünde melankolik bir ifade beliriyor."
    y "…"
    mc "Yuri?"
    y 1v "Başından beri kötü bir fikirdi, değil mi?"
    y "Sadece sana sorun çıkaracağımı biliyordum."
    y "Üzgünüm, [player]. Bu tamamen bir hataydı."
    "Monika'nın çekingen bir şekilde yanıma gelmeye başladığını fark ediyorum."
    show monika 3b at t21
    show yuri 1u at t11
        m "Burada her şey yolunda mı?"
    m "Tam olarak ne olduğunu anlamıyorum ama belki bunu kulüp odasının dışında konuşmak istersiniz?"
    m "Yani, önerimi kabul etmek zorunda değilsiniz, ama iyisin, değil mi?"
    mc "Biz iyiyiz, Monika."
    mc "Sadece… lütfen bunu kendi başımıza çözmemize izin ver."
    show monika 1a at thide 
    hide monika 
    "Monika sessizce başını sallayarak geri dönüp, Natsuki ve Sayori’yi sınıfın diğer köşesine yönlendiriyor."
    "Gerçekten başka kimseyi bu işe karıştırmak istemiyorum."
    y 2v "[player], ben…"
    mc "Bak, Yuri. Dedikodular fazla yayılmamış gibi görünüyor. Yayılmaya başlasalardı, herhalde daha fazla duyardık, değil mi?"
    "Tam olarak doğru olmayabilir, ama şimdilik böyle düşünüyorum."
    mc "Öncelikle sakinleşmemiz gerek. Okuldan sonra bir yere gidelim, ne dersin?"
    "Yuri hâlâ korkmuş görünüyor."
    y 2t "Emin misin?"
    mc "Evet! Bütün bunlardan kafamızı dağıtmak için güzel bir fırsat olacak."
    mc "Çünkü eğer dedikodularla ilgili bir şey yapmaya karar verirsek, önce sakin olmamız gerek, değil mi?"
    y 2v "Sanırım bu biraz stresimizi alır."
    y "Eğer gerçekten işe yarayacağını düşünüyorsan, o zaman kabul ederim."
    mc "Okuldan hemen sonra çıkabiliriz. Bir parka falan gideriz. Gayet güzel olur, değil mi?"
    show yuri 1s at t11
    stop music fadeout 3.0
    "Bunu söylesem de, sanırım Yuri kadar ben de endişeliyim. Bir randevunun işe yarayıp yaramayacağından emin değilim ama denemem gerek."
    "Edebiyat kulübü bittiğinde, Yuri ve ben birlikte kalkıp okuldan dışarı çıkıyoruz."
    "Birbirimize sahibiz. Sonunda her şeyin yoluna gireceğinden eminim."
    call yuriRoute_petrichor
    return

label yuriRoute_petrichor:
    scene bg park_rain with wipeleft_scene
    "Hafif bir rüzgar esiyor."
    "Güneş bulutların arasından süzülen ışıklarıyla havayı tam olarak ılıman hale getiriyor."
    "Burada sadece biz varız."
    "Burada sadece biziz, mükemmel bir park randevusu için."
    mc "Burası gerçekten güzel bir yer, değil mi, Yuri?"
    play music YurTheme fadein 3.0
    show yuri 2n at t11
    "Yanımda bankta oturan Yuri'ye dönüyorum."
    y 2m "Evet, burası gerçekten güzel bir yer."
    y "Ayrıca inanılmaz derecede huzurlu."
    mc "Evet. Aslında en güzel kısmı seninle vakit geçirmek."
    "Yuri'ye biraz daha yaklaşmasını işaret ediyorum."
    y "Gerçekten mi?"
    y 2o "Bunun uygun olduğundan emin misin?"
    mc "Tabii ki! Sonuçta biz randevudayız."
    y "Sanırım bu doğru…"
    show yuri 1q at f11
    "Yuri yavaşça bana daha yakınlaşıyor ve kolumu etrafına sarıyorum."
    mc "Burası harika, değil mi? Ya da en azından iyi, başka bir deyişle."
    y 3c "Evet, kabul ediyorum, gayet güzel."
    mc "Bunu düşündüm. İlk randevumuzda burayı seçmediğimi düşündüğüm için biraz üzgünüm ama neyse."
    y 2s "Böyle küçük şeyler için bile üzülecek kadar düşünceli olman…"
    y "Senin için hislerim giderek daha da güçleniyor, [player]."
    show yuri 1p at t11
    "Bunu söyledikten sonra, Yuri hızla uzaklaşıyor."
    mc "Vay! İyi misin, Yuri?"
    y 1o "Bu kadar ileri gitmek çok mu cesurca oldu?!"
    y "Bununla seni hızlı bir şekilde ilişkiye sokmaya çalıştığımı mı düşünüyorsun?"
    y "Çok üzgünüm, [player]."
    mc "Hayır, Yuri. Ben tamamen sorun değilim."
    mc "Aslında bunu romantik buluyorum."
    y 1t "Emin misin?"
    mc "Evet, Yuri. Eminim."
    "Yuri yavaşça geri kayıyor."
    show yuri 1t at f11
        y "Bana kızmadığın için teşekkür ederim, [player]."
    y 1v "Biliyorsun değil mi, o dedikoduların gerçek olmadığını? Bunu söylediğini duydum ama, yanılıyor olmanı kınamam…"
    mc "Hiçbir dedikodu, sana olan duygularımı değiştiremez, Yuri."
    mc "O insanlar ne düşünürse düşünsün, bunun doğru olmadığını biliyorum."
    mc "Seni seviyorum, Yuri. Önemli olan tek şey bu."
    y 1b "Ben… Teşekkür ederim, [player]."
    "Gün yavaşça ilerlerken, Yuri ve ben parkta oturuyoruz, zaman zaman birbirimize konuşuyoruz ama çoğunlukla huzurlu sessizliğin ve birbirimizin keyfini çıkarıyoruz."
    mc "Biliyorsun, Yuri, biraz önce söylediklerinle ilgili…"
    mc "Sanırım ben de sana olan duygularımın güçlendiğini hissediyorum."
    y 1f "Gerçekten mi?"
    "Yuri şaşırmış bir şekilde bakıyor."
    mc "Evet! Gerçekten çok güzel özelliklerin var. Şiire duyduğun tutku gibi şeyler gerçekten çok etkileyici."
    y 2v "Beni çok şımartıyorsun, [player]."
    y "Ama bu, senin hakkında sevdiğim bir şey de."
    y "Ne kadar derinlemesine ilgileniyor olursam olayım, bana olan saygını seviyorum…"
    show yuri 3s at f11
    "Yuri gözlerini bana dikip yaklaşmaya başlıyor. Ben de aynı şekilde yaklaşırım."
    show yuri 3s at face(y=600) with dissolve
    "Dudaklarımız neredeyse birkaç santim uzaklıkta."
    "Biraz daha yakın…"
    show white
    stop music
    play sound thunder

    "{i}KRA-BOOM.{/i}"
    hide white
    play sound rain
    "Kahretsin."
    mc "Ne? Yağmur yarına kadar yağmayacaktı ki!"
    "Hava aniden yıldırımlar eşliğinde açılıyor ve üzerimize yağmur yağmaya başlıyor."
    scene bg residential_rain with wipeleft_scene
    "Yuri'nin elini tutup, sokaklardan koşarak bir yer bulmaya çalışıyorum."
    "Neyse ki biraz da olsa barınacak bir yer bulabiliyoruz."
    mc "Aman Tanrım…"
    show yuri 1v at f11
    y "Ah… Keşke daha önce deneseydim. Üzgünüm, [player]."
    mc "Hayır, sorun değil. Sadece beklediğim bir şey değildi."
    "Yağmur daha da şiddetle yağmaya başlıyor."
    mc "Şimdi ne yapıyoruz?"
    y 3q "Evinizde biraz daha vakit geçirebiliriz."
    y 3p "Sadece istersen tabii! "
    "Yuri biraz utanmış görünüyor ama yine de söylediklerini anlıyorum."
    mc "Evet, evime gidebiliriz."
    mc "Yağmur daha da kötüleşmeden kalkmamız iyi olur."
    y 3q "Katılıyorum."
    
    scene bg house_entrance_night with wipeleft_scene
    "Evime doğru koşarken, ön kapımı açıyorum ve içeri giriyoruz."
    stop sound fadeout 3.0
    mc "Burası çok daha iyi."
    mc "Bir yer ister misin, Yuri?"
    show yuri 1b at t11
    y "Eğer bana bir yer teklif ediyorsan, reddetmek kaba olurdu."

scene bg home_interior_night with wipeleft_scene
    show yuri 1a at s11
    "Yuri, oturma odasına doğru yürüyüp kanepeye oturuyor, ben de yanına oturuyorum."
    "Kanepe ıslanacak ama şu anda bu konuda endişelenmeyecek kadar umurumda değil."
    mc "Vallahi yağmurun yağacağını bilseydim, şemsiye getirirdim."
    "Yuri titriyor."
    y 1b "Sorun değil, yağmurun yağacağını bilemezdiniz."
    mc "Biliyorum, ama yine de. Gerçekten üşüyor gibisin."
    "Yuri biraz titrediğini fark ediyor."
    y "Bununla idare edebilirim..."
    show yuri 3p at h11
    y 3p "Umarım kanepeyi ıslatmamışımdır!"
    "Yuri hızlıca kalkmaya çalışıyor."
    mc "Hey, sorun değil. Lütfen geri otur. Benim için bir kanepe önemli değil, senin sağlığın önemli."
    show yuri 2u at s11
    "Yuri isteksizce ama yavaşça tekrar oturuyor."
    mc "Al."
    "Ceketimi çıkarıp, Yuri'ye veriyorum."
    y 3o "Ne?"
    mc "Giy onu. Dış tarafı ıslak ama iç tarafı hala sıcak."
    y 2v "Emin misin?"
    mc "Evet. İşte bu yüzden veriyorum."
    y 3c "Anladım... Teşekkür ederim, [player]."
    mc "Kız arkadaşımın donmasına izin veremem, değil mi?"
    "Yuri sessizce gülüyor."
    y 1b "Yağmur fırtınası randevumuzu mahvetmiş olsa da, yağmurun sesi inanılmaz, değil mi?"
    mc "Buna ne kadar dikkat ettiğimi bilmiyorum, ama bir şekilde hoş bir şey gibi."
    y "Evet. Sürekli damlayan damlaların büyüklüğü, şimşeklerin uğuldayan sesiyle birleştiğinde... Gerçekten güzel."
    mc "Nereden geldiğini anlayabiliyorum ama--"
    mc "Ne?!"
    show yuri 3n at f11
    "Yuri'nin kolları sıkıca etrafımda."
    y "Sen de üşüyorsun, [player]."
    y "Neden birbirimizi ısıtmayalım?"
    y 3o "Bunu yaptığım için bana daha sonra kızabilirsin ama en azından bir denemek istedim."
    mc "Yani, tabii? Benim için bir sakınca yok."
    "Kollarımı Yuri'nin etrafına sarıyorum."
    "Birkaç anlamda işler kesinlikle ısınıyor."
    show black with close_eyes
    "Yaklaşık yirmi dakika kadar orada kalıyoruz, sadece yağmurun düşüşünü dinliyoruz."
    
    "{i}BZZT!{/i}"
hide black with open_eyes
    "Cebimden bir bildirim titreşiyor."
    "İçgüdüsel olarak telefonumu çıkarıp yeni bir e-posta mesajı aldığımı görüyorum."
    y 3f "[player]?"
    mc "Sadece bir şey, bir e-posta. Hızlıca okuyacağım."
    show yuri at thide 
    hide yuri
    "Ama bu e-posta'ya göz attığımda, bir şey çok {i}çok{/i} yanlış."
    
    "{i}Konu: Sapık Uyarısı!{/i}"
    "{i}Yuri'nin ne kadar sapık olduğunu hepiniz biliyorsunuz, değil mi? Yani, hepimiz izledik o izleri ve onun nasıl davrandığını da biliyoruz.{/i}"
    "{i}Kendini kesmekten zevk alıyor! Bunu düşündüğünüzde biraz garip, değil mi? Aslında, bunu düşünmeseniz bile, ama işte.{/i}"
    "Ah, hayır."
    
    "{i}Neyse, o bir kaybeden, tamam. Her okulda böyle sapıklar vardır.{/i}"
    "{i}Ama daha da garip olan şey ne biliyor musunuz? Yuri, [player] ile çıkıyor. Evet, doğru duydunuz, arkadaşlar.{/i}"
    "{i}Bu okulda biri ya çaresizdi ya da Yuri gibi bir sapıkla çıkmaya cesaret edecek kadar sapıktı.{/i}"
    "Hayır hayır hayır hayır."
    "Lütfen, hayır."
    "{i}Ama gerçekten, tahmin edebiliyor musunuz, ikisinin ne korkunç şeyler yaptığını? Bence birbirlerini kesmekten zevk alıyorlar!{/i}"
    "{i}Bu yasal mı? Muhtemelen değil, ama dürüst olalım, onları umursar mı? Gerçekten komik ama aynı zamanda gerçekten iğrenç ve korkunç.{/i}"
    "Bunu neden okumaya devam ediyorum? Neden bu hepsi kötü bir rüya değil?"
    "{i}Ve biliyor musunuz? Şimdi bunu görüyorum. Birbirlerini kesip bitirdikten sonra, Yuri iyice tahrik oluyor.{/i}"
    "{i}Ve sonra--Bu cümleyi bitirmem, ama ne yapacaklarını tahmin ediyorsunuz, değil mi? Bahisleri koymaya hazırım. Gerçekler burada, arkadaşlar.{/i}"
    "..."
    "{i}Hatta, Yuri'nin diğer sapkınlıkları hakkında bahis bile koymaya hazırım. Kan oyunları belli, ama ya diğerleri?{/i}"
    "{i}Muhtemelen daha da iğrenç bir şey. İdrar mı? Ondan daha azını beklemiyorum. [player]'ın sapkınlıkları ne, acaba? Daha iyi ya da daha kötü mü?{/i}"
    "..."
    "..."
    "{i}Bir şekilde, tüm bunları öğrendiğim için mutlu oluyorum. Hepinizin kendinizle ilgili kötü hissettiğini biliyorsunuz, değil mi?{/i}"
    "{i}Ama bu tür sapıkların varlığını bilmek… bu beni biraz daha iyi hissettiriyor, açıkçası.{/i}"
    "{i}Umarım sizler de kendinizi daha iyi hissedersiniz, çünkü insan çöpü değilsiniz.{/i}"
    "..."
    "{i}Evet, bu yüzden sadece herkesi uyarıyorum. Uzun lafın kısası, Yuri'den ve [player]'dan uzak durun.{/i}"
    "{i}Belki de birbirlerini kesmek için canları sıkıldığında, yakındaki herkesi keserler, o yüzden hepinizi güvende tutmak istiyorum, tamam mı?{/i}"
    
    "Bu… gerçek olamaz."
    "Telefonuma bakıyorum ve… tabii ki."
    "Tabii ki bu mesaj okuluma gönderildi."
    "Başka bir şey olabilir miydi ki?"
    "Bunlar, altında yattığını düşündüğüm, beni aşan dedikoduların doğal bir ilerlemesi. {i}Bize{/i} ait olduğunu düşündüğüm dedikodular."
    show yuri 3b at t11
    y "[player]."
    show yuri at thide 
    hide yuri
    "Şu an buradayım. Ne yapmalıyım?! Mesaj, Yuri'ye de gönderildi mi?"
    "Eğer mesaj Yuri'ye de gönderildiyse, ne yapmalıyım? Ne yapabilirim ki?"
    "Kusacağım gibi hissediyorum... her şey berbat."
    "{i}BZZT!{/i}"
    "Bir başka bildirim alıyorum, ve bu ikinci bir e-posta."
    "{i}Konu: Ne var, sapık?{/i}"
    "Tabii ki, bu mesajı gönderen kişi, herkese e-posta yollayan o salak. Bu mesaj bana özel olarak gönderilmiş."
    "{i}Selam, [player]! Biliyorsun, adını kullanmayı planlamıyordum, ama okulundaki öğrencilerin sana dair neyin ne olduğunu bilmesi gerektiğini düşündüm.{/i}"
    "{i}Her halükarda, yeni takma adını seviyorsundur, değil mi?{/i}"
    "{i}Ama ciddiyim, nasılsın? Eminim sen ve kız arkadaşın, her zamanki gibi kendinizi kesiyorsunuzdur.{/i}"
    "{i}Yani, eğer rahatsız ediyorsam özür dilerim, eğer böyle bir şey oluyorsa tabii.{/i}"
    "{i}Her neyse, diyordum ki, kız arkadaşına e-postayı göndermedin, değil mi?{/i}"
    "{i}Ona göndermedim. Ama bunu bu mesajı gönderdikten sonra göndereceğim, yani…{/i}"
    "Okuduğum her cümle, fiziksel bir darbe gibi hissediyor, bir avuç bıçak göğsümde dönüyor."
    "{i}Tahmin ediyorum ki panik içindesin, değil mi? Ama hey, biz de seni korkutuyoruz, bu yüzden aslında bu bir tür karma.{/i}"
    "{i}Bu e-postayı bugün erken yazmıştım, yani şu anki yüzünü düşünerek.{/i}"
    "{i}Şimdi, belki bunu senden bir şey almak için yaptığımı düşünüyorsundur, ama gerçekten öyle değil. Dediğim gibi, herkesi güvende tutmaya çalışıyorum.{/i}"
    "{i}Biliyorum ki sen ve Yuri gibi hastalar güvenilmez. Yani, sadece Yuri ile değil, başka bir adamla da bu yola girdik, değil mi?{/i}"
    "{i}Sadece doğru olanı yapıyorum. Anlıyor musun?{/i}"
    "Ben… ben…"
    "{i}Ama yeter bu kadar benden. Bu mesajı bitirdikten sonra, kız arkadaşının telefonunda harika bir melodiyi duyacağından eminim.{/i}"
    "{i}O melodinin ne için çalacağını merak ediyorum. Bildirimi ne içerecek?{/i}"
    "{i}Bunun ne olduğunu tahmin edebiliyorsundur, değil mi? Gerçekten o kadar aptal değilsindir, değil mi? Ama şaşırmam, neyse.{/i}"
    "{i}Asıl soru şu… nasıl tepki vereceksin?{/i}"
    "{i}Tamam, şimdi bitti. Görüşürüz, sapık! Ve lütfen, bir duş al, olur mu? Teşekkürler.{/i}"
    "Yuri'nin telefonunun titreşmesiyle içim bir düğüm oluyor."
    "{i}BZZT!{/i}"
    y 1e "Hmm? Sanırım bir bildirimim var…"
    "Bu kararın iyi bir şey olup olmadığına karar verecek vaktim yok, ama hemen telefonunu almak için Yuri'den önce ekranı açmaması için acele ediyorum."
    "Yuri şaşkın, ama ben onu pek umursamadan, mümkün olduğunca hızlı bir şekilde aldığı e-postayı silmeye çalışıyorum. {i}Öğrenci topluluğundan dostane bir mesaj.{/i} Tabii ki."
    y 1f "[player]? Ne yapıyorsun telefonumla?!"
    "Birkaç kaydırma, ve silindi, sanki hiç var olmamış gibi. {i}Sanki.{/i}"
    "Şimdi sadece bir bahaneye ihtiyacım var."
    mc "Üzgünüm! Bu bir spam e-postasıydı. Aynı başlıkla bir tane de ben almıştım, bu yüzden sana da aynısının gelmiş olabileceğini düşündüm. Tahminim doğruymuş gibi görünüyor."
    show yuri 1h at f11
    "Yuri şüpheli görünüyor."
    y "Gerçekten?"
        mc "Evet, gerçekten. Söz veriyorum, Yuri. Endişelenecek bir şey yok."
    y 1f "Kesin olduğundan emin misin?"
    mc "Eminim."
    "Zaten bir hata yaptım. Yakında bunun sonuçlarıyla yüzleşeceğim."
    y "Hmm..."
    y 2v "[player]..."
    mc "Önemli bir şey değildi. Ayrıca, gerçekten senin telefonunla bir şey yapmayı isteseydim, bunu üç saniyede halletmezdim."
    y 1f "Şüpheli davranıyorsun, [player]."
    y "Bunu kendin de fark ediyorsun."
    mc "Hadi... hadi geçelim, tamam mı? Üzerinde durulacak bir şey yok, neden zaman kaybedelim ki?"
    show yuri at thide
    hide yuri
    "Ama biliyorum, bunu yapamam. O e-postayı okuduktan sonra hiçbir şey eskisi gibi olmayacak."
    "Biliyorum ki, {i}hiçbir şey{/i} aynı olmayacak o e-postayı okuduktan sonra."
    show black with close_eyes
    call yuriRoute_shatter
    return

label yuriRoute_shatter:
    pause(2.0)
    scene bg corridor with open_eyes
    play music Amber fadein 3.0
    "--Pazartesi. Artık gerçeğiyle yüzleşme zamanı."
    "Şu ana kadar, Yuri okulda yayılan zincir e-postayla ilgili hiçbir şey fark etmedi, ama bu sadece bir zaman meselesi."
    "Bunu temizlemem gerek, Yuri fark etmeden önce."
    "Bunu yapabileceğimi bile sanmıyorum, ama denemeliyim. Onun o durumu fark ettiğinde yüzünü görmek dayanılmaz olur. O konuşmanın nasıl gideceğini tam olarak biliyorum."
    "Telefonum titriyor, mesaj. Yuri."
    $ o_name = "Telefon"
    o "Bugün bizim usual yerde seni görmedim. Okula gidiyor musun?"
    scene bg club_day with wipeleft_scene
    "Gerçekten bugün okula aceleyle gittim, düşündüğümde."
    "Hızla yerine oturuyorum ve kısa bir yanıt yazıyorum."
    mc "Evet--ders başlamadan önce öğretmenle bazı işlerim vardı. Üzgünüm!"
    p "Tamam. Seni seviyorum, [player]."
    "Telefonu cebime geri koyuyorum ve hafifçe nefes alıyorum. Planım hazır. İlk iş olarak e-postanın kaynağını bulmalıyım."
    "Ve eğer sezgilerim doğruysa, tam olarak nereden başlamam gerektiğini biliyorum."
    play sound crowds fadein 3.0
    scene bg corridor with wipeleft_scene
    
    mc "Hey."
    "Yuri hakkında beni uyaran çocukla konuşmak, bana birkaç ipucu verebilir gibi görünüyor."
    
    "Çocuk bir an için şaşırmış gibi görünüyor ama sonra nötr bir ifadeyle elini kaldırıyor."
    $ o_name = "Kıdemli"
    o "Selam, [player]."
    mc "Merhaba."
    "Konuşma, eğer buna konuşma denirse, bir türlü ilerlemiyor."
    "Muhtemelen şüpheli davrandığımı fark etti. Şimdi benden ilk hamleyi yapmamı bekliyor."
    "Kaşlarımı çatıyorum."
        mc "Son zamanlarda garip e-postalar aldın mı?"
    "Gözlerini kırpıyor, sonra başını sallıyor."
    o "Hiçbir şey olağan dışı değil, dostum."
    stop sound fadeout 2.0
    "Omuz silkerek bitiriyor, o kadar iyi bir şekilde geçiştiriyor ki, ona ilk şüpheyle yaklaşmamı sorgulamaya başlıyorum."
    "Şüpheler yavaşça kafama sızarken sessizce başımı sallayarak sınıfıma doğru yürümeye başlıyorum."
    scene bg class_day with wipeleft_scene   
    "Sonuçta, her zaman başkaları da olabilir--ve ben etrafımda her yönüyle kör bir şekilde koşuyordum..."
    "Bir şeyi gözden kaçırmış olabilirim... bariz bir şeyi."
    "Ama başka kimin bunun gibi bir şansı olabilir ki?"
    scene bg class_day with wipeleft_scene    
    
    play sound bell
    "İşte, günümün yarısı geçti."
    "Başımı masadan kaldırıyorum, daha önce sadece zaman geçiriyordum. Tarih dersi sıradaki dersim, o yüzden onun için malzemelerimi hazırlamam gerek."
    "Öğleden sonra bilgi toplamaya karar verdim. Edebiyat Kulübüne gitmeyi atlayacağım, ama bence bu iyi bir sebep."
    play sound closet_open
    stop music
    "Sınıfın arka kapısı açılıyor ve {i}o{/i} geri giriyor, ardından bir grup çetesini takip ediyor."
    "Çok yargılayıcı olmamaya çalışıyorum."
    "Başarısız oluyorum."
    o "Aslında hepsi benim yüzümden değildi--"
    $ o_name = "Diğer Öğrenci"
    o "Tabii ki değildi. Ama çocuk sana yüklenmedi mi? En azından bize öyle söylemiştin."
    "Omuz silkiyor. Aynı küçümseyici, alaycı omuz silkme hareketi."
    $ o_name = "Kıdemli"
    o "Yani, ona uyarı yapmaya çalıştım, değil mi?"
    o "Bu sadece aklıma gelen eğlenceli bir fikir, biliyor musun? Uzun zamandır iyi bir zincir e-posta görmemiştim."
    $ o_name = "Diğer Öğrenci"
    o "Evet, doğru söylüyorsun, doğru."
    $ o_name = "Kıdemli"
    o "Kim bilir, belki o buna ilgi duyuyordur. Kesme fetişi mi? Neydi o, ne derler ona?"
    $ o_name = "Diğer Öğrenci"
    o "Sanırım... kan oyunları gibi bir şey?"
    $ o_name = "Kıdemli"
    o "Evet, o. Dur, sen bunu nasıl biliyorsun, heee?"
    "Bir başka çocuk gülerek burnundan nefes alıyor."
    $ o_name = "Diğer Öğrenci"
    o "Muhtemelen düşük özgüvene sahip birini hedef alıp kolayca yenmek için yaptı."
    show red with dissolve:
        alpha .3
    "Kanım kaynamaya başlıyor."
    "Kızgın bir şekilde ayağa kalkıyorum ve çocukların huddle olduğu yere doğru yürüyorum. Sadece sarışın olan, bu kaosu başlatan çocuk, bir tek o başını kaldırıp bana bakıyor."
    "Bana bakıyor ve yüzü, kafası karışık ve gülerek karışmış bir şekilde değişiyor."
    $ o_name = "Kıdemli"
    o "Yo, [player]. Nasıl gidiyor?"
    
    "Artık dinlemeyeceğim."
    
    show red with dissolve  
    window hide 
    pause(3.0)
    scene black with wipeleft_scene 
    window show
        $ o_name = "Müdür"
    o "Yani... o zaman ona yumruk attın."
    "Sarışın çocuk burnundan gülerek, kollarını kavuşturuyor. Müdür onun tarafında, bu da demek oluyor ki, benim söylediklerim önemsiz."
    "Başlatan ben oldum, o yüzden beklenmedik bir şey değil."
    "Sessizce başımı sallıyorum."
    o "Bir kereden fazla, eklemeliyim. Görgü tanıklarına göre, onu öldürmeye çalışıyormuşsun gibi görünmüş."
    "Kaşlarımı çatıp, kravatının düğümüne odaklanıyorum."
    mc "Özür dilemeyeceğim."
    "Şişman müdür, gözlüklerini çıkarıp parmaklarını birbirine geçirerek derin bir nefes alıyor."
    o "Dedikoduya dayalı hareket edemem, ama kavga başlatmak ciddi bir suç."
    o "Ve senin için..."
    "Müdür, çocuğa bakarak konuşmaya devam ediyor."
    o "...gidebilirsin. Eğer gerekirse hemşireye görün."
    "Ona, başını sallar gibi yaparken çektiği acıyı görmek biraz tatmin edici. Çocukça ama ne yapalım, elimde olanla yetineceğim."
    o "[player]."
    "Ah, ne güzel."
    o "Sana iki günlük bir uzaklaştırma veriyorum. Eşyalarını topla ve ailenle iletişime geç."
    "Yorgun bir şekilde derin bir nefes alıyorum, başımı sallayarak geri cevap veriyorum."
    mc "Evet, efendim."
    o "Ve bir dahaki sefere öfkeni kontrol etmeye çalışır mısın?"
    "Dudağımın içinde dişlerimi sıkarak bir cevap vermek üzereyim, ama bunun yerine topuklarımla dönüp çıkıyorum."

    scene bg bedroom with wipeleft_scene    

    "Beklediğim gibi gitti aslında."
    "Yatakta sırt üstü yatarken tavana bakıyorum. Telefonum yaklaşık beş dakikadır sürekli titriyor. Şüphesiz Sayori, durumumu öğrenmeye çalışıyor. Derste mesajlaşmak mı? Onu azarlamam gerek."
    "İlginin değerini takdir ediyorum, ama şu anda sadece sessizlik istiyorum."
    "Bunu nasıl halledeceğimi çözmem gerek, çünkü inanılmaz bir şekilde aptallık yaptım."
    "Kendi öfkemde o kadar boğuldum ki, gerçek amacımı unuttum."
    "Demek ki - belki şanslıysam, başlattığım kavga onlara başka bir dedikodu konusu verir..."
    "Ama öğrenciler hakkında bildiğim bir şey varsa, bu sadece ana hikayeye ek materyal olarak eklenir."
    "Sonunda telefonum titremeyi kesiyor."
    "Yanıma dönerken, yatakta örtülere büzülüp kalıyorum."

    call yuriRoute_aftermath
    return