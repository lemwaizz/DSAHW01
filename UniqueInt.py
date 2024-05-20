"""importing required libraries"""
import resource
import time

class UniqueInt:
    """initializing class uniqueint"""
    @staticmethod
    def processFile(inputFilePath, outputFilePath):
        start_time = time.time()  # Start time for runtime tracking
        
        """multiplying the boolean by false initiates an array with 2048 false integers in this case not seen"""
        seen_integers = [False] * 2048 #it is initialized as a range

        """reading from file"""
        with open(inputFilePath, 'r') as input_file:
            for line in input_file:
                integer = UniqueInt.readNextItemFromFile(line) #function to read from next line
                if integer is not None:
                    """adding 1023  to map the integer to the right index"""
                    seen_integers[integer + 1023] = True  # Mark the integer as seen
        
        with open(outputFilePath, 'w') as output_file:
            for i in range(len(seen_integers)):
                if seen_integers[i]:
                    output_file.write(str(i - 1023) + '\n')

