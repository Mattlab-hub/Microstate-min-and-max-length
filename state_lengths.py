# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 18:04:10 2023

@author: mawin
"""
def state_lengths(array,epoch_length):   
    from itertools import groupby
    import itertools,operator
    import numpy as np 

#flattten segmentation array
    count=0
    for count in range(len(array.labels)):
        if count==0:
            flat=array.labels[count]
        else:
            flat=np.concatenate((flat, array.labels[count]), axis=0)
        count+=1

#find longest state
    max_state=0
    for sl in range(len(array.cluster_names)):
    
        r = max((list(y) for (x,y) in groupby((enumerate(flat)),operator.itemgetter(1)) if x == sl), key=len)
        long0=r[-1][0]-r[0][0]+1
    
        if long0>=max_state: max_state=long0
        else: max_state=max_state
        
    max_state=(epoch_length/len(array.labels[1]))*max_state*1000  

# find shortest state durations 
    min_state=1000
    for sl in range(len(array.cluster_names)):
    
        r = min((list(y) for (x,y) in groupby((enumerate(flat)),operator.itemgetter(1)) if x == sl), key=len)
        short=r[-1][0]-r[0][0]+1
    
        if short<=min_state: min_state=short
        else: min_state=min_state
        
    min_state=(epoch_length/len(array.labels[1]))*min_state*1000

#find mean state    
    count_dups = [sum(1 for _ in group) for _, group in groupby(flat)]
    
    mean_state=np.mean(count_dups)
    mean_state=(epoch_length/len(array.labels[1]))*mean_state*1000

#find standard deviation of state lengths
    count_dups = [sum(1 for _ in group) for _, group in groupby(flat)]
    
    std_state=np.std(count_dups)
    std_state=(epoch_length/len(array.labels[1]))*std_state*1000
    
    return max_state, min_state, mean_state, std_state

#%%
#
epoch_length=epochs.tmax-epochs.tmin

max_state, min_state, mean_state, std_state = state_lengths(seg1010, epoch_length)

