from io import text_encoding
import random
from stat import S_ENFMT


N_gr = 513100150603
N_list = 19

# task 1-st
S3 = 2
print(f"sulution 1: {(pow(N_gr+N_list,11,11) + S3) % 11}")

# task 2-nd
k = 3
alphabet = sorted("йцукенгшщзхъфывапролджэячсмитьбю")
name = "Рубцов Максим Алексеевич"

for i in range(len(name)):
    if name[i].lower() in alphabet:
        new_letter = alphabet[(alphabet.index(name[i].lower()) + k) % 33]
        if name[i].isupper():
            name = name[:i] + new_letter.upper() + name[i+1:]
        else:
            name = name[:i] + new_letter + name[i+1:]
print("\n")
print("solution 2: encrypted name is " + name)

# task 3-rd

def GCD (a, b):
    remainses = [0,0]
    counter = 1
    if (a>b):
        remainses[0] = b
        remainses[1] = a % b
        print(f"шаг {counter}: {a} : {b} = {a//b} (ост: {remainses[1]})")
        
    else:
        remainses[0] = a
        remainses[1] = b % a
        print(f"шаг {counter}: {b} : {a} = {b//a} (ост: {remainses[1]})")
    counter+=1

    while (remainses[1] > 0):
        print(f"шаг {counter}: {remainses[0]} : {remainses[1]} = {remainses[0]//remainses[1]} ", end = "")
        evocative = remainses[0]
        remainses[0] = remainses[1]
        remainses[1] = evocative % remainses[1]
        print(f"(ост: {remainses[1]})")
        counter += 1
    return remainses[0]


A = (N_gr * (8 + N_list % 7)) ** 2
B = 20022007
print("\n")
print("solution 3:")
print(f"A = {A}")
print(f"НОД(A,B % 95 + 900) = {GCD(A,B % 95 + 900)}")
print(f"НОД(A,(B + 50) % 97 + 700) = {GCD(A,(B + 50) % 97 + 700)}")
print(f"НОД(НОД(A,(B + 20) % 101 + 1500), (B - 40) % 103 + 2500) = {GCD(GCD(A,(B + 20) % 101 + 1500), (B - 40) % 103 + 2500)}")

# task 4-th
print("\n")
print("solution 4:")
def iscomposite(N):
    # простые случаи: 1 и 2 не считаем составными
    if N <= 2:
        return False,1
    # чётное число больше 2 точно составное
    if N % 2 == 0:
        return True,1
    steps = 0
    s = 0
    d = N - 1
    while d % 2 == 0:
        s += 1
        d //= 2
        steps+=1

    for _ in range(10):
        a = random.randint(2, N-2)
        if N % a == 0:
            return True,steps+1
        f_cond = pow(a, d, N) == 1
        steps+=1
        s_cond = False
        if s > 0:
            for k in range(s):
                if pow(a, (2 ** k * d), N) == N - 1:
                    s_cond = True
                    steps+=1
                    break
        if not(f_cond or s_cond):
            return True,steps
    return False,steps


N = 777777
N1 = 619
a = iscomposite(N)
b = iscomposite(N1)
print(f"{N} составное? {a[0]} с вероятностью {1 if a[0] else 1 - 1/4**10}. Вычеслено за {a[1]} шагов")
print(f"{N1} составное? {b[0]} с вероятностью {1 if b[0] else 1 - 1/4**10}. Вычеслено за {b[1]} шагов")

# task 5-th
print("\n")
print("solution 5:")
def invers_modul(e, fi_n):
    Q = []
    remainses = [fi_n,e]
    while remainses[1] != 1:
        Q.append(remainses[0] // remainses[1])
        evocative = remainses[0]
        remainses[0] = remainses[1]
        remainses[1] = evocative % remainses[1]
    matrix = [[0,1],[1,-Q[0]]]
    for i in range(1, len(Q)):
        a00 = matrix[0][0]
        a01 = matrix[0][1]
        a10 = matrix[1][0]
        a11 = matrix[1][1]
        matrix[0][0] = a01
        matrix[0][1] = a00 - Q[i]*a01
        matrix[1][0] = a11
        matrix[1][1] = a10 - Q[i]*a11
    if matrix[1][1] < 0:
        return matrix[1][1] + fi_n
    else:
        return matrix[1][1]

q,p = 3343, 24421
n = q * p
fi_n = (q-1) * (p-1)
e = 2
while GCD(e, fi_n) != 1:
    e+=1
d = invers_modul(e, fi_n)

#task 6-th
print("\n")
print("solution 6:")

text = "RSA"

cipher = pow(int.from_bytes(text.encode("ascii"),'big'),e,n)

uncipher = pow(cipher,d,n)
print(uncipher.to_bytes((uncipher.bit_length() + 7) // 8, 'big').decode())


#task 7-th
print("\n")
print("solution 7:")
x = int.from_bytes(text.encode("ascii"),'big')
s= pow(x,d,n)
x_ = pow(s,e,n)
print(f"целостность данных сохранена? {x.to_bytes((x.bit_length() + 7) // 8, 'big').decode() == x_.to_bytes((x_.bit_length() + 7) // 8, 'big').decode()}")


#task 8-th
print("\n")
print("solution 8:")
a = 259
#A actions:
x = random.randint(1, fi_n - 1)
A = pow(a,x,n)

#B actions:
y = random.randint(1, fi_n - 1)
B = pow(a,y,n)

#A actions:
A_key = pow(B,x,n)

#B actions:
B_key = pow(A,y,n)

print(f"A_key = B_key? {A_key == B_key}")
print(f"((a^x) % n)^y % n = ((a^y) % n)^x % n = a^(y * x) % n? {pow(pow(a,x,n),y,n) == pow(pow(a,y,n),x,n) == pow(a,x*y,n)}")

#task 9-th
print("\n")
print("solution 9:")
k=[]
for i in range(8):
    k.append(sum(k) + random.randint(1,40))
m = sum(k) + random.randint(1,40)
n = 6
while GCD(m,n) != 1:
    n+=1
b = [i*n % m for i in k]

text = input()

encoded_text = text.encode("ascii")
cipher=[]
for c in encoded_text:
    bits = [int(bit) for bit in format(c,f"0{len(b)}b")]
    code = [bit*val for bit, val in zip(bits,b)]
    cipher.append(sum(code))
n_1 = invers_modul(n,m)
decrypted_bytes = []
for c in cipher:
    val = c*n_1 % m
    bits = []
    for i in reversed(k):
        if i <= val:
            bits.append("1")
            val -= i
        else:
            bits.append("0")
    
    bits.reverse()
    byte = int("".join(bits),2)
    decrypted_bytes.append(byte)
text_encoding = bytes(decrypted_bytes).decode("ascii")
print(text_encoding)
