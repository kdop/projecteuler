CC=gcc
CXX=g++
RM=rm -rf
CPPFLAGS=-std=gnu++11
EXEC_DIR=build

SOURCES=${wildcard *.cpp}
EXEC=${patsubst %.cpp,%,${SOURCES}}

.PHONY: default all makedir clean

default: all

all: makedir ${EXEC}

makedir:
	mkdir -p ${EXEC_DIR}
	echo "*" > ${EXEC_DIR}/.gitignore

${EXEC}:
	${CXX} $@.cpp ${CPPFLAGS} -o ${EXEC_DIR}/$@

clean:
	$(RM) ${EXEC_DIR}
