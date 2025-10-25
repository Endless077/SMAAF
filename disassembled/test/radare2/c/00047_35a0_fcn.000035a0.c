int fcn.000035a0 (int esi, int edx) {
    loc_0x35a0:
        // CALL XREFS from fcn.00003610 @ 0x4f07, 0x4f5a
        push  (rbp)
        rbp = rsp
        push  (r13)
        push  (r12)
        push  (rbx)
        rbx = rdi     // arg1
        rsp -= 8
        sym.imp.__fpending  ()
        r12d = dword [rbx]
        rdi = rbx
        r13 = rax
        r12d &= 0x20  // "@"
        fcn.00003480  () // fcn.00003480(0x0)
        var = r12d & r12d
        if  (var) goto loc_0x35f0 // unlikely
            
    loc_0x35f0:
        // CODE XREF from fcn.000035a0 @ 0x35ca
        var = eax & eax
        if  (var) goto loc_0x35ff // unlikely
            
    loc_0x35ff:
        // CODE XREFS from fcn.000035a0 @ 0x35d3, 0x35f2
        eax = 0xffffffff // -1
        goto loc_0x35e5
         // do {
    loc_0x35e5:
        // CODE XREFS from fcn.000035a0 @ 0x35ce, 0x3604
        rsp += 8
        rbx = pop  ()
        r12 = pop  ()
        r13 = pop  ()
        rbp = pop  ()
        // DATA XREF from fcn.00003610 @ 0x2fd6
        re
         // } while (?);
         // } while (?);
         // } while (?);
        }
        return eax;
        goto loc_0x35cc
    loc_0x35d0:
        var = r13 & r13
        if  (var) goto loc_0x35ff // unlikely
    loc_0x35d5:
        sym.imp.__errno_location  ()
        var = dword [rax] - 9
        al = ne
        eax = al
        eax ~= eax
}
