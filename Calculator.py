import cal2
import LSJ

cal1 = cal2.Calculator()
cal2 = cal2.Calculator()
cal3 = LSJ.Calculator()
cal4 = LSJ.Calculator()

print("cal1 = ",cal1.add(3))
print(cal1.add(4))
print(cal1.sub(3))

print("cal2 = ",cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print(cal2.sub(4))

print