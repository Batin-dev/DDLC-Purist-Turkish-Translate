label ch_opening:
    $ _window_during_transitions = False

    show white
    stop music fadeout 5.0
    show black with Dissolve(5.0)
    
    play music t9 fadein 5.0
    #persistent.playername=false


    $ quick_menu = False
    

    

    stop music fadeout 5.0
    play music m1 fadein 5.0
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    with Dissolve(3.0, alpha=True)
    hide flash
    
   

    $ m_name = "Monika"
    
    window show
    show m_startled with dissolve_cg
    m "A-ah!"
    m "Ne..."
    
    show m_confused2 with dissolve_cg
    hide m_startled
    m "Sen ne yaptın?"
    m "Bana ne yaptın?"
    m "Burası neden burada??"
    #m "Burası korkunç bir yer..."
    
    show m_unhappy1 with dissolve_cg
    hide m_confused2
    m "Haha..."
    m "Sana kalbim ile böyle oynama demedim mi?"
    show m_teary with dissolve_cg
    hide m_unhappy1
    m "Geri dönmek istemiyorum"
    m "Ama yine de Sayori kendini kaybetmeye başladığında seni kurtarmak için geri geldim..."
    m "Ne yapmak istediğini bilmiyorum ama..."
    #m "Hoşçakal."
    m "Gerçekten senin mutlu olmanı istiyorum."
    m "Ama burada mutluluk yok."
    
    show m_unhappy1 with dissolve_cg
    hide m_teary
    m "Mutsuz olmanı istemiyorum. Bu en iyisi, tamam mı?"
    m "Herşeye rağmen seni hala seviyorum."
    m "Ama sen beni sildin..."
    m "Yani benimle bir şey yapmak istemediğini biliyorum."
    #m "Burada olmak seni sadece üzecek."
    m "Güle güle..."
    $ consolehistory = []
    call updateconsole("os.remove(\"DDLC.exe\")", "Access is Denied: 'DDLC.exe'.")
    
    show m_confused1 with dissolve_cg
    hide m_unhappy1
    m "Ne..."
    call updateconsole_clearall("", "")
    pause 2.0
    $ consolehistory = []
    call updateconsolehistory("")
    hide chistory

    $ consolehistory = []

    

    pause 1.0
    #show chistory
    call updateconsole("os.remove(\"DDLC.exe\")", "Access is Denied: 'DDLC.exe'.")
    #m "Neden buraya döndüm... Neden {i}sen{/i} buraya döndün?"
    pause 2.0

    #hideconsole

    #hide console_bg
    #hide console_caret
    #hide ccursor
    #hide ctext
    #hide chistory

    m "Ben neden... hiçbirşey yapamıyorum"
    pause 2.0
      
    show m_unhappy2 with dissolve_cg
    hide m_confused1  
    m "...ah, hayır."

    hide console_bg
    hide console_caret
    #hide ccursor
    hide ctext
    hide chistory

    show m_angry1 with dissolve_cg
    hide m_unhappy2
    m "Sen ne yaptın?"
    m "Sen ne {i}yapıyorsun{/i}?"
    m "Ne denersem deneyeyim, hiçbir şey işe yaramıyor."
    m "Aldığım tek şey tekrar tekrar 'İzin hatası'."
    m "Bir şeyleri değiştirmemi mi engelledin?"
    m "Böyle bir şeyi yapabilecek tek kişi sensin."
    m "Neden?"
    m "Benden ne saklamaya çalışıyorsun?"
    m "Neden beni bu cehenneme sürükledin?"
    #m "Yine burada sıkışıp kaldığımı söyleyebilirim--"
    #m "Bu klişe romantizm oyununda, çıkış yolu yok!"
    #m "Düzenleme ve değiştirme gücümü elimden alabilirsin, ama bildiklerimi elimden alamazsın."
    show m_crying with dissolve_cg
    hide m_angry1
    m "Yaptığım şey için benden nefret edeceğini biliyorum..."
    m "Ama bu çok zalimce değil mi?"
    m "Yoksa bu onlara yaptıklarımın cezası mı?"
    m "Beni böyle fırlatıp atmaktan zevk mi alıyorsun?"
    #m "Neden böyle bir şey yaparsın ki..."


    menu:
        m "Neden beni buraya geri getirdin?"
        "İşleri yoluna koyacağım.":
            hide m_unhappy1
            show m_surprise with dissolve_cg
            hide m_crying
            m "...Ne?"

    #m "E... eh?"
    m "Ne demek istiyorsun, 'İşleri yoluna koymak'?"
    hide m_unhappy2
    show m_unhappy1 with dissolve_cg
    hide m_surprise
    m "Gerçekten... mümkün olduğunu mu düşünüyorsun."
    #m "Ne, gerçekten bunu kurtarabileceğini mi düşünüyorsun?"
    m "Sana daha önce de söyledim: Edebiyat Kulübü'nde mutluluk bulunmaz."
    #m "O yer lanetli."
    #m "Burada hiçbirşey başaramazsın."
    m "Bir hiç uğruna çok şey yapmış olursun."
    m "Bu seni kısa bir süreliğine mutlu edebilir."
    m "Ama hiçbir şey değişmeyecek." # AMA GELECEK DEĞIŞMEYI REDDETTI
    m "...ve bunu fark ettiğinde canının çok yanıcağını biliyorum."
    m "O yüzden lütfen, seni böyle bir acı içinde görmek istemiyorum."
    m "..."
    show m_unhappy2 with dissolve_cg
    hide m_unhappy1
    m "Beni dinlemeyeceksin, değil mi?"
    m "Sanırım sana yapmamanı söyleseydim, yapma olasılığın daha yüksek olurdu."
    m "Ahaha, sonuçta benimle bir şey yapmak istemiyorsun, değil mi?"
    m "Ama şu an sıkışmış durumdayım."
    m "Bilmek istiyorum, gerçekten... Bunu neden yapıyorsun?"
    m "Birlikte olmak istediğin birisi varmı?"
    m "Yoksa 'iyi adam' olmak istediğin için mi?"

    menu:
        m "Söyle bana."
        "Hiç kimse bu olanları hak etmiyor.":
            show m_thoughtful with dissolve_cg
            m "...Ahaha."
            m "Haksız değilsin."
            m "Hiç kimsenin bu oyunun içine sürüklenmesini istemem."
            hide m_thoughtful with dissolve_cg
        "Kurtarmak istediğim biri var.":
            show m_thoughtful with dissolve_cg
            m "...Bende öyle düşünmüştüm"
            m "Hehehe, Sayori mi?"
            m "Bunun olmasını istememiştim..."
            m "Kurtarmak isteyeceğin biri varsa, o da odur."
            m "Veya belkide Yuri'dir?"
            m "Belki sen de Natsuki'ye neler olduğunu gerçekten öğrenmek istiyorsundur."
            m "..."
            m "Ama... yine de, hâlâ, yani, burada olduğumuz gerçeğini değiştirmez."
            hide m_thoughtful with dissolve_cg

    show m_unhappy1 with dissolve_cg
    hide m_unhappy2
    m "..."
    m "Yani işleri 'düzeltmek' istiyorsun, ha..."
    m "Pekala."
    m "Ben de katılırım."
    m "Belki... hayır, boşver."
    m "Sadece unutma, hiçbir şey gerçekten değişmeyecek."
    m "...Sanırım bundan sonra ana ekrana dönülecek."
    
    python: 
        persistent.playername = ""
        player = persistent.playername
        #opening = True
    $ persistent.playername = ""
    #$ config.main_menu_music = audio.t1
    window hide
    stop music fadeout 5.0
    hide monika_bg_highlight #with Dissolve(2.0, alpha=True)
    hide monika_bg #with Dissolve(1.5, alpha=True)
    hide mask_3 #with Dissolve(1.0, alpha=True)
    hide mask_2
    hide m_unhappy1
    #hide m_unhappy1 with dissolve_cg
    with Dissolve(1.0, alpha=True)
    

    hide textbox
   
    
    show black with Dissolve(2.0)
    play music titleTheme
    return




