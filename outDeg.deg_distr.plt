#
# Out degree distribution for disease-drug network. G(7151, 466369). 1755 (0.2454) nodes with out-deg > avg deg (130.4), 1138 (0.1591) with >2*avg.deg (Thu Dec  6 12:38:07 2018)
#

set title "Out degree distribution for disease-drug network. G(7151, 466369). 1755 (0.2454) nodes with out-deg > avg deg (130.4), 1138 (0.1591) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Out-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'outDeg.deg_distr.png'
plot 	"outDeg.deg_distr.tab" using 1:2 title "" with linespoints pt 6
