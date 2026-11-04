from voter import readData;
from collections import defaultdict

streets = {}

def capwords(s):
    words = s.split()
    words = [w.capitalize() for w in words]
    return " ".join(words)



def XXXaddAddr(n, s, p):
    s = capwords(s)
    
#    print (f"{n} {s}")

    try:
        sideDict = streets[s]
    except:
        sideDict = {}
        streets[s] = sideDict

    side = n%2
    try:
        pDict = sideDict[side]
    except:
        pDict = {}
        sideDict[side] = pDict

    try:
        pData = pDict[p]
    except:
        pDict[p] = [n,n]
        return

    if n < pData[0]:
        pData[0] = n
    if n > pData[1]:
        pData[1] = n
        
def addAddr(n, s, p):
    s = capwords(s)
    
#    print (f"{n} {s}")

    try:
        pDict = streets[s]
    except:
        pDict = {}
        streets[s] = pDict

    try:
        sideDict = pDict[p]
    except:
        sideDict = {}
        pDict[p] = sideDict
        
    side = n%2

    try:
        sData = sideDict[side]
    except:
        sideDict[side] = [n,n]
        return

    if n < sData[0]:
        sData[0] = n
    if n > sData[1]:
        sData[1] = n
        

def splitPrecinct(p):
    muni = int (p / 10000)
    ward = int(p / 100) % 100
    dist = int(p % 100)

    return (muni, ward, dist)

def getSegments(sd, text):
    ret = []
    for p,mm in sd.items():
        m,w,d = splitPrecinct(p)
        ret.append(mm[0], mm[1], text, f"{w}:{d}")
    return ret

#        print (f"   {mm[0]} - {mm[1]} {text} district {w}:{d}")

def dispStreets():
    sList = sorted(streets.keys())

    for s in sList:
        if len(streets[s]) == 1:
            m,w,d = splitPrecinct(list(streets[s].keys())[0])
            print (f"{s}\t{w}:{d}")

        else:
            print(s)
            for p,sides in streets[s].items():
                m,w,d = splitPrecinct(p)
                if 0 in sides:
                    print(f"   {sides[0][0]} - {sides[0][1]} (even)\t{w}:{d}")
                if 1 in sides:
                    print(f"   {sides[1][0]} - {sides[1][1]} (odd)\t{w}:{d}")
        

        
        
    


def main():
    dfChunker = readData()

    #precinctList = [b"1881518"]

    # keystone church
    #precinctList = [b"1881512", b"1881517"]

    # spartan school
    precinctList = [b"1881513", b"1881515", b"1881516", b"1881518"]
    
    
    
    ct = 0
    
    for df in dfChunker:
        for p in precinctList:
            rows = df[df['precinctCode'] == p]
            
            df2 = rows[['addrNum', 'addrStreet']].copy()
            for r in df2.itertuples(index=False):
                addAddr(int(r.addrNum), r.addrStreet.decode('UTF-8'), int(p))
                ct += 1
                #if ct > 40:
                #    return

    #print(f"total count: {ct}")


main()

#print(streets)    

dispStreets()

        
