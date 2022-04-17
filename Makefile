PYTHON_PATH := /usr/bin/python3
ROOT_DIR := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
SCALE_BOARD_PATH := /usr/bin/scale-board
LOGS_DIR := /var/log/scale-board


ifeq (, $(shell which $(PYTHON_PATH) ))
  $(error "PYTHON=$(PYTHON_PATH) not found")
endif

PYTHON_VERSION_MIN=3.9
PYTHON_VERSION=$(shell $(PYTHON_PATH) -c 'import sys; print("%d.%d"% sys.version_info[0:2])' )
PYTHON_VERSION_OK=$(shell $(PYTHON_PATH) -c 'import sys; print(int(int(sys.version_info[1]) > int($(PYTHON_VERSION_MIN)[2:])))')

ifeq ($(PYTHON_VERSION_OK),0)
  $(error "Need python $(PYTHON_VERSION) >= $(PYTHON_VERSION_MIN)")
endif

clear:
	-rm -r "$(ROOT_DIR)/venvScaleBoard"
	-rm $(SCALE_BOARD_PATH)

clear-dirs:
	-rm -r $(LOGS_DIR)

install:
	make clear

	virtualenv --python=$(PYTHON_PATH) "$(ROOT_DIR)/venvScaleBoard"
	"$(ROOT_DIR)/venvScaleBoard/bin/python3" "$(ROOT_DIR)/setup.py" install

	-mkdir $(LOGS_DIR)

	-ln -s "$(ROOT_DIR)/venvScaleBoard/bin/scale-board" $(SCALE_BOARD_PATH)

clear-install:
	make clear
	make clear-dirs
	make install
