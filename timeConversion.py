#Code 1
def timeConversion(s):

    if s[-2::1]=='AM':
        if s[:2]=='12':
            ans = int(s[:2])-12
            ans = str(ans)+'0'+s[2:-2]
           
            
        else:
            ans = s[:-2]
        
    else:
        if s[:2]=='12':
            ans = s[:-2]
           
        else:
            ans = int(s[:2])+12
            ans = str(ans)+s[2:-2]
            
    return ans

