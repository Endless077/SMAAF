            ; CALL XREF from fcn.00003610 @ 0x2bc1
┌ 1661: fcn.00004f80 (int64_t arg1, int64_t arg4, int64_t arg5, int64_t arg6, int64_t arg7, int64_t arg8, int64_t arg9, int64_t arg10, int64_t arg11, int64_t arg_10h);
│           ; var int64_t var_188h @ rbp-0x188
│           ; var int64_t var_180h @ rbp-0x180
│           ; var int64_t var_178h @ rbp-0x178
│           ; var int64_t var_170h @ rbp-0x170
│           ; var int64_t var_168h @ rbp-0x168
│           ; var int64_t var_160h @ rbp-0x160
│           ; var int64_t var_15ch @ rbp-0x15c
│           ; var int64_t var_158h @ rbp-0x158
│           ; var int64_t var_150h @ rbp-0x150
│           ; var char *var_140h @ rbp-0x140
│           ; var char *var_138h @ rbp-0x138
│           ; var char *var_130h @ rbp-0x130
│           ; var char *var_128h @ rbp-0x128
│           ; var char *var_120h @ rbp-0x120
│           ; var int64_t var_118h @ rbp-0x118
│           ; var int64_t var_110h @ rbp-0x110
│           ; var int64_t var_108h @ rbp-0x108
│           ; var int64_t var_100h @ rbp-0x100
│           ; var int64_t var_e8h @ rbp-0xe8
│           ; var int64_t var_e0h @ rbp-0xe0
│           ; var int64_t var_c0h @ rbp-0xc0
│           ; var int64_t var_b8h @ rbp-0xb8
│           ; var int64_t var_b0h @ rbp-0xb0
│           ; var int64_t var_a0h @ rbp-0xa0
│           ; var int64_t var_90h @ rbp-0x90
│           ; var int64_t var_80h @ rbp-0x80
│           ; var int64_t var_70h @ rbp-0x70
│           ; var int64_t var_60h @ rbp-0x60
│           ; var int64_t var_50h @ rbp-0x50
│           ; var int64_t var_40h @ rbp-0x40
│           ; var int64_t var_28h @ rbp-0x28
│           ; arg int64_t arg_10h @ rbp+0x10
│           ; arg int64_t arg1 @ rdi
│           ; arg int64_t arg4 @ rcx
│           ; arg int64_t arg5 @ r8
│           ; arg int64_t arg6 @ r9
│           ; arg int64_t arg7 @ xmm0
│           ; arg int64_t arg8 @ xmm1
│           ; arg int64_t arg9 @ xmm2
│           ; arg int64_t arg10 @ xmm3
│           ; arg int64_t arg11 @ xmm4
│           0x00004f80      55             push rbp
│           0x00004f81      4989ca         mov r10, rcx                ; arg4
│           0x00004f84      4889e5         mov rbp, rsp
│           0x00004f87      4157           push r15
│           0x00004f89      4156           push r14
│           0x00004f8b      4155           push r13
│           0x00004f8d      4154           push r12
│           0x00004f8f      4989fc         mov r12, rdi                ; arg1
│           0x00004f92      53             push rbx
│           0x00004f93      4881ec680100.  sub rsp, 0x168
│           0x00004f9a      4c898540ffff.  mov qword [var_c0h], r8     ; arg5
│           0x00004fa1      4c898d48ffff.  mov qword [var_b8h], r9     ; arg6
│           0x00004fa8      84c0           test al, al
│       ┌─< 0x00004faa      7429           je 0x4fd5
│       │   0x00004fac      0f298550ffff.  movaps xmmword [var_b0h], xmm0 ; arg7
│       │   0x00004fb3      0f298d60ffff.  movaps xmmword [var_a0h], xmm1 ; arg8
│       │   0x00004fba      0f299570ffff.  movaps xmmword [var_90h], xmm2 ; arg9
│       │   0x00004fc1      0f295d80       movaps xmmword [var_80h], xmm3 ; arg10
│       │   0x00004fc5      0f296590       movaps xmmword [var_70h], xmm4 ; arg11
│       │   0x00004fc9      0f296da0       movaps xmmword [var_60h], xmm5
│       │   0x00004fcd      0f2975b0       movaps xmmword [var_50h], xmm6
│       │   0x00004fd1      0f297dc0       movaps xmmword [var_40h], xmm7
│       │   ; CODE XREF from fcn.00004f80 @ 0x4faa
│       └─> 0x00004fd5      64488b042528.  mov rax, qword fs:[0x28]
│           0x00004fde      48898518ffff.  mov qword [var_e8h], rax
│           0x00004fe5      31c0           xor eax, eax
│           0x00004fe7      4c8d8d20ffff.  lea r9, [var_e0h]
│           0x00004fee      488d4510       lea rax, [arg_10h]
│           0x00004ff2      31ff           xor edi, edi
│           0x00004ff4      488985a8feff.  mov qword [var_158h], rax
│           0x00004ffb      488d4d10       lea rcx, [arg_10h]
│           0x00004fff      4531c0         xor r8d, r8d
│           0x00005002      31db           xor ebx, ebx
│           0x00005004      c785a0feffff.  mov dword [var_160h], 0x20  ; "@"
│           0x0000500e      ba20000000     mov edx, 0x20               ; "@"
│           0x00005013      488db5c0feff.  lea rsi, [var_140h]
│           0x0000501a      c785a4feffff.  mov dword [var_15ch], 0x30  ; '0'
│           0x00005024      4c898db0feff.  mov qword [var_150h], r9
│       ┌─< 0x0000502b      eb2b           jmp 0x5058
..
│       │   ; CODE XREF from fcn.00004f80 @ 0x505b
│      ┌──> 0x00005030      89d0           mov eax, edx
│      ╎│   0x00005032      41b801000000   mov r8d, 1
│      ╎│   0x00005038      83c208         add edx, 8
│      ╎│   0x0000503b      4c01c8         add rax, r9
│      ╎│   0x0000503e      488b00         mov rax, qword [rax]
│      ╎│   0x00005041      488904de       mov qword [rsi + rbx*8], rax
│      ╎│   0x00005045      4885c0         test rax, rax
│     ┌───< 0x00005048      742b           je 0x5075
│     │╎│   ; CODE XREF from fcn.00004f80 @ 0x5073
│    ┌────> 0x0000504a      4883c301       add rbx, 1
│    ╎│╎│   0x0000504e      4883fb0a       cmp rbx, 0xa
│   ┌─────< 0x00005052      0f84ee000000   je 0x5146
│   │╎│╎│   ; CODE XREF from fcn.00004f80 @ 0x502b
│   │╎│╎└─> 0x00005058      83fa2f         cmp edx, 0x2f
│   │╎│└──< 0x0000505b      76d3           jbe 0x5030
│   │╎│     0x0000505d      4889c8         mov rax, rcx
│   │╎│     0x00005060      bf01000000     mov edi, 1
│   │╎│     0x00005065      4883c108       add rcx, 8
│   │╎│     0x00005069      488b00         mov rax, qword [rax]
│   │╎│     0x0000506c      488904de       mov qword [rsi + rbx*8], rax
│   │╎│     0x00005070      4885c0         test rax, rax
│   │└────< 0x00005073      75d5           jne 0x504a
│   │ │     ; CODE XREF from fcn.00004f80 @ 0x5048
│   │ └───> 0x00005075      4084ff         test dil, dil
│   │   ┌─< 0x00005078      7407           je 0x5081
│   │   │   0x0000507a      48898da8feff.  mov qword [var_158h], rcx
│   │   │   ; CODE XREF from fcn.00004f80 @ 0x5078
│   │   └─> 0x00005081      4584c0         test r8b, r8b
│   │   ┌─< 0x00005084      7406           je 0x508c
│   │   │   0x00005086      8995a0feffff   mov dword [var_160h], edx
│   │   │   ; CODE XREF from fcn.00004f80 @ 0x5084
│   │   └─> 0x0000508c      4d89d1         mov r9, r10
│   │       0x0000508f      4c8d05281500.  lea r8, str.GNU_coreutils   ; 0x65be ; "GNU coreutils"
│   │       0x00005096      4c89e7         mov rdi, r12
│   │       0x00005099      31c0           xor eax, eax
│   │       0x0000509b      488d0d2a1500.  lea rcx, str.echo           ; 0x65cc ; "echo"
│   │       0x000050a2      488d15281500.  lea rdx, str._s___s___s_n   ; 0x65d1 ; "%s (%s) %s\n"
│   │       0x000050a9      be02000000     mov esi, 2
│   │       0x000050ae      e8cdd3ffff     call sym.imp.__fprintf_chk
│   │       0x000050b3      31ff           xor edi, edi
│   │       0x000050b5      ba05000000     mov edx, 5
│   │       0x000050ba      488d351c1500.  lea rsi, [0x000065dd]       ; "(C)"
│   │       0x000050c1      e84ad2ffff     call sym.imp.dcgettext
│   │       0x000050c6      41b8e7070000   mov r8d, 0x7e7
│   │       0x000050cc      be02000000     mov esi, 2
│   │       0x000050d1      4c89e7         mov rdi, r12
│   │       0x000050d4      4889c1         mov rcx, rax
│   │       0x000050d7      488d15621400.  lea rdx, str.Copyright__s__d_Free_Software_Foundation__Inc. ; 0x6540 ; "Copyright %s %d Free Software Foundation, Inc."
│   │       0x000050de      31c0           xor eax, eax
│   │       0x000050e0      e89bd3ffff     call sym.imp.__fprintf_chk
│   │       0x000050e5      4c89e6         mov rsi, r12
│   │       0x000050e8      bf0a000000     mov edi, 0xa
│   │       0x000050ed      e8ced2ffff     call sym.imp.fputc_unlocked
│   │       0x000050f2      31ff           xor edi, edi
│   │       0x000050f4      ba05000000     mov edx, 5
│   │       0x000050f9      488d35181600.  lea rsi, str.License_GPLv3:_GNU_GPL_version_3_or_later___s_._nThis_is_free_software:_you_are_free_to_change_and_redistribute_it._nThere_is_NO_WARRANTY__to_the_extent_permitted_by_law._n ; 0x6718 ; "License GPLv3+: GNU GPL version 3 or later <%s>.\nThis is free software: you are free to change and redistribute it.\nThere is NO WARRANTY, to the extent permitted by law.\n"
│   │       0x00005100      e80bd2ffff     call sym.imp.dcgettext
│   │       0x00005105      be02000000     mov esi, 2
│   │       0x0000510a      4c89e7         mov rdi, r12
│   │       0x0000510d      488d0db41600.  lea rcx, str.https:__gnu.org_licenses_gpl.html ; 0x67c8 ; "https://gnu.org/licenses/gpl.html"
│   │       0x00005114      4889c2         mov rdx, rax
│   │       0x00005117      31c0           xor eax, eax
│   │       0x00005119      e862d3ffff     call sym.imp.__fprintf_chk
│   │       0x0000511e      4c89e6         mov rsi, r12
│   │       0x00005121      bf0a000000     mov edi, 0xa
│   │       0x00005126      e895d2ffff     call sym.imp.fputc_unlocked
│   │       0x0000512b      4883fb09       cmp rbx, 9
│   │   ┌─< 0x0000512f      0f8769010000   ja case.0x5143.0
│   │   │   0x00005135      488d15a81200.  lea rdx, [0x000063e4]
│   │   │   0x0000513c      4863049a       movsxd rax, dword [rdx + rbx*4]
│   │   │   0x00005140      4801d0         add rax, rdx
│   │   │   ;-- switch
│   │   │   0x00005143      3effe0         jmp rax                     ; switch table (10 cases) at 0x63e4
│   │   │   ; CODE XREF from fcn.00004f80 @ 0x5052
│   └─────> 0x00005146      4d89d1         mov r9, r10
│       │   0x00005149      4c8d056e1400.  lea r8, str.GNU_coreutils   ; 0x65be ; "GNU coreutils"
│       │   0x00005150      4c89e7         mov rdi, r12
│       │   0x00005153      31c0           xor eax, eax
│       │   0x00005155      488d0d701400.  lea rcx, str.echo           ; 0x65cc ; "echo"
│       │   0x0000515c      488d156e1400.  lea rdx, str._s___s___s_n   ; 0x65d1 ; "%s (%s) %s\n"
│       │   0x00005163      be02000000     mov esi, 2
│       │   0x00005168      e813d3ffff     call sym.imp.__fprintf_chk
│       │   0x0000516d      ba05000000     mov edx, 5
│       │   0x00005172      488d35641400.  lea rsi, [0x000065dd]       ; "(C)"
│       │   0x00005179      31ff           xor edi, edi
│       │   0x0000517b      e890d1ffff     call sym.imp.dcgettext
│       │   0x00005180      41b8e7070000   mov r8d, 0x7e7
│       │   0x00005186      be02000000     mov esi, 2
│       │   0x0000518b      4c89e7         mov rdi, r12
│       │   0x0000518e      4889c1         mov rcx, rax
│       │   0x00005191      488d15a81300.  lea rdx, str.Copyright__s__d_Free_Software_Foundation__Inc. ; 0x6540 ; "Copyright %s %d Free Software Foundation, Inc."
│       │   0x00005198      31c0           xor eax, eax
│       │   0x0000519a      e8e1d2ffff     call sym.imp.__fprintf_chk
│       │   0x0000519f      4c89e6         mov rsi, r12
│       │   0x000051a2      bf0a000000     mov edi, 0xa
│       │   0x000051a7      e814d2ffff     call sym.imp.fputc_unlocked
│       │   0x000051ac      ba05000000     mov edx, 5
│       │   0x000051b1      488d35601500.  lea rsi, str.License_GPLv3:_GNU_GPL_version_3_or_later___s_._nThis_is_free_software:_you_are_free_to_change_and_redistribute_it._nThere_is_NO_WARRANTY__to_the_extent_permitted_by_law._n ; 0x6718 ; "License GPLv3+: GNU GPL version 3 or later <%s>.\nThis is free software: you are free to change and redistribute it.\nThere is NO WARRANTY, to the extent permitted by law.\n"
│       │   0x000051b8      31ff           xor edi, edi
│       │   0x000051ba      e851d1ffff     call sym.imp.dcgettext
│       │   0x000051bf      488d0d021600.  lea rcx, str.https:__gnu.org_licenses_gpl.html ; 0x67c8 ; "https://gnu.org/licenses/gpl.html"
│       │   0x000051c6      be02000000     mov esi, 2
│       │   0x000051cb      4c89e7         mov rdi, r12
│       │   0x000051ce      4889c2         mov rdx, rax
│       │   0x000051d1      31c0           xor eax, eax
│       │   0x000051d3      e8a8d2ffff     call sym.imp.__fprintf_chk
│       │   0x000051d8      4c89e6         mov rsi, r12
│       │   0x000051db      bf0a000000     mov edi, 0xa
│       │   0x000051e0      e8dbd1ffff     call sym.imp.fputc_unlocked
│       │   0x000051e5      4c8b9d00ffff.  mov r11, qword [var_100h]
│       │   0x000051ec      4c8b95f8feff.  mov r10, qword [var_108h]
│       │   0x000051f3      ba05000000     mov edx, 5
│       │   0x000051f8      4c8b8dd0feff.  mov r9, qword [var_130h]
│       │   0x000051ff      4c8b85c8feff.  mov r8, qword [var_138h]
│       │   0x00005206      488d35e31500.  lea rsi, str.Written_by__s___s___s__n_s___s___s___s__n_s___s__and_others._n ; 0x67f0 ; "Written by %s, %s, %s,\n%s, %s, %s, %s,\n%s, %s, and others.\n"
│       │   0x0000520d      488b8dc0feff.  mov rcx, qword [var_140h]
│       │   0x00005214      4c899d78feff.  mov qword [var_188h], r11
│       │   0x0000521b      4c899580feff.  mov qword [var_180h], r10
│       │   0x00005222      4c8bb5f0feff.  mov r14, qword [var_110h]
│       │   0x00005229      4c898d88feff.  mov qword [var_178h], r9
│       │   0x00005230      4c8bade8feff.  mov r13, qword [var_118h]
│       │   0x00005237      4c898590feff.  mov qword [var_170h], r8
│       │   0x0000523e      488b9de0feff.  mov rbx, qword [var_120h]
│       │   0x00005245      48898d98feff.  mov qword [var_168h], rcx
│       │   0x0000524c      4c8bbdd8feff.  mov r15, qword [var_128h]
│       │   ; CODE XREF from fcn.00004f80 @ 0x55eb
│      ┌──> 0x00005253      31ff           xor edi, edi
│      ╎│   0x00005255      e8b6d0ffff     call sym.imp.dcgettext
│      ╎│   0x0000525a      4c8b9d78feff.  mov r11, qword [var_188h]
│      ╎│   0x00005261      4889c2         mov rdx, rax
│      ╎│   0x00005264      4153           push r11
│      ╎│   ; CODE XREF from fcn.00004f80 @ 0x532e
│     ┌───> 0x00005266      4c8b9580feff.  mov r10, qword [var_180h]
│     ╎╎│   0x0000526d      4c8b8d88feff.  mov r9, qword [var_178h]
│     ╎╎│   0x00005274      4c89e7         mov rdi, r12
│     ╎╎│   0x00005277      31c0           xor eax, eax
│     ╎╎│   0x00005279      4c8b8590feff.  mov r8, qword [var_170h]
│     ╎╎│   0x00005280      488b8d98feff.  mov rcx, qword [var_168h]
│     ╎╎│   0x00005287      be02000000     mov esi, 2
│     ╎╎│   0x0000528c      4152           push r10
│     ╎╎│   0x0000528e      4156           push r14
│     ╎╎│   0x00005290      4155           push r13
│     ╎╎│   0x00005292      53             push rbx
│     ╎╎│   0x00005293      4157           push r15
│     ╎╎│   0x00005295      e8e6d1ffff     call sym.imp.__fprintf_chk
│     ╎╎│   0x0000529a      4883c430       add rsp, 0x30
│     ╎╎│   ;-- default:                                               ; from 0x5143
│     ╎╎│   ; XREFS: CODE 0x0000512f  CODE 0x00005143  CODE 0x000053be  
│     ╎╎│   ; XREFS: CODE 0x0000547d  CODE 0x00005506  CODE 0x00005544  
│     ╎╎│   ; XREFS: CODE 0x00005578  
│ ┌┌┌┌──└─> 0x0000529e      488b8518ffff.  mov rax, qword [var_e8h]
│ ╎╎╎╎╎╎    0x000052a5      64482b042528.  sub rax, qword fs:[0x28]
│ ╎╎╎╎╎╎┌─< 0x000052ae      0f853c030000   jne 0x55f0
│ ╎╎╎╎╎╎│   0x000052b4      488d65d8       lea rsp, [var_28h]
│ ╎╎╎╎╎╎│   0x000052b8      5b             pop rbx
│ ╎╎╎╎╎╎│   0x000052b9      415c           pop r12
│ ╎╎╎╎╎╎│   0x000052bb      415d           pop r13
│ ╎╎╎╎╎╎│   0x000052bd      415e           pop r14
│ ╎╎╎╎╎╎│   0x000052bf      415f           pop r15
│ ╎╎╎╎╎╎│   0x000052c1      5d             pop rbp
│ ╎╎╎╎╎╎│   0x000052c2      c3             ret
│ ╎╎╎╎╎╎│   ;-- case 8:                                                ; from 0x00005143
│ ╎╎╎╎╎╎│   ; CODE XREF from fcn.00004f80 @ 0x5143
│ ╎╎╎╎╎╎│   0x000052c3      4c8b95f8feff.  mov r10, qword [var_108h]
│ ╎╎╎╎╎╎│   0x000052ca      4c8b8dd0feff.  mov r9, qword [var_130h]
│ ╎╎╎╎╎╎│   0x000052d1      31ff           xor edi, edi
│ ╎╎╎╎╎╎│   0x000052d3      ba05000000     mov edx, 5
│ ╎╎╎╎╎╎│   0x000052d8      4c8b85c8feff.  mov r8, qword [var_138h]
│ ╎╎╎╎╎╎│   0x000052df      488b8dc0feff.  mov rcx, qword [var_140h]
│ ╎╎╎╎╎╎│   0x000052e6      488d35e31500.  lea rsi, str.Written_by__s___s___s__n_s___s___s___s__nand__s._n ; 0x68d0 ; "Written by %s, %s, %s,\n%s, %s, %s, %s,\nand %s.\n"
│ ╎╎╎╎╎╎│   0x000052ed      4c899580feff.  mov qword [var_180h], r10
│ ╎╎╎╎╎╎│   0x000052f4      4c8bb5f0feff.  mov r14, qword [var_110h]
│ ╎╎╎╎╎╎│   0x000052fb      4c898d88feff.  mov qword [var_178h], r9
│ ╎╎╎╎╎╎│   0x00005302      4c8bade8feff.  mov r13, qword [var_118h]
│ ╎╎╎╎╎╎│   0x00005309      4c898590feff.  mov qword [var_170h], r8
│ ╎╎╎╎╎╎│   0x00005310      488b9de0feff.  mov rbx, qword [var_120h]
│ ╎╎╎╎╎╎│   0x00005317      48898d98feff.  mov qword [var_168h], rcx
│ ╎╎╎╎╎╎│   0x0000531e      4c8bbdd8feff.  mov r15, qword [var_128h]
│ ╎╎╎╎╎╎│   0x00005325      e8e6cfffff     call sym.imp.dcgettext
│ ╎╎╎╎╎╎│   0x0000532a      4889c2         mov rdx, rax
│ ╎╎╎╎╎╎│   0x0000532d      50             push rax
│ ╎╎╎╎└───< 0x0000532e      e933ffffff     jmp 0x5266
│ ╎╎╎╎ ╎│   ;-- case 7:                                                ; from 0x00005143
│ ╎╎╎╎ ╎│   ; CODE XREF from fcn.00004f80 @ 0x5143
│ ╎╎╎╎ ╎│   0x00005333      4c8b8dd0feff.  mov r9, qword [var_130h]
│ ╎╎╎╎ ╎│   0x0000533a      4c8bb5f0feff.  mov r14, qword [var_110h]
│ ╎╎╎╎ ╎│   0x00005341      31ff           xor edi, edi
│ ╎╎╎╎ ╎│   0x00005343      ba05000000     mov edx, 5
│ ╎╎╎╎ ╎│   0x00005348      4c8bade8feff.  mov r13, qword [var_118h]
│ ╎╎╎╎ ╎│   0x0000534f      488b9de0feff.  mov rbx, qword [var_120h]
│ ╎╎╎╎ ╎│   0x00005356      488d35431500.  lea rsi, str.Written_by__s___s___s__n_s___s___s__and__s._n ; 0x68a0 ; "Written by %s, %s, %s,\n%s, %s, %s, and %s.\n"
│ ╎╎╎╎ ╎│   0x0000535d      4c8bbdd8feff.  mov r15, qword [var_128h]
│ ╎╎╎╎ ╎│   0x00005364      4c8b85c8feff.  mov r8, qword [var_138h]
│ ╎╎╎╎ ╎│   0x0000536b      4c898d88feff.  mov qword [var_178h], r9
│ ╎╎╎╎ ╎│   0x00005372      488b8dc0feff.  mov rcx, qword [var_140h]
│ ╎╎╎╎ ╎│   0x00005379      4c898590feff.  mov qword [var_170h], r8
│ ╎╎╎╎ ╎│   0x00005380      48898d98feff.  mov qword [var_168h], rcx
│ ╎╎╎╎ ╎│   0x00005387      e884cfffff     call sym.imp.dcgettext
│ ╎╎╎╎ ╎│   0x0000538c      4156           push r14
│ ╎╎╎╎ ╎│   0x0000538e      4c8b8d88feff.  mov r9, qword [var_178h]
│ ╎╎╎╎ ╎│   0x00005395      4155           push r13
│ ╎╎╎╎ ╎│   0x00005397      4889c2         mov rdx, rax
│ ╎╎╎╎ ╎│   0x0000539a      53             push rbx
│ ╎╎╎╎ ╎│   0x0000539b      4157           push r15
│ ╎╎╎╎ ╎│   ; CODE XREF from fcn.00004f80 @ 0x541a
│ ╎╎╎╎┌───> 0x0000539d      4c8b8590feff.  mov r8, qword [var_170h]
│ ╎╎╎╎╎╎│   0x000053a4      488b8d98feff.  mov rcx, qword [var_168h]
│ ╎╎╎╎╎╎│   0x000053ab      4c89e7         mov rdi, r12
│ ╎╎╎╎╎╎│   0x000053ae      31c0           xor eax, eax
│ ╎╎╎╎╎╎│   0x000053b0      be02000000     mov esi, 2
│ ╎╎╎╎╎╎│   0x000053b5      e8c6d0ffff     call sym.imp.__fprintf_chk
│ ╎╎╎╎╎╎│   0x000053ba      4883c420       add rsp, 0x20
│ ────────< 0x000053be      e9dbfeffff     jmp case.0x5143.0
│ ╎╎╎╎╎╎│   ;-- case 6:                                                ; from 0x00005143
│ ╎╎╎╎╎╎│   ; CODE XREF from fcn.00004f80 @ 0x5143
│ ╎╎╎╎╎╎│   0x000053c3      488b8dc0feff.  mov rcx, qword [var_140h]
│ ╎╎╎╎╎╎│   0x000053ca      4c8b85c8feff.  mov r8, qword [var_138h]
│ ╎╎╎╎╎╎│   0x000053d1      31ff           xor edi, edi
│ ╎╎╎╎╎╎│   0x000053d3      ba05000000     mov edx, 5
│ ╎╎╎╎╎╎│   0x000053d8      4c8bade8feff.  mov r13, qword [var_118h]
│ ╎╎╎╎╎╎│   0x000053df      488b9de0feff.  mov rbx, qword [var_120h]
│ ╎╎╎╎╎╎│   0x000053e6      488d358b1400.  lea rsi, str.Written_by__s___s___s__n_s___s__and__s._n ; 0x6878 ; "Written by %s, %s, %s,\n%s, %s, and %s.\n"
│ ╎╎╎╎╎╎│   0x000053ed      4c8bbdd8feff.  mov r15, qword [var_128h]
│ ╎╎╎╎╎╎│   0x000053f4      4c8bb5d0feff.  mov r14, qword [var_130h]
│ ╎╎╎╎╎╎│   0x000053fb      48898d98feff.  mov qword [var_168h], rcx
│ ╎╎╎╎╎╎│   0x00005402      4c898590feff.  mov qword [var_170h], r8
│ ╎╎╎╎╎╎│   0x00005409      e802cfffff     call sym.imp.dcgettext
│ ╎╎╎╎╎╎│   0x0000540e      4d89f1         mov r9, r14
│ ╎╎╎╎╎╎│   0x00005411      51             push rcx
│ ╎╎╎╎╎╎│   0x00005412      4889c2         mov rdx, rax
│ ╎╎╎╎╎╎│   0x00005415      4155           push r13
│ ╎╎╎╎╎╎│   0x00005417      53             push rbx
│ ╎╎╎╎╎╎│   0x00005418      4157           push r15
│ ╎╎╎╎└───< 0x0000541a      eb81           jmp 0x539d
│ ╎╎╎╎ ╎│   ;-- case 5:                                                ; from 0x00005143
│ ╎╎╎╎ ╎│   ; CODE XREF from fcn.00004f80 @ 0x5143
│ ╎╎╎╎ ╎│   0x0000541c      488b8dc0feff.  mov rcx, qword [var_140h]
│ ╎╎╎╎ ╎│   0x00005423      488b9de0feff.  mov rbx, qword [var_120h]
│ ╎╎╎╎ ╎│   0x0000542a      31ff           xor edi, edi
│ ╎╎╎╎ ╎│   0x0000542c      ba05000000     mov edx, 5
│ ╎╎╎╎ ╎│   0x00005431      4c8bbdd8feff.  mov r15, qword [var_128h]
│ ╎╎╎╎ ╎│   0x00005438      488d35111400.  lea rsi, str.Written_by__s___s___s__n_s__and__s._n ; 0x6850 ; "Written by %s, %s, %s,\n%s, and %s.\n"
│ ╎╎╎╎ ╎│   0x0000543f      4c8bb5d0feff.  mov r14, qword [var_130h]
│ ╎╎╎╎ ╎│   0x00005446      48898d98feff.  mov qword [var_168h], rcx
│ ╎╎╎╎ ╎│   0x0000544d      4c8badc8feff.  mov r13, qword [var_138h]
│ ╎╎╎╎ ╎│   0x00005454      e8b7ceffff     call sym.imp.dcgettext
│ ╎╎╎╎ ╎│   0x00005459      53             push rbx
│ ╎╎╎╎ ╎│   0x0000545a      488b8d98feff.  mov rcx, qword [var_168h]
│ ╎╎╎╎ ╎│   0x00005461      4d89f1         mov r9, r14
│ ╎╎╎╎ ╎│   0x00005464      4157           push r15
│ ╎╎╎╎ ╎│   0x00005466      4889c2         mov rdx, rax
│ ╎╎╎╎ ╎│   0x00005469      4d89e8         mov r8, r13
│ ╎╎╎╎ ╎│   ; CODE XREF from fcn.00004f80 @ 0x54c1
│ ╎╎╎╎┌───> 0x0000546c      be02000000     mov esi, 2
│ ╎╎╎╎╎╎│   0x00005471      4c89e7         mov rdi, r12
│ ╎╎╎╎╎╎│   0x00005474      31c0           xor eax, eax
│ ╎╎╎╎╎╎│   0x00005476      e805d0ffff     call sym.imp.__fprintf_chk
│ ╎╎╎╎╎╎│   0x0000547b      5e             pop rsi
│ ╎╎╎╎╎╎│   0x0000547c      5f             pop rdi
│ └───────< 0x0000547d      e91cfeffff     jmp case.0x5143.0
│  ╎╎╎╎╎│   ;-- case 4:                                                ; from 0x00005143
│  ╎╎╎╎╎│   ; CODE XREF from fcn.00004f80 @ 0x5143
│  ╎╎╎╎╎│   0x00005482      4c8bbdd8feff.  mov r15, qword [var_128h]
│  ╎╎╎╎╎│   0x00005489      4c8bb5d0feff.  mov r14, qword [var_130h]
│  ╎╎╎╎╎│   0x00005490      31ff           xor edi, edi
│  ╎╎╎╎╎│   0x00005492      ba05000000     mov edx, 5
│  ╎╎╎╎╎│   0x00005497      4c8badc8feff.  mov r13, qword [var_138h]
│  ╎╎╎╎╎│   0x0000549e      488b9dc0feff.  mov rbx, qword [var_140h]
│  ╎╎╎╎╎│   0x000054a5      488d35841300.  lea rsi, str.Written_by__s___s___s__nand__s._n ; 0x6830 ; "Written by %s, %s, %s,\nand %s.\n"
│  ╎╎╎╎╎│   0x000054ac      e85fceffff     call sym.imp.dcgettext
│  ╎╎╎╎╎│   0x000054b1      4d89f1         mov r9, r14
│  ╎╎╎╎╎│   0x000054b4      4150           push r8
│  ╎╎╎╎╎│   0x000054b6      4889c2         mov rdx, rax
│  ╎╎╎╎╎│   0x000054b9      4d89e8         mov r8, r13
│  ╎╎╎╎╎│   0x000054bc      4889d9         mov rcx, rbx
│  ╎╎╎╎╎│   0x000054bf      4157           push r15
│  ╎╎╎└───< 0x000054c1      eba9           jmp 0x546c
│  ╎╎╎ ╎│   ;-- case 3:                                                ; from 0x00005143
│  ╎╎╎ ╎│   ; CODE XREF from fcn.00004f80 @ 0x5143
│  ╎╎╎ ╎│   0x000054c3      4c8bb5d0feff.  mov r14, qword [var_130h]
│  ╎╎╎ ╎│   0x000054ca      4c8badc8feff.  mov r13, qword [var_138h]
│  ╎╎╎ ╎│   0x000054d1      31ff           xor edi, edi
│  ╎╎╎ ╎│   0x000054d3      ba05000000     mov edx, 5
│  ╎╎╎ ╎│   0x000054d8      488b9dc0feff.  mov rbx, qword [var_140h]
│  ╎╎╎ ╎│   0x000054df      488d35221100.  lea rsi, str.Written_by__s___s__and__s._n ; 0x6608 ; "Written by %s, %s, and %s.\n"
│  ╎╎╎ ╎│   0x000054e6      e825ceffff     call sym.imp.dcgettext
│  ╎╎╎ ╎│   0x000054eb      4d89f1         mov r9, r14
│  ╎╎╎ ╎│   0x000054ee      4d89e8         mov r8, r13
│  ╎╎╎ ╎│   0x000054f1      be02000000     mov esi, 2
│  ╎╎╎ ╎│   0x000054f6      4889c2         mov rdx, rax
│  ╎╎╎ ╎│   0x000054f9      4889d9         mov rcx, rbx
│  ╎╎╎ ╎│   0x000054fc      4c89e7         mov rdi, r12
│  ╎╎╎ ╎│   0x000054ff      31c0           xor eax, eax
│  ╎╎╎ ╎│   0x00005501      e87acfffff     call sym.imp.__fprintf_chk
│  └──────< 0x00005506      e993fdffff     jmp case.0x5143.0
│   ╎╎ ╎│   ;-- case 2:                                                ; from 0x00005143
│   ╎╎ ╎│   ; CODE XREF from fcn.00004f80 @ 0x5143
│   ╎╎ ╎│   0x0000550b      4c8badc8feff.  mov r13, qword [var_138h]
│   ╎╎ ╎│   0x00005512      488b9dc0feff.  mov rbx, qword [var_140h]
│   ╎╎ ╎│   0x00005519      31ff           xor edi, edi
│   ╎╎ ╎│   0x0000551b      ba05000000     mov edx, 5
│   ╎╎ ╎│   0x00005520      488d35ca1000.  lea rsi, str.Written_by__s_and__s._n ; 0x65f1 ; "Written by %s and %s.\n"
│   ╎╎ ╎│   0x00005527      e8e4cdffff     call sym.imp.dcgettext
│   ╎╎ ╎│   0x0000552c      4d89e8         mov r8, r13
│   ╎╎ ╎│   0x0000552f      4889d9         mov rcx, rbx
│   ╎╎ ╎│   0x00005532      be02000000     mov esi, 2
│   ╎╎ ╎│   0x00005537      4889c2         mov rdx, rax
│   ╎╎ ╎│   0x0000553a      4c89e7         mov rdi, r12
│   ╎╎ ╎│   0x0000553d      31c0           xor eax, eax
│   ╎╎ ╎│   0x0000553f      e83ccfffff     call sym.imp.__fprintf_chk
│   └─────< 0x00005544      e955fdffff     jmp case.0x5143.0
│    ╎ ╎│   ;-- case 1:                                                ; from 0x00005143
│    ╎ ╎│   ; CODE XREF from fcn.00004f80 @ 0x5143
│    ╎ ╎│   0x00005549      488b9dc0feff.  mov rbx, qword [var_140h]
│    ╎ ╎│   0x00005550      31ff           xor edi, edi
│    ╎ ╎│   0x00005552      ba05000000     mov edx, 5
│    ╎ ╎│   0x00005557      488d35831000.  lea rsi, str.Written_by__s._n ; 0x65e1 ; "Written by %s.\n"
│    ╎ ╎│   0x0000555e      e8adcdffff     call sym.imp.dcgettext
│    ╎ ╎│   0x00005563      be02000000     mov esi, 2
│    ╎ ╎│   0x00005568      4c89e7         mov rdi, r12
│    ╎ ╎│   0x0000556b      4889c2         mov rdx, rax
│    ╎ ╎│   0x0000556e      4889d9         mov rcx, rbx
│    ╎ ╎│   0x00005571      31c0           xor eax, eax
│    ╎ ╎│   0x00005573      e808cfffff     call sym.imp.__fprintf_chk
│    └────< 0x00005578      e921fdffff     jmp case.0x5143.0
│      ╎│   ;-- case 9:                                                ; from 0x00005143
│      ╎│   ; CODE XREF from fcn.00004f80 @ 0x5143
│      ╎│   0x0000557d      4c8b9d00ffff.  mov r11, qword [var_100h]
│      ╎│   0x00005584      4c8b95f8feff.  mov r10, qword [var_108h]
│      ╎│   0x0000558b      ba05000000     mov edx, 5
│      ╎│   0x00005590      488d35691300.  lea rsi, str.Written_by__s___s___s__n_s___s___s___s__n_s__and__s._n ; 0x6900 ; "Written by %s, %s, %s,\n%s, %s, %s, %s,\n%s, and %s.\n"
│      ╎│   0x00005597      4c8b8dd0feff.  mov r9, qword [var_130h]
│      ╎│   0x0000559e      4c8b85c8feff.  mov r8, qword [var_138h]
│      ╎│   0x000055a5      488b8dc0feff.  mov rcx, qword [var_140h]
│      ╎│   0x000055ac      4c899d78feff.  mov qword [var_188h], r11
│      ╎│   0x000055b3      4c899580feff.  mov qword [var_180h], r10
│      ╎│   0x000055ba      4c8bb5f0feff.  mov r14, qword [var_110h]
│      ╎│   0x000055c1      4c898d88feff.  mov qword [var_178h], r9
│      ╎│   0x000055c8      4c8bade8feff.  mov r13, qword [var_118h]
│      ╎│   0x000055cf      4c898590feff.  mov qword [var_170h], r8
│      ╎│   0x000055d6      488b9de0feff.  mov rbx, qword [var_120h]
│      ╎│   0x000055dd      48898d98feff.  mov qword [var_168h], rcx
│      ╎│   0x000055e4      4c8bbdd8feff.  mov r15, qword [var_128h]
│      └──< 0x000055eb      e963fcffff     jmp 0x5253
│       │   ; CODE XREF from fcn.00004f80 @ 0x52ae
│       └─> 0x000055f0      e84bcdffff     call sym.imp.__stack_chk_fail
│           0x000055f5      662e0f1f8400.  nop word cs:[rax + rax]
└           0x000055ff      90             nop
