import math
import copy

class rgb:
    
    FULL = 2.56
    HALF = 1.28
    LOW = 0.64
    
    def  __init__(self, valence, arousal):
        self.valence = valence
        self.arousal = arousal
        self.valence_color = {}
        self.arousal_color = {}
        self.tmp = {}
    
    #쾌-불쾌
    def valence_to_rgb(self):
        #불쾌
        if 1 <= self.valence < 2:
            self.red(self.valence)
        elif 2 <= self.valence < 3:
            self.green(self.valence)
        elif 3 <= self.valence < 4:
            self.yellow(self.valence)
            
        #쾌
        elif 4 <= self.valence < 5:
            self.orange(self.valence)
        elif 5 <= self.valence < 6:
            self.purple(self.valence)
        elif 6 <= self.valence:
            self.blue(self.valence)
        self.valence_color = copy.deepcopy(self.tmp)
        
    #활성화
    def arousal_to_rgb(self):
        #저활성
        if 1 <= self.arousal < 2:
            self.deep_blue(self.arousal)
        elif 2 <= self.arousal < 3:
            self.shallow_blue(self.arousal)
        elif 3 <= self.arousal < 4:
            self.purple(self.arousal)
            
        #고활성
        elif 4 <= self.arousal < 5:
            self.yellow(self.arousal)
        elif 5 <= self.arousal < 6:
            self.orange(self.arousal)
        elif 6 <= self.arousal:
            self.red(self.arousal)
        self.arousal_color = copy.deepcopy(self.tmp)
        
    #뒤에 소수값을 가져와 + 1 
    # ex) 0.22 라면 23 반환
    def cal(self, num):
        amount = int((num % 1) * 100) + 2
        return amount
            
    def red(self, num):
        amount = self.cal(num)
        self.tmp['r'] = amount * self.FULL
        self.tmp['g'] = 0
        self.tmp['b'] = 0
    
    def orange(self, num):
        amount = self.cal(num)
        self.tmp['r'] = 191 + amount * self.LOW #높은 빨강
        self.tmp['g'] = amount * self.HALF #낮은 초록
        self.tmp['b'] = 0

    
    def yellow(self, num):
        amount = self.cal(num)
        self.tmp['r'] = 191 + amount * self.LOW #높은 빨강
        self.tmp['g'] = 191 + amount * self.LOW #높은 초록
        self.tmp['b'] = 0

    
    def green(self, num):
        amount = self.cal(num)
        self.tmp['r'] = 0
        self.tmp['g'] = amount * self.FULL
        self.tmp['b'] = 0
        
    def blue(self, num):
        amount = self.cal(num)
        self.tmp['r'] = 0
        self.tmp['g'] = 0
        self.tmp['b'] = amount * self.FULL
    
    def shallow_blue(self, num):
        amount = self.cal(num)
        self.tmp['r'] = 0
        self.tmp['g'] = 0
        self.tmp['b'] = 191 + amount * self.LOW
        
    def deep_blue(self, num):
        amount = self.cal(num)
        self.tmp['r'] = 0
        self.tmp['g'] = amount * self.LOW
        self.tmp['b'] = amount * self.HALF
    
    def purple(self, num):
        amount = self.cal(num)
        self.tmp['r'] = amount * self.HALF #낮은 빨강
        self.tmp['g'] = 0
        self.tmp['b'] = amount * self.HALF #낮은 파랑

    def numericalization(self):
        self.valence_to_rgb()
        self.arousal_to_rgb()
        result = {}
        result['r'] = math.ceil(self.diff_weight(self.valence_color['r'],self.arousal_color['r']))
        result['g'] = math.ceil(self.diff_weight(self.valence_color['g'],self.arousal_color['g']))
        result['b'] = math.ceil(self.diff_weight(self.valence_color['b'],self.arousal_color['b']))
        
        result['hexa'] = self.return_hex(result['r'])+self.return_hex(result['g'])+self.return_hex(result['b'])
        return result
    
    def return_hex(self, num):
        hexa = str(hex(num)).split('x')[1] 
        return hexa if len(hexa) != 1 else '0'+hexa

    def diff_weight(self, fir, sec):
        def cal(high, low):
            return high*0.8 + low*0.2
        if fir>sec:
            return cal(fir,sec)
        else:
            return cal(sec,fir)
            
            
        
        
        
# rgb = rgb(6.16, 4.70)
# print(rgb.numericalization())