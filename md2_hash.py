#MD2
import fileinput
S = [41, 46, 67, 201, 162, 216, 124, 1, 61, 54, 84, 161, 236, 240, 6,
  19, 98, 167, 5, 243, 192, 199, 115, 140, 152, 147, 43, 217, 188,
  76, 130, 202, 30, 155, 87, 60, 253, 212, 224, 22, 103, 66, 111, 24,
  138, 23, 229, 18, 190, 78, 196, 214, 218, 158, 222, 73, 160, 251,
  245, 142, 187, 47, 238, 122, 169, 104, 121, 145, 21, 178, 7, 63,
  148, 194, 16, 137, 11, 34, 95, 33, 128, 127, 93, 154, 90, 144, 50,
  39, 53, 62, 204, 231, 191, 247, 151, 3, 255, 25, 48, 179, 72, 165,
  181, 209, 215, 94, 146, 42, 172, 86, 170, 198, 79, 184, 56, 210,
  150, 164, 125, 182, 118, 252, 107, 226, 156, 116, 4, 241, 69, 157,
  112, 89, 100, 113, 135, 32, 134, 91, 207, 101, 230, 45, 168, 2, 27,
  96, 37, 173, 174, 176, 185, 246, 28, 70, 97, 105, 52, 64, 126, 15,
  85, 71, 163, 35, 221, 81, 175, 58, 195, 92, 249, 206, 186, 197,
  234, 38, 44, 83, 13, 110, 133, 40, 132, 9, 211, 223, 205, 244, 65,
  129, 77, 82, 106, 220, 55, 200, 108, 193, 171, 250, 36, 225, 123,
  8, 12, 189, 177, 74, 120, 136, 149, 139, 227, 99, 232, 109, 233,
  203, 213, 254, 59, 0, 29, 57, 242, 239, 183, 14, 102, 88, 208, 228,
  166, 119, 114, 248, 235, 117, 75, 10, 49, 68, 80, 180, 143, 237,
  31, 26, 219, 153, 141, 51, 159, 17, 131, 20]

"""bytes_to_hex(bytes_list)
   Convierte una lista de bytes en una cadena de hexadecimales, dandole un formato especifico al hash.
   bytes_list - lista de bytes"""
def bytes_to_hex(bytes_list):
	hash_value = ''
	for b in bytes_list:
		hex_b = hex(b)[2:]
		while len(hex_b) < 2:
			hex_b = '0' + hex_b
		hash_value += hex_b
	return hash_value

"""padding(bytes_list)
   Aplica el padding de MD2, recibe una lista de bytes y agrega los elementos necesarios para que esta
   tenga un tamaño que sea múltiplo de 16.
   bytes_list - lista de bytes"""
def padding(bytes_list):
	pad_value = 16 - (len(bytes_list) % 16)
	return bytes_list + [pad_value for x in range(pad_value)]

"""checksum(bytes_list, S)
   Agrega 16 elementos (checksum) a la lista de bytes.
   bytes_list - lista de bytes
   S - permutación de [0 ... 255] utilizada en el algoritmo"""
def checksum(bytes_list, S):
	L, C, n = 0, [0 for x in range(16)], len(bytes_list)
	for i in range(n//16):
		for j in range(16):
			c = bytes_list[16 * i + j]
			C[j] = C[j] ^ S[c ^ L]
			L = C[j]
	return bytes_list + C

"""hash(bytes_list)
   Realiza el procedimiento de hash final.
   bytes_list - lista de bytes"""
def hash(bytes_list, S):
	n, X = len(bytes_list), [0 for x in range(48)]
	for i in range(n//16):
		for j in range(16):
			X[j + 16] = bytes_list[16 * i + j]
			X[j + 32] = X[j + 16] ^ X[j]
		t = 0
		for j in range(18):
			for k in range(48):
				t = X[k] ^ S[t]
				X[k] = t
			t = (t + j) % 256
	return X[:16]

"""md2(msg)
   Toma un mensaje de texto plano y produce su respectivo hash value.
   msg - cadena de caracteres"""
def md2(msg):
	m_bytes = list(msg.encode('utf-8'))
	return bytes_to_hex(hash(checksum(padding(m_bytes), S), S))

lines = list()
for line in fileinput.input():
	line = line.replace('\n', '')
	line = line.replace('\"', '')
	lines.append(line)
print(md2(lines[0]))
