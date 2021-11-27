from collections import Counter

def get_mean(var):
    
    """
    calculate mean: sum of observations/ length of observations
    
    observations must me 1 or more than 1 in length
    
    returns int
    """
    
    n = len(var)
    
    if n < 1:
        raise ValueError('Object must have more than one variable')
        
        
    total = sum(var)
    mean = total/n
    return mean

def get_median(var):
    
    """
    calculates median by sorting observations and finding middle value. 
    
    if number of observations are even, 
    finds the average of the two middle numbers
    """
    
    
    n = len(var)
    
    if n < 1:
        raise ValueError('Object must have more than one variable')
        
    sorted_var = sorted(var)
    index = (n - 1) // 2
    
    if n % 2 == 0:
        return (sorted_var[index] + sorted_var[index + 1])/2.0
    else:
        return sorted_var[index]
    
def get_mode(var):
    
    """
    finds mode based on frequency
    
    collections module is used
    """
    
    
    n = len(var)
    
    if n < 1:
        raise ValueError('Object must have more than one variable')
    
    counts = Counter(var)
    for k, v in counts.items():
        if v == counts.most_common(1)[0][1]:
            print(k)
            
def get_variance(var):
    variance = sum((i - get_mean(var)) ** 2 for i in var) / len(var)
    return variance

def get_stdev(var):
    
    variance = get_variance(var)
    
    return variance ** 0.5

def get_percentile(data = 'df', column = 'column', rank = '25, 50 or 75'):
    
    data[column] = sorted(data[column])
    index = int(((len(data[column].index)-1) * rank) / 100.0)
    return data.at[index, column]

