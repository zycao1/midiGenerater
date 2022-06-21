import random

def strtolist(temp):
    temp = temp.replace('[','')
    temp = temp.replace(']','')
    temp = temp.replace("'",'')
    temp = temp.split(',')
    return temp

def PairNote(beat_list,beat):#传入音符列表，以谁为一拍；

    note_needpair = {"'sixteenth_4'": "'sixteenth_note','sixteenth_note','sixteenth_note','sixteenth_note'",
            "'sixteenth_2'": "'sixteenth_note','sixteenth_note'",
            "'sixteenth2_eighth'": "'sixteenth_note','sixteenth_note','eighth_note'",
            "'eighth_2sixteenth'": "'eighth_note','sixteenth_note','sixteenth_note'",
            "'eighth_2'": "'eighth_note','eighth_note'",
            "'sixteenth_syco'": "'sixteenth_note','eighth_note','sixteenth_note'",
            "'quarter_d_eighth'":"'quarter_note_d,eighth_note'",
            "'sixteenth_tri'":"'sixteenth_tri_1,sixteenth_tri_1,sixteenth_tri_1'",
            "'eighth_tri'":"'eighth_tri_1,eighth_tri_1,eighth_tri_1'",
            "'eighth_d_sixteenth'":"'eighth_note_d,sixteenth_note",
            "'eighth_syco'":"'eighth_note','quarter_note','eighth_note'"}

    
    temp = str(beat_list)
    temp = temp.replace(' ','')


    for n in note_needpair:
        if n in temp:
            temp = temp.replace(n,note_needpair[n])
    final = strtolist(temp)


 
    return final


def RhythmicPattern(beat_per_bar,beat): #86拍 16分=1
    beat_list = []

    
#-----------------------------------------------------------------------------    
    beat_container_1 = ['sixteenth_note','sixteenth_note','sixteenth_r']
    beat_container_2 = ['sixteenth_2','eighth_note','eighth_note','eighth_note','eighth_r']#,"sixteenth_tri"
    beat_container_3 = ['eighth_note_d']

    beat_container_4 = ['quarter_note',
                        'quarter_note',
                        'quarter_note',
                        'quarter_r',
                        'eighth_2',
                        'eighth_2sixteenth',
                        'eighth_d_sixteenth',
                        'sixteenth_4',
                        'sixteenth2_eighth'
                        ] #'eighth_tri','sixteenth_syco'
    
    beat_container_6 = ['quarter_note_d']
    beat_container_8 = ['half_note','quarter_d_eighth','eighth_syco']
    beat_container_12 =['half_note_d']
    
#--------------------------------四四拍--------------------------------------
    if beat_per_bar == 4 and beat == 4:
        #beat_container_1.remove('sixteenth_note')
        #beat_container_2.remove('eighth_note')
        beat_group_possibility = [1,2,2,3,4,4,4,6,8]
        i = 0
        while i < 4:
            note = beat_group_possibility[random.randint(0,len(beat_group_possibility)-1)]
            if note == 1:
                #beat_list.append('div')
                for n in range(0,4):
                    note = beat_container_1[random.randint(0,len(beat_container_1)-1)]
                    beat_list.append(note)
                
                
                #print('第%s小节的音符是:'% str(i)+str(note))
                i += 1
                
            elif note == 2:
                #beat_list.append('div')
                for n in range(0,2):
                    note = beat_container_2[random.randint(0,len(beat_container_2)-1)]
                    beat_list.append(note)
                                
                i += 1
                

            elif note == 3: #不足4补足4
                #beat_list.append('div')
                note = beat_container_1[random.randint(0,len(beat_container_1)-1)]
                beat_list.append(note)
                note = beat_container_3[random.randint(0,len(beat_container_3)-1)]
                
                beat_list.append(note)
                            
                i += 1
                
                
            elif note == 4:
                note = beat_container_4[random.randint(0,len(beat_container_4)-1)]
                #beat_list.append('div')
                beat_list.append(note)
                
                i += 1
                

            elif note == 6: #不足6补成8
                if beat_per_bar - i >= 2:
                    #beat_list.append('div')
                    note = beat_container_6[random.randint(0,len(beat_container_6)-1)]
                    beat_list.append(note)
                    note = beat_container_2[random.randint(0,len(beat_container_2)-1)]
                    beat_list.append(note)
                                    
                    i += 2
                    
                else:
                    pass
                
            elif note == 8:
                if beat_per_bar - i >= 2:
                    note =  beat_container_8[random.randint(0,len(beat_container_8)-1)]
                    #beat_list.append('div')
                    beat_list.append(note)
                    
                    i += 2
                    
                else:
                    pass
             

        #return beat_list

#--------------------------------四三拍--------------------------------------
    if beat_per_bar == 3 and beat == 4:
        
        beat_group_possibility = [1,1,1,2,2,2,2,3,4,4,4,6,8]

        #beat_container_1.remove('sixteenth_note')
        #beat_container_2.remove('eighth_note')
        i = 0
        while i < 3:
            note = beat_group_possibility[random.randint(0,len(beat_group_possibility)-1)]
            if note == 1:
                #beat_list.append('div')
                for n in range(0,4):
                    note = beat_container_1[random.randint(0,len(beat_container_1)-1)]
                    beat_list.append(note)
                
                
                #print('第%s小节的音符是:'% str(i)+str(note))
                i += 1
                
            elif note == 2:
                #beat_list.append('div')
                for n in range(0,2):
                    note = beat_container_2[random.randint(0,len(beat_container_2)-1)]
                    beat_list.append(note)
                                
                i += 1
                

            elif note == 3: #不足4补足4
                #beat_list.append('div')
                note = beat_container_1[random.randint(0,len(beat_container_1)-1)]
                beat_list.append(note)
                note = beat_container_3[random.randint(0,len(beat_container_3)-1)]
                
                beat_list.append(note)
                            
                i += 1
                
                
            elif note == 4:
                note = beat_container_4[random.randint(0,len(beat_container_4)-1)]
                #beat_list.append('div')
                beat_list.append(note)
                
                i += 1
                

            elif note == 6: #不足6补成8
                if beat_per_bar - i >= 2:
                    #beat_list.append('div')
                    note = beat_container_6[random.randint(0,len(beat_container_6)-1)]
                    beat_list.append(note)
                    note = beat_container_2[random.randint(0,len(beat_container_2)-1)]
                    beat_list.append(note)
                                    
                    i += 2
                    
                else:
                    pass
                
            elif note == 8:
                if beat_per_bar - i >= 2:
                    note =  beat_container_8[random.randint(0,len(beat_container_8)-1)]
                    #beat_list.append('div')
                    beat_list.append(note)
                    
                    i += 2
                    
                else:
                    pass
             

        #return beat_list

#--------------------------------八三拍--------------------------------------
    if beat_per_bar == 3 and beat == 8:
        beat_group_possibility = [1,1,2,2,2,4]
        i = 0
        beat_container_4.remove('eighth_tri')
        while i < 3: #3组8分音符时值
            note = beat_group_possibility[random.randint(0,len(beat_group_possibility)-1)]
            if note == 1:
                #beat_list.append('div')
                for n in range(0,2):
                    note = beat_container_1[random.randint(0,len(beat_container_1)-1)]
                    beat_list.append(note)
                
                
                #print('第%s小节的音符是:'% str(i)+str(note))
                i += 1
                
            elif note == 2:
                #beat_list.append('div')
                note = beat_container_2[random.randint(0,len(beat_container_2)-1)]
                beat_list.append(note)
                                
                i += 1
                

            elif note == 3: #不足4补足4
                if beat_per_bar - i >= 2:
                    #beat_list.append('div')
                    note = beat_container_1[random.randint(0,len(beat_container_1)-1)]
                    beat_list.append(note)
                    note = beat_container_3[random.randint(0,len(beat_container_3)-1)]                
                    beat_list.append(note)
                            
                    i += 2
                
                
            elif note == 4:
                if beat_per_bar - i >= 2:
                    note = beat_container_4[random.randint(0,len(beat_container_4)-1)]
                    #beat_list.append('div')
                    beat_list.append(note)
                
                    i += 2
                

            elif note == 6: 
                if beat_per_bar - i >= 3:
                    #beat_list.append('div')
                    note = beat_container_6[random.randint(0,len(beat_container_6)-1)]
                    beat_list.append(note)
                                    
                    i += 3
                    
                else:
                    pass

             

        #return beat_list

#--------------------------------八六拍--------------------------------------
    if beat_per_bar == 6 and beat == 8:
        beat_container_4.remove('eighth_tri')
        beat_group_possibility = [1,1,2,2,2,2,4]
        i = 0 
        while i < 6: #6组8分音符时值
            note = beat_group_possibility[random.randint(0,len(beat_group_possibility)-1)]
            if note == 1:
                #beat_list.append('div')
                for n in range(0,2):
                    note = beat_container_1[random.randint(0,len(beat_container_1)-1)]
                    beat_list.append(note)
                
                
                #print('第%s小节的音符是:'% str(i)+str(note))
                i += 1
                
            elif note == 2:
                #beat_list.append('div')
                note = beat_container_2[random.randint(0,len(beat_container_2)-1)]
                beat_list.append(note)
                                
                i += 1
                

            elif note == 3: #不足4补足4
                if beat_per_bar - i >= 2:
                    #beat_list.append('div')
                    note = beat_container_1[random.randint(0,len(beat_container_1)-1)]
                    beat_list.append(note)
                    note = beat_container_3[random.randint(0,len(beat_container_3)-1)]                
                    beat_list.append(note)
                            
                    i += 2
                else:
                    pass
                
                
            elif note == 4:
                if beat_per_bar - i >= 2:
                    note = beat_container_4[random.randint(0,len(beat_container_4)-1)]
                    #beat_list.append('div')
                    beat_list.append(note)
                
                    i += 2
                else:
                    pass
                

            elif note == 6: 
                if beat_per_bar - i >= 3:
                    #beat_list.append('div')
                    note = beat_container_6[random.randint(0,len(beat_container_6)-1)]
                    beat_list.append(note)
                                    
                    i += 3
                    
                else:
                    pass

            elif note == 8:
                if beat_per_bar - i >= 4:
                    note =  beat_container_8[random.randint(0,len(beat_container_8)-1)]
                    #beat_list.append('div')
                    beat_list.append(note)
                    
                    i += 4
                    
                else:
                    pass
            

    beat_list = PairNote(beat_list,beat)     
    #print(beat_list)
    return beat_list

def notesInSong(bar_amount,time_sig):#小节数，拍号；例：6/8 = [6,8]
    notedic = {}
    notelist = []
    for i in range(0,bar_amount):
        b = RhythmicPattern(time_sig[0],time_sig[1])
        notedic[i] = b
        notelist.extend(b)
    return notedic,notelist

def notesDuration(notelist):

#-----------------ms---------------------
    quarter_ms = 480
    whole_ms = int(quarter_ms *4)
    half_ms = int(quarter_ms *2)
    half_d_ms = int(quarter_ms *3)
    quarter_d_ms = int(quarter_ms *1.5)
    eighth_ms = int(quarter_ms/2)
    eighth_d_ms = int(quarter_ms*0.75)
    eighth_tri_ms = int(quarter_ms/3)
    sixteenth_ms = int(quarter_ms/4)
    sixteenth_tri_ms = int(quarter_ms/6)

    ms_dic = {'sixteenth_note':sixteenth_ms,
              'sixteenth_r':sixteenth_ms,
              'sixteenth_tri_1':sixteenth_tri_ms,
              'eighth_note':eighth_ms,
              'eighth_r':eighth_ms,
              'eighth_note_d':eighth_d_ms,
              'eighth_tri_1':eighth_tri_ms,
              'quarter_note':quarter_ms,
              'quarter_r':quarter_ms,
              'quarter_note_d':quarter_d_ms,
              'half_note':half_ms,
              'half_note_d':half_d_ms
          }
    duration = []
    for i in notelist:
        n = ms_dic[i]
        duration.append(n)

    return duration

'''bar_amount = 1
bpm = 60
rhy_dic,rhy_list = notesInSong(bar_amount,[4,4])
#print(rhy_list)
duration = notesDuration(bpm,rhy_list)
#print(duration)'''




