label sayoriRoute_start:
    
    $ persistent.sayoriRouteStarted = True
    stop music fadeout 3.0
    s "[player], bekle!"
    $ sayori_affection = 0
    "Tam çıkmak üzereyken, o bana sesleniyor."
    "Sesinden ne kadar kararsız olduğunu anlayabiliyorum."
    show sayori 4bg at f11
    s 4bh "Lütfen... gitme. Çok korkuyorum. Her şeyin değişmesini istemiyorum. Seni kaybetmek istemiyorum ama..."
    s "Bunun bir parçası olmanı istemiyorum! Zamanını boşa harcamamanı istiyorum."
    mc "Sayori..."
    show sayori 4bk at f11
    "Gözlerinin içine bakıp ona burada olduğumu göstermek için gülümsüyorum."
    "Hatta beynim, Sayori'nin--en yakın arkadaşı--benden yıllardır böyle bir şey saklamış olmasına alışmaya çalışırken, bunu anlayacak kadar zamanım olmadı."
    "Belki de onunla bir süre kalırsam, durumu daha iyi kavrayabilirim."
    mc "Endişelenmene gerek yok. Yavaşça ilerleyelim."
    s 4bl "[player]?"
    mc "Ne yapacağımı bilemiyorum. Depresyon hakkında fazla bir şey bilmiyorum, ama bildiğim bir şey var: Sen benim en iyi arkadaşımsın."
    mc "Eğer seni terk edersem, ne kadar kötü bir arkadaş olurum ki?"
    s 4bk "..."
    "Sayori gözlerini aşağıya indiriyor, sonra cesur bir yüz ifadesiyle tekrar bana bakıyor."
    show sayori 4bt at f11
    "Onun gözlerinden, ağlamamak için kendini zorladığını görebiliyorum."
    "Sonra, farkında olmadan, kollarımı etrafına sarıyorum."
    "Onun sıcaklığını hissediyorum, o ağlarken benim göğsüme."
    "Nedensiz bir şekilde, kendimi ağlama isteğimi bastırmak zorunda hissediyorum."
    "Onun için güçlü kalmaya çalışıyorum."
    "Ama dürüst olmam gerekirse, biraz korkmuş durumdayım."
    hide sayori 
    show black 
    with dissolve_cg
    
    play music Rainclouds fadein 3.0
    "On dakika sonra, Sayori hâlâ benim göğsümde ağlıyor."
    "Bir tek kelime bile etmiyor."
    mc "Neden ağlıyorsun?"
    
    s "Sadece susmalıydım... Şimdi aramızda her şey sonsuza kadar değişecek..."
    "Zihnindeki çatışmalar, yüzünden belli oluyor. Onu bu halde bırakmam gerektiğini fark ediyorum, ne yapacağımı bilmesem de. En azından, ona ağlaması için bir omuz sunabilirim."
    mc "...Bilmiyorum. Ama sanırım yanılıyorsun."
    s "Yanılıyor muyum?" 
    mc "Sen depresyonda olsan da, yine de seninle arkadaşlık yapardım."
    s "Ama... neden?" 
    "Kendim de bilmiyorum. Sadece söyledim, fazla düşünmeden."
    "Bir kaç dakika boyunca, sadece orada duruyoruz, sarılmış bir şekilde. Hiçbirimiz bir şey söylemiyoruz."
    "Duyabildiğimiz tek şey, kendi nefeslerimiz. Ve bazen, birisinin kalp atışlarını duyduğum gibi hissediyorum."
    "Bilmiyorum, bu benimkisi mi, yoksa Sayori'ninki mi?"
    "Zihnimde bir sürü düşünce hızla geçiyor, durumu tam olarak kavramaya çalışıyorum."
    mc "Bana güveniyor musun, Sayori?"
    "Sayori yavaşça başını sallıyor."
    s "Sen benim en iyi arkadaşımsın... Sana herkesten daha fazla güveniyorum. Ama hâlâ bilmiyorum... korkuyorum... Senin benim için ne kadar önemli olduğunu düşündükçe daha çok korkuyorum."
    
    "Saçlarını okşuyorum."
    mc "Sen de benim en iyi arkadaşımsın. Seni asla bırakmam."
    "Kafam karışmış olsa da, bu sözlerin samimi olduğundan eminim."
 
    scene bg sayori_bedroom with dissolve_cg 

    show sayori 1bl at f11
    s "Bu kadar dağınık olduğum için üzgünüm."
    mc "Bunun için özür dileme. Bundan sonra her şey daha iyi olacak."
    s 4bn "Huh?"
    mc "Sana yardım etmek istiyorum, Sayori."
    "Sayori aniden bana dönüyor."
    s 4bw "[player]! Hayır, lütfen zamanını ve enerjini bana harcama!"
    mc "Ama Sayori--"
    "Güvenle gülümsüyorum ve gözlerinin derinliklerine bakıyorum."
    mc "--Seninle olmak zaman kaybı değil. Hiçbir zaman olmadı, hiçbir zaman da olmayacak."
    s 1bu "Ama... neden?"
    mc "Hayatımız boyunca arkadaş olduk. Seni yalnız başına geçirecek bir şey bırakmam."
    "Sözlerime rağmen, Sayori'nin ifadesi değişmiyor gibi görünüyor. Derin bir nefes alıyor."
    s 1bk "Bana yardım edemezsin. Anlamıyorsun... depresyon sadece üzgün olmakla aynı şey değil."
    mc "Belki edemem, belki edebilirim. Ama denemek istiyorum."
    "Sözlerim ona ulaşmış gibi görünüyor. Dudaklarının hareket ettiğini, karşı bir şey söylemeye çalıştığını görüyorum. İşte bu fırsatım--onu bu kadar söylemeden önce, son darbeyi yapıyorum."
    mc "Haklısın. Depresyon hakkında hiçbir şey bilmiyorum. Senin için neyin iyi olduğunu bilmiyorum ve bu beni korkutuyor, ama seni bırakmak için bir neden değil bu. Sadece... bana güven, olur mu?"
    "Sayori, sanki benden şüphe arar gibi bakıyor, sonra aniden, yüzünde bir gülümsemenin gölgesi beliriyor."
    s 1bt "Tamam."
    "O bilmediğim gülümsemenin küçük bir kısmı, Sayori'nin yüzüne geri dönüyor."
    mc "Bundan sonra, bunu birlikte yapacağız."
    "Depresyon hakkında hiçbir şey bilmesem de, Sayori'ye yardım etmeye kararlıyım."
    "O her zaman benim yanımda oldu, ben üzgünken, kendisinin ne kadar yıprandığını hiç belli etmeden..."
    "Bilgim olmasa da, ona yardımcı olmak için kararlıyım."
    mc "Festival yarın."
    s 1bl "Evet..."
    "Tam o sırada, bir fikir aklıma geliyor."
    mc "Hadi birlikte hazırlanalım."
    s 1bk "Ben...?"
    mc "Seninle birlikte hazırlanmak istiyorum."
    s 4bl "Bunu istiyorum, ama kendimi bencil hissetmek istemiyorum..."
    mc "İkimizin de istediği bir şeyse, bencillik değil."
    "Çok utandığımı itiraf edemesem de, gerçekten onunla daha fazla vakit geçirmek istiyorum."
    "Hatta, ona söyledikleriyle başa çıkmanın bir yolu olarak bile görsem."
    "Neredeyse, bu durumdan daha iyi anlamam için her şeyin önceden olduğu gibi kalmış olduğuna kendimi inandırmam gerektiğini düşünüyorum."
    "O hala en iyi arkadaşım. Tek arkadaşım. Bu değişmedi."
    "Bunun asla değişeceğini düşünmüyorum."
    "Ironik bir şekilde, şimdi depresyonda olduğunu bildiğim için, ondan önce olduğumdan daha fazla zaman geçirmek istiyorum."
    s 1bw "Tamam, haklısın... ama başka planların yok muydu?"
    "Başımı sallıyorum."
    mc "Hayır, ve hatta olsaydı bile, diğerleri durumu anlayacaktır."
    "Bundan başka, şu an onun yanında olmam gerektiğini hissediyorum."
    "Ona güven verici bir gülümseme yapmaya çalışıyorum, ama şu anda kafamda, korkunç bir korku romanından fırlamış gibi görünüyorum."
    mc "Hadi bunu her zaman yaptığımız gibi yapalım, Sayori!"
    s 4bt "Tamam!"
    "O hâlâ üzgün görünse de, biraz olsun sakinleşmiş gibi hissediyorum, belki de sadece hayal gücüm."
    "Belki de sadece, beni gitmeye çağırmadığı için rahatlamış hissetmem."
    hide sayori
    show black 
    with dissolve_cg
    "Onunla birlikte akşamın geç saatlerine kadar şiirini yazıyoruz. O yazarken, ben Monika'ya bir mesaj gönderip, bazı planları değiştirmemiz gerektiğini söylüyorum."
    "Hızla, durumu anladığını ve geri kalanını halledeceğini belirtiyor."
    "Akşam boyunca, Sayori'nin eski kişiliğinden ara sıra parlamalar görüyorum, ama bunun gerçekten onun eski hali mi yoksa sadece benim için bir maske mi olduğunu bilmiyorum."
    "Sonunda, kendimizi tükenmiş hissediyoruz ve ancak karınlarımız guruldamaya başladığında, kaç saat geçirdiğimizi fark ediyorum."
    "Ona bir şeyler yemek yapmaya karar veriyorum, itirazlarına rağmen."
    scene bg kitchen with wipeleft_scene
    show sayori 4bx at f11

    s 4bx "Bu çok lezzetli, [player]! Böyle bir yemeği... sanırım hiç bu kadar iyi bir şey yememiştim."
    mc "Beğenmene sevindim. Elimden geleni yaptım."
    "Yemek hazırlarken, neredeyse tüm yediği yemeklerin ya fast food ya da hazır noodle olduğunu fark ettim."
    "Aslında, buna geçmişte onun bana hep servis ettiği yemeklerin de bu olduğunu hatırlıyorum."
    "Şimdi anlıyorum, büyük ihtimalle depresyonu yüzünden yeni yemekler denemiyordu."
    "Ama ne olursa olsun, Sayori yemeğimi çok sevdi ve hızla yedi."
    "Neredeyse boğazına takılacak gibi endişelendim."
    s 1bw "[player], iyi misin?"
    "Sayori, karnımın çok aç olmasına rağmen tabağımı hiç dokunmadığımı fark etti. Onun için endişelendiğimi gizlemek için çaresizce bir esneme yapıyorum."
    mc "Evet, iyiyim. Sanırım biraz yorgunum."
    s 3bg "Eğer istersen, eve gidebilirsin. Şiiri ben bitiririm."
    mc "Hayır, kalacağım. Seninle olmak eğlenceli."
    s 1bl "Eğlenceli mi?"
    "Bitter bir şekilde gülümsüyor."
    mc "Bunu seviyorum-- sadece oturup seninle şiir yazmak. Biraz eğlenceli, değil mi?"
    s "Teşekkür ederim."
    "Sessizce yemek yerken, aramızdaki hiçbir dramın olmadığı eski zamanları ne kadar çok özlediğimi fark ediyorum."
    "Son yıllarda seninle daha fazla vakit geçirmediğime üzülüyorum. Belki o zamanlar, her şey böyle gitmezdi."
    "Belki ona yardımcı olabileceğim bir şeyler yapabilirdim, keşke o ipuçlarını fark etseydim."
    "Nasıl fark etmedim ki, okula ne kadar geç kaldığını?"
    "Ya da hep aynı kıyafetleri haftalarca giydiğini?"
    "Ya da başkalarının hep kararlar almasına izin verdiğini?"
    s 2bh "Kendini suçlama."
    "Bana kararsız bir şekilde bakıyor."
    s "Yüzünden belli. Muhtemelen benden uzak olduğum için kendini suçluyorsundur, değil mi?"
    mc "Beni bu kadar mı kolay okuyorsun?"
    "Sayori gülümsüyor."
    s 1bt "Yapabileceğin bir şey yoktu ki."
    "Başımı sallıyorum."
    play music Thoughts fadein 4.0
    mc "Buna inanmak istemiyorum."
    mc "Gerçek olsa da, bunu tek başına halletmeye çalışman gerçekten iyi sonuçlanmaz."
    "Sayori, sözlerim karşısında şaşkın bir şekilde sessiz kalıyor."
    mc "Depresyonun olsa da, hala seni önemsiyorum. Sana güvenebileceğimi kesin olarak söyleyebileceğim birkaç kişiden birisin."
    s 1bu "Bunu hak etmiyorum..."
    mc "Ne diyorsun? Tabii ki hak ediyorsun. Herkesin, onları önemseyen birisi olmalı!"
    s "Bu söylediğim değil..."
    s 4bw "Beni önemsemeni hak etmiyorum... Biri benim için çaba harcadığında, kendimi yük gibi hissediyorum."
    s "Kimseye yük olmak istemiyorum... özellikle sana."
    mc "Sayori..."
    mc "Sen benim için hiç bir yük olmadın. Ve asla olmayacaksın."
    s 1bg "Ama... ben..."
    mc "Bana arkadaş olmayı neden istediğini sormuştun... Hani senin ne kadar değersiz olduğunu fark ettiğinde?"
    mc "Ama biz arkadaş değil miyiz?"
    s 1bt "E...evet..."
    mc "Kendini değersiz hissettiğinde, ben nasıl hissediyorum sanıyorsun?"
    s 1bl "Tabii ki kötü hissediyorum... bu yüzden hiç bu konuda konuşmam."
    mc "Ama eğer sen mutsuzsan, ve ben de seni bu mutsuzluktan kurtarmak istiyorsam, aslında bunu kendim için yapıyorum, senin için değil."
    s "Evet... ama buradaki amacın ne?"
    mc "Eğer sana bir şey olursa, ben toparlanamam."
    mc "Sana borçlu olmanı istemiyorum."
    mc "Sana yardım etmek istiyorum çünkü bu, benim de mutlu olmamı sağlardı."
    s 1bw "Benim için bunu yapar mıydın? Neden?"
    mc "Çünkü benim için çok değerlisin Sayori. Sen de benim mutlu olmamı istiyorsun, ben de seni mutlu görmek istiyorum."
    mc "Ne seni mutlu eder, ne de senin değerini--hem bana hem de başkalarına--neyle fark ettirir, bilmiyorum ama benim için önemli olan bir şey var."
    s "O... O ne?"
    mc "Seninle daha fazla vakit geçirmek ve seni güldürmek."
    show sayori 4bm
    "Sayori şaşkın bir şekilde bakıyor."
    mc "Sen hep beni mutlu ettin, çünkü beni her zaman açık kollarla kabul ettin."
    mc "Üstelik, beni arkadaşı olarak çağırabileceğim tek kız sensin ve bunu söyleyebilmek beni mutlu ediyor."
    mc "Demek istediğim şu ki, seni kaybetmek istemiyorum."
    mc "Sana yardım etmek istiyorum. Bu beni mutlu eder."
    s 4bv "[player]... teşekkür ederim."
    s 4bd "Senin gibi bir arkadaşım olduğu için şanslıyım, [player]."
    s "Biri beni önemsediğini ve değer verdiğini bilmek güzel bir his."
    mc "Beni böyle hissettiren sensin. Her gün."
    "O gülümsemesine rağmen, yanakları kızarsa da, odada garip bir sessizlik oluyor."
    s "Geç oldu... Sanırım günü sonlandırmalıyız. Çok yorgunum ve düşünmem gereken şeyler var..."
    "Bana güven verici bir gülümseme atıyor."
    s "Ama merak etme. Vazgeçmeyeceğim. Sadece senin için bile olsa."
    mc "Teşekkür ederim. Bunu gerçekten takdir ediyorum."
    show black with dissolve_cg
    "Günü sonlandırıyoruz. Tam çıkarken, arkamdan duyduğum fısıldanan bir şey var."
    "...O gece, bir süre uyuyamadığımı fark ettim."
    "Beynime sürekli konuşmamız tekrar tekrar oynuyor."
    "Gerçekten ona yardımcı olabilir miyim?"
    "..."
    "Yarın festival günü."
    "Sayori, konuşmamızın ardından muhtemelen garip hissedecek. Gözlerimi açar açmaz hemen onu kontrol etmeliyim."
    "Sonuçta, o da benim yerimde olsaydı, bana böyle davranırdı."
    "Sonunda, göz kapaklarımın ağırlaştığını hissediyorum."
    "Uykudan önce son gördüğüm şey, Sayori'nin bana gülümsediği bir anı."
    "Onun gülümsemesinin hep bu kadar sahte olduğuna inanamıyorum."
    stop music fadeout 2.0
    
    scene bg bedroom with dissolve_cg
    "Bugün festival günü."
    "Böylesi bir gün için heyecanlanacağımı düşünmüştüm, ama neredeyse hiç uyumadım, heyecan dışında birçok sebepten dolayı."
    "Dün konuştuğumuz şeyleri düşünerek telefonumu çıkarıp Sayori'nin numarasını arıyorum, ama... cevap vermiyor."
    play music Dusk
    "Bir anda korku sarıyor beni – ya o...?!"
    "Düşüncelerimi tamamlamadan telefonum çalmaya başlıyor."
    "Yanıtlamaya çalışıyorum ama elimdeki stres yüzünden ellerim terlemiş, telefonum yere düşüyor."

    "Görüyorum, arayan o."
    "Hızla yere eğilip ekranı kaydırarak cevap vermeye çalışıyorum."
    s "[player]?"
    "Sesinden anlaşılan o ki, ya onu uyandırdım ya da hiç uyumamış ve bütün gece uyanık kalmış."
    "Bunu dolaylı yoldan sormaya karar veriyorum."
    mc "Üzgünüm, seni uyandırdım mı?"
    s "Hayır... Bir süredir uyanıktım."
    "Sesindeki ton, anormal şekilde neşeli bir hale bürünüyor."
    "Bir şeyler yolunda gitmiyor burada."
    s "Beni boş ver, eheh~"
    "Gülüşü zoraki gibi geliyor. Burada açıkça bir yanlışlık var."
    mc "Sayori..."
    s "Ne oldu?"
    "Birden korku beni sarıyor."
    "Bir şekilde onu oyalamam gerektiğini fark ediyorum, yoksa işler kontrolden çıkacak."
    "Sesinden açıkça üzgün olduğu belli, ve ne kadar yorgun olduğu düşünülünce hiç uyumadığını düşünüyorum."
    "Eğer şimdi ona telefonumu kapatacak olursam, kendisine ne yapabileceğini kimse bilemez."
    mc "Seni aramamın sebebi, festivalden önce görüşmek istememdi."
    mc "Her zaman birlikte okula gideriz, o yüzden... belki kahvaltıyı senin için yaparım?"
    "Hiçbir şey demiyor ama diğer tarafta derin bir iç çekiş duyuyorum."
    mc "Festival için birlikte gideceğimize söz vermiştik."
    s "... Bu, dün söylediğim şey yüzünden mi?"
    s "Beni böyle davranmana sebep olan şey o mu?"
    s "Ben..."
    mc "Hayır, sebep o değil."
    mc "Sadece festivalden önce seninle vakit geçirmek istiyorum."
    mc "Yani, o kadar erken kalktım ki... geçirecek pek zamanım yok, belki sadece anime izlerim."
    mc "Bana, NEET olmamı istemediğini söylemiştin, değil mi?"
    "Sayori telefonun diğer tarafından acı bir şekilde gülüyor."
    s "Haklısın. Tamamen haklısın!"
    mc "Ve tek arkadaşım sen olduğun için, başka kimsede vakit geçiremem. Ya seninle ya da anime ile!"
    s "Söylediklerini anlıyorum..."
    "Bir süre duraklıyor ve sonra bir kapı sesi duyuyorum, ardından ağır bir şeyin yere düşüşü ve kapının kapanması."
    s "Tamam, ne zaman gelirsin?"
    mc "Şu an yoldayım!"
    s "Tamam. Ben de gün için hazırlanayım – kapıyı senin için açık bırakacağım."
     
    scene bg home_interior with dissolve_cg
    pause(1.5)
    scene bg house_entrance with dissolve_cg
    pause(1.5)
    scene bg residential_day with dissolve_cg
    "Telefonu kapatıp kapıdan hızla çıkıyorum, bacaklarım beni ne kadar taşıyorsa."
    "Kapımı bile kapatmayı umursamıyorum, ya da yola bakmayı."
    "Kalbim göğsümden çıkacakmış gibi atarken, hızla Sayori'nin evine doğru koşuyorum ve oraya vardığımda gözlerimde siyah noktalar belirmeye başlıyor."
     
    show black with dissolve_cg
    "Ağır ağır nefes alarak kapıyı açıyorum – gerçekten de kapıyı açık bırakmış."
    "İçeri girdiğim anda, duşun su sesini duyuyorum."
    "Aramanın bittiği anda duyduğum sesleri hatırlayarak, hızla odasına koşuyorum."

    scene bg sayori_bedroom with dissolve_cg
    "Anime izlemekten bunun nereye gidebileceğini az çok tahmin ediyorum."
    "Ama umurumda değil."
    "Gerçekten de düşündüm. Kapı sesi duymuştum. Sonraki seslerden anladığım kadarıyla, ahşap zeminli bir oda olmalıydı."
    "Yani bu demek oluyor ki..."
    "Odanın kapısını açmadan önce, içimden ona affetmesi için dua ediyorum ve dolabını açarak dağınık kıyafetlerin arasından ellerimi geçiriyorum."
    "Belki de sadece hayal gücümün bir ürünüdür bu sesler?"
    "Bir süre hiçbir şey hissetmiyorum, derinlere doğru kazmaya devam ederken."
    "Tam pes etmek üzereyken, ellerim aniden sert ve düzensiz bir şeyin altına değiyor."
    "Onu kazıyorum ve gözlerim büyüyor, elinde uzun, sıkı bir ip tuttuğumu fark ediyorum."
    "Acaba o bunu amaçlamış mıydı?!"
    "Düşüncelerimi bitirmeden, ipi iki elimle kavrayıp hızla odayı geçiyorum ve ipi açık pencereden dışarı atıyorum."
    "Tam her şeyin bittiğini düşünürken, birden su sesi kesiliyor."
    "...Eğer Sayori beni odasında gezinirken görürse, berbat olacağımı fark ediyorum."
    "Hızla yaptığım şeyi örtbas edip odadan çıkıyorum."
    
    scene bg kitchen with dissolve_cg
    "Sonra kahvaltıyı hazırlamaya başlıyorum."
    "...Ve sessizce kendime söz veriyorum, bugün onun için eğlenceli geçmesi için her şeyi yapacağım."
    call sayoriRoute_theFestival
    return

label sayoriRoute_theFestival:


    scene bg club_day with dissolve_cg
    play music Bunkasai fadein 3.0
    show natsuki 4e at f11
    n "Vay be, sonunda geldiniz!"
    show natsuki 4c at t22
    show yuri 1f at f21
    y "Açıkçası, hiç gelmeyeceğinizi düşünmeye başladık..."
    show natsuki 4c at t33
    show yuri 1e at t31
    show monika 4b at f32
    m "Tamam, herkes sonunda buradaymış!"
    "Görünüşe göre ikimiz de son gelenleriz. Neyse ki etkinlik henüz başlamamış."
    show natsuki 4c at t44
    show yuri 1e at t42
    show monika 2a at t43
    show sayori 1l at f41
    s "Ehehe~ üzgünüm, hafta sonu boyunca şiirimi yazmayı unuttum."
    show sayori 1k at t41
    show monika 1b at f43
    m "Peki, şimdi hazır mı?"
    show monika 1a at t43
    show natsuki 4e at f44
    show sayori 1f at t41
    stop music
    n "Aman Tanrım, Sayori! En azından biraz ciddiyet gösterir misin?!"
    show natsuki 4c at t44
    show sayori 1k at t41
    "Sayori gözlerini yere indiriyor."
    hide monika 
    hide yuri 
    with wipeleft 
    show sayori 1k at t21
    show natsuki 4c at f22
    "Bu gerçekten kötü... Natsuki, Sayori'nin yazamama nedenini bilmiyor."
    "Sayori'ye söz vermiştim, durumunu gizli tutacağım diye."
    "Sayori'ye bir bakış atıyorum, gülümsemesi yavaşça soluyor."
    "...Bu hızla giderse, ağlamaya başlayabilir."
    "En kötü ihtimalle, sırrı açığa çıkacak."
    "Öte yandan, Sayori'nin buna dayanacak kadar güçlü olduğunu biliyorum. Eğer birdenbire garip davranmaya başlarsam, şüpheli olabilirler."
    "Konuşmak mı yoksa Sayori'nin dayanıklılığına güvenip sessiz mi kalmalıyım?"


    menu:
        "Ne yapmalıyım?"
        "Gerçekten suçlu benim...":
            $ sayori_affection = sayori_affection + 1 
            
            "Başımı sallayıp, Natsuki'nin gözlerinin içine bakıyorum."
            mc "Bırak, Natsuki. Sayori burada suçlu değil."
            s 4m "[player]?"
            "Hızla Sayori'ye, durumu geçiştirmesi için sert bir bakış atıyorum."
            show sayori 1b at t21
            "O başını sallıyor ve gözlerinde kısa bir teşekkür bakışı görebiliyorum."
            mc "Geç kaldık çünkü Sayori, şiirimi yazmama yardımcı olmak zorunda kaldı."
            show natsuki 1e at f22
            n "Ne?! Sen de şiir yazmadın mı?!"
            mc "Yok, yazmadım..."
            mc "Ama Sayori şiir yazdı – Cuma gününden beri hazırdı."
            "Ona omuzumu dürtüp göz kırpıyorum."
            mc "Tabii ki, beni kötü durumda göstermek istemediği için yalan söyleyecektir..."
            n 1c "Anladım..."
            show natsuki 1c at t22
            show sayori 1w at f21
            s "[player]... neden? Sana söyleme demiştim."
            "Omuzlarımı silkiyorum."
            mc "Benim de vicdanım var, biliyor musun! Arkadaşımın benim yüzümden suçlu duruma düşmesine izin veremem."
            mc "Artık yaptıklarımın sorumluluğunu almaya başlamalıyım."
            show sayori 1w at t21
            show natsuki 1u at f22
            n "Anladım... Üzgünüm, Sayori."
            show natsuki 1u at t22
            show sayori 1x at f21
            "Sayori, parıldayan bir gülümseme atıyor."
            s "Ah, sorun değil! İlk başta yalan söylememeliydim!"
            show sayori 1x at t21
            show natsuki 1e at f22
            "Natsuki bana sinirli bir bakış atıyor."
            n "Ve sen -- tembellik etme de, kulüpteysen katkı sağla! Yoksa sadece burada bir sürü tatlı kız olduğu için mi katıldın?"
            n 5b "Vay be."
        "(Sessiz Kalmak)":
            "Karşılaşmayı sessizce izlemeye karar veriyorum... Sayori'ye güveniyorum – bunun üstesinden gelebileceğini biliyorum!"
            show sayori 5b at f21
            s "E-ehh..."
            show sayori 5b at t21
            show natsuki 4e at f22
            n "Bize burada bu kadar tutkulu olmamız gerektiğini söylüyorsun, sonra da şiir bile yazmaya zahmet etmiyorsun?"
            show sayori 4w at f21
            s "Ben..."
            show sayori 4u at f21
            "Sayori gözlerini kapatıp derin, zor bir nefes alıyor."
            s "Peki, ben..."
            "Sayori tamamen donmuş gibi görünüyor."
            "Ben de devreye girmeye karar veriyorum."
            show sayori 4u at t21
            mc "Eğer şiirimi yazmayı unutmasaydım, Sayori'nin bu kadar zamanımı almasına gerek kalmazdı."
            mc "Bu Sayori'nin suçu değil!"
            show natsuki 1g at f22
            n "Siz ikiniz de... of!!"
            show sayori 4u at t31
            show natsuki 1g at t32
            show monika 3b at f33
            m "Hadi ama, Natsuki! O bu sabah şiirini yazdı, yani yine de sorumluluğunu aldı!"
            show monika 1b at t33
            show natsuki 4e at f32
            n "Tabii ki! O katkı sağlamazsa nasıl görünürüz, sanıyorsun?"
            show natsuki 4c at t32
            show monika 2d at f33
            m "Hadi, lütfen kavga etmeyin."
            show monika 2c at t33
            show sayori 1w at f31
            s "Üzgünüm, herkes. Gelecekte bunu daha ciddi alacağım."
 
    hide monika 
    hide sayori 
    hide natsuki 
    with wipeleft
     
    "Natsuki topuklarını dönüp, duyulamayacak bir şeyler mırıldayarak odadan çıkıyor."
    play music Bunkasai fadein 3.0
    show monika 3l at f11
    m "Ee... neyse, şiirimi görebilir miyim?"
    show monika 3l at t22
    show sayori 1c at f21
    s "Ah, evet, tabii! İşte burada!"
    "Sayori, şiiri içeren zarfı Monika'ya veriyor."
    show sayori 1a at t21
    show monika 3k at f22
    m "Siz ikinizin birlikte şiir yazması... ne kadar tatlısınız."
    show monika 3j at t22
    show sayori 4m at f21
    s "N-ne?"
    "Sayori'nin yanakları pembeleşmeye başlıyor."
    "Ama tuhaf olan, nedense benim yüzümün de aşırı ısındığını hissetmem ve bir kaç saniye hafif baş dönmesi yaşamam."
    s 1l "B-biz... uh..."
    mc "Neden böyle dedin ki?"
    show monika 4b at f22
    show sayori 1l at t21
    m "Hey, benden daha fazlasını biliyorum, sanıyorsun."
    show monika 4b at lhide
    hide monika
    "Bunu söyledikten sonra, Monika zarfı açıp bizi yalnız bırakıyor."
    "Sayori'ye bakmaya bile gerek duymadan onun bana baktığını hissedebiliyorum."
    show sayori 5a at f11
    "Başımı çevirdiğimde gözlerimiz buluşuyor."
    s "Üzgünüm... Monika nereden bu fikri aldı, bilmiyorum."
    mc "Birlikte olsak, tatlı bir çift olurduk, değil mi?"
    "Şaka olarak söylediğim halde, kelimelerim beni garip hissettiriyor."
    "Sayori gülerek nervözce kahkaha atıyor ve ben biraz moralimi kaybediyorum."
    mc "...ve bu yüzden söz veriyorum, bugünün geri kalanında şaka yapmayacağım!"
    s 1g "Haha... hayır, teşekkür ederim."
    show sayori 1g at s11
    "Derin bir nefes alıp, boş bir masaya oturuyor."
    s "...Bunun hakkında bile şaka yapman komik. Ben... "
    show sayori 1r at f11
    "Yanına oturup, sol elini sağ elimle tutuyorum."
    "Ellerinin küçük, sıcak ve terli."
    mc "Üzgünüm. Bunu kastetmedim, Sayori."
    mc "Eğer şaka şaka olarak yapılacaksa, tek amacı, bir kız arkadaş bulmanın benim için ne kadar komik bir fikir olduğu."
    s 4j "Bunu söyleme! Bir gün seni çok seven harika bir kız bulacağına eminim."
    s 4c "Tabii, NEET olmazsan!"
    mc "Hahaha... ha..."
    s 1c "Söz veriyorum, işler düzelince... sana birini bulmana yardım edeceğim."
    s "Mutlu olmanı istiyorum. Gerçekten hak ediyorsun."
    mc "Sen de mutlu olmalısın, Sayori."
    show sayori 1t at f11
    "Sayori hüzünlü bir gülümseme atıyor."
    mc "Diğerleri şüphelenmeye başlayacak, eğer burada oturup durursak. Hadi onlara faydalı olalım, böylece yalnız bırakırlar."
    s 1r "Tamam!"
    hide sayori with dissolve 
    show black with dissolve_cg

    
    "Elini bırakıp diğerleriyle birlikte festival etkinliği için hazırlanmaya başlıyoruz."
    "Dekorasyonları asarken, tuhaf bir şekilde dikkatimin dağıldığını fark ediyorum."
    "Nedenini bilmiyorum ama bu belirsizlik hissi içimi kaplamış durumda ve bir türlü atamıyorum."
    "Ama yine de, şu anda çok fazla düşünmeye zamanım olmadığını biliyorum."
    "Bir anda festival zamanı geliyor."
    
    scene bg club_day with dissolve_cg
    "Sanırım bayağı bir kalabalık toplamışız."
    "Yanımda Sayori'ye bakarken hafifçe gergin olduğumu hissediyorum."
    "Yüzüne hızlıca bakıyorum, gergin ama nazik bir gülümseme var."
    "Odaya bir sessizlik hakim, sadece birkaç fısıldama duyuluyor."
    "Bir süre sonra, Monika’nın sesi bu sessizliği bozan ilk ses oluyor."
    show monika 4b at f11
    m "Herkes, şimdi şiir okumaya başlayacağız! Önce edebiyat kulübümüzün üyeleri harika seçkilerini okuyacak."
    "Monika, Sayori'ye dönüyor."
    m "Eğer sakıncası yoksa... Sayori, sen başlamak ister misin?"
    show monika 2a at t22
    show sayori 3g at f41
    s "Tabii! Elimden gelenin en iyisini yapmaya çalışacağım."
    show sayori 3g at lhide 
    show monika 4b at f22
    hide sayori with wipeleft
    m "Hadi hep birlikte, kulübümüzün başkan yardımcısına sıcak bir alkış gönderelim!"
    scene bg class_day with wipeleft_scene
    show sayori 1g at l11
    "Alkışlar kesildiği anda, Sayori kürsüye yaklaşarak şiirini okumaya başlıyor."
    "Seçtiği şiir, daha önce hiç okumadığım bir şiir."
    
    call showpoem(poem_sayFestival, music=False)
    
    show sayori 1a at f11
    "Başta biraz yavaş başlasa da, şiir ilerledikçe daha fazla güven kazanıyor."
    show sayori 1a at s11
    "Bittiğinde, birkaç kişi alkışlayarak ona selam duruyor."
    "Bu kötü bir durum. Sayori mükemmel bir performans sergiledi ama yine de kalabalıktan yeterli takdiri alamıyor."

    menu:
        "Ne yapmalıyım?"
        "Bravo diye bağırmak":
            $ sayori_affection = sayori_affection + 1
            $ sayori_please_clap = True
            "Ayağa fırlayarak ıslık çalıyor ve tüm gücümle bravo diye bağırıyorum."
            "Bu, kalabalığın dikkatini çekiyor gibi görünüyor."
            "Tabii belki de sadece, kendini aptal gibi gösteren çocuğa bakıyorlardır."
            "Alkışlamaya başlıyorum, diğer edebiyat kulübü üyeleri de daha fazla alkış yapmaya başlıyor."
            show monika 3b at t44
            m "Hadi herkese, ona sıcak bir alkış gönderelim!"
            "Kalabalık nihayet grup baskısına yenik düşüp daha fazla alkışlamaya başlıyor."
            show sayori 1y at f11
            "Sayori hafifçe kızarıyor ve alkışlar arasında kürsüye iniyor."
            "Hiçbir şey söylemese de, ben onun teşekkür ettiğini hissedebiliyorum."
        "Diğerlerinden daha yüksek alkışlamak": 
            "Diğerlerinden daha yüksek alkışlıyorum ama bu sadece ellerimi çırpmaktan başka bir işe yaramıyor ve biraz aptal gibi görünmeme sebep oluyor."
            "Ama Monika, Sayori'yi desteklemek için yaptığım bu hareketi fark ediyor ve kalabalığa Sayori'ye sıcak bir alkış yapmalarını söylüyor."
            "Sonunda kalabalık, grup baskısına yenik düşüp daha fazla alkışlamaya başlıyor."
            "Sayori hafifçe kızarıyor ve alkışlar arasında kürsüye iniyor."
            "Hiçbir şey söylemese de, ona yardım etmeye çalıştığım için minnettar olduğunu hissedebiliyorum."


    show sayori 1a at lhide
    hide sayori 

    show monika 3b at t44
    m "Bu harika şiir için teşekkür ederiz, Sayori! Şimdi sıradaki--"
    show yuri 3j at l11
    "Monika cümlesini bitirmeden, Yuri şiirini sıkıca tutarak kürsüye koşuyor, kalabalığa göz bile atmadan."
    "Sonra şiirini okumaya başlıyor."
    "Yuri’nin performansı mükemmeldi – ona daha önce hiç görmediğim bir yönünü gösterdi."
    show yuri 1b at f11
    "Şiirini okumaya başladığı anda sesi, odayı saran bir güvenle doldu... sanki odanın sahibi gibi."
    "Sayori’nin performansından çok daha güçlü alkışlar aldı." 
    show yuri 1a at lhide 
    hide yuri 
    "Kısa bir süre sonra, Monika ve Natsuki sahneye çıkıyor."
    "Hatta onlar şiirlerini okumadan önce bile, Monika’nın gösterinin yıldızı olduğu belliydi."
    "Şiirini okumadan önce bile, Monika gürültülü alkışlarla karşılandı ve şiiri de harika bir işti."
    "Sonunda... sıra bana geldi."

    scene bg club_day with dissolve_cg
    "Edebiyat kulübündeki tek erkek olarak, iyi bir gösteri yapma baskısını hissediyorum."
    "Kalabalığa baktığımda, çoğu izleyicinin benim sınıfımdan erkekler olduğunu fark ediyorum."
    "Bana tuhaf bir şekilde bakıyorlar." 
    mc "Eh... ne var?"
    "Sınıfımdan birkaç erkek, aralarında fısıldıyorlar."
    "Dedikoduların kaçınılmaz olduğunu biliyorum."
    "Bir yanım sahneden inip gitmek istiyor – aslında böyle yaparsam daha az utanç verici olur."
    "Ancak tam tereddüt etmeye başladığımda, bir kızın bana cesaret verdiğini duyuyorum."
    "Aşağıya bakıyorum ve Sayori’nin bana gülümsediğini görüyorum."
    show sayori 1x at t11
    s "Bunu yapabilirsin, [player]! Sana güveniyorum!!" 
    hide sayori with dissolve
    "...Bunu onun için yapmak zorundayım."
    "İyi bir performans sergilemem gerekiyor – onları memnun etmek için değil, onu mutlu etmek için." 
    "Derin bir nefes alarak kaygımı yutuyorum ve şiirimi okumaya başlıyorum."
    "Diğerlerinin yanında kalitesiz olduğu kesin ama tüm kulüpten en soğuk tepkiyi alıyorum." 
    stop music 
    "Neredeyse kimse beni alkışlamıyor ve birkaç sınıf arkadaşımdan yuhalama sesleri duyuyorum."
    "Bana şiirimin berbat olduğunu söyleyip yazmayı bırakmamı istiyorlar." 
    "Sınıf arkadaşlarımın beni hep şaka gibi görmesine alışkınım ama bu şekilde hakaret edilmeyi her zamankinden biraz daha fazla hissediyorum."
    m "Hadi herkes, ona sıcak bir alkış gönderelim! Harika iş çıkardı!" 
    "Monika bile kalabalığı bana tek bir alkış bile yapmaya ikna edemiyor."

    
    if(sayori_please_clap):
        "Tam o sırada, birinin yüksek sesle alkışladığını duyuyorum."
        "Başımı çevirip Sayori'yi görüyorum."
        mc "Sayori?"
        show sayori 4c at t44
        s "Harika iş çıkardın, [player]!!" 
        s "Sana gurur duyuyorum."
        "Ne yapıyor ki bu?"
        "Sayori, kalabalığa doğru dönüyor."
        show sayori 4r at t44
        s "Eğer [player] olmasaydı, şiirimi asla okuyamazdım – asla bitiremezdim."
        s "[player] harika bir insan ve arkadaş – şiirime yardım etmeyi seçti, hem de kendi şiirinin açıkça eksikleri olmasına rağmen."
        "Sayori, bana parlak bir gülümseme gönderip, kalabalığa tekrar bakıyor."
        s "Yani lütfen... ona hak ettiği krediyi verin!"
        "Kalabalık, aralarında fısıldamalarla birbirlerine konuşuyor."
        "Bir süre sonra, bazıları alkışlamaya başlıyor."
        "Birkaç saniye içinde, neredeyse herkes, birkaç kişi hariç, alkışlamaya başlıyor."
        show sayori 1y at t44
        "Sayori'ye bakıyorum, o da hafifçe kızarmış."
        "...?!"
        "Bu hissettiğim şey ne acaba?"
        "Sanki tüm vücudum acı verici derecede ısınıyor."
        "Bunu kaldıramam!"



    "Hayatımda hiç bu kadar utanmış hissetmedim."
    "Buradan çıkmam gerek!" 
    "Kimse beni durdurmadan, korkunç şiirimi alıp odadan fırlıyorum."

    call sayoriRoute_comfort 
    return 


label sayoriRoute_comfort:
    scene bg corridor with wipeleft_scene
    play music Dusk fadein 4.0 
    "Performansım tam bir felaketti."
    "Hayatımda bu kadar utanmış olduğumu hatırlamıyorum."
    "Kendimi rezil ettim, edebiyat kulübünü rezil ettim ve Sayori'nin önünde mahvoldum."
    "Bu gerçekten berbat!" 
    "Sinirle duvara yumruk atmak istiyorum." 
    "...Ne zaman onu etkilemek istesem, hep böyle bir şey olur..."
    "...Sayori'nin önünde salak gibi gözükmek istemediğim günlerden biriydi..."
    "Tabii ki de bugün hata yapacaktım!" 
    "Üstüne bir de sınıf arkadaşlarımın gözünde rezil oldum."
    "Bunun sonuçları olacağından eminim." 
    "Başımı öne eğip ellerimi cebime koyarak koridorda amaçsızca yürümeye başlıyorum."
    "Çeşitli yiyecek stantlarının hoş kokuları burnuma geliyor ama durup bakmak hiç içimden gelmiyor."
    "Sadece buradan çıkıp eve gidip, bu rezaleti unutmak istiyorum." 
    "Telefonum yürürken titreşimle çalıyor." 
    "Bir an durup kontrol ediyorum ve Sayori'nin bana mesaj attığını görüyorum."
    "Aman tanrım!"
    "Şu anda panikliyordur, ama geri dönemem gibi hissediyorum." 
    "Herkes bana bakıp gülecek."
    "Telefonu tekrar cebime koyup, daha hızlı yürümeye başlıyorum."
    "Tam o sırada, birinin arkamdan koştuğunu duyuyorum."
    "Omzuma bakmaya bile gerek duymuyorum ve ben de koşmaya başlıyorum." 
    "Okul bahçesinin kapısını az sonra göreceğim."
    "Bu hızla ben--" 
    stop music
    mc "Ah!!" 
    show black with close_eyes
    "--yemek stantlarından birinin tabelasına çarpıp yere düşüyorum, sanki devrilmiş bir ağaç gibi."
    "...Harika. Gerçekten harika."
    scene bg corridor with open_eyes
    "Gözlerimi yavaşça açarken, birkaç ikinci sınıf öğrencisinin yüzlerini görüyorum."
    "Gülmelerini zor tuttuklarını fark edebiliyorum."
    "Aniden birisi yolundan çekiliyor ve tanıdık bir yüz, endişeli bir şekilde bana bakıyor."
    "Sayori."
    show sayori 4w at f11
    s "[player], iyi misin?!"

    
    play music Thoughts fadein 3.0
    "O bana doğru uzanıyor."
    "Elini alıp kalkıyorum."
    "Sonra etrafımdaki küçük öğrenci kalabalığına bakıyorum."
    mc "Gösteri bitti... Yolu açın!"
    "Kalabalık yavaşça dağılırken, beni beceriksiz bir aptal olarak nitelendiren bir şeyler fısıldadıklarını duyuyorum."
    "Başım hala biraz dönerken, Sayori'ye bakıyorum."
    s "Çok hızlı koştun... Böyle koşmanı istemiştim aslında..."
    "Sesinde gerçek bir endişe var."
    "Bunu ona düşündürttüğüm için kendimi suçlu hissediyorum."
    s "Üzgünüm... Biraz daha yüksek sesle uyarı yapsaydım belki böyle çarpmayabilirdin."
    mc "Hayır, ben... Benim suçum, böyle bir etkinlikten kaçmak."
    "Diğerlerinin benden kesinlikle kızgın olduğunu düşünüyorum, özellikle Natsuki'nin."
    "Bir anda beni sıkıca sarıyor."
    s 1t "Endişelenme. Eminim anlayacaklardır-"
    "Sayori cümlesini bitiremeden, yanımızdan geçen bazı kız öğrenciler bize 'ahmak çift' diye ıslık çalarak sesleniyor."
    "Birbirimizden ayrılıyoruz ve utançtan yüzüm kızarıyor."
    "Onlara biz bir çift değiliz demek istesem de, bunun durumu daha da kötüleştireceğini biliyorum."
    mc "Hadi şunlardan sıyrılalım. Başım ağrıyor..."
    s "Tamam."
    "O bildiğim neşeli sesi geri geliyor."
    s 1x "Oh, kimse bizi rahatsız etmeyecek harika bir yer biliyorum!"
    "Yürümeye çalışıyorum, ama odanın tamamen döndüğünü hissediyorum."
    "Bu yüzden, Sayori bana destek olmak için yol gösterirken ona yaslanmak zorunda kalıyorum."
    hide sayori with dissolve 
    scene bg school_yard with dissolve_cg
    "Sayori, okul bahçesinin daha ıssız bir köşesinde bulunan bir bankın yanına götürüyor."
    "Etrafa bakıp, çok az öğrenci olduğunu fark ediyorum."
    show sayori 1d at f11
    "Oturur oturmaz, Sayori alnımdan yara olup olmadığını kontrol etmek için parmaklarını gezdiriyor."
    mc "İyiyim, Sayori. Merak etme..."
    s 1w "Biliyorsun, her zaman endişelenirim!"
    s "Neyse, kötü bir şey olmadığını görüyorum."
    show sayori 1g at s11
    "Derin bir nefes alıyor ve yanımda oturuyor."
    stop music fadeout 3.0
    play music SayTheme fadein 3.0
    "Beni izlediğini hissediyorum ve sonunda gözlerimi ona çeviriyorum, gözlerine bakıyorum."
    "Bir süre tek bir kelime bile etmiyoruz."
    "Tek duyduğum şey, öğrencilerin sohbeti ve rüzgarda yaprakların hışırtısı."
    "Aklımdan geçen çok fazla düşünce var."
    "Bir süre sonra Sayori, bakışım yüzünden kendini rahatsız hissedip başını eğiyor, hafifçe kızarıyor."
    "Ben de bakışımı indiriyorum."
    mc "Üzgünüm."
    s 1h "Ne için?"
    mc "Bilmiyorum. Sanırım seni rahatsız ettim."
    s 1r "Endişelenme, ehehe~"
    s "Seninle vakit geçirmek çok eğlenceli."
    "Sayori'nin gülümsemesi birden kayboluyor."
    s 1l "Keşke her şey eskisi gibi olabilse..."
    "Ne yaptığımı fark etmeden sol omuzumu ona koyuyorum."
    "Aramızda garip bir gerilim doğuyor ama Sayori beni itmeyecek gibi görünüyor."
    "Bunun yerine, dudaklarında zayıf, boş bir gülümseme beliriyor."
    mc "Bunu istemiyorum..."
    "Sayori tekrar bana bakıyor, ama tek kelime etmiyor."
    mc "Eskisi gibi olamayız... ama birlikte yeni, mutlu anılar biriktirebiliriz."
    mc "Birlikte kalırsak, bir yolunu buluruz."
    show sayori 1k 
    "Sayori bir şey söylemek istiyor gibi görünüyor, ama kafasını sallayıp derin bir iç çekiyor."
    show sayori 1r 
    "Sonra birdenbire gülmeye başlıyor."
    "İçimden bir derin nefes alıyorum."
    mc "Aman Tanrım, söylediklerim {i}bu kadar{/i} saçma değil."
    "Sayori başını sallıyor."
    s 1c "Üzgünüm, böyle demek istemedim."
    s "Sadece... senin bu kadar iyimser olman ve beni neşelendirmeye çalışman... bu çok gerçek dışı gibi hissediyorum."
    mc "Ah, ne diyorsun! Ben genelde bu kadar negatif miyim?"
    "Yine gülüyor."
    stop music fadeout 3.0
    s "Teşekkür ederim, [player]."
    s "Bir şekilde kendimi değerli hissettiriyorsun."
    mc "Aynı şekilde, Sayori."
    show sayori 1g
    play music Dusk fadein 3.0
    "Gülüşü azalmaya başlıyor ve yüzü ciddi bir ifadeye bürünüyor."
    "Hareketlerinin biraz daha bana doğru yaklaştığını fark ediyorum."
    mc "Sayori?"
    s "Evet?"
    mc "Bana güveniyor musun?"
    s 1h "...Güveniyorum."
    mc "İyi."
    mc "Çünkü sana yardım etmek istediğimi sana güvenmeni istiyorum."
    mc "Dün gece çok düşündüm..."
    "Onu biraz daha kendime çekiyorum. Direnmeden yaklaşıyor."
    mc "Mutlu olmanı istiyorum."
    "Başını sallayıp gözlerini başka bir yere çeviriyor."
    s "Lütfen, istemiyorum--"
    mc "Henüz bitirmedim."
    "Derin bir nefes alıp cesaretimi topluyorum."
    "Bunu bilmesi gerek."
    mc "Bunu yalnız başına halletmeni istemiyorum, ama bunun tek nedeni değil..."
    mc "Seninle daha fazla vakit geçirmek istiyorum."
    stop music fadeout 3.0
    play music Dawn fadein 3.0
    "Uzun bir sessizliğin ardından, Sayori'nin gözleri doluyor ve başını omzuma yaslıyor."
    s 1l "Sanırım bencillik yapıyorum ya da bir şey, ama ben de aynı şekilde hissediyorum."
    mc "V-neyi?"
    "Gözlerinden yaşlarını siliyor ve biraz şaşkın bir şekilde devam ediyor."
    s "Seninle daha fazla vakit geçirebilmek beni mutlu ederdi."
    "Yüzüm kızarıyor."
    "Tam olarak ne dediğini fark ettiğinde o da utanıyor."
    s 1n "Bekle, böyle demek istemedim!"
    mc "Evet, biliyorum."
    s "Sen..."
    "Sesini iyice alçaltıp fısıldıyor."
    s "Bana her şeyimi anlatacak kadar güvendiğim tek kişi sensin."
    "Bunu söylediğini anlamam biraz zaman alıyor."
    mc "Bir sorum var, Sayori."
    s "Hm?"
    mc "Neden ben?"
    "Dudaklarını sıkıca kapatıyor ve doğru cevabı bulmaya çalışıyor ama sonunda başını sallıyor."
    s 1k "Bilmiyorum."
    s "İçimde, bana kötü davranmayacağını hissediyorum."
    s "Ve her zaman bana gülümsediğin... üzüldüğümde bile... değersiz hissettiğimde bile..."
    "Sesinin boğulduğunu duyuyorum ve hemen yüzüne bakıp gözlerinin yaşla dolduğunu görüyorum."
    show sayori 1u
    "Gözyaşlarını silip ona güven verici bir gülümseme atıyorum."
    "Aramızdaki gerilim nefes almamı zorlaştırıyor."
    mc "Merak etme – lütfen devam et. Buradayım, Sayori."
    mc "Eğer yardımcı oluyorsa, bana da aynısını hissettiriyorsun."
    mc "Sana güveniyorum çünkü senin dışında kimse beni bir şaka olarak görmüyor."
    mc "Bu yüzden seni yardım edebileceğimi düşünüyorum – çünkü sen her zaman beni neşelendirmeseydin, ben de belki değersiz hissederdim."
    s 1w "...Benden bencil bir istekte bulunabilir miyim?"
    mc "Tabii."
    "Bir süre doğru kelimeleri bulmaya çalışıyor. Ben onu acele ettirmiyorum – ona ihtiyacı olduğu kadar zaman veriyorum."
    s 1l "Beraber daha fazla vakit geçirebilir miyiz? Yani, daha iyi şeylerin varmış gibi anlarsam sorun değil..."
    mc "Bunu da istiyorum."
    s 1q "Harika!"
    "Bir an tereddüt ediyor."
    s 1l "Eğer diğerlerine de soracaksan, sorun değil!"
    mc "Hayır. Sadece seninle daha fazla vakit geçirmek istiyorum."
    mc "Bu beni mutlu eder."
    s "Tamam... Eğer seni mutlu edeceğini söylüyorsan, sana inanırım."
    "Bunu söyledikten sonra, yüksek bir esneme sesi duyuluyor."
    "Onun gözlerinin altındaki morlukları fark ediyorum."
    mc "Sayori... Dün gece ne kadar uyudun?"
    s 1w "Yeterince uyudum!"
    mc "Tam olarak ne kadar?"
    s 1l "Tamam... Sana yalan söylemenin bir anlamı yok..."
    s "Uykusuzdum... Ben... Sana durumumu anlattıktan sonra ne olacağına dair korkuyordum..."
    mc "O zaman şöyle yapalım. Zaten birlikte daha fazla vakit geçirmeye başlayabiliriz... ama önce dinlenmelisin."
    s "Bir işe yaramaz... Sadece seninle olduğumda yağmur bulutları kayboluyor."
    s "O zamandan beri, bu bir rüya olmadığı için uyanıp seni kaybetmediğimi biliyorum."
    "Bitter bir şekilde gülümsüyorum."
    mc "O zaman... burada dinlenebilirsin. Beni yastık olarak kullan."
    "Protesto etmeden önce, yaklaşıp dizimi okşuyorum."
    "Sayori, geri adım atmayacağımı biliyor."
    s "Bir şey söylesen, sadece bir şey söz ver..."
    mc "Emrinizdir."
    "Kuru bir şekilde gülüyor."
    s 1u "Lütfen... rüyada olduğunu söyleme. Uyurken kaybolma."
    mc "Sana söz veriyorum Sayori. Uyanınca burada olacağım, ve uyanınca... seni eğlenceli bir yere götüreceğim."
    s "Bu... harika olurdu, evet..."
    "Sayori'nin gözleri yorgunluğunu daha fazla gizleyemiyor."
    hide sayori with dissolve
    "Söz verirken, gitmeyeceğime dair ona pembe parmak şekerini yaptıktan sonra gülümsüyor ve dizime uzanıyor."
    "Beş dakika sonra, uyuyakalıyordu."
    "Bir süre onu izliyorum... uyurken daha farklı görünüyor."
    "Yüzü daha nazik ve huzurlu."
    "Ceketimi çıkarıp, uyurken üşümemesi için dikkatlice üstüne örttüm."
    window hide
    scene bg sky_day with dissolve_cg
    window show
    "Sonra gökyüzüne bakıp, ona zarar vermeyeceğime dair sessizce kendime söz veriyorum."
    "Asla."
    "Telefonumu ceketimin cebinden çıkarmak üzereyken, titrediğini görüyorum."
    "Monika’nın mesajını kontrol ediyorum, ben öyle aniden çıkarken iyi olup olmadığımı merak etmiş."
    "Ona, stresin çok fazla olduğunu ve biraz temiz hava almak istediğimi yazıyorum, o da sadece geri kalanı rahatlamamı ve keyfimi çıkarmamı öneriyor."
    "Cevap vermiyorum."
    "Sayori uyanana kadar keyif almak zorundayım. Şu an ona dinlenmesi gerek, ve ona gitmeyeceğime söz verdim."
    "Sayori'nin uyuyan yüzüne bakarken, hikayemizin şimdi başladığını kendime söylüyorum."
    stop music fadeout 3.0
    show black with close_eyes
    call sayoriRoute_language
    return


label sayoriRoute_language:
    "Sayori uyuduktan beş saat geçmiş."
    "Festival sona ermek üzere ve ben, soğuk rüzgarda bir heykel gibi oturmaktan vücudumun uyuştuğunu hissediyorum."
    "Yemek kokusu aç olan karnımı işkenceye sokuyor."
    "Ama rahatsızlığıma rağmen, bir kez olsun kalkmadım."
    "Sayori için bekleyeceğime söz verdim ve bu sözü tutacağım."
    "Hem, onu beklerken durumumu – bizim durumumuzu – çok düşündüm."
    "Depresyonla ilgili her türlü online makale okudum."
    "Bu yeterli olmalı."
    "Yakında yanımda düşük bir mırıldanma duyuyorum ve aşağıya bakıp Sayori'nin yavaşça gözlerini açtığını görüyorum."
    
    scene bg school_yard with dissolve_cg
    play music SayTheme fadein 3.0
    
    mc "Günaydın, ya da... iyi öğleden sonra, sanırım."
    "Beni gördüğünde, rahatlatıcı bir şekilde derin bir nefes alıyor."
    s "Hala buradasın..."
    "Onu şımartmaya karar veriyorum."
    mc "Eğer senden daha iyi biri bekliyorsan, üzgünüm."
    "Gülüyor, sonra üzerindeki ceketi soğumaması için onun üzerine koyduğumu fark ediyor."
    s "Bunu söyleme. Sen tanıdığım herkesten daha iyisin."
    s "Üzgünüm... seni bu kadar beklettiğim için."
    mc "Bunları dert etme. Uykun nasıl geçti?"
    "Başını sallıyor."
    s "Ne kadar uyudum?"
    mc "Beş saat."
    s "Ve bütün bu süre boyunca burada mı oturdun..."
    "Başını okşayıp saçlarını yana doğru düzeltirken ona gülümsüyorum."
    mc "Eh, yapacak bir şeyim yoktu."
    mc "Ayrıca... birine faydalı olmanın nasıl bir şey olduğunu hissetmek güzeldi."
    "Bunun tekrar garipleşmeye başladığını fark ediyorum."
    "Belki bir şaka ortamı yumuşatabilir."
    mc "Bunun dışında... hangi adam bir güzel kızın üstünde dinlenmesini istemez ki?"
    s "Be... beni mi güzel buluyorsun?"
    "Hayır. Bu yalnızca garipliği on katına çıkardı."
    "Birkaç saat önce yüzümde hissettiğim hiçbir şey yokken, yanaklarımın kızarmaya başladığını hissediyorum."
    mc "Her... her neyse, hadi gidelim."
    "Beni şaşkın bir şekilde gözleriyle süzüyor."
    mc "Unuttun mu?"
    mc "Sana uyanınca seni güzel bir yere götüreceğimi söylemiştim."
    mc "...Ama, bu senin cebinden olacak. O kadar bekledim ki, açlıktan bayılacak gibi oldum."
    s "Haha, adil olur."
    "Sayori esnedi ve gözlerini tekrar ovaladı."
    s "Hayatımda aldığım en rahat uykuydu."
    mc "Bunu duyduğuma sevindim, Sayori."
    
    show sayori 1a at f11
    "Sayori, ceketi bana geri verip kalkarken, keyifli bir şekilde mırıldanıyor."
    "Kalkmaya çalışıyorum, fakat onun başını dizime koyarak uyuması yüzünden bacaklarım uyuşmuş."
    
    show sayori 1a at s11
    "Sayori, bunu fark ederek hemen bana yardım ediyor ve bugün ikinci kez, yürürken ona yaslanıyorum."
    
    hide sayori with dissolve
    scene bg streets_day with dissolve_cg
    "Bir süre hiç kimse bir şey söylemiyor, ama zaman zaman ondan düşük bir mırıltı duyuyorum."
    "Yolda durup arabaların geçmesini beklerken, gözlerine bakıp, onların eskisinden daha canlı olduğunu görüyorum."
    "Acaba içinde kaç tane şeytan saklıyor?"
    
    scene bg streets_afternoon with dissolve_cg
    "Güneş batmaya başladığında, evlerimize çok uzak olmayan, kenarda hoş bir kafe buluyoruz."
    
    scene bg cafe with dissolve_cg
    "İçeri girdiğimizde boş bir masaya oturuyoruz."
    
    show sayori 1x at f11
    "Sayori, dün nasıl olduğunu düşünürsek, oldukça neşelenmiş görünüyor."
    s "Vay, gerçekten şaşırdım, [player]!"
    mc "Ne hakkında?"
    s "Yaşadığımız yere böyle güzel bir kafe olduğunu bilmiyordum."
    s "Komik, her seferinde okuldan eve giderken buranın önünden geçtim ama hiç bakmayı bile düşünmedim."
    "Omuzlarımı silkerek utangaçça gülümsüyorum."
    mc "Eh, bir gün tesadüfen buldum. Sıkılmıştım, açtım ve yemek yapmaya üşeniyordum..."
    mc "Bir gün okulda bazı kızların burada çok ucuz bir kafe olduğunu söylediklerini duydum."
    
    show sayori 1l at f11
    "Sayori, gözlerini aşağıya indiriyor."
    s "Öyle mi?"
    mc "Bir şey mi var?"
    "Başını sallıyor ve eski, neşeli haline dönüyor."
    s 1x "Hayır! Hiçbir şey! Burada ne sipariş vereceğimi düşünüyorum sadece..."
    mc "Ne almak istersin?"
    "Omuzlarını silkerek."
    s "Sanırım senin aldığını alırım..."
    mc "Hadi ama... Tatlarını merak ediyorum."
    s 1m "Hı? Neden?"
    mc "Bana geldiğinde her zaman benim istediğimi yedin. Aynı hikaye senin evine geldiğimde de geçerli."
    mc "Yani... Bugün her şey seninle ilgili olsun."
    mc "Bu yüzden, ne alırsan onu sipariş edeceğim."
    
    show sayori 1x at f11
    "Sayori, söylediklerime gülerken, ifadesinden onun hoşlandığını ve benim onun tatlarına ilgimi gösterdiğimi anlıyorum."
    s "Emin misin?"

    "Sessizce başımı sallıyorum."
    s 1c "Öyleyse..."
    "Daha durduramadan, sandalyesini yanıma çekip kafeteryanın menüsünü açıyor."
    s 1x "Hadi birlikte sipariş verelim ve paylaşalım!"
    "Tamam... Bugün daha fazla insanın bizi çift sanmasını gerçekten istemiyorum."
    "Ama diğer yandan, Sayori’nin menüdeki her şeyi heyecanla okuyup mutlu olduğunu görünce, onu reddedemeyeceğimi hissediyorum."
    "Bu haksızlık olurdu. O yüzden oyuna dahil oluyorum."
    mc "Tamam, hadi öyle yapalım! Kulağa eğlenceli geliyor."
    s "Yaşasın! Bunun saçma bir fikir olduğunu söyleyeceğinden korkuyordum ama bence çok tatlı bir şey."
    "Dürüst olmak gerekirse, onunla bir yemeği paylaşmak bana pek de kötü gelmiyor."
    mc "Bu, anime sahnelerindeki fark etmeden randevuya çıkan karakterlerin olduğu durumlardan biri mi?"
    s "Tabii ki hayır!"
    s 1l "Yani... Düşünsene, ne kadar garip olurdu?"
    s "Hem... Ben zaten ilişki insanı değilim..."
    mc "Hey, öyle deme!"
    mc "Sınıfta en az birkaç çocuğun şiirini okurken sana dikkatlice baktığını fark ettim."
    s "Evet ama... Sanırım o strese katlanamam."
    s 1t "Sorun değil, [player]. Büyük ihtimalle hayatım boyunca yalnız kalacağımı çoktan kabullendim."
    s "Ama eğer ben mutlu olamayacaksam, en azından hayatımı başkalarını mutlu etmeye adamak istiyorum."
    s 1x "Sanırım onların mutluluğu bana da yansır!"
    "Ellerini birleştirip gülümsüyor."
    "Fakat nedense bu sözleri beni biraz hüzünlendiriyor."
    "Bu adil değil."
    "Gözlerimdeki endişeyi fark edip başını sallıyor."
    s 1c "Neyse, bu akşamlık yeterince dram yaptık. Hadi sipariş verelim!"
    mc "Tamam, ne istiyorsun?"
    s "Hmm... Ooh! Pizza nasıl olur?"
    mc "Pizza mı? Biraz büyük bir seçim olmadı mı?"
    s "İkimiz de açız. Hem, ortadan ikiye bölersek tam doyacak kadar olur, fazla kaçırmayız."
    mc "Mantıklı."
    mc "Garson!"
    hide sayori
    show black 
    with dissolve_cg
    
    "Sayori yerine oturuyor ve yemeğimizi beklerken biraz sohbet ediyoruz. Sonra da pizzayı aç kurtlar gibi mideye indiriyoruz."
    "Aç olduğum açıkça belli olmasına rağmen, Sayori o kadar hızlı yiyor ki, karnında kara delik mi var diye düşünmeden edemiyorum."
    "Metabolizması benimkinden çok daha iyi olmalı, çünkü o hâlâ gayet enerjikken ben yemeğimin yarısında bile nefes nefese kalmış durumdayım."
    "Bu halimi eğlenceli buluyor ve sonunda beni bitirmem için motive etmeye başlıyor."
    "Bir saat sonra, pizzayla olan destansı savaşım nihayet sona eriyor..."
    
    scene bg cafe wtih wipeleft_scene
    show sayori 1r at f11
    s "Başardın! Seninle gurur duyuyorum!"
    "Cevap verecek hâlim kalmadığı için sadece zayıf bir şekilde başparmağımı kaldırıyorum."
    mc "Be... bensiz... asla... yapamazdım... senin o motivasyon konuşmaların olmasa..."
    mc "Gerçekten... harika... bir antrenör olurdun..."
    "Son bir gayretle bir bardak suyu kafama dikiyorum."
    s 1c "Teşekkürler."
    "Gözleri parlıyor ve ellerini birleştiriyor."
    s "Yarın okuldan sonra parka gidelim mi?"
    s "Orası çok güzel, birlikte bir şeyler yapmış oluruz ve senin bu kötü kondisyonunu biraz düzeltiriz."
    s "Çünkü, kusura bakma ama gördüğüm bazı yaşlı adamların bile senden daha iyi kondisyonu var."
    "Onun bu alaycı yorumuna gülmeden edemiyorum."
    mc "Tamam... kulağa eğlenceli geliyor."
    s 1n "Huh? Gerçekten mi?"
    s 1l "Ben sadece dalga geçiyordum... Normalde böyle şeyleri sevmediğini biliyorum."
    mc "Aslında istiyorum. Birlikte yapabileceğimiz güzel bir aktivite gibi geliyor."
    mc "Hem, haklısın... Biraz egzersiz yapmam gerek."
    mc "Ve az önce senin desteğin olmasaydı, o pizzayı bitirecek gücü bulamazdım."
    s 1c "Tamam o zaman... Karar verildi! Yarın okuldan sonra parkta buluşuyoruz!"
    
    menu:
        "Yemeğimizi bitirdiğimizi gören garson, hesabı ödemeye hazır olup olmadığımızı sormak için yanımıza geliyor."
        "Evet, o ödüyor.":
            $ sayori_affection = sayori_affection + 1
            s "Ah, doğru ya! Ödeyeceğime söz vermiştim!"
            mc "Senin için sorun olmaz, değil mi Sayori? Söylerken yarı şaka yapıyordum aslında."
            show sayori 1a at f11
            "Başını iki yana sallıyor."
            s 1c "Takma kafana."
            s "Seninle çok eğlendim—en azından yemeği ödemek benim borcum olsun."
        "Evet, ben ödüyorum.":
            $ sayori_affection = sayori_affection - 1 
            s 1h "Emin misin? Yemeği ben ödeyeceğime söz vermiştim."
            mc "Dert etme, şaka yapıyordum zaten."
            s "Neden bilmiyorum ama... içten içe biraz hayal kırıklığına uğradım."
            s "Ödemek istiyordum... Sonuçta her şeyde sana güvenemem, değil mi?"
            "Sesindeki hüzün, onun her zamanki neşeli halinden çok uzakta."
            s 1l "Keşke bana sormadan benim yerime kararlar vermeyi bıraksan... Sürekli bana iyilik yapıp duruyorsun ama sana asla karşılık veremiyormuşum gibi hissediyorum."
            "Onu küçümsüyor gibi mi davranıyorum?"
            "Yine de cüzdanımı çıkarıp hesabın tamamını ödüyorum."
        "Hesabı yarı yarıya ödeyelim.":
            $ sayori_affection = sayori_affection + 2 
            $ sayori_flag_one = True
            s 1x "Ooh! Harika bir fikir!"
            s "Aferin sana, [player]!"
            mc "Şey, pizzayı da zaten yarı yarıya bölüştüğümüze göre, hesabı da aynı şekilde ödemek en doğrusu olurdu."
            "Gülümseyerek konuşuyorum."
            mc "Hem böylece bunun bir randevu olmadığını da kesinleştirmiş oluruz."
            s 1r "İyi dedin, az kalsın gerçekten unutuyordum!"
            "Kahkaha atıyoruz ama sonra yanımızda, sabırsızca bekleyen garsonu hatırlıyoruz."
            "Sonunda ikimiz de cüzdanlarımızı çıkarıp payımıza düşeni ödüyoruz."

    
    hide sayori with dissolve
    show black with dissolve_cg

    "Sandalyelerden montlarımızı ve çantalarımızı alıp eve doğru yürümeye başlıyoruz."
    "O kadar çok sohbet etmişiz ki, farkına bile varmadan akşam olmuş."

    scene bg residential_night with dissolve_cg

    show sayori 1h at f11
    s "Brrr... Akşamları biraz serin oluyor..."
    "Bana odaklanmış bir bakışla bakıyor."
    s 4m "Ah, doğru ya! Bugün uzun zamandır beklediğin manganın çıkış günü değil mi?"
    s 2c "Şimdi beni bırakıp dükkâna koşarsan, kapanmadan yetişebilirsin."
    "Teklif cazip gelse de Sayori’nin yorgun olduğunu görebiliyorum."
    "Ayrıca, onu bu saatte tek başına bırakmak içime sinmez."
    "Hobilerim yarına kadar bekleyebilir."
    mc "Yok, önemli değil. Hadi, üşümeden eve yetişelim. Seni bırakayım."
    "Sayori’nin yanaklarının hafifçe kızardığını fark ediyorum."
    s "T-teşekkür ederim. Açıkçası, geceleri tek başıma eve gitmekten biraz korkuyorum."
    mc "Beni de pek mutlu eden bir durum değil. Hem, ben de yorgunum. Dinlenmem lazım."

    scene bg dark_streets with wipeleft_scene
    "Onu evinin kapısına kadar bırakıyorum."
    show sayori 1c at f11
    s "Evet... geldik işte."
    mc "Bugün seninle çok eğlendim, Sayori."
    s "Ben de çok eğlendim, [player]. Çünkü yanımdaydın."
    "Cevap vermeme fırsat kalmadan sıkıca bana sarılıyor."
    s 1r "Bana asla unutamayacağım bir gün yaşattığın için teşekkür ederim."
    "Ona karşılık verip sarılıyorum, sıcaklığını hissediyorum."
    mc "Asıl ben teşekkür ederim. Yarın görüşmeyi sabırsızlıkla bekliyorum. Tatlı rüyalar."
    s "İyi geceler."
    hide sayori with dissolve
    "Sarılmayı bırakıyoruz ama içimde ona bir şeyler söyleme isteği var. Yine de, kelimeleri bir türlü bulamıyorum."
    "Ona iyi geceler diledikten sonra arkamı dönüp evime doğru yürüyorum."

    show black with dissolve_cg
    "Nedense hâlâ üşüyorum. Yatağıma girdiğimde bile titremeye devam ediyorum."
    "Bunun üzerinde fazla düşünmeye vaktim olmuyor çünkü ışığı söndürülmüş bir ampul gibi anında uykuya dalıyorum."
    stop music
    call sayoriRoute_nightmares
    return


label sayoriRoute_nightmares:
    scene bg bedroom with open_eyes
    "Kâbuslarla dolu, sancılı bir gecenin ardından soğuk terler içinde uyanıyorum. Vücudum sanki bütün gün profesyonel dövüşçüler tarafından hırpalanmış gibi hissediyor."
    "Derin bir nefes almaya çalışıyorum ama boğazım zımpara kâğıdıyla ovulmuş gibi yanıyor."
    mc "Tam da şimdi mi hasta olacağım ya?"
    "Şiddetli bir şekilde öksürüyorum ve tüm enerjim tükenmiş gibi hissediyorum."
    "Başımdaki yastığa yaslanıp gözlerimi açmaya çalışıyorum ama göz kapaklarım kurşun gibi ağır."
    
    show black with close_eyes
    "Bu hiç iyi olmadı... Sayori’ye bugün birlikte vakit geçireceğimize dair söz vermiştim."
    "Ama şu an bırak buluşmayı, telefonumu alıp ona haber vermeye bile hâlim yok."
    "Yine de bilmesi lazım... Yoksa bütün günü beni bekleyerek geçirecek."
    "Gelmeyişime bir açıklama getirmezsem nasıl üzüleceğini tahmin etmek zor değil."
    "Vücudumu hareket ettirmeye çalışıyorum ama boşuna... Tüm gücüm tükenmiş gibi."
    "Ama ne olursa olsun kendimi zorlayıp, bu berbat hâlde bile ona haber vermeliyim."

    scene bg bedroom with open_eyes
    "Yatakta bir tırtıl gibi sürünerek telefonuma ulaşmaya çalışıyorum. Sonunda telefon komodinin kenarına düşüyor ve elime geliyor."
    "Hemen Sayori’yi rehberimden seçip arıyorum."
    "Kısa süre sonra uykulu ama neşeli sesi duyuluyor."
    s "[player]? İyi misin? Daha sabahın erken saati..."
    mc "Seni uyandırdıysam özür dilerim-"
    "Bir anda yeniden şiddetle öksürmeye başlıyorum."
    s "Aman Tanrım! Çok kötü ses çıkardın!"
    mc "M-merak etme... Sadece ufak bir üşütme sanırım."
    s "Yapabileceğim bir şey var mı?"
    mc "Sadece aradım çünkü--"
    "Öksürük krizim o kadar kötü ki cümlemi bile tamamlayamadan yanlışlıkla çağrıyı sonlandırıyorum."
    "Lanet olsun."
    "Telefonumun da şarjı bitmek üzere..."
    "Bu gidişle, onu tekrar aramak istersem batarya dayanmaz."

    show black with close_eyes
    "Gözlerimi kapatıyorum ve başka bir kâbusun beni içine çektiğini hissediyorum."

    scene bg rooftop 
    show sayori 1u at f11
    with open_eyes
    "Rüyamda Sayori’yi okulun çatısında, gözyaşları içinde görüyorum."
    show sayori 1u at lhide
    hide sayori
    "Öne doğru bir adım atıyor ve--"
    pause(2.0)
    show sayori 1u at l11
    "Son anda ona yetişip kolundan yakalıyorum."
    hide sayori
    window hide
    scene bg noise1
    with dissolve_cg
    pause(1.0)
    show black with dissolve_cg 
    window show
    "Tam o sırada siyah bir sis her yeri kaplıyor ve görüntü bulanıklaşıyor. Gözlerimi açtığımda içimi derin bir endişe kaplıyor."

    scene bg sayori_bedroom with open_eyes
    show sayori 1bu at f11
    "Göz kapaklarımı açık tutmakta zorlanıyorum. Tekrar kapanıyorlar ve bu sefer Sayori’yi odasında, yere oturmuş, yüzünü elleriyle kapatarak hıçkıra hıçkıra ağlarken görüyorum."
    "Ona doğru yürümeye çalışıyorum ama hareket edemiyorum."
    "Adını seslenmek istiyorum ama sesim çıkmıyor."
    
    show sayori 4bi at f11
    "Sonunda ayağa kalkıp bana dönüyor. Yüzündeki gözyaşları arasında, nefretle yanan kıpkırmızı gözleriyle bana bakıyor."
    
    show sayori 4bj at f11
    "Bana doğru bir hamle yapıyor, haykırarak yıllardır ona verdiğim sözleri tutmadığımı, onu yalnız bıraktığımı söylüyor."
    "Tam bana saldıracakken, rüya yine bozuluyor ve değişiyor."
    
    hide sayori
    window hide
    scene bg noise1
    with dissolve_cg
    show black with dissolve_cg
    play sound hb
    window show
    "Kendimi zifiri karanlığın içinde buluyorum. Tek duyabildiğim şey kendi kalp atışlarım."
    
    stop sound
    show sayori 1j at f11
    "Sonra bir anda Sayori beliriyor. Yavaşça bana doğru yürüyerek sorular sormaya başlıyor."
    "Neden acı çekerken onun yanında olmadığımı, neden bencilce sadece kendi hayatımı yaşadığımı sorguluyor."
    "Ağzımı açıp cevap vermek istiyorum ama o sadece tekrar tekrar 'neden?' diye sormaya devam ediyor."
    "Sesleri giderek çoğalıyor, yankılanıyor... En sonunda etrafımdaki görünmez varlıklar hep bir ağızdan aynı soruyu sormaya başlıyor."
    
    hide sayori with dissolve
    "Sanki bir koro hâlinde, bana neden kötü bir arkadaş olduğumu haykırıyorlar."
    mc "B-ben... üzgünüm..."
    "Onlara yalvarıyorum, ama dinlemiyorlar."
    "Geçmişte Sayori'ye yardım edebilecekken nasıl göz ardı ettiğimi, onun sıkıntılarını nasıl fark etmediğimi bir bir yüzüme vuruyorlar."
    mc "Lütfen... beni affet..."
    "Ama sesler umursamıyor. Tek söyledikleri şey, onun iyiliğini hak etmediğim..."

    
    scene bg bedroom with open_eyes
    play music Dusk fadein 3.0
    "Buz gibi terle sırılsıklam bir halde uyanıyorum."
    "Gördüğüm son rüyanın şokuyla nihayet kendime geldiğimi hissediyorum."
    "Gözyaşlarım süzülüyor, vücudumsa bir sıcak bir soğuk arasında gidip geliyor."
    "Kısa bir süre rahat bir nefes alıp yaşadığım kabusun ne kadar korkunç olduğunu düşünürken... tüm rüyalarımın sadece Sayori ve benle ilgili olduğunu fark ediyorum."
    "... Tam o anda aşağıdan gelen ayak seslerini duyuyorum."
    "Buz gibi bir korku içimi kaplıyor... Dün gece yatmadan önce kapıyı kilitlemeyi unuttuğumu fark ediyorum."
    "Ayak sesleri gitgide yaklaşıyor."
    "Her kimse, doğrudan bana doğru geliyor."
    "Şu anki halimle tamamen savunmasızım... kaçma şansım da yok."
    "Kapı kolunun döndüğünü görüyorum."
    play sound hb
    "Kalbim deli gibi atarken bir kaçış yolu aramaya çalışıyorum."
    stop music fadeout 3.0
    "O sırada tanıdık bir ses duyuyorum."
    play music Dawn fadein 3.0
    s "[player]?"
    
    show sayori 1bh at f11
    "Sayori’yi odamın kapısında bir tepsiyle dururken görünce derin bir nefes alarak rahatlıyorum."
    mc "Sa-Sayori?"
    s "Üzgünüm... Sana sormadan içeri girmek istememiştim ama neyse ki dün gece kapıyı kilitlemeyi unutmuşsun."
    "Ona şaşkın bir şekilde bakıyorum."
    s 4bw "Seni korkuttum mu? Çok üzgünüm eğer öyle olduysa!"
    "Başımı iki yana sallıyorum, o da rahat bir nefes alıyor."
    mc "Sadece... buraya nasıl geldin? Neden?"
    s 1bg "Sana endişelendim. Hasta gibi görünüyordun."
    mc "Sayori..."
    "Ona bakarken aklımda binbir düşünce dönüyor."
    s 4bl "Beni göndermeni istemiyorum. Gitmeyeceğim de..."
    "Ellerimi yumruk yapıyorum. Gerçekten de doğru söylüyor—onu zorla gönderecek gücüm olsa bile, Sayori kafasına koyduğunu yapacak kadar inatçıdır."
    s "Monika ve sınıf öğretmenini aradım, hasta olduğunu söyledim."
    "Ona dikkatlice bakınca okul formasını giymediğini fark ediyorum. Bugün okula gitmeyip benimle ilgilenmeye karar vermiş olmalı."
    mc "Ya sen? Senin için devamsızlık olmayacak mı?"
    s 1bt "Beni boşver. Hasta olduğumu söyledim, yalan söyledim."
    mc "Neden?"
    s 1bl "Çünkü... senin yanında olmak istiyorum. Sana bakacak kimsen yok, değil mi?"
    mc "...Evet."
    s 1bb "O zaman konu kapanmıştır! Sen benim için her zaman oradaysan, ben de sen iyileşene kadar buradayım."
    mc "Lütfen eve git. Senin de hasta olmanı istemiyorum."
    s "Asla olmaz!"
    s 1bq "Hem, ben hasta falan olmam! Eğer gerçekten inanırsam, hiçbir şeyim olmaz!"
    s "Ve... sana bakmak beni mutlu ediyor."
    stop music fadeout 3.0
    "Yüzümün kızarmasına sebep olan şey ateşim mi yoksa içinde bulunduğum garip durum mu, emin değilim."
    mc "Teşekkür ederim, Sayori... Senin gibi bir dosta sahip olmak büyük şans benim için."
    play music SayTheme fadein 3.0
    "Sayori hiçbir şey söylemiyor ama iltifatımı sevdiğini belli ediyor."
    s 1bd "Şimdi ciddi olalım... bana güven. Seni iyileştireceğim."
    show sayori 1bg at s11
    "Yavaşça yanıma geliyor, yatağımın yanındaki sandalyeye oturup alnıma elini koyuyor."
    s "Hmm..."
    s "Peki..."
    "Parmaklarını hafifçe boynumdan aşağıya doğru gezdirmeye başlıyor."
    s 1bh "Anladım!"
    mc "Uhh... Sayori?"
    "İç çekiyor."
    s 1bb "Çok şükür."
    mc "Hey? Sayori? Dünyaya dön?"
    "Kendi dünyasından çıkıp bana dönüyor."
    s 1bc "Ateşin var ama çok ciddi değil. Birkaç güne toparlanırsın."
    "Ona şaşkın bir bakış atıp ağzımı açıp kapatarak ne diyeceğimi bilemiyorum."
    s 1bl "Yalnızken çok fazla tıbbi kitap okuyorum..."
    s "Çünkü... şey... biliyorsun işte..."
    "Başımı sallıyorum ama bir şey söylemiyorum."
    s 1bk "Neyse... şimdilik bunu iç."
    "Bardağa biraz çay döküp bana uzatıyor."
    "Dokunur dokunmaz sıcaklığı hissediyorum ve neredeyse elimi yakıyorum."
    "Sonunda bardağı dudaklarıma götürüp birkaç yudum içiyorum."
    mc "Hmm... gerçekten çok lez—"
    "Tam o anda boğazımda inanılmaz bir yanma hissediyorum."
    "Şiddetle öksürüyor ve çayı yatağa döküyorum."
    mc "Ateş... boğazım yanıyor!"
    s 1bm "A-ayy! Çok mu güçlü yaptım?"
    "Sadece başımı sallıyorum."
    mc "N-ne koydun buna?"
    s 2bl "Şey, okuduğum kitapta boğaz ağrısına zencefil çayı iyi geliyormuş... Ben de buzdolabında bir sürü zencefil buldum."
    "Tedirgin bir şekilde terliyorum... ve ne yaptığını anladığımda içimde bir korku yükseliyor."
    mc "Ne kadar koydun?"
    s "Bütün kökü."
    "Sayori'nin sadece yardım etmek istediğini biliyorum ama..."
    "Asıl sorun şu ki, o zencefili çöpe atmayı planlıyordum çünkü son kullanma tarihi geçmişti."
    stop music fadeout 3.0
    "Sayori hatasını anlıyor ve yüzündeki gülümseme solmaya başlıyor, gözleri kararıyor."
    s 1bu "...Üzgünüm. Yardım etmeye çalıştım ama yine her şeyi berbat ettim."
    "Sesi hiç olmadığı kadar karanlık çıkıyor."
    mc "Şey... yine de teşekkür ederim."
    s 2bf "[player], üzgünüm... Belki de gitmeliyim... Sadece işleri daha kötü hale getirdim."
    "Tam ayağa kalkacakken elini tutuyorum."
    "Bu hareketim onu o kadar şaşırtıyor ki, duraksıyor. Gözlerinde tarifi zor bir ifade var."
    mc "Lütfen gitme..."
    "Sesim neredeyse bir fısıltı kadar zayıf."
    s 1bk "Neden? Sadece bir yüküm ben..."
    "Ayrıca sesi düşer ve ağlamamak için dudaklarını ısırır."
    s "Yardım etmeye çalıştım ama sadece seni daha kötü hissettirdim... her zaman olduğu gibi."
    "Başımı sallarım."
    s "[player]..."
    mc "Sana... kalmanı istiyorum..."
    s 1bl "Hadi ya, işe yaramazken?"
    s 1bw "Sana yardımcı olamayacakken, hastalıkları nasıl tedavi edeceğimi bilmeden ve o kadar sakarım ki bir şekilde her şeyi daha kötü hale getirirken?"
    "Başımı sallamaya çalışırım."
    mc "Evet."
    mc "Gün henüz yeni başladı... hâlâ harika bir şeyler yapabiliriz."
    "Sayori nefesini tutar ve yere oturur."
    "Başımı kaldırdığımda, sözlerimin ona dokunduğunu ve bir şekilde kalbinde bir yerlerde yankı uyandırdığını fark ederim."
    mc "Bana yardımcı olabilirsin... tıpkı ben sana yardımcı olabileceğim gibi."
    "Hiçbir şey söylemez. Derin düşüncelere dalmış gibi."
    mc "Sayori?"
    s 1bl "Sana nasıl yardımcı olabilirim, [player]?"
    mc "İlk olarak... ağrı kesicilere ihtiyacım var, ama kalkamam."
    mc "Ama daha da önemli olanı, duyduğuma göre insanlar daha hızlı iyileşiyormuş, eğer mutluysalar."
    s 1bg "Ah, evet, kusura bakma."
    show sayori 1bg at lhide
    hide sayori
    pause(1.5)
    show sayori 1bg at l11
    "Ağrı kesicileri nereden bulacağını tarif ettikten sonra, Sayori bir dakikadan kısa bir süre içinde geri gelir, elinde bir bardak su ve ilaçlarla."
    "İlaçları içip göğsümdeki yangını söndüren ve genel acımı hafifleten bir içki içtikten sonra, uzanırım. Hiçbirimiz konuşmaz, ama gözlerimi kapatmış olsam da Sayori'nin gözlerini üzerimde hissettiğimi biliyorum."
    "Birden sessizliği bozar."
    s "Eğer biraz negatif olduysam özür dilerim. Gerçekten ne olduğunu bilmiyorum... sadece..."
    s 4bf "Başarısız olduğumda beynimdeki ses bana işe yaramaz ve değersiz olduğumu söylüyor."
    "Ona dönüp, zayıfça gülümsediğimi ve parmaklarımla elini okşadığımı hissediyorum."
    mc "O zaman o sesi susturmalıyız."
    mc "Eğer sen yapamıyorsan, ben iyileştikten sonra deneyeceğim."
    s 1bl "Neden? Neden bunu yapıyorsun?"
    mc "Neden olmasın? Şu anda sana aynı soruyu sorabilirim."
    mc "Hastalandığımı duyduğunda neden okula gitmedin?"
    s 1bw "Sen en yakın arkadaşımsın! Seni yalnız başına acı çekerken nasıl bırakabilirim? Şu anda sana bakacak kimsen yok, biliyorum."
    "Başımı sallarım."
    mc "Sence sen de aynı şekilde muamele görmeyi hak etmiyor musun?"
    show sayori 1bu at f11
    play music Dusk fadein 2.0
    "Sayori sessizleşir."
    mc "Sayori?"
    s 1bl "Bilmiyorum..."
    s "Gerçekten bilmiyorum... hak ediyor muyum?"
    mc "Ne demek istiyorsun?"
    s "Ben..."
    "Görünüşe göre, duygularını kelimelere dökmekte zorlanıyor."
    mc "Bana her şeyi anlatabileceğini biliyorsun."
    s "Henüz hazır olduğumu düşünmüyorum... ben..."
    "Sanki acı çekiyormuş gibi bir sesle konuşuyor."
    "Onun bu şekilde düşünmesinin nedeni gerçekten kişisel bir şey gibi görünüyor."
    "Ama diğer yandan, belki de onun zihniyetinin köklerine inebileceğim tek fırsatım. Eğer onun bu şekilde düşünmesine neden olan şeyi öğrenebilirsem, ona bir şeyler yapabilirim."
    "Ama Sayori baskı altında kalabilir. Onun bunu anlatmak istediğini görebiliyorum ama..."

    menu:
        "Daha fazla zorlamak doğru mu?"
        "Lütfen kendini zorlama.": 
            $ sayori_affection = sayori_affection + 2
            $ sayori_flag_two = True
            s 1bh "...Üzgünüm."
            s "Sana güvenmediğim için değil... ve senin, her şeyden önce, hak ettiğini bildiğim birisin... ama ben..."
            "Sessizce başımı sallarım."
            mc "Merak etme, anlamadım ama gerçekten rahatsız olmuş gibisin."
            mc "Bu senin için çok önemli görünüyor, zorlamanı istemiyorum eğer hazır hissetmiyorsan."
            mc "Bekleyebilirim – ve bekleyeceğim – çünkü sana yardım etmek istiyorum. Ama bunun için, neden değersiz hissettiğini öğrenmem gerekiyor."
            s 1bt "Teşekkür ederim. Gerçekten minnettarım."
            "Bir kez daha başını sallar."
            s 1bu "Keşke bu kadar adaletsiz olmasaydı."
            mc "Ben hiçbir yere gitmiyorum, Sayori."
            s 1bt "Biliyorum."
            s "Söz veriyorum – hazır olduğumda sana anlatacağım."
        "Lütfen ne olduğunu anlat bana.": 
            
            $ sayori_affection = sayori_affection + 1
            s 1bk "...Üzgünüm, ama anlatamam."
            s "İstemek istiyorum – gerçekten de... ama bu benim için çok zor."
            mc "Tamam. Üzgünüm. Seni zorlamak istemiyorum."
            mc "O zaman konuyu değiştirelim."
            s "Özür dilerim... ve teşekkür ederim."
            "Belki de ona daha nazik olmalıyım."
            "Bu gerçekten çok ciddi bir konu gibi görünüyor ve ona zaman tanımalıyım."
    
    
    stop music fadeout 3.0
    
    "Ağrı kesicilerimin etkisini hissetmeye başladım, gözlerim bulanıklaşıyor."
    s 1bh "Yani ilaç etkisini göstermeye mi başladı?"
    mc "Evet."
    s 1bc "İyi. Biraz kestir... Uyanmanı beklerim."
    show black with close_eyes
     
    s "Belki o zaman sana söyleyebilecek cesareti bulurum..."
    "Sesinin giderek uzaklaştığını duyuyorum, yorgunluğum beni derin uykusuz bir uykuya sürüklüyor."
    "Kısa bir süre sonra, iki ses duymaya başlıyorum... bir erkek ve bir kız sesi."
    "Ama hiçbir şey görmüyorum ve sesler, bozuk bir teypten çalınan eski kayıtlar gibi geliyor."
    b "Hey, ne oldu?"
    g "A-a... önemli değil."
    b "Hı? Dizine ne oldu?"
    g "... Düşüyorum..."
    g "Kendimi morarttım... ve... peluş oyuncağım..."
    b "Vay canına. Boynu kırılmış."
    g "... hıçkırık..."
    b "Hey, lütfen ağlama!"
    g "O... benim tek arkadaşımdı."
    b "Tek arkadaşın mı?"
    g "Hı-hı..."
    b "... "
    g "Şimdi... ne yapacağım...?"
    b "Hadi gidelim. Onu tamir edebileceğimizi düşünüyorum."
    g "Gerçekten?!"
    "Seslerin anlamını fark ettiğim an, hemen kayboluyorlar ve yerlerini statik gürültü alıyor."

    scene bg bedroom with open_eyes
    
    play music aNewDay fadein 2.0
    "Bir şekilde hoş, nostaljik bir hisle uyanıyorum."
    "Ateşim biraz daha azalmış gibi hissediyorum ve vücudumu biraz hareket ettirecek kadar enerji buluyorum... ama hâlâ acı çekiyorum."
    "Alarm saatime bakıyorum – zamanına göre, sanırım altı saat kadar uyumuşum."
    "Sayori’nin gitmiş olduğunu fark ediyorum."
    "Gerçekten bana bakmaya geldi mi, yoksa sadece bir rüya mıydı?"
    "... Hayır. O kadar gerçekti ki, rüya olamaz."
    "Anılarımın doğruluğunu sorgularken, aşağıdan aşırı kötü bir şekilde şarkı söyleyen bir ses duyuyorum, ardından sadece bir şey olabileceğini söyleyen bir çarpma sesi geliyor." 
    "Sayori yemek yapmaya çalışıyor."
    "Sonumuz yakın."
    "Şarkı söylemesi daha da yüksek bir hale geliyor ve onun yaklaştığını fark ediyorum."
    show sayori 1ba at l11
    "Ayağa kalkıp, odaya girdiği an ona gülümsüyorum."
    s 1bc "Ah, uyanmışsın! Nasıl hissediyorsun?"
    mc "Bu sabahki halimle kıyasladığımda, çok daha iyi hissediyorum."
    s 1bx "Bunu duyduğuma çok sevindim!"
    show sayori 1bx at s11
    "Sayori, yanımda oturduğu sırada haberle neredeyse parlıyor."
    s 1bc "Uykunda gerçekten huzurlu görünüyordun."
    mc "Evet... Güzel bir rüya gördüm."
    mc "Ama pek hatırlamıyorum."
    s "Bunu duyduğuma sevindim."
    s 1ba "Şey..."
    mc "Ne oldu?"
    "Derin bir nefes alıyor."
    stop music fadeout 3.0
    s 1bh "Hani uyumadan önce söylediklerim vardı ya... Düşünüyordum... ve sana söylemek istiyorum."
    s "Korkmuş olsam da... Ama artık sorunlarımdan kaçamayacağımı biliyorum."
    mc "Senin yalnız olmadığını biliyorsun, Sayori."
    mc "Beni fikrimi değiştirmeye zorlayacak hiçbir şey yok."
    s "Peki..."
    s 4bg "Burası uzun bir hikaye olacak. Uyumadığından emin ol, tamam mı? Uyumamanı çok isterim."
    mc "Merak etme. Gördüğün gibi, uyanığım."
    "O başını sallıyor, anlamış bir şekilde ve kelimeleri ararken başlıyor."
    play music Dusk fadein 3.0
    s 2bh "Hep... gerçekten önemli olamayacağımı düşünmüştüm. Sonuçta, biri diğerlerinden daha önemli olabilir mi? Hepimiz aynı değil miyiz?"
    s 2bl "Bunu zaten biliyorsundur... ama ben büyürken pek arkadaşım olmadı... ta ki seni tanıyana kadar, tabii."
    mc "Hatırlıyorum. Hep beni ‘arkandan gitmekten’ korkuyordun ya da bir şeyler."
    "Başını sallıyor."
    s "Evet. Şey..."
    s 2bh "Hep bencillikten ne kadar farkındaydım. Ne yazık ki çok fazla insan sadece kendi için yaşıyor, ama biz buna toplum diyoruz."
    s "Ben öyle olmak istemiyorum. Başkalarını mutlu etmek istiyorum, özellikle acı çekenleri..."
    mc "Bu yüzden çocukken bana bu kadar bağlandın mı?"
    s 2bl "... En azından bunun bir parçasıydı. Ya da... ilk başlarda öyleydi, evet."
    s "Başkalarına yardım etmek güzel bir şey... ama ne yazık ki bencil insanlar bana nasıl davrandıklarını hiç düşünmedim."
    s 1bh "Onlara ne kadar yardım etmeye çalışırsam çalışayım... asla tatmin olmuyorlardı."
    s "Daha fazlasını istiyorlardı."
    s "Daha kötüsü, onlara yardım ettikten sonra, genellikle beni arkalarına itiyorlardı..."
    "Bir hıçkırık bastırırken, gözyaşlarını siliyor."
    s 1bt "Sonunda, yoruldum. Hiçbir ‘arkadaşım’ benim her gün gülüp pozitif olmamın ne kadar acı verdiğini düşünmedi."
    s 1bl "Ama eğer bunu yapmazsam, beni bırakırlardı. Dedikodular yayarlardı. Hayatlarından çıkarırlardı."
    s "İşte bu yüzden... o yüzden..."
    "O bitirmeden, güç toparlıyorum ve onu sıkıca sarılıyorum."
    s "[player]..."
    mc "Ben o insanlar gibi değilim, Sayori."
    mc "Senin yardımseverliğini kullanmam. Ve daha önemlisi..."
    "Hafifçe uzaklaşıp, onun yüzünü görmek için biraz geri çekiliyorum."
    mc "Sana asla ihanet etmeyeceğim."
    "Sesi fısıldar gibi bir şekilde azalıyor."
    s 1bd "[player]... ben..."
    mc "Senin tek arkadaşın olsam bile, yalnız değilsin."
    "Başka bir şey söylemeye hazırlanırken, fark ediyorum ki yüzlerimiz sadece birkaç santimetre uzaklıkta. Biraz daha yakın olursak, öpüşeceğiz."
    "Sayori de bunu fark ediyor ve utanarak başını çeviriyor."
    "Birbirimizden uzaklaşıyoruz ve aynı anda özür diliyoruz."
    "Tekrar yatağa uzanıyorum ve o hikayesine devam ediyor."
    s 1bl "İşte bu yüzden sana söylemekten çok korkuyordum... ya da başka birine..."
    s 1bg "Neden değersiz gibi hissediyorum..."
    s "Beynimin içinde bir ses var gibi, eğer herkesi memnun etmezsem, hiçbir güzel şey hak etmiyorum."
    mc "Ama bunun doğru olmadığını biliyorsun."
    s 1bu "Bilmiyorum..."
    s "Artık hiçbir şey bilmiyorum..."
    s "Literature Club'a katılmanı istemek iyi bir fikir miydi?"
    s "Sana bunları söylemek iyi bir fikir mıydı?"
    s "Bilmiyorum... Seni kaybetmekten çok korkuyorum."
    mc "Beni kaybetmeyeceksin."
    s 4bv "Anlamıyorsun... benimle burada olsan bile... birini bulursun."
    "Biri bulmak mı?"
    "Dur... O...?"
    s 1bk "Bunu hissetmemeliyim. Yanlış..."
    mc "Yanlış değil."
    mc "Sayori..."
    s 1be "Hep başkaları tarafından bırakılmak ya da sömürülmekten o kadar alıştım ki... mutlu bir geleceği hayal bile edemiyorum. Hak etmiyorum."
    mc "Sen mutluluğu hak ediyorsun. Sömürülmeyeceksin ya da terk edilmeyeceksin."
    mc "Gerçekten sana hayranım."
    mc "Bu kadar şeyden sonra bile gülümsemeye devam etmek ve hala insanlara yardım etmek cesaret ister."
    mc "Ama Sayori, kendinin ne kadar değerli olduğunu fark etmelisin."
    mc "Beni buraya getiren tek neden sensin."
    "Bir fikir aniden aklıma geliyor."
    mc "Bir anime karakterini hatırlatıyorsun bana, gerçekten sevdiğim ve hayranlık duyduğum birini."
    mc "Bunu benimle izlemek ister misin?"
    s 1bb "...Tamam. Eğer seni mutlu ediyorsa."
    stop music fadeout 2.0
    show sayori 1bb at lhide 
    "Kafamı sallayarak, ona odadan çıkmasını söylüyorum, ben de pijamalarımı değiştireceğim."
    show sayori 1bb at l11
    "Beş dakika sonra, ona geri çağırıp çekmecemdeki DVD’yi buluyorum."
    "Ona TV’ye takıyor ve izlemeye başlıyoruz."
    "Anime'nin başrolü Sayori'ye çok benziyor – kendini çok fazla düşünmeden yardım etmeye çalışan biri, ama hep sıkıntıya giriyor."
    "Sayori gibi, tüm düşmanlarını yalnız başına karşılamaya çalışıyor ve birçok tanesini aşmayı başarıyor... ama son engel yalnız başına aşılacak bir şey değil."
    "Umutsuzluk onu aşıyor ve neredeyse ölüyor."
    "Ama sonunda arkadaşları ona ulaşarak ne kadar değerli olduğunu anlamasına yardımcı oluyor."
    "Başrol, nihayet güçlü bir şekilde hayatta kalmayı başarıyor ve serinin son düşmanını yenecek gücü buluyor." 
    "Anime’yi bitirdiğimizde, güneş zaten batmış." 
    "Sayori’yi dikkatle izliyorum."
    "Animesi bittiğinde, sonunda konuşmaya başlıyor."
    s 1bx "Vay... o kadar güçlü ve havalı..."
    mc "Gerçekten de... çocukken hayran kaldığım bir karakter."
    s 1bt "Keşke ben de öyle olabilsem."
    mc "Zaten öylesin. Birçok insan, karşılık beklemeden arkadaşlarına yardımcı olmak için böyle bir şey yapmaz."
    s 1bk "..."
    mc "Pes edemezsin... çünkü ben arkadaşım olmadan kaybolurum."
    mc "Ama senin benim arkadaşlığımı hak etmediğini düşünmeni istemiyorum."
    mc "Bunu ve çok daha fazlasını hak ediyorsun."
    s 1bw "Lütfen, ben..."
    mc "O karaktere neden bu kadar hayran kaldığımı biliyor musun?"
    mc "Çünkü o kendisi olmaktan korkmuyor – o iyi bir insan ve tüm kararlılığını bu özelliği üzerinden buluyor."
    mc "Evet, her zaman seni kullanmak isteyen insanlar olacak, ama senin gibi iyi kalpli biri olduğun için seni seven insanlar da olacak."
    mc "Değersiz değilsin çünkü çok şey yapıyorsun."
    mc "Sadece bana değil, bir de Yuri ile Natsuki’yi geçen gün birbirinden ayırmadığın zaman..."
    mc "Biri sana böyle davranmış olsaydı, onu değersiz mi sayardın?"
    s 1bt "Ben... hayır, saymazdım."
    s "Onların bana bu kadar nazik olmalarına sevinirdim."
    mc "Beni her gün nasıl hissettirdiğini işte böyle hissediyorum."
    s 1bu "[player]..."
    "Dudağını ısırıp alarm saatime bakıyor."
    s "Hmm... geç oldu. Belki yemek yiyebiliriz? Bir yere gitmem gerek."
    mc "Tabii, ben de açım."
    mc "Beni garip hissettirdiysem üzgünüm."
    s 1bd "Merak etme... Benim değersiz olmadığımı duyduğuma çok sevindim."

    hide sayori with dissolve
    scene bg kitchen with wipeleft_scene
    "Sayori, kendi yaptığı yemeği getirip birlikte sessizce yiyoruz."
    scene bg house_entrance_night with wipeleft_scene
    "Yemekten sonra, bana iyi geceler dileyip evine dönerken, yarın tekrar geleceğine söz veriyor."
    scene bg bedroom with dissolve_cg
    "Birinin bana bakması gerçekten güzel bir his."
    "Ama acaba içimdeki bu sıcaklık, sadece yaptığı nazik hareketten mi, yoksa başka bir şeyden mi kaynaklanıyor?"
    "Buna, belki de sadece onun varlığıyla mı?... "
    show black with dissolve_cg
    "Yanıt bulamadan, tekrar uyuyakalıyorum."

    $ o_name = "???"
    play music aNewDay fadein 3.0
    o "Günaydın, uyuyan güzellik!"
    "Genç bir kadının sesi, uykumdan uyanmamı sağlıyor."

    scene bg bedroom with open_eyes

    show sayori 1ba at f11
    "Gözlerimi açtığımda, Sayori'nin elinde buharı tüten bir fincan çayla yatağımın başucunda durduğunu görüyorum."
    "Onu gördüğümde, istemsiz bir şekilde hafifçe gülümsüyorum."
    mc "Günaydın."
    s 1bc "Aslında öğle olmuş... ama sen o kadar huzurlu uyuyordun ki, seni uyandırmaya kıyamadım."
    "Fincanı gece masama bırakırken, alnımı kontrol ediyor."
    s "Nasıl hissediyorsun?"
    "Yanıt vermeye çalışıyorum ama öksürüğüm hala oldukça şiddetli."
    "Sayori derin bir iç çekerek, kendinden memnuniyetsiz olduğunu belli ediyor."
    s 1bd "Daha iyi hissedmeni ummuştum..."
    mc "Hissediyorum."
    mc "Sadece iyileşmek biraz zaman alıyor."
    "Gözlerini doğrudan ona dikerken devam ediyorum."
    mc "Peki ya sen, Sayori?"
    "O, parlayan bir gülümseme ile cevap veriyor."
    s 1br "Dün söyledim ya, bana hiç endişelenme! Göründüğüm kadar zayıf değilim."
    s "Ehehe~"
    s 1bk "Ayrıca... buradayım çünkü seni önemsiyorum."
    "Son cümleyi neredeyse kendi kendine mırıldanıyor, sesi uzaklaşmış gibi."
    mc "Sayori?"
    "Bunu fark eden Sayori, hemen konuyu değiştiriyor."
    s 1bh "Bir şey yok. Sadece kendi kendime konuşuyordum, hepsi bu."
    s "Sanırım biraz garip oluyorum."
    mc "Bence sevimlisin."
    show sayori 1bg at t11
    "Alnımdan elini çekerken, bir adım geri atıyor."
    "Acaba sadece hayal mi ediyorum, yoksa beni 'sevimli' diye çağırmamla birkaç saniyeliğine gerginleşiyor mu?"
    s 1bc "Neyse, öğleyi geçtiği için seni uyandırmam gerektiğini düşündüm."
    s 1bk "Tüm günü uyuyarak geçirmene izin veremem..."
    stop music fadeout 3.0
    "Yüzü biraz kararmış."
    s 1bl "Bunu kişisel tecrübelerimden söylüyorum, yani."
    "Sayori bir garip davranıyor."
    "Acaba bu, depresyonunun yine etkisi mi?"
    mc "Sayori, bir şey mi var?"
    "Başını sallayıp parlak bir gülümseme takınırken, hemen kendini toparlıyor."
    s 1bd "Hayır, bir şey yok... Sadece biraz yorgunum galiba."
    "Bir an düşündüm, depresyonla mücadele eden insanların sıklıkla uyku problemleri yaşadığını okumuştum."
    mc "Sanırım kalkacak kadar iyi hissediyorum."
    mc "İstersen dinlenmek için eve gidebilirsin."
    s 1bw "Hayır, lütfen gitme!!"
    "Sesi o kadar çaresiz ve korkmuş ki, istemsizce irkiliyorum."
    show sayori 1bd at f11
    "O, bir gülümseme takınmaya çalışıyor, ama gözlerinden korktuğu her halinden belli."
    mc "Sayori, lütfen neyin var?"
    s 4bh "Hiçbir şey... İyi olacağım!"
    mc "Sayori..."
    "Ellerini yumruk yaparak sıkıyor."
    s 1bk "Lütfen, [player]... sadece iyileşmene odaklan, tamam mı?"
    s "Senin benim için endişelenmen bana çok rahatsız edici geliyor."
    s "Başkalarına yardım etmek isterim, ama lütfen... benim için endişelenme."
    "Başımı sallayıp, böyle bir şey yapamayacağımı ona söylüyorum."
    s 1bl "Neden? Kolay olmalı, her zaman yaptığın gibi devam edebilirsin."
    mc "Bu o kadar basit değil."
    mc "Bir dostluk, karşılıklı bir ilişki olmalı."
    "‘Karşılıklı ilişki’ kelimelerini duyduğunda Sayori bir an tereddüt ediyor."
    "Ama hemen toparlanıp çayını iki elinin arasına alıyor."
    s 1bt "Neyse, bunu iç. Dün biraz daha hafif yaptım."
    s "Ve lütfen gitmemi söyleme..."
    "Bir iç çekiyorum."
    mc "Tabii... Sadece seni yorgun gördüğüm için endişeliydim."
    "O, sessizleşip bana, sadece içmem için ısrar ediyor."
    "Kendimi bir kayıp gibi hissederek, fincana döküp bir yudum alıyorum."
    "Dediği gibi, gerçekten de daha hafif olmuş. İçimden sıcacık bir rahatlama hissi yayılıyor."
    "Sayori fincanımı alıyor, ama odadan çıkmak yerine yanımda bir sandalyeye oturuyor."
    s 1bg "[player]... yalnız kalmaktan korkuyor musun? Dünyada tamamen yalnız olmaktan?"
    mc "Ne?"
    s 1bl "Hayır... unutsan iyi olur. Bunu söylediğimi bile unut."
    mc "Hayır, gayet geçerli bir soru. Sadece biraz ani oldu."
    mc "Gerçekten, açıkçası pek düşünmemiştim."
    mc "Tabii ki dünyada yalnız olmak istemem, ama neden korkmam gerek ki? Çünkü senin gibi bir arkadaşım var."
    mc "Hep birlikte olacağız, çünkü sen güvenilir birisin."
    s 1bk "Bilmiyorum... ama sanırım yalnız kalma korkusunun olmasına gerek yok."
    s "..."
    hide sayori with dissolve
    "Sayori, sessizleşip başını benden çeviriyor."
    "Bir şeyler gizlediği açık, ama ne olduğunu bir türlü anlayamıyorum."
    mc "Sayori, bir şey oldu mu?"
    show sayori 1bl at f11
    s "Hiçbir şey yok. Endişelenmene gerek yok."
    s 1bt "Sadece... unut bunu. Şu an senin iyileşmen daha önemli."
    s "Bu kadar aptalca bir şey söyledim ki."
    "Sesinden, gözyaşlarını tutmaya çalıştığı belli oluyor."
    "Gülümsemesiyle birlikte sandalyeden kalkıp gitmeye başlıyor."
    "Bunu yapmasına izin veremem!"
    mc "Sayori... bekle!"
    "Güç toplayıp yataktan kalkıyorum."
    s 4bw "[player], hayır! Geri git... hâlâ çok zayıfsın!"
    "Onu hiçe sayıp yanına gidiyorum. O, kaçmak yerine şaşkın bir şekilde bana bakıyor."
    "Geri çekilmeden önce, kollarımı onun etrafına sarıyorum."
    s 1bu "[player]..."
    s "Sen... büyük aptalsın..."
    "Gözlerinden yaşlar süzülmeye başlıyor."
    mc "Beni ne kadar güvendiğini biliyorsun, yani... depresyonundan bile bahsettin."
    s "..."
    "Gözyaşlarını silip bana ciddi bir ifadeyle bakıyor."
    s 1bg "[player], lütfen beni bırak. Kendi sorunlarımı çözmeye çalışarak zamanını boşa harcama."
    "Ses tonu alışılmadık şekilde keskin ve sert."
    "Buna rağmen, kararlı bir şekilde kafamı sallıyorum."
    mc "Bunu yapamam, Sayori. Sen-"
    "Başımı çevirip şiddetli bir öksürük atıyorum, sonra devam ediyorum."
    mc "... Ailem gibisin. Belki daha bile fazlası."
    mc "Sayori..."
    s 1bk "...Açım. Eğer yataktan çıkabilirsen, aşağı inip bir şeyler yiyebiliriz."
    mc "Tamam. Ama önce neyin yanlış olduğunu anlatmanı istiyorum."
    "Sessizce başını sallıyor."
    s "Tamam. Ama seni uyarıyorum – bu mutlu bir hikaye değil."
    mc "Benim için fark etmez. Her ne olursa olsun, birisiyle paylaşmak, her şeyi kendi başına tutmaktan iyidir – özellikle seni rahatsız eden bir şeyse."
    mc "Arkadaşlar bunun için var, değil mi?"
    show sayori 1bk at lhide
    hide sayori
    "Yanıt vermiyor, sadece beni itiyor ve aşağıya iniyor."
    "Onun artık beni görmediğinden emin olduktan sonra, hızlıca pijamalarımı değiştirip günlük kıyafetlerimi giyiyorum."
    "Sonra, kalbim bir şekilde çarparak, aşağıya iniyorum."
    
    scene bg kitchen with dissolve_cg
    "Mutfak kapısından girdiğimde, Sayori’yi masanın yanında otururken görüyorum."
    "Yanında taze ekmek dilimleri ve iki haşlanmış yumurta var."
    "Sayori, ben baygınken bunları alıp hazırlamış olmalı."
    "Yüzü ciddi ve uzak, düşüncelere dalmış gibi görünüyor."
    "Beni ancak seslenmemle fark ediyor."
    show sayori 1bg at f11
    s "İlk önce, yiyelim. Enerjini geri kazanman için yemelisin."
    mc "Tamam."
    mc "Bunları sen mi hazırladın?"
    s "Evet. Senin için kahvaltı yapmak istedim."
    "Onun bu nezaketine minnettar bir şekilde hızlıca yemeye başlıyorum ve söylediği gibi, gücüm geri gelmeye başlıyor."
    "Hastalıktan dolayı iştahım etkilenmiş gibi görünmüyor."
    "Yemekleri bitirdikten sonra, Sayori'nin payına dokunmadığını fark ediyorum ve beni merakla izlediğini görüyorum."
    mc "Aç değil misin?"
    s "Sorun değil... Şu anda yemek yemek istemiyorum. Merak etme."
    s "... Eh, sanırım seninle neden terk edilme korkusu yaşadığımı anlatmam gerekiyor, ha?"
    "Başımı sallıyorum."
    mc "Senin için buradayım, Sayori. Eğer sen üzülüyorsan ve ben bunu biliyorsam, nasıl mutlu olabilirim ki?"
    s 1bk "Çok iyisin... Bunu hak etmiyorum."
    "Gözlerini kapatıp derin bir iç çekiyor."
    play music Dusk fadein 3.0
    "Sonra, hikayesine başlıyor. Ses tonu soğuk ve duygusuz bir şekilde, sanki bir metni okumak gibi – kelimelere çok fazla düşünce koymadan."
    s 1bg "Bildiğin gibi, her zaman başkalarını kendimden önce tutarım..."
    s "Bu, kişisel inançlarım yüzünden."
    s "Kendimi bencil görmek istemem, başkalarına zarar vermek, hatta bencil olmak hayatta kalmanın en iyi yolu gibi görünse bile."
    s "...Büyüdükçe, birçok kişinin yalnızca kendini mutlu etmek için bencilce hareket ettiğini görmek zorunda kaldım."
    s "Anaokulunda, bir arkadaşım başka bir kızın bir bebeğini almak istedi. Kız fark etmeden onu çaldı."
    s "Ben ne yaptığını biliyordum ama arkadaşımı kaybetmek istemediğim için sessiz kaldım."
    s "Sonunda, arkadaşım, başı derde girmesin diye suçu bana attı. Çaldığı kızı ben sevmedi ve ne kadar nefret ettiğini hissedebiliyordum."
    s "O günden sonra, etrafımdakileri mutlu etmek için ne gerekiyorsa yapmaya karar verdim, ne olursa olsun."
    "Sessizleşiyor ve gözlerinden yaşlar süzülmeye başlıyor. Kalkmaya çalışıyorum, ama bunu fark edip, kalmamı istediğini belli eden bir işaret yapıyor."
    "Bir kaç hıçkırığın ardından, toparlanıp hikayesine devam ediyor."
    s "Çocuklar ilkokula başladıklarında, daha bencil olmaya başlarlar."
    s "Sınıftaki diğer çocuklar, kendimi savunamayacağımı fark ettiler çünkü bu, onları hem fiziksel hem de duygusal olarak incitmek anlamına gelirdi... bu yüzden, benden çeşitli favoriler istemeye başladılar."
    s "Ben de dediklerini yaptım, çünkü herkesi mutlu etmek istiyordum."
    s "Birisi vardı, sınıftaki bir çocuk, bana gerçekten değer veriyormuş gibi görünüyordu. Beni her seferinde savunurdu, eğer onlara hayal kırıklığına uğratmışsam."
    s "Sonunda sanırım ona aşık oldum ve onun mutlu olabilmesi için her şeyimi verdim."
    s "Okuldan sonra ona tatlılar alır ve onun yerine derslerini yapardım, ne kadar yorgun olsam da."
    s "Hepsi, onu mutlu etmek için... çünkü gizlice, bencilce, bana karşılık verir diye umuyordum."
    s "Ancak dört yıl sonra öğrendim ki, sadece beni kullanıyormuş..."
    s "Beni hiç değerli görmemişti, ve ben yorulmaya başladığımda, beni küçümsemeye ve zayıf, işe yaramaz diye adlandırmaya başladı..."
    s "Hakkımda arkadan kötü dedikodular yaydı ve yavaşça ama kesinlikle, okuldan korkar hale gelene kadar itibarımı yok etti."
    s "O yaptıklarını öğrendikten sonra bile, ona kızamadım. Benden özür dilediğinde, hemen affettim."
    mc "Vay be... gerçekten bir salakmış!"
    show sayori 1bt at f11
    "Sayori acı bir şekilde gülümsüyor ve dudağını ısırıyor."
    s 1bg "Keşke o kadarla kalsaydı... ve keşke hikaye burada bitseydi..."
    s "Bir gün, bana kız arkadaşı olduğunu söyledi. Ve kim olsa, tahmin edin kim... Aynı kız, bebeğini çalan."
    s "Beni etrafında topladılar ve bana ne kadar değersiz olduğumu söylediler... bana, arkadaşlık ve sevgiyi hak etmediğimi... ne kadar değersiz olduğumu söylediler..."
    s "O kadar ısrar ettiler ki, onlara inanmaya başladım... ve hala inanıyorum."
    s "Sonuçta... bu benim hatam. Eğer başkalarını mutlu etme isteğim bu kadar bencil olmasaydı... belki..."
    s 4bw "Belki..."
    "Bir dizi hıçkırıkla çöker."
    "Yanına gidip onu sarılıp, ağlamasına izin veriyorum."
    stop music fadeout 3.0
    play music Dawn fadein 3.0
    mc "Sayori, beni dinle..."
    mc "Seni terk etmeyeceğim... Ben o salaklardan değilim."
    mc "Seni bir insan olarak değerli buluyorum – yaptığın şeyler için değil, kim olduğun için."
    s 1bw "Ama... çok korkuyorum..."
    s "Ya... y-ya... biri daha iyi birisini bulursa..."
    mc "Gerçekten ‘daha iyi’ birini bulmam söz konusu değil."
    mc "Başka arkadaşlarım olsa da, seni asla terk etmem."
    mc "Ve senin kendini değersiz hissetmen... kesinlikle değilsin."
    mc "Benim için çok değerli birisin..."
    mc "Ve düşündüğünden çok daha iyisin."
    mc "Benim seninle burada olmam, bunun kanıtı değil mi?"
    mc "En düşük anlarında seni terk etmediğime göre... gelecekte seni terk edeceğimi düşünmene gerek yok."
    mc "Zaten... birçok arkadaşım tarafından terk edilmiş ve hayatım boyunca bir şaka gibi görülmüş biri olarak, seni çok iyi anlıyorum."
    "Beni sıkıca sarıldığını hissediyorum ve bir süre, onu sakinleştirip yavaşça sıvazlıyorum."
    "Sonunda, sakinleşiyor ve iç çekiyor."
    s "Bunu görmek zorunda kaldığın için üzgünüm..."
    mc "Sorun değil. Mutluyum... şimdi seni daha iyi tanıyorum, Sayori."
    mc "Arkadaşım olduğun için mutluyum. Ve sana yardımcı olmak da beni mutlu ediyor."
    "Bunun sadece hayal gücüm olup olmadığını bilmiyorum ama, sanki biraz daha sıcak hissediyorum."
    s 1bd "Teşekkür ederim..."
    s "Bana ne kadar çok şey ifade ettiğini sana anlatamam..."
    mc "Bilin ki artık yalnız değilsin."
    mc "Artık içindeki tüm canavarlara yalnız başına karşı olmak zorunda değilsin."
    "Gülümsemesi geri dönüyor."
    s 1bc "Tamam. Sana güveniyorum..."
    s "Hmm... ne garip..."
    mc "Neyin var?"
    s "Bu sıcaklık hissi... sana her şeyi söylediğime dair tuhaf bir rahatlama hissediyorum."
    mc "İyi hissetmene sevindim."
    s "Hey! O benim repliğim!!"
    s "Unutma, sana bakmaya geldim. Tam tersine değil!"
    mc "Haha, nasıl unuturum ki?"
    mc "Ama her zaman benimle konuşabilirsin, Sayori. Sorunun büyük ya da küçük olsun, endişelerin varsa, yanındayım. Tıpkı senin benim için olduğun gibi."
    s "Biliyorum... ve bunun için çok minnettarım... ama hala korkuyorum. Yük olmak istemiyorum."
    mc "Hiçbir zaman bana yük olmadın."
    mc "Şu anda biraz utanç verici şeyler söyleme havasındaysak... sanırım şunu söylemeliyim ki, senin hayatımda olman dışında, tamamen yalnız kalırdım."
    mc "Başka kimse beni ciddiye almaz. Hatta annem bile beni sadece bir salak olarak görüyor olabilir."
    mc "Ama sen her zaman beni ciddiye alıyorsun ve bana her zaman saygı gösteriyorsun."
    mc "Sana gerçekten daha fazla borçlu olduğumu biliyorsun."
    s 2bt "Çok iyisin."
    s "Hey, bunu şimdi bitirelim."
    s "Eğer konuyu değiştirmezsek, kalbim patlayacak gibi hissediyorum."
    mc "Tamam. Ne yapmak istersin?"
    s 1bt "Lütfen, geri dönüp sana bakmama izin ver. Bunu gerçekten çok seviyorum."
    s "Sana faydalı olmak güzel bir his."
    "İçimden üzgün bir iç çekiş atıyorum."
    mc "Tamam, peki."
    "Oturup odam için çıkmak üzereyken, bana sesleniyor."
    s "Ayrıca, [player]..."
    mc "Hmm?"
    "Gülümsüyor."
    s 1br "Bir kez daha teşekkür ederim. Seninle konuşmak gerçekten çok mutlu ediyor beni!"
    "Sadece gülümsüyorum ve yukarı çıkıyorum."
    stop music fadeout 2.0
    hide sayori with dissolve
    show black with dissolve_cg
    
    "Günün geri kalanı drama olmadan geçiyor."
    "Sayori, bana bakıyor ve günün sonunda hastalığımın giderek zayıfladığını hissediyorum."
    "Konfor olmasına rağmen, aramızda dün olmadığı bir gerginlik var."
    "Sürekli onun söylediklerini düşünüyorum."
    "Nihayet Sayori evine gittiğinde, gece yarısı çoktan geçmişti ve uyumaya hazırlanırken, onun gerçekten nasıl acı çektiğini fark ettim."
    "Sayori..."
    "Uykunun karanlığı beni sarhoş ederken, ona nasıl hissettiğimi yarın söylemeye karar veriyorum."

    call sayoriRoute_truth
    return


label sayoriRoute_truth: 

    scene bg bedroom with open_eyes
    "..."
    "Gözlerimi açıyorum ve sabah güneşi perdemden içeri sızıyor."
    "Sayori'nin ilgisi sayesinde oldukça iyi hissediyorum. Ateşim hala geçmedi, ama artık çok daha hafif."
    "Yavaşça yataktan kalkıyorum."
    "Bacaklarım zayıf ve giyinirken biraz başım dönüyor."
    "Saate bakıyorum ve Sayori’nin çok geçmeden gelmesi gerektiğini düşünüyorum, bu yüzden aşağıya inip ona sürpriz yapmaya karar veriyorum."
    
    scene bg kitchen with dissolve
    "Yarım saat geçiyor, kahvaltıyı hazırlayıp Sayori'yi bekliyorum..."
    "Ama hala gelmedi."
    "Saate bakıp telaşlanmaya başlıyorum – şimdiye kadar gelmesi gerekirdi."
    "Hatta bir söz vermiştik."
    "Bunu çok mu zorlamış olabilirim? Belki onu kendi durumuma bu kadar aniden ilgimi göstererek korkutmuş olabilirim?"
    "Ama diğer taraftan, Sayori’nin çokça dikkatsiz olduğunu ve bazen uykusunu geçirebildiğini de biliyorum."
    "Belki hala hazırlanıyor."
    "Bir şekilde kendimi sakinleştirmeye çalışırken, mideimdeki kaygıyı bir türlü atamıyorum."
    "Onu aramalı mıyım? Yoksa bu sadece yapışkan biri gibi mi görünmeme sebep olur?"
    "Kafamda tartışırken, kapı kolunun döndüğünü duyuyorum."
    "Ama kapı açılmıyor."
    "Pencereyi aralayıp dışarıya bakınca, Sayori’nin kapımın önünde, yüzünde kararsız bir ifadeyle durduğunu görüyorum."
    "Neden tereddüt ediyor?"
    "Beni görmek istemiyor mu?"
    "Anahtarını parmaklarında çeviriyor, sanki kapıyı açıp açmaması gerektiğinden emin değilmiş gibi."
    "Aman Tanrım... Sanırım sorunun ne olduğunu biliyorum."
    "Kesinlikle benim söylediklerimi, sanki ona aşık olduğumu düşündü ve o da bana karşı aynı duyguları beslemiyor."
    "Neden ki? Hem... neden bu düşünce beni bu kadar üzüyor?"
    "Gerçekten ona ilgi mi duydum?"
    "Hayır, bu imkansız. Yıllardır birbirimizi tanıyoruz ve herhangi bir belirti görmedim."
    "Ama riskin de çok büyük olduğunu biliyorum."
    "Ama bu düşüncelerim, pencereden bana bakarken gözleri korkudan büyüyen Sayori’yi gördüğümde kesiliyor."
    "Gözleri korkuyla genişliyor, geri adım atıp hızla koşmaya başlıyor."
    "Kaygı içimde mantıklı düşüncelerimi yutuyor."
    scene bg house_entrance with wipeleft_scene
    play sound closet_open
    "Ceketimi alıp, kapıyı bile kilitlemeden hızla peşinden koşuyorum."
    play sound closet_close
    scene bg residential_day with dissolve_cg
    
    "Güçsüz bacaklarımda ne kadar hızlanmaya çalıştıysam da yeterli olmuyor."
    "Kötü kondisyonum ve Sayori’nin göründüğünden çok daha hızlı olmasından dolayı aramızdaki mesafe açılmaya devam ediyor."
    "Bunu kaybetmek üzereyim..."
    "Sadece onu kaybetme düşüncesi, her şeyden daha fazla korku veriyor, bir şeyleri doğru yapamadığımı hissediyorum ve koşarken tüm gücümü harcıyorum."
    "Ortada yolun ortasında Sayori koşarken, nefes nefese kalmış bir şekilde arkamı döndü ve beni gördü."
    show sayori 4bm at f11
    "Gözleri korkudan genişliyor. Aramızdaki mesafe hızla kapanıyor ve bir anda tam önümde."
    s "Neden...? "
    "Ben de gözlerimi açarak şaşkınlıkla bakıyorum."
    "Ama Sayori'nin durmasından değil... "
    "...gözlerimi büyüten büyük bir kamyonun tam hızla gelmesinden."
    "Eğer şu anda hareket etmezse, sürücü frene basmış olsa bile bir şekilde sağlam zarar alacak."
    mc "Sayori, dikkat et!"
    show black
    "Son gücümü toparlayarak, bir jaguar gibi üzerine atlıyorum ve onu yoldan çekiyorum."
    "Kendimi onun için yastık yaparak, kamyonun neredeyse birkaç santimden geçmesini sağlıyorum."
    scene bg residential_day
    show sayori 1bn at f11
    with open_eyes
    "Gözlerimi yavaşça açıyorum ve Sayori'nin üstümde yatarken beni izlediğini görüyorum."
    "O hala şok olmuş, ama tamamen sağlıklı."
    show sayori 1bn at t11
    "İkimizin de güvende olduğunu fark eder etmez, tek kelime etmeden üstümden kalkıyor."
    "Yine kaçmaya çalışıyor, ama ben onun elini tutup başımı sallıyorum."
    mc "Lütfen gitme."
    show sayori 1bt at f11
    "Bir şey söylemeden, sadece yüzündeki ifade bana artık direnmeyeceğini gösteriyor."
    mc "Hadi, daha güvenli bir yere gidelim."
    "Vücudu gibi, benimkisi de titriyor."
    "Hayatımda hiç bu kadar korkmamıştım."
    "Bir anlığına, tek dostumu kalıcı olarak kaybettiğimi düşünmüştüm."
    
    scene bg house with wipeleft_scene
    show sayori 1bt at f11
    "Sayori’nin evinin önüne geldiğimizde duruyorum ve onun elini bırakıyorum."
    mc "Sayori... ne oldu? Neden kaçtın?"
    mc "Hemen ölme tehlikesiyle karşılaşabilirdik! Ne kadar korktum, biliyor musun?"
    s 1bw "Ben... Özür dilerim..."
    s "Şey... Dün söylediğin şeyden sonra ne yapacağımı bilemedim..."
    s "Bana ne kadar değerli olduğumu söylediğin zaman... bu beni korkutuyor."
    s 1bh "Bunu hissetmek bana yabancı, kimsenin bana değer göstermesini istemiyorum ama aynı zamanda seni kaybetmek, ölmeye korktuğumdan daha çok korkutuyor."
    "Omuzlarından tutup, gözlerinin içine bakıyorum."
    mc "Neden kaybetmekten bu kadar korkuyorsun, sana defalarca kaybetmeyeceğini söyledim?"
    s "Ben... "
    mc "Lütfen bana söylemekten korkma."
    "O, ellerini sıkarak gözlerinden yaşlar süzüldüğünü görüyorum."
    play music Thoughts fadein 3.0
    s "Tamam. Söyleyeceğim."
    s "Gerçekten... uzun zamandır..."
    s "Ben... sana... duygularım var, [player]."
    "Ona bakıp, şaşkına dönüyorum. Sadece gözlerimi kırpabilirim."
    s "Aslında... dün gelmemin nedeni de buydu..."
    s "Seni görmek istedim ve sana bakmak... "
    s 1bw "Aslında bunu senin için yapmadım... Ben bencildim ve bunu... "
    mc "Sen... sen... hissediyor musun...?"
    mc "NE?!"
    "Bunu hiç bilmiyordum. Hiçbir şey buna hazırlıklı olamazdı."
    s 1bh "Özür dilerim. Gidip gideceğim... sana söz veriyorum, bir daha asla seni görmeyeceğim."
    s "Benden çok daha iyisin."
    s "Bunu her zaman hissettim, küçükken oyuncak ayıcığımı tamir ettiğin zaman."
    s "Okulda tek senin bana iyi davrandığın zaman."
    s 1bl "Ama son birkaç haftadır, duygularım daha da arttı."
    mc "Sayori..."
    s 2bv "Literatür Kulübü’ne katılmanı istememin nedeni de bu... Seninle daha çok vakit geçirmek istedim..."
    s "Ama sonra endişelenmeye başladım. Ben yeterince iyi değilim... hem zaten Literature Club’ta benden çok daha iyi kızlar var."
    s 4bw "Lütfen... unuturum dediklerimi! Seni kaybetmek istemiyorum. Romantik olarak seninle olamasam da, en azından seni arkadaş olarak kaybetmek istemiyorum!"
    hide sayori with dissolve
    "Onu kollarıma alıp sarılıyorum."
    mc "Sayori..."
    mc "Hiç bu kadar mutlu olmamıştım."
    mc "Ben... aynı şekilde hissediyorum."
    s "... Gerçekten...?!"
    "Başımı sallıyorum."
    "Bunu tarif etmek zor, ama son zamanlarda Sayori, bana her zamankinden daha önemli hale geldi."
    "Ona duygularım olduğunu söylediği zaman... daha önce hiç hissetmediğim kadar mutlu oldum."
    show sayori 1bt at f11
    "Gözlerinin içine bakıyorum. Artık kararımı verdim – ne olursa olsun, olacak."
    mc "Sayori..."
    mc "Her zaman özel oldun... ama son zamanlarda, fark etmeye başladım ki sana olan duygularım artık sıradan arkadaşlık duygularını aşıyor."
    s 1bg "[player]... Ben... "
    mc "Çıkmak ister misin?"
    if(sayori_affection <= 0):
        call sayoriRoute_REJECTED
    else:
        call sayoriRoute_notRejected

    return

label sayoriRoute_REJECTED:


    stop music
    play music Dusk
    "Sayori nefesini tutarak gözlerinden yaşlar süzüldü."
    show sayori 1bw at f11
    s "Ben... Yapamam..."
    mc "Sayori?"
    s 4bw "Özür dilerim. Bunu yapamam!"
    s "Bu çok fazla... Gerçekten emin olamam, bunu kastettiğine nasıl güvenebilirim?"
    mc "Gerçekten de öyleyim."
    s "Hayır. Üzgünüm... Bunu yapamam... Gitmeliyim."
    s "Biraz düşünmem gerek."
    s "Lütfen..."
    
    show sayori 4bw at lhide
    hide sayori
    stop music fadeout 3.0
    show black with dissolve
    "Ona engel olmadan, ağlayarak kaçtı."
    "Sesindeki güvensizlik çok barizdi."
    "Evinin kapısını kilitledi ve aramalarımı cevaplamadı."
    "Ertesi gün gelmedi ve iyileşip okula gitmeye çalışırken, beni aramaya cevap vermedi."
    "Endişeleniyorum..."
    call sayoriRoute_badEnd
    return


    label sayoriRoute_badEnd:
    
    
    $ sayori_goodEnd = False
    
    play music LettingGo fadein 3.0
    scene bg residential_day with dissolve_cg
    "Okula tek başıma yürürken... Sayori'yle yürüdüğümdeki gibi hissetmiyorum."
    "Ve bu, iyi bir şekilde değil..."
    scene bg class_day with dissolve_cg
    "Derslere odaklanamıyorum. Aklımda tek şey, Sayori'nin durumuyla ilgili endişelerim."
    scene bg corridor with dissolve_cg
    "Bir süre sonra, günün son dersi bitiyor ve ben hızla Edebiyat Kulübüne koşuyorum."
    scene bg club_day
    show sayori 1t at f11
    with dissolve_cg
    "Orada, Sayori'yi bir masada, bir şeyler yazarken buluyorum."
    s 1l "Ah, [player]."
    mc "Selam, Sayori... Dün sana yanlış bir şey söylediysem özür dilerim."
    s 1k "Bu... bu sorun değil. Endişelenme."
    "Aramızda garip bir sessizlik var."
    s "[player]... Sanırım ben sana özür borçluyum..."
    s "Ama... pes ediyorum. Artık bunu yapamayacağım."
    mc "Ne? Ne demek istiyorsun?"
    s 1g "Artık mutluymuş gibi yapmanın bir anlamı yok."
    s "Yalan söylemeyi bırakıyorum..."
    mc "Sayori..."
    "Bütün bunların suçlusu ben miyim?!"
    "Keşke onu daha iyi anlamış olsaydım... Ona güvenmesi için bir neden verseydim..."
    "O zaman bu asla olmayacaktı."
    s 2k "Edebiyat Kulübünden ayrılıyorum."
    "Omuzlarından tutarak ona yalvarmaya çalışıyorum."
    mc "Lütfen bunu yapma, Sayori! Hala-"
    s 4t "Yeter. Bu beni daha da çok acıtıyor."
    s "Denemeye çalıştım. Gerçekten ama... sen beni ciddiye almadın bile."
    s "Biliyorum nasıl hissettiğini... Ama bana dürüst ol... Beni sadece depresyonum yüzünden kolay bir hedef olarak gördün, değil mi?"
    s "Sonuçta, kim istemez ki kendisine koşulsuz bir şekilde sevgi veren bir kız arkadaş, çünkü özgüveni çok düşük olduğu için sana karşı çıkamayacak?"
    mc "Bu hiç böyle değil!"
    mc "Biliyorum, bu sadece depresyonumun kafanı karıştırdığına işaret!"
    s 1u "...Hayır. Bunu düşündüm... ve sanırım bundan sonra insanlardan uzak durmam daha iyi olur."
    s "Sana ne kadar mutlu oldum dediğinizi söylemen beni gerçekten mutlu etse de... aynı zamanda bana değersiz, önemsiz hissettirdi... kendimi senin altımda gibi hissettirdi."
    s "Bir arkadaşımın sadece bana acıdığı için iyi davranmasını, benimle buluşmasını istemiyorum."
    s 1k "Özür dilerim... ama sanırım bir süre konuşmamız daha iyi olacak."
    show sayori 1k at lhide
    hide sayori
    "Beni itip odadan çıkıyor."
    mc "Sayori, dur!!"
    scene bg corridor with wipeleft_scene
    "Onun peşinden koşuyorum ama çoktan koridordaki yerini almış."
    mc "Beni bırakma. Pes etme! Depresyonunun seni alt etmesine izin verme!!" 
    show sayori 4n at f11
    "Bir anda duruyor, bir de ne göreyim."
    "O an anlıyorum ki, onun en derin sırrını herkesin duyacağı şekilde yüksek sesle bağırdım."
    show sayori 1w at f11
    pause(2.0)
    show sayori 1w at lhide
    hide sayori 
    "Bana gözyaşlarıyla kısa bir bakış atıyor ve hızla uzaklaşıyor."
    "Ben de peşinden koşuyorum ama o benden çok hızlı."
    "O bana gönderdiği bakış... üzüntü ve nefretle doluydu."
    "Kesinlikle biliyorum, bu bitti. En iyi arkadaşımdan oldum, tek arkadaşımdan."
    "Yere çöküyorum ve gözyaşlarım akıyor."
    "...Onu kaybettim."
    "Onu aramaya çalışıyorum ama numaramın engellendiğini öğreniyorum."
    "Sayori..."
    
    show black with dissolve_cg
    "Ve işte, günler, haftalar ve aylar geçiyor."
    "Okulda Sayori’yi her gördüğümde, o beni görmezden geliyor. Eğer onunla konuşmaya çalışırsam, bana öyle bir bakıyor ki, başarısızlığımı hatırlatıyor."
    "Sonunda, korkunç bir hata yapıyor."
    "Bir gün, onunla konuşmaya çalışırken okul çatısına atlamaya kalkıyor."
    "Baskı çok fazla."
    "Başka birinin hayatını tehlikeye atmayı başaramıyor. Ama düşüşünden aldığı yaralar nedeniyle hastaneye kaldırılıyor." 
    "Ve o, ondan bir daha hiç haber almadığım zamandı." 
    
    scene bg bedroom with open_eyes
    "..."
    "O günden beri üç ay geçti."
    "Bitti. Artık yaşamak için hiçbir nedenim yok."
    "Ne ironik ki, artık onun için bir şey yapmanın çok geç olduğu bir noktada, ben de depresyona girdim... Şimdi Sayori'nin nasıl hissettiğini anlayabiliyorum."
    "Sayori'nin son durumuyla ilgili tek bildiğim şey, hâlâ bir yerde yaşadığı... ama artık günlerini hastanede geçirdiği." 
    "Düşüşü birkaç kemiğini kırdı ve ayrıca... onun intihar girişimi, ailesinin alarm vermesini sağladı ve bir psikiyatrist atadılar." 
    "...Bunu, Edebiyat Kulübündeki diğerlerinin yardımıyla öğrendim." 
    "Kulüp hakkında ise, işler yavaşça dağıldı."
    scene bg club_day
    show natsuki 4e at t21
    show yuri 2k at t22
    with dissolve_cg
    "Yuri ve Natsuki arasındaki tartışmalar, Sayori’nin engellemesiyle eskisinden bile daha sık hale geldi ve çatışmalar, o kadar şiddetli bir boyuta geldi ki, artık aynı odada bile kalamıyorlardı."
    hide natsuki
    hide yuri 
    with wipeleft
    show monika 1f at t11
    "Monika kulübü feshetmek zorunda kaldı."
    hide monika with wipeleft
    scene bg bedroom with dissolve_cg
    "...O iki ay önceydi."
    "O günden beri evden dışarı adımımı atmadım." 
    "Bundan sonra hayatımın geri kalanını burada geçireceğim." 
    "Ama bu, bir şekilde bunu telafi etmek için olduğunu düşünmüyorsunuz, değil mi?"
    "Sadece pes ettim."
    "Artık hiçbir şeyin anlamı yok."
    "Beni her zaman mutlu eden anime bile artık sinirimi bozuyor." 
    "Okula gitmenin bir anlamı yok."
    "Notlarım artık tamamen bozulmuş durumda."
    "Beni önemseyen tek şey gitti..."
    "Sayori gitti."
    "O hâlâ yaşıyor olabilir, ama bir daha onu asla göremem."
    "Onunla mutlu olabilirdim – ve daha da önemlisi, onu mutlu edebilirdim ve ona gerçekten ne kadar sevdiğimi gösterebilirdim."
    "...Ama artık o olmayacak."
    
    show black with dissolve_cg
    "Asla..."
    
    window hide
    pause(1.5)
    show end with Dissolve(3.0)
    stop music fadeout 3.0
    pause(2.0)
    hide end with Dissolve(2.0)
    return



label sayoriRoute_notRejected:
    "Sayori derin bir nefes alıp bana şaşkın bir şekilde bakıyor."
    mc "Sayori?"
    s 4bm "İstemem, ama..."
    s 4bh "Buna emin misin?"
    s "Yani... Seni pişman olacağın bir şey yapmanı istemem."

    scene s_cg3 with dissolve_cg
    "Hissettiklerimi gösterebilmek için onu sımsıkı kucaklıyorum. O da bunu karşılık veriyor ve beni o kadar sıkı tutuyor ki, neredeyse biraz acıyor."
    "Açıkça, benden ayrılmaktan korkuyor, tıpkı ben de ondan ayrılmaktan korktuğum gibi."
    "Boynumdan gözyaşlarının aktığını hissediyorum ve sırtını okşayarak tüm kaygılarını dökmesine izin veriyorum."
    "Fark etmeden, gözlerim de yaşarmaya başlıyor."
    mc "İnan bana, bunu istiyorum."
    mc "Sanırım... her zaman böyle hissettim, sadece fark edecek kadar farkındalık gösteremedim."
    mc "Sayori... Ben..."
    "Cümlemi bitiremiyorum, çünkü ben de ağlamaya başlıyorum."
    "Ve böylece, ikimiz de sessizce birbirimizi tutuyoruz. Bizim tek duyduğumuz şey, içimizden gelen boğuk hıçkırıklar ve telaşlı nefesler."
    "Onu daha yakın alırken, kalbinin hızla atışını adeta hissediyorum."
    "İkimiz de titriyoruz, hem korkudan hem de beklentiden."
    "Bunu düşününce, nasıl fark etmedim ki? Sayori, bana kimsenin bana hissettirmediği bir şey hissettirdi."
    "Hep bunu arkadaşlık olarak adlandırmıştım... ama sanırım hislerimi küçümsemişim."
    "Hayır, küçümsemek değil... tamamen yanlış anlamışım."
    "Tam da ne olduğunu anlamadığımda, işte bu an, gerçekte ne hissettiğimi fark ettiğim an oldu."
    s "Bu benim için çok fazla... Hem mutluyum hem korkuyorum."
    mc "Üzgünüm..."
    s "Üzülme. Açıklamak zor, ama... mutluyum çünkü korkuyorum."
    s "Sanırım... aşktan korkuyorum."
    mc "Ben de aynı şekilde."
    mc "...Sayori, sana şunu soracağım: Benimle sevgili olur musun?"
    "Sayori, gözleri yaşlarla dolmuş şekilde bana bakıyor."
    stop music fadeout 3.0
    scene bg house
    show sayori 1bl at f11
    with dissolve_cg
    s "İstemek isterdim, ama... yapamam."
    s "Kendimi sevmediğim sürece... hiç bir ilişki nasıl iyi gidebilir ki?"
    s "Yine de, bu anın bitmesini istemiyorum."
    "Birden aklıma bir fikir geliyor."
    mc "Peki, o zaman?"
    mc "Neden gayri resmi bir ilişki denemiyoruz?"
    s 1bn "Gayri resmi... ilişki?"
    "Başımı sallayarak gülümsüyorum."
    mc "Yani... bir ilişki yaşamaya çalışalım, ama arkadaşlıktan daha fazlası olalım, fakat normalden daha yavaş ilerleyelim."
    mc "Bunu, senin – yani ikimizin de rahat edeceği bir hızda yapabiliriz."
    mc "Artık biliyorum... bence unutmak istemiyorum."
    s 1bt "Ben de istemiyorum."
    s "Ama lütfen, neye bulaştığını bilmeni umarım."
    s "Yani, gerçekten... oldukça yüksek bakım isteyen biriyim, diyelim."
    mc "Ben de öyleyim. Ama dürüst olmak gerekirse, hiç fark etmez. Eğer bu sensen, fark etmez."
    "Yüzünü okşayıp gözyaşlarını siliyorum."
    mc "Beni garip bulabilirsin, ama seni yardımcı olmak hoşuma gidiyor. Eğer seni güldürebilirsem, gerektiğinde ‘bakım yapmayı’ sevinçle kabul ederim."
    s "Vay..."
    s "Ben... bu hissettiğim şey ne, bilmiyorum..."
    "Gözyaşları yine yüzünden süzülmeye başlıyor ama bu sefer gülümsüyor."
    s 1bx "Hayatımda hiç bu kadar mutlu olmamıştım!"
    s "Ben..."
    s "Seni seviyorum, [player]."
    "Bu sözleri ağzından duymak, bana içimi ısıtan ve beni neşelendiren bir his veriyor."

    "Tüm vücudum ısınıyor."
    "Onu daha da yakın alıyorum."
    "Onu böyle tutmak o kadar güzel ki..."
    mc "Ben de seni seviyorum, Sayori."
    mc "Ve seni hayal kırıklığına uğratmayacağım, ne kadar zorlu bir yol olursa olsun."
    "Sayori hiçbir şey demiyor ve sadece sessizce ağlıyor."
    "Ağlaması bittikten sonra başını kaldırıp gözlerime bakıyor."
    show sayori 1bq at face_one(y=300) with dissolve
    "Gözlerini kapatıp yüzünü bana yaklaştırdığını görüyorum."

    show black with close_eyes

    "Gözlerimi kapatıp, yarı yolda buluşuyorum, dudaklarının benimkilerle buluştuğunu hissediyorum."
    "Dudakları o kadar yumuşak ki, biraz ıslaklar, ve o kadar nazikçe bastırıyor ki, sanki eğer fazla güç uygularsa ben toz olacağım korkusuyla."
    "Bunu karşılık veriyorum."
    "O kadar sıcak hissediyorum... bu his sadece aşk olabilir."
    scene bg house
    show sayori 1ba at f11
    with open_eyes
    "Gözlerimi açtığımda, az önce ilk öpücüğümü aldığımı ve bunun Sayori ile olduğunu fark etmeye başlıyorum."
    "Ve bu, hep arkadaşımdan daha fazlası olarak önemsediğim, başlangıcından beri yanımda olan kızla."


    mc "Vay."
    s "Bu... çok güzeldi."
    "Ses tonu neredeyse bir fısıltı gibi. Şimdi başka bir şekilde... çok daha nazik ve yumuşak."
    s 1bh "[player]..."
    s "Belki sana en iyi seçim olamayacağım... ama sana mükemmel bir partner olmak için elimden geleni yapacağım."
    "Başımı sallıyorum."
    mc "Hayır, lütfen çabalama."
    "Kendi sesimi de daha düşük duyuyorum. Sadece ona duyması için söylemek istiyorum."
    "Saçlarını okşuyorum."
    mc "Seni olduğun gibi seviyorum."
    s 1be "Neden?"
    mc "Çünkü seni sevdiğim kişi sensin."
    mc "Mükemmel olmaya çalışmanı istemiyorum... çünkü kimse mükemmel değil."
    mc "Ama seni tanıdıkça, inatçı olduğunu biliyorum ve yine de çabalayacaksın, değil mi?"
    "O gülüyor."
    s 1bx "Görünüşe göre, sonunda beni bütün bu yıllardan sonra anlamaya başlıyorsun."
    s "Senin için her şeyi yaparım, [player]. Seni mutlu etmek için her şeyi... bu şekilde hissetmeme sebep olduğun için sana borçluyum."
    "Onu kollarımda tutarken, gerçekten ona aşık olduğumu fark ediyorum ve bu kadar harika birinin bana aşık olmasından çok mutluyum."
    "Onu, şu anki kadar mutlu edebilmek için nasıl bir şey yapabilirim ki?"
    mc "Sadece bir şey söz ver..."
    s "Nedir?"
    mc "Lütfen artık birbirimizden sır tutmayalım."
    "Beklemediğim bir şekilde Sayori başını sallayarak onaylıyor."
    s 1bc "Tamam. Söz veriyorum..."
    s "Sadece... bana da bir şey söz ver, [player]."
    "Başımı sallayıp ellerini tutuyorum. Ellerinin sıcacık ve biraz terli."
    mc "Her şey."
    s 1bl "Lütfen... gitme. Asla. Benden daha iyi birini bulsan bile..."
    "Onu sıkıca tutup kulağına nazikçe fısıldıyorum."
    mc "Merak etme. Hiçbir kızın yönüne bile bakmam."
    mc "Ve ayrıca, bence kimse sana kıyasla senin kadar özel olamaz."
    mc "Sen her zaman yanımda oldun... ve ben de seninle olmak istiyorum. Başka hiç kimseyle."
    s 1be "Seni çok seviyorum..."
    s "Kimse bana böyle tatlı ve nazik şeyler söylememişti daha önce..."
    show sayori 1bm at f11
    "Birden gasps."
    s "Aman Tanrım! Hala hasta olduğunu tamamen unuttum!"
    mc "Endişelenme."
    mc "Hiç bu kadar iyi hissettiğimi sanmıyorum..."
    s 1bn "Emin misin? Hala seninle ilgilenebilmek için günü izinli almıştım."
    "Başımı sallarken, başka bir fikir aklıma geliyor."
    mc "Yine de seninle gün boyunca vakit geçirmek istiyorum."
    s "Ben de aynı şekilde hissediyorum."
    mc "Yani... senin için sorun olur mu? Hani şimdi ne olduğunu düşündükten sonra, ister bir süre vakit geçirmemiz..."
    "Beni yalnızca bir öpücükle susturuyor."
    s "Bunu hayal ettiğim kadar çok bekledim..."
    s "Her anı seninle geçirmek istiyorum."
    s 2bl "Bana izin verirsen tabii..."
    "Onu geri öpüp, tüm içimi rahatça hissettirdiğini fark ediyorum ve birlikte zaman geçirme kararı veriyorum."
    s 2bc "Peki, ne yapmak istersin?"
    mc "Pek umurumda değil, yeter ki seninle birlikte bir şeyler yapalım."
    s 1ba "Ehehe... Aynı şekilde hissediyorum."
    s "Ama herhalde bir şeyler yapmalıyız..."
    mc "Parkta yürümeye ne dersin?"
    s "Bunu çok beğendim."
    scene bg residential_day
    show sayori 1ba at f11
    with dissolve_cg
    "Birbirimizden ayrılıp, otobüs durağına doğru yürümeye başlıyoruz."
    "Ancak, bir süre sonra Sayori aniden duruyor."
    mc "Sayori, iyi misin?"
    "Sesimdeki endişeyi duyduğunda, sadece nazikçe gülümsüyor."
    s 2bn "İyiyim. Sadece... bu, birlikte yaptığımız ilk şey, çift olarak."
    mc "Bunu dert etme, istediğin hızda ilerleyebiliriz."
    s "Biliyorum..."
    s 1ba "Sadece... heyecanlıyım sanırım."
    mc "Ben de. Heyecanlı ve biraz gerginim... ilk günden bir şeyleri mahvetmek istemiyorum."
    mc "Hadi, yoksa otobüsü kaçırırız."
    stop music fadeout 4.0
    "Başını sallıyor ve yan yana yürürken, bir noktada elini tutmaya başlıyoruz."
    "Yan yana yürürken, yüzümün ısındığını hissediyorum. Onunla el tutuşmak harika."
    "Ve işte çift olarak geçireceğimiz zaman böyle başlıyor."
    
    scene bg park_day with dissolve_cg
    play music NextToYou fadein 3.0
    "Parkta, biraz garip ama harika bir gün geçiriyoruz."
    "İkimiz de birlikte yürüyüp el tutuyoruz."
    "Birçok başka çiftin yürüdüğünü fark ediyoruz ve bu manzara, Sayori’yi benim gibi biraz da olsa utandırıyor gibi."
    "Sonunda, Sayori duruyor ve derin bir nefes alıyor."
    show sayori 1bt at f11
    s "Onlar çok mutlu görünüyorlar."
    "Dudaklarını ısırarak devam ediyor."
    s 2bl "Sence... yani..."
    "Onun ne demek istediğini hemen anlıyorum ve başımı sallayarak, parmaklarımı saçlarında gezdirip nazikçe karıştırıyorum."
    mc "Evet, bir gün biz de onlara benzer bir noktaya geleceğimizi düşünüyorum."
    s 1bh "Çok haksız. Ben seninle çok mutluyum... ama yola çıktığımızda kafamda birçok düşünce vardı."
    s "Çok korkuyorum, bu durum sonsuza kadar sürmez diye."
    mc "İkimiz de istemiyoruz, değil mi?"
    "Sadece başını sallıyor."
    s "Ama sanmıyorum ki onlardan birinin içinde, benim gibi bir şeyler olsun."
    "Omuz silkiyorum."
    mc "Biliriz, belki de biliyorlardır."
    mc "Son bir haftada öğrendiğim bir şey varsa, o da... insanın içini tam olarak neyle doldurduğunu asla bilemeyeceğimizdir."
    mc "... Bütün bir hayatını tanıdığın biri olsa bile."
    s 1bt "Evet..."
    "O kadar çok onu güldürmek, ona ne kadar değerli olduğunu anlatmak istiyorum ki."
    "O yüzden, sadece onu daha yakın tutup sarılıyorum."
    mc "Bana ne zaman çok garip gelirse, lütfen söyle olur mu?"
    s 4bg "Söyleyeceğim."
    s "Sen de..."
    "Birden yüz ifadesi kararıyor."
    s 1bh "Yine de sanırım, arkadaşlığımız mahvoldu."
    s "Şeyler artık eskisi gibi olmayacak, bu beni korkutuyor."
    mc "Beni biraz korkutuyor ama... bence bu risk almaya değer, bizi mutlu ediyorsa."
    mc "Yoksa... mutsuz musun? Bu sabahki halimize geri dönmek ister misin?"
    s "İstemiyorum."
    mc "Sadece iki arkadaş olarak vakit geçirdiğimizi söyleyebiliriz."
    s 1ba "Evet, bu hoş olurdu..."
    s "Ama sanırım sadece arkadaş olmak istemiyorum."
    s 1bt "Ne kadar düşünsem de kaybediyorum..."
    s "Sanırım hayat böyle adil değil."
    mc "Böyle olmak zorunda değil. Sadece sen vazgeçersen biter."
    mc "Ve ben seni mutlu etmek için her şeyi yapmaya kararlıyım."
    s "Bu sadece benim için mi?"
    mc "Hayır... seni romantik olarak sevmenin ötesinde seni seviyorum--seni..."
    "Cümlem bitmeden, beni öpüyor ve bana sıkıca sarılıyor."
    s 1bc "Ne kadar kusurlarını düşünmeye çalışsam da, senin mükemmel olduğunu hissediyorum... rüyada gibisin."
    mc "Sayori..."
    s 1bt "Beni sevdiğin için mutluyum... ama senin sevgini hak etmediğimi düşünüyorum."
    s "Öyle çok kusurum var ki, seni sadece yük yapacağım diye korkuyorum."
    "Çimenlerin üzerinde oturuyoruz. Hava hafif bir esintiyle çalkalanıyor."
    s 3bk "Daha kötüsü, sadece yerine başka birini koyabileceğinden korkuyorum..."
    "Başını omzuma koyuyor."
    mc "Bunu ne kadar saçma olduğunu çok iyi biliyorsun."
    mc "Eğer benimle olmak istemeseydin, neden yıllarca arkadaşım olurdun ki?"
    mc "Ve şimdi, seninle daha fazla vakit geçirmek istiyorum."
    hide sayori with wipeleft
    "Sayori kollarımdan ayrılıp, gözlerini kapayarak, yüzü gökyüzüne bakarak çimenlere uzanıyor."
    s "[player], hava nasıl?"
    mc "Hıh? Güneşli bir gün."
    "Yüzüne acı bir gülümseme yerleşiyor ve fısıldayarak, sözlerinin sadece benim için olduğunu belli ediyor."
    s "Belki de öyledir... ama ben sadece bir kara yağmur bulutunun gökyüzünü kapladığını görüyorum."
    s "Bulutların içinde bir çatlak var, ve minik bir ışık huzmesi dışarıya çıkmaya çalışıyor."
    s "Ama güneş çıkmaya çalıştığı için, yağmur bulutları korkunç bir fırtına gönderiyor."
    s "O fırtına hızla bana doğru geliyor."
    s "Buz gibi yağmur... soğuk rüzgar..."
    scene bg sky_day
    "O devam edemeden yanına uzanıp kollarımı etrafına sardım."
    "Kendimi ona yaklaştırarak sıcaklığımı hissetmesini sağlıyorum."
    s "Bu... yavaşlıyor."
    "Gözlerini açıp aynı fısıldayarak devam ediyor."
    s "Bana dokunduğunda... fırtına... yavaşladı."
    s "Ama sadece bir süreliğine."
    mc "Bu iyi bir şey."
    mc "Demek ki hala bir şansımız var."
    s "Ama yağmur düşmeye devam ediyor."
    mc "Ama güneş ve yağmur bir gökkuşağı oluşturur..."
    mc "Gözlerini kapat ve güneşe odaklan... görebiliyor musun?"
    "Sayori gözlerini kapatıp birkaç dakika sessiz kalıyor."
    s "Evet... uzaklarda soluk bir gökkuşağı gördüğümü düşünüyorum."
    s "Zor görünüyor çünkü çok uzakta... ama sanırım onu görebiliyorum."
    "Dudaklarımı onunkilerle buluşturup yüzünü okşuyorum."
    mc "Eğer çocukken yanımda olmasaydın, kafam da yağmur bulutlarıyla dolardı."
    mc "Bana devam etmem için bir neden verdin."
    mc "Eğer yağmur bulutlarını kafamdan uzaklaştırabiliyorsan, eminim ben de senin için aynısını yapabilirim."
    "Parmaklarının benimle birleştiğini hissediyorum."
    s "Sanırım bunu yapabilen tek kişi sensin."
    mc "Yarın okula dönmem gerek. Seninle yürüyerek gitmeyi sabırsızlıkla bekliyorum."
    s "Bu güzel olurdu, evet."
    s "Ama bence ilişkimize gizli kalması daha iyi olur."
    s "Başkalarının öğrenmesi düşüncesi beni çok rahatsız ediyor."
    mc "Eğer bunu istiyorsan, elimden gelenin en iyisini yaparım."
    mc "Ama seninle bir ilişki düşüncesi beni çok mutlu ediyor."
    s "Garip..."
    s "O düşünce beni de mutlu ediyor. Sadece seni mutlu ettiğim için değil, çünkü ben de bunu istiyorum."
    s "Aşkım bencil."
    mc "Bunu umursamıyorum."
    mc "Sen çok fedakar oldun. Biraz bencil olmanı kendine izin vermeni istiyorum."
    mc "Yapamıyorsan, o zaman benim için biraz bencil olmayı dene."
    s "Yani... kendime bakarak seni mutlu etmeli miyim?"
    mc "Tam olarak."
    mc "Kendime bakmazsam, nasıl hissediyorsun?"
    s "Çok endişelenirim."
    "Gözleriyle beni tarıyor."
    s "Tamam... deneyeceğim. Ama sadece seninle birlikte yaparsak."
    "Konuşmasını bitirir bitirmez, karnından kocaman bir guruldamada ses geliyor."
    "Aynı şekilde benim karnım da guruldayınca, kahvaltı yapmadığımı hatırlıyorum."
    s "Sanırım sen de bir şey yemedin, değil mi?"
    mc "Yemedim."
    s "Buna izin veremem..."
    s "O zaman bir şeyler yiyelim."
    "Başımı sallıyorum."
    mc "Beş dakika daha bekleyebilir miyiz?"
    mc "Burada çok rahatım."
    "Yüzünde parlak bir gülümseme belirdi."
    s "Tabii."
    s "Teşekkür ederim... bu anı da kıymetini bilerek yaşamak istiyorum."
    stop music fadeout 3.0
    show black with dissolve_cg
    
    "‘Beş dakika’ bir saat oldu."
    "Yemek yedikten sonra gün neredeyse bitiyor ve son bir yürüyüş yapmak için parka gitmeye karar veriyoruz."
    "Sayori'yi evine kadar takip ediyorum ve ikimizin de veda etmek istemediğini fark ediyorum."
    "Bir süre sonra saat kaç olduğunu fark ediyorum, bu yüzden ona iyi geceler öpücüğü verip ayrılıyorum."
    scene bg bedroom with dissolve_cg
    "Eve vardığımda, nihayet kız arkadaşım olduğunu fark edip sevincimi haykırıyorum."
    "Her ne kadar ilişkimiz gizli kalsın diye planlasak da."
    "Ama yatağa gitmeden önce, birden kaygılanmaya başlıyorum."
    "Gerçekten onun beklentilerini karşılayabilir miyim? Gerçekten depresyonuyla baş edebilmesine yardım edebilir miyim?"
    "Aşkın yeterli olduğunu düşünmüyorum ve aşkımı açıklamak da işe yaramayacak gibi."
    "Işıkları kapatmaya çalışırken telefonum titriyor."
    "Mesajına bakıyorum, Sayori bana bir mesaj göndermiş."
    "Mesajda ‘Bana asla yalan söylemeyeceğine söz verebilir misin?’ yazıyor."
    "Hızla, ona asla yalan söylemeyeceğimi yazıyorum."
    "Uykuya dalmak zor, saatlerce onu düşünüyorum."
    show black with close_eyes
    "Neredeyse uyuyacakken, kendime şunu söylüyorum: Onu mutlu etmek için her şeyi yaparım, hatta kendi hesabıma bile olsa."
    call sayoriRoute_dinner
    return


label sayoriRoute_dinner:

    scene bg club_day with dissolve_cg
    play music aNewDay fadein 3.0
    show monika 4b at f11
    m "Tamam, herkes! Bugünlük bu kadar!"
    "Monika'nın sesi, düşüncelerimden sıyrılmamı sağlıyor."
    "Sayori ile okul sonrası ne yapacağımızı o kadar çok düşündüm ki, Edebiyat Kulübü'nde olan her şeye odaklanamadım."
    "Diğer kızların, boş boş bir noktaya bakarken, arada Sayori'ye göz atmamı fark etmemiş olmasını umuyorum."
    "Bugün Sayori ekstra tatlı görünüyor, ama aslında her zamanki gibi."
    "Acaba bu, aşkın bir etkisi mi?"
    "Her neyse, ilişkimizin gizli tutulması düşündüğümden daha zor."
    "Dünden beri fark ettim ki, neredeyse her an aklımda sadece yeni kız arkadaşım var."
    "Yine de, ikimiz de aramızda bir şey olmuş gibi görünmemeye çalışıyoruz."
    "Yuri ve Natsuki odadan çıkarken, Sayori odanın temizliğini üstleneceğini duyuruyor."
    "Bunu söylerken bana göz kırpıyor ve ne yapmayı planladığını anlıyorum."
    "Böylece, ben de Sayori'nin doğal dikkatsizliğini bahane ederek yardımcı olmayı teklif ediyorum."
    show monika 1a at lhide
    hide monika
    "Monika bunu kabul ediyor gibi görünüyor ve odayı bize bırakıyor."
    show sayori 1c at f11
    "Kimse bizi izlemiyor olduğundan emin olduktan sonra, Sayori ve ben konuşmaya başlıyoruz."
    s "Hıh... Bitmeyecek gibi geldi."
    s "[player], bana yardım eder misin?"
    "Ona şaşkın bir şekilde bakıyorum."
    s "Yani, ‘temizliyoruz’ ya."
    mc "Cidden mi?"
    s 1r "Merak etme, bir planım var. Sadece bir paspas al."
    "İçimden bir iç çekiyorum ve söylediği gibi yapıyorum."
    "Yeri temizlerken, Sayori'nin gözlerini benden ayıramadığını fark ediyorum."
    mc "Bugün için planın var mı?"
    s 1c "Hayır, pek... Senin aklında bir şey var mı?"
    "Gerçekten, hiçbir planım yoktu. Birlikte yapabileceğimiz bir şey düşünmeye çalıştım ama gün boyunca sadece onunla vakit geçirmekle ilgili hayallere dalmışım."
    mc "Normalde ne yapmayı seversin?"
    s 5b "Vallahi... çok fazla hobim yok aslında."
    mc "Aa... doğru."
    "Depresyonu olan insanların genellikle çok enerji bulamadığını okumuştum."
    mc "Dur, biliyorum."
    mc "Ya bir alışverişe gitsen?"
    mc "Rahat olur, kimse bizi çift olarak şüphelenmez ve aslında... o mangayı almak istiyorum."
    "Gerçekten umurunda değil, ama onunla mağazaya gitmek ve oradaki adamlara kız arkadaşım olduğunu göstermek hoş olurdu."
    "Aslında, Sayori'nin bunu yalnızca kendisi için yapmamı düşünmesini sağlamak için söylediğim bir şey."
    s 1q "Ehehe~"
    s 1c "Bu çok hoş olur!"
    s "Tamam o zaman, temizlik bitince gidelim."
    "Başımda soğuk terler oluşuyor."
    mc "Dur, hala temizlik mi yapıyoruz?"
    mc "Monika bu odayı ne kadar temiz tutmamızı istiyor?"
    s "Bilmiyorum ki..."
    s 2a "Ama iyi bir iş çıkarırsak mutlu olur diye düşündüm."
    "İçimden bir iç çekiyorum ve ilişki olsa da olmasa da bazı şeylerin asla değişmeyeceğini fark ediyorum."
    s "Ama... "
    s 1c "Bazen sıradan şeyler bile, birlikte yapınca eğlenceli oluyor, değil mi?"
    "Pes etmiş bir şekilde başımı sallıyor ve paspası alıyorum."
    s "Aa, [player]?"
    "Yanıt verecekken, elimdeki paspası unutuveriyorum ve hareketim nedeniyle çubuğu kafamın arkasına çarpıyorum."
    mc "Evet?"
    "Sahte bir gülümseme takınıp kafamdaki ağrıyı gizlemeye çalışıyorum."
    s 3l "Acaba... yani..."
    s 3k "Birlikte başka bir anime izlesek nasıl olur?"
    "Bir süre kafamda belirsiz bir şekilde blinkliyorum."
    mc "Genelde onları sevmediğini düşünmüştüm."
    s 5b "Açıkçası, hala animeye pek ilgim yok, ama seninle izlediğimiz o animesi hoşuma gitmişti..."
    s "Ama bunlar senin hoşlandığın şeyler, ve bence seni daha iyi anlayabilmem için hobilerinle ilgilenmem gerek."
    s "H-hani... biraz daha fazla hobim olmalı."
    mc "Benimle izlemek istemen beni mutlu ediyor."
    mc "Belki akşam yemeği yerken izleriz."
    s 4r "Oooh! Harika bir fikir!"
    "Sayori durup bir kez daha bana bakıyor."
    s 5a "Ee, [player]... biraz utandırıcı bir şey sorabilir miyim?"
    mc "Sana aramızda sır olmayacak demiştim, değil mi? Sor, lütfen!"
    s 1b "Teşekkürler."
    s "Yani... işte sorum."
    s 1c "Hayalindeki romantik akşam yemeği nasıl olurdu?"
    "Açıkça beni test etmeye çalıştığı belli."

    menu:
        "Nasıl cevap vermeliyim?"
        "Hiçbir şey fazla gösterişli değil, sıradan bir akşam yemeği.":
            $ sayori_informal = True
            s 4c "Vay, ben de tam olarak aynı şekilde düşünüyorum!"
            mc "Gerçekten mi?"
            s 1c "Evet. Lüks restoranlar ve formaliteler bana gerçekten itici geliyor."
            s "Sanki her şey... zorla yapılmış gibi hissediyorum."
            mc "Evet, seni lüks bir restorana girdiğini hayal etmek hiç kolay değil."
            s 1r "Gerçekten mi? O kadar mı berbatım?"
            mc "Hayır, asla."
            mc "Sen sadece içtensin."
            s 1k "Açıkçası, seni şık bir takım elbise içinde ve klas bir restorana gitmiş görmem... ehehe~"
            mc "Haha... evet, kesinlikle tam bir aptal gibi görünürdüm."
            s 1c "Gerçekten de öyle olurdu."
            s "Ama yine de yakışıklı olurdun."
            show sayori 1c at h11
            "Biraz sevinçle dans etmeye başlıyor ve neredeyse bir sandalyeye takılıyor."
            "Onu düşmekten kurtarmak için omuzlarından tutuyorum."
            mc "Daha dikkatli olmalısın."
            show sayori 1c at f11
            s "Aman Tanrım... üzgünüm. Sanırım biraz heyecanlandım, değil mi?"
            s "Sadece... seni şık bir takım elbise içinde düşünmek kalbimi çarptırıyor."
            mc "Ah..."
            "Kendimi çekici bir insan olarak hiç düşünmemiştim."
            "Bunun gibi bir şey duymak beni biraz huzursuz ediyor."
            mc "Aslında, elbiseyle çok çekici olurdun."
            s 2y "Gerçekten mi?"
            s "Çekici mi?"
            s 1l "Hmm... belki alışverişe gittiğimizde elbise bakarım o zaman."
            mc "Lütfen yapma. Gerçekten çok pahalıdırlar..."
            "Beni nazikçe öpüyor."
            s 1a "Buna aldırmam."
            s 1c "Seni mutlu edecekse, neden yapmayayım ki?"
            mc "... Çünkü o zaman ben de şık bir takım elbise almak zorunda kalırım."
            s "Neden?"
            mc "Çünkü seninle aynı seviyeye gelmek adil olur."
            "Boynuma kollarını sarıyor."
            s "Tamam o zaman, tamam, yapmayacağım."
            mc "Güzel."
            mc "Zaten her şeyde yakışıklısın."
            s 2e "Ben... Bilmiyorum..."
            s 1c "Ama teşekkür ederim."
            s "Bunu senden duymak gerçekten özgüvenimi artırıyor."
            mc "Tekrar duymak istersen, bana sadece söyle."
            s "Hmm... belki söylerim."
            "Derin bir nefes alıyor."
            s "Bana şimdi bunu söylemen, sana itiraf etmek gerçekten doğru bir karardı diye düşündürüyor."
            s "Beni şu an o kadar mutlu ettin ki."
            mc "Şimdi, son birkaç yıldır senin de beni nasıl hissettirdiğini biliyorsun."

        "Romantik bir akşam yemeği – mum ışıklarıyla aydınlanmış.":
            $ sayori_informal = False
            s 1c "Hmm... Bunu söylediğine biraz şaşırdım."
            mc "Bana o kadar mı saygısız görünüyorum?"
            s 4n "Hayır, asla!"
            s 1c "Sadece... sanki senin hoşlanacağın bir şey gibi gelmiyor. O kadar."
            mc "Aslında, lüks restoranlara gitmekten pek hoşlanmıyorum... ortamı biraz rahatsız edici geliyor."
            s "Gerçekten mi?"
            "Başımı sallıyorum."
            s "Ben de, tamamen dürüst olursam."
            s "Ama neden o zaman resmi, romantik bir akşam yemeği istersin?"
            mc "Lütfen gülme, tamam mı?"
            s 2a "Söz veriyorum."
            mc "Hep bir hayalim vardı, gerçekten sevdiğim bir kız arkadaşım olduğunda, ilk randevumuzun mükemmel olmasını isterdim – onu şık bir yere götürür, romantik bir akşam yemeği yerim... ve sonra..."
            s 1c "Sonra ne?"
            mc "Ona ne kadar sevdiğimi söylerim, öperim... ve sonra o akşamı onun için mükemmel hale getirmek için her şeyi yaparım."
            "Bunu söylerken yüzlerimiz birbirine yaklaşıyor."
            s 1a "Vay..."
            "Elden kovayı düşürüp, yüzümü iki eline alarak beni öpüyor."
            s "Demek gizliden bir romantiksin... kim bilebilirdi ki?"
            "Başımı sallıyorum ve umarım ona, yıllar önce izlediğim bir anime fikrini çaldığımı asla öğrenmez."
            s 1c "O tür bir huzurlu, mükemmel bir tarihe sahip olmayı çok isterim..."
            mc "Bunu bir gün yapabiliriz."
            mc "Ama sanırım sen okul kıyafetinle bu kadar güzelsen, seni elbiseyle görmek benim zavallı kalbimi taşıyamaz."
            s 4n "Sen... beni güzel mi buluyorsun?"
            "Başımı sallıyorum."
            s 1e "Vay... Hiç kimse bana bunu söylemedi..."
            s "Seni her zaman gördüğüm en çekici insan olarak düşündüm."
            s "İlişkimizin nereye gittiği konusunda endişelenebilirim ama seninle ilişkide olmanın anılarını her zaman kıymetli tutacağım."
            mc "Dürüst olmak gerekirse... dün gece uyumakta zorlandım çünkü seni o kadar çok düşündüm."
            s 1c "Ben de... seni düşünmekten duramadım."

    
    
    
    
    "Okul zili çalar çalar, tutkulu bir öpücük paylaşıyoruz."
    "Zamanı kontrol ediyorum ve acele etmemiz gerektiğini fark ediyorum, yoksa hala okulda olan öğrenciler neden burada olduklarına dair şüphelenmeye başlayacak."
    stop music fadeout 3.0
    "Hızla odayı topluyoruz ve okuldan çıkarken tam okul kapıları kapanıyor."

    scene bg sayori_bedroom with wipeleft_scene
    play music SayTheme fadein 3.0
    "Birkaç saat sonra Sayori’nin evine dönüyoruz, ben de inanılmaz ağır torbaları taşıyorum."
    "Torbaları yere bırakıyorum, derin bir iç çekerek."
    show sayori 5b at f11
    s "Tekrar özür dilerim. Ben... hıh, biraz fazla heyecanlandım."
    mc "Evet... bunu söylemek kesinlikle doğru olur..."
    mc "Neden kızlar hep bu kadar çok para harcıyor kıyafetlere?"
    s 1c "Bilmiyorum. Peki ya erkekler neden modaya hiç aldırmaz?"
    mc "Bilmiyorum – oh, sanırım bunu bütün gece konuşabiliriz, değil mi?"
    show sayori 1r at f11
    "Birlikte kahkahalarımızı paylaşıyoruz."
    s 1c "Haklısın. O zaman kavga etmeden, hemen tekrar mutlu olduğumuz noktaya gelelim."
    s "Beni alışverişe çıkardığın için teşekkür ederim. Çok eğlendim!"
    mc "Evet, gerçekten eğlendiğini görüyordum."
    "Biraz fazla eğlendiğini eklemek isterim."
    s "Bu akşam yemeği benden."
    mc "Gerçekten mi? Sadece geçen sefer evin neredeyse yanmıyordu, dikkat et!"
    s 4n "H-hayır! Artık çocuk değilim!"
    mc "Ne yapıyorsun?"
    "Yüzünde ufak bir şeytani gülümseme beliriyor."
    s 1a "Sürpriz olacak."
    s "Bu arada, sen o oyun mağazasına gittiğinde, ben de biraz anime kiraladım. Romantik bir akşam için en iyisini seçebilir misin?"
    mc "Tabii! Bunu bana bırak."
    s 1c "Teşekkür ederim! Senin üzerine güvenebileceğimi biliyordum."
    s "Oh... ve bana bir iyilik yapabilir misin? Ben geri gelene kadar odadan çıkma, olur mu?"
    mc "Neden?"
    s 4s "Bir sürpriz... eheh~"
    show sayori 4s at lhide
    hide sayori
    "Son bir kez bana gülümsüyor, sonra aşağıya doğru, insan şeklinde bir kasırga gibi koşuyor."
    "Bir dakikadan daha kısa bir süre sonra, yüksek bir sesle bir şeyler düşüp metalin çarpması geliyor."
    s "İyiyim!"
    "...Şimdi düşündüğümde, o sakarlık, onu sevdiğim şeylerden biri."
    "Ve... beni gerçekten ciddiye alması."
    "Bana güveniyor. Beni bir şaka gibi görmüyor."
    "Bu, gerçekten parlamam için fırsatım."
    "Torbayı açıyorum ve birçok film olduğunu görüyorum. Hepsi çok romantik görünüyor."
    "Biraz düşündükten sonra telefonumu çıkarıp onları internette kontrol ediyorum ve kararımı veriyorum."
    "Sonunda sıcak kalp dolu bir romantik komedi seçiyorum."
    "Aşağıdan Sayori’nin çeyrek nota kaymış bir şekilde şarkı söylediğini duyuyorum, ve yüzümde bir gülümseme beliriyor."
    "Bu akşamı, bizim için unutulmaz bir akşam yapmak için elimden gelenin en iyisini yapacağım."
    "...Onun için elimden gelenin en iyisini yapmak zorundayım."
    "...Birkaç saat geçiyor ve Sayori’den ne ses var, ne de iz."
    "Onun iyi olduğundan eminim ve odadan çıkmayacağıma söz vermiştim ama yine de onu merak ediyorum."
    "Telefonumu çıkarıp onu aramayı düşündüğüm anda, ön kapının açıldığını ve kapandığını duyuyorum."
    show sayori 1a at l11
    "Bir süre sonra, Sayori odaya büyük bir tepsi taşıyarak kapıyı açıyor."

    
    if(sayori_informal is True):
        "Sayori, tepsiyi kaplayan büyük torbayı kaldırarak taze sushiyle dolu iki büyük tabak ortaya çıkarıyor."
        "Sadece görünüşü ve kokusu bile ağzımın sulanmasına yetiyor."
        mc "Sayori, bunu kendin mi yaptın?"
        show sayori 1a at f11
        "Başını sallayıp gururla gülümsüyor."
        s 5b "Yani... ben, hıh... akşam yemeği yapmaya çalıştım ama pek istediğim gibi gitmedi, o yüzden en yakın sushi restoranına gidip paket siparişi aldım."
        s 2c "Biliyorum, senin sevdiğin her farklı tadı seçtim."
        mc "Vay... bu harika."
        mc "Gerçekten çok düşüncelisin, kelimelerim tükendi..."
        "Tepsiyi masasına koyuyor."
        s 1q "Bazen hiçbir şey söylemene gerek yok... yüz ifaden her şeyi anlatıyor."
        "Ona bir öpücük veriyorum ve en düşünceli kız arkadaşım olduğunu söylüyorum."
        "Bu tepki onu kızartıp utanarak gülümsedi."
        s 1b "Beğenmene çok sevindim..."
        s "Her zaman seni güldürmek için elimden geleni yapacağım, [player]..."
        s "Tıpkı birlikteyken her gün beni güldürdüğün gibi."
        mc "Sadece seninle birlikte olduğumda mutlu oluyorum..."
        mc "Ve bunu her gün kanıtlayacağım."
        s "Ne kadar tatlısın... Bunu hak etmek için ne yaptım, bilmiyorum."
        "Tekrar öpüyorum."
        mc "Bilmiyorum... ama aklıma gelen ilk şey, doğduğun andan itibaren bunu hak ettiğindir."
        "O gülüyor ve öpücüğü geri veriyor."
        "Onun dudaklarının ne kadar yumuşak ve nazik olduğunu asla sıkılmadan hissedeceğimi düşünüyorum."
        s 1c "Yemekler taze olduğu için yemeye başlamalıyız, ve hangi animeyi seçtiğini görmek için sabırsızlanıyorum!"
        mc "Seçerken seni düşündüm."
        "Sayori’nin ellerini birlikte ovuştururkenki mutlu yüzünü görmek her şeye değiyor."
        "Anime oynamaya başlarken, kendisini bana yasladığını hissediyorum."
    
    else:
    
        s 1c "Bir dakika gözlerini kapatır mısın, tamam mı?"
        mc "Tamam."
        
        show black with close_eyes
        "Gözlerimi kapatıyorum ve onun, kendine şarkı mırıldanırken bir şeyler açıp kapadığını, çekmecelerini karıştırdığını duyuyorum."
        "Biftek kokusu burun deliklerimi sarıyor ve karnım guruldamaya başlıyor."
        s "Tamam, şimdi tekrar açabilirsin!"
        
        hide black with open_eyes
        "Gözlerimi açıyorum ve Sayori, odaya gururla girmiş, etrafında yanıp sönen mumlar var."
        "Masada şık bir yemek duruyor."
        "Görünüşü mü yoksa kokusu mu, bilemiyorum, ama ağzım sulanıyor."
        "Sayori’ye bakıyorum, yüzünde zafer dolu bir ifade var."
        s 1h "Peki, ne düşünüyorsun?"
        mc "Vay."
        "Tam anlamıyla şaşkınım – Sayori’nin böyle bir şey yapmasını beklemiyordum."
        s 1r "Beğenmene çok sevindim!"
        s 5a "Kendim bir şık akşam yemeği yapmayı denedim... ama işler beklediğim gibi gitmedi."
        s "O yüzden o çok pahalı restorana gidip bunu aldım."
        "Beni sıkıca kucaklıyor."
        s 1c "Şık, romantik akşam yemeklerini sevdiğini söylemiştin, değil mi?"
        mc "E-evet..."
        s 1a "Bak, sana her şeyin en iyisini yapmak için elimden geleni yapacağımı söylemiştim."
        mc "Sayori..."
        mc "Seninle burada olduğumda mutlu oluyorum."
        s 1c "Bunu duyduğuma sevindim."
        "Onu kendime yaslarken karnının guruldadığını hissediyorum."
        mc "O zaman hadi yiyelim!"
        s "Sanırım bu, çift olarak ilk akşam yemeğimiz, değil mi?"
        s 4r "Çok heyecanlıyım!"
        s "Tıpkı hangi animeyi seçtiğini görmek için heyecanlı olduğum gibi!"
        "Başımı kaşıyıp utanarak gülümsüyorum."
        mc "Seçerken seni düşündüm."
        "Sayori’nin ellerini birlikte ovuştururkenki mutlu yüzünü görmek her şeye değiyor."
        "Anime oynamaya başlarken, kendisini bana yasladığını hissediyorum."

    
    hide sayori with dissolve
    "Sanırım doğru seçimi yaptım."
    "Sayori, ilk randevumuz için seçtiğim filmi gerçekten sevdi."
    "Film, zaman içinde yolculuk yapan ve suçları çözen, soğukkanlı ve güçlü bir kadın dedektifin hikayesi."
    "Ancak, film ortalarına doğru, peşinde olduğu suçluya aşık olmaya başlıyor ve suçlu da ona karşı hisler besliyor."
    show sayori 4n at f11
    s "Vay... demek buna yasak aşk diyorlar, ha?"
    mc "Sanırım? Gerçekten emin değilim."
    s 2c "Birbirlerine ait olan iki insan... ama bir dizi sebepten dolayı bir araya gelemiyorlar."
    s 1a "Hem acı tatlı hem de romantik bir durum! Tam anlamıyla!"
    s "Yani... bak ona, nasıl ona bakıyor, o da ona öyle bakıyor!"
    s "Kesinlikle birbirlerine aitler, ama o gururlu ve inatçı olduğu için bunu kabul etmiyor, o ise aşık olduğunu anlamayacak kadar olgunlaşmamış."
    s 1r "Bir şekilde, o kişilik özellikleri onları birlikte çok daha iyi yapıyor."
    "O, kolumu sarıp bana bakıyor."
    s 1h "Hey, [player]... sen ve ben, o ikisi gibi mükemmel bir takım olabilir miyiz, sence?"
    "Gözlerimi kırpıyorum."
    mc "Yani, hı... zaman içinde suç mu çözelim?"
    s 1a "Hayır, aptal! "
    s 1c "Bunu kastetmedim... bir çift olarak. Aslında, onların dinamiğinden biraz kıskanıyorum."
    mc "Her şey mümkün, yeterince istersen."
    s 1b "O zaman... seninle sonsuza kadar olmak istiyorum."
    "Gülümsüyorum."
    mc "Bunu ben de diliyorum... tüm kalbimle."
    hide sayori with dissolve
    "Yemek yerken filmi izlemeye devam ediyoruz."
    "Filmin sonunda, dedektif ve suçlu, evli bir çift gibi davranarak bir kaleyi balo salonundan geçip güvenlikten gizlice geçmek zorunda kalıyorlar."
    show sayori 3c at h11
    "Bir anda Sayori ayağa kalkıp elimi tutuyor."
    show sayori 3c at f11
    s "Hadi gidelim, [player]!"
    mc "Benimle dans etmek mi istiyorsun?"
    "O başını sallıyor."
    s 3r "Evet. Hadi, eğlenceli olacak!"
    mc "Tamam... seninle olursa o kadar utanç verici hissetmem."
    "O, kollarını omuzlarıma sararken, yanaklarımın ısındığını hissediyorum."
    "Yutkunuyorum ve kollarımı beline sarıyorum."
    show sayori 2q at f11
    "Sadece dans etmeye başladığımızda, ekrandaki karakterlerin hareketlerini taklit etmeye çalışırken kendimi rahat hissediyorum."
    show sayori 2q at f21
    "İşte o zaman, bundan ne kadar keyif aldığımı fark ediyorum – çünkü bu, sadece ikimiz arasında kişisel bir şey."
    show sayori 2q at f22
    "Onu bu kadar mutlu görmek başka bir şey... ama onunla böyle yakın olmak, onu tutmak ve onunla dans etmek..."
    show sayori 2a at f11
    "...Gerçekten bu kıza bağlandığımı fark ediyorum."
    "Onun gökyüzü mavisi gözlerine bakarken, bana da aşık olduğunu fark ediyorum."
    "Onun bakışlarında gerçek bir sevgi hissediyorum."
    "... O zaman, bu anın bitmesini istemediğimi fark ediyorum."
    "Sahne bittiğinde, Sayori'yi bırakmıyorum."
    "Onun da beni bırakmaya niyeti olmadığını fark ediyorum."
    "Kısa süre sonra, filmi ve yemeği tamamen unutuyoruz."
    show sayori 2b at f11
    "Sadece duruyoruz... birbirimizi tutuyoruz ve gözlerimize bakıyoruz."
    "Hiçbirimiz, bu anın huzurunu bozma korkusuyla nefes almak dahi istemiyoruz."
    
    show black with dissolve_cg
    "Geriye kalan geceyi, diğer iki filmi izleyerek, birbirimize sarılarak ve öpüşerek geçiriyoruz."
    "Gece yarısından çok geç bir saatte ayrılıyorum."
    "Eve doğru giderken, vücudum hafif gibi hissediyorum ve mutlu bir şekilde zıplayarak yürüyorum."
    "... Aklımda sadece, giderek daha fazla sevdiğim kız var."
    stop music fadeout 3.0
    
    
    scene bg bedroom_night
    "O gece başka bir kabus görüyorum."
    show black with dissolve_cg
    "Rüyamda, Sayori’yi başka bir adamla öpüşürken görüyorum – adamın yüzünü görmüyorum, ama Sayori onunla benden daha mutlu görünüyor."
    "Yaklaştığımda, adamın mükemmel biri olduğunu fark ediyorum – uzun, kaslı ve bana döndüğünde inanılmaz derecede yakışıklı."
    "Sonra tekrar ona dönüp, öpüşmeye devam ediyorlar."
    "Sayori bana hiç dikkat etmiyor, ta ki adını bağırana kadar."
    "Rüyada onu sorguladığımda, gülüyor ve bana, sadece depresyonunu atlattığı için geçici bir dönemeç olduğumu söylüyor."
    "Artık iyileştiği için bana ihtiyacı kalmadığını ve bir kaybedenle kalmasının bir anlamı olmadığını söylüyor."
    "Rüya adamı sonra dönüp bana çok sert bir şekilde yumruk atıyor."
    "Çığlık atarak uyanıyorum."
    scene bg bedroom with dissolve_cg
    
    "Uyanıp alarm saatine bakıyorum."
    "Henüz çok erken – sanırım tekrar yatmalıyım."
    "Yine de uyumaya çalışırken, göğsümde bir ağırlık hissediyorum ve geri uyuyamıyorum."
    "Rüyanın sahnesi kafamda, tekrar tekrar dönüp duruyor."
    "Sayori böyle bir şey yapmazdı..."
    "...Değil mi?"
    "Beni bir başkasıyla bırakmazdı... değil mi?"
    "Kafamı sallıyorum ve kendime sadece saçmaladığımı söylüyorum."
    "Sayori, yeterince iyi olmadığım için beni terk edecek biri değil."
    "... değil mi?"
    "Yarım saat bekliyorum, sonra tekrar uyumaya çalışmanın kayıp bir sebep olduğunu düşünüyorum."
    "Telefonumu çıkarıp, Sayori’ye okula gitmeden önce benimle yürüyüşe çıkıp çıkamayacağını soruyorum."
    "Yanıtı hemen geliyor."
    "Hızla giyinip, hızlıca bir kahvaltı yaparak dışarı çıkıp onu bulmaya koşuyorum."

    
    scene bg house with dissolve_cg
    show sayori 1c at f11
    s "Günaydın, [player]!"
    play music aNewDay fadein 3.0
    "Onun parlak gülümsemesini gördüğüm an, yüzümde otomatik olarak bir gülümseme belirdi."
    "Keşke öpüşebilseydik, ama bu, ilişkimizin olduğunu izleyen biri için fazla belli ederdi."
    scene bg residential_day
    "Neyse ki, okula doğru yola çıkıyoruz."
    "Bütün yol boyunca, el ele tutuşuyoruz."
    "Gerçekten de, bunu sevgi dolu bir jest olarak mı yapıyorum, yoksa soğuk sabahı atlatabilmek için mi elini tutuyorum, bilmiyorum."
    show sayori 4a at f11
    s 4a "Nasıl uyudun?"
    "Utangaç bir şekilde gülümsüyorum ve ona gerçeği söyleyemeyeceğimi fark ediyorum."
    mc "Sanırım iyiydi, ama fazla uykusuz kaldım."
    s "Evet, normalden erken kalktığını fark ettim."
    mc "Kendini söyleme, ben seni geç uyandıracağım diye endişelendim."
    "Onun yanakları kızarır ve fısıldayarak devam eder."
    s 1c "Aslında... son zamanlarda daha erken uyanıyorum."
    s "O kadar çok düşünce ve his var ki, onları içinde tutmak zor, ve aynı zamanda onlardan yenilenmiş hissediyorum."
    "Gülümsüyorum ama hemen ardından rüyamda söylediği şeyi hatırlıyorum."
    mc "Ah, evet... Aynı şey benim için de geçerli."
    s 2b "Sana mutlu ettiğimi bilmek beni çok mutlu ediyor..."
    s "Hep hayalini kurduğum ilişki, dünyadaki en mutlu adam yapabileceğim biri olmak."
    mc "Ne garip, ben de hep aynı şeyi diledim."
    "Bir an duraklarım ve utanırım."
    mc "Yani... kız arkadaşımı mutlu etmek istiyorum!"
    s 1d "Beni, belki de hak ettiğinden çok daha mutlu ediyorsun..."
    mc "Sen bundan çok daha iyisini hak ediyorsun..."
    mc "Ama elimden gelenin en iyisini yapmaya çalışıyorum."
    s 4r "Aynı şekilde, sana da!"

    stop music fadeout 3.0
    scene bg class_day with dissolve_cg
    "Bugün derslerde, alışık olduğumdan çok daha zor odaklanıyorum."
    "Normalde pek dikkat etmem ama bugün öğretmenin sesi kulağımın bir tarafından girip diğerinden çıkıyor gibi."
    "Ne kadar uğraşsam da, rüyam aklımdan çıkmıyor."
    "Sınıftaki diğer çocuklara bakıyorum – her biri bir şekilde benden daha iyi."
    "Birçoğu her açıdan benden daha zeki ve sınavlarımıza her zaman en üst sırada yerleşiyorlar."
    "Ve ardından, benden çok daha yakışıklı olan, yıllık okul etkinliklerinde bir sürü kızın ilgisini çeken çocuklar var."
    "Daha da fazlası, futbol kulübü başkan yardımcısı gibi insanlar var, ki o bile en sert öğretmenleri güldürebiliyor. Ayrıca kızları, ben animeyi ne kadar iyi biliyorsam, o kadar iyi tanıyor."
    "...Hepsi Sayori için, eğer isterlerse, benden çok daha uygun olabilir."
    "Bir şekilde, her erkekle göz göze geldiğimde, tehdit altında hissediyorum."
    "Her bakışımda Sayori’yi başka bir çocukla, benim yerime, ilişkide hayal ediyorum."
    "Başımı sallayarak, kendime onun beni seçtiğini hatırlatıyorum – beni seviyor ve sadece beni..."
    "Diğer çocuklarla şansı varken, hala beni seçti..."
    "Ama merak ediyorum..."
    "Beni seçti çünkü en düşük noktayım ve depresyonu yüzünden daha iyisini hedeflemeye cesaret etmedi mi, yoksa gerçekten mi beni seviyor?"
    "Gerçekten Sayori gibi bir kızı, benim gibi bir çocuk ilgisini tutabilir mi?"
    "O kadar düşünceler içinde kaybolmuşum ki, öğle arası başladığını bile fark etmiyorum."
    "Sadece yüksek bir gürültüyle, düşüncelerimden sıyrılıp sesin geldiği yöne döndüm."
    scene bg club_day with wipeleft_scene
    show sayori 5b at t22
    "Sırtımdan terler süzülmeye başlıyor, çünkü Sayori’yi görüyorum. O, kalçasına oturmuş, elindeki sandviç yüzünden bir kız öğrenciye boyalı bir suratla bakıyor."
    $ o_name = "F. Öğrenci"
    o "Ah, nereye bakıyorsun, salak!"
    s "Özür dilerim. Kaydım."
    o "Eww, şimdi somonlu sandviçim saçımda!"
    o "Aman Tanrım – insan birinin önünde durduğunu görüp buna nasıl dikkat etmez?"
    s 1w "Özür dilerim, kastetmedim-"
    o "Vah, güzel uzun saçlarla ilgilenmeyi bilmediğini tahmin ediyorum, değil mi?"
    o "Sana söyleyeyim – saçımı güzelleştirmem saatlerimi aldı, ama şimdi mahvettin, salak!"
    o "Ama sanırım şaşırmamalıyım... Benden kıskanıyorsun, değil mi?"
    s 4n "Kıskanmak mı?"
    s "Yemin ederim, kazara oldu..."
    s "Lütfen affet beni."
    o "Sus! Saçımın asla benimki kadar güzel olamayacağını kıskandığını biliyorum, bu yüzden saçlarını kestin, değil mi?"
    o "Saçımda o pisliği bulundurman, senin kadar berbat değil!" 
    "Sayori’nin gözleri büyür."
    "Benim de gözlerim büyür, çünkü bu ukala öğrencinin onu tokatlayacak olduğunu fark ediyorum."
    hide sayori with wipeleft

    show white 
    play sound slap 
    pause(0.5)
    hide white
    "Hızla ilerliyorum ve palmiyenin Sayori'nin yanağına vurmasına engel olmak için araya giriyorum, tüm gücünü hissediyorum."
    o "[player], buna karışma!!"
    "Kalkıyorum. Yanağım, sanki bir arı sokmuş gibi hissediyor."
    "Yüzümde çok öfkeli bir ifadeyle ona bakıyorum."
    mc "Yapma."
    "Sesimin ne kadar düşman bir tonda çıktığını fark etmiyorum."
    mc "Sayori hiçbir şey yapmadı--bu bir kazaydı."
    mc "Onu küçümsemek ve ona zarar vermek için hiçbir sebep yok!"
    "Aniden gösterdiğim düşmanlığa rağmen, o kendini beğenmiş öğrenci pes etmiyor."
    o "Yemin ederim, bunu kasıtlı yaptı!"
    "Yine elini kaldırıp Sayori'yi tekrar tokatlayacak, ama bu sefer onun bileğini yakalayıp sıkıca tutuyorum, elini indirene kadar."
    mc "Hayır, yapmadı."
    mc "Onu yıllardır tanıyorum, o sadece sakar."
    mc "Şimdi, öğretmenlere gelip sana fiziksel şiddet uyguladığını ve onu küçümsemeni söyleyebilirim ya da seni salıverebilirim."
    mc "Eğer şimdi ona özür dilersen, sanki hiçbir şey olmamış gibi davranırım."
    o "Hmph. Siz ikinizin de neyi var?"
    o "Ne kadar kaybeden bir çiftsiniz..."
    "Sayori'ye küçümseyici bir bakış atıp, başını dik tutarak odadan çıkıyor."
    "Sınıf arkadaşlarımın fısıldadığını duyuyorum ve bu, öfkemin ilk kez bu kadar kontrolden çıktığını fark ediyorum."
    "Dönüp onlara keskin bir bakış atıyorum."
    mc "Gösteri bitti--burada görülecek bir şey yok!"
    "Çantamı alıp, hala yerde oturan Sayori'ye bakıyorum, yüzünde şaşkın bir ifade var."
    mc "Hadi gidelim, Sayori."
    s "O-okay."
    scene bg rooftop with dissolve_cg

    "Okulun çatısına çıkıyoruz, burada oturuyoruz ve Sayori, gözlerinde yaşlarla bana bakıyor."
    show sayori 4w at f11
    s "Çok üzgünüm... O kızı görmedim."
    s "Sadece seni şaşırtmak ve seninle öğle yemeği yemek istedim..."
    s 2l "Ama şimdi senin yüzünden yaralandın."
    s "Ben bir başarısızım..."
    mc "Sorun değil... tokat o kadar da canım acıtmadı."
    mc "Ve, hani... hâlâ birlikte yemek yiyebiliriz."
    s "Ama... öğle yemeğim şu anda o kızın saçında."
    s "Yüzündeki ifadeyi gördün mü?"
    s 1f "Ne kadar nefret ediyordum, hissedebiliyordum..."
    mc "Endişelenme--o kız, senin umursaman gereken biri değil."
    "Ellerimi uzatıp, nazikçe saçlarını okşuyorum."
    mc "Önemli olan, senin güvende olman."
    s 4g "Peki ya sen?"
    mc "Sana söyledim--o kızı umursamıyorum."
    s "Ama o gerçekten çok güzeldi..."
    s 1t "O uzun saçlar... o güçlü gözler..."
    mc "Evet, ve tamamen boş bir kafa ve sadece kendini umursuyor."
    mc "O kadar çok erkek arkadaşı oldu ki saymaya bile dayanamam, ve ne zaman onlardan istediğini alırsa, onları bir kenara atıyor."
    s 3h "Bu korkunç... İnsanlar neden böyle yapar ki?"
    mc "Bilmiyorum. Ama sana şunu söyleyebilirim ki, o senin tam zıttın."
    mc "Belki de seni bu kadar çekici bulmamın sebeplerinden biri bu."
    s 4n "G-Gerçekten mi?"
    "Öğle yemeğimi açıp, yemeği ikiye ayırıp büyük olan kısmını Sayori'ye veriyorum."
    mc "Yemek yeyelim – bu günü atlatmak için sana enerji gerek."
    "Baş başa sessizce yemek yerken, Sayori’nin zaman zaman bana bakıp yanağımdaki kırmızı izlere göz attığını hissediyorum."
    s 1q "Burada seninle oturmak ve yemek yemek çok güzel."
    s "Sadece sen ve ben..."
    mc "Başka bir şekilde olmasını istemezdim."
    mc "Seninle vakit geçirmek, günümün en güzel anı."
    s "Benim için de aynı."
    s 2b "Hayır, daha da önemlisi--seninle olduğumda, o yağmur bulutlarının ne kadar uzaklaştığını hissediyorum..."
    s "Birini sevmenin ve sevildiğini bilmenin nasıl bir şey olduğunu hiç düşünmemiştim."
    s 1h "Sana zarar verdiğim için o kadar üzgünüm... Ama senin benim için savunduğun zaman mutlu oldum. Oysa senin buna gerek yoktu."
    mc "Ne tür bir berbat erkek arkadaş olurum ki seni böyle zorbalardan korumasam?"
    s "Sanki benim için çok şey yapıyorsun... Ben sana karşılık veremiyorum..."
    "Sessizleşip, hayalime dönüyorum."
    mc "Sadece benden dolayı mı ilişki içindesin?"
    s 4m "Ne? Hayır, tabii ki değil!"
    s 2g "Seninle ilişki içindeyim çünkü seni seviyorum."
    s "Bu duygularım uzun zamandır var..."
    mc "Neden?"
    mc "Daha pek çok başka--daha iyi--erkek var dışarıda."
    mc "Bunu, onların senin seviyende olmadığını düşündüğün için mi?"
    s 1g "Hayır, öyle bir şey yok."
    s "Kesinlikle öyle değil."
    s 1a "Çünkü... her zaman bana çok naziksin."
    s "Her zaman benim için savaştın ve hep kendimi çok değerli hissettirdin."
    s 2b "Her şeyimi sana güvenebileceğimi hissediyorum, [player]."
    mc "Her şeyini mi?"
    s "Beni nasıl hissettirdiğin... gerçekten benzersiz."
    mc "Sayori..."
    mc "Ben de seni aynı şekilde hissediyorum."
    "Birbirimize sarılıyoruz, birlikte vakit geçirdiğimiz için mutlu bir şekilde okul zili tekrar çalana kadar."
    s 1f "Derse dönmem gerekiyor..."
    mc "Aynı. Keşke dönmek zorunda olmasam."
    s "Keşke ders kaçamağı yapabilsem... ama yakında bir sınavımız var."
    mc "Evet, galiba--"
    mc "Aman tanrım."
    s 1n "Ne oldu?"
    mc "Sınavı tamamen unuttum!"
    s 1f "Yağmur bulutları yüzünden çalışmaya bile vakit bulamadım..."
    s "Her zaman sinirlerim bozulduğunda, sonrasında o kadar yorgun oluyorum ki!"
    mc "Bu durumda..."
    s "...İkimiz de başarısız olup bir yıl geride kalacağız."
    mc "Bu bir sorun... ama belki..."
    s 1c "Bir fikrin mi var?"
    mc "Beni duyduğunda, depresyonunun zayıfladığını hissediyorsun, değil mi?"
    s "Evet."
    mc "Ya sınav için birlikte çalışırsak?"
    "Yüzü aydınlanıyor."
    s 4r "Bunu çok isterim!"
    s "Ben... seni sormak istedim, ama reddedileceğinden korktum."
    mc "Ve depresyonun seni etkilerse, çalışmayı senin evinde yapabiliriz--böylece geri gelirse, evde olursun ve ihtiyacın olduğunda dinlenebilirsin."
    s "Harika bir fikir, teşekkür ederim!"

    
    show black with dissolve_cg
    "Gün boyunca ne kadar uğraşsam da, bir türlü odaklanamıyorum."
    "Sonsuzmuş gibi hisseden bir süre sonra, son ders de bitiyor ve Sayori ile buluşmak için dışarıya çıkıyorum."
     
    scene bg sayori_bedroom with dissolve_cg
    show sayori 1c at f11
    play music SayTheme fadein 3.0
    s "Puhh... bana mı öyle geliyor, yoksa dersler bugün daha uzun mu geçti?"
    "Sayori, sırt çantasını yatağa fırlatıp derin bir nefes alırken, ben de hemen onu takip ediyorum."
    mc "Bana da öyle geldi."
    mc "Ama zaten derslere pek dikkat etmedim."
    s 2h "Ama etmelisin! O zaman nasıl geçeceksin ki?"
    mc "Eh, merak etme. Daha önce de zorlanmadım, yine geçerim."
    s 5b "Keşke senin gibi gereksiz bir iyimserliğim olsa."
    mc "Bunu kimden öğrendiğimi sanıyorsun?"
    mc "Bunu, çok tatlı bir kız olan Sayori'den öğrendim."
    show sayori 1q at f11
    "Sayori, ciddi bir ifade takınmaya çalışırken, yüzünü gizlemeye çalışsa da, çenesi hafifçe titriyor ve yüzü kızarıyor."
    s 1c "Bari bir işime yaradım."
    s "Bunu dediğim için üzgünüm ama... depresyonum beni çok yavaşlatıyor, ama yine de elimden geleni yapıyorum!"
    mc "Sanırım bu doğru."
    mc "Sonuçta, bu çok senin tarzın gibi – her fırsatı değerlendirip ilerlemeye çalışıyorsun."
    "Birden sessizleşiyorum ve ikimizin ne kadar farklı olduğuna kafa yoruyorum."
    mc "Ama, eğer sınav için çalışmam gerekecekse, sanırım en iyi çalışma arkadaşımsın."
    stop music fadeout 3.0
    s 1a "Tabii, yardımcı olmaktan mutluluk duyarım... ama benden fazla bir şey bekleme."
    "Birden yüzü kararıyor."
    
    s 2t "Aslında sana ne kadar yardımcı olabilirim, onu da bilmiyorum."
    s "Ve, dürüst olmak gerekirse, bu konuda ne yapalım ki, belki de hiçbir zaman bir işim olmayacak bu saçmalık yüzünden?"
    s "Hadi itiraf edelim... çok rekabetçi bir dünyada yaşıyoruz."
    s 2w "Benden gibi zayıf bir kız burada tutunamaz."
    "Bunun depresyonunun etkisi olduğunu fark ediyorum."
    "Sayori’yi omuzlarından tutup ona sıcağımı hissettirmesi için onu yerinde tutuyorum."
    mc "Sayori, bana bak."
    mc "Her şey bitti demeden bitmez."
    mc "Evet, depresyon zor... Senin nasıl hissettiğini tam olarak anlayamam, ama kesin olarak söyleyebilirim ki, bu son değil."
    mc "Bundan daha güçlü olduğunu biliyorum – vazgeçme."
    
    play music Thoughts fadein 3.0
    s 1d "[player]..."
    s 1a "Teşekkür ederim. Bunları duyduğumda biraz daha iyi hissettim."
    s "Çok utanç verici... Senin sözlerin dışında kimse önemli değil."
    mc "Neden utanç verici olsun ki?"
    s 2c "Çünkü seni her yardıma çağırdığımda, sana daha fazla aşık oluyorum."
    s "Gerçekten başkalarına bu kadar bağımlı olmayı sevmiyorum."
    mc "Seni seviyorum, kendini sevmesen bile..."
    mc "Sana yardım edebilmek beni mutlu ediyor."
    mc "Ve garip gelebilir ama, depresyonlu anlarını dinlemek bana seni daha iyi anlamamı sağlıyor gibi geliyor."
    show sayori 1d at s11
    play sound fall
    "Sayori, zayıf bir gülümseme ile yere düşmeye başlıyor. Ben onu yakalayıp kollarımda tutuyorum."
    s "Çok zayıf hissediyorum... başım dönüyor."
    s 1t "Endişelenme – bu, yağmur bulutları devreye girdiğinde her zaman böyle oluyor."
    "Sonrasında son kısmı, yüzümdeki endişeli ifadeyi görünce ekliyor."
    "Hiç düşünmeden, bir kolumu sırtına, diğerini ise bacaklarına sarıyorum."
    s 4m "H-hey, ne yapıyorsun-?"
    "Onu yatağına taşırken, dikkatlice yatırıyorum."
    hide sayori with dissolve
    mc "Birkaç dakika sonra devam ederiz."
    mc "Yüzünden yorgun olduğunu görebiliyorum – biraz dinlenmelisin."
    s "Emin misin?"
    "Başımı sallıyorum."
    mc "Zamanımız kısıtlı, ama senin tükenmiş bir halde olman ikimize de fayda sağlamaz."
    mc "Ayrıca, şu an benim için en önemli kişi sensin."
    mc "Yorgun olduğun bir zamanda benden sınav çalışmasına yardım etmeni istemek haksızlık olur."
    s "Tamam."
    s "Beni göz ardı etmediğin için teşekkür ederim, [player]."
    mc "Teşekkür etmene gerek yok – bunu yapıyorum çünkü hoşlanıyorum."
    mc "Gerçekten seninle vakit geçirmeyi seviyorum, mutlu ya da üzgün olman fark etmez."
    mc "Çünkü sensin."
    "Sayori bana bir öpücük vermek için kalkmaya çalışıyor ama düşecek gibi oluyor – açıkça hareket etmek için çok yorgun."
    "Ne yapmaya çalıştığını fark edip, gözlerimi boş bir alana çeviriyorum. Yatakta oturabileceğim kadar geniş bir yer var."
    mc "Yanına oturabilir miyim?"
    s "Tabii."
    "Sesindeki ve gülümsemesindeki samimiyeti fark ediyorum. Bu sefer gerçekten samimi."
    "Gülümsüyorum ve yanına oturuyorum. Sonra pencereyi açıp biraz taze hava almasını sağlıyorum."
    s "[player]... bana dürüst olabilir misin?"
    mc "Tabii ki. Sana yalan söylememeyi söyledim, hatırlıyor musun?"
    "Başını sallıyor ve devam etmekte zorlanıyor gibi görünüyor."
    s "Sana doğrudan sormak için çok üzgünüm ama..."
    s "Benimle ilgili ne hissediyorsun?"
    s "Yani, seni sevdiğini biliyorum, ama merak ediyorum... yaşadıklarımı gördüğünde... seni korkutmuyor muyum?"
    "Saçlarını okşayıp, elimi sıcak yanaklarına doğru indiriyorum."
    mc "Depresyonundan korkmuyorum."
    mc "Çünkü bu senin bir parçası – seni sen yapan birçok güç ve zayıflıktan biri."
    mc "Tabii ki, keşke olmasa, ama seni buna rağmen daha az sevmediğimi söyleyebilirim..."
    mc "Sana mutlu olmanı istiyorum, ve bunun hayatını ne kadar zorlaştırdığını biliyorum."
    mc "Gerçekten haksız olduğunu düşünüyorum."
    s "Neden böyle diyorsun?"
    mc "Bana karşı hep iyilik ve sevgiyle davrandın."
    mc "Sadece bana değil, çevrendeki herkese – Yuri, Natsuki, Monika..."
    "Saçlarını tekrar okşarken, yüzünde mutlu bir gülümseme beliriyor."
    "Farkında olmadan, gülümsememi yansıtıyorum."
    "Bir an, ikimiz de aynı ritimde nefes alıyoruz."
    mc "Herhangi bir sebepten dolayı o haughty kız gibi olabilirdin."
    mc "Onun herkese karşı bu kadar kaba olmasının sebebi? Küçükken zorbalık görmüş ve belki de depresyonu vardır."
    mc "Ama sen, acını bu kadar tatlı ve sevgi dolu bir şekilde saklıyorsun... bunu gerçekten çok takdir ediyorum."
    mc "Keşke senin gibi güçlü olabilseydim."
    mc "Hep gösterdiğin pozitifliğin sahte olduğunu düşünmek istemiyorum..."
    "Sayori sessizleşiyor ve bir süre sessizce saçlarını okşarken bana bakıyor."
    "Gülümsüyor."
    s "Artık bilmiyorum."
    s "Pozitifliğimin sahte olduğunu düşünürdüm..."
    s "Ama... söylediklerin beni biraz düşündürdü."
    stop music
    "Birden korkunç bir acı içinde yüksek sesle çığlık atıyor."


    play music td
    show sayori 4w at f11
    s "Agh... başım!"
    "Sayori gözlerini kapatıp, ifadesi acı içinde şekil alıyor. Kafasını kollarıyla tutuyor."
    s "Çık... kafamdan çık!"
    s "Artık yalanlarını duymak istemiyorum!"
    "Ayağa kalkmaya çalışıyorum ama o, sol koluma güçlü bir şekilde sarılıyor."
    "Göründüğünden çok daha güçlü ve kolayca beni durduruyor, oturmak zorunda kalıyorum."
    s "Ben... artık seni dinlemek istemiyorum..."
    s "Sadece [player]'ı duymak istiyorum..."
    s "Onun sözlerine gerçek olarak inanmak istiyorum..."
    s 2j "Susturun şunu!"
    mc "Sayori... ne oluyor?!"
    "Sesimdeki endişeyi duyması, Sayori’yi trance halinden çıkarıyor."
    s 1h "B... beynim... söylediğin her şeyin yalan olduğunu söylüyor..."
    s "Ama artık... buna kulak vermek istemiyorum!"
    s 4g "Sadece senin nasıl mutlu olduğunu gördüğümde... ikimizin mutlu olduğunu düşündüğümde!"
    "Birden bir fikir geliyor aklıma."
    mc "Sayori... depresyona girmeden önce, yağmur bulutları arasında hiç güneş ışığı gördün mü?"
    "Başını sallıyor."
    "Açıkça acı çekiyor."
    stop music fadeout 3.0
    "İki elini de alıp onu öpüyorum."
    "Sayori nefesini tutarak bir anda yumuşuyor."
    
    mc "Endişelenme – yağmur bulutlarını ben yok edeceğim."
    mc "Eğer depresyonun seni izliyorsa, bilsin ki seni ne olursa olsun seviyorum."
    mc "Beni ne kadar itmeye çalışırsan çalış, bu değişmeyecek."
    s 2h "[player]... hayır... bunu yapma..."
    s 2w "Bu... buna değmez."
    "Gözyaşlarını tutmaya çalışıyor ve nefesi çok ağır."
    mc "Bana değiyor."
    mc "Sen buna değersin. Her gün böyle geçse bile, iyi ya da kötü, hep senin yanında olacağım."
    s 1h "Bu saçma! Sadece kendine zarar veriyorsun..."
    mc "Aşkın güzelliği de burada. Aşık olan insanlar, irrasyonel aptallar olurlar."
    mc "O yüzden depresyonuna söyle, defolup gitmeye çalışsın, çünkü ben buradayım – ne kadar beni itmeye çalışsa da, işe yaramayacak."
    mc "Çünkü biliyorum ki Sayori, benim kaybolmamı istemezdi."
    s "Sen..."
    s 1g "Ah!"
    "Bedeninden acıyla titreme geliyor."
    play music Dusk fadein 3.0
    "Onu kaldırıp sarılıyorum."
    "Sıkıca sarılıyorum, ne kadar mücadele etse de bırakmamaya kararlıyım."
    
    s 4w "Yağmur bulutları... gök gürültüsü bulutlarına dönüştü!"
    mc "O zaman ben onları uzaklaştıracak rüzgar olacağım."
    mc "Lütfen, Sayori... güçlü kal."
    mc "Bana inan, Sayori, sana olan sevgim gerçek!"
    mc "Seni seviyorum Sayori... ve asla seni bırakmak istemiyorum."
    mc "Sen benim tekim."
    s 1t "[player]..."
    mc "Söylediklerime inan, Sayori..."
    mc "Senin seni seviyorum... ve seni olduğun gibi seviyorum – depresyonunla ya da onsuz."
    mc "Hala seni sevdiğim o harika kızsın."
    stop music fadeout 3.0
    mc "Bu ne olursa olsun değişmeyecek."
    s "Haklısın..."
    play music Dawn fadein 3.0
    "Gözlerini kapatıyor ve yüzünde bir gülümseme beliriyor."
    s 1q "Yağmur bulutları rüzgarla geri itiliyor."
    "Onu kendime daha da yaklaştırıyorum."
    mc "Korkma, Sayori. Ben buradayım."
    mc "Artık yalnız değilsin... birlikte onları uzaklaştıracağız."
    "Bir an için, kalp atışlarımız tam uyum içinde atıyormuş gibi hissediyorum."
    "Nefeslerimiz birbirimizle senkronize."

    
    s "Gittiler..."
    s "Kaçtılar... yağmur bulutları kaçtı ve şimdi ufukta parlak bir güneş var."
    s "Bir gökkuşağı görüyorum... fırtınanın ardından gelen sakinlik."
    show sayori 1b at f11
    "Gözlerini açıyor ve konuşmasına gerek yok, sadece bakışları bana, kelimelerin tarif edemeyeceği kadar çok sevdiğini anlatıyor."
    "Ben de ona aynı şekilde hissediyorum."
    mc "Şimdi dinlenmelisin. Hala çalışmamız gerektiğini hatırlıyor musun?"
    s "Evet..."
    show sayori 1b at s11
    "Onu bırakıyorum ve o, yorgun bir bebek gibi yatağına geri yığılıyor."
    s "[player]... seni seviyorum."
    mc "Ben de seni seviyorum, Sayori."
    "Ellerini alıyorum."
    mc "Sadece... bu iş bittiğinde beni terk etme."
    mc "İyileştikten sonra bile seninle bir ilişki sürdürmek istiyorum."
    s 1c "Benden daha iyi bir erkek arkadaş bulamam."
    "Kızarıyor."
    s 1y "Komik... bir gün evleneceğim adamın, yağmur bulutlarını uzaklaştırabilen biri olacağını hep hayal ederdim."
    "Şaşkınlıkla başını sallıyor ve utanmış bir şekilde başını öne eğiyor."
    s "Uhh... söylediklerimi unut, tamam mı? Şoktan dolayı saçmalıyorum."
    "Başını okşayarak başını sallıyorum."
    mc "Aceleme Sayori."
    mc "Ben hiçbir yere gitmiyorum."
    s "Ben de gitmiyorum..."
    s "Sonsuza kadar seninle olmak istiyorum."
    s 1b "Bu çok gerçek dışı hissediyor..."
    mc "Evet, ama bugün biz sınav için çalışana kadar buradayım."
    mc "...Hey, Sayori?"
    s "Ne var?"
    mc "Özür dilerim."
    s 1h "Ne için?"
    mc "Son birkaç yıldır sana nasıl davrandım için."
    mc "Gerçekten aptaldım..."
    mc "Söylediklerimin sana nasıl etki ettiğine hiç dikkat etmedim."
    s 1c "Hiçbir zaman özür dilemen gerekmiyor, [player]."
    s "Eğer seninle vakit geçirmek istemeseydim, Seni Edebiyat Kulübü'ne katılmaya davet etmezdim."
    mc "Ama yine de... durumunu önceden bilseydim..."
    mc "Kesinlikle sana çok daha iyi davranırdım."
    s 1g "Lütfen yapma."
    s "Sana kızmıyorum – ben senin kendin olmanı istiyorum."
    s "Hatta şimdi..."
    s 1c "Çünkü seni, kusurlarına rağmen seviyorum."
    s "Her insanın hem iyi hem kötü yönleri vardır. Birini görmezden gelmek ya da diğerini kayırmak, sevgi olmaz."
    s "Sana bu kadar çekiliyorum çünkü beni gerçekten olduğum gibi görüyorsun. Bunu devam ettirmeni istiyorum."
    mc "Vay..."
    mc "Bana söylenen en tatlı şey bu."
    mc "Seninle tanıştığım için çok mutluyum, Sayori."
    mc "Sadece arkadaşken bile, her zaman nasıl neşelendirileceğimi bilirdin."
    s 1a "Zevk tamamen bana ait, [player]."
    s 1c "Sen benim güneş ışığımsın."
    s "...Gücümü geri kazandığımı hissediyorum."
    mc "O zaman çalışmaya başlayalım mı?"
    "Başını sallıyor."
    s 1b "Hayır..."
    s "Beş dakika daha... tamam mı?"
    s "Burası çok rahat... bu anın daha uzun sürmesini istiyorum."
    mc "...Evet."
    mc "Bunu ben de istiyorum."
    show black with close_eyes 
    
    "Bir süre birlikte sarılıyoruz."
    "Hiçbirimiz birbirimizi bırakmak istemiyor gibi görünüyor ama sonunda Sayori’ye neden burada olduğumuzu hatırlatıyorum."
    "Gecenin geri kalanında, taraflardan herhangi bir drama olmadan geçiyor."
    "Sayori, her zamankinden çok daha enerjik ve canlı görünüyor ve bu pozitiflik beni de etkiliyor."
    "Onun sabırlı rehberliği sayesinde, onunla geçirdiğim birkaç saatte, sınıftaki son birkaç aydan daha fazla şey öğreniyorum."
    "Akşam çok erken geliyor ve bana iyi geceler öpücüğü verdiğinde, artık kendini tutmadığını anlayabiliyorum."
    
    stop music fadeout 3.0
    scene bg bedroom_night with dissolve_cg
    "Neredeyse gece yarısı, evime dönüp yatağıma zafer dolu bir gülümsemeyle uzanıyorum."
    "Sayori’yi o kadar çok seviyorum."
    "Bugün onu daha iyi hissettirmeyi başardığımı bilmek, bana her şeyi yapabileceğimi hissettiriyor!"
    "Yorgun olmama rağmen, telefonumu çıkarıp ilişkilerde depresyonla başa çıkma hakkında bir makale aramaya başlıyorum."
    "Bir daha asla Sayori’yi hayal kırıklığına uğratmayacağım!"

    window hide
    show black with close_eyes 
    window show
    "O gece yine bir rüya gördüm."
    "Yine aynı sesleri duyuyorum."
    g "Bizi takip ediyorlar!"
    b "Onlardan bir şekilde kurtulamaz mıyız?"
    g "Çok fazla var... "
    g "Aah!"
    b "Şimdi mi, her şeyin tam ortasında?!"
    g "Y-yardım edin!"
    b "Tamam... sırtıma tırman!"
    g "A-ama... beni taşıyabilir misin?"
    b "Şimdi öğrenmenin tam zamanı!"
    "Sonra bir grup köpeğin havlaması ve hırlaması duyuluyor."
    "Bir dakika kadar sonra, havlamalar uzaklaşıyor."
    b "Of... iyisin değil mi?"
    g "E-evet..."
    b "Dur, kanıyorsun!"
    g "Beni boş ver..."
    g "Bu hiçbir şey..."
    b "Bir bandaja ihtiyacın var! Hadi gidelim."
    g "Nereye?"
    b "Evim. Orada sana bir bandaj alabiliriz, ayrıca oyuncak bebeğini de tamir ederiz."
    g "P-peki."
    b "Bana güvenebilir misin?"
    "Uzun bir sessizlik oluyor, sonra kız cevap veriyor."
    g "Evet, güvenebilirim."
    b "Bu arada... sanırım adını bile bilmiyorum, değil mi?"
    b "Benim adım [player]."
    mc "Ya senin?"
    g "Benim adım..."
    g "Sayori."
    "Sesler birden kesiliyor ve kısa bir süre sonra çalar saatin sesi duyuluyor."
    window hide
    call sayoriRoute_midnight
    return


label sayoriRoute_midnight:


    scene bg bedroom with open_eyes
    play music EarlyBird
    window show
    "Bir ay geçti, Sayori ile çıkmaya başlayalı."
    "Onunla geçirdiğim her gün, gerçek olamayacak kadar güzel bir rüya gibi."
    "İlişkimize gizli kalması için elimizden geleni yapıyoruz ve şimdiye kadar hiç kimse bir şey fark etmiş gibi görünmüyor."
    "Eğer birisi şüphelenirse, Sayori her zaman 'çocukluk arkadaşıyız' bahanesini kullanmaya hazır."
    scene bg residential_day with dissolve_cg
    "Bu güzel bir şey tabii..."
    "... Ama keşke ilişkimizden artık gizlemek zorunda kalmasak."
    "Sayori'nin depresyonu da son zamanlarda oldukça sessiz."
    "Neredeyse fazla huzurlu."
    stop music fadeout 3.0
    scene bg class_day with dissolve_cg
    "Sayori, yine gülüşünün arkasına acısını mı gizliyor acaba?"
    "O kadar düşüncelerimle kaybolmuşum ki, kağıt uçan kuşun alnıma çarpacağını fark etmedim bile."
    "Sınıfa bakınıyorum, kimlerin bana attığını anlamaya çalışıyorum ama çok fazla şüpheli var."
    "Yavaşça kağıt uçan kuşu açıyorum ve yerel parktaki 'ay ışığı geçidi' adlı etkinlik ilanını görüyorum, Sayori ve benim sık gittiğimiz bir park."
    "Bu neyin nesi?"
    "Telefonumu çıkarıp ismi aratıyorum ve gerçekten, her dolunayda yapılan bir etkinlik gibi görünüyor."
    "Sanırım kağıt uçan kuşu atan kişi beni özellikle hedef almadı ama neyse."
    "İlanı cebime koyup dersten çıkana kadar bekliyorum."
    "Bu pek de kötü bir fikir gibi görünmüyor - Sayori ile bir ayımızı kutlamak için iyi bir yol olabilir."
    show bg corridor with wipeleft_scene
    "Ders bitince, Sayori’yi burada bulabilmeyi umarak Edebiyat Kulübüne gidiyorum."
    show bg club_day with wipeleft_scene
    play music aNewDay fadein 3.0
    
    show monika 1a at t32
    show yuri 1a at t31
    show natsuki 1a at t33
    "Odaya girdiğimde, Monika ortada, Yuri ve Natsuki ise sandalyelerinde oturuyorlar."
    "Sayori ise hiç görünmüyor."
    show monika 1b at f32
    m "Ah, merhaba, [player]!"
    "Etrafa bakınıyorum. Sayori’nin hiç izini göremiyorum."
    mc "Sayori nerede?"
    show monika 1a at t32
    show yuri 1b at f31
    y "Bütün gün onu görmedim."
    show yuri 1a at t31
    show natsuki 1b at f33
    n "Ben de görmedim. Belki tuvalete gitmiştir ve kendini kilitlemiştir?"
    show yuri 2b at f31
    show natsuki 2r at t33
    y "N-Natsuki! Böyle şeyler söyleme."
    show yuri 2b at t31
    show natsuki 4b at f33
    n "Ne oldu ki? Olabilir. Onun ne kadar sakar olduğunu biliyorsun."
    hide natsuki
    hide yuri 
    with wipeleft
    show monika 2c at f11
    "O korkunç düşünceyi kafamdan atmaya çalışıp, Monika'ya dönüyorum, ki o da normalden oldukça sessiz ve düşünceli görünüyor."
    mc "Ya sen, Monika?"
    m 2d "Hm, acaba gerçekten...?"
    mc "Monika?"
    m 4q "Ama, bu sefer ben bir şey yapmadım ki..."
    mc "Monika! Sayori hakkında bir şey biliyor musun?" 
    "Monika derin bir iç çekiyor."
    m 4r "Son kez onu öğle yemeğinde gördüm, ama okulun giriş kapısına doğru yürüyormuş gibi görünüyordu."
    m "Çok garip bir şekilde keyifsizdi."
    "Yoksa sadece bana mı öyle geliyor, yoksa Monika’nın sesi biraz garip bir şekilde acı mı?" 
    m 5a "Bence onu görmelisin, [player]. Hadi ama, çabuk ol--onu fazla bekletme."
    scene bg corridor with wipeleft_scene
    "Bunu söyledikten sonra, Monika eski haline dönüyor ve ben hemen odadan çıkıp, en hızlı şekilde eve koşuyorum."
    scene bg residential_day with wipeleft_scene
    "Neden bir garip dejavu hissi içindeyim? Daha önce hiç böyle bir şey yaşamamıştım..."

    
    scene bg house with wipeleft_scene
    "Sayori'nin telefon numarasını arıyorum, ama cevap vermiyor."
    "Kapı kolunu çalmayı deniyorum ve kapının kilitli olmadığını fark ediyorum."
    show black with dissolve_cg
    
    "Sayori'nin odasının önünde kapısını çalıyorum."
    mc "Sayori?"
    mc "Lütfen, bana cevap ver..."
    play music Rainclouds fadein 3.0
    "Cevap yok."
    "Gerçekten, onun odasına böyle girmek istemedim..."
    "Bu biraz mahremiyet ihlali gibi değil mi?"
    "Ama gerçekten başka çarem yok."
    "Kapıyı nazikçe açıyorum ve sonunda onu buluyorum--" 
    
    scene bg sayori_bedroom with dissolve_cg
    mc "S-Sayori?!"
    show sayori 4f at t21
    "Yatak odasının köşesine kıvrılmış, bacaklarını kollarıyla sarmış."
    "Vücudu nadiren titreyen ara sıra hıçkırıkların dışında tamamen hareketsiz."
    mc "Sayori... ne oldu?"
    "Cevap vermiyor."
    hide sayori with dissolve
    "Onu kollarıma sararken, bile pek cevap vermiyor."
    "Tek yaptığı şey, zayıf bir şekilde başını sallayarak varlığımı kabul etmek."
    show sayori 1f at f11
    s "[player]..."
    mc "Buradayım, Sayori... lütfen bana ne olduğunu söyle."
    "Hıçkırıklar içinde beni sıkıca sarılıyor."
    s 1w "Öğle yemeğinde sana mesaj atmayı düşünüyordum... sana çıkma teklif etmek için..."
    s "A-ama sınıfımdan bazı kızlar telefonumda yazdığımı gördü... telefonumu çaldılar... ve mesajlarımızı okudular..."
    mc "Ne?!"
    s "S-onra... bana öyle korkunç şeyler söylediler..."
    s "Bundan sonra, hiçbir şey olmamış gibi davranmaya çalıştım... Monika ile konuşurken sakin kaldım ama..."
    hide sayori with dissolve
    "Duruyor ve yüzünü göğsüme gömüyor."
    s "Ne yapmam gerektiğini bilmiyorum..."
    s "Hatta... benim durumumu da okudular..."
    s "Bana... seninle ayrılmamı söylediler... ç-çünkü sadece bir yüküm..." 
    s "V-ve eğer yapmazsam... b-bunu... herkese... anlatacaklar..."
    "Sırtını okşuyor ve ona her şeyin şimdi yoluna gireceğini tekrar ediyorum. Birlikte bir yol bulacağız."
    show sayori 4w at f11
    s "Eğer seninle ayrılmazsam... bunu... herkesin depresyonumdan... bahsedecekler..."
    s "Farklı muamele göreceğim... Artık... aynı olmayacağım..."
    "Onu daha sıkı sarılıyorum."
    mc "Bunları söyleme."
    mc "Buradayım, Sayori. Seni terk etmeyeceğim."
    s "Evet... ben depresif olduğum sürece, sen gitmeyeceksin."
    mc "Ne?"
    s "Evimde yolda... bahçemde bir sokak köpeği gördüm, bir şey çekmeye çalışıyordu..."
    "Yanına kayarak uzun bir ipi çekiyor."
    "...ah, hayır."
    "Neden daha iyi saklamadım?"
    s 1l "Biliyordun... değil mi?"
    s "Bu sadece bana acıma gösterme şeklinizdi... hayatsız hayatımı sonlandırmamı engellemek için."
    "Sesi üzgün ve hayal kırıklığına uğramış... ama aynı zamanda yalvaran bir ton."
    "Bana korkmuş ve kararsız bir ifadeyle bakıyor."
    s 1h "Dürüstçe cevap ver, [player]..."
    "Ona ne söylemeliyim?"
    "Başlangıçta ona yardım etmek istediğim doğru olsa da, zamanla çok daha kişisel bir hale geldi."
    "Biliyorum, sadece bir şansım var."
    "İpini sıkıca tutuş şekli... cevabımın, ikimizin de geleceğini belirleyeceğini biliyorum."
    s 1g "Neden..."
#  DEVAM EDİCEM
    menu:
        s "Neden yaptın bunu?"
        "Çünkü sana yardım etmek istedim.":
            s 1f "...Biliyordum."
            s "Demek gerçekten diğerleri gibiydin..."
            s 1h "Üzgünüm... ama bence gitmen en iyisi olur."
            s "Yalnız kalmaya ihtiyacım var... kafamdaki ses... o kara bulutlar... çok gürültülü..."
            s "Ben..."
            s "AAAAAAAAAAGH!!!"

            show black with dissolve_cg
            "Sayori yere yığılıp bir çocuk gibi ağlamaya başlıyor."
            "Ne kadar teselli etmeye çalışsam da beni görmezden geliyor."
            "Sonunda bana bağırıp yalnız kalmak istediğini söylüyor—ona asla bir insan olarak bakmadığımı, sadece kendimi onun üstünde görmek için bir araç olarak gördüğümü..."
            "...Onun güvenini boşa çıkarmış gibi hissediyorum..."
            "Her şey bitti."

            call sayoriRoute_badEnd
            return
        "Çünkü sana aşığım.":
            stop music fadeout 3.0
            s 4m "N- ne?"
    play music AfterAll fadein 3.0
    mc "Senin depresyonda olduğunu öğrenmeden önce de sana aşıktım."
    mc "Sadece bunun dostluktan daha fazlası olduğunu anlamam çok uzun sürdü."
    show sayori 4v at f11
    "Sayori’nin yüzü kıpkırmızı oluyor ve tekrar göğsüme gömülüyor, ama bu sefer ağlamıyor."
    "Muhtemelen çok şaşırdı—ya da artık gözyaşlarını tüketti."
    mc "Sanırım şimdi anlıyorum..."
    mc "Edebiyat Kulübü’ne katılmamın sebebini..."
    mc "Çünkü sen istemiştin." 
    mc "Çünkü seninle olmak istiyordum—seninle vakit geçirmek istiyordum."
    mc "Ve sanırım... derinlerde bir yerde, arkadaşlıktan daha fazlası olabilmemiz için bir şans diliyordum."
    s 4w "Ben... ben yapamam..."
    mc "Lütfen beni itme. Sırf birkaç insan sana bunu söyledi diye benden ayrılma."
    s 4h "Ama... herkese anlatacaklar."
    mc "Belki de diğerlerinin de bilmeye hakkı vardır."
    s 1m "Ne demek istiyorsun?"
    mc "Gerçeği onlardan saklamaya devam edemezsin."
    show sayori 1f at f11
    mc "Bazı aptallar seni küçümseyecek olsa bile, ne olmuş yani?"
    mc "Seni gerçekten sevenler yine de yanında olacak... belki de her zamankinden daha fazla."
    mc "Ben olacağım."
    mc "Ve seni asla bırakmayacağım..."
    mc "Asla."
    s 1g "[player]..."
    s 1t "Teşekkür ederim..."
    "Gözyaşlarını silerek bana bakıyor."
    s "Ben..."
    "Elindeki ipi bana uzatıyor."
    s 1g "Bu ipi... kendimi bitirmek için kullanmayı planlıyordum."
    s "Ama senin bana nasıl hissettiğini söylemeden önceydi."
    s "Hayır... bu, hâlâ devam edecek cesareti bulabileceğimi fark etmeden önceydi."
    "Başını öne eğip dudaklarını ısırıyor, derin nefesler alarak devam ediyor."
    s "Ben... istiyorum ki bunu yakmanı."
    mc "Sayori?"
    s 4h "Sanırım yaşamak için gücü bulabilirim... ucuz kaçış yollarına bel bağlamadan."
    s "Yaşamak istiyorum..."
    "Sesi daha kararlı ve güçlü çıkıyor, tıpkı şiirlerini okurken olduğu gibi."
    s 4c"Yaşamak istiyorum!"
    s "Ben... yaşamak istiyorum! Ve güneşin bir kez olsun doğmasını istiyorum!"
    s "Hayatta kalmak istiyorum... senin yanında olmak istiyorum..."
    s 4x "Böylece ikimiz de mutluluğu bulabiliriz! Birlikte mutluluğu bulabiliriz!"
    mc "Sayori..."
    "Elimden nazikçe ipi alıyorum."
    mc "Bunu benimle birlikte yakmak ister misin?"
    s 4m "Ne?"
    mc "Hadi birlikte yakalım."
    mc "Bu, geçmişin sona erdiğini ve yeni bir hayatın başlangıcını simgeleyebilir. Birlikte, çift olarak."
    s 1m "Ben..."
    "Bir an tereddüt ediyor, ama sonra yüzüne kocaman bir gülümseme yayılıyor."
    s 1x "Evet. Seninle birlikte yakmayı çok isterim, [player]!"

    call sayoriRoute_future
    return



    label sayoriRoute_future:

    scene bg house with dissolve_cg
    "Arka bahçesine girdik ve ipi birlikte çekerek ardımızdan sürükledik."
    "Ağır ama güçlerimizi birleştirerek, onu ızgarasına yerleştirmeyi başardık."
    "Sayori gelip, düğmeyi çevirmeye çalıştı ama son anda tereddüt etti."
    "Ellerinin titrediğini fark ettim."
    "İçgüdüsel olarak yanına gidip, sağ elini tuttum, gözlerinin içine bakıp başımı salladım."
    "O da başını sallayıp, yüzüne küçük bir gülümseme yerleşti."
    "Sonra, serbest kalan ellerimizle birlikte, gücü maksimuma getirene kadar düğmeyi çevirdik."
    "Bir adım geri atıp, olan biteni izledik."
    "Bir süre hiçbir şey olmadı."
    play sound fall
    "Bir anda, Sayori yere yığıldı, oldukça yorulmuş görünüyordu."
    show sayori 2h at f11
    s "Ben... Başardım."
    s "Hayır... Biz başardık."
    "Ona biraz şaşkın ve endişeli bir şekilde baktım."
    "Sonra birden kahkahalarla gülmeye başladı."
    s 1c "Başardık! Kafamdaki seslere karşı koydum–onlara susmalarını söyledim."
    s 2x "Ve sustular!"
    s 1a "Bu tamamen senin sayende."
    s "Elini tuttuğunda, dünyada her şeyi yapabileceğimi hissettim."
    mc "Ben de aynısını hissettim..."
    mc "Sanırım işte buna aşkın gücü deniyor."
    s 1r "Neyse ki... Şimdi çok mutluyum!"
    "Bir öpücük için birbirimize yaklaşıyoruz ama bir anda yüksek bir çatlama sesi duyuyoruz, ikimiz de hemen grillere bakıyoruz."
    s "Vay... Harika..."
    "Büyüleyici..."
    
    "Ayağa kalkıp, ipin yavaşça yanmaya başladığını izledim, dev bir ateş topuna dönüşüyor."
    "Bir süre, alevler dans ediyormuş gibi görünüyor."
    s 1c "Bunun bir işaret olduğunu düşünüyorum..."
    s "Belki de kara bulutlar şimdi kaybolur."
    mc "Bence hemen kaybolmazlar... ama bu ilk adım."
    mc "Ve biz birlikte olduğumuz sürece, bunu başarabiliriz."
    s "Katılıyorum."
    
    show black with dissolve_cg
    "Alevlerin dansını izlemeye devam ettik, güneş batana kadar."
    "Hiçbirimiz bir kelime etmedik, ama sarıldık ve birbirimize sıkıca yaslandık – hem ısınmak için, hem de birbirimizi yakın hissetmek için."
    "Sadece ateş söndüğünde ve ip kül olana kadar, artık hiçbir şeyin eskisi gibi olmayacağını fark ettim."
    
    "İpi toplamaya yaklaşırken, güçlü bir rüzgar esiyor ve küller havaya savruluyor, rüzgar onları götürüyor."
    "Bitti."
    "Yanına gidip, onu öpmek istedim ama şaşırtıcı bir şekilde beni durdurdu."
    s "Ne yapacağımı bilmiyorum..."
    s "Şu anda o kadar çok düşünce ve duygu var ki içimde."
    mc "Ah..."
    mc "Dur... Bunu unuttum!"
    "Cebimden biraz önce üzerime düşen broşürü çıkarıyorum."
    s "Vay! Bu eğlenceli görünüyor!"
    mc "Evet, bunu yapabiliriz – belki ikimiz de biraz rahatlarız."
    s "Bugün gereksiz yere gergindik, değil mi?"
    mc "... Evet."
    s "Özür dilerim. Ama söz veriyorum... senin için değişeceğim ve daha iyi olacağım."
    s "Hayır... senin için değil."
    s "Seni seviyorum... ama kendimi sevip sevmediğimi bilmiyorum."
    s "Ama eğer kendimi sevmezsem... seninle bir ilişkide nasıl rahat edebilirim ki?"
    s "..."
    scene bg home_interior with wipeleft_scene
    "Gözlerini üzerimde gezdirirken, eve doğru yürürken, beni inceliyor."
    show sayori 1c at f11
    s "[player], bir süre hiçbir şey olmamış gibi davranabilir miyiz?"
    s "Beynimi, ne olduğunu biraz sindirmem için zamana ihtiyacım var."
    "Onu kucaklıyorum."
    "O da bana sıkıca sarılıyor."
    mc "Tabii. İstediğin kadar zamana sahip olabilirsin."
    mc "Beni de yanında ister misin?"
    s 1b "Hayır. Tam burada, benimle kalmanı istiyorum."
    mc "Huh...?"
    s "İlişkimize resmi olarak başlamak istiyorum, ama sanırım beynim seni erkek arkadaşım olarak görmeye alışana kadar biraz zamana ihtiyacı var."
    s 1a "Bu yüzden son bir akşam sadece arkadaş gibi geçirelim."
    s "Ve sonra..."
    "Yüzüne biraz yaramaz bir gülümseme yerleşiyor."
    s 1x "Sonra... seni çıkma teklif etmeye çağıracağım–tıpkı çocukken hep istediğim gibi."
    "Başımı sallıyorum."
    mc "Tamam – bence güzel bir fikir."
    s 1a "Ehehe~"
    s 4r "Sen en iyisisin."
    
    s 1c "Tamam, burada biraz bekle. Bu akşam sana yemek yapacağım."
    "Alnımdan ter damladığını hissediyorum."
    mc "Sadece--"
    s "- Evi yaktığım o zaman gibi mi? Merak etme, yakmayacağım."
    s "Çalışıyorum!"
    
    show sayori 1c at lhide 
    hide sayori 
    "Bununla birlikte, mutfağa doğru koştu."
    "Canlı enerji... o pozitif patlamalar..."
    "İşte bu, tanıdığım Sayori."
    "Hayır... hâlâ onu tanıyorum. Derinlerde, bunun onun gerçek kişiliği olduğuna inanıyorum."
    "Yanılıyorsam, ve gerçek kişiliği depresif kızsa bile, onu her halükarda seviyorum."
    "Ve asla onu bırakmak istemiyorum."
    "Şimdi değil, asla."
    
    scene bg park_night with wipeleft_scene
    play music Brick fadein 3.0
    "Okul kıyafetlerimizi değiştirmeye bile gerek duymadık."
    "Saat on bir buçuk civarı, ilk randevumuza gittiğimiz parka geldik."
    "O günden beri sanki yıllar geçmiş gibi hissediyorum."
    "Sayori ve ben el ele tutuşuyoruz ve onun yeniden kazandığı motivasyonu ve enerjiyi, ona bakmadan hissedebiliyorum."
    "Ellerinin, eskisinden daha sıcak."
    show sayori 1c at f11
    s "Sanırım havai fişekler yakında başlayacak..."
    s "Gel, güzel bir yer bulalım, izlemek için."
    mc "Bana bırak!"
    s 1x "Ne kadar güvenilir olduğuna bayılıyorum!"
    "Ona gülümsedim ve başımı salladım."
    mc "Sanırım bu bizim resmi ilk randevumuz, değil mi?"
    s 1a "Evet... ya da, bekle ve gör, tamam mı?"
    mc "Tamam."
    "Bir süre aradıktan sonra, boş bir masa ve iki sandalye bulduk."
    s 4c "Sanırım gösteriyi izlemek için yerimizi bulduk!"
    
    "Tam zamanında, oturduğu an, gökyüzü sayısız havai fişekle aydınlanıyor."
    s 1x "Vay, harika!"
    "Yanına oturuyorum, onu sıcak tutmak için kollarımda sarılıyorum."
    "O da aynı şekilde beni sarıyor."
    "Bilmiyorum, belki de onun dokunuşu yüzündendir ama onu yakın tutmak içimi ısıtıyor."
    s "Bu havai fişekleri seninle izleyebileceğim için çok mutluyum."
    mc "Ben de aynı şekilde."
    s 1b "Hey... [player]?"
    mc "Huh?"
    s 1c "Düşünüyordum..."
    s "Bizimle ve ilişkimizle ilgili."
    s 2c "Resmi olarak yapmak istiyorum–artık saklamak istemiyorum."
    s "Bunu istemediğinden emin misin?"
    mc "Ben de resmi yapmak istiyorum."
    mc "Ama bunu yapacaksak..."
    "Ellerini tutuyorum."
    mc "Bunu düzgün yapalım."
    "Gözlerine bakıyorum."
    s 1c "[player]... lütfen benim erkek arkadaşım olur musun?"
    mc "Sayori... lütfen benim kız arkadaşım olur musun?"
    "Sayori’nin gözleri, mutluluktan yaşlarla doluyor."
    "Aynı anda bu sözleri söyledik."
    
    
    s "Çok mutluyum, [player]!"
    s "Bunun hepsi senin sayende."
    mc "Söz veriyorum, seni bir daha asla hayal kırıklığına uğratmayacağım."
    s "Beni hiç hayal kırıklığına uğratmadın."
    s "Ve biliyorum ki asla uğratmayacaksın!"
    "Dudaklarımız birbirinden ayrılınca, aniden gökyüzünden yüksek bir patlama sesi duyuluyor."
    window hide
    scene bg sky_night with dissolve_cg

    
    play sound fireworks
    show green with Dissolve(1.0):
        alpha .5
    hide green with Dissolve(1.0)

    show blue with Dissolve(1.0):
        alpha .5
    hide blue with Dissolve(1.0)

    show red with Dissolve(1.0):
        alpha .4
    hide red with Dissolve(1.0)
    window show
    "Gözlerimizi gökyüzüne çeviriyoruz ve rengârenk bir havai fişek, tepemizde patlıyor."
    stop sound fadeout 3.0
    s "Bu bir işaret!"
    s "Kesinlikle her şeyin daha iyi olacağının bir işareti olmalı!"
    s "Hey, [player]?"
    mc "Hmm?"
    "Bana derin bir sevgiyle bakıyor ve saçlarımın arkasını nazikçe okşuyor."
    s "Seni mutlu etmek için elimden gelen her şeyi yapacağım, artık senin sevgilin olarak."
    mc "Zaten beni çok mutlu ediyorsun... Her gün ediyorsun."
    mc "Senin hayatta olman ve her gün yanımda olman benim için yeterli bir mutluluk."
    s "Ve bundan sonra, her günü seni daha da mutlu etmek için geçireceğime söz veriyorum."
    s "Çünkü artık ikimizin de mutlu olması için çabalayacağım."
    s "Bencil olmak istemem ama..."
    mc "Bazen bencil olmadan, başkaları için fedakâr olamazsın."
    mc "Ama kendini fazla yıpratma, olur mu?"
    s "Merak etme, yapmam."
    s "Zaten sen hep yanımda olacaksın ve bana rehberlik edeceksin, değil mi?"
    mc "Bu benim için mutluluk kaynağı."
    mc "Seni gerçekten çok seviyorum, Sayori."
    s "Ve ben de seni gerçekten çok seviyorum, [player]."
    s "Bazen senin benim için fazla iyi olduğunu düşünüyorum ama... artık senin sevgini hissetmek bana gerçekten mutluluk veriyor."
    s "Başta çok korkuyordum..."
    s "Ama artık değil."
    s "Sen bana cesaret veriyorsun ve sevgimizin karşılıklı olduğunu bilmek güzel bir his."
    mc "O zaman bundan sonra, her günü harika bir gün yapalım!"
    s "Anlaştık!"
    scene bg park_night with dissolve_cg
    
    "Sayori’yle birbirimize sıkıca sarılıyoruz."
    show sayori 1b at f11
    s "Bu arada..."
    s "[player], bir şey daha var."
    mc "Nedir?"
    "Dudaklarını büzüp derin bir nefes alıyor, sonra devam ediyor."
    s 2h "Depresyonumu diğerlerine anlatmaya karar verdim."
    s "Senin söylediklerini düşündüm ve fark ettim ki, bundan kaçmam yanlış olur."
    s "En azından, bunu açıkça söylemem ileride beni gereksiz bir stresten kurtarabilir."
    mc "Emin misin, Sayori?"
    "Başını sallıyor."
    s "Kolay olmayacak, biliyorum..."
    "Bileklerimi sıkıca kavradığını hissediyorum."
    s 1b "Ama sen yanımdayken başarabilirim."
    s "Bu bana yeter."
    s 2c "Ayrıca edebiyat kulübündekilerin de bilmesi gerekiyor. Onların benim için endişelenmesini istemiyorum, çünkü onlar da benim arkadaşlarım."
    mc "Sayori..."
    s 1c "Senden bir ricam olabilir mi?"
    mc "Ne istersen."
    s "Bunu onlara anlatırken yanımda olur musun?"
    s 4h "Ve eğer tereddüt edersem, gerçeği onlara sen söyler misin?"
    mc "Gerçekten emin misin bundan?"
    mc "Bunu yaptıktan sonra hiçbir şey eskisi gibi olmayacak."
    "Sayori hafifçe gülüyor, ama biraz buruk bir şekilde."
    s 1b "O gemi çoktan kalktı, [player]."
    s "Sana duygularımı açıkladığımda ve sevgili olduğumuzda çoktan değişti her şey."
    s 1c "Ama sorun değil."
    s "O kadar da özlemiyorum geçmişi."
    s "Tek gidebileceğim yön, ileriye doğru."
    mc "Evet."
    mc "Ne kadar istersek isteyelim, geçmiş hep geçmişte kalacak."
    mc "Hatta şu an hakkında konuştuğumda bile, o an geçmişe dönüşüyor."
    mc "Bu yüzden tek yol, ileriye bakmak."
    "Sayori başını sallıyor."
    s "O halde ben de geleceğime odaklanacağım."
    s 1x "Seninle birlikte, parlak bir geleceğe."
    s "Ve bunu istiyorsam, geçmişimle vedalaşmalıyım."
    s "Tıpkı o ipi yaktığımız gibi, insanları mutlu etmek için her şey yolundaymış gibi davranmaktan vazgeçmek istiyorum."
    s "Çünkü eğer ben de gerçekten mutlu olursam, onları da mutlu edebilirim."
    mc "Gerçekten çok büyüdün, Sayori."
    s "Bu tamamen senin sayende."
    s 4x "Çünkü dünyanın en harika erkek arkadaşına sahibim!"


    if(sayori_flag_one is True and sayori_flag_two is True):
        window hide
        stop music fadeout 4.0
        show white with Dissolve(5.0)
        pause(6.0)
        call sayoriRoute_sunshine
        window hide
        $ sayoriCompletedGood = True
        stop music fadeout 5.0
        show white_end with Dissolve(5.0)
        pause(3.0)
        
        show white with Dissolve(2.0)
        pause(5.0)
        $ persistent.sayoriCompletedGood = True
        
        return
    else:
        window hide
        show white with Dissolve(4.0)
        pause(3.0)
        $ sayoriCompletedGood = True
        stop music fadeout 5.0
        show white_end with Dissolve(4.0)
        pause(2.0)
        
        show white with Dissolve(2.0)
        pause(4.0)
        $ persistent.sayoriCompletedGood = True
        return
  
    
    
    label sayoriRoute_sunshine:
    
    
    show black with Dissolve(3.0)
    window show
    "Birkaç ay geçti ve yeni bir yıl başladı."
    
    
    scene bg club_day with dissolve_cg
    
    show sayori 4t at t41 zorder 1
    show yuri 1a at t42 zorder 2
    show natsuki 1a at t43 zorder 3
    show monika 1a at t44 zorder 4
    "Söz verdiği gibi, Sayori Edebiyat Kulübü'ndeki arkadaşlarına depresyonundan bahsetti."
    "...Tabii, benim yardımımla."
    "O günü hâlâ çok net hatırlıyorum."
    "Söylemeye çalıştı ama yarısında gözyaşlarına boğuldu."
    "Sonunda itirafın kalan kısmını ben tamamladım."
    show natsuki 1u at f43
    n "Vay be... Bunu hiç bilmiyordum..."
    show natsuki 1u at t43
    show yuri 3f at f42
    y "Sayori..."
    y "Senin için yapabileceğimiz bir şey var mı?"
    show yuri 3f at t42
    show monika 1c at t44
    m "..."
    "Sayori içini dökerken Monika'nın yüzündeki ifade..."
    "Ciddi bir ifadeydi ama aynı zamanda mutlu görünüyordu."
    show monika 1b at f44
    m "Ne zaman istersen benimle konuşabilirsin, Sayori."
    m 3b "Kulüp başkanı olarak elimden gelen her şeyi yaparım, sana bu süreçte destek olmak için."
    m 5a "...Ama sanırım senden çok daha iyi yardımcı olabilecek biri var zaten."
    m "[player], değil mi?"
    show monika 5a at t44
    show yuri 1e at f42
    y "[player]?"
    show yuri 1e at t42
    show natsuki 4b at f43
    n "Ooo! Demek bu yüzden ikiniz her zamankinden daha fazla salak aşıklar gibi davranıyordunuz!"
    show natsuki 4a at t43
    show yuri 2e at f42
    y "Siz... sevgili miydiniz?"
    show yuri 2e at t42
    show monika 2c at f44
    m "Anlıyorum..."
    m 3c "Demek hislerim doğruymuş."
    m 3k "Umarım ikiniz çok mutlu olursunuz!"
    show monika 1a at t44
    show natsuki 1c at f43
    n "Yani bundan sonra hep aşırı romantik şiirler mi yazacaksınız?"
    show natsuki 1c at t43
    show monika 4k at f44
    m "Bunu görmek eğlenceli olurdu!"
    show natsuki 3b at f43
    show monika 2j at t44
    n "Heh. [player]'ın aşk şiiri yazdığı bir an bile düşünmek komik geliyor!"
    show natsuki 3j at t43
    show monika 4b at f44
    m "Kesinlikle ilginç olurdu."
    show monika 3j at t44
    mc "Ah, hadi ama! O kadar da kötü değilim!"
    mc "Hem... Sayori bana yardım edecek."
    mc "O yüzden dikkatli ol Monika—bir sonraki festivalde bizim şiirimiz en iyisi olacak!"
    m "Bunu görmek için sabırsızlanıyorum."
    show yuri 3f at f42
    y "Y-yaani... kulüpten ayrılmayacaksın mı?"
    mc "Hayır. Burada kalıyorum."
    show yuri 1c at t42
    show natsuki 2c at f43
    n "Hah! Sakın ilişkiye girdin diye tembellik etmeye kalkma!"
    mc "Merak etme, etmeyeceğim."
    show natsuki 2a at t43
    show monika 1a at f44
    m "Ve Sayori..."
    m 5a "Ne olursa olsun, biz her zaman yanındayız."
    show monika 1a at t44
    show yuri 1b at f42
    y "Evet. Ne zaman bir şeye ihtiyacın olursa bana güvenebilirsin."
    show yuri 1a at t42
    show natsuki 1d at f43
    n "Aynen öyle!"
    n "Şekerin depresyona iyi geldiğini duymuştum—istersen sana bolca cupcake yaparım!"
    hide monika 
    hide natsuki 
    hide yuri 
    with wipeleft
    show sayori 1t at f11
    
    s "[player]..."
    s "Teşekkür ederim."
    s 1c "Sanki omuzlarımdan büyük bir yük kalktı gibi hissediyorum."
    mc "Ama unutma – bu işin en kolay kısmıydı."
    mc "Şimdi sınıfına söylemen gerekiyor."
    mc "Ve bunu bensiz yapacaksın."
    mc "Gerçekten başarabileceğine emin misin?"
    s 4c "Endişelenme--Biliyorum, yapabilirim."
    s "Beni yargılasalar bile... Umrumda değil."
    s "Çünkü sen, beni ben olduğum için seviyorsun."
    s 1x "Ve Edebiyat Kulübü'ndeki arkadaşlarım, onlara yalan söylemiş olmama rağmen beni kabul ettiler."
    s 4r "Bu yüzden, başarabileceğimi biliyorum!"

    stop music fadeout 2.0
    hide sayori
    show black 
    with dissolve_cg

    "Önümüzdeki birkaç ay boyunca, ikimizin de hayatı giderek daha iyi hale geldi."
    "Sayori, ailesine her şeyi anlatmak zorunda kaldı, ama düşündüğünden daha iyi karşıladılar."
    "Hatta bir araya gelip, ona gerçekten iyi bir psikiyatrist tuttular."
    "Zamanla, Sayori'nin depresyonunun giderek zayıfladığını gördüm."
    "Yeni yıl geldiğinde ise neredeyse tamamen yok olduğunu fark ettim."
    "Bense... Sayori'nin tedavisinin bir parçası olarak daha dışa dönük ve aktif biri haline geldim."
    "Onunla birlikte her terapi seansına gittim, doğru kelimeleri bulmasına yardımcı oldum, yanında oldum."
    "Sonunda, psikiyatristimiz ikimizin de daha aktif olmasını ve daha fazla egzersiz yapmasını önerdi."
    "Bilmiyorum... Bu onun uzmanlığı mıydı, yoksa benim sevgim ve sabrım mıydı..."
    "...ama sonunda, Sayori eskisi gibi oldu."
    "Ve bu kez, gülümsemesinin sahte olmadığını biliyorum."

    scene bg kitchen with dissolve_cg
    play music aNewDay fadein 3.0

    "Birkaç ay ileri saralım..."
    "Bugün 14 Şubat, Sevgililer Günü."
    "İronik olan şu ki, her zaman nefret ettiğim bu gün, bu yıl en çok heyecanlandığım gün oldu."
    "Masaya oturmuş, ayağımı hafifçe yere vururken, bu yılki Sevgililer Günü'nü Sayori ile geçireceğim için ne kadar şanslı olduğumu düşünüyorum."
    "...Her günü anlamlı kılan, beni daha iyi bir insan olmaya teşvik eden o kız."
    "Onu her düşündüğümde, istemsizce yüzüme bir gülümseme yerleşiyor."
    "İp olayından sonra aramızdaki sevgi her geçen gün daha da büyüdü."
    "Birbirimize tamamen güveniyoruz—ve o, kendimi yanında en rahat hissettiğim tek kişi."
    "İkimiz de sakarız, hatalar yapıyoruz ama biliyorum ki, kusurlarımla da beni seviyor."
    "...Tıpkı benim de onu kusurlarıyla sevdiğim gibi."
    "Ve bunun böyle devam etmesini istiyorum, yıllarca..."
    "Ona şimdilik söylemek istemiyorum, umutlandırmak da istemiyorum, ama bir gün istikrarlı bir işim ve iyi bir gelir kaynağım olduğunda..."
    "...Ona evlenme teklif edeceğim."
    "Uzun zamandır düşünüyorum ve artık eminim, hayatımı birlikte geçirmek istediğim kişi o."
    "Düşüncelerim, kapının çalınmasıyla bölünüyor."
    "Kendi kendime gülmeden edemiyorum."
    "Sayori, evimin anahtarına sahip ama her seferinde kapıyı çalmaya devam ediyor."
    mc "Açık, gel içeri Sayori!"

    stop music fadeout 3.0

    "Kapı açılıyor ve odayı, ona yılbaşı hediyesi olarak aldığım parfümün kokusu kaplıyor."
    s "Ah, doğru ya... Anahtarım olduğunu unutmuşum!"
    s "Hazır mısın, [player]?"
    play music NextToYou fadein 3.0
    s "Sana söz verdiğim gibi, yeni bir tarz deniyorum."
    mc "Bekliyorum."

    window hide
    scene bg sayoriChocolate1 with Dissolve(3.0)
    pause(1.5)
    window show

    mc "Vay..."
    s "Ş-şey... Beğendin mi?"
    mc "Her geçen gün daha da güzelleşiyorsun..."
    mc "Seni her gördüğümde nasıl daha güzel olabiliyorsun?"
    s "Çok mutlu oldum!"
    s "Ah, doğru ya... Şey..."
    s "Çikolataları ben yaptım."
    s "Umarım berbat etmemişimdir..."
    "Elindeki kutuyu bana uzatıyor."
    mc "Neden oturup birlikte tadını çıkarmıyoruz?"
    "Sayori, yüzünde mutlu bir gülümsemeyle yanıma oturuyor, başını omzuma yaslıyor."
    "Beni izlerken heyecandan yerinde duramıyor."
    "Kutuyu açıyorum ve içi kalp şeklinde çikolatalarla dolu."

    scene bg kitchen with dissolve_cg

    show sayori 7a at f11 
    "Bir tane alıp Sayori’ye uzatıyorum, ardından elini tutuyorum."
    mc "Bence ilk lokmayı birlikte yemek daha romantik olurdu."
    "Sayori kızarıyor ve birlikte çikolatayı ısırıyoruz."
    "Tam ortasında, dudaklarımız birbirine değiyor ve öpüşüyoruz."
    s 6x "Nasıl olmuş?"
    mc "Bu çikolatalar... mükemmel olmuş!"
    mc "Gerçekten, mutfaktaki yeteneğin inanılmaz gelişmiş!"
    s 7c "Ehehe~"
    s "Ama en iyi öğretmene sahiptim!"
    s 6c "Ve ayrıca... her şeyden çok bir motivasyonum vardı."
    s "Seni mutlu etmek istedim, çünkü senin yanında mutluyken..."
    s "Bu, kalbimi hızlandırıyor ve seni mutlu etmek için daha çok çabalıyorum."
    s "Çünkü beni mutlu ediyorsun... ve bu yüzden yağmur bulutlarını kovmaya devam ettim."
    "Sıkıca sarılıyoruz, kalp atışını hissedebiliyorum."
    s 6a "Aslında, bununla ilgili..."
    "Bir an duraksıyor."
    mc "Evet?"
    s 7h "Psikiyatristime göre, tam iyileşmeye çok yakınım."
    s "Bunun tamamen mümkün olmadığını biliyorum..."
    s "Ama dürüst olmak gerekirse, artık o duyguyu hissetmiyorum."
    s 7a "Yağmur bulutları gitti."
    s "Arada bir hüzün dalgası gelse de, seninle vakit geçirmeyi düşündüğümde hemen yok oluyor."
    mc "Sayori..."
    s 6c "Bunun tek sebebi, hep yanımda olmandı."
    s "Beni hiçbir zaman farklı görmedin ve bana gerçekten sevildiğimi hissettirdin."
    s "Sen buradayken ve aramızdaki bağdan emin olduğum sürece..."
    s "Vazgeçmem için hiçbir sebep yok."
    mc "Sayori..."
    s 6f "[player]... ne oldu?"
    s "Ağlıyor musun?"
    "Gözyaşlarımın aktığını fark etmiyorum bile, ta ki Sayori nazikçe onları silene kadar."
    "Gülümseyerek bana bakıyor."
    mc "Sanırım sadece... çok mutluyum ve rahatladım..."
    s 7h "Lütfen ağlama. Biliyorsun, ben de kolay ağlarım."
    s "Ve artık ağlamak istemiyorum..."
    s 6c "Her günü gülümseyerek karşılayacağım—ister güneşli olsun, ister yağmurlu."
    s "Biliyor musun neden?"

    scene bg sayoriChocolate3 with dissolve_cg
    s "Çünkü seni seviyorum, [player]."
    s "Seni her zaman seveceğim!"
    s "Ve senin sevgini hissetmek, kendimi kabullenmemi sağladı."
    s "Bu yüzden, tüm kalbimle..."
    scene bg sayoriChocolate4 with dissolve_cg
    s "Teşekkür ederim!"
    return
