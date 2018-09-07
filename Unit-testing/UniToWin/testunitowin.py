import unittest
import unitowin

class TestZG2UNI(unittest.TestCase):
    def test_article_one(self):
        win = u'''vlwdkif;onf wlnD vGwfvyfaom *kPfodu©mjzihf vnf;aumif;? wlnDvGwfvyfaom tcGihfta&;rsm;jzihf vnf;aumif;? arG;zGm;vmolrsm; jzpfonf/
         xdkolwdkYü ydkif;jcm; a0zefwwfaom ÓPfESihf usihf0wf odwwfaom pdwfwdkY½SdMuí xdkolwdkYonf tcsif;csif; arwÅmxm;í qufqHusihfokH;oihf\/'''
        unicode = u'''လူတိုင်းသည် တူညီ လွတ်လပ်သော ဂုဏ်သိက္ခာဖြင့် လည်းကောင်း၊ တူညီလွတ်လပ်သော အခွင့်အရေးများဖြင့် လည်းကောင်း၊ မွေးဖွားလာသူများ ဖြစ်သည်။
         ထိုသူတို့၌ ပိုင်းခြား ဝေဖန်တတ်သော ဉာဏ်နှင့် ကျင့်ဝတ် သိတတ်သော စိတ်တို့ရှိကြ၍ ထိုသူတို့သည် အချင်းချင်း မေတ္တာထား၍ ဆက်ဆံကျင့်သုံးသင့်၏။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article One")
    # def test_article_two(self):
    #     win = u'''vlwdkif;onf vlYtcGihf ta&; aMunmpmwrf;wGif azmfjyxm;onhf tcGihfta&; tm;vkH;? vGwfvyfcGihf tm;vkH;wdkYudk ydkifqdkif cHpm;cGihf½Sdonf/
    #     vlrsdK;EG,ftm;jzihf jzpfap? tom;ta&miftm;jzihf jzpfap? usm;? r? obm0tm;jzihf jzpfap? bmompum;tm;jzihf jzpfap? udk;uG,fonhf bmomtm;jzihf jzpfap?
    #     EdkifiHa&;,lqcsuf? odkYwnf;r[kwf tjcm;,lqcsuftm;jzihf jzpfap? EdkifiHESihf qdkifaom? odkYwnf;r[kwf vlrItqihftwef;ESihf qdkifaom Zpfjrpf tm;jzihfjzpfap?
    #     ypönf; Opöm *kPftm;jzihf jzpfap? rsdK;½dk;Zmwdtm;jzihf jzpfap? tjcm; tqihftwef; tm;jzihf jzpfap cGJjcm;jcif;r½Sdap&/
    #     xdkYjyif vlwpfOD; wpfa,muf aexdkif&m EdkifiH\ odkYwnf;r[kwf e,fajra'o\ EdkifiHa&;qdkif&m jzpfap pD&ifydkifcGihfqdkif&m jzpfap
    #     wdkif;jynf tcsif;csif;qdkif&mjzpfap? tqihftwef; wpfckckudk tajcûyí aomfvnf;aumif;?
    #     a'oe,fajrwpfckonf tcsKyftjcm tmPmydkif vGwfvyfonhf e,fajr? odkYwnf;r[kwf ukvor*¾ xdef;odrf; apmihfa½Smuf xm;&onhf e,fajr?
    #     odkYwnf;r[kwf udk,fydkif tkyfcsKyfcGihf tmPmwdkY wpdwfwa'oavmufom &½Sdonhf e,fajr pojzihf ,if;odkY aom e,fajrrsm;
    #     jzpfonf [laom taMumif;udk taxmuftxm; ûyí aomfvnf;aumif; cGJjcm;jcif; vkH;0 r½Sdap&/
    #     '''
    #     unicode = u'''လူတိုင်းသည် လူ့အခွင့် အရေး ကြေညာစာတမ်းတွင် ဖော်ပြထားသည့် အခွင့်အရေး အားလုံး၊ လွတ်လပ်ခွင့် အားလုံးတို့ကို ပိုင်ဆိုင် ခံစားခွင့်ရှိသည်။
    #     လူမျိုးနွယ်အားဖြင့် ဖြစ်စေ၊ အသားအရောင်အားဖြင့် ဖြစ်စေ၊ ကျား၊ မ၊ သဘာဝအားဖြင့် ဖြစ်စေ၊ ဘာသာစကားအားဖြင့် ဖြစ်စေ၊ ကိုးကွယ်သည့် ဘာသာအားဖြင့် ဖြစ်စေ၊
    #     နိုင်ငံရေးယူဆချက်၊ သို့တည်းမဟုတ် အခြားယူဆချက်အားဖြင့် ဖြစ်စေ၊ နိုင်ငံနှင့် ဆိုင်သော၊ သို့တည်းမဟုတ် လူမှုအဆင့်အတန်းနှင့် ဆိုင်သော ဇစ်မြစ် အားဖြင့်ဖြစ်စေ၊
    #     ပစ္စည်း ဥစ္စာ ဂုဏ်အားဖြင့် ဖြစ်စေ၊ မျိုးရိုးဇာတိအားဖြင့် ဖြစ်စေ၊ အခြား အဆင့်အတန်း အားဖြင့် ဖြစ်စေ ခွဲခြားခြင်းမရှိစေရ။
    #     ထို့ပြင် လူတစ်ဦး တစ်ယောက် နေထိုင်ရာ နိုင်ငံ၏ သို့တည်းမဟုတ် နယ်မြေဒေသ၏ နိုင်ငံရေးဆိုင်ရာ ဖြစ်စေ စီရင်ပိုင်ခွင့်ဆိုင်ရာ ဖြစ်စေ
    #     တိုင်းပြည် အချင်းချင်း ဆိုင်ရာဖြစ်စေ၊အဆင့်အတန်း တစ်ခုခုကို အခြေပြု၍ သော်လည်းကောင်း၊
    #     ဒေသနယ်မြေတစ်ခုသည် အချုပ်အခြာ အာဏာပိုင် လွတ်လပ်သည့် နယ်မြေ၊ သို့တည်းမဟုတ် ကုလသမဂ္ဂ ထိန်းသိမ်း စောင့်ရှောက် ထားရသည့် နယ်မြေ၊
    #     သို့တည်းမဟုတ် ကိုယ်ပိုင် အုပ်ချုပ်ခွင့် အာဏာတို့ တစိတ်တဒေသလောက်သာ ရရှိသည့် နယ်မြေ စသဖြင့် ယင်းသို့ သော နယ်မြေများ
    #     ဖြစ်သည် ဟူသော အကြောင်းကို အထောက်အထား ပြု၍ သော်လည်းကောင်း ခွဲခြားခြင်း လုံးဝ မရှိစေရ။
    #      '''
    #     result = unitowin.convert(unicode)
    #     self.assertEqual(win, result, "Failed converting Article Two")
    def test_article_three(self):
        win = u'''vlwdkif;ü touf½Sif&ef vGwfvyfrIcGihfESihf vkHûcHpdwfcscGihf ½Sdonf/'''
        unicode = u'''လူတိုင်း၌ အသက်ရှင်ရန် လွတ်လပ်မှုခွင့်နှင့် လုံခြုံစိတ်ချခွင့် ရှိသည်။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Three")
    def test_article_four(self):
        win = u'''rnfoludkrQ aus;uReftjzpf? odkYwnf;r[kwf taptyg;tjzpf? EdkifxufpD;eif; apcdkif;jcif; rûy&?
        vludk aus;uRefozG,f t"r® apcdkif;jcif;? ta&mif;t0,f ûyjcif;ESihf xdkoabm
        oufa&mufaom vkyfief;[lorQudk ydwfyif wm;jrpf &rnf/
        '''
        unicode = u'''မည်သူကိုမျှ ကျေးကျွန်အဖြစ်၊ သို့တည်းမဟုတ် အစေအပါးအဖြစ်၊ နိုင်ထက်စီးနင်း စေခိုင်းခြင်း မပြုရ၊
        လူကို ကျေးကျွန်သဖွယ် အဓမ္မ စေခိုင်းခြင်း၊ အရောင်းအဝယ် ပြုခြင်းနှင့် ထိုသဘော
        သက်ရောက်သော လုပ်ငန်းဟူသမျှကို ပိတ်ပင် တားမြစ် ရမည်။
        '''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Four")

    def test_article_five(self):
        win = u'''rnfoludkrQ n§Úf;yef; ESdyfpufjcif;? odkYwnf;r[kwf
        &ufpufMurf;êuwfpGm vlrqefpGm *kPfi,fapaom qufqHrI rûy&?
        odkYwnf;r[kwf tjypf'Pf ay;jcif;rûy&/'''
        unicode = u'''မည်သူကိုမျှ ညှဉ်းပန်း နှိပ်စက်ခြင်း၊ သို့တည်းမဟုတ်
        ရက်စက်ကြမ်းကြုတ်စွာ လူမဆန်စွာ ဂုဏ်ငယ်စေသော ဆက်ဆံမှု မပြုရ၊
        သို့တည်းမဟုတ် အပြစ်ဒဏ် ပေးခြင်းမပြုရ။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Five")
    def test_article_six(self):
        win = u'''vlwdkif;wGif Oya't&mü vlyk*¾dKvfwpfOD; tjzpfjzihf t&mcyfodrf;wGif todtrSwf ûyjcif;udk cH,lydkifcGihf½Sdonf/'''
        unicode = u'''လူတိုင်းတွင် ဥပဒေအရာ၌ လူပုဂ္ဂိုလ်တစ်ဦး အဖြစ်ဖြင့် အရာခပ်သိမ်းတွင် အသိအမှတ် ပြုခြင်းကို ခံယူပိုင်ခွင့်ရှိသည်။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Six")
    def test_article_seven(self):
        win = u'''vltm;vkH;wdkYonf Oya't&mü wlnDMuonhftjyif? Oya'\ tumtuG,fudk jcm;em;jcif; rcH&apbJ wlnDpGm cHpm;ydkifcGihf½Sdonf/
        þaMunm pmwrf;yg oabmw&m;rsm;udk zDqefí cGJjcm;jcif;rS vnf;aumif;?xdkodkYcGJjcm;jcif;udk vIHhaqmfjcif;rS vnf;aumif;?
        uif;vGwf ap&ef tumtuG,fudk wlnDpGm cHpm;ydkifcGihf ½Sdonf/'''
        unicode = u'''လူအားလုံးတို့သည် ဥပဒေအရာ၌ တူညီကြသည့်အပြင်၊ ဥပဒေ၏ အကာအကွယ်ကို ခြားနားခြင်း မခံရစေဘဲ တူညီစွာ ခံစားပိုင်ခွင့်ရှိသည်။
        ဤကြေညာ စာတမ်းပါ သဘောတရားများကို ဖီဆန်၍ ခွဲခြားခြင်းမှ လည်းကောင်း၊ထိုသို့ခွဲခြားခြင်းကို လှုံ့ဆော်ခြင်းမှ လည်းကောင်း၊
        ကင်းလွတ် စေရန် အကာအကွယ်ကို တူညီစွာ ခံစားပိုင်ခွင့် ရှိသည်။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Seven")
    def test_article_eight(self):
        win = u'''zGJYpnf;ykH tajccHOya'u aomfvnf;aumif; tjcm; Oya'u aomfvnf;aumif; vlwdkif;twGuf
        ay;xm;onhf tajccH tcGihfta&; rsm;onf csdK;azmuf zsufqD;jcif;cHcJh&vQif xdkodkY csdK;azmufzsufqD; aom ûyvkyfrIaMumihf
        jzpfay:vmaom epfemcsuf twGuf xdkolonf EdkifiHqdkif&m tmPmydkifw&m;½kH;wGif xda&mufpGm oufomcGihf ½SdEdkifap&rnf/'''
        unicode = u'''ဖွဲ့စည်းပုံ အခြေခံဥပဒေက သော်လည်းကောင်း အခြား ဥပဒေက သော်လည်းကောင်း လူတိုင်းအတွက်
        ပေးထားသည့် အခြေခံ အခွင့်အရေး များသည် ချိုးဖောက် ဖျက်ဆီးခြင်းခံခဲ့ရလျှင် ထိုသို့ ချိုးဖောက်ဖျက်ဆီး သော ပြုလုပ်မှုကြောင့်
        ဖြစ်ပေါ်လာသော နစ်နာချက် အတွက် ထိုသူသည် နိုင်ငံဆိုင်ရာ အာဏာပိုင်တရားရုံးတွင် ထိရောက်စွာ သက်သာခွင့် ရှိနိုင်စေရမည်။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Eight")
    def test_article_nine(self):
        win = u'''rnfolrQ Oya't& r[kwfaom zrf;qD;jcif;udk jzpfap? csKyfaESmifjcif;udk jzpfap? jynfESifjcif;udkjzpfap rcHap&/'''
        unicode = u'''မည်သူမျှ ဥပဒေအရ မဟုတ်သော ဖမ်းဆီးခြင်းကို ဖြစ်စေ၊ ချုပ်နှောင်ခြင်းကို ဖြစ်စေ၊ ပြည်နှင်ခြင်းကိုဖြစ်စေ မခံစေရ။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Nine")
    def test_article_ten(self):
        win = u'''tcGihfta&;rsm;ESihf wm0ef 0wÅ&m;rsm;udk tqkH;tjzwfcH&mwGif vnf;aumif;?jypfrIaMumihf w&m;pGJqdk pD&if qkH;jzwfcH&mwGif vnf;aumif;?
        vlwdkif;onf vGwfvyfí bufrvdkufaom w&m;½kH;awmf\ vltrsm; a½SYarSmufwGifrQwpGm Mum;emppfaq;jcif;udk wlnDpGm cHpm; ydkifcGihf½Sdonf/'''
        unicode = u'''အခွင့်အရေးများနှင့် တာဝန် ဝတ္တရားများကို အဆုံးအဖြတ်ခံရာတွင် လည်းကောင်း၊ပြစ်မှုကြောင့် တရားစွဲဆို စီရင် ဆုံးဖြတ်ခံရာတွင် လည်းကောင်း၊
        လူတိုင်းသည် လွတ်လပ်၍ ဘက်မလိုက်သော တရားရုံးတော်၏ လူအများ ရှေ့မှောက်တွင်မျှတစွာ ကြားနာစစ်ဆေးခြင်းကို တူညီစွာ ခံစား ပိုင်ခွင့်ရှိသည်။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Ten")
    def test_article_eleven(self):
        win = u'''vltrsm; a½SYarSmufü Oya'twdkif; ppfaq;í jypfrIusL;vGefonf[k xif½Sm; pD&ifjcif;cH&onhf tcsdeftxd
        jypfrIESihf w&m;pGJqdkjcif; cH&olwdkif;onf tjypfrJhol[lí ,lq jcif;cHxdkufonhf tcGihfta&;½Sdonf/
        xdktrIudk Mum;emppfaq;&m0,f pGyfpGJcH&onhf jypfrItwGuf ckcHacsyEdkif&ef vdktyfaom tcGihfta&;rsm;udk xdkoltm; ay;NyD; jzpfap&rnf/
        vlwpfOD;wpfa,muftm; EdkifiHOya't&jzpfap? tjynfjynfqdkif&m Oya't& jzpfap? jypfrIrajrmufaom vkyf&yf odkYr[kwf ysufuGufrIt& qGJqdkjypfay;jcif; rûy&/
        xdkYtjyif jypfrIusL;vGefpÚftcgu xdkufoihfapEdkifaom tjypf'PfxufydkrdkBuD;av;aom tjypf'Pfudk xdkufoihfjcif;r½Sdap&/
        '''
        unicode = u'''လူအများ ရှေ့မှောက်၌ ဥပဒေအတိုင်း စစ်ဆေး၍ ပြစ်မှုကျူးလွန်သည်ဟု ထင်ရှား စီရင်ခြင်းခံရသည့် အချိန်အထိ
        ပြစ်မှုနှင့် တရားစွဲဆိုခြင်း ခံရသူတိုင်းသည် အပြစ်မဲ့သူဟူ၍ ယူဆ ခြင်းခံထိုက်သည့် အခွင့်အရေးရှိသည်။
        ထိုအမှုကို ကြားနာစစ်ဆေးရာဝယ် စွပ်စွဲခံရသည့် ပြစ်မှုအတွက် ခုခံချေပနိုင်ရန် လိုအပ်သော အခွင့်အရေးများကို ထိုသူအား ပေးပြီး ဖြစ်စေရမည်။
        လူတစ်ဦးတစ်ယောက်အား နိုင်ငံဥပဒေအရဖြစ်စေ၊ အပြည်ပြည်ဆိုင်ရာ ဥပဒေအရ ဖြစ်စေ၊ ပြစ်မှုမမြောက်သော လုပ်ရပ် သို့မဟုတ် ပျက်ကွက်မှုအရ ဆွဲဆိုပြစ်ပေးခြင်း မပြုရ။
        ထို့အပြင် ပြစ်မှုကျူးလွန်စဉ်အခါက ထိုက်သင့်စေနိုင်သော အပြစ်ဒဏ်ထက်ပိုမိုကြီးလေးသော အပြစ်ဒဏ်ကို ထိုက်သင့်ခြင်းမရှိစေရ။
        '''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Eleven")

    def test_article_twelve(self):
        win = u'''rnfolrQ rdrdoabmtwdkif; at;csrf;vGwfvyfpGm aexdkifjcif;udk aomfvnf;aumif;? rdrd\ rdom;pkudk aomfvnf;aumif;?rdrd\ aetdrf todkuft0ef;udk
        aomfvnf;aumif;? pmay;pm,ludk aomfvnf;aumif;? Oya't& r[kwfaom 0ifa&muf pGufzufjcif; rcHap&/
        xdkYjyif rdrd\*kPfodu©m udkvnf; txufyg twdkif; ykwfcwfjcif; rcHap&/ vlwdkif;wGif xdkodkY 0ifa&mufpGufzufjcif;rS aomfvnf;aumif;
        ykwfcwfjcif;rS aomfvnf;aumif; Oya't& umuG,f ydkifcGihf½Sdonf/
        '''
        unicode = u'''မည်သူမျှ မိမိသဘောအတိုင်း အေးချမ်းလွတ်လပ်စွာ နေထိုင်ခြင်းကို သော်လည်းကောင်း၊ မိမိ၏ မိသားစုကို သော်လည်းကောင်း၊မိမိ၏ နေအိမ် အသိုက်အဝန်းကို
        သော်လည်းကောင်း၊ စာပေးစာယူကို သော်လည်းကောင်း၊ ဥပဒေအရ မဟုတ်သော ဝင်ရောက် စွက်ဖက်ခြင်း မခံစေရ။
        ထို့ပြင် မိမိ၏ဂုဏ်သိက္ခာ ကိုလည်း အထက်ပါ အတိုင်း ပုတ်ခတ်ခြင်း မခံစေရ။ လူတိုင်းတွင် ထိုသို့ ဝင်ရောက်စွက်ဖက်ခြင်းမှ သော်လည်းကောင်း
        ပုတ်ခတ်ခြင်းမှ သော်လည်းကောင်း ဥပဒေအရ ကာကွယ် ပိုင်ခွင့်ရှိသည်။
        '''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Twelve")

    def test_article_thirteen(self):
        win = u'''vlwdkif;wGif rdrd\EdkifiH e,fedrdwf twGif;ü vGwfvyfpGm oGm;vm a½TYajymif; EdkifcGihf? aexdkifcGihf½Sdonf/ vlwdkif;wGif rdrdaexdkif&m
        wdkif;jynfrS vnf;aumif;? tjcm;wdkif;jynfrSvnf;aumif; xGufcGm oGm;ydkifcGihf½Sdonhftjyif?rdrd\ wdkif;jynfodkY jyefvm ydkifcGihfvnf;½Sdonf/'''
        unicode = u'''လူတိုင်းတွင် မိမိ၏နိုင်ငံ နယ်နိမိတ် အတွင်း၌ လွတ်လပ်စွာ သွားလာ ရွှေ့ပြောင်း နိုင်ခွင့်၊ နေထိုင်ခွင့်ရှိသည်။ လူတိုင်းတွင် မိမိနေထိုင်ရာ
        တိုင်းပြည်မှ လည်းကောင်း၊ အခြားတိုင်းပြည်မှလည်းကောင်း ထွက်ခွာ သွားပိုင်ခွင့်ရှိသည့်အပြင်၊မိမိ၏ တိုင်းပြည်သို့ ပြန်လာ ပိုင်ခွင့်လည်းရှိသည်။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Thirteen")

    def test_article_fourteen(self):
        win = u'''vlwdkif;onf n§Úf;yef; ESdyfpuf cHae&jcif;rS vGwfuif;&ef tjcm;wdkif;jynf rsm;ü at;csrf;pGm cdkvIHaeEdkifcGihf½Sdonf/ EdkifiHa&;ESihf
        rywfoufonhf jypfrIrsm;rS aomfvnf;aumif;? ukvor*¾\ &nf½GufcsufESihf oabmw&m; rIrsm;udk zDqefaom trIrsm;rS aomfvn;faumif;?
        trSef ay:ayguf vmaom jypfrIaMumihf w&m;pGJqdkjcif; cH&onhf trItcif;rsm;wGif txufyg tcGihfta&;udk tokH;rûyEdkifap&/'''
        unicode = u'''လူတိုင်းသည် ညှဉ်းပန်း နှိပ်စက် ခံနေရခြင်းမှ လွတ်ကင်းရန် အခြားတိုင်းပြည် များ၌ အေးချမ်းစွာ ခိုလှုံနေနိုင်ခွင့်ရှိသည်။ နိုင်ငံရေးနှင့်
        မပတ်သက်သည့် ပြစ်မှုများမှ သော်လည်းကောင်း၊ ကုလသမဂ္ဂ၏ ရည်ရွက်ချက်နှင့် သဘောတရား မှုများကို ဖီဆန်သော အမှုများမှ သော်လညး်ကောင်း၊
        အမှန် ပေါ်ပေါက် လာသော ပြစ်မှုကြောင့် တရားစွဲဆိုခြင်း ခံရသည့် အမှုအခင်းများတွင် အထက်ပါ အခွင့်အရေးကို အသုံးမပြုနိုင်စေရ။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Fourteen")
    def test_article_fifteen(self):
        win = u'''vlwdkif;onf? EdkifiH wpfEdkifiH\ EdkifiHom;tjzpf cH,lcGihf½Sdonf/ Oya't& r[kwfvQif rnfolrQ rdrd\ EdkifiHom;tjzpfudk pGeYfvTwfjcif; rcHap&?
        EdkifiHom;tjzpf ajymif;vJEdkifaomtcGihfta&;udk vnf; jiif;y,fjcif; rcHap&/'''
        unicode = u'''လူတိုင်းသည်၊ နိုင်ငံ တစ်နိုင်ငံ၏ နိုင်ငံသားအဖြစ် ခံယူခွင့်ရှိသည်။ ဥပဒေအရ မဟုတ်လျှင် မည်သူမျှ မိမိ၏ နိုင်ငံသားအဖြစ်ကို စွန့်လွှတ်ခြင်း မခံစေရ၊
        နိုင်ငံသားအဖြစ် ပြောင်းလဲနိုင်သောအခွင့်အရေးကို လည်း ငြင်းပယ်ခြင်း မခံစေရ။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Fifteen")
    def test_article_sixteen(self):
        win = u'''t½G,fa&muf NyD;aom a,musmf; ESihf rdef;rwdkYwGif vlrsdK;udk aomfvnf;aumif;? EdkifiHom; tjzpfudk aomfvnf;aumif;
        udk;uG,fonhf bmomudk aomfvnf;aumif;? taMumif;ûyí csKyfcs,f ueYfowfjcif; r½SdbJ? xdrf;jrm;EdkifcGihf ESihf
        aomfvnf;aumif;? tdrfaxmifudk zsufodrf;í uGm½Sif;Muonhf tcgüvnf;aumif;? vufxyf aygif;oif; tdrfaxmifûyjcif;ESihf
        pyfvsÚf;aom wlnDonhf tcGihfta&;rsm;udk &½Sdxdkufonf/
        rdom;pk wpfckonf vlYtzGJYtpnf;\ obm0usaom tajccHtzGJYwpf&yfjzpfonf?
        xdkrdom;pkonf vlY tzGJYtpnf;ESihf tpdk;&wdkY\ umuG,fapmihfa½Smufjcif;udk cH,lcGihf½Sdonf/'''
        unicode = u'''အရွယ်ရောက် ပြီးသော ယောကျာ်း နှင့် မိန်းမတို့တွင် လူမျိုးကို သော်လည်းကောင်း၊ နိုင်ငံသား အဖြစ်ကို သော်လည်းကောင်း
        ကိုးကွယ်သည့် ဘာသာကို သော်လည်းကောင်း၊ အကြောင်းပြု၍ ချုပ်ချယ် ကန့်သတ်ခြင်း မရှိဘဲ၊ ထိမ်းမြားနိုင်ခွင့် နှင့်
        သော်လည်းကောင်း၊ အိမ်ထောင်ကို ဖျက်သိမ်း၍ ကွာရှင်းကြသည့် အခါ၌လည်းကောင်း၊ လက်ထပ် ပေါင်းသင်း အိမ်ထောင်ပြုခြင်းနှင့်
        စပ်လျဉ်းသော တူညီသည့် အခွင့်အရေးများကို ရရှိထိုက်သည်။
        မိသားစု တစ်ခုသည် လူ့အဖွဲ့အစည်း၏ သဘာ၀ကျသော အခြေခံအဖွဲ့တစ်ရပ်ဖြစ်သည်၊
        ထိုမိသားစုသည် လူ့ အဖွဲ့အစည်းနှင့် အစိုးရတို့၏ ကာကွယ်စောင့်ရှောက်ခြင်းကို ခံယူခွင့်ရှိသည်။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Sixteen")

    def test_article_seventeen(self):
        win = u'''vlwdkif;wGif rdrd wpfOD;csif;aomfvnf;aumif; ? tjcm;olrsm;ESihf zufpyfí aomfvnf;aumif;?
        ypönf;Opöm wdkYudk ydkifqdkif&ef tcGihfta&;½Sd&rnf/ Oya't& r[kwfvQif? rnfolrQ rdrd\ypönf;OpömydkifqdkifcGihfudk pGeYfvTwfjcif; rcHap&/'''
        unicode = u'''လူတိုင်းတွင် မိမိ တစ်ဦးချင်းသော်လည်းကောင်း ၊ အခြားသူများနှင့် ဖက်စပ်၍ သော်လည်းကောင်း၊
        ပစ္စည်းဥစ္စာ တို့ကို ပိုင်ဆိုင်ရန် အခွင့်အရေးရှိရမည်။ ဥပဒေအရ မဟုတ်လျှင်၊ မည်သူမျှ မိမိ၏ပစ္စည်းဥစ္စာပိုင်ဆိုင်ခွင့်ကို စွန့်လွှတ်ခြင်း မခံစေရ။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Seventeen")

    def test_article_eighteen(self):
        win = u'''vlwdkif;wGif vGwfvyfpGm awG;ac: BuHqEdkifcGihf? vGwfvyfpGm cH,l&yfwnfEdkifcGihf ESihf vGwfvyfpGm ouf0if udk;uG,fEdkifcGihf½Sdonf/
       tqdkyg tcGihfta&;rsm;ü rdrdudk;uG,fonhf bmomudk odkYwnf;r[kwf ouf0if,kHMunfcsufudk vGwfvyfpGm ajymif;vJEdkifcGihf
       yg0ifonhf tjyif rdrd wpfa,mufcsif;jzpfap? tjcm;olrsm;ESihf pkaygif;íjzpfap? jynfoltrsm; a½SYarSmufwGif aomfvnf;aumif;?
       a½SYarSmufwGif r[kwfbJ aomfvnf;aumif;? rdrd udk;uG,faom bmomudk odkYwnf;r[kwf ouf0if ,kHMunfcsufudk vGwfvyf pGm
       oifjyEdkifcGihf? usihfokH;EdkifcGihf? 0wfûyudk;uG,fEdkifcGihfESihf aqmufwnf EdkifcGihfwdkYvnf; yg0ifonf/'''
        unicode = u'''လူတိုင်းတွင် လွတ်လပ်စွာ တွေးခေါ် ကြံဆနိုင်ခွင့်၊ လွတ်လပ်စွာ ခံယူရပ်တည်နိုင်ခွင့် နှင့် လွတ်လပ်စွာ သက်ဝင် ကိုးကွယ်နိုင်ခွင့်ရှိသည်။
       အဆိုပါ အခွင့်အရေးများ၌ မိမိကိုးကွယ်သည့် ဘာသာကို သို့တည်းမဟုတ် သက်ဝင်ယုံကြည်ချက်ကို လွတ်လပ်စွာ ပြောင်းလဲနိုင်ခွင့်
       ပါဝင်သည့် အပြင် မိမိ တစ်ယောက်ချင်းဖြစ်စေ၊ အခြားသူများနှင့် စုပေါင်း၍ဖြစ်စေ၊ ပြည်သူအများ ရှေ့မှောက်တွင် သော်လည်းကောင်း၊
       ရှေ့မှောက်တွင် မဟုတ်ဘဲ သော်လည်းကောင်း၊ မိမိ ကိုးကွယ်သော ဘာသာကို သို့တည်းမဟုတ် သက်ဝင် ယုံကြည်ချက်ကို လွတ်လပ် စွာ
       သင်ပြနိုင်ခွင့်၊ ကျင့်သုံးနိုင်ခွင့်၊ ဝတ်ပြုကိုးကွယ်နိုင်ခွင့်နှင့် ဆောက်တည် နိုင်ခွင့်တို့လည်း ပါဝင်သည်။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Eighteen")

    def test_article_nineteen(self):
        win = u'''vlwdkif;wGif vGwfvyfpGm xifjrif ,lqEdkifcGihfESihf vGwfvyfpGm zGihf[ azmfjyEdkifcGihf½Sdonf/
        tqdkyg tcGihfta&;rsm;ü taESmihf t,Sufr½SdbJ vGwfvyfpGm xifjrif,lqEdkifcGihf yg0if onhftjyif?
        EdkifiHe,fedrdwfrsm;udk axmufxm;&ef rvdkbJ owif;taMumif;t&mESihf oabmw&m;rsm;udk wenf;enf; jzihf vGwfvyfpGm ½Sm,lqnf;yl;EdkifcGihf?
        vufcHEdkifcGihfESihf a0iS jzeYfcsdcGihfwdkYvnf; yg0ifonf/'''
        unicode = u'''လူတိုင်းတွင် လွတ်လပ်စွာ ထင်မြင် ယူဆနိုင်ခွင့်နှင့် လွတ်လပ်စွာ ဖွင့်ဟ ဖော်ပြနိုင်ခွင့်ရှိသည်။
        အဆိုပါ အခွင့်အရေးများ၌ အနှောင့် အယှက်မရှိဘဲ လွတ်လပ်စွာ ထင်မြင်ယူဆနိုင်ခွင့် ပါဝင် သည့်အပြင်၊
        နိုင်ငံနယ်နိမိတ်များကို ထောက်ထားရန် မလိုဘဲ သတင်းအကြောင်းအရာနှင့် သဘောတရားများကို တနည်းနည်း ဖြင့် လွတ်လပ်စွာ ရှာယူဆည်းပူးနိုင်ခွင့်၊
        လက်ခံနိုင်ခွင့်နှင့် ဝေငှ ဖြန့်ချိခွင့်တို့လည်း ပါဝင်သည်။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Nineteen")

    def test_article_twenty(self):
        win = u'''vlwdkif;wGif vGwfvyf at;csrf;pGm pka0;EdkifcGihf ESihf zGJYpnf;EdkifcGihf wdkY ½Sdonf/
        rnfolYudkrQ tzGJYtpnf;wpfckodkY 0ifap&ef twif;t$rûy&/'''
        unicode = u'''လူတိုင်းတွင် လွတ်လပ် အေးချမ်းစွာ စုဝေးနိုင်ခွင့် နှင့် ဖွဲ့စည်းနိုင်ခွင့် တို့ ရှိသည်။
        မည်သူ့ကိုမျှ အဖွဲ့အစည်းတစ်ခုသို့ ဝင်စေရန် အတင်းအကျပ်မပြုရ။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Twenty")

    def test_article_twentyone(self):
        win = u'''vlwdkif;wGif rdrdEdkifiH\ tkyfcsKyfa&;ü udk,fwdkifjzpfap? vGwfvyfpGm a½G;cs,fvdkufonhf udk,fpm;vS,frsm;rS wpfqihfjzpfap yg0if aqmif½GufEdkifcGihf ½Sdonf/
        vlwdkif;wGif rdrd\EdkifiH½Sd jynfolY 0efxrf;tzGJYü 0ifa&mufEdkif&ef wlnDonhf tcGihfta&;½Sdonf/ jynfoljynfom;wdkY\ qE´onf tkyfcsKyf tmPm\ tajccHjzpf&rnf?tqdkyg qE´udk
        tcsdefumvydkif;jcm;vsuf ppfrSefaoma½G;aumufyGJrsm;jzihf xif½Sm;ap&rnf/'''
        unicode = u'''လူတိုင်းတွင် မိမိနိုင်ငံ၏ အုပ်ချုပ်ရေး၌ ကိုယ်တိုင်ဖြစ်စေ၊ လွတ်လပ်စွာ ရွေးချယ်လိုက်သည့် ကိုယ်စားလှယ်များမှ တစ်ဆင့်ဖြစ်စေ ပါဝင် ဆောင်ရွက်နိုင်ခွင့် ရှိသည်။
        လူတိုင်းတွင် မိမိ၏နိုင်ငံရှိ ပြည်သူ့ ဝန်ထမ်းအဖွဲ့၌ ဝင်ရောက်နိုင်ရန် တူညီသည့် အခွင့်အရေးရှိသည်။ ပြည်သူပြည်သားတို့၏ ဆန္ဒသည် အုပ်ချုပ် အာဏာ၏ အခြေခံဖြစ်ရမည်၊အဆိုပါ ဆန္ဒကို
        အချိန်ကာလပိုင်းခြားလျက် စစ်မှန်သောရွေးကောက်ပွဲများဖြင့် ထင်ရှားစေရမည်။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Twentyone")

    def test_article_twentytwo(self):
        win = u'''xdkvl\ *kPfodu©mESihf p½dkufvu©Pm vGwfvyfpGm wdk;wufjrihfrm;a&;twGuf r½Sdrjzpfvdktyfaom pD;yGm;a&;?vlrIa&;ESihf,Úfaus;rI tcGihfta&;rsm;udk okH;pGJydkifcGihf½Sdonf/'''
        unicode = u'''ထိုလူ၏ ဂုဏ်သိက္ခာနှင့် စရိုက်လက္ခဏာ လွတ်လပ်စွာ တိုးတက်မြင့်မားရေးအတွက် မရှိမဖြစ်လိုအပ်သော စီးပွားရေး၊လူမှုရေးနှင့်ယဉ်ကျေးမှု အခွင့်အရေးများကို သုံးစွဲပိုင်ခွင့်ရှိသည်။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Twentytwo")

    def test_article_twentyfour(self):
        win = u'''vlwdkif;wGif oihfjrwfavsmfuefpGm ueYfowfxm;onhf tvkyfvkyfcsdef tjyif? vpmESihfwuG tcgumvtm;avsmfpGm
        owfrSwf xm;onhf tvkyf tm;vyf&ufrsm;yg0ifonhf tem;,lcGihfESihf tm;vyfcGihf cHpm;ydkifcGihf ½Sdonf/'''
        unicode = u'''လူတိုင်းတွင် သင့်မြတ်လျော်ကန်စွာ ကန့်သတ်ထားသည့် အလုပ်လုပ်ချိန် အပြင်၊ လစာနှင့်တကွ အခါကာလအားလျော်စွာ
        သတ်မှတ် ထားသည့် အလုပ် အားလပ်ရက်များပါဝင်သည့် အနားယူခွင့်နှင့် အားလပ်ခွင့် ခံစားပိုင်ခွင့် ရှိသည်။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Twentyfour")

    def test_article_twentyfive(self):
        win = u'''vlwdkif;wGif rdrdESihfwuG rdrd\ rdom;pk usef;rma&;ESihfwuG udk,fpdwfESpfjzm at;csrf;pGm aexdkifEdkifa&; twGuf tpmt[m&?'''
        unicode = u'''လူတိုင်းတွင် မိမိနှင့်တကွ မိမိ၏ မိသားစု ကျန်းမာရေးနှင့်တကွ ကိုယ်စိတ်နှစ်ဖြာ အေးချမ်းစွာ နေထိုင်နိုင်ရေး အတွက် အစာအဟာရ၊'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Twentyfive")
    def test_myanmar_pangram(self):
        win = u'''oD[dkVfrS ÓPfBuD;½Sifonf tm,k0¹eaq;ñTef;pmudk ZvGefaps;ab;Am'Hyifxuf t"d|mefvsuf *CePzwfcJhonf/'''
        unicode = u'''သီဟိုဠ်မှ ဉာဏ်ကြီးရှင်သည် အာယုဝဍ္ဎနဆေးညွှန်းစာကို ဇလွန်ဈေးဘေးဗာဒံပင်ထက် အဓိဋ္ဌာန်လျက် ဂဃနဏဖတ်ခဲ့သည်။'''
        result = unitowin.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Pangram")

if __name__ == "__main__":
    unittest.main()
