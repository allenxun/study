main:main.o DoubleList.o
	gcc -o main main.o DoubleList.o
main.o:main.c DoubleList.h
	gcc -c main.c DoubleList.h
DList.o:DoubleList.c DoubleList.h
	gcc -c DoulbeList.c
clean:
	rm DoubleList.o main.o DoubleList.h.gch
