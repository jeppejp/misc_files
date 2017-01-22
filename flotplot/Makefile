CC := g++ # This is the main compiler
# CC := clang --analyze # and comment out the linker last line for sanity
SRCDIR := src
TSTDIR := test
BUILDDIR := build
TARGET := bin/runner
TESTBIN := test/testrunner
#  
SRCEXT := cpp
#SOURCES := src/Plotdata.cpp src/Filereader.cpp test/dirt_test.cpp src/main.cpp 
SOURCES := $(shell find src/ | grep .cpp | grep -v .swp)
OBJECTS := $(shell find src/ | grep .cpp | grep -v .swp | sed 's/src/build/g' | sed 's/.cpp/.o/g')
CFLAGS := -g # -Wall
LIB := -lncurses -lcppunit
INC := -I include

TESTSRC := $(shell find test/ | grep .cpp | grep -v .swp)
TESTOBJECTS := $(shell find test/ | grep .cpp | grep -v .swp | sed 's/.cpp/.o/g')

$(TARGET): $(OBJECTS)
	@echo " Linking..."
	@mkdir -p bin
	@echo " $(CC) $^ -o $(TARGET) $(LIB)"; $(CC) $^ -o $(TARGET) $(LIB)

$(BUILDDIR)/%.o: $(SRCDIR)/%.$(SRCEXT)
	@echo " Compiling"
	@mkdir -p $(BUILDDIR)
	@echo " $(CC) $(CFLAGS) $(INC) -c -o $@ $<"; $(CC) $(CFLAGS) $(INC) -c -o $@ $<

clean:
	@echo " Cleaning..."; 
	@echo " $(RM) -r $(BUILDDIR) $(TARGET)"; $(RM) -r $(BUILDDIR) $(TARGET)
	$(MAKE) -C test clean
test:
	$(MAKE) -C test clean
	$(MAKE) -C test

$(TESTBIN): $(OBJECTS) $(TESTOBJECTS)

