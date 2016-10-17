def canConstruct(ransomNote, magazine):
    def strToCharDict(s):
        counts = {}
        for ch in s:
            try:
                counts[ch] += 1
            except KeyError:
                counts[ch] = 1
        return counts
    
    ransomDict = strToCharDict(ransomNote)
    magDict = strToCharDict(magazine)

    for ch in ransomDict:
        count = ransomDict[ch]
        try:
            magCount = magDict[ch]
        except KeyError:
            return False
        if magCount < count:
            return False
    return True