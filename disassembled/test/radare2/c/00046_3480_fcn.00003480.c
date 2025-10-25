int fcn.00003480 (int esi, int edx) {
    loc_0x3480:
        // CALL XREF from fcn.000035a0 @ 0x35c2
        push  (rbp)
        rbp = rsp
        push  (r13)
        push  (r12)
        push  (rbx)
        rbx = rdi     // arg1
        rsp -= 8
        sym.imp.fileno  ()
        // int fileno(?)
        rdi = rbx
        var = eax & eax
        js 0x3507     // unlikely
            
    loc_0x3507:
        // CODE XREF from fcn.00003480 @ 0x349a
        rsp += 8
        rbx = pop  ()
        r12 = pop  ()
        r13 = pop  ()
        rbp = pop  ()
        goto loc_0x22f0 // sym.imp.fclose // sym.imp.fclose
        // int fclose(?)
         // } else {
    loc_0x349c:
        sym.imp.__freading  ()
        var = eax & eax
        if  (var) goto loc_0x34e8 // unlikely
        }
        return eax;
    loc_0x34a5:
        // CODE XREF from fcn.00003480 @ 0x3502
        rdi = rbx
        sym.imp.__freading  ()
        var = eax & eax
        if  (var) goto loc_0x3520 // unlikely
            
    loc_0x3520:
        // CODE XREF from fcn.00003480 @ 0x34af
        var = dword [rbx] & 0x100
        if  (!var) goto loc_0x34b1 // unlikely
    loc_0x3528:
        rax = qword [rbx + 8]
        var = qword [rbx + 0x10] - rax
        if  (!var) goto loc_0x3550 // unlikely
            
    loc_0x3550:
        // CODE XREF from fcn.00003480 @ 0x3530
        rax = qword [rbx + 0x20] // elf_phdr
        var = qword [rbx + 0x28] - rax
        if  (var) goto loc_0x3532 // likely
    loc_0x355a:
        var = qword [rbx + 0x48] - 0
        if  (var) goto loc_0x3532 // likely
    loc_0x3561:
        rdi = rbx     // FILE *stream
        sym.imp.fileno  ()
        // int fileno(?)
        esi = 0
        edx = 1
        edi = eax
        sym.imp.lseek  ()
        var = rax - 0xffffffffffffffff
        if  (!var) goto loc_0x34b1 // unlikely
    loc_0x3581:
        dword [rbx] &= 0xffffffef // [0xffffffef:4]=-1 // 4294967279
        qword [rbx + 0x90] = rax
        goto loc_0x34b1
    loc_0x000034b1: // orphan
             // CODE XREFS from fcn.00003480 @ 0x3526, 0x3541, 0x357b, 0x358b
             rdi = rbx                // FILE *stream
             sym.imp.fflush  ()
                                      // int fflush(?)
             var = eax & eax
             if  (!var) goto loc_0x3504 // likely

    loc_0x000034bd: // orphan
         sym.imp.__errno_location  ()
         rdi = rbx                // FILE *stream
         r13d = dword [rax]
         r12 = rax
         sym.imp.fclose  ()
                                  // int fclose(?)
         var = r13d & r13d
         if  (var) goto loc_0x3590 // likely

    loc_0x000034d9: // orphan
         // CODE XREF from fcn.00003480 @ 0x3599
         rsp += 8
         rbx = pop  ()
         r12 = pop  ()
         r13 = pop  ()
         rbp = pop  ()
         re

    loc_0x000034e8: // orphan
         // CODE XREF from fcn.00003480 @ 0x34a3
         rdi = rbx                // FILE *stream
         sym.imp.fileno  ()
                                  // int fileno(?)
         esi = 0
         edx = 1
         edi = eax
         sym.imp.lseek  ()
         var = rax - 0xffffffffffffffff
         if  (var) goto loc_0x34a5 // likely

    loc_0x00003504: // orphan
         // CODE XREF from fcn.00003480 @ 0x34bb
         rdi = rbx

    loc_0x00003532: // orphan
         // CODE XREFS from fcn.00003480 @ 0x3558, 0x355f
         edx = 1
         esi = 0
         rdi = rbx
         sym.imp.fseeko  ()
         goto loc_0x34b1

    loc_0x00003590: // orphan
         // CODE XREF from fcn.00003480 @ 0x34d3
         dword [r12] = r13d
         eax = 0xffffffff         // -1
         goto loc_0x34d9

}
