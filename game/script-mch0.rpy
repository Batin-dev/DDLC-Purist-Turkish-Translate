label mon_ch0_1:
    "Hep kendi kendime, artık dışarı çıkıp birkaç kızla tanışmam lazım diyordum."
    "Ama bak, zaten burada bir kız var."
    show sayori 1a at t11
    "O kız, çocukluktan beri yan komşum ve iyi arkadaşım olan Sayori."
    "Eskiden böyle günlerde beraber okula yürürdük."
    "Son zamanlarda bu alışkanlığı tekrar kazandık."
    $ s_name = "Sayori" 
    s "[player], benimle gurur duyuyor musun?"
    return

label mon_ch0_2:
    mc "Ha? Ne için?"
    s 1c "Biliyorsun işte..."
    s "Zamanında uyanabildiğim için!"
    mc "Ama bunu bir süredir yapıyorsun zaten."
    s "Evet ama..."
    s "Bunu hiç dile bile getirmedin!"
    show sayori at s11
    s "Oysa her gün beraber okula yürüyoruz..."
    mc "Şey... evet..."
    mc "Ama bunu söylemeye gerek yokmuş gibi düşündüm hep."
    mc "Bunu yüksek sesle söylemek biraz utanç verici."
    s 1d "Hadi ama, lütfen?"
    s "Bu benim için motivasyon olur."
    mc "Tamam, tamam..."
    mc "Seninle gurur duyuyorum, Sayori."
    show sayori at t11
    s 1q "Ehehe~"
    "Birlikte karşıdan karşıya geçip okula doğru yol alıyoruz."
    "Yaklaştıkça sokaklar kalabalıklaşmaya başlıyor."
    s 3a "Bu arada, [player]."
    s "Hangi kulübe katılacağına karar verdin mi?"
    mc "Evet, verdim."
    s 4m "Ooooh, hadi söyle!"
    return

label mon_ch0_3:
    mc "Sürpriz."
    s 2f "Aww..."
    mc "Okul çıkışı söylerim."
    s 1q "Tamam ama söz verdin!"
    "Bunu söylemek biraz garip aslında."
    "Eskiden kızlarla tanışmak istediğimi düşünürdüm..."
    "Ama son zamanlarda, bu duygu biraz değişti."
    "Sanki kaderimdeki kişiyle tanışmam an meselesiymiş gibi hissediyorum."
    "Her şey Edebiyat Kulübü için gördüğüm bir ilanla başladı."
    "Edebiyata özel bir ilgim yoktu ama içimden bir şey beni oraya çekti."
    "Gerçekten garip."
    "Bugün kulüpler yeni üye almaya başlayacak, o yüzden cesaretimi toplamaya çalışıyorum."
    scene bg class_day with wipeleft_scene
    "Okul günü her zamanki kadar sıradan geçiyor ve göz açıp kapayıncaya kadar sona eriyor."
    "Bugün odaklanmaya çalıştım ama Edebiyat Kulübü'ne gitme düşüncesi nedense beni biraz gergin yaptı."
    "Belki biraz dinlenip sakinleşmeliyim."
    return
