class BowlingGame:
    def __init__(self):
        self.rolls = []  #stores the number of pins knocked down in each roll
    
    def roll(self, pins):
        self.rolls.append(pins)  #add the pins knocked down in each roll
    
    def score(self):
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            #check for strike
            if self.isStrike(rollIndex):  
                result += self.strikeScore(rollIndex)
                rollIndex += 1  
            elif self.isSpare(rollIndex):  #check for spare
                result += self.spareScore(rollIndex)
                rollIndex += 2  
            else:  #regular frame (no strike or spare)
                result += self.frameScore(rollIndex)
                rollIndex += 2  
        return result
    
    #check if the roll is a strike
    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10
    
    #check if the frame is a spare
    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10
    
    #calculate the score for a strike
    def strikeScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]
    
    #calculate the score for a spare
    def spareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 2]
    
    #calculate the score for a normal frame (no strike or spare)
    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
