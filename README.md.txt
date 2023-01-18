'''State Lengths

    This function takes in a segmentation arrray from a microstates eeg/meg pipeline 
    such as Pycrostates, and then flattens the data and outputs four variables 
    
    Args:
        array: the segemntation array from a microstates pipeline
        epoch_length: the length of your epochs for epoched data or the 
        total length of your data if raw
                
    Returns:
        max_length: your longest lasting state in milliseconds
        min_length: your shortest lasting state in milliseconds
        mean_length: the average length of your states in milliseconds
        std_length: the standard deviation of your states in milliseconds''' 