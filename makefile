# author: Furkan Cayci, 2021
# description:
#   run make to check syntax of all files
#   run make simulate MODULE=tb_xxx to run the given testbench.
#   run make display MODULE=tb_xxx to create a dump file and
#       open the waveform using gtkwave

QUIET = @
CC = iverilog
SIM = vvp
VIEW = gtkwave

# temporary macos hack
ifeq ($(shell uname -m), arm64)
VIEW = open -a gtkwave
endif

MODULE?= tb_adder_str

VERILOG_SOURCES  = $(wildcard rtl/*.sv)
VERILOG_SOURCES += $(wildcard tb/tb_*.sv)

CFLAGS += -Wall # enable all warnings
CFLAGS += -Winfloop
CFLAGS += -Wno-timescale
CFLAGS += -gassertions
CFLAGS += -g2012 # enable system verilog

.PHONY: all
all: check
	@echo ">>> Completed..."


.PHONY: check
check:
	@echo ">>> Checking syntax on all designs..."
	$(QUIET)$(CC) $(CFLAGS) -o /dev/null $(VERILOG_SOURCES)


.PHONY: simulate
simulate: clean
	@echo ">>> Simulating design " $(MODULE)
	$(QUIET)$(CC) $(CFLAGS) -o $(MODULE).vvp -s $(MODULE) $(VERILOG_SOURCES)
	$(QUIET)$(SIM) -n $(MODULE).vvp
	@echo ">>> Done"


.PHONY: display
display: clean dumpy.sv
	@echo ">>> Displaying design " $(MODULE)
	$(QUIET)$(CC) $(CFLAGS) -o $(MODULE).vvp -s dumpy $(VERILOG_SOURCES) dumpy.sv
	$(QUIET)$(SIM) -n $(MODULE).vvp -lxt2
	$(QUIET)$(VIEW) $(MODULE).lx2

dumpy.sv:
	@echo '>>> Creating top module for dumping waveform'
	@echo 'module dumpy();' > $@
	@echo '$(MODULE) test();' >> $@
	@echo 'initial' >> $@
	@echo 'begin' >> $@
	@echo '    $$dumpfile("$(MODULE).lx2");' >> $@
	@echo '    $$dumpvars(0, dumpy);' >> $@
	@echo 'end' >> $@
	@echo 'endmodule' >> $@


.PHONY: clean
clean:
	@echo "cleaning design..."
	$(QUIET)rm -rf dumpy.sv
	$(QUIET)rm -rf $(MODULE).vvp
	$(QUIET)rm -rf $(MODULE).lx2
