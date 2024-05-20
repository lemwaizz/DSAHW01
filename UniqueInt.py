import time
import psutil
import sys

class UniqueInt:
    """initializing class uniqueint"""
    @staticmethod
    #Used to show the method belongs to the class and not an instance of the class.
    
    def processFile(inputFilePath, outputFilePath):
        """Define the manipulation for the command line inputs."""
        start_time = time.time()  # Start time for runtime tracking
        start_memory = psutil.virtual_memory().used  # Start memory usage
        
        seen_integers = set()  # Initialize an empty set to store seen integers
        
        # Reading from file
        with open(inputFilePath, 'r') as input_file:
            for line in input_file:
                integer = UniqueInt.readNextItemFromFile(line)  # Read integer from next line
                if integer is not None:
                    seen_integers.add(integer)  # Add integer to set
        
        # Writing to output file
        with open(outputFilePath, 'w') as output_file:
            for integer in sorted(seen_integers):
                output_file.write(str(integer) + '\n')

        end_time = time.time()  # End time for runtime tracking
        end_memory = psutil.virtual_memory().used  # End memory usage

        runtime = end_time - start_time
        memory_used = end_memory - start_memory
        print(f"Runtime: {runtime} seconds")  # Print runtime
        print(f"Memory used: {memory_used / (1024 * 1024)} MB")  # Print memory usage

    @staticmethod
    def readNextItemFromFile(line):
        if line.strip() == '':  
            """Skipping empty lines"""
            return None
        
        spaces = line.strip().split()  
        if len(spaces) != 1:  
            """Skip lines with more than one space to account for the one integer condition"""
            return None
        
        try:
            integer = int(spaces[0])  
            if -1023 <= integer <= 1023:  
                return integer
        except ValueError:
            pass
        
        return None  # Caught by the try and except block to handle cases without a valid output

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python UniqueInt.py <inputFilePath> <outputFilePath>")
    else:
        inputFilePath = sys.argv[1]
        outputFilePath = sys.argv[2]
        UniqueInt.processFile(inputFilePath, outputFilePath)
