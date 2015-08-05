#
#	joeecc - A small Elliptic Curve Cryptography Demonstration.
#	Copyright (C) 2011-2015 Johannes Bauer
#
#	This file is part of joeecc.
#
#	joeecc is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; this program is ONLY licensed under
#	version 3 of the License, later versions are explicitly excluded.
#
#	joeecc is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with joeecc; if not, write to the Free Software
#	Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#	Johannes Bauer <JohannesBauer@gmx.de>
#

import unittest
from ..ModInt import ModInt

class ModIntTests(unittest.TestCase):
	def test_basic(self):
		a = ModInt(15, 23)
		b = ModInt(20, 23)
		self.assertEqual(a + b, ModInt(12, 23))
		self.assertEqual(b + a, ModInt(12, 23))
		self.assertEqual(a + b - b, a)
		self.assertEqual(b + a - a, b)

		self.assertEqual(a - b, ModInt(18, 23))
		self.assertEqual(a - b + b, a)
		self.assertEqual(b - a + a, b)

		self.assertEqual(a * b, ModInt(1, 23))
		self.assertEqual(b * a, ModInt(1, 23))
		self.assertEqual(a * b // b, a)
		self.assertEqual(b * a // a, b)

		self.assertEqual(a // b, ModInt(18, 23))
		self.assertEqual(a // b * b, a)
		self.assertEqual(b // a * a, b)

		self.assertEqual(int(ModInt(2, 101) ** 473289743783748378), 21)
		self.assertEqual(int(ModInt(3, 101) ** 473289743783748378), 33)
		self.assertEqual(int(ModInt(4, 101) ** 473289743783748378), 37)
		self.assertEqual(int(ModInt(5, 101) ** 473289743783748378), 24)

		x = ModInt(1000, 2003)
		s = x.sqrt()
		assert(s)
		(s1, s2) = s
		self.assertEqual(s1 * s1, x)
		self.assertEqual(s2 * s2, x)

	def test_exp(self):
		self.assertEqual(int(ModInt(19, 23) ** 5), 11)
		self.assertEqual(int(ModInt(19, 23) ** 12), 4)
		self.assertEqual(int(ModInt(14, 23) ** 20), 2)
		self.assertEqual(int(ModInt(1, 23) ** 19), 1)
		self.assertEqual(int(ModInt(18, 23) ** 17), 8)
		self.assertEqual(int(ModInt(18, 23) ** 20), 12)
		self.assertEqual(int(ModInt(18, 23) ** 17), 8)
		self.assertEqual(int(ModInt(20, 23) ** 12), 3)
		self.assertEqual(int(ModInt(3, 23) ** 17), 16)
		self.assertEqual(int(ModInt(14, 23) ** 3), 7)
		self.assertEqual(int(ModInt(4, 23) ** 4), 3)
		self.assertEqual(int(ModInt(10, 23) ** 4), 18)
		self.assertEqual(int(ModInt(18, 23) ** 2), 2)
		self.assertEqual(int(ModInt(10, 23) ** 17), 17)
		self.assertEqual(int(ModInt(3, 23) ** 9), 18)
		self.assertEqual(int(ModInt(6, 23) ** 10), 4)
		self.assertEqual(int(ModInt(22, 23) + 3), 2)
		self.assertEqual(int(ModInt(16, 23) + 16), 9)
		self.assertEqual(int(ModInt(22, 23) + 10), 9)
		self.assertEqual(int(ModInt(6, 23) + 22), 5)
		self.assertEqual(int(ModInt(6, 23) + 13), 19)
		self.assertEqual(int(ModInt(20, 23) + 17), 14)
		self.assertEqual(int(ModInt(3, 23) + 2), 5)
		self.assertEqual(int(ModInt(6, 23) + 21), 4)
		self.assertEqual(int(ModInt(16, 23) + 6), 22)
		self.assertEqual(int(ModInt(5, 23) + 6), 11)
		self.assertEqual(int(ModInt(9, 23) + 10), 19)
		self.assertEqual(int(ModInt(18, 23) + 17), 12)
		self.assertEqual(int(ModInt(2, 23) + 15), 17)
		self.assertEqual(int(ModInt(14, 23) + 21), 12)
		self.assertEqual(int(ModInt(15, 23) + 2), 17)
		self.assertEqual(int(ModInt(20, 23) + 20), 17)
		self.assertEqual(int(ModInt(1, 23) - 3), 21)
		self.assertEqual(int(ModInt(12, 23) - 9), 3)
		self.assertEqual(int(ModInt(19, 23) - 3), 16)
		self.assertEqual(int(ModInt(8, 23) - 10), 21)
		self.assertEqual(int(ModInt(4, 23) - 9), 18)
		self.assertEqual(int(ModInt(21, 23) - 20), 1)
		self.assertEqual(int(ModInt(17, 23) - 17), 0)
		self.assertEqual(int(ModInt(8, 23) - 17), 14)
		self.assertEqual(int(ModInt(18, 23) - 9), 9)
		self.assertEqual(int(ModInt(15, 23) - 18), 20)
		self.assertEqual(int(ModInt(7, 23) - 5), 2)
		self.assertEqual(int(ModInt(14, 23) - 21), 16)
		self.assertEqual(int(ModInt(1, 23) - 5), 19)
		self.assertEqual(int(ModInt(13, 23) - 3), 10)
		self.assertEqual(int(ModInt(2, 23) - 1), 1)
		self.assertEqual(int(ModInt(13, 23) - 15), 21)
		self.assertEqual(int(ModInt(13, 23) // 16), 8)
		self.assertEqual(int(ModInt(14, 23) // 8), 19)
		self.assertEqual(int(ModInt(2, 23) // 17), 15)
		self.assertEqual(int(ModInt(0, 23) // 5), 0)
		self.assertEqual(int(ModInt(9, 23) // 6), 13)
		self.assertEqual(int(ModInt(14, 23) // 17), 13)
		self.assertEqual(int(ModInt(1, 23) // 11), 21)
		self.assertEqual(int(ModInt(14, 23) // 9), 22)
		self.assertEqual(int(ModInt(9, 23) // 16), 2)
		self.assertEqual(int(ModInt(1, 23) // 12), 2)
		self.assertEqual(int(ModInt(13, 23) // 21), 5)
		self.assertEqual(int(ModInt(15, 23) // 19), 2)
		self.assertEqual(int(ModInt(5, 23) // 5), 1)
		self.assertEqual(int(ModInt(8, 23) // 6), 9)
		self.assertEqual(int(ModInt(19, 23) // 8), 11)
		self.assertEqual(int(ModInt(4, 23) // 10), 5)
		self.assertEqual(int(ModInt(3, 101) ** 46), 96)
		self.assertEqual(int(ModInt(17, 101) ** 89), 6)
		self.assertEqual(int(ModInt(83, 101) ** 97), 35)
		self.assertEqual(int(ModInt(64, 101) ** 30), 84)
		self.assertEqual(int(ModInt(61, 101) ** 56), 56)
		self.assertEqual(int(ModInt(61, 101) ** 9), 15)
		self.assertEqual(int(ModInt(39, 101) ** 28), 84)
		self.assertEqual(int(ModInt(40, 101) ** 32), 79)
		self.assertEqual(int(ModInt(69, 101) ** 98), 65)
		self.assertEqual(int(ModInt(74, 101) ** 56), 58)
		self.assertEqual(int(ModInt(73, 101) ** 0), 1)
		self.assertEqual(int(ModInt(8, 101) ** 86), 47)
		self.assertEqual(int(ModInt(56, 101) ** 92), 16)
		self.assertEqual(int(ModInt(60, 101) ** 25), 91)
		self.assertEqual(int(ModInt(86, 101) ** 84), 56)
		self.assertEqual(int(ModInt(94, 101) ** 11), 50)
		self.assertEqual(int(ModInt(91, 101) + 52), 42)
		self.assertEqual(int(ModInt(75, 101) + 79), 53)
		self.assertEqual(int(ModInt(42, 101) + 43), 85)
		self.assertEqual(int(ModInt(75, 101) + 82), 56)
		self.assertEqual(int(ModInt(99, 101) + 63), 61)
		self.assertEqual(int(ModInt(10, 101) + 49), 59)
		self.assertEqual(int(ModInt(8, 101) + 49), 57)
		self.assertEqual(int(ModInt(74, 101) + 81), 54)
		self.assertEqual(int(ModInt(53, 101) + 19), 72)
		self.assertEqual(int(ModInt(51, 101) + 65), 15)
		self.assertEqual(int(ModInt(80, 101) + 56), 35)
		self.assertEqual(int(ModInt(55, 101) + 61), 15)
		self.assertEqual(int(ModInt(53, 101) + 80), 32)
		self.assertEqual(int(ModInt(58, 101) + 2), 60)
		self.assertEqual(int(ModInt(96, 101) + 74), 69)
		self.assertEqual(int(ModInt(83, 101) + 93), 75)
		self.assertEqual(int(ModInt(17, 101) - 27), 91)
		self.assertEqual(int(ModInt(34, 101) - 1), 33)
		self.assertEqual(int(ModInt(63, 101) - 23), 40)
		self.assertEqual(int(ModInt(74, 101) - 76), 99)
		self.assertEqual(int(ModInt(64, 101) - 65), 100)
		self.assertEqual(int(ModInt(29, 101) - 25), 4)
		self.assertEqual(int(ModInt(0, 101) - 69), 32)
		self.assertEqual(int(ModInt(23, 101) - 40), 84)
		self.assertEqual(int(ModInt(23, 101) - 46), 78)
		self.assertEqual(int(ModInt(31, 101) - 67), 65)
		self.assertEqual(int(ModInt(17, 101) - 100), 18)
		self.assertEqual(int(ModInt(11, 101) - 22), 90)
		self.assertEqual(int(ModInt(26, 101) - 6), 20)
		self.assertEqual(int(ModInt(5, 101) - 21), 85)
		self.assertEqual(int(ModInt(19, 101) - 48), 72)
		self.assertEqual(int(ModInt(52, 101) - 34), 18)
		self.assertEqual(int(ModInt(70, 101) // 84), 85)
		self.assertEqual(int(ModInt(42, 101) // 92), 29)
		self.assertEqual(int(ModInt(9, 101) // 11), 10)
		self.assertEqual(int(ModInt(87, 101) // 28), 50)
		self.assertEqual(int(ModInt(99, 101) // 10), 20)
		self.assertEqual(int(ModInt(21, 101) // 89), 74)
		self.assertEqual(int(ModInt(51, 101) // 29), 54)
		self.assertEqual(int(ModInt(10, 101) // 99), 96)
		self.assertEqual(int(ModInt(2, 101) // 64), 60)
		self.assertEqual(int(ModInt(98, 101) // 79), 69)
		self.assertEqual(int(ModInt(24, 101) // 6), 4)
		self.assertEqual(int(ModInt(65, 101) // 34), 94)
		self.assertEqual(int(ModInt(54, 101) // 59), 42)
		self.assertEqual(int(ModInt(96, 101) // 55), 55)
		self.assertEqual(int(ModInt(27, 101) // 94), 25)
		self.assertEqual(int(ModInt(84, 101) // 36), 36)

	def test_exp_large(self):
		self.assertEqual(int(ModInt(45329398547330232435475204068501392759, 170141183460469231731687303715884105727) ** 23973357120524123688767677450838423404), 110625867554914261405235347771839473528)
		self.assertEqual(int(ModInt(11096317216645540333687625413300885798, 170141183460469231731687303715884105727) ** 18350067802502312484374146949394432005), 158114342748150869616337867244357893527)
		self.assertEqual(int(ModInt(105193728357093738052129993765343901393, 170141183460469231731687303715884105727) ** 28949868692861977936123607826349169475), 97469690940520651844215943924110140562)
		self.assertEqual(int(ModInt(111055120216185479216549737895719889955, 170141183460469231731687303715884105727) ** 116796601068080310567096901526856239558), 143288233252562942061753559724655924484)
		self.assertEqual(int(ModInt(118573387676321580035191294408665717202, 170141183460469231731687303715884105727) ** 118468724281467837804867816531495356951), 25384169807760052976344572805881045078)
		self.assertEqual(int(ModInt(8453841496330693524076697666656810794, 170141183460469231731687303715884105727) ** 50936640660640246195941254951084298956), 89980634104306998553990016030498527717)
		self.assertEqual(int(ModInt(3126171733569194607538752261348981043, 170141183460469231731687303715884105727) ** 89540119583121092487935700750509976672), 76789997572366225883637242904225680866)
		self.assertEqual(int(ModInt(87408682732145428292803410374197679069, 170141183460469231731687303715884105727) ** 73294773716505932813644442251790490252), 30190042501166266896046398631549945852)
		self.assertEqual(int(ModInt(133656934690862077279671066447610175665, 170141183460469231731687303715884105727) ** 167537713805753850504640915450779147113), 35661701185378333693521640055115158413)
		self.assertEqual(int(ModInt(98916010222012311006195259181587327980, 170141183460469231731687303715884105727) ** 43646275964617627585990852451242571176), 113494102718163694969171327315905227995)
		self.assertEqual(int(ModInt(63972045063721755734341771679385747085, 170141183460469231731687303715884105727) ** 54196951232327114864338986457233698387), 45674328667154461933222295595156598033)
		self.assertEqual(int(ModInt(30148817818891517113115639309493720746, 170141183460469231731687303715884105727) ** 79460949570435413221573946148779586587), 44923150826036815903390792324737278379)
		self.assertEqual(int(ModInt(14365600219786747087436337553351351653, 170141183460469231731687303715884105727) ** 112788553884177448692041938153888362529), 66193098425771394236023545922584075435)
		self.assertEqual(int(ModInt(107876445691250920950383433660235638727, 170141183460469231731687303715884105727) ** 63175031301901038638538102811208915385), 43293126929407246606869088225298896601)
		self.assertEqual(int(ModInt(656600543513838100592447618947479104, 170141183460469231731687303715884105727) ** 9316063397339917001814241291992219008), 125439992161573737926617751254277143302)
		self.assertEqual(int(ModInt(8515732054006400859632859854758105270, 170141183460469231731687303715884105727) ** 154793104050145597808664399207755838006), 80169600713538798061924004526058523555)
		self.assertEqual(int(ModInt(136632104926671259150658557204382855307, 170141183460469231731687303715884105727) + 140120717775505985648375652851614073638), 106611639241708013067346906340112823218)
		self.assertEqual(int(ModInt(38621638155689111539732260997177321764, 170141183460469231731687303715884105727) + 148910265184787996364066007383537138821), 17390719880007876172110964664830354858)
		self.assertEqual(int(ModInt(104060080608448838825399857423116490745, 170141183460469231731687303715884105727) + 15866546562265594892647176808646907722), 119926627170714433718047034231763398467)
		self.assertEqual(int(ModInt(135283065963309348867343419514142663254, 170141183460469231731687303715884105727) + 19283766952051149519051861565933157158), 154566832915360498386395281080075820412)
		self.assertEqual(int(ModInt(129120665366701743301002608695639274872, 170141183460469231731687303715884105727) + 146665354566953345487941378645052581274), 105644836473185857057256683624807750419)
		self.assertEqual(int(ModInt(30274191172009551312658490814045446047, 170141183460469231731687303715884105727) + 116086245620507866092530122516684873230), 146360436792517417405188613330730319277)
		self.assertEqual(int(ModInt(92821078054382328459521199148602253460, 170141183460469231731687303715884105727) + 21453897095620677846008191705950115569), 114274975150003006305529390854552369029)
		self.assertEqual(int(ModInt(113196838221973538581294430840107593118, 170141183460469231731687303715884105727) + 7120339564147990318433671914714064895), 120317177786121528899728102754821658013)
		self.assertEqual(int(ModInt(69114258914682490045468116259427841467, 170141183460469231731687303715884105727) + 1991712575999046718015252192095523128), 71105971490681536763483368451523364595)
		self.assertEqual(int(ModInt(109545890323014722350320179132149710664, 170141183460469231731687303715884105727) + 163857925843134909444560687945185850758), 103262632705680400063193563361451455695)
		self.assertEqual(int(ModInt(71961452646098185936710794302606932344, 170141183460469231731687303715884105727) + 123269683332847795071057959722788502465), 25089952518476749276081450309511329082)
		self.assertEqual(int(ModInt(77479169662442455854731274618943998038, 170141183460469231731687303715884105727) + 59269467271209903523116433439279610302), 136748636933652359377847708058223608340)
		self.assertEqual(int(ModInt(4000584729672543964294135190189425293, 170141183460469231731687303715884105727) + 124633593148062781483437344640225262257), 128634177877735325447731479830414687550)
		self.assertEqual(int(ModInt(44944448567903287336360285271047036054, 170141183460469231731687303715884105727) + 42934577016844380890687405816579749647), 87879025584747668227047691087626785701)
		self.assertEqual(int(ModInt(15792232760272254417367391186546298212, 170141183460469231731687303715884105727) + 92629712458496110182888116723592226146), 108421945218768364600255507910138524358)
		self.assertEqual(int(ModInt(16744519022997425945591286216498857854, 170141183460469231731687303715884105727) + 60097347038133774973283644794283514608), 76841866061131200918874931010782372462)
		self.assertEqual(int(ModInt(106152913003121313917911941285262726732, 170141183460469231731687303715884105727) - 87195086898390730358371679807644887247), 18957826104730583559540261477617839485)
		self.assertEqual(int(ModInt(45687281695846974635956411826165480656, 170141183460469231731687303715884105727) - 162213007661054927807473821400626255209), 53615457495261278560169894141423331174)
		self.assertEqual(int(ModInt(15257030762745645948491801499137632857, 170141183460469231731687303715884105727) - 7418989103289055301648335264728502394), 7838041659456590646843466234409130463)
		self.assertEqual(int(ModInt(106611804313960378162812847699836663716, 170141183460469231731687303715884105727) - 140665279939978230481300773387419903967), 136087707834451379413199378028300865476)
		self.assertEqual(int(ModInt(133838733144617943706855944584448231448, 170141183460469231731687303715884105727) - 58467537767098938120996889592931844682), 75371195377519005585859054991516386766)
		self.assertEqual(int(ModInt(95450444652509275212240754918440080423, 170141183460469231731687303715884105727) - 76033833226821264963537581552025667121), 19416611425688010248703173366414413302)
		self.assertEqual(int(ModInt(55367802431278463738034647542577651919, 170141183460469231731687303715884105727) - 18005316014316544179988151202837054857), 37362486416961919558046496339740597062)
		self.assertEqual(int(ModInt(125163033529513795858921820373190159377, 170141183460469231731687303715884105727) - 54475023212382152652298561017006898212), 70688010317131643206623259356183261165)
		self.assertEqual(int(ModInt(64661737350159901732983806959842729302, 170141183460469231731687303715884105727) - 45176078586475432784323819536299959164), 19485658763684468948659987423542770138)
		self.assertEqual(int(ModInt(107632274661578650916779608041071393978, 170141183460469231731687303715884105727) - 7589249240176203346240012712050723130), 100043025421402447570539595329020670848)
		self.assertEqual(int(ModInt(164830283351449861312560615156382133149, 170141183460469231731687303715884105727) - 38881694406333428951872876266198212847), 125948588945116432360687738890183920302)
		self.assertEqual(int(ModInt(145614266142808620579696974736201112667, 170141183460469231731687303715884105727) - 98440694630752268006876234464090231362), 47173571512056352572820740272110881305)
		self.assertEqual(int(ModInt(64490301041749803164735778256826041594, 170141183460469231731687303715884105727) - 154475020120574089642783104165898103822), 80156464381644945253639977806812043499)
		self.assertEqual(int(ModInt(115379742931322370510762640452114179672, 170141183460469231731687303715884105727) - 133011663520640094345715915522570422404), 152509262871151507896734028645427862995)
		self.assertEqual(int(ModInt(130168725802159753553417756246748506660, 170141183460469231731687303715884105727) - 123362500924770089422799946293438475643), 6806224877389664130617809953310031017)
		self.assertEqual(int(ModInt(38798461907097343442844080195939551410, 170141183460469231731687303715884105727) - 112708521425705507018391248752189820480), 96231123941861068156140135159633836657)
		self.assertEqual(int(ModInt(169635720912393385456311228029418721549, 170141183460469231731687303715884105727) // 5125980552749438842852750418916796525), 107646814503452217117283843436202007165)
		self.assertEqual(int(ModInt(107882884231390003679995023970257678803, 170141183460469231731687303715884105727) // 151763708725767129083405213066672737954), 82889642741106710193739689277845192084)
		self.assertEqual(int(ModInt(94241150083544367565611230042352711183, 170141183460469231731687303715884105727) // 75036922656613131426921476208210274563), 153955148262808660845602842965393338168)
		self.assertEqual(int(ModInt(100495636541697890794063010067874869700, 170141183460469231731687303715884105727) // 106212552742865435371691465447091858111), 102733954716615225361079724718408770035)
		self.assertEqual(int(ModInt(108839390278524717297468354520537885106, 170141183460469231731687303715884105727) // 100040281751285786749878371784622849611), 9321205938575402744328233089858754436)
		self.assertEqual(int(ModInt(117511643750848179104389378603022818870, 170141183460469231731687303715884105727) // 28480687143633577095730875558790621479), 57299652569101370544286329898224085396)
		self.assertEqual(int(ModInt(114994670019423707745148692983614490300, 170141183460469231731687303715884105727) // 58187529989294639311237210961779471414), 147155163523377143250121888935297674289)
		self.assertEqual(int(ModInt(107318671941012978233844525463904778624, 170141183460469231731687303715884105727) // 123654017802499232542387840704798462996), 106439330727364375694930105937996868447)
		self.assertEqual(int(ModInt(132944172934937854746756050726407372454, 170141183460469231731687303715884105727) // 154276342736674962621014167992354449125), 27903634466374769281978778767278769694)
		self.assertEqual(int(ModInt(25662843858972547447022692024664104224, 170141183460469231731687303715884105727) // 158748231144141156279066123094923903399), 29201388396028385555406537979410867836)
		self.assertEqual(int(ModInt(113465879405035451701821832943645298828, 170141183460469231731687303715884105727) // 120460349755642205984621606946479112366), 71248519280901116320580234730652271391)
		self.assertEqual(int(ModInt(8334941716861450887188645947309029530, 170141183460469231731687303715884105727) // 50138957532465094846999960859152732423), 101160997466615734206526379505805888684)
		self.assertEqual(int(ModInt(26920812363722003034821933852333560994, 170141183460469231731687303715884105727) // 102212722464591334411157093773616161792), 25692793581031235137954843595156037418)
		self.assertEqual(int(ModInt(134287335350600618899342739598509916590, 170141183460469231731687303715884105727) // 156617330166893666970965386415918144196), 144891184299551137640458323577893882867)
		self.assertEqual(int(ModInt(128108665602581376305705079145332638442, 170141183460469231731687303715884105727) // 151184636384337255092177528680036397052), 7671040721822175495116587335138601275)
		self.assertEqual(int(ModInt(14455986081875437153071558887236407967, 170141183460469231731687303715884105727) // 154668195530012920576141463919463625172), 157598580654627146019924599576602305897)
