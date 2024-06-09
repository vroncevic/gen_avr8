# Makefile
# Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# new_simple_test is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# new_simple_test is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program_name. If not, see <http://www.gnu.org/licenses/>.

include sources.mk
include subdir.mk
include objects.mk
include cflags.mk
include odflags.mk
include ocflags.mk
include csflags.mk
include tools.mk

ifneq ($(MAKECMDGOALS),clean)
	ifneq ($(strip $(I_DEPS)),)
		-include $(I_DEPS)
	endif
	ifneq ($(strip $(ASM_DEPS)),)
		-include $(ASM_DEPS)
	endif
	ifneq ($(strip $(M_DEPS)),)
		-include $(M_DEPS)
	endif
	ifneq ($(strip $(MI_DEPS)),)
		-include $(MI_DEPS)
	endif
	ifneq ($(strip $(S_DEPS)),)
		-include $(S_DEPS)
	endif
	ifneq ($(strip $(S_UPPER_DEPS)),)
		-include $(S_UPPER_DEPS)
	endif
	ifneq ($(strip $(C_DEPS)),)
		-include $(C_DEPS)
	endif
endif

LSS += \
	new_simple_test.lss

FLASH_IMAGE += \
	new_simple_test.hex

SIZEDUMMY += \
	sizedummy

CLEAN_LIST += \
	$(FLASH_IMAGE) \
	$(ELFS) \
	$(I_DEPS) \
	$(OBJS) \
	$(ASM_DEPS) \
	$(M_DEPS) \
	$(MI_DEPS) \
	$(S_DEPS) \
	$(SIZEDUMMY) \
	$(S_UPPER_DEPS) \
	$(LSS) \
	$(C_DEPS) \
	main.i \
	main.s \
	new_simple_test.map \
	new_simple_test.elf

all: new_simple_test.elf secondary-outputs

new_simple_test.elf: $(OBJS) $(USER_OBJS)
	@echo 'Building target: $@'
	@echo 'Invoking: AVR C Linker'
	$(CC) $(CFLAGS) -o "new_simple_test.elf" $(OBJS) $(USER_OBJS) $(LIBS)
	@echo 'Finished building target: $@'
	@echo ' '

new_simple_test.lss: new_simple_test.elf
	@echo 'Invoking: AVR Create Extended Listing'
	$(OD) $(ODFLAGS) new_simple_test.elf > "new_simple_test.lss"
	@echo 'Finished building: $@'
	@echo ' '

new_simple_test.hex: new_simple_test.elf
	@echo 'Create Flash image (ihex format)'
	$(OC) $(OCFLAGS) -O ihex new_simple_test.elf "new_simple_test.hex"
	@echo 'Finished building: $@'
	@echo ' '

sizedummy: new_simple_test.elf
	@echo 'Invoking: Print Size'
	$(CS) $(CSFLAGS) new_simple_test.elf
	@echo 'Finished building: $@'
	@echo ' '

clean:
	@for item in $(CLEAN_LIST);do echo "$(RM) $$item";$(RM) $$item;done
	@echo ' '

secondary-outputs: $(LSS) $(FLASH_IMAGE) $(SIZEDUMMY)

