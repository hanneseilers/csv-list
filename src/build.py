import csv,json,sys,os
# Aufruf: build.py <ausgabe.html> [daten.csv]   (ohne CSV: leere Seite zum Laden per Dateiauswahl)
out=sys.argv[1]
d="null"
if len(sys.argv)>2:
    src=sys.argv[2]
    r=list(csv.reader(open(src,encoding='utf-8-sig',newline=''),delimiter=';'))
    d=json.dumps({"name":os.path.basename(src),"delim":";","h":r[0],"r":r[1:]},ensure_ascii=False).replace("</","<\\/")
t=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'template.html'),encoding='utf-8').read()
open(out,'w',encoding='utf-8').write(t.replace('/*DATA*/null',d))
