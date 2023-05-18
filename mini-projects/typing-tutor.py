import time, threading

class TypingTester:
    def __init__(self, para):
        self.correctWords=[]
        self.incorrectWords={}
        self.typeWords=[]
        self.totalWords=[]
        self.input=None
        self.para=para
        self.accuracy=0
        self.time=0
        self.wordPerMin=0
        self.run()

    def clock(self):
        while len(self.typeWords)==0:
            self.time+=1
            time.sleep(1)

    def run(self):
        threading.Thread(target=self.clock).start()
        threading.Thread(target=self.testSpeed).start()
    
    def testSpeed(self):
        print(self.para+'\n')
        self.input=str(input("Start typing \n"))
        self.totalWords=self.para.split(" ")
        self.typeWords=self.input.split(" ")

        try:
            for i in range (len(self.typeWords)):
                if (self.typeWords[i] == self.totalWords[i]):
                    self.correctWords.append(self.typeWords[i])
                else:
                    self.incorrectWords.update({self.totalWords[i]: self.typeWords[i]})
        except Exception as err:
            print(err)

        self.accuracy=len(self.correctWords)/len(self.totalWords)*100
        self.wordPerMin=len(self.typeWords)/(self.time/60)

        print("\n------Your typing test result------")
        print(f"Accuracy: {self.accuracy}")
        print(f"Words per min: {self.wordPerMin}")
        print(f"Incorrect words: {self.incorrectWords}")

test=TypingTester("Hello this is typing tester.")
# test.testSpeed()