import targets
import testlib

class spike64_hart(targets.Hart):
    xlen = 64
    ram = 0x1212340000
    ram_size = 0x10000000
    bad_address = ram - 8
    instruction_hardware_breakpoint_count = 4
    reset_vectors = [0x1000]
    link_script_path = "spike64.lds"
    #misa = 0x8000000000141125
    misa = 0x8000000000141105    

class spike64(targets.Target):
    harts = [spike64_hart()]
    openocd_config_path = "spike-1.cfg"
    timeout_sec = 180
    implements_custom_test = True
    freertos_binary = "bin/RTOSDemo64.axf"
    support_unavailable_control = True

    def create(self):
        # # 32-bit FPRs only
        return testlib.Spike(self, isa="RV64IMAC", progbufsize=2,
                abstract_rti=30, support_abstract_csr=True,
                support_abstract_fpr=True)
