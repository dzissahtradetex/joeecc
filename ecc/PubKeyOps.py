import hashlib

from .FieldElement import FieldElement
from .AffineCurvePoint import AffineCurvePoint
from .Random import secure_rand_int_between
from . import Tools

class PubKeyOpECDSAExploitReusedNonce(object):
	def ecdsa_exploit_reused_nonce(self, msg1, sig1, msg2, sig2):
		"""Given two different messages msg1 and msg2 and their corresponding
		signatures sig1, sig2, try to calculate the private key that was used
		for signing if during signature generation no unique nonces were
		used."""
		assert(isinstance(msg1, bytes))
		assert(isinstance(msg2, bytes))
		assert(msg1 != msg2)
		assert(sig1.r == sig2.r)

		# Hash the messages
		dig1 = hashlib.new(sig1.hashalg)
		dig1.update(msg1)
		dig1 = dig1.digest()
		dig2 = hashlib.new(sig2.hashalg)
		dig2.update(msg2)
		dig2 = dig2.digest()

		# Calculate hashes of messages
		e1 = Tools.ecdsa_msgdigest_to_int(dig1, self.point.curve.n)
		e2 = Tools.ecdsa_msgdigest_to_int(dig2, self.point.curve.n)

		# Take them modulo n
		e1 = FieldElement(e1, self.point.curve.n)
		e2 = FieldElement(e2, self.point.curve.n)

		(s1, s2) = (FieldElement(sig1.s, self.point.curve.n), FieldElement(sig2.s, self.point.curve.n))
		r = sig1.r

		# Recover (supposedly) random nonce
		nonce = (e1 - e2) // (s1 - s2)

		# Recover private key
		priv = ((nonce * s1) - e1) // r

		return { "nonce": nonce, "privatekey": priv }


class PubKeyOpECDSAVerify(object):
	def ecdsa_verify_hash(self, message_digest, signature):
		"""Verify ECDSA signature over the hash of a message (the message
		digest)."""
		assert(isinstance(message_digest, bytes))
		assert(0 < signature.r < self.curve.n)
		assert(0 < signature.s < self.curve.n)

		# Convert message digest to integer value
		e = Tools.ecdsa_msgdigest_to_int(message_digest, self.curve.n)

		(r, s) = (signature.r, FieldElement(signature.s, self.curve.n))
		w = s.inverse()
		u1 = int(e * w)
		u2 = int(r * w)

		pt = (u1 * self.curve.G) + (u2 * self.point)
		x1 = int(pt.x) % self.curve.n
		return x1 == r

	def ecdsa_verify(self, message, signature):
		"""Verify an ECDSA signature over a message."""
		assert(isinstance(message, bytes))
		digest_fnc = hashlib.new(signature.hashalg)
		digest_fnc.update(message)
		message_digest = digest_fnc.digest()
		return self.ecdsa_verify_hash(message_digest, signature)


class PubKeyOpEDDSAVerify(object):
	def eddsa_verify(self, message, signature):
		"""Verify an EdDSA signature over a message."""
		h = Tools.bytestoint_le(Tools.eddsa_hash(signature.R.eddsa_encode() + self.point.eddsa_encode() + message))
		return (signature.s * self.curve.G) == signature.R + (h * self.point)


class PubKeyOpEDDSAEncode(object):
	def eddsa_encode(self):
		"""Encodes a EdDSA-encoded public key to its serialized (bytes)
		form."""
		return self.point.eddsa_encode()

	@classmethod
	def eddsa_decode(cls, curve, encoded_pubkey):
		"""Decodes a EdDSA-encoded public key from its serialized (bytes)
		form."""
		pubkey = AffineCurvePoint.eddsa_decode(curve, encoded_pubkey)
		return cls(pubkey)

class PubKeyOpECIESEncrypt(object):
	def ecies_encrypt(self, r = None):
		"""Generates a shared secret which can be used to symetrically encrypt
		data that only the holder of the corresponding private key can read.
		The output are two points, R and S: R is the public point that is
		transmitted together with the message while S is the point which
		resembles the shared secret. The receiver can use R together with her
		private key to reconstruct S. A random nonce r can be supplied for this
		function. If it isn't supplied, it is randomly chosen."""

		# Chose a random number
		if r is None:
			r = secure_rand_int_between(1, self.curve.n - 1)

		R = r * self.curve.G
		S = r * self.point

		# Return the publicly transmitted R and the symmetric key S
		return { "R": R, "S": S }
