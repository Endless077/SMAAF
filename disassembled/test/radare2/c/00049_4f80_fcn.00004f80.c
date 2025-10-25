int fcn.00004f80 (int esi, int edx) {
    loc_0x4f80:
        // CALL XREF from fcn.00003610 @ 0x2bc1
        push  (rbp)
        r10 = rcx     // arg4
        rbp = rsp
        push  (r15)
        push  (r14)
        push  (r13)
        push  (r12)
        r12 = rdi     // arg1
        push  (rbx)
        rsp -= 0x168
        qword [var_c0h] = r8 // arg5
        qword [var_b8h] = r9 // arg6
        var = al & al
        if  (!var) goto loc_0x4fd5 // likely
            
    loc_0x4fd5:
        // CODE XREF from fcn.00004f80 @ 0x4faa
        rax = qword fs:[0x28]
        qword [var_e8h] = rax
        eax = 0
        r9 = var_e0h
        rax = arg_10h
        edi = 0
        qword [var_158h] = rax
        rcx = arg_10h
        r8d = 0
        ebx = 0
        dword [var_160h] = 0x20 // "@"
        edx = 0x20    // "@"
        rsi = var_140h
        dword [var_15ch] = 0x30 // '0'
        qword [var_150h] = r9
        goto loc_0x5058
         // do {
    loc_0x5058:
        // CODE XREF from fcn.00004f80 @ 0x502b
        var = edx - 0x2f
        if  (((unsigned) var) <= 0) goto 0x5030 // likely
         // } while (?);
         // } while (?);
        }
        return eax;
    loc_0x00005030: // orphan
             // CODE XREF from fcn.00004f80 @ 0x505b
             eax = edx
             r8d = 1
             edx += 8
             rax += r9
             rax = qword [rax]
             qword [rsi + rbx*8] = rax
             var = rax & rax
             if  (!var) goto loc_0x5075 // unlikely

    loc_0x0000504a: // orphan
         // CODE XREF from fcn.00004f80 @ 0x5073
         rbx += 1
         var = rbx - 0xa
         if  (!var) goto loc_0x5146 // unlikely

    loc_0x0000505d: // orphan
         rax = rcx
         edi = 1
         rcx += 8
         rax = qword [rax]
         qword [rsi + rbx*8] = rax
         var = rax & rax
         if  (var) goto loc_0x504a // likely

    loc_0x00005075: // orphan
         // CODE XREF from fcn.00004f80 @ 0x5048
         var = dil & dil
         if  (!var) goto loc_0x5081 // likely

    loc_0x0000507a: // orphan
         qword [var_158h] = rcx

    loc_0x00005081: // orphan
         // CODE XREF from fcn.00004f80 @ 0x5078
         var = r8b & r8b
         if  (!var) goto loc_0x508c // likely

    loc_0x00005086: // orphan
         dword [var_160h] = edx

    loc_0x0000508c: // orphan
         // CODE XREF from fcn.00004f80 @ 0x5084
         r9 = r10
         r8 = rip + str.GNU_coreutils // 0x65be // "GNU coreutils"
         rdi = r12
         eax = 0
         rcx = rip + str.echo     // 0x65cc // "echo"
         rdx = rip + str._s___s___s_n // 0x65d1 // "%s (%s) %s\n"
         esi = 2
         sym.imp.__fprintf_chk  ()
         edi = 0
         edx = 5
         rsi = rip + 0x151c       // "(C)"
                                  // 0x65dd
         sym.imp.dcgettext  ()
         r8d = 0x7e7
         esi = 2
         rdi = r12
         rcx = rax
         rdx = rip + str.Copyright__s__d_Free_Software_Foundation__Inc. // 0x6540 // "Copyright %s %d Free Software Foundation, Inc."
         eax = 0
         sym.imp.__fprintf_chk  ()
         rsi = r12
         edi = 0xa
         sym.imp.fputc_unlocked  ()
         edi = 0
         edx = 5
         rsi = rip + str.License_GPLv3:_GNU_GPL_version_3_or_later___s_._nThis_is_free_software:_you_are_free_to_change_and_redistribute_it._nThere_is_NO_WARRANTY__to_the_extent_permitted_by_law._n // 0x6718 // "License GPLv3+: GNU GPL version 3 or later <%s>.\nThis is free software: you are free to change and redistribute it.\nThere is NO WARRANTY, to the extent permitted by law.\n"
         sym.imp.dcgettext  ()
         esi = 2
         rdi = r12
         rcx = rip + str.https:__gnu.org_licenses_gpl.html // 0x67c8 // "https://gnu.org/licenses/gpl.html"
         rdx = rax
         eax = 0
         sym.imp.__fprintf_chk  ()
         rsi = r12
         edi = 0xa
         sym.imp.fputc_unlocked  ()
         var = rbx - 9
         if  (((unsigned) var) > 0) goto case.0x5143.0 // unlikely

    loc_0x00005135: // orphan
         rdx = rip + 0x12a8       // 0x63e4
         rax = dword [rdx + rbx*4]
         rax += rdx               // case.default.0x5143
         goto loc_rax             // switch table (10 cases) at 0x63e4 // case.default.0x5143

    loc_0x00005146: // orphan
         // CODE XREF from fcn.00004f80 @ 0x5052
         r9 = r10
         r8 = rip + str.GNU_coreutils // 0x65be // "GNU coreutils"
         rdi = r12
         eax = 0
         rcx = rip + str.echo     // 0x65cc // "echo"
         rdx = rip + str._s___s___s_n // 0x65d1 // "%s (%s) %s\n"
         esi = 2
         sym.imp.__fprintf_chk  ()
         edx = 5
         rsi = rip + 0x1464       // "(C)"
                                  // 0x65dd
         edi = 0
         sym.imp.dcgettext  ()
         r8d = 0x7e7
         esi = 2
         rdi = r12
         rcx = rax
         rdx = rip + str.Copyright__s__d_Free_Software_Foundation__Inc. // 0x6540 // "Copyright %s %d Free Software Foundation, Inc."
         eax = 0
         sym.imp.__fprintf_chk  ()
         rsi = r12
         edi = 0xa
         sym.imp.fputc_unlocked  ()
         edx = 5
         rsi = rip + str.License_GPLv3:_GNU_GPL_version_3_or_later___s_._nThis_is_free_software:_you_are_free_to_change_and_redistribute_it._nThere_is_NO_WARRANTY__to_the_extent_permitted_by_law._n // 0x6718 // "License GPLv3+: GNU GPL version 3 or later <%s>.\nThis is free software: you are free to change and redistribute it.\nThere is NO WARRANTY, to the extent permitted by law.\n"
         edi = 0
         sym.imp.dcgettext  ()
         rcx = rip + str.https:__gnu.org_licenses_gpl.html // 0x67c8 // "https://gnu.org/licenses/gpl.html"
         esi = 2
         rdi = r12
         rdx = rax
         eax = 0
         sym.imp.__fprintf_chk  ()
         rsi = r12
         edi = 0xa
         sym.imp.fputc_unlocked  ()
         r11 = qword [var_100h]
         r10 = qword [var_108h]
         edx = 5
         r9 = qword [var_130h]
         r8 = qword [var_138h]
         rsi = rip + str.Written_by__s___s___s__n_s___s___s___s__n_s___s__and_others._n // 0x67f0 // "Written by %s, %s, %s,\n%s, %s, %s, %s,\n%s, %s, and others.\n"
         rcx = qword [var_140h]
         qword [var_188h] = r11
         qword [var_180h] = r10
         r14 = qword [var_110h]
         qword [var_178h] = r9
         r13 = qword [var_118h]
         qword [var_170h] = r8
         rbx = qword [var_120h]
         qword [var_168h] = rcx
         r15 = qword [var_128h]

    loc_0x00005253: // orphan
         // CODE XREF from fcn.00004f80 @ 0x55eb
         edi = 0
         sym.imp.dcgettext  ()
         r11 = qword [var_188h]
         rdx = rax
         push  (r11)

    loc_0x00005266: // orphan
         // CODE XREF from fcn.00004f80 @ 0x532e
         r10 = qword [var_180h]
         r9 = qword [var_178h]
         rdi = r12
         eax = 0
         r8 = qword [var_170h]
         rcx = qword [var_168h]
         esi = 2
         push  (r10)
         push  (r14)
         push  (r13)
         push  (rbx)
         push  (r15)
         sym.imp.__fprintf_chk  ()
         rsp += 0x30

    loc_0x0000529e: // orphan
         // XREFS: CODE 0x0000512f  CODE 0x00005143  CODE 0x000053be  
         // XREFS: CODE 0x0000547d  CODE 0x00005506  CODE 0x00005544  
         // XREFS: CODE 0x00005578  
         rax = qword [var_e8h]
         rax -= qword fs:[0x28]
         if  (var) goto loc_0x55f0 // unlikely

    loc_0x000052b4: // orphan
         rsp = var_28h
         rbx = pop  ()
         r12 = pop  ()
         r13 = pop  ()
         r14 = pop  ()
         r15 = pop  ()            // rsp
         rbp = pop  ()
         re

    loc_0x000052c3: // orphan
         // CODE XREF from fcn.00004f80 @ 0x5143
         r10 = qword [var_108h]
         r9 = qword [var_130h]
         edi = 0
         edx = 5
         r8 = qword [var_138h]
         rcx = qword [var_140h]
         rsi = rip + str.Written_by__s___s___s__n_s___s___s___s__nand__s._n // 0x68d0 // "Written by %s, %s, %s,\n%s, %s, %s, %s,\nand %s.\n"
         qword [var_180h] = r10
         r14 = qword [var_110h]
         qword [var_178h] = r9
         r13 = qword [var_118h]
         qword [var_170h] = r8
         rbx = qword [var_120h]
         qword [var_168h] = rcx
         r15 = qword [var_128h]
         sym.imp.dcgettext  ()
         rdx = rax
         push  (rax)
         goto loc_0x5266

    loc_0x00005333: // orphan
         // CODE XREF from fcn.00004f80 @ 0x5143
         r9 = qword [var_130h]
         r14 = qword [var_110h]
         edi = 0
         edx = 5
         r13 = qword [var_118h]
         rbx = qword [var_120h]
         rsi = rip + str.Written_by__s___s___s__n_s___s___s__and__s._n // 0x68a0 // "Written by %s, %s, %s,\n%s, %s, %s, and %s.\n"
         r15 = qword [var_128h]
         r8 = qword [var_138h]
         qword [var_178h] = r9
         rcx = qword [var_140h]
         qword [var_170h] = r8
         qword [var_168h] = rcx
         sym.imp.dcgettext  ()
         push  (r14)
         r9 = qword [var_178h]
         push  (r13)
         rdx = rax
         push  (rbx)
         push  (r15)

    loc_0x0000539d: // orphan
         // CODE XREF from fcn.00004f80 @ 0x541a
         r8 = qword [var_170h]
         rcx = qword [var_168h]
         rdi = r12
         eax = 0
         esi = 2
         sym.imp.__fprintf_chk  ()
         rsp += 0x20
         goto loc_0x529e          // case.default.0x5143 // case.default.0x5143(0x0, 0x2, 0x0, 0x0)

    loc_0x000053c3: // orphan
         // CODE XREF from fcn.00004f80 @ 0x5143
         rcx = qword [var_140h]
         r8 = qword [var_138h]
         edi = 0
         edx = 5
         r13 = qword [var_118h]
         rbx = qword [var_120h]
         rsi = rip + str.Written_by__s___s___s__n_s___s__and__s._n // 0x6878 // "Written by %s, %s, %s,\n%s, %s, and %s.\n"
         r15 = qword [var_128h]
         r14 = qword [var_130h]
         qword [var_168h] = rcx
         qword [var_170h] = r8
         sym.imp.dcgettext  ()
         r9 = r14
         push  (rcx)
         rdx = rax
         push  (r13)
         push  (rbx)
         push  (r15)
         goto loc_0x539d

    loc_0x0000541c: // orphan
         // CODE XREF from fcn.00004f80 @ 0x5143
         rcx = qword [var_140h]
         rbx = qword [var_120h]
         edi = 0
         edx = 5
         r15 = qword [var_128h]
         rsi = rip + str.Written_by__s___s___s__n_s__and__s._n // 0x6850 // "Written by %s, %s, %s,\n%s, and %s.\n"
         r14 = qword [var_130h]
         qword [var_168h] = rcx
         r13 = qword [var_138h]
         sym.imp.dcgettext  ()
         push  (rbx)
         rcx = qword [var_168h]
         r9 = r14
         push  (r15)
         rdx = rax
         r8 = r13

    loc_0x0000546c: // orphan
         // CODE XREF from fcn.00004f80 @ 0x54c1
         esi = 2
         rdi = r12
         eax = 0
         sym.imp.__fprintf_chk  ()
         rsi = pop  ()            // rsp
         rdi = pop  ()
         goto loc_0x529e          // case.default.0x5143 // case.default.0x5143(0x0, 0x547b, 0x0, 0x0)

    loc_0x00005482: // orphan
         // CODE XREF from fcn.00004f80 @ 0x5143
         r15 = qword [var_128h]
         r14 = qword [var_130h]
         edi = 0
         edx = 5
         r13 = qword [var_138h]
         rbx = qword [var_140h]
         rsi = rip + str.Written_by__s___s___s__nand__s._n // 0x6830 // "Written by %s, %s, %s,\nand %s.\n"
         sym.imp.dcgettext  ()
         r9 = r14
         push  (r8)
         rdx = rax
         r8 = r13
         rcx = rbx
         push  (r15)
         goto loc_0x546c

    loc_0x000054c3: // orphan
         // CODE XREF from fcn.00004f80 @ 0x5143
         r14 = qword [var_130h]
         r13 = qword [var_138h]
         edi = 0
         edx = 5
         rbx = qword [var_140h]
         rsi = rip + str.Written_by__s___s__and__s._n // 0x6608 // "Written by %s, %s, and %s.\n"
         sym.imp.dcgettext  ()
         r9 = r14
         r8 = r13
         esi = 2
         rdx = rax
         rcx = rbx
         rdi = r12
         eax = 0
         sym.imp.__fprintf_chk  ()
         goto loc_0x529e          // case.default.0x5143 // case.default.0x5143(0x0, 0x2, 0x0, 0x0)

    loc_0x0000550b: // orphan
         // CODE XREF from fcn.00004f80 @ 0x5143
         r13 = qword [var_138h]
         rbx = qword [var_140h]
         edi = 0
         edx = 5
         rsi = rip + str.Written_by__s_and__s._n // 0x65f1 // "Written by %s and %s.\n"
         sym.imp.dcgettext  ()
         r8 = r13
         rcx = rbx
         esi = 2
         rdx = rax
         rdi = r12
         eax = 0
         sym.imp.__fprintf_chk  ()
         goto loc_0x529e          // case.default.0x5143 // case.default.0x5143(0x0, 0x2, 0x0, 0x0)

    loc_0x00005549: // orphan
         // CODE XREF from fcn.00004f80 @ 0x5143
         rbx = qword [var_140h]
         edi = 0
         edx = 5
         rsi = rip + str.Written_by__s._n // 0x65e1 // "Written by %s.\n"
         sym.imp.dcgettext  ()
         esi = 2
         rdi = r12
         rdx = rax
         rcx = rbx
         eax = 0
         sym.imp.__fprintf_chk  ()
         goto loc_0x529e          // case.default.0x5143 // case.default.0x5143(0x0, 0x2, 0x0, 0x0)

    loc_0x0000557d: // orphan
         // CODE XREF from fcn.00004f80 @ 0x5143
         r11 = qword [var_100h]
         r10 = qword [var_108h]
         edx = 5
         rsi = rip + str.Written_by__s___s___s__n_s___s___s___s__n_s__and__s._n // 0x6900 // "Written by %s, %s, %s,\n%s, %s, %s, %s,\n%s, and %s.\n"
         r9 = qword [var_130h]
         r8 = qword [var_138h]
         rcx = qword [var_140h]
         qword [var_188h] = r11
         qword [var_180h] = r10
         r14 = qword [var_110h]
         qword [var_178h] = r9
         r13 = qword [var_118h]
         qword [var_170h] = r8
         rbx = qword [var_120h]
         qword [var_168h] = rcx
         r15 = qword [var_128h]
         goto loc_0x5253

    loc_0x000055f0: // orphan
         // CODE XREF from fcn.00004f80 @ 0x52ae
         sym.imp.__stack_chk_fail  ()
         
         no

}
