"""importing required libraries"""
import resource
import time

"""declaring file paths"""
inputFilePath = "sample_input_for_students-20240520T133354Z-001\sample_01.txt"
outputFilePath = "results_for_sample_inputs-20240520T133355Z-001\sample_01.txt_result.txt"

class UniqueInt:
    """initializing class uniqueint"""
    @staticmethod
    def processFile(inputFilePath, outputFilePath):
        start_time = time.time()  # Start time for runtime tracking
        
        seen_integers = [False] * 2048 #it is initialized as a range
        
          