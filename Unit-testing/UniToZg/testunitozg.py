import unittest
import uni2zg

class TestZG2UNI(unittest.TestCase):
#     def test_myanmar_consonants(self):
#         zawgyi = u'''ကခဂငစဆဇည ဋဌဍ ဏတထဒဓနပဖဗဘမ ယရလ၀သဟ ဠအ'''
#         unicode = u'''ကခဂငစဆဇည ဋဌဍ ဏတထဒဓနပဖဗဘမ ယရလ၀သဟ ဠအ'''
#         result = uni2zg.convert(unicode)
#         self.assertEqual(zawgyi, result, "Failed converting Article Consonants")
# #
    def test_article_one(self):
        zawgyi = u'''လူတိုင္းသည္ တူညီ လြတ္လပ္ေသာ ဂုဏ္သိကၡာျဖင့္ လည္းေကာင္း၊ တူညီလြတ္လပ္ေသာ အခြင့္အေရးမ်ားျဖင့္ လည္းေကာင္း၊ ေမြးဖြားလာသူမ်ား ျဖစ္သည္။
        ထိုသူတို႔၌ ပိုင္းျခား ေဝဖန္တတ္ေသာ ဉာဏ္ႏွင့္ က်င့္ဝတ္ သိတတ္ေသာ စိတ္တို႔႐ွိၾက၍ ထိုသူတို႔သည္ အခ်င္းခ်င္း ေမတၱာထား၍ ဆက္ဆံက်င့္သုံးသင့္၏။
'''
        unicode = u'''လူတိုင်းသည် တူညီ လွတ်လပ်သော ဂုဏ်သိက္ခာဖြင့် လည်းကောင်း၊ တူညီလွတ်လပ်သော အခွင့်အရေးများဖြင့် လည်းကောင်း၊ မွေးဖွားလာသူများ ဖြစ်သည်။
        ထိုသူတို့၌ ပိုင်းခြား ဝေဖန်တတ်သော ဉာဏ်နှင့် ကျင့်ဝတ် သိတတ်သော စိတ်တို့ရှိကြ၍ ထိုသူတို့သည် အချင်းချင်း မေတ္တာထား၍ ဆက်ဆံကျင့်သုံးသင့်၏။
'''
        result = uni2zg.convert(unicode)
        self.assertEqual(zawgyi, result, "Failed converting Article One")
#
#     def test_article_two(self):
#         zawgyi = u'''လူတိုင္းသည္ လူ႔အခြင့္ အေရး ေၾကညာစာတမ္းတြင္ ေဖာ္ျပထားသည့္ အခြင့္အေရး အားလုံး၊ လြတ္လပ္ခြင့္ အားလုံးတို႔ကို ပိုင္ဆိုင္ ခံစားခြင့္ရွိသည္။
#                      လူမ်ိဳးႏြယ္အားျဖင့္ ျဖစ္ေစ၊ အသားအေရာင္အားျဖင့္ ျဖစ္ေစ၊ က်ား၊ မ၊ သဘာဝအားျဖင့္ ျဖစ္ေစ၊ ဘာသာစကားအားျဖင့္ ျဖစ္ေစ၊ ကိုးကြယ္သည့္ ဘာသာအားျဖင့္ ျဖစ္ေစ၊
#                       နိုင္ငံေရးယူဆခ်က္၊ သို႔တည္းမဟုတ္ အျခားယူဆခ်က္အားျဖင့္ ျဖစ္ေစ၊ နိုင္ငံႏွင့္ ဆိုင္ေသာ၊ သို႔တည္းမဟုတ္ လူမွုအဆင့္အတန္းႏွင့္ ဆိုင္ေသာ ဇစ္ျမစ္ အားျဖင့္ျဖစ္ေစ၊
#                        ပစၥည္း ဥစၥာ ဂုဏ္အားျဖင့္ ျဖစ္ေစ၊ မ်ိဳးရိုးဇာတိအားျဖင့္ ျဖစ္ေစ၊ အျခား အဆင့္အတန္း အားျဖင့္ ျဖစ္ေစ ခြဲျခားျခင္းမရွိေစရ။
#                         ထို႔ျပင္ လူတစ္ဦး တစ္ေယာက္ ေနထိုင္ရာ နိုင္ငံ၏ သို႔တည္းမဟုတ္ နယ္ေျမေဒသ၏ နိုင္ငံေရးဆိုင္ရာ ျဖစ္ေစ စီရင္ပိုင္ခြင့္ဆိုင္ရာ ျဖစ္ေစ တိုင္းျပည္ အခ်င္းခ်င္း ဆိုင္ရာျဖစ္ေစ၊
#                          အဆင့္အတန္း တစ္ခုခုကို အေျချပဳ၍ ေသာ္လည္းေကာင္း၊ ေဒသနယ္ေျမတစ္ခုသည္ အခ်ဳပ္အျခာ အာဏာပိုင္ လြတ္လပ္သည့္ နယ္ေျမ၊ သို႔တည္းမဟုတ္ ကုလသမဂၢ ထိန္းသိမ္း ေစာင့္ေရွာက္ ထားရသည့္ နယ္ေျမ၊
#                           သို႔တည္းမဟုတ္ ကိုယ္ပိုင္ အုပ္ခ်ဳပ္ခြင့္ အာဏာတို႔ တစိတ္တေဒသေလာက္သာ ရရွိသည့္ နယ္ေၿမ စသျဖင့္ ယင္းသို႔ ေသာ နယ္ေျမမ်ား ျဖစ္သည္ ဟူေသာ အေၾကာင္းကို အေထာက္အထား ျပဳ၍ ေသာ္လည္းေကာင္း ခြဲျခားျခင္း လုံးဝ မရွိေစရ။
#     '''
#         unicode = u'''လူတိုင်းသည် လူ့အခွင့် အရေး ကြေညာစာတမ်းတွင် ဖော်ပြထားသည့် အခွင့်အရေး အားလုံး၊ လွတ်လပ်ခွင့် အားလုံးတို့ကို ပိုင်ဆိုင် ခံစားခွင့်ရှိသည်။
#                      လူမျိုးနွယ်အားဖြင့် ဖြစ်စေ၊ အသားအရောင်အားဖြင့် ဖြစ်စေ၊ ကျား၊ မ၊ သဘာဝအားဖြင့် ဖြစ်စေ၊ ဘာသာစကားအားဖြင့် ဖြစ်စေ၊ ကိုးကွယ်သည့် ဘာသာအားဖြင့် ဖြစ်စေ၊
#                       နိုင်ငံရေးယူဆချက်၊ သို့တည်းမဟုတ် အခြားယူဆချက်အားဖြင့် ဖြစ်စေ၊ နိုင်ငံနှင့် ဆိုင်သော၊ သို့တည်းမဟုတ် လူမှုအဆင့်အတန်းနှင့် ဆိုင်သော ဇစ်မြစ် အားဖြင့်ဖြစ်စေ၊
#                        ပစ္စည်း ဥစ္စာ ဂုဏ်အားဖြင့် ဖြစ်စေ၊ မျိုးရိုးဇာတိအားဖြင့် ဖြစ်စေ၊ အခြား အဆင့်အတန်း အားဖြင့် ဖြစ်စေ ခွဲခြားခြင်းမရှိစေရ။
#                         ထို့ပြင် လူတစ်ဦး တစ်ယောက် နေထိုင်ရာ နိုင်ငံ၏ သို့တည်းမဟုတ် နယ်မြေဒေသ၏ နိုင်ငံရေးဆိုင်ရာ ဖြစ်စေ စီရင်ပိုင်ခွင့်ဆိုင်ရာ ဖြစ်စေ တိုင်းပြည် အချင်းချင်း ဆိုင်ရာဖြစ်စေ၊
#                          အဆင့်အတန်း တစ်ခုခုကို အခြေပြု၍ သော်လည်းကောင်း၊ ဒေသနယ်မြေတစ်ခုသည် အချုပ်အခြာ အာဏာပိုင် လွတ်လပ်သည့် နယ်မြေ၊ သို့တည်းမဟုတ် ကုလသမဂ္ဂ ထိန်းသိမ်း စောင့်ရှောက် ထားရသည့် နယ်မြေ၊
#                           သို့တည်းမဟုတ် ကိုယ်ပိုင် အုပ်ချုပ်ခွင့် အာဏာတို့ တစိတ်တဒေသလောက်သာ ရရှိသည့် နယ်မြေ စသဖြင့် ယင်းသို့ သော နယ်မြေများ ဖြစ်သည် ဟူသော အကြောင်းကို အထောက်အထား ပြု၍ သော်လည်းကောင်း ခွဲခြားခြင်း လုံးဝ မရှိစေရ။
#     '''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed converting Article Two")
#
    # def test_article_three(self):
    #     zawgyi = u'''လူတိုင္း၌ အသက္႐ွင္ရန္ လြတ္လပ္မႈခြင့္ႏွင့္ လုံျခဳံစိတ္ခ်ခြင့္ ႐ွိသည္။'''
    #     unicode = u'''လူတိုင်း၌ အသက်ရှင်ရန် လွတ်လပ်မှုခွင့်နှင့် လုံခြုံစိတ်ချခွင့် ရှိသည်။'''
    #     result = uni2zg.convert(unicode)
    #     self.assertEqual(zawgyi, result, "Failed converting Article Three")

    # def test_article_four(self):
    #     zawgyi = u'''မည္သူကိုမၽွ ေက်းကၽြန္အျဖစ္၊ သို႔တည္းမဟုတ္ အေစအပါးအျဖစ္၊ နိုင္ထက္စီးနင္း ေစခိုင္းျခင္းမျပဳရ၊လူကို ေက်းကၽြန္သဖြယ္ အဓမၼ ေစခိုင္းျခင္း၊ အေရာင္းအဝယ္ ျပဳျခင္းႏွင့္ ထိုသေဘာ သက္ေရာက္ေသာ လုပ္ငန္းဟူသမၽွကို ပိတ္ပင္ တားျမစ္ ရမည္။'''
    #     unicode = u'''မည်သူကိုမျှ ကျေးကျွန်အဖြစ်၊ သို့တည်းမဟုတ် အစေအပါးအဖြစ်၊ နိုင်ထက်စီးနင်း စေခိုင်းခြင်း မပြုရ၊လူကို ကျေးကျွန်သဖွယ် အဓမ္မ စေခိုင်းခြင်း၊ အရောင်းအဝယ် ပြုခြင်းနှင့် ထိုသဘော သက်ရောက်သော လုပ်ငန်းဟူသမျှကို ပိတ်ပင် တားမြစ် ရမည်။'''
    #     result = uni2zg.convert(unicode)
    #     self.assertEqual(zawgyi, result, "Failed converting Article Four")

    # def test_article_five(self):
    #     zawgyi = u'''မည္သူကိုမၽွ ညႇဥ္းပန္း ႏွိပ္စက္ျခင္း၊ သို႔တည္းမဟုတ္ ရက္စက္ၾကမ္းၾကဳတ္စြာ လူမဆန္စြာ ဂုဏ္ငယ္ေစေသာ ဆက္ဆံမွု မျပဳရ၊ သို႔တည္းမဟုတ္ အျပစ္ဒဏ္ ေပးျခင္းမျပဳရ။'''
    #     unicode = u'''မည်သူကိုမျှ ညှဉ်းပန်း နှိပ်စက်ခြင်း၊ သို့တည်းမဟုတ် ရက်စက်ကြမ်းကြုတ်စွာ လူမဆန်စွာ ဂုဏ်ငယ်စေသော ဆက်ဆံမှု မပြုရ၊ သို့တည်းမဟုတ် အပြစ်ဒဏ် ပေးခြင်းမပြုရ။'''
    #     result = uni2zg.convert(unicode)
    #     self.assertEqual(zawgyi, result, "Failed to Convert Article Five")

    def test_article_six(self):
        zawgyi = u'''လူတိုင္းတြင္ ဥပေဒအရာ၌ လူပုဂၢိဳလ္တစ္ဦး အျဖစ္ျဖင့္ အရာခပ္သိမ္းတြင္ အသိအမွတ္ ျပဳျခင္းကို ခံယူပိုင္ခြင့္႐ွိသည္။'''
        unicode = u'''လူတိုင်းတွင် ဥပဒေအရာ၌ လူပုဂ္ဂိုလ်တစ်ဦး အဖြစ်ဖြင့် အရာခပ်သိမ်းတွင် အသိအမှတ် ပြုခြင်းကို ခံယူပိုင်ခွင့်ရှိသည်။'''
        result = uni2zg.convert(unicode)
        self.assertEqual(zawgyi, result, "Failed converting Article Six")

    # def test_article_seaven(self):
    #     zawgyi = u'''လူအားလုံးတို႔သည္ ဥပေဒအရာ၌ တူညီၾကသည့္အျပင္၊ ဥပေဒ၏ အကာအကြယ္ကို ျခားနားျခင္း မခံရေစဘဲ တူညီစြာ ခံစားပိုင္ခြင့္႐ွိသည္။
    #     ဤေၾကညာ စာတမ္းပါ သေဘာတရားမ်ားကို ဖီဆန္၍ ခြဲျခားျခင္းမွ လည္းေကာင္း၊ထိုသို႔ခြဲျခားျခင္းကို ားျခင္းကို လႈံ႔ေဆာ္ျခင္းမွ လည္းေကာင္း။'''
    #     unicode = u'''လူအားလုံးတို့သည် ဥပဒေအရာ၌ တူညီကြသည့်အပြင်၊ ဥပဒေ၏ အကာအကွယ်ကို ခြားနားခြင်း မခံရစေဘဲ တူညီစွာ ခံစားပိုင်ခွင့်ရှိသည်။
    #     ဤကြေညာ စာတမ်းပါ သဘောတရားများကို ဖီဆန်၍ ခွဲခြားခြင်းမှ လည်းကောင်း၊ထိုသို့ခွဲခြားခြင်းကို လှုံ့ဆော်ခြင်းမှ လည်းကောင်း၊'''
    #     result = uni2zg.convert(unicode)
    #     self.assertEqual(zawgyi, result, "Failed converting Article Seaven")

#     def test_article_eight(self):
#         zawgyi = u'''ဖြဲ႕စည္းပုံ အေျခခံဥပေဒက ေသာ္လည္းေကာင္း အျခား ဥပေဒက ေသာ္လည္းေကာင္း လူတိုင္းအတြက္ ေပးထားသည့္
#          အေျခခံ အခြင့္အေရး မ်ားသည္ ခ်ိဳးေဖာက္ ဖ်က္ဆီးျခင္းခံခဲ့ရလၽွင္ ထိုသို႔ ခ်ိဳးေဖာက္ဖ်က္ဆီး ေသာ ျပဳလုပ္မွုေၾကာင့္ ျဖစ္ေပၚလာေသာ နစ္နာခ်က္ အတြက္
#           ထိုသူသည္ နိုင္ငံဆိုင္ရာ အာဏာပိုင္တရား႐ုံးတြင္ ထိေရာက္စြာ သက္သာခြင့္ ရွိနိုင္ေစရမည္။
# '''
#         unicode = u'''ဖွဲ့စည်းပုံ အခြေခံဥပဒေက သော်လည်းကောင်း အခြား ဥပဒေက သော်လည်းကောင်း လူတိုင်းအတွက် ပေးထားသည့်
#          အခြေခံ အခွင့်အရေး များသည် ချိုးဖောက် ဖျက်ဆီးခြင်းခံခဲ့ရလျှင် ထိုသို့ ချိုးဖောက်ဖျက်ဆီး သော ပြုလုပ်မှုကြောင့် ဖြစ်ပေါ်လာသော နစ်နာချက် အတွက်
#           ထိုသူသည် နိုင်ငံဆိုင်ရာ အာဏာပိုင်တရားရုံးတွင် ထိရောက်စွာ သက်သာခွင့် ရှိနိုင်စေရမည်။
# '''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed converting Article Eight")
#
    def test_article_nine(self):
        zawgyi = u'''မည္သူမၽွ ဥပေဒအရ မဟုတ္ေသာ ဖမ္းဆီးျခင္းကို ျဖစ္ေစ၊ ခ်ဳပ္ေႏွာင္ျခင္းကို ျဖစ္ေစ၊ ျပည္ႏွင္ျခင္းကိုျဖစ္ေစ မခံေစရ။
'''
        unicode = u'''မည်သူမျှ ဥပဒေအရ မဟုတ်သော ဖမ်းဆီးခြင်းကို ဖြစ်စေ၊ ချုပ်နှောင်ခြင်းကို ဖြစ်စေ၊ ပြည်နှင်ခြင်းကိုဖြစ်စေ မခံစေရ။
'''
        result = uni2zg.convert(unicode)
        self.assertEqual(zawgyi, result, "Failed converting Article Nine")
#
#
#     def test_article_ten(self):
#         zawgyi = u'''အခြင့္အေရးမ်ားႏွင့္ တာဝန္ ဝတၱရားမ်ားကို အဆုံးအျဖတ္ခံရာတြင္ လည္းေကာင္း၊ ျပစ္မွုေၾကာင့္ တရားစြဲဆို စီရင္ ဆုံးျဖတ္ခံရာတြင္ လည္းေကာင္း၊
#          လူတိုင္းသည္ လြတ္လပ္၍ ဘက္မလိုက္ေသာ တရား႐ုံးေတာ္၏ လူအမ်ား ေရွ႕ေမွာက္တြင္ မၽွတစြာ ၾကားနာစစ္ေဆးျခင္းကို တူညီစြာ ခံစား ပိုင္ခြင့္ရွိသည္။
# '''
#         unicode = u'''အခွင့်အရေးများနှင့် တာဝန် ဝတ္တရားများကို အဆုံးအဖြတ်ခံရာတွင် လည်းကောင်း၊ ပြစ်မှုကြောင့် တရားစွဲဆို စီရင် ဆုံးဖြတ်ခံရာတွင် လည်းကောင်း၊
#          လူတိုင်းသည် လွတ်လပ်၍ ဘက်မလိုက်သော တရားရုံးတော်၏ လူအများ ရှေ့မှောက်တွင် မျှတစွာ ကြားနာစစ်ဆေးခြင်းကို တူညီစွာ ခံစား ပိုင်ခွင့်ရှိသည်။
# '''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed converting Article Ten")
#
#     def test_article_eleven(self):
#         zawgyi = u'''အပိုဒ္ ၁၁
#            လူအမ်ား ေရွ႕ေမွာက္၌ ဥပေဒအတိုင္း စစ္ေဆး၍ ျပစ္မွုက်ဴးလြန္သည္ဟု ထင္ရွား စီရင္ျခင္းခံရသည့္ အခ်ိန္အထိ ျပစ္မွုႏွင့္
#            တရားစြဲဆိုျခင္း ခံရသူတိုင္းသည္ အျပစ္မဲ့သူဟူ၍ ယူဆ ျခင္းခံထိုက္သည့္ အခြင့္အေရးရွိသည္။ ထိုအမွုကို ၾကားနာစစ္ေဆးရာဝယ္
#            စြပ္စြဲခံရသည့္ ျပစ္မွုအတြက္ ခုခံေခ်ပနိုင္ရန္ လိုအပ္ေသာ အခြင့္အေရးမ်ားကို ထိုသူအား ေပးၿပီး ျဖစ္ေစရမည္။
#            လူတစ္ဦးတစ္ေယာက္အား နိုင္ငံဥပေဒအရျဖစ္ေစ၊ အျပည္ျပည္ဆိုင္ရာ ဥပေဒအရ ျဖစ္ေစ၊ ျပစ္မွုမေျမာက္ေသာ လုပ္ရပ္ သို႔မဟုတ္ ပ်က္ကြက္မွုအရ
#            ဆြဲဆိုျပစ္ေပးျခင္း မျပဳရ။ ထို႔အျပင္ ျပစ္မွုက်ဴးလြန္စဥ္အခါက ထိုက္သင့္ေစနိုင္ေသာ အျပစ္ဒဏ္ထက္ပိုမိုႀကီးေလးေသာ အျပစ္ဒဏ္ကို ထိုက္သင့္ျခင္းမရွိေစရ။'''
#         unicode = u'''အပိုဒ် ၁၁
#            လူအများ ရှေ့မှောက်၌ ဥပဒေအတိုင်း စစ်ဆေး၍ ပြစ်မှုကျူးလွန်သည်ဟု ထင်ရှား စီရင်ခြင်းခံရသည့် အချိန်အထိ ပြစ်မှုနှင့်
#            တရားစွဲဆိုခြင်း ခံရသူတိုင်းသည် အပြစ်မဲ့သူဟူ၍ ယူဆ ခြင်းခံထိုက်သည့် အခွင့်အရေးရှိသည်။ ထိုအမှုကို ကြားနာစစ်ဆေးရာဝယ်
#            စွပ်စွဲခံရသည့် ပြစ်မှုအတွက် ခုခံချေပနိုင်ရန် လိုအပ်သော အခွင့်အရေးများကို ထိုသူအား ပေးပြီး ဖြစ်စေရမည်။
#            လူတစ်ဦးတစ်ယောက်အား နိုင်ငံဥပဒေအရဖြစ်စေ၊ အပြည်ပြည်ဆိုင်ရာ ဥပဒေအရ ဖြစ်စေ၊ ပြစ်မှုမမြောက်သော လုပ်ရပ် သို့မဟုတ် ပျက်ကွက်မှုအရ
#            ဆွဲဆိုပြစ်ပေးခြင်း မပြုရ။ ထို့အပြင် ပြစ်မှုကျူးလွန်စဉ်အခါက ထိုက်သင့်စေနိုင်သော အပြစ်ဒဏ်ထက်ပိုမိုကြီးလေးသော အပြစ်ဒဏ်ကို ထိုက်သင့်ခြင်းမရှိစေရ။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed to Convert Article Eleven")
#
#     def test_article_twelve(self):
#         zawgyi = u'''မည္သူမၽွ မိမိသေဘာအတိုင္း ေအးခ်မ္းလြတ္လပ္စြာ ေနထိုင္ျခင္းကို ေသာ္လည္းေကာင္း၊ မိမိ၏ မိသားစုကို ေသာ္လည္းေကာင္း၊ မိမိ၏ ေနအိမ္ အသိုက္အဝန္းကို ေသာ္လည္းေကာင္း၊ စာေပးစာယူကို ေသာ္လည္းေကာင္း၊
#          ဥပေဒအရ မဟုတ္ေသာ ဝင္ေရာက္ စြက္ဖက္ျခင္း မခံေစရ။ ထို႔ျပင္ မိမိ၏ဂုဏ္သိကၡာ ကိုလည္း အထက္ပါ အတိုင္း ပုတ္ခတ္ျခင္း မခံေစရ။ လူတိုင္းတြင္ ထိုသို႔ ဝင္ေရာက္စြက္ဖက္ျခင္းမွ ေသာ္လည္းေကာင္း ပုတ္ခတ္ျခင္းမွ ေသာ္လည္းေကာင္း ဥပေဒအရ ကာကြယ္ ပိုင္ခြင့္ရွိသည္။
# '''
#         unicode = u'''မည်သူမျှ မိမိသဘောအတိုင်း အေးချမ်းလွတ်လပ်စွာ နေထိုင်ခြင်းကို သော်လည်းကောင်း၊ မိမိ၏ မိသားစုကို သော်လည်းကောင်း၊ မိမိ၏ နေအိမ် အသိုက်အဝန်းကို သော်လည်းကောင်း၊ စာပေးစာယူကို သော်လည်းကောင်း၊
#          ဥပဒေအရ မဟုတ်သော ဝင်ရောက် စွက်ဖက်ခြင်း မခံစေရ။ ထို့ပြင် မိမိ၏ဂုဏ်သိက္ခာ ကိုလည်း အထက်ပါ အတိုင်း ပုတ်ခတ်ခြင်း မခံစေရ။ လူတိုင်းတွင် ထိုသို့ ဝင်ရောက်စွက်ဖက်ခြင်းမှ သော်လည်းကောင်း ပုတ်ခတ်ခြင်းမှ သော်လည်းကောင်း ဥပဒေအရ ကာကွယ် ပိုင်ခွင့်ရှိသည်။
# '''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed converting Article Twelve")
#
#     def test_article_thirteen(self):
#         zawgyi = u'''လူတိုင္းတြင္ မိမိ၏နိုင္ငံ နယ္နိမိတ္ အတြင္း၌ လြတ္လပ္စြာ သြားလာ ေရႊ႕ေျပာင္း နိုင္ခြင့္၊ ေနထိုင္ခြင့္ရွိသည္။
# လူတိုင္းတြင္ မိမိေနထိုင္ရာ တိုင္းျပည္မွ လည္းေကာင္း၊ အျခားတိုင္းျပည္မွလည္းေကာင္း ထြက္ခြာ သြားပိုင္ခြင့္ရွိသည့္အျပင္၊မိမိ၏ တိုင္းျပည္သို႔ ျပန္လာ ပိုင္ခြင့္လည္းရွိသည္။
# '''
#         unicode = u'''လူတိုင်းတွင် မိမိ၏နိုင်ငံ နယ်နိမိတ် အတွင်း၌ လွတ်လပ်စွာ သွားလာ ရွှေ့ပြောင်း နိုင်ခွင့်၊ နေထိုင်ခွင့်ရှိသည်။
# လူတိုင်းတွင် မိမိနေထိုင်ရာ တိုင်းပြည်မှ လည်းကောင်း၊ အခြားတိုင်းပြည်မှလည်းကောင်း ထွက်ခွာ သွားပိုင်ခွင့်ရှိသည့်အပြင်၊မိမိ၏ တိုင်းပြည်သို့ ပြန်လာ ပိုင်ခွင့်လည်းရှိသည်။
# '''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed converting Article Thirteen")
#
#     def test_article_fourteen(self):
#         zawgyi = u'''လူတိုင္းသည္ ညႇဥ္းပန္း ႏွိပ္စက္ ခံေနရျခင္းမွ လြတ္ကင္းရန္ အျခားတိုင္းျပည္ မ်ား၌ ေအးခ်မ္းစြာ ခိုလွုံေနနိုင္ခြင့္ရွိသည္။
# နိုင္ငံေရးႏွင့္ မပတ္သက္သည့္ ျပစ္မွုမ်ားမွ ေသာ္လည္းေကာင္း၊ ကုလသမဂၢ၏ ရည္ရြက္ခ်က္ႏွင့္ သေဘာတရား မွုမ်ားကို ဖီဆန္ေသာ အမွုမ်ားမွ ေသာ္လညး္ေကာင္း၊
#  အမွန္ ေပၚေပါက္ လာေသာ ျပစ္မွုေၾကာင့္ တရားစြဲဆိုျခင္း ခံရသည့္ အမွုအခင္းမ်ားတြင္ အထက္ပါ အခြင့္အေရးကို အသုံးမျပဳနိုင္ေစရ။
# '''
#         unicode = u'''လူတိုင်းသည် ညှဉ်းပန်း နှိပ်စက် ခံနေရခြင်းမှ လွတ်ကင်းရန် အခြားတိုင်းပြည် များ၌ အေးချမ်းစွာ ခိုလှုံနေနိုင်ခွင့်ရှိသည်။
# နိုင်ငံရေးနှင့် မပတ်သက်သည့် ပြစ်မှုများမှ သော်လည်းကောင်း၊ ကုလသမဂ္ဂ၏ ရည်ရွက်ချက်နှင့် သဘောတရား မှုများကို ဖီဆန်သော အမှုများမှ သော်လညး်ကောင်း၊
#  အမှန် ပေါ်ပေါက် လာသော ပြစ်မှုကြောင့် တရားစွဲဆိုခြင်း ခံရသည့် အမှုအခင်းများတွင် အထက်ပါ အခွင့်အရေးကို အသုံးမပြုနိုင်စေရ။
# '''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed converting Article Fourteen")
#
#     def test_article_fifteen(self):
#         zawgyi = u'''လူတိုင္းသည္၊ နိုင္ငံ တစ္နိုင္ငံ၏ နိုင္ငံသားအျဖစ္ ခံယူခြင့္ရွိသည္။
#            ဥပေဒအရ မဟုတ္လၽွင္ မည္သူမၽွ မိမိ၏ နိုင္ငံသားအျဖစ္ကို စြန႔္လႊတ္ျခင္း မခံေစရ၊ နိုင္ငံသားအျဖစ္ ေျပာင္းလဲနိုင္ေသာအခြင့္အေရးကို လည္း ျငင္းပယ္ျခင္း မခံေစရ။'''
#         unicode = u'''လူတိုင်းသည်၊ နိုင်ငံ တစ်နိုင်ငံ၏ နိုင်ငံသားအဖြစ် ခံယူခွင့်ရှိသည်။
#            ဥပဒေအရ မဟုတ်လျှင် မည်သူမျှ မိမိ၏ နိုင်ငံသားအဖြစ်ကို စွန့်လွှတ်ခြင်း မခံစေရ၊ နိုင်ငံသားအဖြစ် ပြောင်းလဲနိုင်သောအခွင့်အရေးကို လည်း ငြင်းပယ်ခြင်း မခံစေရ။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed to Convert Article Fifteen")
#
#     def test_article_sixteen(self):
#         zawgyi = u'''အရြယ္ေရာက္ ၿပီးေသာ ေယာက်ာ္း ႏွင့္ မိန္းမတို႔တြင္ လူမ်ိဳးကို ေသာ္လည္းေကာင္း၊ နိုင္ငံသား အျဖစ္ကို ေသာ္လည္းေကာင္း ကိုးကြယ္သည့္ ဘာသာကို ေသာ္လည္းေကာင္း၊
#         အေၾကာင္းျပဳ၍ ခ်ဳပ္ခ်ယ္ ကန႔္သတ္ျခင္း မရွိဘဲ၊ ထိမ္းျမားနိုင္ခြင့္ ႏွင့္ မိသားစုထူေထာင္နိုင္ခြင့္ရွိသည္။ အဆိုပါ ေယာက်ာ္းႏွင့္ မိန္းမ တို႔သည္ လင္မယားအျဖစ္ ေပါင္းသင္းေနစဥ္
#         အခ်ိန္ အတြင္း၌ ေသာ္လည္းေကာင္း၊ အိမ္ေထာင္ကို ဖ်က္သိမ္း၍ ကြာရွင္းၾကသည့္ အခါ၌လည္းေကာင္း၊ လက္ထပ္ ေပါင္းသင္း အိမ္ေထာင္ျပဳျခင္းႏွင့္ စပ္လ်ဥ္းေသာ
#         တူညီသည့္ အခြင့္အေရးမ်ားကို ရရွိထိုက္သည္။သတို႔သား ႏွင့္ သတို႔သမီး ႏွစ္ဦးႏွစ္ဘက္၏ လြတ္လပ္ေသာ သေဘာဆႏၵရွိမွသာလၽွင္ ထိမ္းျမားျခင္းကို ျပဳရမည္။
#         မိသားစု တစ္ခုသည္ လူ႔အဖြဲ႕အစည္း၏ သဘာ၀က်ေသာ အေျခခံအဖြဲ႕တစ္ရပ္ျဖစ္သည္၊ ထိုမိသားစုသည္ လူ႔ အဖြဲ႕အစည္းႏွင့္ အစိုးရတို႔၏ ကာကြယ္ေစာင့္ေရွာက္ျခင္းကို ခံယူခြင့္ရွိသည္။'''
#         unicode = u'''အရွယ်ရောက် ပြီးသော ယောကျာ်း နှင့် မိန်းမတို့တွင် လူမျိုးကို သော်လည်းကောင်း၊ နိုင်ငံသား အဖြစ်ကို သော်လည်းကောင်း ကိုးကွယ်သည့် ဘာသာကို သော်လည်းကောင်း၊
#         အကြောင်းပြု၍ ချုပ်ချယ် ကန့်သတ်ခြင်း မရှိဘဲ၊ ထိမ်းမြားနိုင်ခွင့် နှင့် မိသားစုထူထောင်နိုင်ခွင့်ရှိသည်။ အဆိုပါ ယောကျာ်းနှင့် မိန်းမ တို့သည် လင်မယားအဖြစ် ပေါင်းသင်းနေစဉ်
#         အချိန် အတွင်း၌ သော်လည်းကောင်း၊ အိမ်ထောင်ကို ဖျက်သိမ်း၍ ကွာရှင်းကြသည့် အခါ၌လည်းကောင်း၊ လက်ထပ် ပေါင်းသင်း အိမ်ထောင်ပြုခြင်းနှင့် စပ်လျဉ်းသော
#         တူညီသည့် အခွင့်အရေးများကို ရရှိထိုက်သည်။သတို့သား နှင့် သတို့သမီး နှစ်ဦးနှစ်ဘက်၏ လွတ်လပ်သော သဘောဆန္ဒရှိမှသာလျှင် ထိမ်းမြားခြင်းကို ပြုရမည်။
#         မိသားစု တစ်ခုသည် လူ့အဖွဲ့အစည်း၏ သဘာ၀ကျသော အခြေခံအဖွဲ့တစ်ရပ်ဖြစ်သည်၊ ထိုမိသားစုသည် လူ့ အဖွဲ့အစည်းနှင့် အစိုးရတို့၏ ကာကွယ်စောင့်ရှောက်ခြင်းကို ခံယူခွင့်ရှိသည်။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed to Convert Article Sixteen")
#
#     def test_article_seventeen(self):
#         zawgyi = u'''လူတိုင္းတြင္ မိမိ တစ္ဦးခ်င္းေသာ္လည္းေကာင္း ၊ အျခားသူမ်ားႏွင့္ ဖက္စပ္၍ ေသာ္လည္းေကာင္း၊ ပစၥည္းဥစၥာ တို႔ကို ပိုင္ဆိုင္ရန္ အခြင့္အေရးရွိရမည္။
#            ဥပေဒအရ မဟုတ္လၽွင္၊ မည္သူမၽွ မိမိ၏ပစၥည္းဥစၥာပိုင္ဆိုင္ခြင့္ကို စြန႔္လႊတ္ျခင္း မခံေစရ။'''
#         unicode = u'''လူတိုင်းတွင် မိမိ တစ်ဦးချင်းသော်လည်းကောင်း ၊ အခြားသူများနှင့် ဖက်စပ်၍ သော်လည်းကောင်း၊ ပစ္စည်းဥစ္စာ တို့ကို ပိုင်ဆိုင်ရန် အခွင့်အရေးရှိရမည်။
#            ဥပဒေအရ မဟုတ်လျှင်၊ မည်သူမျှ မိမိ၏ပစ္စည်းဥစ္စာပိုင်ဆိုင်ခွင့်ကို စွန့်လွှတ်ခြင်း မခံစေရ။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed to Convert Article Seventeen")
#
#     def test_article_eighteen(self):
#         zawgyi = u'''လူတိုင္းတြင္ လြတ္လပ္စြာ ေတြးေခၚ ႀကံဆနိုင္ခြင့္၊ လြတ္လပ္စြာ ခံယူရပ္တည္နိုင္ခြင့္ ႏွင့္ လြတ္လပ္စြာ သက္ဝင္ ကိုးကြယ္နိုင္ခြင့္ရွိသည္။
#            အဆိုပါ အခြင့္အေရးမ်ား၌ မိမိကိုးကြယ္သည့္ ဘာသာကို သို႔တည္းမဟုတ္ သက္ဝင္ယုံၾကည္ခ်က္ကို လြတ္လပ္စြာ ေျပာင္းလဲနိုင္ခြင့္ ပါဝင္သည့္ အျပင္ မိမိ တစ္ေယာက္ခ်င္းျဖစ္ေစ၊
#            အျခားသူမ်ားႏွင့္ စုေပါင္း၍ျဖစ္ေစ၊ ျပည္သူအမ်ား ေရွ႕ေမွာက္တြင္ ေသာ္လည္းေကာင္း၊ ေရွ႕ေမွာက္တြင္ မဟုတ္ဘဲ ေသာ္လည္းေကာင္း၊
#            မိမိ ကိုးကြယ္ေသာ ဘာသာကို သို႔တည္းမဟုတ္ သက္ဝင္ ယုံၾကည္ခ်က္ကို လြတ္လပ္ စြာ သင္ျပနိုင္ခြင့္၊ က်င့္သုံးနိုင္ခြင့္၊
#            ဝတ္ျပဳကိုးကြယ္နိုင္ခြင့္ႏွင့္ ေဆာက္တည္ နိုင္ခြင့္တို႔လည္း ပါဝင္သည္။'''
#         unicode = u'''လူတိုင်းတွင် လွတ်လပ်စွာ တွေးခေါ် ကြံဆနိုင်ခွင့်၊ လွတ်လပ်စွာ ခံယူရပ်တည်နိုင်ခွင့် နှင့် လွတ်လပ်စွာ သက်ဝင် ကိုးကွယ်နိုင်ခွင့်ရှိသည်။
#            အဆိုပါ အခွင့်အရေးများ၌ မိမိကိုးကွယ်သည့် ဘာသာကို သို့တည်းမဟုတ် သက်ဝင်ယုံကြည်ချက်ကို လွတ်လပ်စွာ ပြောင်းလဲနိုင်ခွင့် ပါဝင်သည့် အပြင် မိမိ တစ်ယောက်ချင်းဖြစ်စေ၊
#            အခြားသူများနှင့် စုပေါင်း၍ဖြစ်စေ၊ ပြည်သူအများ ရှေ့မှောက်တွင် သော်လည်းကောင်း၊ ရှေ့မှောက်တွင် မဟုတ်ဘဲ သော်လည်းကောင်း၊
#            မိမိ ကိုးကွယ်သော ဘာသာကို သို့တည်းမဟုတ် သက်ဝင် ယုံကြည်ချက်ကို လွတ်လပ် စွာ သင်ပြနိုင်ခွင့်၊ ကျင့်သုံးနိုင်ခွင့်၊
#            ဝတ်ပြုကိုးကွယ်နိုင်ခွင့်နှင့် ဆောက်တည် နိုင်ခွင့်တို့လည်း ပါဝင်သည်။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed to Convert Article Eighteen")
#
#     def test_article_nineteen(self):
#         zawgyi = u'''လူတိုင္းတြင္ လြတ္လပ္စြာ ထင္ျမင္ ယူဆနိုင္ခြင့္ႏွင့္ လြတ္လပ္စြာ ဖြင့္ဟ ေဖာ္ျပနိုင္ခြင့္ရွိသည္။ အဆိုပါ အခြင့္အေရးမ်ား၌
#         အေႏွာင့္ အယွက္မရွိဘဲ လြတ္လပ္စြာ ထင္ျမင္ယူဆနိုင္ခြင့္ ပါဝင္ သည့္အျပင္၊ နိုင္ငံနယ္နိမိတ္မ်ားကို ေထာက္ထားရန္ မလိုဘဲ
#         သတင္းအေၾကာင္းအရာႏွင့္ သေဘာတရားမ်ားကို တနည္းနည္း ျဖင့္ လြတ္လပ္စြာ ရွာယူဆည္းပူးနိုင္ခြင့္၊ လက္ခံနိုင္ခြင့္ႏွင့္
#         ေဝငွ ျဖန႔္ခ်ိခြင့္တို႔လည္း ပါဝင္သည္။'''
#         unicode = u'''လူတိုင်းတွင် လွတ်လပ်စွာ ထင်မြင် ယူဆနိုင်ခွင့်နှင့် လွတ်လပ်စွာ ဖွင့်ဟ ဖော်ပြနိုင်ခွင့်ရှိသည်။ အဆိုပါ အခွင့်အရေးများ၌
#         အနှောင့် အယှက်မရှိဘဲ လွတ်လပ်စွာ ထင်မြင်ယူဆနိုင်ခွင့် ပါဝင် သည့်အပြင်၊ နိုင်ငံနယ်နိမိတ်များကို ထောက်ထားရန် မလိုဘဲ
#         သတင်းအကြောင်းအရာနှင့် သဘောတရားများကို တနည်းနည်း ဖြင့် လွတ်လပ်စွာ ရှာယူဆည်းပူးနိုင်ခွင့်၊ လက်ခံနိုင်ခွင့်နှင့်
#         ဝေငှ ဖြန့်ချိခွင့်တို့လည်း ပါဝင်သည်။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed to Convert Article Nineteen")
#
#     def test_article_twenty(self):
#         zawgyi = u'''လူတိုင္းတြင္ လြတ္လပ္ ေအးခ်မ္းစြာ စုေဝးနိုင္ခြင့္ ႏွင့္ ဖြဲ႕စည္းနိုင္ခြင့္ တို႔ ရွိသည္။
#            မည္သူ႔ကိုမၽွ အဖြဲ႕အစည္းတစ္ခုသို႔ ဝင္ေစရန္ အတင္းအက်ပ္မျပဳရ။'''
#         unicode = u'''လူတိုင်းတွင် လွတ်လပ် အေးချမ်းစွာ စုဝေးနိုင်ခွင့် နှင့် ဖွဲ့စည်းနိုင်ခွင့် တို့ ရှိသည်။
#            မည်သူ့ကိုမျှ အဖွဲ့အစည်းတစ်ခုသို့ ဝင်စေရန် အတင်းအကျပ်မပြုရ။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed to Convert Article Twenty")
#
#     def test_article_twentyone(self):
#         zawgyi = u'''လူတိုင္းတြင္ မိမိနိုင္ငံ၏ အုပ္ခ်ဳပ္ေရး၌ ကိုယ္တိုင္ျဖစ္ေစ၊ လြတ္လပ္စြာ ေရြးခ်ယ္လိုက္သည့္ ကိုယ္စားလွယ္မ်ားမွ တစ္ဆင့္ျဖစ္ေစ ပါဝင္ ေဆာင္ရြက္နိုင္ခြင့္ ရွိသည္။
#         လူတိုင္းတြင္ မိမိ၏နိုင္ငံရွိ ျပည္သူ႔ ဝန္ထမ္းအဖြဲ႕၌ ဝင္ေရာက္နိုင္ရန္ တူညီသည့္ အခြင့္ အေရးရွိသည္။
#         ျပည္သူျပည္သားတို႔၏ ဆႏၵသည္ အုပ္ခ်ဳပ္ အာဏာ၏ အေျခခံျဖစ္ရမည္၊ အဆိုပါ ဆႏၵကို အခ်ိန္ကာလပိုင္းျခားလ်က္ စစ္မွန္ေသာေရြးေကာက္ပြဲမ်ားျဖင့္ ထင္ရွားေစရမည္။
#         ေရြးေကာက္ ပြဲမ်ားတြင္လည္း လူတိုင္းအညီအမၽွ ဆႏၵမဲ ေပးနိုင္ခြင့္ ရွိရမည့္အျပင္ ၊ ထိုေရြးေကာက္ပြဲမ်ားကို လၽွို႔ဝွက္
#         မဲေပး စနစ္ျဖင့္ ျဖစ္ေစ၊ အလားတူ လြတ္လပ္ေသာ မဲေပးစနစ္ ျဖင့္ျဖစ္ေစ က်င္းပရမည္။'''
#         unicode = u'''လူတိုင်းတွင် မိမိနိုင်ငံ၏ အုပ်ချုပ်ရေး၌ ကိုယ်တိုင်ဖြစ်စေ၊ လွတ်လပ်စွာ ရွေးချယ်လိုက်သည့် ကိုယ်စားလှယ်များမှ တစ်ဆင့်ဖြစ်စေ ပါဝင် ဆောင်ရွက်နိုင်ခွင့် ရှိသည်။
#         လူတိုင်းတွင် မိမိ၏နိုင်ငံရှိ ပြည်သူ့ ဝန်ထမ်းအဖွဲ့၌ ဝင်ရောက်နိုင်ရန် တူညီသည့် အခွင့် အရေးရှိသည်။
#         ပြည်သူပြည်သားတို့၏ ဆန္ဒသည် အုပ်ချုပ် အာဏာ၏ အခြေခံဖြစ်ရမည်၊ အဆိုပါ ဆန္ဒကို အချိန်ကာလပိုင်းခြားလျက် စစ်မှန်သောရွေးကောက်ပွဲများဖြင့် ထင်ရှားစေရမည်။
#         ရွေးကောက် ပွဲများတွင်လည်း လူတိုင်းအညီအမျှ ဆန္ဒမဲ ပေးနိုင်ခွင့် ရှိရမည့်အပြင် ၊ ထိုရွေးကောက်ပွဲများကို လျှို့ဝှက်
#         မဲပေး စနစ်ဖြင့် ဖြစ်စေ၊ အလားတူ လွတ်လပ်သော မဲပေးစနစ် ဖြင့်ဖြစ်စေ ကျင်းပရမည်။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed to Convert Article TwentyOne")
#
#     def test_article_twentytwo(self):
#         zawgyi = u'''လူတိုင္းတြင္ လူ႔အဖြဲ႕အစည္း၏ အဖြဲ႕ဝင္တစ္ဦးအေနႏွင့္ လူမွုေရးလုံျခဳံခြင့္ရယူပိုင့္ခြင့္ရွိသည့္ အျပင္နိုင္ငံေရး ႀကိဳးပမ္းမွုျဖင့္ျဖစ္ေစ၊
#         နိုင္ငံတကာ ပူေပါင္းေဆာင္ရြက္မွုျဖင့္ျဖစ္ေစ၊ နိုင္ငံအသီးသီး၏ဖြဲ႕စည္းပုံႏွင့္ လည္းေကာင္း၊ သယံဇာတ အင္အားႏွင့္လည္းေကာင္း
#         ထိုလူ၏ ဂုဏ္သိကၡာႏွင့္ စရိုက္လကၡဏာ လြတ္လပ္စြာ တိုးတက္ျမင့္မားေရးအတြက္ မရွိမျဖစ္လိုအပ္ေသာ စီးပြားေရး၊လူမွုေရးႏွင့္ ယဥ္ေက်းမွု အခြင့္အေရးမ်ားကို သုံးစြဲပိုင္ခြင့္ရွိသည္။'''
#         unicode = u'''လူတိုင်းတွင် လူ့အဖွဲ့အစည်း၏ အဖွဲ့ဝင်တစ်ဦးအနေနှင့် လူမှုရေးလုံခြုံခွင့်ရယူပိုင့်ခွင့်ရှိသည့် အပြင်နိုင်ငံရေး ကြိုးပမ်းမှုဖြင့်ဖြစ်စေ၊
#         နိုင်ငံတကာ ပူပေါင်းဆောင်ရွက်မှုဖြင့်ဖြစ်စေ၊ နိုင်ငံအသီးသီး၏ဖွဲ့စည်းပုံနှင့် လည်းကောင်း၊ သယံဇာတ အင်အားနှင့်လည်းကောင်း
#         ထိုလူ၏ ဂုဏ်သိက္ခာနှင့် စရိုက်လက္ခဏာ လွတ်လပ်စွာ တိုးတက်မြင့်မားရေးအတွက် မရှိမဖြစ်လိုအပ်သော စီးပွားရေး၊လူမှုရေးနှင့် ယဉ်ကျေးမှု အခွင့်အရေးများကို သုံးစွဲပိုင်ခွင့်ရှိသည်။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed to Convert Article TwentyTwo")
#
#     def test_article_twentythree(self):
#         zawgyi = u'''လူတိုင္းတြင္ အလုပ္လုပ္ ရန္လည္းေကာင္း၊ မိမိႏွစ္သက္ရာ အသက္ေမြးမွု အလုပ္ အကိုင္ကို လြတ္လပ္စြာေရြးခ်ယ္ရန္ လည္းေကာင္း၊
#            တရားမၽွတ၍ လုပ္ေပ်ာ္ေသာ အလုပ္ခြင္၏ အေျခအေနကို ရရွိရန္ လည္းေကာင္း၊ အလုပ္လက္မဲ့ ျဖစ္ရျခင္းမွ အကာအကြယ္ ရရွိရန္ လည္းေကာင္း အခြင့္အေရးရွိသည္။
#            လူတိုင္းတြင္ ခြဲျခားျခင္းမခံရေစဘဲ၊ တူညီေသာ အလုပ္အတြက္ တူညီေသာ အခေၾကးေငြ ရပိုင္ခြင့္ရွိသည္။
#            အလုပ္လုပ္ကိုင္သည့္ လူတိုင္းတြင္၊ မိမိႏွင့္ မိမိ၏ မိသားစုအတြက္ လူ႔ဂုဏ္သိကၡာ ႏွင့္ ညီေအာင္ ေနထိုင္ စားေသာက္နိုင္ရန္၊
#            စိတ္ခ်ေလာက္သည့္ျပင္၊ တရား မၽွတ၍ လုပ္ေပ်ာ္သည့္ လစာေၾကးေငြ ရပိုင္ခြင့္ရွိသည္။ လိုအပ္ခဲ့လၽွင္အျခား နည္းလမ္းမ်ားမွ လူမွုေရး အေထာက္အပံ့ကိုလည္း ထပ္မံ၍ ရပိုင္ခြင့္ ရွိသည္။
#            လူတိုင္းတြင္ မိမိအက်ိဳး ခံစားခြင့္ကို ကာကြယ္ရန္ အလုပ္သမား အစည္းအ႐ုံးမ်ား ဖြဲ႕စည္းခြင့္ ၊ ပါဝင္ ေဆာင္ရြက္ခြင့္ ရွိသည္။'''
#         unicode = u'''လူတိုင်းတွင် အလုပ်လုပ် ရန်လည်းကောင်း၊ မိမိနှစ်သက်ရာ အသက်မွေးမှု အလုပ် အကိုင်ကို လွတ်လပ်စွာရွေးချယ်ရန် လည်းကောင်း၊
#            တရားမျှတ၍ လုပ်ပျော်သော အလုပ်ခွင်၏ အခြေအနေကို ရရှိရန် လည်းကောင်း၊ အလုပ်လက်မဲ့ ဖြစ်ရခြင်းမှ အကာအကွယ် ရရှိရန် လည်းကောင်း အခွင့်အရေးရှိသည်။
#            လူတိုင်းတွင် ခွဲခြားခြင်းမခံရစေဘဲ၊ တူညီသော အလုပ်အတွက် တူညီသော အခကြေးငွေ ရပိုင်ခွင့်ရှိသည်။
#            အလုပ်လုပ်ကိုင်သည့် လူတိုင်းတွင်၊ မိမိနှင့် မိမိ၏ မိသားစုအတွက် လူ့ဂုဏ်သိက္ခာ နှင့် ညီအောင် နေထိုင် စားသောက်နိုင်ရန်၊
#            စိတ်ချလောက်သည့်ပြင်၊ တရား မျှတ၍ လုပ်ပျော်သည့် လစာကြေးငွေ ရပိုင်ခွင့်ရှိသည်။ လိုအပ်ခဲ့လျှင်အခြား နည်းလမ်းများမှ လူမှုရေး အထောက်အပံ့ကိုလည်း ထပ်မံ၍ ရပိုင်ခွင့် ရှိသည်။
#            လူတိုင်းတွင် မိမိအကျိုး ခံစားခွင့်ကို ကာကွယ်ရန် အလုပ်သမား အစည်းအရုံးများ ဖွဲ့စည်းခွင့် ၊ ပါဝင် ဆောင်ရွက်ခွင့် ရှိသည်။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed to Convert Article TwentyThree")
#
#     def test_article_twentyfour(self):
#         zawgyi = u'''လူတိုင္းတြင္ သင့္ျမတ္ေလ်ာ္ကန္စြာ ကန႔္သတ္ထားသည့္ အလုပ္လုပ္ခ်ိန္ အျပင္၊ လစာႏွင့္တကြ အခါကာလအားေလ်ာ္စြာ သတ္မွတ္ ထားသည့္
#         အလုပ္ အားလပ္ရက္မ်ားပါဝင္သည့္ အနားယူခြင့္ႏွင့္ အားလပ္ခြင့္ ခံစားပိုင္ခြင့္ ရွိသည္။'''
#         unicode = u'''လူတိုင်းတွင် သင့်မြတ်လျော်ကန်စွာ ကန့်သတ်ထားသည့် အလုပ်လုပ်ချိန် အပြင်၊ လစာနှင့်တကွ အခါကာလအားလျော်စွာ သတ်မှတ် ထားသည့်
#         အလုပ် အားလပ်ရက်များပါဝင်သည့် အနားယူခွင့်နှင့် အားလပ်ခွင့် ခံစားပိုင်ခွင့် ရှိသည်။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed to Convert Article TwentyFour")
#
#     def test_article_twentyfive(self):
#         zawgyi = u'''လူတိုင္းတြင္ မိမိႏွင့္တကြ မိမိ၏ မိသားစု က်န္းမာေရးႏွင့္တကြ ကိုယ္စိတ္ႏွစ္ျဖာ ေအးခ်မ္းစြာ ေနထိုင္နိုင္ေရး အတြက္
#         အစာအဟာရ၊ အဝတ္အထည္ ေနအိမ္၊ ေဆးဝါး အကူအညီႏွင့္ လိုအပ္သည့္ လူမွု အေထာက္အပံ့မ်ား ပါဝင္ေသာ သင့္ေတာ္ ေလၽွာက္ပတ္သည့္
#         လူမွု အဆင့္အတန္းကို ရယူခံစားခြင့္ ရွိသည္။ ထို႔ျပင္ အလုပ္လက္မဲ့ျဖစ္ေသာ အခါ၌ ေသာ္လည္းေကာင္း၊ မက်န္းမမာ ျဖစ္ေသာ အခါ၌ ေသာ္လည္းေကာင္း၊
#         ကိုယ္အဂၤါ မစြမ္း မသန္ျဖစ္ေသာ အခါ၌ ေသာ္လည္းေကာင္း၊ မုဆိုးမျဖစ္ေသာအခါ၌ ေသာ္လည္းေကာင္း၊ အသက္အရြယ္အိုမင္းေသာ အခါ၌ ေသာ္လည္းေကာင္း၊
#         မိမိကိုယ္တိုင္က မတတ္နိုင္ေသာ အေၾကာင္းေၾကာင့္ ဝမ္းစာ ရွာမွီးနိုင္ေသာ နည္းလမ္း မရွိေသာ အခါ၌ ေသာ္လည္းေကာင္း၊ ေနထိုင္စားေသာက္ေရးအတြက္ လုံျခဳံစိတ္ခ်ရမွု အခြင့္အေရးရွိသည္။
#         သားသည္ မိခင္မ်ားႏွင့္ ကေလးမ်ားသည္ အထူးေစာင့္ေရွာက္ျခင္းႏွင့္ အကူအညီေပးျခင္းကို ရခြင့္ ရွိသည္။ ဥပေဒအရ ထိမ္းျမားျခင္းျဖင့္ျဖစ္ေစ
#         အျခား နည္းျဖင့္ ျဖစ္ေစ ေမြးဖြားေသာ ကေလးအားလုံး သည္ တူညီေသာ လူမွု ကာကြယ္ ေစာင့္ေရွာက္ေရးကို ရယူ ခံစားၾကရမည္။'''
#         unicode = u'''လူတိုင်းတွင် မိမိနှင့်တကွ မိမိ၏ မိသားစု ကျန်းမာရေးနှင့်တကွ ကိုယ်စိတ်နှစ်ဖြာ အေးချမ်းစွာ နေထိုင်နိုင်ရေး အတွက်
#         အစာအဟာရ၊ အဝတ်အထည် နေအိမ်၊ ဆေးဝါး အကူအညီနှင့် လိုအပ်သည့် လူမှု အထောက်အပံ့များ ပါဝင်သော သင့်တော် လျှောက်ပတ်သည့်
#         လူမှု အဆင့်အတန်းကို ရယူခံစားခွင့် ရှိသည်။ ထို့ပြင် အလုပ်လက်မဲ့ဖြစ်သော အခါ၌ သော်လည်းကောင်း၊ မကျန်းမမာ ဖြစ်သော အခါ၌ သော်လည်းကောင်း၊
#         ကိုယ်အင်္ဂါ မစွမ်း မသန်ဖြစ်သော အခါ၌ သော်လည်းကောင်း၊ မုဆိုးမဖြစ်သောအခါ၌ သော်လည်းကောင်း၊ အသက်အရွယ်အိုမင်းသော အခါ၌ သော်လည်းကောင်း၊
#         မိမိကိုယ်တိုင်က မတတ်နိုင်သော အကြောင်းကြောင့် ဝမ်းစာ ရှာမှီးနိုင်သော နည်းလမ်း မရှိသော အခါ၌ သော်လည်းကောင်း၊ နေထိုင်စားသောက်ရေးအတွက် လုံခြုံစိတ်ချရမှု အခွင့်အရေးရှိသည်။
#         သားသည် မိခင်များနှင့် ကလေးများသည် အထူးစောင့်ရှောက်ခြင်းနှင့် အကူအညီပေးခြင်းကို ရခွင့် ရှိသည်။ ဥပဒေအရ ထိမ်းမြားခြင်းဖြင့်ဖြစ်စေ
#         အခြား နည်းဖြင့် ဖြစ်စေ မွေးဖွားသော ကလေးအားလုံး သည် တူညီသော လူမှု ကာကွယ် စောင့်ရှောက်ရေးကို ရယူ ခံစားကြရမည်။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed to Convert Article TwentyFive")
#
#     def test_article_twentysix(self):
#         zawgyi = u'''လူတိုင္းသည္ ပညာသင္ ယူနိုင္ခြင့္ရွိသည္၊ အနည္းဆုံးမူလတန္းႏွင့္ အေျခခံ အဆင့္ အတန္းမ်ားတြင္ ပညာ သင္ၾကားေရးသည္ အခမဲ့ျဖစ္ရမည္။
#         မူလတန္းပညာသည္ မသင္မေနရ ပညာ ျဖစ္ရမည္။ စက္မွုလက္မွုပညာႏွင့္ အသက္ေမြးမွု ပညာမ်ားကို ေယဘူယ်အားျဖင့္ သင္ၾကားရယူ နိုင္ေစရမည္။
#         ထို႔ျပင္ အထက္တန္းပညာအတြက္ အရည္အခ်င္းကို အေျခခံျပဳ၍ တူညီေသာ အခြင့္အေရး ရရွိေစရမည္။
#         ပညာသင္ၾကားေရးကို လူသားတို႔၏ စရိုက္လကၡဏာ အျပည့္အဝ တိုးတက္မွု အျပင္၊ လူ႔အခြင့္အေရးႏွင့္ အေျခခံလြတ္လပ္ခြင့္ ရိုေသ
#         ေလးစားမွု တို႔ကို ရွင္သန္ဖြံ့ၿဖိဳးလာေစရန္ ရည္ရြယ္၍ သင္ၾကား ေစရမည္။ ပညာသင္ၾကားေရးသည္ နိုင္ငံ အားလုံး တို႔တြင္ လည္းေကာင္း၊
#         လူမ်ိဳးစုမ်ား တြင္လည္းေကာင္း၊ ဘာသာေရးအသင္းအဖြဲ႕မ်ားတြင္ လည္းေကာင္း၊ အခ်င္းခ်င္းနားလည္မွု၊ သည္းခံ မွုႏွင့္ ခင္မင္ရင္းႏွီးမွုတို႔ကို အားေပးရမည္။
#         ထို႔ျပင္ ၿငိမ္းခ်မ္းေရး တည္တံ့ေအာင္ ေဆာင္ရြက္ရန္ အလို႔ငွါ၊ ကုလသမဂၢ၏ ေဆာင္ရြက္မွုမ်ားကိုလည္း ျဖစ္ေျမာက္ ေအာင္ အားေပးရမည္။
#         မိဘတို႔တြင္၊ မိမိတို႔၏ ကေလးမ်ား သင္ယူရမည့္ပညာ အမ်ိဳးအစားကို ေရြးခ်ယ္နိုင္ေသာ လက္ဦး အခြင့္အေရးရွိသည္။'''
#         unicode = u'''လူတိုင်းသည် ပညာသင် ယူနိုင်ခွင့်ရှိသည်၊ အနည်းဆုံးမူလတန်းနှင့် အခြေခံ အဆင့် အတန်းများတွင် ပညာ သင်ကြားရေးသည် အခမဲ့ဖြစ်ရမည်။
#         မူလတန်းပညာသည် မသင်မနေရ ပညာ ဖြစ်ရမည်။ စက်မှုလက်မှုပညာနှင့် အသက်မွေးမှု ပညာများကို ယေဘူယျအားဖြင့် သင်ကြားရယူ နိုင်စေရမည်။
#         ထို့ပြင် အထက်တန်းပညာအတွက် အရည်အချင်းကို အခြေခံပြု၍ တူညီသော အခွင့်အရေး ရရှိစေရမည်။
#         ပညာသင်ကြားရေးကို လူသားတို့၏ စရိုက်လက္ခဏာ အပြည့်အဝ တိုးတက်မှု အပြင်၊ လူ့အခွင့်အရေးနှင့် အခြေခံလွတ်လပ်ခွင့် ရိုသေ
#         လေးစားမှု တို့ကို ရှင်သန်ဖွံ့ဖြိုးလာစေရန် ရည်ရွယ်၍ သင်ကြား စေရမည်။ ပညာသင်ကြားရေးသည် နိုင်ငံ အားလုံး တို့တွင် လည်းကောင်း၊
#         လူမျိုးစုများ တွင်လည်းကောင်း၊ ဘာသာရေးအသင်းအဖွဲ့များတွင် လည်းကောင်း၊ အချင်းချင်းနားလည်မှု၊ သည်းခံ မှုနှင့် ခင်မင်ရင်းနှီးမှုတို့ကို အားပေးရမည်။
#         ထို့ပြင် ငြိမ်းချမ်းရေး တည်တံ့အောင် ဆောင်ရွက်ရန် အလို့ငှါ၊ ကုလသမဂ္ဂ၏ ဆောင်ရွက်မှုများကိုလည်း ဖြစ်မြောက် အောင် အားပေးရမည်။
#         မိဘတို့တွင်၊ မိမိတို့၏ ကလေးများ သင်ယူရမည့်ပညာ အမျိုးအစားကို ရွေးချယ်နိုင်သော လက်ဦး အခွင့်အရေးရှိသည်။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed to Convert Article TwentySix")
#
#
#
#     def test_article_twentyseven(self):
#         zawgyi = u'''လူတိုင္းတြင္ သက္ဆိုင္ရာ ယဥ္ေက်းမွု ေလာက၌ လြတ္လပ္စြာ ပါဝင္ေဆာင္ ရြက္နိုင္ခြင့္ သုခုမပညာရပ္ မ်ားကိုလြတ္လပ္စြာလိုက္စား ေမြ႕ေလ်ာ္နိုင္ခြင့္၊
#         သိပၸံ ပညာထြန္းကားေရး လုပ္ငန္းမ်ားတြင္ လြတ္လပ္စြာ ဝင္ေရာက္ လုပ္ကိုင္ နိုင္ခြင့္ႏွင့္ ထိုပညာ၏ အက်ိဳး အာနိသင္မ်ားကို လြတ္လပ္စြာ ခံစားသုံးစြဲနိုင္ခြင့္ ရွိသည္။
#         လူတိုင္းတြင္ သိပၸံမွ ျဖစ္ေစ၊ စာေပမွျဖစ္ေစ၊ သုခုမပညာမွ ျဖစ္ေစ၊ မိမိကိုယ္ပိုင္ဉာဏ္ျဖင့္ႀကံစည္ ဖန္တီးမွုမွ ျဖစ္ထြန္းလာသည့္ ဂုဏ္ႏွင့္ ေငြေၾကး
#         အက်ိဳးအျမတ္မ်ားကို ခံစားရယူနိုင္ရန္ အခြင့္အေရး အတြက္ ကာကြယ္မွုကို ရရွိရန္ အခြင့္အေရး ရွိသည္။'''
#         unicode = u'''လူတိုင်းတွင် သက်ဆိုင်ရာ ယဉ်ကျေးမှု လောက၌ လွတ်လပ်စွာ ပါဝင်ဆောင် ရွက်နိုင်ခွင့် သုခုမပညာရပ် များကိုလွတ်လပ်စွာလိုက်စား မွေ့လျော်နိုင်ခွင့်၊
#         သိပ္ပံ ပညာထွန်းကားရေး လုပ်ငန်းများတွင် လွတ်လပ်စွာ ဝင်ရောက် လုပ်ကိုင် နိုင်ခွင့်နှင့် ထိုပညာ၏ အကျိုး အာနိသင်များကို လွတ်လပ်စွာ ခံစားသုံးစွဲနိုင်ခွင့် ရှိသည်။
#         လူတိုင်းတွင် သိပ္ပံမှ ဖြစ်စေ၊ စာပေမှဖြစ်စေ၊ သုခုမပညာမှ ဖြစ်စေ၊ မိမိကိုယ်ပိုင်ဉာဏ်ဖြင့်ကြံစည် ဖန်တီးမှုမှ ဖြစ်ထွန်းလာသည့် ဂုဏ်နှင့် ငွေကြေး
#         အကျိုးအမြတ်များကို ခံစားရယူနိုင်ရန် အခွင့်အရေး အတွက် ကာကွယ်မှုကို ရရှိရန် အခွင့်အရေး ရှိသည်။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed to Convert Article TwentySeven")
#
#     def test_article_twentyeight(self):
#         zawgyi = u'''လူတိုင္းသည္ ဤေၾကညာ စာတမ္းတြင္ ေဖာ္ျပထားသည့္ အခြင့္အေရးမ်ား ႏွင့္ လြတ္လပ္ခြင့္မ်ားကို အျပည့္အစုံ ရယူနိုင္ေသာ
#         လူမွု ဆက္ဆံေရး အေျခအေနႏွင့္ အျပည္ျပည္ဆိုင္ရာ ဆက္ဆံေရး အေျခအေနတို႔၏ အက်ိဳးေက်းဇူးကို ခံစားနိုင္ခြင့္ ရွိသည္။'''
#         unicode = u'''လူတိုင်းသည် ဤကြေညာ စာတမ်းတွင် ဖော်ပြထားသည့် အခွင့်အရေးများ နှင့် လွတ်လပ်ခွင့်များကို အပြည့်အစုံ ရယူနိုင်သော
#         လူမှု ဆက်ဆံရေး အခြေအနေနှင့် အပြည်ပြည်ဆိုင်ရာ ဆက်ဆံရေး အခြေအနေတို့၏ အကျိုးကျေးဇူးကို ခံစားနိုင်ခွင့် ရှိသည်။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed to Convert Article TwentyEight")
#
#     def test_article_twentynine(self):
#         zawgyi = u'''မိမိ၏စရိုက္လကၡဏာ လြတ္လပ္စြာ ဖြံ့ၿဖိဳး တိုးတက္နိုင္သည့္ တစ္ခုတည္းေသာ လူ႔အသိုက္အဝန္း အတြက္လူတိုင္း၌ တာဝန္ ရွိသည္။
#         မိမိ၏ အခြင့္အေရးမ်ားႏွင့္ လြတ္လပ္ ခြင့္မ်ားကို သုံးစြဲရာတြင္ လူတိုင္းသည္၊ အျခားသူမ်ား၏ အခြင့္အေရးမ်ားႏွင့္လြတ္လပ္ခြင့္မ်ားကို
#         အသိအမွတ္ျပဳ၍ ရိုေသေလးစားေစရန္အလို႔ငွာ လည္းေကာင္း၊ ဒီမိုကေရစီက်င့္သုံးေသာ လူ႔အဖြဲ႕အစည္းတြင္ ကိုယ္က်င့္တရားအျပင္၊
#         ရပ္ရြာေအးခ်မ္းသာယာေရးႏွင့္ ျပည္သူ႔ အက်ိဳး စီးပြား ျဖစ္ထြန္းေရးတို႔ အတြက္၊ တရားမၽွတစြာ က်င့္ေဆာင္ရန္ အလို႔ငွာ လည္းေကာင္း၊
#         ဥပေဒက ျပဌာန္းထားသည့္ ခ်ဳပ္ခ်ယ္မွုမ်ားျဖင့္သာ ကန႔္သတ္ျခင္းခံရမည္။
#         အဆိုပါ အခြင့္အေရးမ်ားႏွင့္ လြတ္လပ္ ခြင့္မ်ားကို မည္သည့္ အမွုကိစၥတြင္မၽွ ကုလသမဂၢ၏ ရည္ရြယ္ခ်က္မ်ားႏွင့္လည္းေကာင္း၊ အေျခခံမူမ်ားႏွင့္ လည္းေကာင္း ဆန႔္က်င္၍ မသုံးစြဲရ။'''
#         unicode = u'''မိမိ၏စရိုက်လက္ခဏာ လွတ်လပ်စွာ ဖွံ့ဖြိုး တိုးတက်နိုင်သည့် တစ်ခုတည်းသော လူ့အသိုက်အဝန်း အတွက်လူတိုင်း၌ တာဝန် ရှိသည်။
#         မိမိ၏ အခွင့်အရေးများနှင့် လွတ်လပ် ခွင့်များကို သုံးစွဲရာတွင် လူတိုင်းသည်၊ အခြားသူများ၏ အခွင့်အရေးများနှင့်လွတ်လပ်ခွင့်များကို
#         အသိအမှတ်ပြု၍ ရိုသေလေးစားစေရန်အလို့ငှာ လည်းကောင်း၊ ဒီမိုကရေစီကျင့်သုံးသော လူ့အဖွဲ့အစည်းတွင် ကိုယ်ကျင့်တရားအပြင်၊
#         ရပ်ရွာအေးချမ်းသာယာရေးနှင့် ပြည်သူ့ အကျိုး စီးပွား ဖြစ်ထွန်းရေးတို့ အတွက်၊ တရားမျှတစွာ ကျင့်ဆောင်ရန် အလို့ငှာ လည်းကောင်း၊
#         ဥပဒေက ပြဌာန်းထားသည့် ချုပ်ချယ်မှုများဖြင့်သာ ကန့်သတ်ခြင်းခံရမည်။
#         အဆိုပါ အခွင့်အရေးများနှင့် လွတ်လပ် ခွင့်များကို မည်သည့် အမှုကိစ္စတွင်မျှ ကုလသမဂ္ဂ၏ ရည်ရွယ်ချက်များနှင့်လည်းကောင်း၊ အခြေခံမူများနှင့် လည်းကောင်း ဆန့်ကျင်၍ မသုံးစွဲရ။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed to Convert Article TwentyNine")
#
#     def test_article_thirty(self):
#         zawgyi = u'''ဤေၾကညာစာတမ္းပါ အခြင့္အေရးႏွင့္တကြ လြတ္လပ္ခြင့္မ်ား ပ်က္စီးရာပ်က္စီးေၾကာင္းတို႔ကိုရည္ရြယ္၍၊ နိုင္ငံတစ္နိုင္ငံ အတြက္ ျဖစ္ေစ၊
#         လူတစ္စုအတြက္ ျဖစ္ေစ၊ လူတစ္ဦးတစ္ေယာက္ အတြက္ ျဖစ္ေစ ပါဝင္ ေဆာင္ရြက္ရန္ အခြင့္ရွိသည္ဟု ေသာ္လည္းေကာင္း၊
#         ကိုယ္တိုင္ေဆာင္ရြက္ရန္ အခြင့္ရွိသည္ ဟုေသာ္လည္းေကာင္းအဓိပၸါယ္ ပိုင္းျခားေကာက္ယူျခင္း မရွိေစရ။'''
#         unicode = u'''ဤကြေညာစာတမ်းပါ အခွင့်အရေးနှင့်တကွ လွတ်လပ်ခွင့်များ ပျက်စီးရာပျက်စီးကြောင်းတို့ကိုရည်ရွယ်၍၊ နိုင်ငံတစ်နိုင်ငံ အတွက် ဖြစ်စေ၊
#         လူတစ်စုအတွက် ဖြစ်စေ၊ လူတစ်ဦးတစ်ယောက် အတွက် ဖြစ်စေ ပါဝင် ဆောင်ရွက်ရန် အခွင့်ရှိသည်ဟု သော်လည်းကောင်း၊
#         ကိုယ်တိုင်ဆောင်ရွက်ရန် အခွင့်ရှိသည် ဟုသော်လည်းကောင်းအဓိပ္ပါယ် ပိုင်းခြားကောက်ယူခြင်း မရှိစေရ။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed to Convert Article Thirty")
#
#     def test_myanmar_pangram(self):
#         zawgyi = u'''သီဟိုဠ္မွ ဉာဏ္ႀကီးရွင္သည္ အာယုဝၯနေဆးၫႊန္းစာကို ဇလြန္ေဈးေဘးဗာဒံပင္ထက္ အဓိ႒ာန္လ်က္ ဂဃနဏဖတ္ခဲ့သည္။'''
#         unicode = u'''သီဟိုဠ်မှ ဉာဏ်ကြီးရှင်သည် အာယုဝဍ္ဎနဆေးညွှန်းစာကို ဇလွန်ဈေးဘေးဗာဒံပင်ထက် အဓိဋ္ဌာန်လျက် ဂဃနဏဖတ်ခဲ့သည်။'''
#         result = zg2uni.convert(zawgyi)
#         self.assertEqual(unicode, result, "Failed converting Article Pangram")


if __name__ == "__main__":
    unittest.main()
