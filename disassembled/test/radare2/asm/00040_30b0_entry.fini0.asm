┌ 54: entry.fini0 ();
│           0x000030b0      f30f1efa       endbr64
│           0x000030b4      803d5d5f0000.  cmp byte [section..bss], 0  ; [0x9018:1]=0
│       ┌─< 0x000030bb      752b           jne 0x30e8
│       │   0x000030bd      55             push rbp
│       │   0x000030be      48833d2a5f00.  cmp qword [reloc.__cxa_finalize], 0 ; [0x8ff0:8]=0
│       │   0x000030c6      4889e5         mov rbp, rsp
│      ┌──< 0x000030c9      740c           je 0x30d7
│      ││   0x000030cb      488b3d365f00.  mov rdi, qword [0x00009008] ; [0x9008:8]=0x9008
│      ││   0x000030d2      e899f1ffff     call fcn.00002270
│      ││   ; CODE XREF from entry.fini0 @ 0x30c9
│      └──> 0x000030d7      e864ffffff     call fcn.00003040
│       │   0x000030dc      c605355f0000.  mov byte [section..bss], 1  ; [0x9018:1]=0
│       │   0x000030e3      5d             pop rbp
│       │   0x000030e4      c3             ret
..
│       │   ; CODE XREF from entry.fini0 @ 0x30bb
└       └─> 0x000030e8      c3             ret
