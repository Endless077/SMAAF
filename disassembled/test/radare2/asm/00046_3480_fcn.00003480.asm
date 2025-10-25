        ╎   ; CALL XREF from fcn.000035a0 @ 0x35c2
┌ 262: fcn.00003480 (int64_t arg1);
│       ╎   ; arg int64_t arg1 @ rdi
│       ╎   0x00003480      55             push rbp
│       ╎   0x00003481      4889e5         mov rbp, rsp
│       ╎   0x00003484      4155           push r13
│       ╎   0x00003486      4154           push r12
│       ╎   0x00003488      53             push rbx
│       ╎   0x00003489      4889fb         mov rbx, rdi                ; arg1
│       ╎   0x0000348c      4883ec08       sub rsp, 8
│       ╎   0x00003490      e83befffff     call sym.imp.fileno         ; int fileno(FILE *stream)
│       ╎   0x00003495      4889df         mov rdi, rbx
│       ╎   0x00003498      85c0           test eax, eax
│      ┌──< 0x0000349a      786b           js 0x3507
│      │╎   0x0000349c      e85fefffff     call sym.imp.__freading
│      │╎   0x000034a1      85c0           test eax, eax
│     ┌───< 0x000034a3      7543           jne 0x34e8
│     ││╎   ; CODE XREF from fcn.00003480 @ 0x3502
│    ┌────> 0x000034a5      4889df         mov rdi, rbx
│    ╎││╎   0x000034a8      e853efffff     call sym.imp.__freading
│    ╎││╎   0x000034ad      85c0           test eax, eax
│   ┌─────< 0x000034af      756f           jne 0x3520
│   │╎││╎   ; CODE XREFS from fcn.00003480 @ 0x3526, 0x3541, 0x357b, 0x358b
│ ┌┌──────> 0x000034b1      4889df         mov rdi, rbx                ; FILE *stream
│ ╎╎│╎││╎   0x000034b4      e827efffff     call sym.imp.fflush         ; int fflush(FILE *stream)
│ ╎╎│╎││╎   0x000034b9      85c0           test eax, eax
│ ────────< 0x000034bb      7447           je 0x3504
│ ╎╎│╎││╎   0x000034bd      e8deedffff     call sym.imp.__errno_location
│ ╎╎│╎││╎   0x000034c2      4889df         mov rdi, rbx                ; FILE *stream
│ ╎╎│╎││╎   0x000034c5      448b28         mov r13d, dword [rax]
│ ╎╎│╎││╎   0x000034c8      4989c4         mov r12, rax
│ ╎╎│╎││╎   0x000034cb      e820eeffff     call sym.imp.fclose         ; int fclose(FILE *stream)
│ ╎╎│╎││╎   0x000034d0      4585ed         test r13d, r13d
│ ────────< 0x000034d3      0f85b7000000   jne 0x3590
│ ╎╎│╎││╎   ; CODE XREF from fcn.00003480 @ 0x3599
│ ────────> 0x000034d9      4883c408       add rsp, 8
│ ╎╎│╎││╎   0x000034dd      5b             pop rbx
│ ╎╎│╎││╎   0x000034de      415c           pop r12
│ ╎╎│╎││╎   0x000034e0      415d           pop r13
│ ╎╎│╎││╎   0x000034e2      5d             pop rbp
│ ╎╎│╎││╎   0x000034e3      c3             ret
..
│ ╎╎│╎││╎   ; CODE XREF from fcn.00003480 @ 0x34a3
│ ╎╎│╎└───> 0x000034e8      4889df         mov rdi, rbx                ; FILE *stream
│ ╎╎│╎ │╎   0x000034eb      e8e0eeffff     call sym.imp.fileno         ; int fileno(FILE *stream)
│ ╎╎│╎ │╎   0x000034f0      31f6           xor esi, esi
│ ╎╎│╎ │╎   0x000034f2      ba01000000     mov edx, 1
│ ╎╎│╎ │╎   0x000034f7      89c7           mov edi, eax
│ ╎╎│╎ │╎   0x000034f9      e872eeffff     call sym.imp.lseek
│ ╎╎│╎ │╎   0x000034fe      4883f8ff       cmp rax, 0xffffffffffffffff
│ ╎╎│└────< 0x00003502      75a1           jne 0x34a5
│ ╎╎│  │╎   ; CODE XREF from fcn.00003480 @ 0x34bb
│ ────────> 0x00003504      4889df         mov rdi, rbx
│ ╎╎│  │╎   ; CODE XREF from fcn.00003480 @ 0x349a
│ ╎╎│  └──> 0x00003507      4883c408       add rsp, 8
│ ╎╎│   ╎   0x0000350b      5b             pop rbx
│ ╎╎│   ╎   0x0000350c      415c           pop r12
│ ╎╎│   ╎   0x0000350e      415d           pop r13
│ ╎╎│   ╎   0x00003510      5d             pop rbp
│ ╎╎│   └─< 0x00003511      e9daedffff     jmp sym.imp.fclose
..
│ ╎╎│       ; CODE XREF from fcn.00003480 @ 0x34af
│ ╎╎└─────> 0x00003520      f70300010000   test dword [rbx], 0x100
│ ────────< 0x00003526      7489           je 0x34b1
│ ╎╎        0x00003528      488b4308       mov rax, qword [rbx + 8]
│ ╎╎        0x0000352c      48394310       cmp qword [rbx + 0x10], rax
│ ╎╎    ┌─< 0x00003530      741e           je 0x3550
│ ╎╎    │   ; CODE XREFS from fcn.00003480 @ 0x3558, 0x355f
│ ╎╎  ┌┌──> 0x00003532      ba01000000     mov edx, 1
│ ╎╎  ╎╎│   0x00003537      31f6           xor esi, esi
│ ╎╎  ╎╎│   0x00003539      4889df         mov rdi, rbx
│ ╎╎  ╎╎│   0x0000353c      e8ffeeffff     call sym.imp.fseeko
│ ────────< 0x00003541      e96bffffff     jmp 0x34b1
..
│ ╎╎  ╎╎│   ; CODE XREF from fcn.00003480 @ 0x3530
│ ╎╎  ╎╎└─> 0x00003550      488b4320       mov rax, qword [rbx + 0x20]
│ ╎╎  ╎╎    0x00003554      48394328       cmp qword [rbx + 0x28], rax
│ ╎╎  └───< 0x00003558      75d8           jne 0x3532
│ ╎╎   ╎    0x0000355a      48837b4800     cmp qword [rbx + 0x48], 0
│ ╎╎   └──< 0x0000355f      75d1           jne 0x3532
│ ╎╎        0x00003561      4889df         mov rdi, rbx                ; FILE *stream
│ ╎╎        0x00003564      e867eeffff     call sym.imp.fileno         ; int fileno(FILE *stream)
│ ╎╎        0x00003569      31f6           xor esi, esi
│ ╎╎        0x0000356b      ba01000000     mov edx, 1
│ ╎╎        0x00003570      89c7           mov edi, eax
│ ╎╎        0x00003572      e8f9edffff     call sym.imp.lseek
│ ╎╎        0x00003577      4883f8ff       cmp rax, 0xffffffffffffffff
│ └───────< 0x0000357b      0f8430ffffff   je 0x34b1
│  ╎        0x00003581      8323ef         and dword [rbx], 0xffffffef ; [0xffffffef:4]=-1 ; 4294967279
│  ╎        0x00003584      488983900000.  mov qword [rbx + 0x90], rax
│  └──────< 0x0000358b      e921ffffff     jmp 0x34b1
│           ; CODE XREF from fcn.00003480 @ 0x34d3
│ ────────> 0x00003590      45892c24       mov dword [r12], r13d
│           0x00003594      b8ffffffff     mov eax, 0xffffffff         ; -1
└ ────────< 0x00003599      e93bffffff     jmp 0x34d9
