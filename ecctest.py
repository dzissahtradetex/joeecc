#!/usr/bin/python3
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

import sys

from ecc import AffineCurvePoint, EllipticCurveFP, getcurvebyname

def separator():
	print("-" * 150)


usedcurve = getcurvebyname("secp112r1")
#usedcurve = getcurvebyname("brainpoolP160r1")
#usedcurve = getcurvebyname("secp192k1")
print("Selected curve parameters")
print(str(usedcurve))
separator()

keypair = usedcurve.genknownkeypair(0x12345)
print("Generated keypair")
print(str(keypair))
separator()


########################### Encryption example ###########################
e = keypair.encrypt()
print("Encryption")
print("Transmitted R  :", e["R"])
print("Symmetric key S:", e["S"])
separator()

# And decrypt at receiver
print("Decryption")
recovered_s = keypair.decrypt(e["R"])
print("Recovered S    :", recovered_s)
separator()


########################### Signature example ###########################
print("Signing message")
signature = keypair.sign_msg(b"foobar", "sha1")
print("r:", signature.r)
print("s:", signature.s)
separator()

print("Verification of signature")
print("Original message:", keypair.verify_msg(b"foobar", signature))
print("Modified message:", keypair.verify_msg(b"foobaz", signature))
separator()


########################### Identical-nonce-in-signature exploit ###########################
print("Generating signatures with identical nonces for exploitation")
signature1 = keypair.sign_msg(b"foobar", "sha1", k = 123456)
signature2 = keypair.sign_msg(b"foobaz", "sha1", k = 123456)

print("r1:", signature1.r)
print("s1:", signature1.s)
print("r2:", signature2.r)
print("s2:", signature2.s)
recvr = usedcurve.exploitidenticalnoncesig(b"foobar", signature1, b"foobaz", signature2)

print("Recovered nonce      :", recvr["nonce"])
print("Recovered private key: 0x%x" % (int(recvr["privatekey"])))
separator()


########################### Finding arbitrary points on the curve ###########################
x = 123456
print("Finding points on the curve with x == %d" % (x))
points = usedcurve.getpointwithx(x)
if points:
	(pt1, pt2) = points
	print("Point 1:", pt1)
	print("Point 2:", pt2)
	print("On curve?", pt1.oncurve(), pt2.oncurve())
else:
	print("No point found")
separator()


########################### Generating tiny curve for example purposes ###########################
print("Generating a tiny curve")
tinycurve = EllipticCurveFP(
	2, 			# A
	3,	 		# B
	263, 		# p
	270,		# n (order)
	1,			# cofactor
	200,		# G_x
	39			# G_y
)
print(str(tinycurve))
print("Curve is of order", tinycurve.countpoints())

determine_all_points = False		# This takes long
walk_generator_points = False		# This takes long

if determine_all_points:
	points = set()
	g = None
	for x in range(tinycurve.getp()):
		p = tinycurve.getpointwithx(x)
		if p:
			print(p[0], p[1])
			points.add(p[0])
			points.add(p[1])
	print("Curve has %d distinct points (plus one at infinity)." % (len(points)))


if determine_all_points and walk_generator_points:
	pointorders = { }
	while len(points) > 0:
		rdpt = points.pop()
		print("Randomly selected curve point:", rdpt)

		curpt = rdpt.clone()
		order = 1
		while not curpt.at_infinity:
			curpt += rdpt
			order += 1
		pointorders[order] = pointorders.get(order, set())
		pointorders[order].add(rdpt)

	for order in sorted(pointorders.keys()):
		print("Points with order %d:" % (order))
		for point in sorted(pointorders[order]):
			print("   %s" % (str(point)))


separator()


########################### Checking point compression ###########################
for randomnumber in range(125, 125 + 2):
	p = usedcurve.G * randomnumber
	print("Uncompressed point:", p)
	c = p.compress()
	print("Compressed point  :", c)
	u = AffineCurvePoint(None, None, usedcurve).uncompress(c)
	print("Uncompressed point:", u)
	assert(u == p)
	separator()



