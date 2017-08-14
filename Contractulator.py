import datetime

contractNum = 0
startContracts = []
timeContracts = []
avgContraction = 0
frequency = 0
freqContracts = []
avgFrequency = 0

print("Welcome to the Contractulator. Let's see if you're about to have a baby!")
print('-- Remember the 5-1-1 rule --')
print('Press RETURN at the start of the first contraction.')

#Start of the first contraction
raw_input()
startTime = datetime.datetime.now()
startContracts.append(startTime)
contractNum += 1

print('Contraction #%s began at %s' % (contractNum, startTime.time().replace(microsecond=0)))
print('When contraction #%s ends, press RETURN.' % contractNum)

#End of first contraction
raw_input()
endTime = datetime.datetime.now() - startTime
timeContracts.append(endTime.seconds)

print('Contraction was %d seconds long' % endTime.seconds)
print('------------Next Contraction------------')

try:
    while True:
        print('Press RETURN at the start of next contraction.')
        #Start of next contraction
        raw_input()
        startTime = datetime.datetime.now()
        startContracts.append(startTime)
        contractNum += 1
        print('Contraction #%s began at %s' % (contractNum, startTime.time().replace(microsecond=0)))
        frequency = startTime - startContracts[(contractNum - 2)]
        freqContracts.append(frequency.seconds)
        print('When contraction #%s ends, press RETURN.' % contractNum)

        #End of next contraction
        raw_input()
        endTime = datetime.datetime.now() - startTime
        timeContracts.append(endTime.seconds)
        print('Contraction was %d seconds long' % endTime.seconds)

        #Calculate averages
        def avg(l):
            return sum(l, 0.0) / len(l)
        def convertToMin(t):
            mins = int(t / 60)
            sec = t % 60
            return '%s minutes %s seconds' % (mins, sec)
        avgContraction = int(avg(timeContracts))
        dispAvgContract = convertToMin(avgContraction)
        avgFrequency = int(avg(freqContracts))
        dispAvgFrequency = convertToMin(avgFrequency)
        print('===> Average contraction is %s long and %s apart!! <===' % (dispAvgContract, dispAvgFrequency))
        if avgContraction > 60 and\
           avgFrequency < 300:
            print('CALL THE DOCTOR! It is time to go to the hospital!!!')
        else:
            print('Relax. You are still in early labor')
            
        print('------------Next Contraction------------')
except KeyboardInterrupt:
    print('\nDone')

