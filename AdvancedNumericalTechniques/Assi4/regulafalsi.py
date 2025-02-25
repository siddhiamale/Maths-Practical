def falseposition(f,x0,x1,e):
                  # f = function
    x0=float(x0)  # initial lower guess
    x1=float(x1)  # initial upper guess
    e=float(e)    # allowed error to stop iterations
    
    # to check function has opposite signs
    if f(x0)*f(x1)>0.0:   
        print('given value is dosent a root')
        print('try with another value')
    
    
    else:
        step=1
        condition=True
        while condition:
            # formula
            x2=x0-(x1-x0)*f(x0)/(f(x1)-f(x0))

            # print each iteration 
            print('iteration %d ,x2=%0.6f and f(x2)=%0.6f'%(step,x2,f(x2)))   

            # updating interval
            if f(x0)*f(x2)<0:
                x1=x2   # root lies between x0 and x2
            else:
                x0=x2   # root lies between x2 and x1

                # update the step(iteration)
                step=step+1
                condition=abs(f(x2))>e
                print('\nrequired root is %0.8f'%x2)

#def f(x):
 #   return x**3-3*x+1

#falseposition(f,0,1,0.00001)

def f(x):
    return x**3-2*x-5

falseposition(f,2,3,0.00001)