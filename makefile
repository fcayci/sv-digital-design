# author: Furkan Cayci, 2021
# description:
#   run make to check syntax of all files
#   run make simulate MODULE=tb_xxx to simulate the given testbench.
#   run make display to open the waveform using gtkwave

CC = iverilog
SIM = vvp
VIEW = gtkwave
QUIET = @

MODULE?= tb_adder_str

SOURCES = $(wildcard rtl/*.sv)
TBS = $(wildcard tb/tb_*.sv)

CFLAGS += -Wall # enable all warnings
CLFAGS += -Winfloop
CFLAGS += -gassertions
CFLAGS += -g2012 # enable system verilog

.PHONY: all
all: check
	@echo ">>> completed..."

.PHONY: check
check:
	@echo ">>> Checking syntax on all designs..."
	$(QUIET)$(CC) $(CFLAGS) -o /dev/null $(SOURCES) $(TBS)

.PHONY: simulate
simulate:
	@echo ">>> simulating design " $(MODULE)
	$(QUIET)$(CC) $(CFLAGS) -o test.vvp \
		-s $(MODULE) $(SOURCES) $(TBS)
	$(SIM) -N test.vvp -lxt2
	@echo ">>> waveform is ready for " $(MODULE)

.PHONY: display
display:
	@echo ">>> displaying design " $(MODULE)
	$(QUIET)$(VIEW) dump.lx2
	@echo ">>> waveform is ready for " $(MODULE)

.PHONY: clean
clean:
	@echo "cleaning design..."
	$(QUIET)rm -rf test.vvp
	$(QUIET)rm -rf dump.lx2
