import random
def check_letter(le):
    if len(le)==1:
        #print 'c'
        return True
    else:
        return False
list=['my','name','is','sandesh']
word=list[random.randint(1,len(list))]
print word
num=len(word)
cnt=0
g_word=''
guess=num+2
print 'u have ' + str(guess) + ' guesses'
while guess!=0:
    i=0
    wrd_cnt=0
    letter=raw_input('enter a letter:')
    if check_letter(letter)==True:
        while i<num:
            if letter==word[i]:
                wrd_cnt+=1
                print 'there is a match for '+word[i]+' and it occurs '+str(wrd_cnt)+' times'
                g_word+=letter
            i=i+1
        if wrd_cnt==1:
             cnt+=1
        else:
            cnt=cnt+wrd_cnt
        if cnt==num:
            break
        guess=guess-1
    print 'u have '+ str(guess) +' guesses'

if cnt==num:
    print 'u won'
    
    
            
        


