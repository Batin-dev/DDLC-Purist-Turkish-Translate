## Bu başlangıç ekranı, Ren'Py'nin oyuncuya gösterdiği ilk şeydir
##
## Yüklemeden önce, arşiv dosyalarının bulunduğundan emin olun.
## Eğer yoksa, bir hata mesajı gösterin ve çıkın.
init -100 python:
    # Gerekli her arşivi kontrol et
    for archive in ['audio','images','scripts','fonts']:
        if not archive in config.archives:
            # Eğer bir eksikse, bir hata mesajı göster ve çık
            renpy.error("DDLC arşiv dosyaları /game klasöründe bulunamadı. Kurulumu kontrol edin ve tekrar deneyin.")

## Önce, bu mod olduğunu belirten bir uyarı gösterilir, ardından
## orijinal DDLC varlıklarının kurulum klasöründe olup olmadığı kontrol edilir. 
## Eğer bulunamazsa, oyuncu geliştiricinin sitesine yönlendirilir.
##
init python:
    menu_trans_time = 1
    # Varsayılan başlangıç mesajı, ilk ve dördüncü bölümde gösterilen
    splash_message_default = "DDLC purist modu için geliştirici versiyon"
    # Opsiyonel başlangıç mesajları, ikinci ve üçüncü bölümde rastgele seçilen
    splash_messages = [
    "O senin için bekliyor.",
    "Benim için de bir tane var mı?",
    "Bu oyun resmi olmayan bir hayran çalışmasıdır, Team Salvato ile bağlantısı yoktur.",
    "Tekrar hoş geldin."
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

## Logo dosyasını istediğiniz şeyle değiştirebilirsiniz
image menu_logo:
    "images/menu/mod_logo.png"
    subpixel True
    xcenter 180
    ycenter 150
    zoom 0.60
    menu_logo_move

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=20, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat  
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"

label splashscreen:

    # Eğer bu oyunun ilk kez çalıştırılıyorsa, bir uyarı göster
    default persistent.first_run = False
    if not persistent.first_run:
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "[config.name] Doki Doki Edebiyat Kulübü fan modudur ve Team Salvato ile bağlantısı yoktur."
        "Resmi oyunun tamamlandıktan sonra oynanması için tasarlanmıştır ve resmi oyunun spoilerlarını içermektedir."
        "Doki Doki Edebiyat Kulübü oyun dosyaları bu modu oynamak için gereklidir ve ücretsiz olarak indirilebilir: http://ddlc.moe"
        menu:
            "[config.name] oynayarak, Doki Doki Edebiyat Kulübü'nü tamamladığınızı ve içindeki tüm spoilerları kabul ettiğinizi onaylıyorsunuz."
            "Kabul ediyorum.":
                pass
        scene tos2
        with Dissolve(1.5)
        pause 1.0

        # Opsiyonel, DDLC kayıt verisinin bir kopyasını yükle
        #call import_ddlc_persistent

        scene white
        with Dissolve(1.5)

        $ persistent.first_run = True

    $ basedir = config.basedir.replace('\\', '/')

    # autoload işlemleri
    # splash ekranını atlamak istiyorsanız persistent.autoload kullanabilirsiniz
    if persistent.autoload and not _restart:
        jump autoload

    # Başlangıç ekranı mantığı
    $ config.allow_skipping = False

    # Splash ekranı
    show white
    $ persistent.ghost_menu = False # DDLC'den gelen bir şaka için
    $ splash_message = splash_message_default # Varsayılan başlangıç mesajı

    #if persistent.monikaRouteStarted is True:
    #    $ splash_message = renpy.random.choice(splash_messages)

    if persistent.opening_scene is True:
        $ config.main_menu_music = audio.titleTheme
    else:
        $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)
    # İsterseniz rastgele başlangıç mesajları kullanabilirsiniz. Varsayılan olarak, yalnızca belirli bölümlerde gösterilirler.
    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    return

label warningscreen:
    hide intro
    show warning
    pause 3.0

label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False # DDLC'den gelen bir şaka için
    $ style.say_dialogue = style.normal
    # Kayıt dosyasının değiştirilip değiştirilmediğini kontrol et
    if anticheat != persistent.anticheat:
        stop music
        scene black
        "Kayıt dosyası yüklenemedi."
        "Hile yapmaya mı çalışıyorsunuz?"
        # İstediğiniz gibi işleyin, varsayılan olarak tüm kayıt verilerini sıfırlamak
        $ renpy.utter_restart()
    return

label autoload:
    python:
        # Genellikle splash'tan sonra yapılan işler
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()

        # Oyun bağlamını düzeltin (genellikle kayıt dosyası yüklendiğinde yapılır)
        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    # _splashscreen etiketini poplayın, burada _confirm_quit False ve diğer şeyler var
    $ renpy.pop_call()
    jump expression persistent.autoload

label before_main_menu:
    #$ persistent.opening_scene = False
    if persistent.opening_scene is False: # açılış sahnesi yoksa, göster
        #$ persistent.opening_scene = False
        call ch_opening
        $ persistent.opening_scene = True
        $ persistent.playername = ""
        $ persistent.autoload = ""

    $ config.name = "Doki Doki Edebiyat Kulübü - Purist"

    if persistent.opening_scene is True:
        $ config.main_menu_music = audio.titleTheme
    else:
        $ config.main_menu_music = audio.t1
        
    $ config.main_menu_music = audio.titleTheme
    $ config.developer = True
    $ config.console = True
    #$ renpy.music.play(config.main_menu_music)
    return

label quit:
    return
