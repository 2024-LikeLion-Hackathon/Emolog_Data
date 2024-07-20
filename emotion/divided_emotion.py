
import pandas as pd

#divided em
emotionset = pd.read_excel("data\\rgb\\감정_rgb.xlsx")
emotionset = emotionset.drop(['hexa'], axis=1)

pos = emotionset[emotionset['쾌-불쾌'] > 3.8]
neg = emotionset[emotionset['쾌-불쾌'] <= 3.8]

pos_active = pos[pos['활성화'] > 4.28].reset_index(drop=True)
pos_unactive = pos[pos['활성화'] <= 4.28].reset_index(drop=True)

neg_active = neg[neg['활성화'] > 4.28].reset_index(drop=True)
neg_unactive = neg[neg['활성화'] <= 4.28].reset_index(drop=True)

# pos_active.to_csv('pos&active.csv', index=False)
# pos_unactive.to_csv('pos&unactive.csv', index=False)

# neg_active.to_csv('neg&active.csv', index=False)
# neg_unactive.to_csv('neg&unactive.csv', index=False)

div_emotion = ((pos_active, len(pos_active), 'pos_act'), (pos_unactive, len(pos_unactive), 'pos_unact'), (neg_active, len(neg_active), 'neg_act'), (neg_unactive, len(neg_unactive), 'neg_unact'))


insert_sql = []
name = 0
for emotion in div_emotion:
    print(emotion[1])
    lis = emotion[0]
    for i in range(1, emotion[1]):
        red = str(lis['r'][i])
        green = str(lis['g'][i])
        blue = str(lis['b'][i])
        sql = "INSERT INTO default_emotion(emotion, red, green, blue, type) VALUES ("+ "'"+lis['단어'][i]+"'"+"," + red +"," + green +"," + blue + ","+ str(name)+")"+";"
        insert_sql.append(sql)
    name += 1
    
insert_sql = pd.DataFrame(insert_sql)


insert_sql.to_excel('sql문.xlsx', index=False)