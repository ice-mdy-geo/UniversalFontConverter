# -*- coding: utf-8 -*-
import re

def replace(input):
    output =input
    output = output.replace(u'\u100b\u1039\u100c', u'\u1092')
    output = output.replace(u'\u1039\u1000', u'\u1060')
    output = output.replace(u'\u1039\u1001', u'\u1061')
    output = output.replace(u'\u1039\u1002', u'\u1062')
    output = output.replace(u'\u1039\u1003', u'\u1063')
    output = output.replace(u'\u1039\u1005', u'\u1065')
    output = output.replace(u'\u1039\u1006', u'\u1066')
    output = output.replace(u'\u1039\u1006', u'\u1067')
    output = output.replace(u'\u1039\u1007', u'\u1068')
    output = output.replace(u'\u1039\u1008', u'\u1069')
    output = output.replace(u'\u1039\u100B', u'\u106C')
    output = output.replace(u'\u1039\u100C', u'\u106D')
    output = output.replace(u'\u1039\u100F', u'\u1070')
    output = output.replace(u'\u1039\u1010', u'\u1071')
    output = output.replace(u'\u1039\u1011', u'\u1073')
    output = output.replace(u'\u1039\u1011', u'\u1074')
    output = output.replace(u'\u1039\u1012', u'\u1075')
    output = output.replace(u'\u1039\u1013', u'\u1076')
    output = output.replace(u'\u1039\u1014', u'\u1077')
    output = output.replace(u'\u1039\u1015', u'\u1078')
    output = output.replace(u'\u1039\u1016', u'\u1079')
    output = output.replace(u'\u1039\u1017', u'\u107A')
    output = output.replace(u'\u1039\u1019', u'\u107C')
    output = output.replace(u'\u1039\u101C', u'\u1085')
    output = output.replace(u'\u1039\u1018', u'\u107B')
    ####-----------------------------------------------------------------------------
    output = output.replace(u'\u100F\u103A\u100D', u'\u1091')
    output = output.replace(u'\u100d\u1039\u100e', u'\u106f')
    output = output.replace(u'\u103A', u'\u1039')  # a-that
    output = output.replace(u'\u103B', u'\u103A')  # ya-pint
    output = output.replace(u'\u103C', u'\u103B')  # ya-yit
    output = output.replace(u'\u103D', u'\u103C')  # wa-swae
    output = output.replace(u'\u103E', u'\u103D')  # ha-htoe
    output = output.replace(u'\u103F', u'\u1086')  # ta-gyi
    return  output
def decompose(input):
    output =input
    # -------------------------ta-wai-htoe-----------------------------------------------------------------------------------
    output = re.sub(u'([\u1000-\u1021])([\u103A])(\u1031)', u"\\3\\1\\2", output)  # tawai-yapint-byee
    output = re.sub(u'([\u1000-\u1021])(\u103B)', u"\\2\\1", output)  # yayit-byee
    output = re.sub(u'([\u1000-\u1021])(\u1031)', u"\\2\\1", output)  # thawai-byee
    output = re.sub(u'([\u103B])(\u1031)', u"\\2\\1", output)  # tawai-yayit
    output = re.sub(u'([\u1000-\u1021])([\u103C\u103D])(\u1031)', u"\\3\\1\\2", output)  # tawai-byee-swae-htoe
    output = re.sub(u'(\u108F)([\u103C\u103D])(\u1031)', u"\\3\\1\\2", output)  # tawai-nagnge-swae-htoe
    output = re.sub(u'(\u1090)([\u103C\u103D])(\u1031)', u"\\3\\1\\2", output)  # tawai-ya-swae-htoe
    output = re.sub(u'(\u108F)(\u108A)(\u1031)', u"\\3\\1\\2", output)  # tawai-nagnge-swae-htoe
    output = re.sub(u'(\u1090)(\u108A)(\u1031)', u"\\3\\1\\2", output)  # tawai-nagnge-swae-htoe
    output = re.sub(u'([\u1000-\u1021])([\u108A])(\u1031)', u"\\3\\1\\2", output)  # tawai-byee-swae-htoe
    output = re.sub(u'([\u1000-\u1021])(\u103A)(\u103D)(\u1031)', u"\\4\\1\\2\\3", output)  # tawai-yapint-byee
    output = re.sub(u'\u1014([\u1070-\u107c])', u'\u108f\\1', output)

    # --------------------------------------------------------------------------------------------------------------------------
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1062((?:\u103b)?)', u'\\1\\2\u1002\u1064', output)  # Ka....
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1060((?:\u103b)?)', u'\\1\\2\u1000\u1064', output)  # Kha...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1061((?:\u103b)?)', u'\\1\\2\u1001\u1064', output)  # Ga....
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1063((?:\u103b)?)', u'\\1\\2\u1003\u1064', output)  # NgaGyi...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1065((?:\u103b)?)', u'\\1\\2\u1005\u1064', output)  # sa...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1066((?:\u103b)?)', u'\\1\\2\u1006\u1064', output)  # salane...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1067((?:\u103b)?)', u'\\1\\2\u1006\u1064', output)  # salane...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1068((?:\u103b)?)', u'\\1\\2\u1007\u1064', output)  # za...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1069((?:\u103b)?)', u'\\1\\2\u1008\u1064', output)  # zamyin...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u106c((?:\u103b)?)', u'\\1\\2\u100b\u1064', output)  # tatalin...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u106d((?:\u103b)?)', u'\\1\\2\u100c\u1064', output)  # htaone...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1070((?:\u103b)?)', u'\\1\\2\u100f\u1064', output)  # nagyi...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1071((?:\u103b)?)', u'\\1\\2\u1010\u1064', output)  # ta...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1072((?:\u103b)?)', u'\\1\\2\u1010\u1064', output)  # ta...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1073((?:\u103b)?)', u'\\1\\2\u1011\u1064', output)  # hta...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1074((?:\u103b)?)', u'\\1\\2\u1011\u1064', output)  # hta...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1075((?:\u103b)?)', u'\\1\\2\u1012\u1064', output)  # da...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1076((?:\u103b)?)', u'\\1\\2\u1013\u1064', output)  # daout...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1077((?:\u103b)?)', u'\\1\\2\u1014\u1064', output)  # na...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1078((?:\u103b)?)', u'\\1\\2\u1015\u1064', output)  # pa...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u1079((?:\u103b)?)', u'\\1\\2\u1016\u1064', output)  # pha...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u107a((?:\u103b)?)', u'\\1\\2\u1017\u1064', output)  # va...
    output = re.sub(u'((?:\u1031)?)\u1004\u1039\u107b((?:\u103b)?)', u'\\1\\2\u1018\u1064', output)  # ba...
    # output = output.replace(u'\u1004\u1039\u1093', u'\u1018\u1064')  # NgaGyi...
    output = re.sub(u'\u1004\u1039\u107c', u'\u1019\u1064', output)  # NgaGyi...
    output = re.sub(u'\u1004\u1039\u1084', u'\u101c\u1064', output)  # NgaGyi...
    output = re.sub(u'\u1064\u102D', u'\u108B', output)  # NgaGyi...
    output = re.sub(u'\u1064\u102E', u'\u108C', output)  # NgaGyi...
    output = re.sub(u'\u1064\u1036', u'\u108D', output)  # NgaGyi...
    output = re.sub(u'\u102D\u1036', u'\u108E', output)  # NgaGyi...
    output= re.sub(u'((?:\u101f)?)\u1004\u1039\u1039(\u101e)', u'\\1\\2\u1064', output)  # hintar
    # -------------------------------------------------------------------------------------------------------------------------------
    output = output.replace(u'\u1009\u1039', u'\u1025\u1039')  # nyalay-that
    output = output.replace(u'\u103C\u103D', u'\u103D\u103C')  # swae-htoe
    output = output.replace(u'\u103a\u103d', u'\u103d\u103a')  # pint-htoe
    output = output.replace(u'\u103d\u103a', u'\u103d\u107d')  # pint-htoe
    output = output.replace(u'\u103c\u103A', u'\u103A\u103c')  # pint-swae
    output = re.sub(u'\u103d\u102f', u'\u1088', output)  # hatoe-tachaung
    output = re.sub(u'\u103d\u1030', u'\u1089', output)  # hatoe-nachaung
    output = output.replace(u'\u103D\u103C', u'\u108A')  # waswae-hatoe
    output = output.replace(u'\u102B\u1039', u'\u105A')  # yaecha-shaehtoe
    output = output.replace(u'\u103D\u102F', u'\u1088')  # hatoe-tachaung
    output = output.replace(u'\u103D\u1030', u'\u1089')  # hatoe-nachaung
    output = output.replace(u'\u102D\u1036', u'\u108E')  # lonetin-ttt
    output = output.replace(u'\u100A\u103D', u'\u100A\u1087')  # nya-htoe
    output = output.replace(u'\u102f\u1036', u'\u1036\u102f')  # ttt-tachaung
    output = re.sub(u'([\u1000-\u1021])(\u103b)\u103d', u'\\1\\2\u1087', output)  # byee-yit-hatoe
    # -----------------------tachaung-nachaung-------------------------------------------------------------------------------
    output = re.sub(u'(\u103B)([\u1000-\u1021])\u102F', u'\\1\\2\u1033', output)  # yit-tachaung
    output = re.sub(u'(\u103B)([\u1000-\u1021])\u1030', u'\\1\\2\u1034', output)  # yit-nachaung
    output = re.sub(u'\u103A\u102F', u'\u103A\u1033', output)  # pint-tachaung
    output = re.sub(u'\u103A\u1030', u'\u103A\u1034', output)  # pint-nachaung
    output = re.sub(u'\u103A\u103C', u'\u107D\u103C', output)  # pint-waswe
    output = re.sub(u'([\u103A\u103b])([\u102D\u102e\u1036])\u102F', u'\\1\\2\u1033',
                    output)  # yit-pint-lontin-tachaung
    output = re.sub(u'(\u1020)\u102f', u'\\1\u1033', output)  # la-gyi tachaung
    output = re.sub(
        u'([\u1060\u1061\u1062\u1063\u1065\u1066\u1068\u1069\u106b\u106d\u1070\u1071\u1073\u1075\u1076\u1077\u1078\u1079\u107a\u107b\u107c\u1085])((?:[\u102D\u102E\u1036])?)\u102F',
        u'\\1\\2\u1033', output)  # sint lonetin chaungnin
    output = re.sub(
        u'([\u1060\u1061\u1062\u1063\u1065\u1066\u1068\u1069\u106b\u106d\u1070\u1071\u1073\u1075\u1076\u1077\u1078\u1079\u107a\u107b\u107c\u1085])((?:[\u102D\u102E\u1036])?)\u1030',
        u'\\1\\2\u1034', output)  # sint lonetin chaungnin

    # -----------------------nange-------------------------------------------------------------------------------------------------
    output = re.sub(u'\u1014([\u103D\u103C\u102F\u1030\u1088\u1089\u108a])((?:[\u102d\u102e\u1036])?)', u'\u108F\\1\\2',output)  # nange-hatoe
    output = re.sub(u'\u1014([\u1060\u1061\u1062\u1063\u1065\u1066\u1068\u1069\u106b\u106d\u1070\u1071\u1073\u1075\u1076\u1077\u1078\u1079\u107a\u107b\u107c\u1085])',u'\u108F\\1', output)  # nange-byee-sint
    # ----------------------ya-----------------------------------------------------------------------------------------------
    output = re.sub(u'\u101b((?:[\u102d\u102e\u1036])?)([\u103D\u103C\u102F\u1030\u1088\u1089\u108a])((?:[\u102d\u102e\u1036])?)',u'\u1090\\1\\2\\3', output)  # ya-hatoe
    output = re.sub(
        u'\u101b\u103d((?:[\u102d\u102e\u1036])?)', u'\u1090\u103d\\1', output)  # ya-hatoe
    output = re.sub(
        u'\u101b([\u1060\u1061\u1062\u1063\u1065\u1066\u1068\u1069\u106b\u106d\u1070\u1071\u1073\u1075\u1076\u1077\u1078\u1079\u107a\u107b\u107c\u1085])',
        u'\u1090\\1', output)  # ya-byee-sint
    return output
#
# def virtual2logical(input):
#     output = input
#
#     return output
def shape(input):
     output= input
     # -------------------------------out myit-------------------------------------------------------------------------------
     output = re.sub(u'\u1030\u1037', u'\u1030\u1094', output)  # out-myit nachaung
     output = re.sub(u'\u103C\u1037', u'\u103C\u1095', output)  # out-myit waswae
     output = re.sub(u'\u108A\u1037', u'\u108A\u1095', output)  # out-myit waswaehtoe
     output = re.sub(u'\u102D\u102F\u1037', u'\u102D\u102F\u1094', output)  # out-myit lonetin tachaung
     output = re.sub(u'\u103C\u1032\u1037', u'\u103C\u1032\u1094', output)  # out-myit nouthtoe waswae
     output = re.sub(u'\u103C\u1036\u1037', u'\u103C\u1036\u1095', output)  # out-myit taetin waswae
     output = re.sub(u'\u1036\u1088\u1037', u'\u1036\u1088\u1095', output)  # out-myit hahtoe nachaung
     output = re.sub(u'([\u103D\u1036\u102F])\u1037', u'\\1\u1094', output)  # out-myit hahtoe nachaung
     output = re.sub(u'\u1014\u1037', u'\u1014\u1094', output)  # autmyint-nang

     # -------------------yitgyi-------------------------------------------------------------------------------------------
     output = re.sub(u'\u103b([\u1000\u1003\u1006\u100f\u1011\u1018\u101a\u101e\u101f\u1021\u1010])', u'\u107E\\1',output)
     # -------------------yitgyilonegyitin-----------------------------------------------------------------------------------------------
     output = re.sub(u'\u107e([\u1000\u1003\u1006\u100f\u1011\u1018\u101a\u101e\u101f\u1021\u1010])([\u1036\u102D\u102E\u1064\u108b\u108c\u108d\u108e])',u'\u1080\\1\\2', output)
     # --------------yitgyi-lonetin-waswae-------------------------------------------------------------
     output = re.sub(u'\u107E([\u1000\u1003\u1006\u100f\u1011\u1018\u101a\u101e\u101f\u1021\u1010])\u103C([\u1036\u102D\u102E\u1064\u108b\u108c\u108d\u108e])',u'\u1084\\1\u103C\\2', output)
     # -------------------------yayutgi-waswae-------------------------------------------------------------------------------------------------------------------
     output = re.sub(u'\u107E([\u1000\u1003\u1006\u100f\u1011\u1018\u101a\u101e\u101f\u1021\u1010])\u103C',u'\u1082\\1\u103C', output)
     output = re.sub(u'\u107E\u1010([\u1070-\u107c])', u'\u1082\u1010([\u1070-\u107c])', output)
     #---------------yitlay-lonetin-ttt-----------------------------------------------------------------------------------------------------------------------

     # --------------------------yitlay-waswae-----------------------------------------------------------------------------------------
     output = re.sub(u'\u103B([\u1001\u1002\u1004\u1005\u1007\u1012\u1013\u1015\u1016\u1017\u1019])\u103C', u'\u1081\\1\u103C', output)
     # ---------------------------------yitlay-lonetin-waswae------------------------------------------ -----------------------------------------
     output = re.sub(u'\u103b\u1001\u103C\u1036 ',u'\u1083\u1001\u103C\u1036', output)
     # output = re.sub(u'\u1019\u107B\u102c', u'\u1019\u1093\u102c', output)  # ma-ba
     # output = re.sub(u'\u1005\u1066\u102c', u'\u1005\u1067\u102c', output)  # sa-sal
     # output = re.sub(u'\u1014\u1071\u102c', u'\u108f\u1072\u102c', output)  # na-ta
     # output = re.sub(u'\u1019\u107B\u102c', u'\u1019\u1093\u102c', output)  # ma-ba
     output = re.sub(u'\u100a(\u108a)', u'\u106b\\1', output)  # nya-swae-htoe
     output = re.sub(u'(\u1036)(\u102f)', u'\\2\\1', output)
     output = re.sub(u'\u1025([\u1065\u1068])', u'\u106a\\1', output)
     output = re.sub(u'(\u108f)(\u1075)\u103b', u'\u1081\\1\\2', output)
     return output
def convert(input):
    output = input
    output = replace(output)
    output = decompose(output)
    # output = virtual2logical(output)
    output = shape(output)


    return output
