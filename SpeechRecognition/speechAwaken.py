arrMsg={"小瘪三","？小瘪三","，小瘪三","你好，小瘪三。","，你好，小瘪三。","你好小瘪三","，小瘪三。","小瘪三","你好，小别删","你好小别删","小别删","小车","晓聪","消除","小葱"}
def awaken(msg):
    for i in arrMsg:
        if(msg==i):
            return True
    return False
