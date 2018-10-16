# 9.3 
## Calculate Euler–Mascheroni constant, which is given by formula:
# ![alt text](https://latex.codecogs.com/gif.latex?C%20%3D%20%5Clim%20%5Climits_%7Bn%20%5Cto%20%5Cinfty%7D%20%28%5Csum%20%5Climits_%7Bk%3D0%7D%5E%7Bn%7D%20%5Cfrac%7B1%7D%7Bk%7D%20-%20%5Cln%20n%29 "Logo Title Text 1")

I will sum over sums given by every *10 000 000* harmonic terms. First tests showed that series converge to **C** very slowly, in this  case I have to sum vast amount of terms. So I decided to calculate every 10 000 000 once. If you decide to make step of algorithm smaller (e.g. ~ 1000) it takes a terrible amount of time and memory.  

9.3 program output:
~~~~Current approximation: 8.661487806918693e-09
Current approximation: 4.330132162554772e-09
Current approximation: 2.8863428444897556e-09
Current approximation: 2.164383558843842e-09
Current approximation: 1.7312929252910555e-09
Current approximation: 1.442608920664802e-09
Current approximation: 1.2364007845755673e-09
Current approximation: 1.081721601575282e-09
Current approximation: 9.614053121602338e-10
Current approximation: 8.651608975099828e-10
Current approximation: 7.864333725505045e-10
Current approximation: 7.208158177390748e-10
Current approximation: 6.652861695345236e-10
Current approximation: 6.176902074899887e-10
Current approximation: 5.764399633903544e-10
Current approximation: 5.403413836165025e-10
Current approximation: 5.085081603274381e-10
Current approximation: 4.801955487401033e-10
Current approximation: 4.548680712005635e-10
Current approximation: 4.3207641887275895e-10
Current approximation: 4.114574517385042e-10
Current approximation: 3.927218887663635e-10
Current approximation: 3.7560506858715087e-10
Current approximation: 3.5990387898730494e-10
Current approximation: 3.4547060199332664e-10
Current approximation: 3.321452098005919e-10
Current approximation: 3.1980460409785135e-10
Current approximation: 3.083441513205432e-10
Current approximation: 2.976838375663554e-10
Current approximation: 2.87719029270726e-10
Current approximation: 2.7840664202471785e-10
Current approximation: 2.6967897175714375e-10
Current approximation: 2.6148062422794157e-10
Current approximation: 2.5376236011261157e-10
Current approximation: 2.4648109500221656e-10
Current approximation: 2.3960605431894417e-10
Current approximation: 2.331003085694196e-10
Current approximation: 2.2693923809139305e-10
Current approximation: 2.210982232226146e-10
Current approximation: 2.1554033446970953e-10
Current approximation: 2.1025941691711534e-10
Current approximation: 2.0523085090258217e-10
Current approximation: 2.0043001676386018e-10
Current approximation: 1.9585691450094934e-10
Current approximation: 1.9148076953603738e-10
Current approximation: 1.872954269535618e-10
Current approximation: 1.832947318379601e-10
Current approximation: 1.7945406452698253e-10
Current approximation: 1.75773425020629e-10
Current approximation: 1.7223434857221215e-10
Current approximation: 1.6884299009729442e-10
Current approximation: 1.6556857501806352e-10
Current approximation: 1.6242956808120684e-10
Current approximation: 1.594013496244745e-10
Current approximation: 1.5649007456342898e-10
Current approximation: 1.536772781513829e-10
Current approximation: 1.5095680547277376e-10
Current approximation: 1.4833481144316404e-10
Current approximation: 1.458051411469913e-10
Current approximation: 1.4336163966869305e-10
Current approximation: 1.4099199717714438e-10
Current approximation: 1.3870236858790773e-10
Current approximation: 1.3648659898542065e-10
Current approximation: 1.3433237853855823e-10
Current approximation: 1.3225201707844537e-10
Current approximation: 1.3023320477395714e-10
Current approximation: 1.2826978670953108e-10
Current approximation: 1.2636791780072968e-10
Current approximation: 1.245275980475529e-10
Current approximation: 1.227303627033134e-10
Current approximation: 1.2098852159913605e-10
Current approximation: 1.1929591981945844e-10
Current approximation: 1.1764640244871806e-10
Current approximation: 1.1603996948691493e-10
Current approximation: 1.1447662093404904e-10
Current approximation: 1.1296251170568288e-10
Current approximation: 1.1148533197069149e-10
Current approximation: 1.1003892681351242e-10
Current approximation: 1.0863560606527062e-10
Current approximation: 1.0726305989484112e-10
Current approximation: 1.0592744321778641e-10
Current approximation: 1.0462260111854402e-10
Current approximation: 1.0334853359711396e-10
Current approximation: 1.0210524065349621e-10
Current approximation: 1.0089272228769077e-10
Current approximation: 9.971097849969767e-11
~~~~
Euler–Mascheroni constant is approximately: **C = 0.5772156649586**
