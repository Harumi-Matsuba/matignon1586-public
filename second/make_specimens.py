# EN: Build the sign specimen sheet used in the second transcriptions v2-v4 (second/v*/PROMPT.md).
#     Usage: python3 second/make_specimens.py henryiii_MayenneForget2.png specimens.png
#     Input: Tomokiyo's Cipher-2 table (https://cryptiana.web.fc2.com/code/henryiii_MayenneForget2.png, 727x319), not included here.
#     It is scaled to 1800 px wide; each sign's shape is cut out (no value cells) and labelled with our sign name (W01... = neutral names, see names_map.tsv).
# 2回目の書き起こし v2〜v4 で使った記号の見本表を作る。入力は友清氏の表の画像（このリポジトリには含めない）。
# 幅1800画素に拡大し、記号の形だけを切り出して（値の欄は入れない）、こちらの記号名を付けて並べる。
# v2〜v4 で実際に渡した画像は、先に拡大しておいた同じ表から作ったもので、このスクリプトの出力とは画素の値の平均で約1.2（255段階）違う。
#     The image actually used in v2-v4 was made from a copy of the same table enlarged beforehand; it differs from this script's output by about 1.2 grey levels (of 255) on average.
import sys
from PIL import Image, ImageDraw, ImageFont
src=Image.open(sys.argv[1]).convert('L')
im=src.resize((1800, round(src.size[1]*1800/src.size[0])), Image.LANCZOS)
R1,R2,R3,R4,R5=85,138,192,248,305
G=[('A<',145,R1),('+',148,R2),('4',150,R3),('pi',200,R1),('s',255,R2),('9',312,R1),('dy',310,R2),
   ('r',375,R1),('dl',372,R2),('4H',375,R3),('m',425,R1),('6b',423,R2),('box',418,R5),('tri',475,R1),('g2',478,R2),
   ('F',527,R1),('R',527,R2),('n',592,R1),('fi',590,R2),('nu',592,R4),('lq',648,R1),('y',643,R2),('H',660,R5),
   ('2',705,R1),('gam',705,R2),('40',712,R5),('6',755,R1),('fn',752,R2),('nd',762,R5),('o3',820,R1),('//',822,R2),
   ('pl',868,R1),('xo',920,R2),('#',975,R1),('rh',968,R2),('r5',965,R3),('f',1030,R1),('J',1030,R2),('sl',1030,R3),
   ('*',1032,300),('a',1085,R1),('8',1088,R2),('oc',1083,R3),('psi',1088,R5),('x',1147,R1),('T',1145,R2),('th',1150,R3),
   ('v3',1148,R4),('Id',1155,R5),('Ry',1268,R1),('y2',1265,R3),
   ('W08',50,475),('W03',490,472),('W07',575,472),('W04',705,472),('W05',785,475),('W12',900,475),('W09',1190,472),
   ('W06',40,604),('W15',237,592),('W10',325,592),('W02',420,596),('W01',493,594),('cd',778,594),('W11',965,592)]
try:
    font=ImageFont.truetype('Arial.ttf',22)
except OSError:
    font=ImageFont.load_default()
cw,ch=150,110; cols=8
rows=(len(G)+cols-1)//cols
sh=Image.new('L',(cols*cw,rows*ch),255); d=ImageDraw.Draw(sh)
for i,(nm,x,y) in enumerate(G):
    cr=im.crop((x-34,y-30,x+34,y+30)).resize((102,90))
    cx,cy=(i%cols)*cw,(i//cols)*ch
    sh.paste(cr,(cx+4,cy+2)); d.text((cx+108,cy+35),nm,fill=0,font=font)
    d.rectangle((cx,cy,cx+cw-1,cy+ch-1),outline=180)
sh.save(sys.argv[2]); print(len(G))
