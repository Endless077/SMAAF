int fcn.00003290 (int esi, int edx) {
    loc_0x3290:
        // CALL XREFS from fcn.00003610 @ 0x2b80, 0x2b92
        push  (rbp)
        edx = 5       // (pstr 0x00000101) " "
        rbp = rsp
        push  (r13)
        r13 = rsi     // arg2
        rsi = rdi     // arg1
        push  (r12)
        r12 = rdi     // arg1
        edi = 0
        push  (rbx)
        rsp -= 8
        sym.imp.dcgettext  ()
        rbx = rax
        var = r12 - rax
        if  (!var) goto loc_0x32c8 // likely
            
    loc_0x32c8:
        // CODE XREF from fcn.00003290 @ 0x32b8
        edi = 0xe     // nl_item item
        sym.imp.nl_langinfo  ()
        // char *nl_langinfo(?)
        var = rax & rax
        if  (!var) goto loc_0x32ed // likely
            
    loc_0x32ed:
        // CODE XREFS from fcn.00003290 @ 0x32d5, 0x32da
        rax = rip + 0x327b // str.ASCII
        // 0x656f // "ASCII"
         // do {
    loc_0x32f4:
        // CODE XREF from fcn.00003290 @ 0x32e6
        r8 = rip + 0x327a // str.UTF_8
        // 0x6575 // "UTF-8"
        goto loc_0x331b
         // } while (?);
         // } while (?);
         // } while (?);
        }
        return eax;
    loc_0x000032dc: // orphan
             rdx = rip + 0x3292       // str.UTF_8
                                      // 0x6575 // "UTF-8"
             var = rax - rdx
             if  (var) goto loc_0x32f4 // likely

    loc_0x000032e8: // orphan
         rbx = r13
         goto loc_0x32ba

    loc_0x000032fd: // orphan
         // CODE XREF from fcn.00003290 @ 0x3332
         edi += 0x20              // "@"
         ecx += 0x20              // "@"
         var = r9d - 0x19
         if  (((unsigned) var) > 0) goto 0x330f // unlikely

    loc_0x00003309: // orphan
         esi += 0x20              // "@"
         edx += 0x20              // "@"

    loc_0x0000330f: // orphan
         // CODE XREFS from fcn.00003290 @ 0x3307, 0x3341
         rax += 1
         r8 += 1
         var = cl - dl
         if  (var) goto loc_0x3343 // unlikely

    loc_0x0000331b: // orphan
         // CODE XREF from fcn.00003290 @ 0x32fb
         edi = byte [rax]
         esi = byte [r8]
         r10d = rdi - 0x41
         ecx = edi
         r9d = rsi - 0x41
         edx = esi
         var = r10d - 0x19
         if  (((unsigned) var) <= 0) goto 0x32fd // unlikely

    loc_0x00003334: // orphan
         var = r9d - 0x19
         if  (((unsigned) var) > 0) goto 0x333d // unlikely

    loc_0x0000333a: // orphan
         esi += 0x20              // "@"

    loc_0x0000333d: // orphan
         // CODE XREF from fcn.00003290 @ 0x3338
         edx = esi
         var = edi & edi
         if  (var) goto loc_0x330f // unlikely

    loc_0x00003343: // orphan
         // CODE XREF from fcn.00003290 @ 0x3319
         var = edi - esi
         if  (!var) rbx = r13
         goto loc_0x32ba

}
