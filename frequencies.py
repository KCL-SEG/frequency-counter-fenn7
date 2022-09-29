"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from operator import contains


def frequencies(items):
    frequencies = {}
    
    for item in items:
        # convert items to strings
        item = str(item)
        
        # updates the 'counter' for each unique item
        if frequencies.get(item) == None:
            scheduledUpdate = { item : 1 }
        else:
            scheduledUpdate = { item: int(frequencies.get(item) + 1) }  
            
        frequencies.update(scheduledUpdate)
        
    print (frequencies)
    return frequencies

# frequencies( [1, "john", 1, 1, True, "john", "john", "1", True] )
