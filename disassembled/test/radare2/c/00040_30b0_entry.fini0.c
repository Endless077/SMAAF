int entry.fini0 (int esi, int edx) {
    loc_0x30b0:
        endbr6
        var = byte [section..bss] - 0 // [0x9018:1]=0
        if  (var) goto loc_0x30e8 // unlikely
            
    loc_0x30e8:
        // CODE XREF from entry.fini0 @ 0x30bb
        re
         // } else {
    loc_0x30bd:
        push  (rbp)
        var = qword [reloc.__cxa_finalize] - 0 // [0x8ff0:8]=0
        rbp = rsp
        if  (!var) goto loc_0x30d7 // likely
        }
        return eax;
    loc_0x30cb:
        rdi = qword [0x00009008] // [0x9008:8]=0x9008
        fcn.00002270  ()
         // do {
    loc_0x30d7:
        // CODE XREF from entry.fini0 @ 0x30c9
        fcn.00003040  ()
        byte [section..bss] = 1 // [0x9018:1]=0
        rbp = pop  () // rsp
        re
         // } while (?);
        }
        return eax;
}
