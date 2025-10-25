int fcn.00003100 (int esi, int edx) {
    loc_0x3100:
        // CALL XREFS from fcn.00003610 @ 0x28f2, 0x2914
        eax = rdi - 0x41 // arg1
        var = al - 0x25
        if  (((unsigned) var) > 0) goto case.0x3118.71 // case.default.0x3118 // likely
            
    loc_0x3120:
        // CODE XREFS from fcn.00003100 @ 0x3105, 0x3118
        edi = dil
        eax = rdi - 0x30
        re
         // } else {
    loc_0x3107:
        rdx = rip + 0x2f12 // 0x6020 // "`\xd1\xff\xffP\xd1\xff\xff\x10\xd1\xff\xff \xd1\xff\xff0\xd1\xff\xff@\xd1\xff\xff"
        eax = al
        rax = dword [rdx + rax*4]
        rax += rdx    // (pstr 0x00000ab8) "terTMCloneTable" case.0x3118.97
        goto loc_rax  // switch table (38 cases) at 0x6020 // case.0x3118.97
        }
        return eax;
    loc_0x00003130: // orphan
             // CODE XREF from fcn.00003100 @ 0x3118
             eax = 0xc
             re

    loc_0x00003140: // orphan
         // CODE XREF from fcn.00003100 @ 0x3118
         eax = 0xd
         re

    loc_0x00003150: // orphan
         // CODE XREF from fcn.00003100 @ 0x3118
         eax = 0xe
         re

    loc_0x00003160: // orphan
         // CODE XREF from fcn.00003100 @ 0x3118
         eax = 0xf
         re

    loc_0x00003170: // orphan
         // CODE XREF from fcn.00003100 @ 0x3118
         eax = 0xb
         // DATA XREF from fcn.00003350 @ 0x3412
         re

    loc_0x00003180: // orphan
         // CODE XREF from fcn.00003100 @ 0x3118
         eax = 0xa
         re

}
