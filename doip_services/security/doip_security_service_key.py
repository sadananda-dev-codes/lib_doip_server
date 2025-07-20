def yield_keys(seeds):
    keys = []
    
    for seed in seeds:
        keys.append(((seed | 32) + (seed ^ 85)) & 0xFF)
        
    return keys
        