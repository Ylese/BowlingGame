class BowlingGame:
    """
    A class to represent a 10-pin bowling game.

    Methods
    -------
    roll(pins)
        Records the number of pins knocked down in a single roll.
    score()
        Returns the total score for the game after all frames are completed.
    isStrike(rollIndex)
        Checks if the current roll is a strike (all 10 pins knocked down).
    isSpare(rollIndex)
        Checks if the current frame is a spare (10 pins knocked down in two rolls).
    strikeScore(rollIndex)
        Calculates the score for a strike, including the next two rolls.
    spareScore(rollIndex)
        Calculates the score for a spare, including the next roll.
    frameScore(rollIndex)
        Calculates the score for a normal frame (sum of two rolls).
    """

    def __init__(self):
        """Initializes an empty list of rolls."""
        self.rolls = []

    def roll(self, pins):
        """
        Records the number of pins knocked down in a single roll.

        Parameters
        ----------
        pins : int
            The number of pins knocked down in this roll.
        """
        self.rolls.append(pins)

    def score(self):
        """
        Calculates and returns the total score for the game.

        Returns
        -------
        int
            The total score after 10 frames.
        """
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2
        return result

    def isStrike(self, rollIndex):
        """
        Checks if the current roll is a strike (all 10 pins knocked down).

        Parameters
        ----------
        rollIndex : int
            The index of the current roll.

        Returns
        -------
        bool
            True if the current roll is a strike, False otherwise.
        """
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        """
        Checks if the current frame is a spare (10 pins knocked down in two rolls).

        Parameters
        ----------
        rollIndex : int
            The index of the current roll.

        Returns
        -------
        bool
            True if the frame is a spare, False otherwise.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    def strikeScore(self, rollIndex):
        """
        Calculates the score for a strike, which includes the next two rolls.

        Parameters
        ----------
        rollIndex : int
            The index of the current roll.

        Returns
        -------
        int
            The score for the strike, including the next two rolls.
        """
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def spareScore(self, rollIndex):
        """
        Calculates the score for a spare, which includes the next roll.

        Parameters
        ----------
        rollIndex : int
            The index of the current roll.

        Returns
        -------
        int
            The score for the spare, including the next roll.
        """
        return 10 + self.rolls[rollIndex + 2]

    def frameScore(self, rollIndex):
        """
        Calculates the score for a normal frame (sum of two rolls).

        Parameters
        ----------
        rollIndex : int
            The index of the current roll.

        Returns
        -------
        int
            The sum of the two rolls in the current frame.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
