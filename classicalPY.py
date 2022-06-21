from mido import Message, MidiFile, MidiTrack,bpm2tempo
import random
import os
import time
from mido.midifiles.meta import MetaMessage
from rhythm import notesDuration, notesInSong


#time = 480(tick) = 60 bpm

class CreateMIDI:
    
    '''需要的参数：
    key = 'G'
    bar_amount = 16 #要生成的小节数，>=6
    bpm_final = 120 #速度bpm
    time_signature = [4,4] #拍号，[每小节几拍，以什么音符为一拍]；例：[3.4]
    '''
    def __init__(self,k,b,bp,t):#：调，小节数，速度，拍号 'G',8,120,[4,4]
        self.key = k
        self.bar_amount = b
        self.bpm_final = bp
        self.time_signature = t
        self.scale = self.getkeyscale()#生成调式音阶
        self.chord_dic = self.createChordDic()#生成和弦字典
        #----生成轨道相关
        self.mid = MidiFile(type=2)
        self.track = MidiTrack()
        self.track2 = MidiTrack()
        self.mid.tracks.append(self.track)
        self.mid.tracks.append(self.track2)   
        self.track.append(Message('program_change', channel=1, program=0, time=0))


    def getkeyscale(self):#C,4 = 60 octaveEnd-octaveStart>=2  #4（-1用于伴奏）-6八度音域
        octaveStart=4
        octaveEnd=6

        main_note_dic={'C':0,
                       'Cm':0,
                       'Db':1,
                       'C#m':1,
                       'D':2,
                       'Dm':2,
                       'Eb':3,
                       'Ebm':3,
                       'E':4,
                       'Em':4,
                       'F':5,
                       'Fm':5,
                       'Gb':6,
                       'F#m':6,
                       'G':7,
                       'Gm':7,
                       'Ab':8,
                       'G#m':8,
                       'A':9,
                       'Am':9,
                       'Bb':10,
                       'Bbm':10,
                       'B':11,
                       'Bm':11,
                       }
        #print(self.key)
        mainnote = main_note_dic[self.key]#获取主音
        startnote = octaveStart*12+mainnote#获取主音所在八度的编号
        MajorScale = [2,2,1,2,2,2,1]#大调音阶
        MinorScale = [2,1,2,2,1,2,1,1]#和声小调
        scale = []
        end = 0
    
        if 'm' in self.key:
            ScaleRelation = MinorScale
        elif 'm' not in self.key:
            ScaleRelation = MajorScale

        for i in range(octaveStart-1,octaveEnd):
            if end:
                break
            for note in ScaleRelation:
                if startnote > 127:
                    end = 1
                    break
                
                scale.append(startnote)
                startnote+=note            
        scale.append(octaveEnd*12+mainnote) #加入结束的主音 
        return scale
    
    def createChordDic(self):
        chord_dic = {}
        for n,lv in zip(range(0,7),['I','II','III','IV','V','VI','VII']):
            chord = [self.scale[n],self.scale[n+2],self.scale[n+4]]
            chord_dic[lv] = chord
    
        chord_dic['V7'] = [self.scale[1],self.scale[3],self.scale[4],self.scale[6]]
        return chord_dic

    def createMeloDic(self):
        melody_dic = {}
        for n,lv in zip(range(0,7),['I','II','III','IV','V','VI','VII']):
            melody = [self.scale[n],self.scale[n],self.scale[n],self.scale[n],self.scale[n+1],self.scale[n+2],self.scale[n+2],self.scale[n+2],self.scale[n+4],self.scale[n+4],self.scale[n+6]]
            melody_dic[lv] = melody
    
        melody_dic['V7'] = [self.scale[1],self.scale[3],self.scale[4],self.scale[6]]
        return melody_dic


    def createChordProgression(self):#12 must >=6

        Ifunc = ['I','I','I','III','VI']
        IVfunc = ['IV','IV','II','VI']
        Vfunc = ['V','V','V','III','V7']
        CProgression = []
        chord_amount_a = int(self.bar_amount/2)
        chord_amount_b = self.bar_amount - chord_amount_a
        r = random.randint(0,len(Ifunc)-1)
    
        startChord = Ifunc[r]
        tempC = [startChord]#加入开始的I功能组
        for chord in range(0,chord_amount_a-2):       
            rf = random.randint(0,2)
            #print(tempC[len(tempC)-1])

            if str(tempC[len(tempC)-1]) in ['V','V7']:
                #print('接主')
                tempC.append('I')
            
            else:
                if rf == 0:
                    tempC.append(Ifunc[random.randint(0,len(Ifunc)-1)])
                elif rf == 1:
                    tempC.append(IVfunc[random.randint(0,len(IVfunc)-1)])
                elif rf == 2:
                    tempC.append(Vfunc[random.randint(0,len(Vfunc)-1)])
        tempC.append('V')    
        tempC.append(startChord)
        for chord in range(0,chord_amount_b-3):       
            rf = random.randint(0,2)
            if tempC[:len(tempC)-1] in ['V','V7']:
                tempC.append('I')
            
            else:
                if rf == 0:
                    tempC.append(Ifunc[random.randint(0,len(Ifunc)-1)])
                elif rf == 1:
                    tempC.append(IVfunc[random.randint(0,len(IVfunc)-1)])
                elif rf == 2:
                    tempC.append(Vfunc[random.randint(0,len(Vfunc)-1)])
        tempC.append('V7')
        tempC.append('I')

        return tempC


    def comMeloRhy(self,rhy_dic,melody_dic,chordpro):#rhy_dic = {0:['sixteenth_note','eighth_note_r']};chordpro = ['III','V']
        playlist = []
        for i in range(0,len(rhy_dic)):
            bar_i_note = rhy_dic[i]
            for j in bar_i_note:
                if j[-1:] == 'r':
                    seq = bar_i_note.index(j)
                    bar_i_note[seq] = '0'


            #print(bar_i_note)
            notes_amount = len(bar_i_note)
            #print(notes_amount)
            ava_notes = melody_dic[chordpro[i]]
            for n in bar_i_note:
                if n == '0':
                    playlist.append(0)
                else:
                    r = random.randint(0,len(ava_notes)-1)
                    playlist.append(ava_notes[r])
        #print(playlist)
        return playlist

    def addMelody(self,track,notelist,rhylist,add_octave=0):
        #print(notelist)
        temp_duration = 0
        fff = max(notelist)
        for note,duration in zip(notelist,rhylist):
            if note == 0:
                temp_duration += duration
                #print('此休止时常：'+str(temp_duration))
                continue
            on = temp_duration
            vel = int(note*(127/fff))#自动音量
            #print (vel)
            note += add_octave*12
            track.append(Message('note_on', note=note, velocity=vel, time=on))
            off = duration
            track.append(Message('note_off', note=note, velocity=vel, time=off))
            #print('当前音是：'+str(note)+'开始时间：'+str(on) +'结束时间：'+str(off)+'持续时长：'+str(duration))
            temp_duration = 0

    def addChord(track,chordlist,duration,velocity):#轨道，和弦音切片list，时长（毫秒），力度；[1,2,3]
        for note in chordlist:
            track.append(Message('note_on', note=note, velocity=velocity, time=0))
        for note in chordlist:
            track.append(Message('note_off', note=note, velocity=velocity-20, time=duration))
            duration = 0

    def ChordAccomp(self,track,chordpro,sequence = 'medium'):
        chord_dic = self.createChordDic()
        chord_per_bar = self.time_signature[0] #每小节几个和弦，默认4个一拍一个
        chord_tempo = {'medium':480,
                       'fast':240,
                       'slow':960}

        if sequence == 'slow':
            chord_per_bar = 2
        elif sequence == 'fast':
            chord_per_bar = 8

        for bar in range(0,self.bar_amount):
            #加入第一小节原位和弦

            chord = chord_dic[chordpro[bar]]
            for beat in range(0,chord_per_bar):#每拍
                CreateMIDI.addChord(track,chord,chord_tempo[sequence],65)
                #获得下一小节和弦然后进行转位并更改chord字典
            try:
                nextchord = chord_dic[chordpro[bar+1]]
                temp = CreateMIDI.chordTransition(chord,nextchord)
                chord_dic[chordpro[bar+1]] = temp
            except:
                continue
        

    def chordTransition(chord,nextchord):#chord:[52,54,56],nextchord:[55,58,60]

        if max(nextchord) - max(chord)>4: #转位阈值大于或小于几个半音进行转位
            nextchord[nextchord.index(max(nextchord))] = max(nextchord)-12
        elif max(nextchord) - max(chord)<-4:
            nextchord[nextchord.index(min(nextchord))] = min(nextchord)+12
        elif nextchord == chord:
            nextchord[nextchord.index(min(nextchord))] = min(nextchord)+12
        return nextchord

    def SmoothMelo(self,pitch_list):
        for p_index in range(0,len(pitch_list)-1):
            pitch = pitch_list[p_index]
            nextpitch = pitch_list[p_index+1]
        
            if pitch == 0 or nextpitch == 0:
                continue

            else:
                if nextpitch - pitch>5:
                    nextpitch-=12
                    pitch_list[p_index+1] = nextpitch
                elif nextpitch - pitch <-5:
                    nextpitch+=12
                    pitch_list[p_index+1] = nextpitch
        return pitch_list

    def randomcode(self):

        H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        f = ''
        for i in range(8):
            f += random.choice(H)
        return f

    def run(self):
        
        tempo_final = bpm2tempo(self.bpm_final)
        self.track.append(MetaMessage('key_signature', key=self.key))
        self.track.append(MetaMessage('set_tempo', tempo = tempo_final))
        self.track2.append(MetaMessage('key_signature', key=self.key))
        self.track2.append(MetaMessage('set_tempo', tempo = tempo_final))

        chordpro = self.createChordProgression()
        rhy_dic,rhy_list = notesInSong(self.bar_amount,self.time_signature)
        duration = notesDuration(rhy_list)
        chord_dic = self.createChordDic()
        melody_dic = self.createMeloDic()
        pitch_list = self.comMeloRhy(rhy_dic,melody_dic,chordpro)
        pitch_list = self.SmoothMelo(pitch_list)

        self.addMelody(self.track,pitch_list,duration,1)#添加旋律到音轨
        self.ChordAccomp(self.track2,chordpro,sequence = 'medium')#添加和弦伴奏到音轨
        rcode = self.randomcode()
        self.mid.save(r'%s.mid'%rcode)#D:\Lunch\statics\midi\
        return rcode

midi = CreateMIDI('F',8,72,[4,4])
print(midi.run())
