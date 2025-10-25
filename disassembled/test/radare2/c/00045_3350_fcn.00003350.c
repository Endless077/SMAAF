int fcn.00003350 (int esi, int edx) {
    loc_0x3350:
        // CALL XREFS from fcn.00003610 @ 0x4d91, 0x4dac
        push  (rbp)
        rbp = rsp
        push  (r12)
        r12d = esi    // arg2
        push  (rbx)
        rbx = rdi     // arg1
        edi = 0xe     // nl_item item
        sym.imp.nl_langinfo  ()
        // char *nl_langinfo(?)
        var = rax & rax
        if  (!var) goto loc_0x33cf // likely
            
    loc_0x33cf:
        // XREFS: CODE 0x0000336a  CODE 0x00003374  CODE 0x00003386
        // XREFS: CODE 0x00003391  CODE 0x00003397  CODE 0x0000339d
        // XREFS: CODE 0x000033a3  CODE 0x000033c2  CODE 0x000033f4
        // XREFS: CODE 0x000033fa  CODE 0x00003400  CODE 0x00003406
        // XREFS: CODE 0x0000340c  CODE 0x00003420
        var = r12d - 9
        rax = rip + 0x31aa // "'"
        // 0x6584
        rdx = rip + 0x31a1 // u"\"'\u07a1e\u80e2\x98\u4247\u3831\u33300\u656d\u6f6d\u7972\u6520\u6878\u7561\u7473\u6465\u2500s\u4f50\u4953X`\u7277\u7469\u2065\u7265\u6f72r\u4e47\u2055\u6f63\u6572\u7475\u6c69s\u6365\u6f68\u2500\u2073\u2528\u2973\u2520\u0a73\u2800\u2943\u5700\u6972\u7474\u6e65\u6220\u2079\u7325\u0a2e\u5700\u6972\u7474\u6e65\u6220\u2079\u7325\u6120"
        // 0x6582
        rbx = pop  ()
        if  (!var) rax = rdx
        r12 = pop  ()
        rbp = pop  ()
        re
         // } else {
    loc_0x336c:
        rdi = rax
        eax = byte [rax]
        var = al & al
        if  (!var) goto loc_0x33cf // unlikely
        }
        return eax;
    loc_0x3376:
        eax &= 0xffffffdf // 4294967263
        var = al - 0x55
        if  (var) goto loc_0x33c0 // likely
            
    loc_0x33c0:
        // CODE XREF from fcn.00003350 @ 0x337b
        var = al - 0x47
        if  (var) goto loc_0x33cf // likely
    loc_0x33c4:
        eax = byte [rdi + 1]
        eax &= 0xffffffdf // 4294967263
        var = al - 0x42
        if  (!var) goto loc_0x33f0 // unlikely
            
    loc_0x33f0:
        // CODE XREF from fcn.00003350 @ 0x33cd
        var = byte [rdi + 2] - 0x31
        if  (var) goto loc_0x33cf // likely
    loc_0x33f6:
        var = byte [rdi + 3] - 0x38
        if  (var) goto loc_0x33cf // likely
    loc_0x33fc:
        var = byte [rdi + 4] - 0x30
        if  (var) goto loc_0x33cf // likely
    loc_0x3402:
        var = byte [rdi + 5] - 0x33
        if  (var) goto loc_0x33cf // likely
    loc_0x3408:
        var = byte [rdi + 6] - 0x30
        if  (var) goto loc_0x33cf // likely
    loc_0x340e:
        ecx = 0
        edx = 0
        rsi = rip + 0x3175 // str.GB18030
        // 0x658e // "GB18030"
        fcn.00003190  () // fcn.00003190(0x0, 0x658e)
        var = eax & eax
        if  (!var) goto loc_0x33cf // likely
    loc_0x3422:
        var = byte [rbx] - 0x60
        rax = rip + 0x3153 // 0x657f
        rdx = rip + 0x3153 // 0x6586
        rbx = pop  ()
        if  (!var) rax = rdx
        r12 = pop  ()
        rbp = pop  ()
        re
         // } else {
         // } else {
        }
        return eax;
        goto loc_0x337d
    loc_0x3388:
        eax = byte [rdi + 2]
        eax &= 0xffffffdf // 4294967263
        var = al - 0x46
        if  (var) goto loc_0x33cf // likely
    loc_0x3393:
        var = byte [rdi + 3] - 0x2d
        if  (var) goto loc_0x33cf // likely
    loc_0x3399:
        var = byte [rdi + 4] - 0x38
        if  (var) goto loc_0x33cf // likely
    loc_0x339f:
        var = byte [rdi + 5] - 0
        if  (var) goto loc_0x33cf // likely
    loc_0x33a5:
        var = byte [rbx] - 0x60
        rax = rip + 0x31cc // "\u2019"
        // 0x657b
        rdx = rip + 0x31d4 // "\u2018"
        // 0x658a
        rbx = pop  ()
        if  (!var) rax = rdx
        r12 = pop  ()
        rbp = pop  ()
        re
         // (break)
}
