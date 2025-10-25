            ; CALL XREF from entry.fini0 @ 0x30d7
┌ 34: fcn.00003040 ();
│           0x00003040      488d3dd15f00.  lea rdi, section..bss       ; 0x9018
│           0x00003047      488d05ca5f00.  lea rax, section..bss       ; 0x9018
│           0x0000304e      4839f8         cmp rax, rdi
│       ┌─< 0x00003051      7415           je 0x3068
│       │   0x00003053      488b05665f00.  mov rax, qword [reloc._ITM_deregisterTMCloneTable] ; [0x8fc0:8]=0
│       │   0x0000305a      4885c0         test rax, rax
│      ┌──< 0x0000305d      7409           je 0x3068
│      ││   0x0000305f      ffe0           jmp rax
..
│      ││   ; CODE XREFS from fcn.00003040 @ 0x3051, 0x305d
└      └└─> 0x00003068      c3             ret
