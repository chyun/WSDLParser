class WebService:
    def __init__(self):
        self.name = ''
        self.inputList = {}
        self.outputList = {}

    def addInput(self, inputVal):
        self.inputList[inputVal.lower()] = None
        
    def addOutput(self, outputVal):
        self.outputList[outputVal.lower()] = None
                
    def getInputList(self):
        return self.inputList
        
    def getOutputList(self):
        return self.outputList

##    def belongInputTo(self, inputset):
##        if Set(self.inputList).issubset(Set(inputset)):
##            return 1
##        return 0

    def getNumInputs(self):
        return len (self.inputList)
	
    def getNumOutputs(self):
        return len (self.outputList)
