set output "Surface_Trimming_Shell_pointC_conv.svg"

set terminal svg enhanced fsize 8  size 262,226
#set terminal postscript solid color eps enhanced  "Palatino" size 7.4cm,6cm
#set terminal epslatex dashed size 16cm,10cm color colortext

reset 
set border lw 0.5 

set xlabel "Number of degrees of freedom"
set xtics font "Times-Roman, 10" 
#set xrange [0.5:100]
set logscale x 10

set grid back lw 0.05 ls -1

set ytics font "Times-Roman, 10" 
set ylabel "z-displacement"
set yrange [0:-3]

set format y "%3.2f"
set format x '$ 10\^{%T}$'
set key right bottom box  lc -1 lt 1 lw 0.3 Left

plot 	'Surface_Trimming_Shell_pointC_conv.txt' using 1:2       with linespoints                   ps 0.5  pt 9 lt 1 lw 1 lc rgb "blue" title  '  p=2', \
		'Surface_Trimming_Shell_pointC_conv.txt' using 3:4       with linespoints                   ps 0.5  pt 5 lt 1 lw 1 lc rgb "red" title   '  p=3', \
		'Surface_Trimming_Shell_pointC_conv.txt' using 5:6       with linespoints                   ps 0.5  pt 7 lt 1 lw 1 lc rgb "black" title '  p=5', \
		'Surface_Trimming_Shell_pointC_conv.txt' using 7:8       with linespoints                   ps 0.5  pt 13 lt 1 lw 1 lc rgb "#8B0000" title '  ANSYS'
set output