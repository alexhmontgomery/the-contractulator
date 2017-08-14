import datetime

contractNum = 0
startContracts = []
timeContracts = []
timeActive = []
avgContraction = 0
avgActiveCont = 0
frequency = 0
freqContracts = []
freqActive = []
avgFrequency = 0
avgActiveFreq = 0
activeBegin = 0
#For 5-1-1, testContraction = 60
testContraction = 4
#For 5-1-1, testFrequency = 300
testFrequency = 300
#For 5-1-1, testRange = 3600
testRange = 15

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

        #Determine if active labor tracking should begin
        if timeContracts[(contractNum - 1)] >= testContraction and\
           activeBegin == 0:
            activeBegin = startContracts[(contractNum - 1)]
            print('* Begin tracking for active labor *')
        elif timeContracts[(contractNum - 1)] >= testContraction:
            timeActive.append(timeContracts[(contractNum - 1)])
            freqActive.append(freqContracts[(contractNum - 2)])

        #Calculate general averages
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

        #Calculate active labor averages
        if len(timeActive) > 1 and\
           len(freqActive) > 1:
            avgActiveCont = int(avg(timeActive))
            avgActiveFreq = int(avg(freqActive))
        
        #Print averages & current status
        print('==> Average contraction is %s long and %s apart!! <==' % (dispAvgContract, dispAvgFrequency))
        if avgActiveCont > testContraction and\
           avgActiveFreq < testFrequency and\
           (startContracts[(contractNum - 1)] - activeBegin).seconds > testRange:
            print('********CALL THE DOCTOR! IT IS TIME TO GO TO THE HOSPITAL! You are now in active labor.********')
        else:
            print('Relax. You are still in early labor')
            
        print('------------Next Contraction------------')
except KeyboardInterrupt:
    print('\nDone')

