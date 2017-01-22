BIN := bin/flotplot
CC := g++
LIB := -lncurses
CFLAGS := -g# -Wall
INC := -I include

all: $(BIN) test/unittest
	./test/unittest
	@echo "DONE!"

$(BIN) : build/main.o build/Filereader.o build/Plotdata.o
	$(CC) $^ -o $(BIN) $(LIB)

build/main.o : src/main.cpp
	$(CC) $(CFLAGS) $(INC) -c -o $@ $<
build/Filereader.o : src/Filereader.cpp
	$(CC) $(CFLAGS) $(INC) -c -o $@ $<
build/Plotdata.o : src/Plotdata.cpp
	$(CC) $(CFLAGS) $(INC) -c -o $@ $<
test/unittest : build/Filereader.o build/flot_test.o
	$(CC) $^ -o test/unittest $(LIB) -lcppunit
build/flot_test.o : test/flot_test.cpp
	$(CC) $(CFLAGS) $(INC) -c -o $@ $<

