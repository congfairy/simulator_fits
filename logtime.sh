#!/bin/bash
filename=$1
filetime=${filename%.*}"_logtime.xml"
awk -F'[:" "]' '!d[$2]++&&NR>=3 {
gsub("]","",$4);
printf(" process=\"%s\" start_time=\"%s\"\n",$2,$4)}
' $filename > $filetime
echo "====================================================">>$filetime
awk -F'[:" "]' ' NR>=3{
gsub("]","",$4);
a[$2]=$4;
}END{for(i=1;i<asorti(a,b);i++)
{
printf("process=\"%s\" end_time=\"%s\"\n",b[i],a[b[i]])}}' $filename >>$filetime

