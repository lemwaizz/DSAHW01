"""importing required libraries"""
import resource
import time

class UniqueInt:
    """initializing class uniqueint"""
    @staticmethod
    def processFile(inputFilePath, outputFilePath):
        start_time = time.time()  # Start time for runtime tracking
        
        seen_integers = [False] * 2048 #it is initialized as a range

