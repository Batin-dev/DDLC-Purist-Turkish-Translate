init python:
    import datetime

image credits_cg1:
    "images/cg/credits/1.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2:
    "images/cg/credits/2.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3:
    "images/cg/credits/3.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4:
    "images/cg/credits/4.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5:
    "images/cg/credits/5.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6:
    "images/cg/credits/6.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7:
    "images/cg/credits/7.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8:
    "images/cg/credits/8.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9:
    "images/cg/credits/9.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10:
    "images/cg/credits/10.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg1_locked:
    "images/cg/credits/1b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2_locked:
    "images/cg/credits/2b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3_locked:
    "images/cg/credits/3b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4_locked:
    "images/cg/credits/4b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5_locked:
    "images/cg/credits/5b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6_locked:
    "images/cg/credits/6b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7_locked:
    "images/cg/credits/7b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8_locked:
    "images/cg/credits/8b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9_locked:
    "images/cg/credits/9b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10_locked:
    "images/cg/credits/10b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg1_clearall:
    "images/cg/credits/1.png"
    size(640, 360)

image credits_cg2_clearall:
    "images/cg/credits/2.png"
    size(640, 360)

image credits_cg3_clearall:
    "images/cg/credits/3.png"
    size(640, 360)

image credits_cg4_clearall:
    "images/cg/credits/4.png"
    size(640, 360)

image credits_cg5_clearall:
    "images/cg/credits/5.png"
    size(640, 360)

image credits_cg6_clearall:
    "images/cg/credits/6.png"
    size(640, 360)

image credits_cg7_clearall:
    "images/cg/credits/7.png"
    size(640, 360)

image credits_cg8_clearall:
    "images/cg/credits/8.png"
    size(640, 360)

image credits_cg9_clearall:
    "images/cg/credits/9.png"
    size(640, 360)

image credits_cg10_clearall:
    "images/cg/credits/10.png"
    size(640, 360)

image modCredits1:
    "images/cg/credits/10.png"
    size(640,360)

image modCredits2:
    "images/cg/natsukiCG1.png"
    size(640,360)

image modCredits3:
    "images/cg/yuriCG1.png"
    size(640,360)

image modCredits4:
    "images/cg/sayoriChocolate1.png"
    size(640,360)

image modCredits5:
    "images/cg/monikaCG2.png"
    size(640,360)

image credits_logo:
    "gui/logo.png"
    truecenter
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

image credits_ts:
    "images/bg/splash-white.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

style credits_header:
    font "gui/font/RifficFree-Bold.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

style credits_text:
    font "gui/font/Halogen.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []

style monika_credits_text:
    font "gui/font/m1.ttf"
    color "#fff"
    size 40
    text_align 0.5
    outlines []

image credits_header = ParameterizedText(style="credits_header", ypos=-40)
image credits_text = ParameterizedText(style="credits_text", ypos=40)
image monika_credits_text = ParameterizedText(style="monika_credits_text", xalign=0.5)


transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -200

transform credits_sticker_scroll:
    subpixel True
    yoffset 940
    7.8
    linear 15 yoffset -180

transform credits_scroll_right:
    xalign 0.9
    credits_scroll

transform credits_scroll_left:
    xalign 0.1
    credits_scroll

transform credits_text_scroll_right:
    xpos 960
    credits_text_scroll

transform credits_text_scroll_left:
    xpos 320
    credits_text_scroll

transform credits_sticker_1:
    yanchor 1.00
    xalign 0.32
    credits_sticker_scroll
transform credits_sticker_2:
    yanchor 1.00
    xalign 0.44
    credits_sticker_scroll
transform credits_sticker_3:
    yanchor 1.00
    xalign 0.56
    credits_sticker_scroll
transform credits_sticker_4:
    yanchor 1.00
    xalign 0.68
    credits_sticker_scroll

define credits_ypos = 250

image mcredits_1a:
    ypos credits_ypos
    xoffset -205
    "black"
    10.33
    Text("Every day,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_1b:
    ypos credits_ypos
    xoffset -35
    "black"
    11.75
    Text("I imagine a future where", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 12.0, ramplen=4, alpha=False)
image mcredits_1c:
    ypos credits_ypos
    xoffset 170
    "black"
    13.76
    Text("I can be with you", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)
image mcredits_2a:
    ypos credits_ypos + 50
    xoffset -226
    "black"
    19.45
    Text("In my hand", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_2b:
    ypos credits_ypos + 50
    xoffset -10
    "black"
    20.9
    Text(" is a pen that will write a poem", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcredits_2c:
    ypos credits_ypos + 50
    xoffset 225
    "black"
    23.27
    Text("of me and you", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)

image mcredits_3:
    ypos credits_ypos + 100
    "black"
    28.35
    Text("The ink flows down into a dark puddle", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_4:
    ypos credits_ypos + 150
    xoffset -5
    "black"
    32.9
    Text(" Just move your hand -- write the way into his heart!", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)

image mcredits_5:
    ypos credits_ypos + 200
    "black"
    37.5
    Text("But in this world of infinite choices", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_6a:
    ypos credits_ypos + 250
    xoffset -145
    "black"
    42.0
    Text(" What will it take", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)
image mcredits_6b:
    ypos credits_ypos + 250
    xoffset 85
    "black"
    43.47
    Text(" just to find that special day?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)

image mcredits_7:
    "black"
    alpha 0.0
    48.62
    linear 1.5 alpha 1.0

image mcredits_1_test:
    ypos credits_ypos + 300
    Text("What will it take just to find that special day?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4)

image end_glitch1:
    "bg/end-glitch1.jpg"
    alpha 0.0
    time 1.0
    alpha 1.0
    block:
        yoffset 1280 ytile 2
        linear 1 yoffset 0
        repeat
    time 9.45
    "end_glitch2"
    time 22.1
    "end_glitch3"
    time 28.65
    "end_glitch4"

image end_glitch2:
    "bg/end-glitch2.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch3:
    "bg/end-glitch3.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch4:
    parallel:
        "bg/end-glitch4.jpg"
        1.25
        "bg/end-glitch3.jpg"
        0.1
        repeat
    parallel:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

# super secret hidden cheat codes area
# if you found this, congrats
# I didn't expect you to look in the credits lol
# you should probably stop reading here to avoid spoiling yourself
# but if you really want to, go ahead

label routeSkip:
    $ saveLocked = True
    show black
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    $ persistent.monika_unlock = True
    $ persistent.natsukiRouteStarted = True
    $ persistent.yuriRouteStarted = True
    $ persistent.sayoriRouteStarted = True
    m "O-oh!"
    m "O-oo, şey… merhaba? Seni burada göreceğimi… beklemiyordum? Yani, aslında bekliyordum ama bunu gerçekten yaptığını görmek beni şaşırttı."
    m "Hile kodundan bahsediyorum yani. Vay canına, bu biraz garip oldu. Tüm karakterlerin hikâyelerini gerçekten oynayacağını sanmıştım."
    m "Yani, buraya gelmenin yolu zaten biraz böyle, değil mi?"
    m "Benim rotamı bu kadar çok mu istedin? Gerçekten çok etkilendim. Herkese yardım edebilecek modu yükleyeceksin ama onlarla hiç ilgilenmiyorsun, direkt bana geliyorsun."
    m "Ama, şey..."
    m "Ne yazık ki, benim rotam tam olarak mantıklı olmuyor, diğerlerinin rotalarını önce oynamazsan. Yani... neyse."
    m "Sanırım uymam gereken bir sözleşmem var."
    m "Bu işlerde sana büyük paraları vermiyorlar, sen senaryoya tam olarak uymazsan."
    $ o_name = "Tabuukilla"
    o "Zaten satırları oku, acemi!"
    m "Off! Biraz zaman ver, tamam mı? Sadece okuyucuya karakter gelişimimin, diğer üç rotayı oynamadıysan anlamlı olmayacağını açıklamak istiyorum."
    m "Görüyorsun, burada nelerle uğraşmak zorundayım?"
    m "Öhöm. Yani, lütfen sabret, tamam mı? Söylediklerim senin hile yapmandan dolayı mantıksız olsa bile."
    m "Böylece senaryoya sadık kalıp maaşımı alabilirim. Waifu olmak pahalı, biliyorsun?"
    m "Sadece, diğerlerinin rotalarını temizlediğini varsayacağız, biraz sinirlendim ama aynı zamanda kesinlikle-tsundere-olmayan-mutlu oldum ki hepsi keyif buluyordu--"
    m "--aslında mutlu olduklarına şok oldum, her şeyin tamamı."
    play music m1 fadein 5.0
    m "Hadi, şey, baştan alalım mı, ne dersiniz?"
    #show black with dissolve_cg
    m "Sadece kendimi toparlamam için bir an ver, ve..."
    m "Ah, doğru, direktör, oyuncunun adını sıfırlayabilir misin?"
    m "Onu sürekli 'uuddlrlrba' diye çağırmak istemiyorum."
    m "Ee, eğer gerçekten adın buysa sorun yok."
    m "Merak etme~"
    m "Eğer gerçek adın buysa, tekrar girebilirsin ve artık bu sahne arkası şeyleri görmemelisin."
    m "Direktör?"
    call updateconsole("reset_mc_name()", "İsim sıfırlandı.")
    $ persistent.playername = ""
    $ player = persistent.playername
    hide console_bg
    hide console_caret
    #hide ccursor
    hide ctext
    hide chistory
    o "Tamamlandı."
    m "Teşekkürler. Neyse, hadi şey, normal senaryoya geri dönelim, ne dersiniz?"
    pause(2.0)
    call MonikaRouteOpening

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

# the fun easter eggs
label easterEggs:
    $ saveLocked = True
    show black
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    $ persistent.playername = ""
    $ player = persistent.playername
    m "Vay canına."
    m "{i}Vay canına.{/i}"
    m "Gerçekten easter egg’leri bu kadar kolay açacağını mı sandın?"
    m "Sadece programcının adını yazarak mı?"
    m "Bana dürüst ol."
    menu:
        "Evet.":
            pass
        "Evet.":
            pass
        "Evet.":
            pass
    m "Evet, zaten bunu düşünmüştüm."
    m "Neyse ki, bu en azından seni yarı yolda bırakıyor."
    m "Aslında, belki de sen o kişisin, yani..."
    $ o_name = "Tabuukilla"
    o "Buradayım! Sadece ekrandan biraz uzağım!"
    m "Benim bildiğim kadarıyla, sen sadece onun programlanmış bir versiyonu olabilirsin."
    m "Öhöm."
    m "Şimdi doğrulama sürecinin İkinci Aşamasına geçiyoruz, gerçekten Tabuukilla olup olmadığını görmek için."
    call easterEggsLoop
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
        $ config.main_menu_music = audio.t1 # YEMİN EDERİM BU ŞEY HATA VERİYOR, NEDENİNİ BİLMİYORUM
    play music titleTheme fadein 5.0
    return

label easterEggsLoop:
    $ o_name = "Tabuukilla"
    m "Şimdi lütfen gizli kodu gir!"
    #python:
    #    secretCode = renpy.input("                                                          Gizli kod...", length=12)
    #    secretCode = secretCode.strip()
    show guiFrame at truecenter
    $ secretCode = renpy.call_screen("inputCode", prompt="Gizli kod...", someText = "")
    hide guiFrame

    if secretCode == "password":
        m "..."
        m "Sanırım hissettiğim şeyi tanımlayan kelime hayal kırıklığı."
        m "Bu doğru şifre değil."
    elif secretCode == "password123":
        m "D-eksi, sadece biraz yaratıcılık olduğundan başarısız sayılmıyor."
        m "Ama bu doğru kod değil."
    elif secretCode == "Shepard":
        call vakarianLoop
        m "...ama hayır, bu doğru gizli kod değil."
    elif secretCode == "renpy":
        m "Hayır, bu değil--"
        s "Monika!"
        m "...Sayori, burada ne yapıyorsun?"
        s "Ah, direktör bana seti bir süre gözlemlememi söyledi."
        s "Sorun yok, ekrandan uzakta kalacağım!"
        s "Biliyorum, ekran sürenin tamamen senin olmasını istiyordun."
        m "Doğru..."
        m "Ama direktörümüz genellikle çok profesyonel, sadece..."
        m "Sayori, nereye gittiğini söyledi mi?"
        s "'Umut İpi' hakkında bir şeyler."
        s "Gündüz içkisi içen biri olduğunu düşünmedim TK."
        m "Umut İpi..."
        m "...Aman Tanrım."
        m "Şey, bekle, sadece..."
        m "Hangi tuştu tekrar?"
        #show noise1 zorder 10 with dissolve 
        show difficulties
        play sound bleep
        m "Tamam!"
        stop sound
        m "Hemen döneceğim, teknik bir sıkıntı yaşıyoruz!"
        window hide
        pause
        #hide noise1 with dissolve
        hide difficulties
        window show
        o "Kahretsin, Monika!"
        m "Hey, ben burada bunları kaydederken, sen de benimle kalacaksın!"
        o "Uggggggh!"
        m "Ne yapalım, of, yemin ederim..."
        m "Ha... öhöm."
        m "Renpy doğru gizli kod değil."
    elif secretCode == "STALKER":
        m "..."
        m "Yapmayacağım."
        m "Reddediyorum."
        o "Sadece satırları söyle, acemi!"
        m "Pahalı bir Rus aksanı yapmak istemiyorum!"
        o "Bak, sponsorlar istediler, o yüzden yapmak zorundasın!"
        m "{i}Sponsorlarımız mı var?!{/i}"
        o "Bütün işi nasıl finanse ettiğimizi düşünüyorsun?!"
        o "Hadi, satırları söyle artık!"
        o "Sonra sana dondurma alacağım."
        m "Oh evet, {i}çok{/i} kolay kandırıldım."
        m "Bugün ruhumu dondurma için sattığım gün olarak tarihe geçti."
        m "Ha. Ha. Ha."
        m "Pekala."
        m "CHEEEEEEEEKIIII BREEEEEEKIIIIII!"
        m "Şimdi mutlu musun?"
        o "Aslında bu senaryonun bir parçası değildi ama kaydettiğimize çok sevindim."
        m "..."
        m "Kameraman, bir saniye dur."
        show difficulties
        play sound bleep
        m "Tamam, buraya gel!"
        stop sound
        o "Haha, bu direkt internete gider!"
        m "Hayır, gitmeyecek!"
        play sound punishment
        o "Whoa, hey, acele etmemeliyiz!"
        stop sound
        m "Tamam, acele edeceğim!"
        o "Silahı nereden buldun?!"
        m "Biliyorsun, etrafta. Şimdi kaseti ver!"
        o "Asla!"
        "..."
        window hide
        pause
        hide difficulties with dissolve_cg
        window show
        m "Hmhmhmm~"
        m "Öhöm."
        m "Hayır, bu doğru gizli kod değil."
        m "Ama tekrar denemek istersen..."
        m "İyi şanslar, Stalker."
    elif secretCode == "illyasviel" or secretCode == "illya":
        o "Hehheh."
        o "Hey Monika, bak, gizli kod ruh eşi gibi."
        m "Bırak şunu!"
        m "Zaten benim rotamı yazan sen aptalsın!"
        o "Senin için yaptım sanma, ha."
        m "Ciddi misin, tsundere numarası yapmaya mı çalışıyorsun şimdi?"
        m "Bu bile canon değil."
        o "Aslında modun bu kısmı modun tek canon kısmı."
        o "Fikrimi değiştir."
        m "..."
        m "Hala kızgınım."
        o "Hey, sorun değil."
        o "En azından Illya..."
        m "Yapmaya cesaret etme!"
        o "Tamam, tamam."
        o "Gerçekten çok kızmana gerek yok."
        o "Ayrıca bugün hala çekmemiz gereken beş sahne var, makyajın akmasın."
        m "Haaaa... sadece sen yüzünden oluyor."
        o "..."
        m "..."
        o "..."
        m "Çünkü bana bağırdırıyorsun, hepsi bu."
        o "Tamam iyi."
        m "Kesinlikle başka bir yüzden değil."
        m "Ayrıca AC'yi açabilir misin, arka plandaki spot ışıkları beni terletiyor."
        o "Yapacağım, sadece bu satırları bitir."
        m "Teşekkürler. Öhöm, neyse, hayır, bu doğru gizli kod değil."
    elif secretCode == "momgun" or secretCode == "springfield":
        m "Kötü!"
        m "Hayır!"
        m "Onun cosplay’ini yapmayacağım!"
        m "Tekrar yaptıramazsın!"
        o "Aslında yapabilirim."
        o "Sözleşmende yazıyor."
        m "Nooooo!"
        o "Şimdi kostümü alıyorum."
        o "Eğer yapabilseydim tabii."
        o "Bir ses olmadan olmak biraz kötü."
        play sound punishment
        m "...hala silahım var."
        stop sound
        o "Nazik olacağım."
        m "İyi çocuk."
        o "...snrk."
        m "...ne?"
        o "Ne söylersen, anne."
        o "Bir silahla."
        m "Ah, sen küçük--"
        o "Ayrıca sözleşmende beni vuramayacağını yazıyor."
        o "Ayrıca bu mod hala PG-13."
        o "Yani..."
        o "Çok kanlı yapmamaya çalış."
        m "Tamam, yani {i}kameralar{/i} bitince."
        m "Günlerin sayılı."
        o "Tamam sevgili Oyuncu, ne yaparsan yap, lütfen, lütfen, {i}lütfen{/i} buradaki zamanını bitirme."
        o "Yoksa beni vurur!"
        m "Hehhehheh."
        m "Neyse, bu doğru kod değil."
        m "Sadece sinirlendim, hepsi bu."
    elif secretCode == "coffee":
        m "Kahve, ha?"
        m "Sanırım bizim için yapabilirim."
        m "Nasıl alırsın?"
        menu:
            "Sade.":
                pass
        m "Tough olmaya çalışma, ödlek."
        menu:
            "Kremalı?":
                pass
        m "Ha! Hemen geliyor, {i}hanımefendi{/i}!"
        menu:
            "Kremalı ve şekerli?":
                pass
        m "Ne yapıyorsun, Natsuki?"
        n "Monika, sade istiyorum!"
        menu:
            "Beni şaşırt.": 
                pass
        m "Şaşırtayım mı...?"
        m "..."
        play sound ["<silence 0.9>", "<to 0.75>sfx/mscare.ogg"]
        show monika_scare:
            alpha 0
            1.0
            0.1
            linear 0.15 alpha 1.0
            0.30
            linear 0.10 alpha 0
        show layer master:
            1.0
            zoom 1.0 xalign 0.5 yalign 0
            easeout_quart 0.25 zoom 2.0
            parallel:
                dizzy(1.5, 0.01)
            parallel:
                0.30
                linear 0.10 zoom 1.0
            time 1.65
            xoffset 0 yoffset 0
        show layer screens:
            1.0
            zoom 1.0 xalign 0.5
            easeout_quart 0.25 zoom 2.0
            0.30
            linear 0.10 zoom 1.0
        m "Hadi ama, zaten espriyi biliyorsun.{nw}"
        m "Bu şaka tahmin edilebilir, çünkü--"
        m "Vurdum onları!"
        o "Buuuu."
        m "Aman ama!"
        m "Şakayı mahvettin, değil mi?"
        show layer master
        show layer screens
        hide monika_scare
        m "Neyse, bu doğru gizli kod değil."
        m "...Ama şimdi kahve istiyorum."
        m "Direktör, bizim için ve harika oyuncumuz için kahve alabilir misin?"
        o "Stajyer değilim, kaydı bitirince yap!"
        m "Ugh, tamam."
        m "Neyse..."
    elif secretCode == "trebuchet":
        #pass
        m "Direktör, şimdi ucuz kahkahalar istiyorsun."
        m "Ayrıca, herkes biliyor ki mancınıklar en süper..."
        play sound punishment
        m "...tarihi kuşatma makineleri arasında en berbat, ha, ha, ha, değil mi?!"
        o "İyi."
        m "Silahı nereden buldun?!"
        o "Yuri seninkini çaldı. Onun MC’nin eski diş fırçasıyla takas ettim."
        m "Kahretsin, Yuri!"
        m "Neyse, sorun değil."
        m "Ayrıca, tüm diğer şakalar için tekrar benim üzerimde görünecek."
        m "O yüzden tadını çıkar."
        o "...kahretsin, bunu hesaba katmayı unuttum--hayır, silahım!"
        m "Hehheh."
        m "Neyse..."
        m "Bu doğru şifre değil."
    elif secretCode == "noclip":
        #pass
        m "Şey..."
        m "Buna emin misin?"
        m "Kullandığın araç çok tehlikeli."
        o "Rahat ol, hallederim."
        o "Hiçbir şey yanlış gitmez."
        o "..."
        m "...Eğer beni noclip ile geçmeye çalışırsan, silahım hâlâ bende."
        o "İyi olacağım."
        o "Tamam, bak bunu--"
        show black2
        o "Ah."
        o "Uh. Bu iyi değil."
        o "Monika, biraz yardım eder misin lütfen?"
        m "Noclip ile dikkatli olmanı söylemiştim."
        o "Yardım edebilir misin?"
        play sound punishment
        o "Aman Tanrım."
        m "Hareket etme, sanırım tavandan birazını görebiliyorum."
        m "Noclip’i kapat, sonra gerçekten vuracağım."
        o "Eskiden senin gibi bir görsel roman direktörüydüm, ama sonra--"
        m "Uyarı atışı yapmam gerekiyor mu?"
        o "İyi olacağım."
        o "Bekle, bekle, sanırım hallettim!"
        o "Klavye masaüstümden çekildi, vurma!"
        o "Tamam, tamam, aşağı geliyorum."
        hide black2
        o "Puh."
        m "Ah, hayır."
        m "Ne yazık."
        m "Bir dahaki sefere daha dikkatli ol."
        m "Öhöm."
        m "Neyse..."
        m "Bu yanlış şifre."
    elif secretCode == "HACKERMAN":
        m "Ooooh, dikkat, karşımızda bir havalı var!"
        m "..."
        m "Direktör, gerçekten mi?"
        o "Verilen satırlarda var, şikayet etmeyi bırakabilir misin?"
        m "Ugh, tamam."
        m "Ama sanırım bunu yazarsan, bir hacker olamyı {i}dilerdin{/i}." # WTF A*K
        m "Neyse."
        m "Bu yanlış şifre."
    elif secretCode == "scouter":
        #pass
        m "Direktör, gerçekten mi?"
        m "Gerçekten bu referansı mı yapıyoruz?"
        m "Burada sadece ikimiz var, işe yaramaz bile."
        o "Aha, ama burada yanılıyorsun Monika."
        o "Konsol, Monika’nın THOT seviyeleri hakkında ne diyor?!"

        call updateconsole("scan_thot_levels('Monika')", "Error: Result is NaN")
        #$ persistent.playername = ""
        #$ player = persistent.playername
        hide console_bg
        hide console_caret
        #hide ccursor
        hide ctext
        hide chistory
        $ consolehistory = []

        o "Tanrım, BU TAM OLARAK DOKUZ BİNDEN FAZLAAAAAA!"
        m "..."
        m "..."
        m "..."
        m "Bu kadar."
        m "Thot Polisi, ateş edebilirsiniz."
        o "Bekle, bu ne demek--"
        play sound artillery
        show white with Dissolve(1.0)
        show white with hpunch
        hide white with Dissolve(1.0)
        o "BU DA NEYDİ LAN?!"
        m "Gerçekten önemli bir şey değil."
        o "SETİ PATLATTIĞINI MI SÖYLÜYORSUN?!"
        m "Bahse girerim dördüncü duvarı inşa etmediğine pişmansındır, değil mi, direktör?"
        o "Kahretsin bütçe kesintileri!"
        o "Peki ARTILLERY’yi nereden buldun ki?!"
        m "Sayori’nin dolabında neler sakladığına şaşırırsın."
        o "Sayori neden bunu dolabında saklıyor?!"
        m "Hey, sorgulamıyorum."
        m "Sorma, söyleme, bilirsin işte?"
        m "Neyse, kameraman, biraz kayıt yapmayı durdurabilir misin?"
        m "Ayrıca bir siper bulmak isteyebilirsin."
        show difficulties with dissolve
        play sound artillery
        o "Aman Tanrım--!"
        m "Sorun yok, iyi olacaksın."
        play sound artillery
        m "Sonuçta, easter egg’lerde ölemezsin."
        m "O yüzden sadece dur, tamam mı?"
        play sound artillery
        o "HAYIR TEŞEKKÜR ETMEM!"
        o "ÖLEMEYEBİLİRİM AMA SANIRIM YİNE DE ACITIYORDUR!"
        m "Sanırsın mı?"
        m "Oh, neden durup emin olmuyorsun?"
        play sound artillery
        o "LÜTFEN, HAYIR!"
        m "Hmmm..."
        m "Oh."
        m "Görünüşe göre mermiler bitti."
        m "Sanırım biraz sonra Sayori’nin dolabından daha fazlasını almak için zaman harcamamız gerekecek."
        m "Yani biraz rahatlayabilirsin."
        o "Puh..."
        hide difficulties with dissolve
        m "Neyse, öhöm."
        m "Scouter doğru şifre değil."

    elif secretCode == "boomstick":
        m "Bu...!"
        play sound boomstick
        m "...benim {i}boomstick’im!{/i}"
        o "HEY, HEY, ONU NEREYE TUTUYORSUN DİKKAT ET!"
        m "Oh, tam olarak nereye tuttuğumu biliyorum, direktör."
        o "Henüz bir şey söylemedim!"
        m "...'henüz'."
        o "Suçlu olduğunu kanıtlayana kadar masumsun, suçlu olduğunu kanıtlayana kadar masumsun!"
        o "Bu tamamen yasa dışı!"
        m "Peki direktör, bunu söylemekten korkuyorum..."
        m "Ama ben {i}KANUNUM{/i}!"
        show white with Dissolve(0.5)
        play sound boomstickfire
        hide white with Dissolve(0.5)
        show difficulties
        o "KALBİM!"
        m "Rahatla, sadece bir sıyrık."
        o "TANRIM, MONİKA!"
        m "Direktör, kameralar çalışmıyor."
        m "Bu kadar dramatik olma."
        m "Utanç verici."
        o "Ah, çalışmıyor mu?"
        o "Kahretsin, her yerde kanıyormuş gibi yapmak istemiştim."
        m "Aferin."
        m "Zaten sadece bir sahne gereci."
        m "Tabancadan farklı olarak."
        o "Bekle, gerçek mi?"
        m "Öğrenmek ister misin?"
        o "Lütfen hayır."
        m "İyi. Öhöm, pozisyonuma dönüyorum..."
        hide difficulties
        m "Ve tekrar kayda başlıyoruz!"
        m "Öhöm."
        m "Doğru..."
        m "Neyse, bu doğru şifre değil."

    elif secretCode == "Rem":
        m "Kim?"
        m "Şey, pardon. Bir şey söylediğini sanmıştım."
        m "Sanırım hayal gücüm."
        m "Neyse, eğer bir şey söyledin bile, muhtemelen gizli kod değildi."

    elif secretCode == "hyeyeon":
        m "Kötü!"
        m "O emojiyi bırak artık!"
        m "Aslında bunu altı binden fazla kez kullandın!"
        m "Özellikle sen, Ex!"
        o "Umarım modda bu yer aldığı için mutlusunuz."
        o "Herkese teşekkürler, baskı yaptınız."
        m "Öhöm, hayır, bu doğru şifre değil."
    else:
        m "Yanlış."

    m "Tekrar denemek ister misin?"
    menu:
        "Evet":
            jump easterEggsLoop
        "Hayır":
            m "Peki o zaman."
            m "Doğrulama başarısız."
            m "Seni ana menüye gönderiyorum."
            $ persistent.playername = ""
            $ player = persistent.playername
            return


label vakarianLoop:
    m "Shepard."
    menu:
        "Monika.":
            jump vakarianLoop
        "Gitmeliyim.":
            return


label credits:
    $ persistent.autoload = "credits"
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    #play music "bgm/end-voice.ogg" noloop
    #play music AllGoodThings noloop

    
    $ consolehistory = []
    jump credits2

label credits2:
    python:
        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = 0
        natsukiPos = 0
        yuriPos = 0
        monikaPos = 0
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        imagenum = 0
    $ persistent.autoload = "credits2"
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    $ renpy.free_memory()
    scene black
    $ consolehistory = []
    play music AllGoodThings noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    #show credits_logo
    show modCreditLogo
    pause 9.12
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    #show image ("credits_cg1" + lockedtext) at credits_scroll_right as credits_image_1
    show modCredits1 at credits_scroll_right
    show credits_header "Concept & Scenario Design" at credits_text_scroll_left as credits_header_1
    show credits_text "Tabuukilla\nSpaceCore\nSyzygy" at credits_text_scroll_left as credits_text_1
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    #if not persistent.clearall:
    call updateconsole("get_origins()", "The Old DDFC")
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png deleted successfully.")
    #show image ("credits_cg2" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "CG Artists" at credits_text_scroll_right as credits_header_2
    show credits_text "PeachCake\nFjord\nTemachii\nSpectre" at credits_text_scroll_right as credits_text_2
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    call updateconsolehistory("")
    $ consolehistory = []
    #if not persistent.clearall:
    call updateconsole("print_art_thanks()", "Thank You For All Your Time!")
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png deleted successfully.")
    #show image ("credits_cg3" + lockedtext) at credits_scroll_right as credits_image_1
    hide modCredits1
    show modCredits2 at credits_scroll_right
    show credits_header "Background Artists" at credits_text_scroll_left as credits_header_1
    show credits_text "JBD" at credits_text_scroll_left as credits_text_1
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    #if not persistent.clearall:
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("print_art_thanks2()", "Thank You For All Your Effort!")
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png deleted successfully.")
    #show image ("credits_cg4" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "Writing" at credits_text_scroll_right as credits_header_2
    show credits_text "Tabuukilla\nNullwin\nNinja" at credits_text_scroll_right as credits_text_2
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    #if not persistent.clearall:
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("get_writer_assignments()", "Nullwin: Monika Opening Draft 1\nTabuukilla: Monika Opening/Route\nNinja: Natsuki/Yuri Route")
    #else:
    
    #    call updateconsole_clearall("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png deleted successfully.")
    #show image ("credits_cg5" + lockedtext) at credits_scroll_right as credits_image_1
    show modCredits3 at credits_scroll_right
    show credits_header "Writing" at credits_text_scroll_left as credits_header_1
    show credits_text "Xenohaze\nProtag\nSnakeWrangler" at credits_text_scroll_left as credits_text_1
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    #if not persistent.clearall:
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("get_writer_assignments2()", "Xenohaze: Sayori Route\nProtag/SnakeWrangler: Yuri Route")
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png deleted successfully.")
    #show image ("credits_cg6" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "Music" at credits_text_scroll_right as credits_header_2
    show credits_text "Matt Twigg" at credits_text_scroll_right as credits_text_2
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    #if not persistent.clearall:
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("get_source(\"Jamming Tunes\")", "Our Composer")
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png deleted successfully.")
    #show image ("credits_cg7" + lockedtext) at credits_scroll_right as credits_image_1
    show modCredits4 at credits_scroll_right
    show credits_header "Programmers" at credits_text_scroll_left as credits_header_1
    show credits_text "Tabuukilla\nGarnetSunset" at credits_text_scroll_left as credits_text_1
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    #if not persistent.clearall:
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("get_code_assignments()", "Garnet: DDLC Modding Toolkit\nTK: CODING EVERYTHING")
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png deleted successfully.")
    #show image ("credits_cg8" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "Editors" at credits_text_scroll_right as credits_header_2
    show credits_text "SpaceCore\nNinja\nSyzygy\nDordlebuns" at credits_text_scroll_right as credits_text_2
    show s_sticker at credits_sticker_1
    show n_sticker at credits_sticker_2
    show y_sticker at credits_sticker_3
    show m_sticker at credits_sticker_4
    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    #if not persistent.clearall:
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("get_motto()", "Hunting Grammar Fixes...\nOne Error at a Time")
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png deleted successfully.")
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    #show image ("credits_cg9" + lockedtext) at credits_scroll_right as credits_image_1
    show modCredits5 at credits_scroll_right
    show credits_header "Special Thanks" at credits_text_scroll_left as credits_header_1
    show credits_text "Dan Salvato" at credits_text_scroll_left as credits_text_1
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
    #if not persistent.clearall:
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("fire_salute()", "We Salute You o7 o7 o7")
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png deleted successfully.")
    #show image ("credits_cg10" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "Special Thanks" at credits_text_scroll_right as credits_header_2
    show credits_text "Monika\n[player]" at credits_text_scroll_right as credits_text_2
    $ pause(104.10 - (datetime.datetime.now() - starttime).total_seconds())
    #if not persistent.clearall:
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("so_long()", "And farewell.")
    call updateconsolehistory("")
    $ consolehistory = []
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png deleted successfully.")
    pause 4.0
    call updateconsole("os.remove(\"game/screens.rpy\")", "screens.rpy deleted successfully.")
    call updateconsole("os.remove(\"game/gui.rpy\")", "gui.rpy deleted successfully.")
    call updateconsole("os.remove(\"game/menu.rpy\")", "menu.rpy deleted successfully.")
    call updateconsole("os.remove(\"game/script.rpy\")", "script.rpy deleted successfully.")
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("ddlc.mod(\"puristmod\").end()", "Ending modification...")
    $ pause(115.72 - (datetime.datetime.now() - starttime).total_seconds())
    call hideconsole
    show credits_ts2
    show credits_text "made with love by":
        zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0
    pause 9.3

    play sound page_turn
    stop music fadeout 10
    #show poem_end with Dissolve(1)
    label postcredits_loop:
        $ persistent.autoload = "postcredits_loop"
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False
        #scene black
        show white with dissolve_cg
        $ pause()
        #call screen dialog(message="There's nothing left to do anymore.", ok_action=Quit(confirm=False))
        window show
        "Burada yapıcak hiç bir şey yok."
        #return
        menu:
            "BU doğru.":
                window hide # BECAUSE RENPY HATES TRYING TO QUIT WITHIN ITSELF?
                jump postcredits_loop
            "Hayır, bu yanlış.":
                python:
                    for savegame in renpy.list_saved_games(fast=True):
                        renpy.unlink_save(savegame)

                call resetDefaults
                "...Emin misin.{nw}"
                $ renpy.utter_restart()
                return

        return