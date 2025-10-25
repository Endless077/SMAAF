int entry.init0 (int esi, int edx) {
    loc_0x3070:
        // CODE XREF from entry.init0 @ 0x30f4
        rdi = rip + 0x5fa1 // section..bss
        // 0x9018
        rsi = rip + 0x5f9a // section..bss
        // 0x9018
        rsi -= rdi
        rax = rsi
        rsi >>>= 0x3f
        rax >>= 3
        rsi += rax
        rsi >>= 1
        if  (!var) goto loc_0x30a8 // likely
            
    loc_0x30a8:
        // CODE XREFS from entry.init0 @ 0x3092, 0x309e
        re
         // } else {
    loc_0x3094:
        rax = qword [reloc._ITM_registerTMCloneTable] // [0x8fe0:8]=0
        var = rax & rax
        if  (!var) goto loc_0x30a8 // likely
        }
        return eax;
    loc_0x30a0:
        goto loc_rax
         // (break)
    loc_0x000030f0: // orphan
             endbr6
             goto loc_0x3070

}
