import os
import jieba
import jieba.posseg as pseg


path = os.path.abspath('.')
path = path.split('/')
basepath = "/".join(path[:-2])
datapath = os.path.join(basepath,'data/train/relation_train/task1.trainSentence')
with open(datapath) as f:
    dataset = f.readlines()    

posset = set()
for line in dataset[:]:
    data = line[:-1].split('\t')
    sentence = data[3].decode('utf-8')
    relation = data[0]
    entity1,entity2 = data[1].decode('utf-8'),data[2].decode('utf-8')
    jieba.add_word(entity1,1000)
    jieba.add_word(entity2,1000)

    ent1_pos = sentence.find(entity1)
    ent2_pos = sentence.find(entity2)
    words = pseg.cut(sentence)
    for w in words:
        # print "%s %s "  % (w.word, w.flag)
        posset.add(w.flag)    

datapath = os.path.join(basepath,'data/posdict.txt')

datawriter = open(datapath,'w')
posdict = dict()
posset = list(posset)
for pos in posset:
    posdict[pos] = posset.index(pos)+1
    line  = '%s\t%s\n' % (pos,posdict[pos] ) 
    datawriter.write(line)
datawriter.close()