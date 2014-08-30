# self_checks 1, 2, and 5

def self_check_1():
    wordlist = ['cat','dog','rabbit']
    letterlist = []
    for word in wordlist:
        for letter in word:
            if letter not in letterlist:
                letterlist.append(letter)
    print(letterlist)

def self_check_2():
    wordlist = ['cat','dog','rabbit']
    letterlist = [l for l in ''.join(wordlist)]
    noDuplicates = list(reduce(lambda accum, l: accum if l in accum else accum + l, letterlist))
    print 'letterlist is %s,\n noDuplicates is %s' % (letterlist, noDuplicates)


class LogicGate(object):
    
    def __init__(self,n):
        self.name = n
        self.output = None
        
    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getName()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getName()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getName()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class Connector(object):

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


class NorGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==0 and b==0:
            return 1
        else:
            return 0

class NandGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if not(a==1 and b==1):
            return 1
        else:
            return 0

class Signal(LogicGate, Connector):
    """One-way truth value; represents the input end of a circuit."""
    def __init__(self, n, binaryVal):
        super(Signal, self).__init__(n)
        self.binaryVal = binaryVal

    def performGateLogic(self):
        return self.binaryVal

    def getFrom(self):
        """Connector method; rather than returning a preceding
        gate, returns itself b/c it IS the preceding gate"""
        return self

    def getTo(self):
        """Because of the backwards-recursive nature of .getOutput()
        never need to look forwards from a Signal"""
        raise NotImplementedError('does not support Connector method getTo')

def self_check_5():
    
    # circuit Alpha is NOT (( A and B) or (C and D)) 
    alphaAnd1 = AndGate("AlphaAnd1")
    alphaAnd2 = AndGate("AlphaAnd2")

    alphaOr = OrGate("AlphaOr")
    alphaNotFinal = NotGate("AlphaNot")

    alphaFinalConnector = Connector(alphaOr, alphaNotFinal)
    alphaMiddleConnector1 = Connector(alphaAnd1, alphaOr)
    alphaMilleConnector2 = Connector(alphaAnd2, alphaOr)

    # circuit Beta is NOT( A and B ) and NOT (C and D)
    betaAnd1 = AndGate("BetaAnd1")
    betaAnd2 = AndGate("BetaAnd2")

    betaNot1 = NotGate("BetaNot1")
    betaNot2 = NotGate("BetaNot2")

    betaAndFinal = AndGate("BetaAndFinal")

    betaNotToFinal1 = Connector(betaNot1, betaAndFinal)
    betaNotToFinal1 = Connector(betaNot2, betaAndFinal)

    betaAnd1ToNot1 = Connector(betaAnd1, betaNot1)
    betaAnd2ToNot2 = Connector(betaAnd2, betaNot2)
    
    # generate all 16 cases
    from itertools import product
    allPossibilities = product((0,1), repeat=4)
    
    for possibility in allPossibilities:
        # A, B, C, D represent the four truth value inputs
        A, B, C, D = possibility
        
        # both circuits recieve same inputs at respective gates
        alphaAnd1.pinA, betaAnd1.pinA = Signal('Sig', A), Signal('Sig', A)
        alphaAnd1.pinB, betaAnd1.pinB = Signal('Sig', B), Signal('Sig', B)
        alphaAnd2.pinA, betaAnd2.pinA = Signal('Sig', C), Signal('Sig', C)
        alphaAnd2.pinB, betaAnd2.pinB = Signal('Sig', D), Signal('Sig', D)

        print "For the Case %s, Circuit Alpha outputs %s and Circuit Beta outputs %s" % (possibility, alphaNotFinal.getOutput(), betaAndFinal.getOutput())


def _main():
    print 'self_check_1'
    self_check_1()
    print '\nself_check_2'
    self_check_2()
    print '\nself_check_5\n'
    self_check_5()

    return 0

if __name__ == '__main__':
    _main()

