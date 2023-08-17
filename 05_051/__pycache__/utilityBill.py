
income = 0; waterPrice = 0; electricPrice = 0; gasPrice = 0

def setIncome(ic):
    global income 
    income = ic

def getIncome():
    return income

def setWaterPrice(wp):
    global waterPrice 
    waterPrice = wp

def getWaterPrice():
    return waterPrice

def setEletricPrice(ep):
    global electricPrice 
    electricPrice = ep

def getEletricPrice():
    return electricPrice

def setGasPrice(gp):
    global gasPrice 
    gasPrice = gp

def getGasPrice():
    return gasPrice

def getUtilityBill():
    result = waterPrice + gasPrice + electricPrice
    return result

def getUtilityBillRate():
    #result = getUtilityBill() / getIncome() * 100
    return getUtilityBill() / getIncome() * 100