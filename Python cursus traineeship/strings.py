a = 'banaan'
b = 4
c = 'konijn'
d = 538
t1 = 'een vogel eet {}'
t2 = 'een vogel eet {1} {0}'
#t3 = f'een {c} eet {d} zaden'
t4 = 'een vogel heeft {1:f} benen'
t5 = 'een konijn heeft{3:.4f} poten'
t6 = 'een vogel eet {1:.0f} insecten'
t7 = 'een konijn poept {1:d} keer'
t8 = 'een {0:4} is een dier'
t9 = 'hoe wordt {2:<2} uitgeleind?'
t10 = 'en hoe wordt {2:^5} gedaan?'
t11 = f'en natuurlijk eet een {a} geen {c} voor meer dan {d} dagen per jaar'

print(t1.format(a,b,c,d))
print(t2.format(a,b,c,d))
#print(t3)
print(t4.format(a,b,c,d))
print(t5.format(a,b,c,d))
print(t6.format(a,b,c,d))
print(t7.format(a,b,c,d))
print(t8.format(a,b,c,d))
print(t9.format(a,b,c,d))
print(t10.format(a,b,c,d))
print(t11.format(a,b,c,d))