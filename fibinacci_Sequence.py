nterms = int(input("How many terms? "))  #nterms=10

# first two terms
n1, n2 = 0, 1
count = 0 #i

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:  #i<10
       print(n1)
       nth = n1 + n2 #nth=1+2 =3
       n1 = n2 #n=2
       n2 = nth #n2=2

       count += 1 #count = count+1