import re

# ファイルを開く
with open(r'C:\Users\permi\Desktop\test.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 台詞の鍵括弧前後の改行を削除
text = re.sub(r"\n\n「","\n「",text)
text = re.sub(r"」\n\n","」\n",text)

# チート能力の表記修正
replace_from = ['『|蘇生《リザレクション》』','『#蘇生__リザレクション__#』',
                '『|反射《カウンター》』','『#反射__カウンター__#』',
                '『|身体強化《ストレングス》』','『#身体強化__ストレングス__#』',
                '『|創造《クリエイト》』','『#創造__クリエイト__#』',
                '『|模倣《コピー》』','『#模倣__コピー__#』',
                '『|即死《エクゼキュート》』','『#即死__エクゼキュート__#』',
                '『|龍変化《ドラゴナイズ》』','『#龍変化__ドラゴナイズ__#』',
                '『|無敵《インビンシブル》』','『#無敵__インビンシブル__#』',
                '『|爆発《エクスプロージョン》』','『#爆発__エクスプロージョン__#』',
                '『|建築《ビルド》』','『#建築__ビルド__#』',
                '『|動物使役《テイマー》』','『#動物使役__テイマー__#』',
                '『|植物使役《プランター》』','『#植物使役__プランター__#』',
                '『|契約《コントラクト》』','『#契約__コントラクト__#』',
                '『|反射《カウンター》』','『#反射__カウンター__#』',
                '『|治癒《ヒール》』','『#治癒__ヒール__#』',
                '『|操作《マニュピレート》』','『#操作__マニュピレート__#』',
                '『|加速《アクセル》』','『#加速__アクセル__#』'
                ]
replace_to = ['【蘇生】', '【蘇生】',
              '【反射】','【反射】',
              '【身体強化】','【身体強化】',
              '【創造】','【創造】',
              '【模倣】','【模倣】',
              '【即死】','【即死】',
              '【龍変化】','【龍変化】',
              '【無敵】','【無敵】',
              '【爆発】','【爆発】',
              '【建築】','【建築】',
              '【動物使役】','【動物使役】',
              '【植物使役】','【植物使役】',
              '【契約】','【契約】',
              '【反射】','【反射】',
              '【治癒】','【治癒】',
              '【操作】','【操作】',
              '【加速】','【加速】'
              ]
for i in range(len(replace_from)):
    text = text.replace(replace_from[i], replace_to[i])

# 強調傍点の削除
m = re.findall(r'#.+?__・__#',text)
m=list(set(m))
print(m)
for word in m:
    modified_word=word[1:len(word)-len("__・__#")]
    text=re.sub(word,modified_word,text)

# 話数表記の削除
m2 = re.findall(r'\n第\d{1,2}話：.+\n',text)
m2=list(set(m2))
print(m2)
for word in m2:
    text=re.sub(word,'\n',text)

# 特殊記法に使う記号#、《、|が残っていないかチェック
m_check1=re.findall(r'#',text)
m_check2=re.findall(r'《',text)
m_check3=re.findall(r'\|',text)
print('特殊記法の記号残り：',len(m_check1)+len(m_check2)+len(m_check3))

# 新しいファイルに保存する
with open(r'C:\Users\permi\Desktop\output.txt', 'w', encoding='utf-8') as file:
    file.write(text)

print('done')
