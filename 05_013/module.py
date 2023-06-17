import unitConversion as uc

if __name__ == '__main__':
    cmInput = int(input('enter cm : '))

    returnValue = uc.cmToMm(cmInput)
    print(f'return Value : {returnValue}mm')

    returnValue = uc.cmToInch(cmInput)
    print(f'return Value : {returnValue}inch')

    returnValue = uc.cmToM(cmInput)
    print(f'return Value : {returnValue}m')

    returnValue = uc.cmToFt(cmInput)
    print(f'return Value : {returnValue}ft')