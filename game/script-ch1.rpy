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
    n "Hangi insanlar {i}did{/i}, bu arada."
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
    y 2r "Maybe you're just jealous that [player] appreciates my advice more than he appreciated yours!"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1e "Huh! And how do you know he didn't appreciate {i}my{/i} advice more?"
    n "Are you that full of yourself?"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 3h "I...!"
    y "No..."
    y "If I was full of myself..."
    y 1r "...I would deliberately go out of my way to make everything I do overly cutesy!"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1o "Uuuuuu...!"
    show sayori 2l at l41 behind yuri,natsuki
    show yuri at t32 zorder 2
    show natsuki at t33 zorder 2
    s "U-Um!!"
    s "Is everyone okay...?"
    show sayori 2 at lhide
    hide sayori
    show natsuki at f33 zorder 3
    n 1f "Well, you know what?!"
    n "I wasn't the one whose boobs magically grew a size bigger as soon as [player] started showing up!!"
    show yuri 3p at h32
    show natsuki at t33 zorder 2
    y "N-Natsuki!!"
    show monika 3l at l41 behind yuri,natsuki
    m "Um, Natsuki, that's a little--"
    show monika at h41
    show yuri 3p at f32 zorder 3
    show natsuki 1e at f33 zorder 3
    ny "This doesn't involve you!"
    show monika at lhide
    hide monika
    show yuri at t32 zorder 2
    show natsuki at t33 zorder 2
    show sayori 4p at l41 behind yuri,natsuki
    s "I-I don't like fighting, guys...!"
    show sayori at lhide
    hide sayori
    show yuri at t21 zorder 2
    show natsuki 1g at t22 zorder 2
    "Suddenly, both girls turn towards me, as if they just noticed I was standing there."
    show yuri at f21 zorder 3
    y 2n "[player]...!"
    y "She-- She's just trying to make me look bad...!"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 4w "That's not true!"
    n "She started it!"
    n 4e "If she could get over herself and learn to appreciate that {i}simple{/i} writing is more effective..."
    n "Then this wouldn't have happened in the first place!"
    n "What's the point in making your poems all convoluted for no reason?"
    n "The meaning should jump out at the reader, not force them to have to figure it out."
    n 1f "Help me explain that to her, [player]!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 3o "W-Wait!"
    y "There's a reason we have so many deep and expressive words in our language!"
    y 3w "It's the only way to convey complex feelings and meaning the most effectively."
    y "Avoiding them is not only unnecessarily limiting yourself...it's also a waste!"
    y 1t "You understand that, right, [player]?"
    show yuri at t21 zorder 2
    mc "Um...!"
    show yuri 1t at f21 zorder 3
    show natsuki 1e at f22 zorder 3
    ny "Well??"
    mc "..."
    show yuri at t21 zorder 2
    show natsuki 1g at t22 zorder 2
    "How did I get dragged into this in the first place?!"
    "It's not like I know anything about writing..."
    "But whomever I agree with, they'll probably think more highly of me!"
    menu:
        "So, of course that's going to be...!"
        "Natsuki.":
            call ch1_end_natsuki
        "Yuri.":
            call ch1_end_yuri
        "Help me, Sayori!!":
            call ch1_end_sayori

    scene bg club_day
    show monika 4b at t11 zorder 2
    with wipeleft_scene
    m "Okay, everyone!"
    m "It's just about time for us to leave."
    m "How did you all feel about sharing poems?"
    show monika 4a
    show sayori 4x at t31 zorder 2
    s "It was a lot of fun!"
    show sayori at thide behind yuri
    show yuri 1i at t31 zorder 2
    hide sayori
    y "Well, I'd say it was worth it."
    show yuri at thide behind natsuki
    show natsuki 4q at t31 zorder 2
    hide yuri
    n "It was alright. Well, mostly."
    show natsuki at thide zorder 1
    hide natsuki
    m 1a "[player], how about you?"
    mc "...Yeah, I'd say the same."
    mc "It was a neat thing to talk about with everyone."
    m 1j "Awesome!"
    m 1a "In that case, we'll do the same thing tomorrow."
    m "And maybe you learned something from your friends, too."
    m 3b "So your poems will turn out even better!"
    mc "..."
    show monika at thide zorder 1
    hide monika
    "I think to myself."
    "I did learn a little more about the kinds of poems everyone likes."
    "With any luck, that means I can at least do a better job impressing those I want to impress."
    "I nod to myself with newfound determination."
    show sayori 1x at t11 zorder 2
    s "[player]!"
    s "Ready to walk home?"
    mc "Sure, let's go."
    s 4q "Ehehe~"
    "Sayori beams at me."
    "It truly has been a while since Sayori and I have spent this much time together."
    "I can't really say I'm not enjoying it, either."
    scene bg residential_day
    show sayori 1a at t11 zorder 2
    with wipeleft_scene
    mc "Sayori..."
    mc "About what happened earlier..."
    s 1b "Eh? What do you mean?"
    mc "You know, between Yuri and Natsuki."
    mc "Does that kind of thing happen often?"
    s 4j "No, no, no!"
    s "That's really the first time I've seen them fight like that..."
    s "I promise they're both wonderful people."
    show sayori at s11
    s 1g "You don't... You don't hate them, do you??"
    mc "No, I don't hate them!"
    mc "I just wanted your opinion, that's all."
    mc "I can see why they'd make good friends with you."
    show sayori at t11 zorder 2
    s 1d "Phew..."
    s "You know, [player]..."
    s "It's nice that I get to spend time with you in the club."
    s "But I think seeing you get along with everyone is what makes me the happiest."
    s 1x "And I think everyone really likes you, too!"
    mc "That's--!"
    s 4q "Ehehe~"
    s "Every day is going to be so much fun~"
    mc "Sigh..."
    "It looks like Sayori still hasn't caught onto the kind of situation I'm in."
    "Sure, being friends with everyone is nice, but..."
    "...Does it really need to stop there?"
    mc "We'll just have to see what the future holds, Sayori."
    "I pat Sayori on the shoulder."
    "I said that more to myself than to her, but it's easy to use Sayori as an internal monologue sometimes."
    show sayori at h11
    s 1x "Okay~!"
    "Yeah..."
    "Let's do this!"
    return

label ch1_end_natsuki:
    $ ch1_choice = "natsuki"
    stop music fadeout 1.0
    mc "Um..."
    mc "Yuri!"
    mc "You're really talented."
    show yuri 4a at s21
    y "Eh? W-Well..."
    play music t8
    mc "But Natsuki has a point!"
    mc "I think that..."
    show yuri at t21 zorder 2
    "I wrack my brain in an attempt to back myself up."
    mc "I think that conveying feelings with few words..."
    mc "Can be just as impressive as well!"
    mc "It lets the reader's imagination take over."
    mc "And Natsuki's poem did a really good job at that!"
    show natsuki at f22 zorder 3
    n 5y "...Yeah!!"
    n "It did, didn't it?!"
    n "Ahah!"
    n "Shows how much {i}you{/i} know!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 4b "T-That's not..."
    show yuri at t21 zorder 2
    mc "Natsuki..."
    mc "I think that's enough."
    show natsuki at f22 zorder 3
    n 1m "Huh?"
    n "Me?"
    n "But she was so mean to me...!"
    "Natsuki's voice whines."
    show natsuki at t22 zorder 2
    mc "Look..."
    mc "What we talked about yesterday was right."
    mc "Writing is a really personal thing."
    mc "And sharing it can definitely be hard."
    mc "It looks like we learned that today."
    mc "Even small criticism can lead to something pretty heated."
    "I glance over my shoulder."
    "Sayori is nodding vigorously."
    mc "Yeah, so..."
    mc "You don't need to feel threatened."
    mc "You're a great writer, Natsuki."
    show natsuki at f22 zorder 3
    n 1h "Ah--"
    "Natsuki's voice gets caught in surprise."
    n 1q "...Thanks for noticing."
    "She finally mutters that, barely audible."
    show natsuki at t22 zorder 2
    mc "Yuri..."
    show yuri at f21 zorder 3
    y 4a "...?"
    "Yuri looks at me dejectedly."
    "With a face like that, I can't help but feel bad for her as well."
    show yuri at t21 zorder 2
    mc "I'm sure that Natsuki didn't mean everything she said."
    mc "So you don't need to feel threatened, either."
    show yuri at f21 zorder 3
    y 2v "Well..."
    y "If you say so..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1g "Hey...!"
    n "It's not like you need to apologize {i}for{/i} me, [player]."
    n 1w "Sheesh."
    "Natsuki takes a breath."
    n 1q "I..."
    n "The thing about..."
    n "Uu..."
    "Natsuki glances around the room."
    show natsuki at hf22 zorder 3
    n 1x "{i}Would everyone stop staring at me??{/i}"
    "Unsurprisingly, Natsuki has a harder time with it than she boasted."
    "Sayori and Monika look away."
    show natsuki at f22 zorder 3
    n 1i "Hmph."
    n "Anyway...!"
    n 1q "The thing about your boobs. I didn't mean it, okay?"
    n "That's all."
    "Natsuki looks away, avoiding eye contact with anyone."
    show natsuki at t22 zorder 2
    show sayori 4x at l41 behind yuri
    s "Yeah! You're naturally beautiful, Yuri!!"
    mc "Sayori?!"
    show yuri 4c at f21 zorder 3
    y "..."
    y "I-I'll go make some tea..."
    show yuri at lhide
    hide yuri
    show sayori at f41 zorder 3
    s 4h "Ehh?"
    s "I was just trying to help!"
    show sayori at t41 zorder 2
    mc "I'm sure she appreciated it, Sayori."
    "I pat Sayori on the shoulder."
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    show monika 4m at t11 zorder 2
    hide sayori
    hide natsuki
    m "Well, now that we're past that..."
    m 4b "Everyone's read each other's poems, right?"
    m "I hope that it was worthwhile for everyone!"
    m 5 "Especially you, [player]!"
    m "And to be honest..."
    m "It's a nice change of pace from the lazing around we got a little too used to."
    m "Ahahaha!"
    mc "Ah, so my joining the club was responsible for ruining the atmosphere..."
    m 1d "No, not at all, not at all!"
    m "There's still time before we go home."
    m 1a "So we'll all relax for a bit."
    m "Of course, besides chatting, we do literature-related things in the clubroom..."
    m "So maybe you can take the chance to pick up a book, or do some writing."
    m 1b "After all, that's what the club is for!"
    show sayori 2j at f31 zorder 3
    s "I disagree, Monika!"
    show sayori at t31 zorder 2
    show monika at f32 zorder 3
    m 1d "Eh? About what?"
    show monika at t32 zorder 2
    show sayori at f31 zorder 3
    s 2i "That's not the most important thing about the literature club!"
    s "The most important thing..."
    show sayori 4r at hf31 zorder 3
    s "Is having fun!"
    show sayori at t31 zorder 2
    show monika at f32 zorder 3
    m 2l "Ahaha, of course..."
    m 2a "Well, I guess that's why you're the Vice President, Sayori."
    show monika at t32 zorder 2
    show sayori at f31 zorder 3
    s 4q "Ehehe..."
    hide sayori
    hide monika
    with wipeleft
    "In the end, though, Monika's right."
    "Being in the Literature Club probably means I can't spend all my time doing nothing."
    "But in the end..."
    "...I guess it's been worth it so far."
    return
    
label ch1_end_yuri:
    $ ch1_choice = "yuri"
    stop music fadeout 1.0
    mc "Natsuki."
    mc "You're right that I liked your poem."
    show natsuki at f22 zorder 3
    n 1e "See??"
    show natsuki 1g at t22 zorder 2
    play music t8
    mc "Wait!"
    mc "That's not an excuse for you to be so mean!"
    mc "You shouldn't pick a fight just because someone's opinion is different."
    show natsuki at f22 zorder 3
    n 1m "That's not what happened at all!"
    n "Yuri wouldn't even take my poem seriously!"
    show natsuki at t22 zorder 2
    mc "Mm..."
    mc "I understand."
    mc "Yuri."
    show yuri at f21 zorder 3
    y 2t "Eh?"
    show yuri at t21 zorder 2
    mc "You're a seriously talented writer."
    mc "It's no secret that I was impressed."
    show yuri at f21 zorder 3
    y 2u "W-Well, that's..."
    show yuri at t21 zorder 2
    mc "But here's the thing."
    mc "No matter how simple or refined someone's writing style is..."
    mc "They're still putting feelings into it, and it becomes something really personal."
    mc "That's why Natsuki felt threatened when you said her poem was cute."
    show yuri at f21 zorder 3
    y 2v "I...see..."
    y "I didn't notice that I..."
    show yuri at t21 zorder 2
    y 2w "I-I'm sorry..."
    show yuri at s21
    y "Uuu..."
    show natsuki at t11 zorder 2
    show yuri at thide zorder 1
    hide yuri
    mc "But Natsuki, you took it way too far!"
    mc "Yuri means well, and if you just told her how you felt..."
    mc "Then this wouldn't have happened in the first place."
    n 1e "Are you kidding?"
    n "That's exactly what I did!"
    n "It was {i}her{/i} that--"
    show natsuki at t22 zorder 2
    show monika 2i at f21 zorder 3
    m "Natsuki, I think that's enough."
    m "You both said some things that you didn't mean."
    m "Yuri apologized. Don't you think you should, too?"
    show monika at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1x "Nnn...!"
    show natsuki at t22 zorder 2
    "Natsuki clenches her fists."
    "In the end, nobody has taken her side."
    "She's trapped, at this point being defiant only because she can't handle the pressure."
    "I end up even feeling bad for her."
    show monika at t32 zorder 2
    show natsuki at t33 zorder 2
    show sayori 2h at l41
    s "U-Um!"
    s "Sometimes when I'm hurt..."
    s "It helps to take a walk and clear my head!"
    show sayori at t41 zorder 2
    mc "Sayori, she doesn't need to--"
    show natsuki at f33 zorder 3
    n 2q "You know what?"
    n "I'm going to do that."
    n 2w "It'll spare me from having to look at all your faces right now."
    show natsuki at thide zorder 1
    hide natsuki
    "Without warning, Natsuki snatches her own poem up from the desk and storms out."
    "On her way out, she crumples up the poem with her hands and throws it in the trash."
    show sayori at f41 zorder 3
    s 1k "Natsuki..."
    show sayori at t41 zorder 2
    show monika at f32 zorder 3
    m 1r "She really didn't need to do that..."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    hide sayori
    hide monika
    "I look across the room."
    "Yuri has her chin buried in her hands while she stares down at her desk."
    "I gingerly approach her and sit in an adjacent chair."
    show yuri 4b at t11 zorder 2
    y "Sigh..."
    mc "Everything alright?"
    y "I'm so embarrassed..."
    y "I can't believe I acted like that."
    y "You probably hate me now..."
    mc "No--Yuri!"
    mc "How could anyone not have gotten frustrated after being treated like that?"
    mc "You handled it as well as anyone could."
    mc "I don't think any less of you."
    y 2v "Well..."
    y "...Alright, I believe you."
    y 2s "Thanks, [player]. You're too kind."
    y "I'm thankful to have you a part of this club now."
    mc "Er-- It's nothing."
    y 2v "One more thing..."
    y "Um, that one thing that Natsuki said..."
    y 4c "About...you know..."
    y "I would never do anything...so shameful..."
    y "So..."
    mc "...Eh?"
    mc "What thing did Natsuki say?"
    y 3n "--!"
    y "U-Um!"
    y 3q "Well, never mind that..."
    y "I-I'm going to go make some tea..."
    mc "Ah, good idea."
    mc "Make enough for more than one person, okay?"
    y "Y-Yeah."
    return

label ch1_end_sayori:
    $ ch1_choice = "sayori"
    mc "N-Natsuki..."
    show natsuki 5f
    "Natsuki glares at me, drying up any words I had in my mouth."
    "So instead, I turn to Yuri."
    mc "Yuri..."
    y 4a "..."
    "But Yuri's expression is so defenseless that I can't bring myself to say anything to her."
    stop music fadeout 1.0
    mc "..."
    mc "...Sayori!"
    show sayori 4m at l31 behind yuri
    show yuri at t32 zorder 2
    show natsuki at t33 zorder 2
    s "Eh?!"
    mc "...Yeah!"
    mc "Everyone's fighting is making Sayori uncomfortable."
    mc "How can the two of you keep fighting when you know you're making your friend feel like this?"
    show sayori at f31 zorder 3
    s 4d "[player]..."
    show sayori at t31 zorder 2
    show natsuki 4w at f33 zorder 3
    n "Well... That's her problem! This isn't about her."
    show natsuki at t33 zorder 2
    show yuri 2g at f32 zorder 3
    y "I-I agree..."
    y "It's unfair for others to interject their own feelings into our conflict."
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    n 4c "Yeah, unless Sayori wants to tell Yuri what a stuck-up jerk she's being."
    show natsuki at t33 zorder 2
    show yuri 3r at f32 zorder 3
    play music t7
    y "She would never...!"
    y "It's your immaturity that's made her upset in the first place!"
    show yuri at t32 zorder 2
    show natsuki 1e at f33 zorder 3
    n "{i}Excuse{/i} me?"
    n "Are you listening to yourself?"
    n 1x "This is exactly why..."
    n 1w "Exactly why nobody likes--"
    show natsuki at t33 zorder 2
    show sayori 4p at h31
    stop music
    s "{i}Stop!!{/i}"
    show yuri 3f at f32 zorder 3
    show natsuki 1o at f33 zorder 3
    ny "--"
    show yuri at t32 zorder 2
    show natsuki at t33 zorder 2
    show sayori at f31 zorder 3
    play music t8
    s 1h "Natsuki! Yuri!"
    s "You guys are my friends!"
    s 1v "I-I just want everyone to get along and be happy!"
    s "My friends are wonderful people..."
    s "And I love them because of their differences!"
    s 1g "Natsuki's poems..."
    s "They're amazing because they give you so many feelings with just a few words!"
    s "And Yuri's poems are amazing because they paint beautiful pictures in your head!"
    s 4k "Everyone's so talented..."
    s "...So why are we fighting...?"
    show sayori at t31 zorder 2
    show natsuki at f33 zorder 3
    n 1r "Be-Because..."
    show natsuki at t33 zorder 2
    show yuri 3v at f32 zorder 3
    y "Well..."
    show yuri at t32 zorder 2
    show sayori at f31 zorder 3
    s 1j "Also!"
    s "Natsuki's cute and there's nothing wrong with that!"
    s 1i "And Yuri's boobs are the same as they always were!"
    show sayori at hf31
    s 1j "Big and beautiful!!"
    show sayori 1i at t31 zorder 2
    show natsuki at f33 zorder 3
    n 1o "..."
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 3n "..."
    show yuri at t32 zorder 2
    mc "Sayori..."
    "Sayori stands triumphantly."
    "Monika stands behind her with a bewildered expression."
    show yuri at s32
    y 3q "I'll...make some tea..."
    show yuri at lhide behind sayori
    hide yuri
    "Yuri rushes off."
    show natsuki at thide zorder 1
    hide natsuki
    "Natsuki sits down with a blank expression on her face, staring at nothing."
    show sayori at thide zorder 1
    show monika 1i at t11 zorder 2
    hide sayori
    mc "So, this is why Sayori is Vice President..."
    "I whisper to Monika."
    "She nods in return."
    m 1d "To be honest..."
    m "I might come off as a good leader, and I can organize things..."
    m 3e "But I'm not very good with people..."
    m "I couldn't even bring myself to interject."
    m 1m "As President, that's kind of embarrassing of me."
    m 1l "Ahaha..."
    mc "Nah..."
    mc "It's not like I can blame you."
    mc "I wasn't able to say anything, either."
    m "Well..."
    m 2a "I guess that just means Sayori is amazing in her own ways, isn't she?"
    mc "You could say that."
    mc "She might be an airhead, but sometimes it's weirdly suspicious that she knows exactly what she's doing."
    m 5 "I see~"
    m "Take good care of her, okay?"
    m "I would hate to see her get herself hurt."
    mc "That makes two of us..."
    mc "You can count on me."
    "Monika smiles sweetly at me, causing my stomach to knot."
    "Such a genuine person really does make a good President, regardless of what she says."
    "If only I could get the chance to talk to her a little more..."
    return
