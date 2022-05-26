

walletDays = {'address':{['days','custodian-id']}}
tempDaysaddresses = []
tempDaycollection = 0 

def DaysCounter(_address,_startdays):

    if walletDays[_address] == 0:
        #jail the system
        print('jail activated')

    elif walletDays[_address] == _startdays:
        tempDaysaddresses.append(_address)
        tempDaycollection.append(balanceOf[_address])

    else:
        walletDays[_address] -= 1

def DaysEnumerater(_startdays,_maxamt):
    for _idx,_address in enumerate(walletDays):
        DaysCounter(_address,_startdays)

    if tempDaycollection >= _maxamt:
        chooseone = random.randit(1,20)
        donorone = random.randit(1,20)
        transactRet(donorone,chooseone,tempDaycollection)
        for _idx,_address in enumerate(tempDaysaddresses):
            walletDays[_address] -= 1
        print(chooseone,tempDaycollection,tempDaysaddresses)

    else:
        print(tempDaycollection,' : is not enough to transactRet')
        print('try on a next day')

walletnegative = {'custodian-id': {
    ['custodian-id',
        'amount',
        'days']
    }}

def negAdder():
    pass

def NegEnumerater():
    
    
