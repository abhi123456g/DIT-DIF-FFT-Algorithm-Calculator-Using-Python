# DIT-DIF-FFT-Algorithm-Calculator-Using-Python

•	FFT Algorithms are basically fast Fourier transform Algorithms. They are used to calculate DFT efficiently.
•	Because of FFT algorithms, DFT can be calculated in real time
•	DSP processors have special architectural provisions to implement FFT algorithms efficiently.
•	DIT & DIF FFT Algorithm Calculator is Designed for calculating DFT of the input Sequence by performing Butterfly computation.
•	In this Calculators if the user enters the input sequence it will display all the stage values of Butterfly Diagram and will display Magnitude plot and Phase plot.

In this Python Based Application calculators are classified into:
1.	4 Point DIT FFT
2.	8 Point DIT FFT
3.	4 Point DIF FFT
4.	8 Point DIF FFT

                                            DIT FFT ALGORITHM
•	The number of input samples N=2M, where M is an Integer.
•	The input sequence is shuffled through bit reversed.
•	Output Sequence is in natural order.
•	The number of stages in the butterfly diagram is given by M=log2*N.
•	Each Stages consists of N/2 Butterflies.
•	This DIT FFT algorithm is also called as radix-2 DIT FFT algorithm.
                                          
                                            DIF FFT ALGORITHM 
•	The number of input samples N=2M, where M is an Integer.
•	The input sequence is in natural order
•	 Output Sequence is in bit reversed order.
•	The number of stages in the butterfly diagram is given by M=log2*N.
•	Each Stages consists of N/2 Butterflies.
•	This DIF FFT algorithm is also called as radix-2 DIF FFT algorithm.
