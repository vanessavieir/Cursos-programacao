
# ângulos

from math import radians, sin , cos, tan
ângulo=float(input('Digite o ângulo desejado:'))
seno=sin(radians(ângulo))
print('O ângulo de {} vale {:.2f} no seno '.format(ângulo,seno))
coss=cos(radians(ângulo))
print('O ângulo de {} vale {:.2f} no cosseno '.format(ângulo,coss))
tang=tan(radians(ângulo))
print('O ângulo de {} vale {:.2f} na tangente '.format(ângulo,tang))