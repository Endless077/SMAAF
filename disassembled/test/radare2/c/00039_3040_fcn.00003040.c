int fcn.00003040 (int esi, int edx) {
    loc_0x3040:
        // CALL XREF from entry.fini0 @ 0x30d7
        rdi = rip + 0x5fd1 // section..bss
        // 0x9018
        rax = rip + 0x5fca // section..bss
        // 0x9018
        var = rax - rdi
        if  (!var) goto loc_0x3068 // likely
            
    loc_0x3068:
        // CODE XREFS from fcn.00003040 @ 0x3051, 0x305d
        re
         // } else {
    loc_0x3053:
        rax = qword [reloc._ITM_deregisterTMCloneTable] // [0x8fc0:8]=0
        var = rax & rax
        if  (!var) goto loc_0x3068 // likely
        }
        return eax;
    loc_0x305f:
        goto loc_rax
         // (break)
}
