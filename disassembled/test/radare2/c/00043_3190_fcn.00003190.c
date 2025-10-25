int fcn.00003190 (int esi, int edx) {
    loc_0x3190:
        // CALL XREF from fcn.00003350 @ 0x3419
        rax = rdi     // arg1
        rdi = rsi     // arg2
        esi = dl
        esi -= 0x41
        r8d = byte [rax + 7]
        // DATA XREF from fcn.00003350 @ 0x33da
        var = esi - 0x19
        if  (((unsigned) var) > 0) goto 0x3250 // likely
            
    loc_0x3250:
        // CODE XREF from fcn.00003190 @ 0x31a4
        esi = 0
        var = dl - r8b
        if  (var) goto loc_0x3246 // unlikely
            
    loc_0x3246:
        // CODE XREFS from fcn.00003190 @ 0x31e0, 0x3255, 0x327d, 0x3286
        eax = esi
        re
         // } else {
    loc_0x3257:
        esi = 1
        var = dl & dl
        if  (var) goto loc_0x31b7 // unlikely
         // } else {
        }
        return eax;
        goto loc_0x31aa
    loc_0x31b7:
        // CODE XREF from fcn.00003190 @ 0x325e
        edx = cl
        r8d = byte [rax + 8]
        edx -= 0x41
        var = edx - 0x19
        if  (((unsigned) var) > 0) goto 0x3278 // likely
            
    loc_0x3278:
        // CODE XREF from fcn.00003190 @ 0x31c5
        esi = 0
        // DATA XREF from fcn.00003290 @ 0x32f4
        var = cl - r8b
        if  (var) goto loc_0x3246 // unlikely
    loc_0x327f:
        esi = 1
        var = cl & cl
        if  (!var) goto loc_0x3246 // likely
    loc_0x3288:
        goto loc_0x31d8
         // do {
    loc_0x31d8:
        // CODE XREF from fcn.00003190 @ 0x3288
        esi = 1
        var = rax - rdi
        if  (!var) goto loc_0x3246 // likely
         // } while (?);
         // } while (?);
        }
        return eax;
        goto loc_0x31cb
    loc_0x3270:
        // CODE XREFS from fcn.00003190 @ 0x31b1, 0x31d2
        esi = 0
        eax = esi
        re
         // (break)
    loc_0x000031e2: // orphan
             edx = 9
             goto loc_0x320d

    loc_0x000031f0: // orphan
         // CODE XREF from fcn.00003190 @ 0x3229
         r8d += 0x20              // "@"
         esi += 0x20              // "@"
         var = r10d - 0x19
         if  (((unsigned) var) > 0) goto 0x3204 // unlikely

    loc_0x000031fd: // orphan
         r9d += 0x20              // "@"
         ecx += 0x20              // "@"

    loc_0x00003204: // orphan
         // CODE XREFS from fcn.00003190 @ 0x31fb, 0x323b
         rdx += 1
         var = sil - cl
         if  (var) goto loc_0x323d // unlikely

    loc_0x0000320d: // orphan
         // CODE XREF from fcn.00003190 @ 0x31e7
         r8d = byte [rax + rdx]
         r9d = byte [rdi + rdx]
         r11d = r8 - 0x41
         esi = r8d
         r10d = r9 - 0x41
         ecx = r9d
         var = r11d - 0x19
         if  (((unsigned) var) <= 0) goto 0x31f0 // unlikely

    loc_0x0000322b: // orphan
         var = r10d - 0x19
         if  (((unsigned) var) > 0) goto 0x3238 // unlikely

    loc_0x00003231: // orphan
         r9d += 0x20              // "@"
         ecx += 0x20              // "@"

    loc_0x00003238: // orphan
         // CODE XREF from fcn.00003190 @ 0x322f
         var = r8d & r8d
         if  (var) goto loc_0x3204 // unlikely

    loc_0x0000323d: // orphan
         // CODE XREF from fcn.00003190 @ 0x320b
         esi = 0
         var = r8d - r9d
         sil = e

    loc_0x00003264: // orphan
         eax = esi
         re

}
