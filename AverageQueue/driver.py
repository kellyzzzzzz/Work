from AverageQueue import AverageQueue as AQ
import datetime as dt
import random

test1 = AQ()
test1.push(100)
test1.push(10)
test1.push(13)

print "the sum of test1 is " + str(test1.get_avg())
errors1 = 0

if(test1.front() != 100):
    print "Error"
    errors1 += 1

if(test1.pop() != 100):
    print "Error"
    errors1 += 1
    
if(test1.front() != 10):
    print "Error"
    errors1 += 1

if(test1.pop() != 10):
    print "Error"
    errors1 += 1

if(test1.front() != 13):
    print "Error"
    errors1 += 1

if(test1.pop() != 13):
    print "Error"
    errors1 += 1

print "with " + str(errors1) + " errors"

print ""
test2 = [random.randrange(1, 100, 1) for i in range(1000)]

start = dt.datetime.now()
test2 = AQ(test2)

print "the sum of test2 is " + str(test2.get_avg())

end = dt.datetime.now()
print "test2 took " + str((end - start))
sum = 0
for i in test2._elements:
    sum += i

check = float(sum) / len(test2._elements)
print "check test2 " + str(check)

print ""
test3 = []

start = dt.datetime.now()
test3 = AQ(test3)

for i in range(100000):
    test3.avg_push(random.randrange(1, 100, 1))
    
print "the sum of test3 is " + str(test3.get_avg())
end = dt.datetime.now()
print "test3 took " + str((end - start))
sum = 0
for i in test3._elements:
    sum += i

check = float(sum) / len(test3._elements)
print "check test3  " + str(check)


test4 = test3
start = dt.datetime.now()


for i in range(10000):
    test4.avg_pop()

print "the sum of test4 is " + str(test4.get_avg())
end = dt.datetime.now()
print "test4 took " + str((end - start))
sum = 0
for i in test4._elements:
    sum += i

check = float(sum) / len(test4._elements)
print "check test4 " + str(check)
