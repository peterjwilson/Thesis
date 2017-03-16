set output "Surface_Trimming_Shell_pointC_conv2.svg"

set terminal svg enhanced fsize 8  size 262,226
#set terminal postscript solid color eps enhanced  "Palatino" size 7.4cm,6cm
#set terminal epslatex dashed size 16cm,10cm color colortext

reset 
set border lw 0.5 


set xtics font "Times-Roman, 5" 
set xlabel "Number of degrees of freedom"
#set xrange [0.5:100]
set logscale x 10

set grid back lw 0.05 ls -1

set ylabel "relative difference []" font "Times-Roman,10"
set ytics font "Times-Roman, 5" 
set logscale y 10
#set yrange [-3.6:-4.5]
#set lmargin 10

#set format y "%.2t"
set format y '$10\^\{%T\}$'
set format x '$10\^\{%T\}$'
set key right top box  lc -1 lt 1 lw 0.3 Left

plot 	'Surface_Trimming_Shell_pointC_conv2.txt' using 1:2       with linespoints                   ps 0.5  pt 9 lt 1 lw 1 lc rgb "blue" title  '  p=2', \
		'Surface_Trimming_Shell_pointC_conv2.txt' using 3:4       with linespoints                   ps 0.5  pt 5 lt 1 lw 1 lc rgb "red" title   '  p=3', \
		'Surface_Trimming_Shell_pointC_conv2.txt' using 5:6       with linespoints                   ps 0.5  pt 7 lt 1 lw 1 lc rgb "black" title '  p=5'

set output