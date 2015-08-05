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
from ..Ed25519 import Ed25519Params, Ed25519Point, Ed25519Keypair, Ed25519Signature

class Curve25519BasicTests(unittest.TestCase):
	def test_domain(self):
		self.assertEqual(Ed25519Params.B, 256)
		self.assertEqual(Ed25519Params.Q, (2 ** 255) - 19)
		self.assertEqual(Ed25519Params.L, (2 ** 252) + 27742317777372353535851937790883648493)
		self.assertEqual(Ed25519Params.D, -121665 * Ed25519Params.invert(121666))
		self.assertEqual(Ed25519Params.I, pow(2, (Ed25519Params.Q - 1) // 4, Ed25519Params.Q))
		By = 4 * Ed25519Params.invert(5)
		Bx = Ed25519Point._recoverx(By)
		B = Ed25519Point(Bx, By)
		self.assertEqual(B, Ed25519Params.PB)

	def test_sign_verify(self):
		keypair = Ed25519Keypair.genkeypair()

		msg = b"foobar"
		signature = keypair.sign_msg(msg)

		self.assertTrue(keypair.public.verify_msg(msg, signature))
		self.assertFalse(keypair.public.verify_msg(msg + b"x", signature))

	def test_sig_encode_decode(self):
		keypair = Ed25519Keypair.genkeypair()
		msg = b"foobar"
		signature = keypair.sign_msg(msg)

		encoded_signature = signature.encode()
		decoded_signature = Ed25519Signature.decode(encoded_signature)
		self.assertEqual(decoded_signature, signature)
		self.assertTrue(keypair.public.verify_msg(msg, signature))
		self.assertTrue(keypair.public.verify_msg(msg, decoded_signature))


	def test_scalarmult(self):
		basepoint = Ed25519Params.PB
		expected_results = [
			(0, Ed25519Point(0x0, 0x1)),
			(1, Ed25519Point(0x216936d3cd6e53fec0a4e231fdd6dc5c692cc7609525a7b2c9562d608f25d51a, 0x6666666666666666666666666666666666666666666666666666666666666658)),
			(2, Ed25519Point(0x36ab384c9f5a046c3d043b7d1833e7ac080d8e4515d7a45f83c5a14e2843ce0e, 0x2260cdf3092329c21da25ee8c9a21f5697390f51643851560e5f46ae6af8a3c9)),
			(3, Ed25519Point(0x67ae9c4a22928f491ff4ae743edac83a6343981981624886ac62485fd3f8e25c, 0x1267b1d177ee69aba126a18e60269ef79f16ec176724030402c3684878f5b4d4)),
			(4, Ed25519Point(0x203da8db56cff1468325d4b87a3520f91a739ec193ce1547493aa657c4c9f870, 0x47d0e827cb1595e1470eb88580d5716c4cf22832ea2f0ff0df38ab61ca32112f)),
			(5, Ed25519Point(0x49fda73eade3587bfcef7cf7d12da5de5c2819f93e1be1a591409cc0322ef233, 0x5f4825b298feae6fe02c6e148992466631282eca89430b5d10d21f83d676c8ed)),
			(6, Ed25519Point(0x4c9797ba7a45601c62aeacc0dd0a29bea1e599826c7b4427783a741a7dcbf23d, 0x54de3fc2886d8a11db709a7fd4f7d77f9417c06944d6b60c1d27ad0f9497ef4)),
			(7, Ed25519Point(0x14568685fcf4bd4ee9e3ee194b1d810783e809f3bbf1ce955855981af50e4107, 0x31c563e32b47d52f87ce6468dd36ad41f0882b46f7abf23d12c4c4b59f4062b8)),
			(8, Ed25519Point(0x6742e15f97d771b642862d5cf84ecf93eb3ac67b80698b993b87fdbc08a584c8, 0x21d30600c9e573796ead6f09668af38f81783cfc621ee4931e2f5ba9fc37b9b4)),
			(9, Ed25519Point(0x357cc970c80071651bf336e06f9422b886d80e5c2e4e0294d3e023065185715c, 0x7f3d23c2c2dd0df4b2befce956f2d2fd1f789013236e4430c74e44845522f1c0)),
			(10, Ed25519Point(0x602c797e30ca6d754470b60ed2bc8677207e8e4ed836f81444951f224877f94f, 0x637ffcaa7a1b2477c8e44d54c898bfcf2576a6853de0e843ba8874b06ae87b2c)),
			(11, Ed25519Point(0x14e528b1154be417b6cf078dd6712438d381a5b2c593d552ff2fd2c1207cf3cb, 0x2d9082313f21ab975a6f7ce340ff0fce1258591c3c9c58d4308f2dc36a033713)),
			(12, Ed25519Point(0x4719e17e016e5d355ecf70e00ca249db3295bf2385c13b42ae62fe6678f0902d, 0x4070ce608bce8022e71d6c4e637825b856487eb45273966733d281dc2e2de4f9)),
			(13, Ed25519Point(0x107427e0d5f366ccdb33adf0282d304f8843e3e88d22b7b83780e073b7c05fed, 0x12dbb00ded538b7478466022d2da89b83740cfb2289a272387efe1aeea401f80)),
			(14, Ed25519Point(0x205f3b42f5884aaf048c7a895ccabb15d8dee6d83e39832aa38e7353b58515b9, 0x4e50256f50c4cb8115bad17acbb702bfa74898e819b6265c8369fd98899c2839)),
			(15, Ed25519Point(0x4f162deaec2ec435dc5ac6f95d20419ed9631374770189cb90617f3e66a18dc1, 0x12cbfb2d04ff22f55162f70164d29331ace5af18a19a9aa1946d4cc4ad2e5cdf)),
			(16, Ed25519Point(0x23a4860627e53aeeb8e22b1508249c9109578d33e7bf237459b2596d6c28f9f8, 0x709696f2827fc3729f980f2e3aad6e78b06a11ff8e079c27d87aab37c16727eb)),
			(17, Ed25519Point(0x7dc52d5a7db816e9b850741ea2fd72918d94985b85a20b4dc5597853a876df6a, 0x6f6d2bca60003ef9f24ac245cc919fb717b188723b34f901cd6cfe9bec97be04)),
			(18, Ed25519Point(0x1368877f4867292aaf9c0393bc2b0e869158987876b8001297b644a64bb10b96, 0x2e1126847e0bd8987de8e8ea8a96c3a5bc810e4ed6d496b0354e3e90e075b04a)),
			(19, Ed25519Point(0x1d81f74a5ba45c7022e8c140d763b9c1b0e281a5304696e74f791a3a04a94472, 0x3f185a93d95a4347227c5bb6ddd65cf42e1830823f435f3083fe6102691d55b9)),
			(20, Ed25519Point(0x673c65caedd698b94f5bbd757df73a9e6985150ecd4a2135a058e273ab4cf9af, 0x136cebacb6260a9d5e6a3e3171c535f0be71cfbe16a960b9dd317bda6f3c5a38)),
			(21, Ed25519Point(0x6f0ac78e5eb90e87958588f9d47541edf252cb1dde3d073cc45e3e7ef9365716, 0x6628d116b7975ae5f323e5ddf4f8cc35ae06d5c5c7d8a56effc66051336d289e)),
			(22, Ed25519Point(0x1e029b938c915f04b0c73d7338516ad51e376a9afa7de7c8c077622c2aec2f7a, 0x6bfc9472cde96427c4ac03f52e0d2b3cdce6566535dcee5a85a6a44b8975f24)),
			(23, Ed25519Point(0x2188ac423c67db5625915e05222a391bcaf91f05d9b7cc2cab5798b2d2e14d95, 0x23240c559c57b79a4df69a23fc46e50504277b1fa49369ab663d79782b33c0ee)),
			(24, Ed25519Point(0x70985f28875d4006e0968d9c952d799e610ed8e052a9a10e9677c71ee8886b81, 0x604e1b93c877b9896dca33cf8a2093cddf9fd21208c20d08e7b2444fed7b79f1)),
			(25, Ed25519Point(0x794241471ed9ceb009384b370cb8790fca98552ecb822dc06b19362c36353455, 0x71e918c03cdfca7207772e8d18ee8f9d92d79a0a83f378912362bc68d311dcd0)),
			(26, Ed25519Point(0x7982f658573d3d2519905e0d62c9469b667197fd602c7be16d5aa882178d4e9, 0x6c66e7e8eab0cfc9e9a180a04d91d6e5c9709380b7d63eb011dfe9afa1fa1a0c)),
			(27, Ed25519Point(0x163bc180c22dfc5da23c5c052107bba93a88b4360aa1d4e729611d8f5a7f8079, 0x631107a6ba83f7458194b9766a0a54f638ca20daf800384dbae1498677501939)),
			(28, Ed25519Point(0x47827fc68c31ec77e418a77ed5281a3c85bdbab18d755b18bcdf5b549748291, 0x7324ec33cef7b3ea9331141ae90f02866ce1bcfcdcd8c2d0191002f02078f0bb)),
			(29, Ed25519Point(0x39a32a30f3eb1da0eb7e3903b8ace3da3890b24b61a3a9e79db663b5db0f7a5d, 0x4d4c54675dc1f1c9a1af9ca0010045dc803c16af345823136dd203715d67c491)),
			(30, Ed25519Point(0x7e40e656adbd6aa0cb203f337dd19d441336400f59e341c837ebd71b7881e1e4, 0x342740ff1d2cc47aefed1e9b1c1b387cad3ff6f842729e20a414557407d2f3e4)),
			(31, Ed25519Point(0x38085391a0e2831f59c33fcce7591515784d359925f11ff958e0e4658efac0e9, 0x42918001a829f49b5634e34ab7fac21b30e24660669ed91955cc31944a19e62a)),
			(32, Ed25519Point(0x39cf6c6917421af98582561d0b39567de6033190f97852fc4fdd40f6977e4f26, 0x4434a90ee12cce6b7ade93ecc0f88b78b41205e74c8c4038f92d394f3a06d269)),
			(33, Ed25519Point(0x5e3573b049d6135ffbbbbd9a480617434f2455b4a591f719e91153eeb75a32a1, 0x54bc665420c789da1105d53983c1a0fc33bcc2690cd9b37d6566e21a85892871)),
			(34, Ed25519Point(0x43b314af3fad092a519dd4c1e4d90f6e6909eee8d3f9e99ca245db9d4de0a886, 0xaebdaf9a47afa9625f4a71b1f2d9b79da982c3139dbdbe3dbefa92d62333393)),
			(100, Ed25519Point(0x4b87a1147457b111116b878cfc2312de451370ac38fe8690876ef6ac346fd47, 0x405ea0cdd414bda960318b3108769a8928a25b756c372b254c69c78ea2fd81c5)),
			(256, Ed25519Point(0x5e7e07ed4e1decbfe6e9cbc126905449d4b578fbb561576d20b8bcdd0cc2a556, 0xf55755c51f102796bf5ebaa81d3260e7d1b3d9ac127d9a80e142031566cf6c7)),
			(1000, Ed25519Point(0x7d729f34487672ba293b953eaf0c41221c762b90f195f8e13e0e76abef68ce7e, 0xee1a16689ad85c7246c61a7192b28ba997c449bc5fe43aeaf943a3783aacae7)),
			(4096, Ed25519Point(0x7d13c0248b891b47eb524f2692008e2f97b199bac426cb5902b9003a29ded6ea, 0x59a976ab2c01a81a91f1a56c75ccc77a9e1e9e878e9fe9c3952080a6805b20d5)),
			(89478485, Ed25519Point(0x16d82ba2233fffa25a66fbf5da00bd6e761ecb5128e8404df22a0be5295a0a79, 0x5701ebcb79787ef64057ee32ee5bf0e1e127d7a082b79bd0a4c1dd6bd247052)),
			(178956970, Ed25519Point(0x6d6f8c2593b33ca1ccd705ed3b722645b6204f7693d98ff131767df19cf7cc65, 0x7bf3279fe978d59fd7a869995107b50fe64d00e7fd17b97ff5b73b05d4256141)),
			(269488144, Ed25519Point(0x5b4637afc2317d0549781d2aa9febdfa2be765e1352dd63c328da9c4bb7cd014, 0x518e8a42479c4ea248d963342f85968be9c75766689483cd404f5ab9f1e6f7eb)),
			(1437226410, Ed25519Point(0x3aabbf7c82aa6bd17fbc24c0e701348f3dde1252a68302fb01a43058abc1bae5, 0x24f569c61916a6a639aa15b71e19d3d4dd1843c742bdd6be1bf0faed7ff3208f)),
			(4294967295, Ed25519Point(0x2e768d4b624578616c2bf1694a975337fb8729c87e08957d284bbc79b401682, 0x4eb4a25a350c7c9a33282c700da2c187efb514fc056b92f6d249db423be1fb3c)),
			(18446744073709551616, Ed25519Point(0x6222bd88bf2df9d5d44b60cfb4a08a960078db7ed51a35eb3e0b6b8ff4eda202, 0x325bb42ea4ed025dd6bdaed261b7c4f5410b608ba902b068f1efa5782e45313)),
			(2833419889721787128217, Ed25519Point(0x2462d10f10d73e1ee34f23e8995c6b335134764e3edb18cd51aa064815da074e, 0x3e8e3dd79f911bfe8f1be627201c60462334431f6bf712615ed27962dd5ec90b)),
			(309485009821345068724781055, Ed25519Point(0x674ad10bbd2df4ce13533bcfd25afebe1d55690377fff91b89f1c1bbf44e6f7, 0x5d78bffab87940cebd0ce34488e0d49d4dd1cc5820ca6780e6af721f6d389c04)),
		]
		self.assertTrue(basepoint.oncurve())
		for (scalar, expected_result_point) in expected_results:
			result_point = scalar * basepoint
			self.assertTrue(result_point.oncurve())
			#print("(%d, Ed25519Point(0x%x, 0x%x))," % (scalar, result_point.x, result_point.y))
			self.assertEqual(expected_result_point, result_point)
