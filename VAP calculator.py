#Program to find area ,volume or perimeter of some figures.
while True:
    print("""Enter the operator no. to find your required result:-
1= area of rectangle
2= perimeter of rectangle
3= area of square
4= perimeter of square
5= area of triangle
6= area of parallelogram
7= area of circle
8= perimeter of circle
9= area of sphere
10= area of trpezium
11= area of cuboid
12= area of cube
13= curved surface area of cylinder
14= total surface area of cylinder
15= curved surface area of cone
16= total surface area of cone
17= curved surface area of hemisphere
18= total surface area of hemisphere
19= volume of cuboid
20= volume of cube
21= volume of cylinder
22= volume of cone
23= volume of sphere
24= volume of hemisphere """)
    op=input("enter the operator out of these:-('1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24') =")

    if op=='1':
        print("you are finding area of the recatangle =")
        l=float(input("enter the length:-"))
        b=float(input("enter the breadth:-"))
        area =l*b
        print(area)
        choice = input('press enter to continue or e/E to exit...')

    
    elif op=='2':
        print("you are finding perimeter of the rectangle =")
        l=float(input("enter the length:-"))
        b=float(input("enter the breadth:-"))
        perimeter=2*(l+b)
        print(perimeter)
        choice = input('press enter to continue or e/E to exit...')
    
    elif op=='3':
        print("you are finding area of square =")
        s=float(input("enter the side:-"))
        area =s*s
        print(area)
        choice = input('press enter to continue or e/E to exit...')
        
    
    
    elif op=='4':
        print('you are finding perimeter of the square =')
        s=float(input("enter the side:-"))
        perimeter=4*s
        print(perimeter)
        choice = input('press enter to continue or e/E to exit...')
    
    elif op=='5':
        print('you are finding area of the triangle =')
        b=float(input("enter the base:-"))
        h=float(input("enter the height:-"))
        area=0.5*b*h
        print(area)
        choice = input('press enter to continue or e/E to exit...')
    
    elif op=='6':  
        print('you are finding area of parallelogram =')
        l=float(input("enter the length"))
        b=float(input("enter the breadth"))
        area=l*b
        print(area)
        choice = input('press enter to continue or e/E to exit...')
    
    elif op=='7':
        print('you are finding area of the circle =')
        r=float(input("enter the radius:-"))
        area=3.14*r*r
        print(area)
        choice = input('press enter to continue or e/E to exit...')
   
    elif op=='8':
        print('you are finding circumference/perimeter of the cicle =')
        r=float(input("enter the radius:-"))
        perimeter=2*3.14*r
        print(perimeter)
        choice = input('press enter to continue or e/E to exit...')
    
    
    elif op=='9':
        print('you are finding area of sphere =')
        r=float(input("enter the radius:-"))
        area=4*3.14*r*r
        print(area)
        choice = input('press enter to continue or e/E to exit...') 
    
    
    elif op=='10':
        print('you are finding area of trapezium =')
        x=float(input('enter the sum of parallel sides:-'))
        h=float(input("enter the height:- "))
        area=0.5*x*h
        print(area)
        choice = input('press enter to continue or e/E to exit...')
   

    elif op=='11':
    
        print('you are finding area of cuboid =')
        l=float(input("enter the value of length:-"))
        b = float(input("enter the value of breadth:-"))
        h = float(input("enter the value of height:-"))
        area = 2*(l*b + b*h + h*l)
        print(area)
        choice = input('press enter to continue or e/E to exit...')
    
    elif op=='12':
        print('you are finding area of cube =')
        a=float(input("enter the value of side:-"))
        cube=6*a*a
        print(cube)
        choice = input('press enter to continue or e/E to exit...')
    
    elif op=='13':
        print('you are finding curved surface area of a cylinder =')
        r=float(input("enter the value of radius:-"))
        h = float(input("enter the value of height:-"))
        area =2*3.14*r*h
        print(area)
        choice = input('press enter to continue or e/E to exit...')
    
            
    elif op=='14':
    
        print('you are finding total surface area of cylinder =')
        r=float(input("enter the value of radius of cylinder:-"))
        h = float(input("enter the value of height of cylinder:-"))
        area=2*3.14*r*(r+h)
        print(area)
        choice = input('press enter to continue or e/E to exit...')
  
    elif op=='15':
        print('you are finding curved surface area of cone =')
        r =float(input("enter the value of radius:-"))
        l = float(input("enter the value of length:-"))
        area = 3.14*r*l
        print(area)
        choice = input('press enter to continue or e/E to exit...')
    
    
    elif op=='16':
        print('you are finding total surface area of cone =')
        r =float(input("enter the value of radius:-"))
        l = float(input("enter the value of length:-"))
        area=3.14*r*(l+r)
        print(area)
        choice = input('press enter to continue or e/E to exit...')

    elif op=='17':
        print('you are finding curved surface area of hemisphere =')
    
        r=float(input('enter the radius:-'))
        area=2*3.14*r*r
        print(area)
        choice = input('press enter to continue or e/E to exit...')
          
    elif op=='18':
        print('you are finding total surface area of hemisphere =')
        r=float(input('enter the radius:-'))
        area=3*3.14*r*r
        print(area)
        choice = input('press enter to continue or e/E to exit...')

    
    elif op=='19':
        print('you are finding volume of cuboid =')
        l=float(input("enter the value of length:-"))
        b = float(input("enter the value of breadth:-"))
        h = float(input("enter the value of height:-"))
        volume=l*b*h
        print(volume)
        choice = input('press enter to continue or e/E to exit...') 
    
    elif op=='20':
        print('you are finding volume of cube =')
        a = float(input('enter value of side:-'))
        volume=a*a*a
        print(volume)
        choice = input('press enter to continue or e/E to exit...')
    
    
    elif op=='21':
        print('you are finding volume of cylinder =')
        r = float(input('enter value of radius:-'))
        h = float(input('enter value of height:-'))
        volume = 3.14*r*r*h
        print(volume)
        choice = input('press enter to continue or e/E to exit...')
   
    
    elif op=='22':
        print('you are finding volume of cone =')
        r = float(input('enter value of radius:-'))
        h = float(input('enter value of height:-'))
        volume = 0.33*3.14*r*r*h
        print(volume)
        choice = input('press enter to continue or e/E to exit...')
    
    elif op=='23':
        print('you are finding volume of sphere =')
        r = float(input('enter value of radius:-'))
        volume = 1.3*3.14*r*r*r
        print(volume)
        choice = input('press enter to continue or e/E to exit...') 
    
    
    elif op=='24':
        print('you are finding volume of hemisphere =')
        r = float(input('enter value of radius:-'))
        volume = 0.66*3.14*r*r*r
        print(volume)
        choice = input('press enter to continue or e/E to exit...')

    else:
        print("Access denied!")

    if choice in ('e','E'):
        break

print('Code exit successfully.')


    
        

    
    
    
    
    
