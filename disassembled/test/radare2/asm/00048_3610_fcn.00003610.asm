       ╎╎   ; CALL XREF from fcn.00003610 @ 0x46d6
┌ 9228: fcn.00003610 ();
│      ╎╎   ; var uint32_t var_120h @ rbp-0x120
│      ╎╎   ; var uint32_t var_11fh @ rbp-0x11f
│      ╎╎   ; var char *var_e8h @ rbp-0xe8
│      ╎╎   ; var char *var_e0h @ rbp-0xe0
│      ╎╎   ; var char *var_d8h @ rbp-0xd8
│      ╎╎   ; var uint32_t var_d0h_3 @ rbp-0xd0
│      ╎╎   ; var uint32_t var_c8h_2 @ rbp-0xc8
│      ╎╎   ; var char *var_c0h_2 @ rbp-0xc0
│      ╎╎   ; var char *var_bfh @ rbp-0xbf
│      ╎╎   ; var int64_t var_beh @ rbp-0xbe
│      ╎╎   ; var int64_t var_bdh @ rbp-0xbd
│      ╎╎   ; var int64_t var_bch_2 @ rbp-0xbc
│      ╎╎   ; var char *s2 @ rbp-0xb8
│      ╎╎   ; var char *var_c8h @ rbp-0xb0
│      ╎╎   ; var char *s1 @ rbp-0xa8
│      ╎╎   ; var char *var_b8h @ rbp-0xa0
│      ╎╎   ; var size_t *var_b0h @ rbp-0x98
│      ╎╎   ; var char *var_90h_2 @ rbp-0x90
│      ╎╎   ; var mbstate_t *ps @ rbp-0x88
│      ╎╎   ; var int64_t var_80h_3 @ rbp-0x80
│      ╎╎   ; var size_t n @ rbp-0x78
│      ╎╎   ; var char *s @ rbp-0x70
│      ╎╎   ; var uint32_t var_80h_2 @ rbp-0x68
│      ╎╎   ; var uint32_t var_78h @ rbp-0x60
│      ╎╎   ; var uint32_t var_5fh_2 @ rbp-0x5f
│      ╎╎   ; var uint32_t var_5eh_2 @ rbp-0x5e
│      ╎╎   ; var uint32_t var_5dh_3 @ rbp-0x5d
│      ╎╎   ; var uint32_t var_5ch_3 @ rbp-0x5c
│      ╎╎   ; var uint32_t var_70h_2 @ rbp-0x58
│      ╎╎   ; var int64_t var_68h_2 @ rbp-0x50
│      ╎╎   ; var uint32_t var_60h @ rbp-0x48
│      ╎╎   ; var int64_t var_5fh @ rbp-0x47
│      ╎╎   ; var int64_t var_5eh @ rbp-0x46
│      ╎╎   ; var int64_t var_5dh_2 @ rbp-0x45
│      ╎╎   ; var wint_t wc @ rbp-0x44
│      ╎╎   ; var uint32_t var_58h_2 @ rbp-0x40
│      ╎╎   ; var int64_t var_50h @ rbp-0x38
│      ╎╎   ; var int64_t var_38h_2 @ rbp-0x20
│      ╎╎   ; var int64_t var_28h @ rbp-0x10
│      ╎╎   ; var int64_t var_8h @ rbp-0x8
│      ╎╎   ; var int64_t var_d0h @ rbp+0x40
│      ╎╎   ; var int64_t var_bch @ rbp+0x54
│      ╎╎   ; var int64_t var_80h @ rbp+0x90
│      ╎╎   ; var int64_t var_70h @ rbp+0xa0
│      ╎╎   ; var int64_t var_68h @ rbp+0xa8
│      ╎╎   ; var int64_t var_5dh @ rbp+0xb3
│      ╎╎   ; var int64_t var_5ch @ rbp+0xb4
│      ╎╎   ; var int64_t var_58h @ rbp+0xb8
│      ╎╎   ; var int64_t var_38h @ rbp+0xd8
│      ╎╎   ; var int64_t var_10h @ rbp+0x120
│      ╎╎   ; var int64_t var_18h_2 @ rbp+0x128
│      ╎╎   ; var int64_t var_18h @ rbp+0x220
│      ╎╎   0x00003610      55             push rbp
│      ╎╎   0x00003611      31f6           xor esi, esi                ; const char *locale
│      ╎╎   0x00003613      31ff           xor edi, edi                ; int category
│      ╎╎   0x00003615      4889e5         mov rbp, rsp
│      ╎╎   0x00003618      53             push rbx
│      ╎╎   0x00003619      4881ec180100.  sub rsp, 0x118
│      ╎╎   0x00003620      64488b042528.  mov rax, qword fs:[0x28]
│      ╎╎   0x00003629      488945e8       mov qword [var_18h], rax
│      ╎╎   0x0000362d      31c0           xor eax, eax
│      ╎╎   0x0000362f      e8dcedffff     call sym.imp.setlocale      ; char *setlocale(int category, const char *locale)
│      ╎╎   0x00003634      4885c0         test rax, rax
│     ┌───< 0x00003637      7413           je 0x364c
│     │╎╎   0x00003639      4889c7         mov rdi, rax                ; const char *s
│     │╎╎   0x0000363c      4889c3         mov rbx, rax
│     │╎╎   0x0000363f      e8ececffff     call sym.imp.strlen         ; size_t strlen(const char *s)
│     │╎╎   0x00003644      483d00010000   cmp rax, 0x100
│    ┌────< 0x0000364a      7624           jbe 0x3670
│    ││╎╎   ; CODE XREFS from fcn.00003610 @ 0x3637, 0x36b7
│   ┌─└───> 0x0000364c      31c0           xor eax, eax
│   ╎│ ╎╎   ; CODE XREF from fcn.00003610 @ 0x36ae
│   ╎│┌───> 0x0000364e      488b55e8       mov rdx, qword [var_18h]
│   ╎│╎╎╎   0x00003652      64482b142528.  sub rdx, qword fs:[0x28]
│  ┌──────< 0x0000365b      0f85b9000000   jne 0x371a
│  │╎│╎╎╎   0x00003661      488b5df8       mov rbx, qword [var_8h]
│  │╎│╎╎╎   0x00003665      c9             leave
│  │╎│╎╎╎   0x00003666      c3             ret
..
│  │╎│╎╎╎   ; CODE XREF from fcn.00003610 @ 0x364a
│  │╎└────> 0x00003670      4c8d85e0feff.  lea r8, [var_120h]
│  │╎ ╎╎╎   0x00003677      4883c001       add rax, 1
│  │╎ ╎╎╎   0x0000367b      4c89c7         mov rdi, r8
│  │╎ ╎╎╎   0x0000367e      83f808         cmp eax, 8
│  │╎┌────< 0x00003681      737d           jae 0x3700
│  │╎│╎╎╎   0x00003683      31d2           xor edx, edx
│  │╎│╎╎╎   0x00003685      a804           test al, 4
│ ┌───────< 0x00003687      7567           jne 0x36f0
│ ││╎│╎╎╎   ; CODE XREF from fcn.00003610 @ 0x3712
│ ────────> 0x00003689      a802           test al, 2
│ ────────< 0x0000368b      754b           jne 0x36d8
│ ││╎│╎╎╎   ; CODE XREF from fcn.00003610 @ 0x36fb
│ ────────> 0x0000368d      a801           test al, 1
│ ────────< 0x0000368f      752f           jne 0x36c0
│ ││╎│╎╎╎   ; CODE XREF from fcn.00003610 @ 0x36e6
│ ────────> 0x00003691      80bde0feffff.  cmp byte [var_120h], 0x43
│ ────────< 0x00003698      7416           je 0x36b0
│ ││╎│╎╎╎   ; CODE XREFS from fcn.00003610 @ 0x36b9, 0x36ce
│ ────────> 0x0000369a      488d35092f00.  lea rsi, str.POSIX          ; 0x65aa ; "POSIX" ; const char *s2
│ ││╎│╎╎╎   0x000036a1      4c89c7         mov rdi, r8                 ; const char *s1
│ ││╎│╎╎╎   0x000036a4      e807edffff     call sym.imp.strcmp         ; int strcmp(const char *s1, const char *s2)
│ ││╎│╎╎╎   0x000036a9      85c0           test eax, eax
│ ││╎│╎╎╎   0x000036ab      0f95c0         setne al
│ ││╎│└───< 0x000036ae      eb9e           jmp 0x364e
│ ││╎│ ╎╎   ; CODE XREFS from fcn.00003610 @ 0x3698, 0x36d0
│ ────┌───> 0x000036b0      80bde1feffff.  cmp byte [var_11fh], 0
│ ││└─────< 0x000036b7      7493           je 0x364c
│ ────────< 0x000036b9      ebdf           jmp 0x369a
..
│ ││ │╎╎╎   ; CODE XREFS from fcn.00003610 @ 0x368f, 0x36e8
│ ──┌─────> 0x000036c0      0fb60413       movzx eax, byte [rbx + rdx]
│ ││╎│╎╎╎   0x000036c4      880417         mov byte [rdi + rdx], al
│ ││╎│╎╎╎   0x000036c7      80bde0feffff.  cmp byte [var_120h], 0x43
│ ────────< 0x000036ce      75ca           jne 0x369a
│ ││╎│└───< 0x000036d0      ebde           jmp 0x36b0
..
│ ││╎│ ╎╎   ; CODE XREFS from fcn.00003610 @ 0x368b, 0x36fd
│ ────┌───> 0x000036d8      0fb70c13       movzx ecx, word [rbx + rdx]
│ ││╎│╎╎╎   0x000036dc      66890c17       mov word [rdi + rdx], cx
│ ││╎│╎╎╎   0x000036e0      4883c202       add rdx, 2
│ ││╎│╎╎╎   0x000036e4      a801           test al, 1
│ ────────< 0x000036e6      74a9           je 0x3691
│ ││└─────< 0x000036e8      ebd6           jmp 0x36c0
..
│ ││ │╎╎╎   ; CODE XREFS from fcn.00003610 @ 0x3687, 0x3718
│ └─┌─────> 0x000036f0      8b13           mov edx, dword [rbx]
│  │╎│╎╎╎   ; DATA XREF from fcn.00003610 @ 0x2ec5
│  │╎│╎╎╎   0x000036f2      8917           mov dword [rdi], edx
│  │╎│╎╎╎   0x000036f4      ba04000000     mov edx, 4
│  │╎│╎╎╎   0x000036f9      a802           test al, 2
│ ────────< 0x000036fb      7490           je 0x368d
│  │╎│└───< 0x000036fd      ebd9           jmp 0x36d8
..
│  │╎│ ╎╎   ; CODE XREF from fcn.00003610 @ 0x3681
│  │╎└────> 0x00003700      89c1           mov ecx, eax
│  │╎  ╎╎   0x00003702      4889de         mov rsi, rbx
│  │╎  ╎╎   0x00003705      31d2           xor edx, edx
│  │╎  ╎╎   0x00003707      c1e903         shr ecx, 3
│  │╎  ╎╎   0x0000370a      f348a5         rep movsq qword [rdi], qword ptr [rsi]
│  │╎  ╎╎   0x0000370d      4889f3         mov rbx, rsi
│  │╎  ╎╎   0x00003710      a804           test al, 4
│ ────────< 0x00003712      0f8471ffffff   je 0x3689
│  │└─────< 0x00003718      ebd6           jmp 0x36f0
│  │   ╎╎   ; CODE XREF from fcn.00003610 @ 0x365b
│  └──────> 0x0000371a      e821ecffff     call sym.imp.__stack_chk_fail
│      ╎╎   0x0000371f      90             nop
│      ╎╎   0x00003720      55             push rbp
│      ╎╎   0x00003721      4989f3         mov r11, rsi
│      ╎╎   0x00003724      4889e5         mov rbp, rsp
│      ╎╎   0x00003727      4157           push r15
│      ╎╎   0x00003729      4156           push r14
│      ╎╎   0x0000372b      4155           push r13
│      ╎╎   0x0000372d      4154           push r12
│      ╎╎   0x0000372f      53             push rbx
│      ╎╎   0x00003730      4881ecc80000.  sub rsp, 0xc8
│      ╎╎   0x00003737      4c894d80       mov qword [var_80h], r9
│      ╎╎   0x0000373b      4c8b7510       mov r14, qword [var_10h]
│      ╎╎   0x0000373f      49c7c1ffffff.  mov r9, 0xffffffffffffffff
│      ╎╎   0x00003746      48895590       mov qword [var_70h], rdx
│      ╎╎   0x0000374a      4c8b7d18       mov r15, qword [var_18h_2]
│      ╎╎   0x0000374e      44898544ffff.  mov dword [var_bch], r8d
│      ╎╎   0x00003755      4d89f5         mov r13, r14
│      ╎╎   0x00003758      4d89ce         mov r14, r9
│      ╎╎   0x0000375b      4989f9         mov r9, rdi
│      ╎╎   0x0000375e      64488b042528.  mov rax, qword fs:[0x28]
│      ╎╎   0x00003767      488945c8       mov qword [var_38h], rax
│      ╎╎   0x0000376b      31c0           xor eax, eax
│      ╎╎   0x0000376d      894da4         mov dword [var_5ch], ecx
│      ╎╎   ; CODE XREFS from fcn.00003610 @ 0x3c75, 0x4e36
│    ┌┌───> 0x00003770      4c895d98       mov qword [var_68h], r11
│    ╎╎╎╎   0x00003774      4c894da8       mov qword [var_58h], r9
│    ╎╎╎╎   0x00003778      e8a3ebffff     call sym.imp.__ctype_get_mb_cur_max
│    ╎╎╎╎   0x0000377d      8b9d44ffffff   mov ebx, dword [var_bch]
│    ╎╎╎╎   0x00003783      48898530ffff.  mov qword [var_d0h], rax
│    ╎╎╎╎   0x0000378a      8b45a4         mov eax, dword [var_5ch]
│    ╎╎╎╎   0x0000378d      83e302         and ebx, 2
│    ╎╎╎╎   0x00003790      0f9545a3       setne byte [var_5dh]
│    ╎╎╎╎   0x00003794      83f80a         cmp eax, 0xa
│    ╎╎└──< 0x00003797      0f8723edffff   ja section..text
│    ╎╎ ╎   0x0000379d      488d35142900.  lea rsi, [0x000060b8]
│    ╎╎ ╎   0x000037a4      4c8b4da8       mov r9, qword [var_70h_2]
│    ╎╎ ╎   0x000037a8      4c8b5d98       mov r11, qword [var_80h_2]
│    ╎╎ ╎   0x000037ac      48630486       movsxd rax, dword [rsi + rax*4]
│    ╎╎ ╎   0x000037b0      4801f0         add rax, rsi
│    ╎╎ ╎   ;-- switch
│    ╎╎ ╎   0x000037b3      3effe0         jmp rax                     ; switch table (11 cases) at 0x60b8
..
│    ╎╎ ╎   ;-- case 8...10:                                           ; from 0x000037b3
│    ╎╎ ╎   ; CODE XREF from fcn.00003610 @ 0x37b3
│    ╎╎ ╎   0x000037c0      837da40a       cmp dword [var_5ch_3], 0xa
│    ╎╎ ╎   ; DATA XREF from fcn.00003610 @ 0x2f0b
│    ╎╎┌──< 0x000037c4      7464           je 0x382a
│    ╎╎│╎   0x000037c6      4c8d25e32d00.  lea r12, [0x000065b0]       ; "`"
│    ╎╎│╎   0x000037cd      31ff           xor edi, edi
│    ╎╎│╎   0x000037cf      ba05000000     mov edx, 5
│    ╎╎│╎   0x000037d4      4c895d98       mov qword [var_80h_2], r11
│    ╎╎│╎   0x000037d8      4c89e6         mov rsi, r12
│    ╎╎│╎   0x000037db      4c894da8       mov qword [var_70h_2], r9
│    ╎╎│╎   0x000037df      e82cebffff     call sym.imp.dcgettext
│    ╎╎│╎   0x000037e4      4c8b4da8       mov r9, qword [var_70h_2]
│    ╎╎│╎   0x000037e8      4c8b5d98       mov r11, qword [var_80h_2]
│    ╎╎│╎   0x000037ec      4c39e0         cmp rax, r12
│    ╎╎│╎   0x000037ef      4989c5         mov r13, rax
│   ┌─────< 0x000037f2      0f84ae150000   je 0x4da6
│   │╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x4dbc
│  ┌──────> 0x000037f8      4c8d25852d00.  lea r12, [0x00006584]       ; "'"
│  ╎│╎╎│╎   0x000037ff      31ff           xor edi, edi
│  ╎│╎╎│╎   0x00003801      ba05000000     mov edx, 5
│  ╎│╎╎│╎   0x00003806      4c895d98       mov qword [var_80h_2], r11
│  ╎│╎╎│╎   0x0000380a      4c89e6         mov rsi, r12
│  ╎│╎╎│╎   0x0000380d      4c894da8       mov qword [var_70h_2], r9
│  ╎│╎╎│╎   0x00003811      e8faeaffff     call sym.imp.dcgettext
│  ╎│╎╎│╎   0x00003816      4c8b4da8       mov r9, qword [var_70h_2]
│  ╎│╎╎│╎   0x0000381a      4c8b5d98       mov r11, qword [var_80h_2]
│  ╎│╎╎│╎   0x0000381e      4c39e0         cmp rax, r12
│  ╎│╎╎│╎   0x00003821      4989c7         mov r15, rax
│ ┌───────< 0x00003824      0f8461150000   je 0x4d8b
│ │╎│╎╎│╎   ; CODE XREFS from fcn.00003610 @ 0x37c4, 0x4da1
│ ─────└──> 0x0000382a      48c745a80000.  mov qword [var_70h_2], 0
│ │╎│╎╎ ╎   ; DATA XREF from fcn.00003610 @ 0x2e23
│ │╎│╎╎ ╎   0x00003832      85db           test ebx, ebx
│ │╎│╎╎┌──< 0x00003834      0f8494140000   je 0x4cce
│ │╎│╎╎│╎   ; CODE XREFS from fcn.00003610 @ 0x4cd5, 0x4cfb
│ ────────> 0x0000383a      4c89ff         mov rdi, r15                ; const char *s
│ │╎│╎╎│╎   0x0000383d      4c899d70ffff.  mov qword [var_90h_2], r11
│ │╎│╎╎│╎   0x00003844      4c898d78ffff.  mov qword [ps], r9
│ │╎│╎╎│╎   0x0000384b      e8e0eaffff     call sym.imp.strlen         ; size_t strlen(const char *s)
│ │╎│╎╎│╎   ; DATA XREF from fcn.00003610 @ 0x2e5a
│ │╎│╎╎│╎   0x00003850      c6459801       mov byte [var_80h_2], 1
│ │╎│╎╎│╎   0x00003854      4c8b8d78ffff.  mov r9, qword [ps]
│ │╎│╎╎│╎   0x0000385b      48894588       mov qword [n], rax
│ │╎│╎╎│╎   0x0000385f      4c8b9d70ffff.  mov r11, qword [var_90h_2]
│ │╎│╎╎│╎   0x00003866      4c89bd48ffff.  mov qword [s2], r15
│ │╎│╎╎│╎   0x0000386d      c645a000       mov byte [var_78h], 0
│ │╎│╎╎│╎   0x00003871      c645a200       mov byte [var_5eh_2], 0
│ │╎│╎╎│╎   0x00003875      48c78538ffff.  mov qword [var_c8h_2], 0
│ │╎│╎╎│╎   0x00003880      c645a101       mov byte [var_5fh_2], 1
│ │╎│╎╎│╎   0x00003884      0f1f4000       nop dword [rax]
│ │╎│╎╎│╎   ; XREFS: DATA 0x00002ddc  CODE 0x00003ed6  CODE 0x00003f31  
│ │╎│╎╎│╎   ; XREFS: CODE 0x00003f70  CODE 0x00003fc3  CODE 0x0000400c  
│ │╎│╎╎│╎   ; XREFS: CODE 0x00004055  CODE 0x00004af1  CODE 0x00004d3d  
│ ────────> 0x00003888      31db           xor ebx, ebx
│ │╎│╎╎│╎   0x0000388a      660f1f440000   nop word [rax + rax]
│ │╎│╎╎│╎   ; CODE XREFS from fcn.00003610 @ 0x39fb, 0x4b41
│ ────────> 0x00003890      4c39f3         cmp rbx, r14
│ │╎│╎╎│╎   0x00003893      410f95c2       setne r10b
│ │╎│╎╎│╎   0x00003897      4983feff       cmp r14, 0xffffffffffffffff
│ ────────< 0x0000389b      750c           jne 0x38a9
│ │╎│╎╎│╎   0x0000389d      488b4590       mov rax, qword [s]
│ │╎│╎╎│╎   0x000038a1      803c1800       cmp byte [rax + rbx], 0
│ │╎│╎╎│╎   0x000038a5      410f95c2       setne r10b
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x389b
│ ────────> 0x000038a9      4584d2         test r10b, r10b
│ ────────< 0x000038ac      0f84b70e0000   je 0x4769
│ │╎│╎╎│╎   0x000038b2      837da402       cmp dword [var_5ch_3], 2
│ │╎│╎╎│╎   0x000038b6      488b7d90       mov rdi, qword [s]
│ │╎│╎╎│╎   0x000038ba      0f95c0         setne al
│ │╎│╎╎│╎   0x000038bd      2245a1         and al, byte [var_5fh_2]
│ │╎│╎╎│╎   0x000038c0      48837d8800     cmp qword [n], 0
│ │╎│╎╎│╎   0x000038c5      4189c0         mov r8d, eax
│ │╎│╎╎│╎   0x000038c8      0f95c0         setne al
│ │╎│╎╎│╎   0x000038cb      488d0c1f       lea rcx, [rdi + rbx]
│ │╎│╎╎│╎   0x000038cf      4420c0         and al, r8b
│ │╎│╎╎│╎   0x000038d2      4189c4         mov r12d, eax
│ ────────< 0x000038d5      0f85a5070000   jne 0x4080
│ │╎│╎╎│╎   0x000038db      0fb631         movzx esi, byte [rcx]
│ │╎│╎╎│╎   0x000038de      4080fe3f       cmp sil, 0x3f
│ ────────< 0x000038e2      0f8fa80b0000   jg 0x4490
│ │╎│╎╎│╎   0x000038e8      4084f6         test sil, sil
│ ────────< 0x000038eb      0f887f010000   js case.0x419a.1
│ │╎│╎╎│╎   0x000038f1      4080fe3f       cmp sil, 0x3f
│ ────────< 0x000038f5      0f8775010000   ja case.0x419a.1
│ │╎│╎╎│╎   0x000038fb      488d3de22700.  lea rdi, [0x000060e4]
│ │╎│╎╎│╎   0x00003902      400fb6c6       movzx eax, sil
│ │╎│╎╎│╎   0x00003906      48630487       movsxd rax, dword [rdi + rax*4]
│ │╎│╎╎│╎   0x0000390a      4801f8         add rax, rdi
│ │╎│╎╎│╎   ;-- switch
│ │╎│╎╎│╎   0x0000390d      3effe0         jmp rax                     ; switch table (64 cases) at 0x60e4
│ │╎│╎╎│╎   ;-- case 12:                                               ; from 0x0000390d
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x390d
│ │╎│╎╎│╎   0x00003910      837da402       cmp dword [var_5ch_3], 2
│ │╎│╎╎│╎   0x00003914      be0c000000     mov esi, 0xc
│ │╎│╎╎│╎   0x00003919      b866000000     mov eax, 0x66               ; 'f'
│ │╎│╎╎│╎   0x0000391e      0f94c2         sete dl
│ │╎│╎╎│╎   0x00003921      0f1f80000000.  nop dword [rax]
│ │╎│╎╎│╎   ; XREFS: CODE 0x00003cbd  CODE 0x00003e0a  CODE 0x00003e79  
│ │╎│╎╎│╎   ; XREFS: CODE 0x000041c0  CODE 0x0000423f  CODE 0x00004287  
│ │╎│╎╎│╎   ; XREFS: CODE 0x000043ac  CODE 0x00004428  CODE 0x0000444b  
│ ────────> 0x00003928      807da100       cmp byte [var_5fh_2], 0
│ ────────< 0x0000392c      0f8566030000   jne 0x3c98
│ │╎│╎╎│╎   ;-- case 33...34:                                          ; from 0x0000419a
│ │╎│╎╎│╎   ;-- case 36:                                               ; from 0x0000419a
│ │╎│╎╎│╎   ;-- case 38:                                               ; from 0x0000419a
│ │╎│╎╎│╎   ;-- case 41...42:                                          ; from 0x0000419a
│ │╎│╎╎│╎   ;-- case 59:                                               ; from 0x0000419a
│ │╎│╎╎│╎   ;-- case 60...62:                                          ; from 0x0000419a
│ │╎│╎╎│╎   ; XREFS: CODE 0x00003c8f  CODE 0x00003e4b  CODE 0x0000419a  
│ │╎│╎╎│╎   ; XREFS: CODE 0x00004313  CODE 0x0000451c  CODE 0x000047d0  
│ │╎│╎╎│╎   ; XREFS: CODE 0x00004802  CODE 0x00004867  CODE 0x00004871  
│ │╎│╎╎│╎   ; XREFS: CODE 0x00004c55  
│ ────────> 0x00003932      4531d2         xor r10d, r10d
│ │╎│╎╎│╎   ;-- case 37:                                               ; from 0x0000390d
│ │╎│╎╎│╎   ;-- case 44...58:                                          ; from 0x0000390d
│ │╎│╎╎│╎   ; XREFS: CODE 0x0000390d  CODE 0x00003adb  CODE 0x00003c3f  
│ │╎│╎╎│╎   ; XREFS: CODE 0x00003c49  CODE 0x00003cf2  CODE 0x00003d01  
│ │╎│╎╎│╎   ; XREFS: CODE 0x00003dad  CODE 0x000044b8  
│ ────────> 0x00003935      4489c0         mov eax, r8d
│ │╎│╎╎│╎   0x00003938      0a45a3         or al, byte [var_5dh_3]
│ ────────< 0x0000393b      0f84d7000000   je 0x3a18
│ │╎│╎╎│╎   ; XREFS: CODE 0x00003d92  CODE 0x00003e34  CODE 0x000041a9  
│ │╎│╎╎│╎   ; XREFS: CODE 0x00004261  CODE 0x000042ad  CODE 0x00004304  
│ │╎│╎╎│╎   ; XREFS: CODE 0x000043ee  CODE 0x0000440e  CODE 0x0000447f  
│ │╎│╎╎│╎   ; XREFS: CODE 0x00004bf8  CODE 0x00004c2f  CODE 0x00004dd9  
│ ────────> 0x00003941      31c0           xor eax, eax
│ │╎│╎╎│╎   ; CODE XREFS from fcn.00003610 @ 0x422e, 0x4c77
│ ────────> 0x00003943      488b4d80       mov rcx, qword [var_80h_3]
│ │╎│╎╎│╎   0x00003947      4885c9         test rcx, rcx
│ ────────< 0x0000394a      0f84c8000000   je 0x3a18
│ │╎│╎╎│╎   0x00003950      89f2           mov edx, esi
│ │╎│╎╎│╎   0x00003952      c0ea05         shr dl, 5
│ │╎│╎╎│╎   0x00003955      0fb6d2         movzx edx, dl
│ │╎│╎╎│╎   0x00003958      8b1491         mov edx, dword [rcx + rdx*4]
│ │╎│╎╎│╎   0x0000395b      89f1           mov ecx, esi
│ │╎│╎╎│╎   0x0000395d      d3ea           shr edx, cl
│ │╎│╎╎│╎   0x0000395f      83e201         and edx, 1
│ ────────< 0x00003962      0f84b0000000   je 0x3a18
│ │╎│╎╎│╎   0x00003968      837da402       cmp dword [var_5ch_3], 2
│ │╎│╎╎│╎   0x0000396c      0f94c2         sete dl
│ │╎│╎╎│╎   ; CODE XREFS from fcn.00003610 @ 0x3a22, 0x43c8, 0x4437, 0x445a, 0x4469
│ ────────> 0x0000396f      807da300       cmp byte [var_5dh_3], 0
│ ────────< 0x00003973      0f852e030000   jne 0x3ca7
│ │╎│╎╎│╎   ; CODE XREFS from fcn.00003610 @ 0x3ca1, 0x41cf, 0x424e, 0x4276, 0x4296
│ ────────> 0x00003979      0fb645a2       movzx eax, byte [var_5eh_2]
│ │╎│╎╎│╎   0x0000397d      83f001         xor eax, 1
│ │╎│╎╎│╎   0x00003980      20d0           and al, dl
│ ────────< 0x00003982      743c           je 0x39c0
│ │╎│╎╎│╎   0x00003984      488b7da8       mov rdi, qword [var_70h_2]
│ │╎│╎╎│╎   0x00003988      4c39df         cmp rdi, r11
│ ────────< 0x0000398b      7305           jae 0x3992
│ │╎│╎╎│╎   0x0000398d      41c6043927     mov byte [r9 + rdi], 0x27   ; '''
│ │╎│╎╎│╎                                                              ; [0x27:1]=0
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x398b
│ ────────> 0x00003992      488b4da8       mov rcx, qword [var_70h_2]
│ │╎│╎╎│╎   0x00003996      488d5101       lea rdx, [rcx + 1]
│ │╎│╎╎│╎   0x0000399a      4c39da         cmp rdx, r11
│ ────────< 0x0000399d      7306           jae 0x39a5
│ │╎│╎╎│╎   0x0000399f      41c644090124   mov byte [r9 + rcx + 1], 0x24 ; '$'
│ │╎│╎╎│╎                                                              ; [0x24:1]=0
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x399d
│ ────────> 0x000039a5      488b7da8       mov rdi, qword [var_70h_2]
│ │╎│╎╎│╎   0x000039a9      488d5702       lea rdx, [rdi + 2]
│ │╎│╎╎│╎   0x000039ad      4c39da         cmp rdx, r11
│ ────────< 0x000039b0      7306           jae 0x39b8
│ │╎│╎╎│╎   0x000039b2      41c644390227   mov byte [r9 + rdi + 2], 0x27 ; '''
│ │╎│╎╎│╎                                                              ; [0x27:1]=0
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x39b0
│ ────────> 0x000039b8      488345a803     add qword [var_70h_2], 3
│ │╎│╎╎│╎   0x000039bd      8845a2         mov byte [var_5eh_2], al
│ │╎│╎╎│╎   ; CODE XREFS from fcn.00003610 @ 0x3982, 0x487f
│ ────────> 0x000039c0      488b45a8       mov rax, qword [var_70h_2]
│ │╎│╎╎│╎   0x000039c4      4c39d8         cmp rax, r11
│ ────────< 0x000039c7      7305           jae 0x39ce
│ │╎│╎╎│╎   0x000039c9      41c604015c     mov byte [r9 + rax], 0x5c   ; '\\'
│ │╎│╎╎│╎                                                              ; [0x5c:1]=0
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x39c7
│ ────────> 0x000039ce      488345a801     add qword [var_70h_2], 1
│ │╎│╎╎│╎   0x000039d3      4883c301       add rbx, 1
│ │╎│╎╎│╎   ; CODE XREFS from fcn.00003610 @ 0x3a34, 0x3a60, 0x4bbf
│ ────────> 0x000039d7      488b45a8       mov rax, qword [var_70h_2]
│ │╎│╎╎│╎   0x000039db      4c39d8         cmp rax, r11
│ ────────< 0x000039de      7304           jae 0x39e4
│ │╎│╎╎│╎   0x000039e0      41883401       mov byte [r9 + rax], sil
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x39de
│ ────────> 0x000039e4      0fb64598       movzx eax, byte [var_80h_2]
│ │╎│╎╎│╎   0x000039e8      488345a801     add qword [var_70h_2], 1
│ │╎│╎╎│╎   0x000039ed      bf00000000     mov edi, 0
│ │╎│╎╎│╎   0x000039f2      4584d2         test r10b, r10b
│ │╎│╎╎│╎   0x000039f5      0f44c7         cmove eax, edi
│ │╎│╎╎│╎   0x000039f8      884598         mov byte [var_80h_2], al
│ ────────< 0x000039fb      e990feffff     jmp 0x3890
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x41f1
│ ────────> 0x00003a00      48894da8       mov qword [var_70h_2], rcx
│ │╎│╎╎│╎   0x00003a04      4189c4         mov r12d, eax
│ │╎│╎╎│╎   0x00003a07      be30000000     mov esi, 0x30               ; '0'
│ │╎│╎╎│╎   0x00003a0c      4489d0         mov eax, r10d
│ │╎│╎╎│╎   0x00003a0f      4531d2         xor r10d, r10d
│ │╎│╎╎│╎   ; DATA XREF from fcn.00003610 @ 0x2bb3
│ │╎│╎╎│╎   0x00003a12      660f1f440000   nop word [rax + rax]
│ │╎│╎╎│╎   ; XREFS: CODE 0x0000393b  CODE 0x0000394a  CODE 0x00003962  
│ │╎│╎╎│╎   ; XREFS: CODE 0x00003d98  CODE 0x00003e3a  CODE 0x000041af  
│ │╎│╎╎│╎   ; XREFS: CODE 0x00004267  CODE 0x000042b3  CODE 0x0000430a  
│ │╎│╎╎│╎   ; XREFS: CODE 0x000043f4  CODE 0x00004414  CODE 0x00004485  
│ │╎│╎╎│╎   ; XREFS: CODE 0x00004c35  CODE 0x00004ddf  
│ ────────> 0x00003a18      837da402       cmp dword [var_5ch_3], 2
│ │╎│╎╎│╎   0x00003a1c      0f94c2         sete dl
│ │╎│╎╎│╎   0x00003a1f      4584e4         test r12b, r12b
│ ────────< 0x00003a22      0f8547ffffff   jne 0x396f
│ │╎│╎╎│╎   ; CODE XREFS from fcn.00003610 @ 0x3df4, 0x4398, 0x4824, 0x4c08
│ ────────> 0x00003a28      83f001         xor eax, 1
│ │╎│╎╎│╎   0x00003a2b      4883c301       add rbx, 1
│ │╎│╎╎│╎   0x00003a2f      2245a2         and al, byte [var_5eh_2]
│ │╎│╎╎│╎   ; CODE XREFS from fcn.00003610 @ 0x44ed, 0x4b6b
│ ────────> 0x00003a32      84c0           test al, al
│ ────────< 0x00003a34      74a1           je 0x39d7
│ │╎│╎╎│╎   0x00003a36      488b45a8       mov rax, qword [var_70h_2]
│ │╎│╎╎│╎   0x00003a3a      4c39d8         cmp rax, r11
│ ────────< 0x00003a3d      7305           jae 0x3a44
│ │╎│╎╎│╎   0x00003a3f      41c6040127     mov byte [r9 + rax], 0x27   ; '''
│ │╎│╎╎│╎                                                              ; [0x27:1]=0
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x3a3d
│ ────────> 0x00003a44      488b4da8       mov rcx, qword [var_70h_2]
│ │╎│╎╎│╎   0x00003a48      488d4101       lea rax, [rcx + 1]
│ │╎│╎╎│╎   0x00003a4c      4c39d8         cmp rax, r11
│ ────────< 0x00003a4f      7306           jae 0x3a57
│ │╎│╎╎│╎   0x00003a51      41c644090127   mov byte [r9 + rcx + 1], 0x27 ; '''
│ │╎│╎╎│╎                                                              ; [0x27:1]=0
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x3a4f
│ ────────> 0x00003a57      488345a802     add qword [var_70h_2], 2
│ │╎│╎╎│╎   0x00003a5c      c645a200       mov byte [var_5eh_2], 0
│ ────────< 0x00003a60      e972ffffff     jmp 0x39d7
..
│ │╎│╎╎│╎   ;-- case 1...6:                                            ; from 0x000042f2
│ │╎│╎╎│╎   ;-- case 14:                                               ; from 0x000042f2
│ │╎│╎╎│╎   ;-- default:                                               ; from 0x42f2
│ │╎│╎╎│╎   ; CODE XREFS from fcn.00003610 @ 0x42d0, 0x42da, 0x42f2, 0x453e
│ ────────> 0x00003a68      4531e4         xor r12d, r12d
│ │╎│╎╎│╎   0x00003a6b      0f1f440000     nop dword [rax + rax]
│ │╎│╎╎│╎   ;-- case 1...6:                                            ; from 0x0000419a
│ │╎│╎╎│╎   ;-- case 14:                                               ; from 0x0000419a
│ │╎│╎╎│╎   ;-- default:                                               ; from 0x419a
│ │╎│╎╎│╎   ;-- case 15...0:                                           ; from 0x0000390d
│ │╎│╎╎│╎   ;-- case 1:                                                ; from 0x0000390d
│ │╎│╎╎│╎   ;-- case 2...6:                                            ; from 0x0000390d
│ │╎│╎╎│╎   ;-- case 14:                                               ; from 0x0000390d
│ │╎│╎╎│╎   ;-- default:                                               ; from 0x390d
│ │╎│╎╎│╎   ; XREFS: CODE 0x000038eb  CODE 0x000038f5  CODE 0x0000390d  
│ │╎│╎╎│╎   ; XREFS: CODE 0x00004178  CODE 0x00004182  CODE 0x0000419a  
│ │╎│╎╎│╎   ; XREFS: CODE 0x0000449a  CODE 0x0000483e  CODE 0x00004dc9  
│ ────────> 0x00003a70      4883bd30ffff.  cmp qword [var_d0h_3], 1
│ ────────< 0x00003a78      0f85320b0000   jne 0x45b0
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x45a7
│ ────────> 0x00003a7e      4c899d60ffff.  mov qword [var_b8h], r11
│ │╎│╎╎│╎   0x00003a85      4c898d68ffff.  mov qword [var_b0h], r9
│ │╎│╎╎│╎   0x00003a8c      4088b570ffff.  mov byte [var_90h_2], sil
│ │╎│╎╎│╎   0x00003a93      44888578ffff.  mov byte [ps], r8b
│ │╎│╎╎│╎   0x00003a9a      e811eaffff     call sym.imp.__ctype_b_loc
│ │╎│╎╎│╎   0x00003a9f      440fb68578ff.  movzx r8d, byte [ps]
│ │╎│╎╎│╎   0x00003aa7      4c8b8d68ffff.  mov r9, qword [var_b0h]
│ │╎│╎╎│╎   0x00003aae      4889c2         mov rdx, rax
│ │╎│╎╎│╎   0x00003ab1      0fb68570ffff.  movzx eax, byte [var_90h_2]
│ │╎│╎╎│╎   0x00003ab8      4c8b9d60ffff.  mov r11, qword [var_b8h]
│ │╎│╎╎│╎   0x00003abf      488b12         mov rdx, qword [rdx]
│ │╎│╎╎│╎   0x00003ac2      4889c6         mov rsi, rax
│ │╎│╎╎│╎   0x00003ac5      f644420140     test byte [rdx + rax*2 + 1], 0x40
│ │╎│╎╎│╎   0x00003aca      b801000000     mov eax, 1
│ │╎│╎╎│╎   0x00003acf      410f95c2       setne r10b
│ │╎│╎╎│╎   0x00003ad3      0f94c2         sete dl
│ │╎│╎╎│╎   0x00003ad6      2255a1         and dl, byte [var_5fh_2]
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x4764
│ ────────> 0x00003ad9      84d2           test dl, dl
│ ────────< 0x00003adb      0f8454feffff   je case.0x390d.37
│ │╎│╎╎│╎   0x00003ae1      0fb655a1       movzx edx, byte [var_5fh_2]
│ │╎│╎╎│╎   0x00003ae5      4531d2         xor r10d, r10d
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x475e
│ ────────> 0x00003ae8      44889560ffff.  mov byte [var_b8h], r10b
│ │╎│╎╎│╎   0x00003aef      4c8b45a8       mov r8, qword [var_70h_2]
│ │╎│╎╎│╎   0x00003af3      488d0c03       lea rcx, [rbx + rax]
│ │╎│╎╎│╎   0x00003af7      31ff           xor edi, edi
│ │╎│╎╎│╎   0x00003af9      4c89b578ffff.  mov qword [ps], r14
│ │╎│╎╎│╎   0x00003b00      440fb655a2     movzx r10d, byte [var_5eh_2]
│ │╎│╎╎│╎   0x00003b05      4c89ad70ffff.  mov qword [var_90h_2], r13
│ │╎│╎╎│╎   0x00003b0c      4c8b7590       mov r14, qword [s]
│ │╎│╎╎│╎   0x00003b10      4c89bd68ffff.  mov qword [var_b0h], r15
│ │╎│╎╎│╎   0x00003b17      440fb66da3     movzx r13d, byte [var_5dh_3]
│ │╎│╎╎│╎   0x00003b1c      448b7da4       mov r15d, dword [var_5ch_3]
│ ────────< 0x00003b20      e9b1000000     jmp 0x3bd6
..
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x3bd8
│ ────────> 0x00003b28      4183ff02       cmp r15d, 2
│ │╎│╎╎│╎   0x00003b2c      0f94c0         sete al
│ │╎│╎╎│╎   0x00003b2f      4584ed         test r13b, r13b
│ ────────< 0x00003b32      0f8538100000   jne 0x4b70
│ │╎│╎╎│╎   0x00003b38      4489d7         mov edi, r10d
│ │╎│╎╎│╎   0x00003b3b      83f701         xor edi, 1
│ │╎│╎╎│╎   0x00003b3e      4020f8         and al, dil
│ ────────< 0x00003b41      742f           je 0x3b72
│ │╎│╎╎│╎   0x00003b43      4d39d8         cmp r8, r11
│ ────────< 0x00003b46      7305           jae 0x3b4d
│ │╎│╎╎│╎   0x00003b48      43c6040127     mov byte [r9 + r8], 0x27    ; '''
│ │╎│╎╎│╎                                                              ; [0x27:1]=0
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x3b46
│ ────────> 0x00003b4d      498d7801       lea rdi, [r8 + 1]
│ │╎│╎╎│╎   0x00003b51      4c39df         cmp rdi, r11
│ ────────< 0x00003b54      7306           jae 0x3b5c
│ │╎│╎╎│╎   0x00003b56      43c644010124   mov byte [r9 + r8 + 1], 0x24 ; '$'
│ │╎│╎╎│╎                                                              ; [0x24:1]=0
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x3b54
│ ────────> 0x00003b5c      498d7802       lea rdi, [r8 + 2]
│ │╎│╎╎│╎   0x00003b60      4c39df         cmp rdi, r11
│ ────────< 0x00003b63      7306           jae 0x3b6b
│ │╎│╎╎│╎   0x00003b65      43c644010227   mov byte [r9 + r8 + 2], 0x27 ; '''
│ │╎│╎╎│╎                                                              ; [0x27:1]=0
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x3b63
│ ────────> 0x00003b6b      4983c003       add r8, 3
│ │╎│╎╎│╎   0x00003b6f      4189c2         mov r10d, eax
│ │╎│╎╎│╎   ; CODE XREFS from fcn.00003610 @ 0x2b97, 0x3b41
│ ────────> 0x00003b72      4d39d8         cmp r8, r11
│ ────────< 0x00003b75      7305           jae 0x3b7c
│ │╎│╎╎│╎   0x00003b77      43c604015c     mov byte [r9 + r8], 0x5c    ; '\\'
│ │╎│╎╎│╎                                                              ; [0x5c:1]=0
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x3b75
│ ────────> 0x00003b7c      498d4001       lea rax, [r8 + 1]
│ │╎│╎╎│╎   0x00003b80      4c39d8         cmp rax, r11
│ ────────< 0x00003b83      730d           jae 0x3b92
│ │╎│╎╎│╎   0x00003b85      89f0           mov eax, esi
│ │╎│╎╎│╎   0x00003b87      c0e806         shr al, 6
│ │╎│╎╎│╎   0x00003b8a      83c030         add eax, 0x30
│ │╎│╎╎│╎   0x00003b8d      4388440101     mov byte [r9 + r8 + 1], al
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x3b83
│ ────────> 0x00003b92      498d4002       lea rax, [r8 + 2]
│ │╎│╎╎│╎   0x00003b96      4c39d8         cmp rax, r11
│ ────────< 0x00003b99      7310           jae 0x3bab
│ │╎│╎╎│╎   0x00003b9b      89f0           mov eax, esi
│ │╎│╎╎│╎   0x00003b9d      c0e803         shr al, 3
│ │╎│╎╎│╎   0x00003ba0      83e007         and eax, 7
│ │╎│╎╎│╎   0x00003ba3      83c030         add eax, 0x30
│ │╎│╎╎│╎   0x00003ba6      4388440102     mov byte [r9 + r8 + 2], al
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x3b99
│ ────────> 0x00003bab      83e607         and esi, 7
│ │╎│╎╎│╎   0x00003bae      4883c301       add rbx, 1
│ │╎│╎╎│╎   0x00003bb2      4983c003       add r8, 3
│ │╎│╎╎│╎   0x00003bb6      83c630         add esi, 0x30
│ │╎│╎╎│╎   0x00003bb9      4839cb         cmp rbx, rcx
│ ────────< 0x00003bbc      0f83d80f0000   jae 0x4b9a
│ │╎│╎╎│╎   0x00003bc2      89d7           mov edi, edx
│ │╎│╎╎│╎   ; CODE XREFS from fcn.00003610 @ 0x3c31, 0x4c65
│ ────────> 0x00003bc4      4d39d8         cmp r8, r11
│ ────────< 0x00003bc7      7304           jae 0x3bcd
│ │╎│╎╎│╎   0x00003bc9      43883401       mov byte [r9 + r8], sil
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x3bc7
│ ────────> 0x00003bcd      410fb6341e     movzx esi, byte [r14 + rbx]
│ │╎│╎╎│╎   0x00003bd2      4983c001       add r8, 1
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x3b20
│ ────────> 0x00003bd6      84d2           test dl, dl
│ ────────< 0x00003bd8      0f854affffff   jne 0x3b28
│ │╎│╎╎│╎   0x00003bde      89f8           mov eax, edi
│ │╎│╎╎│╎   0x00003be0      83f001         xor eax, 1
│ │╎│╎╎│╎   0x00003be3      4421d0         and eax, r10d
│ │╎│╎╎│╎   0x00003be6      4584e4         test r12b, r12b
│ ────────< 0x00003be9      740e           je 0x3bf9
│ │╎│╎╎│╎   0x00003beb      4d39d8         cmp r8, r11
│ ────────< 0x00003bee      7305           jae 0x3bf5
│ │╎│╎╎│╎   0x00003bf0      43c604015c     mov byte [r9 + r8], 0x5c    ; '\\'
│ │╎│╎╎│╎                                                              ; [0x5c:1]=0
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x3bee
│ ────────> 0x00003bf5      4983c001       add r8, 1
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x3be9
│ ────────> 0x00003bf9      4883c301       add rbx, 1
│ │╎│╎╎│╎   0x00003bfd      4839cb         cmp rbx, rcx
│ ────────< 0x00003c00      0f83400f0000   jae 0x4b46
│ │╎│╎╎│╎   0x00003c06      84c0           test al, al
│ ────────< 0x00003c08      0f8454100000   je 0x4c62
│ │╎│╎╎│╎   0x00003c0e      4d39d8         cmp r8, r11
│ ────────< 0x00003c11      7305           jae 0x3c18
│ │╎│╎╎│╎   0x00003c13      43c6040127     mov byte [r9 + r8], 0x27    ; '''
│ │╎│╎╎│╎                                                              ; [0x27:1]=0
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x3c11
│ ────────> 0x00003c18      498d4001       lea rax, [r8 + 1]
│ │╎│╎╎│╎   0x00003c1c      4c39d8         cmp rax, r11
│ ────────< 0x00003c1f      7306           jae 0x3c27
│ │╎│╎╎│╎   0x00003c21      43c644010127   mov byte [r9 + r8 + 1], 0x27 ; '''
│ │╎│╎╎│╎                                                              ; [0x27:1]=0
│ │╎│╎╎│╎   ; CODE XREF from fcn.00003610 @ 0x3c1f
│ ────────> 0x00003c27      4983c002       add r8, 2
│ │╎│╎╎│╎   0x00003c2b      4531e4         xor r12d, r12d
│ │╎│╎╎│╎   0x00003c2e      4531d2         xor r10d, r10d
│ ────────< 0x00003c31      eb91           jmp 0x3bc4
..
│ │╎│╎╎│╎   ;-- case 33...34:                                          ; from 0x0000390d
│ │╎│╎╎│╎   ;-- case 36:                                               ; from 0x0000390d
│ │╎│╎╎│╎   ;-- case 38:                                               ; from 0x0000390d
│ │╎│╎╎│╎   ;-- case 41...42:                                          ; from 0x0000390d
│ │╎│╎╎│╎   ;-- case 59:                                               ; from 0x0000390d
│ │╎│╎╎│╎   ;-- case 60...62:                                          ; from 0x0000390d
│ │╎│╎╎│╎   ; CODE XREFS from fcn.00003610 @ 0x390d, 0x44c3
│ ────────> 0x00003c38      4531d2         xor r10d, r10d
│ │╎│╎╎│╎   ; CODE XREFS from fcn.00003610 @ 0x3e51, 0x3e5b, 0x4b95
│ ────────> 0x00003c3b      837da402       cmp dword [var_5ch_3], 2
│ ────────< 0x00003c3f      0f85f0fcffff   jne case.0x390d.37
│ │╎│╎╎│╎   0x00003c45      807da300       cmp byte [var_5dh_3], 0
│ ────────< 0x00003c49      0f84e6fcffff   je case.0x390d.37
│ │╎│╎╎│╎   ; CODE XREFS from fcn.00003610 @ 0x3e7f, 0x4784
│ ────────> 0x00003c4f      c745a4020000.  mov dword [var_5ch_3], 2
│ │╎│╎╎│╎   ; XREFS: CODE 0x00003caa  CODE 0x00003db7  CODE 0x000044d7  
│ │╎│╎╎│╎   ; XREFS: CODE 0x00004814  CODE 0x000049e9  CODE 0x00004b88  
│ ────────> 0x00003c56      807da100       cmp byte [var_5fh_2], 0
│ │╎│╎╎│╎   0x00003c5a      b804000000     mov eax, 4
│ │╎│╎╎│╎   0x00003c5f      0f4445a4       cmove eax, dword [var_5ch_3]
│ │╎│╎╎│╎   0x00003c63      8945a4         mov dword [var_5ch_3], eax
│ │╎│╎╎│╎   ; CODE XREFS from fcn.00003610 @ 0x3d34, 0x4162, 0x4581, 0x4e23
│ ────────> 0x00003c66      83a544ffffff.  and dword [var_bch_2], 0xfffffffd ; [0xfffffffd:4]=-1 ; 4294967293
│ │╎│╎╎│╎   0x00003c6d      48c745800000.  mov qword [var_80h_3], 0
│ │╎│└────< 0x00003c75      e9f6faffff     jmp 0x3770
│ │╎│ ╎│╎   ;-- case 8:                                                ; from 0x0000390d
│ │╎│ ╎│╎   ; CODE XREF from fcn.00003610 @ 0x390d
│ │╎│ ╎│╎   0x00003c7a      837da402       cmp dword [var_5ch_3], 2
│ │╎│ ╎│╎   0x00003c7e      be08000000     mov esi, 8
│ │╎│ ╎│╎   0x00003c83      b862000000     mov eax, 0x62               ; 'b'
│ │╎│ ╎│╎   0x00003c88      0f94c2         sete dl
│ │╎│ ╎│╎   0x00003c8b      807da100       cmp byte [var_5fh_2], 0
│ ────────< 0x00003c8f      0f849dfcffff   je case.0x419a.33
│ │╎│ ╎│╎   0x00003c95      0f1f00         nop dword [rax]
│ │╎│ ╎│╎   ; CODE XREF from fcn.00003610 @ 0x392c
│ ────────> 0x00003c98      4531d2         xor r10d, r10d
│ │╎│ ╎│╎   0x00003c9b      807da300       cmp byte [var_5dh_3], 0
│ │╎│ ╎│╎   0x00003c9f      89c6           mov esi, eax
│ ────────< 0x00003ca1      0f84d2fcffff   je 0x3979
│ │╎│ ╎│╎   ; CODE XREF from fcn.00003610 @ 0x3973
│ ────────> 0x00003ca7      2055a1         and byte [var_5fh_2], dl
│ ────────< 0x00003caa      ebaa           jmp 0x3c56
│ │╎│ ╎│╎   ;-- case 11:                                               ; from 0x0000390d
│ │╎│ ╎│╎   ; CODE XREF from fcn.00003610 @ 0x390d
│ │╎│ ╎│╎   0x00003cac      837da402       cmp dword [var_5ch_3], 2
│ │╎│ ╎│╎   0x00003cb0      be0b000000     mov esi, 0xb
│ │╎│ ╎│╎   0x00003cb5      b876000000     mov eax, 0x76               ; 'v'
│ │╎│ ╎│╎   0x00003cba      0f94c2         sete dl
│ ────────< 0x00003cbd      e966fcffff     jmp 0x3928
│ │╎│ ╎│╎   ;-- case 63:                                               ; from 0x0000390d
│ │╎│ ╎│╎   ; CODE XREF from fcn.00003610 @ 0x390d
│ │╎│ ╎│╎   0x00003cc2      837da402       cmp dword [var_5ch_3], 2
│ │╎│┌────< 0x00003cc6      0f84440b0000   je 0x4810
│ │╎││╎│╎   ;-- case 63:                                               ; from 0x0000419a
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x419a
│ │╎││╎│╎   0x00003ccc      837da405       cmp dword [var_5ch_3], 5
│ ────────< 0x00003cd0      0f850a070000   jne 0x43e0
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x43d4
│ ────────> 0x00003cd6      f68544ffffff.  test byte [var_bch_2], 4
│ ────────< 0x00003cdd      0f84fd060000   je 0x43e0
│ │╎││╎│╎   0x00003ce3      488d4302       lea rax, [rbx + 2]
│ │╎││╎│╎   0x00003ce7      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x00003cea      be3f000000     mov esi, 0x3f               ; '?'
│ │╎││╎│╎   0x00003cef      4c39f0         cmp rax, r14
│ ────────< 0x00003cf2      0f833dfcffff   jae case.0x390d.37
│ │╎││╎│╎   0x00003cf8      488b5590       mov rdx, qword [s]
│ │╎││╎│╎   0x00003cfc      807c1a013f     cmp byte [rdx + rbx + 1], 0x3f
│ ────────< 0x00003d01      0f852efcffff   jne case.0x390d.37
│ │╎││╎│╎   0x00003d07      0fb63402       movzx esi, byte [rdx + rax]
│ │╎││╎│╎   0x00003d0b      4080fe3e       cmp sil, 0x3e
│ ────────< 0x00003d0f      0f87b9100000   ja 0x4dce
│ │╎││╎│╎   0x00003d15      48ba00000000.  movabs rdx, 0x7000a38200000000 ; 8070630310989004800
│ │╎││╎│╎   0x00003d1f      480fa3f2       bt rdx, rsi
│ │╎││╎│╎   0x00003d23      410f92c2       setb r10b
│ │╎││╎│╎   0x00003d27      4584d2         test r10b, r10b
│ ────────< 0x00003d2a      0f849e100000   je 0x4dce
│ │╎││╎│╎   0x00003d30      807da300       cmp byte [var_5dh_3], 0
│ ────────< 0x00003d34      0f852cffffff   jne 0x3c66
│ │╎││╎│╎   0x00003d3a      488b5da8       mov rbx, qword [var_70h_2]
│ │╎││╎│╎   0x00003d3e      4c39db         cmp rbx, r11
│ ────────< 0x00003d41      7305           jae 0x3d48
│ │╎││╎│╎   0x00003d43      41c604193f     mov byte [r9 + rbx], 0x3f   ; '?'
│ │╎││╎│╎                                                              ; [0x3f:1]=0
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x3d41
│ ────────> 0x00003d48      488b5da8       mov rbx, qword [var_70h_2]
│ │╎││╎│╎   0x00003d4c      488d5301       lea rdx, [rbx + 1]
│ │╎││╎│╎   0x00003d50      4c39da         cmp rdx, r11
│ ────────< 0x00003d53      7306           jae 0x3d5b
│ │╎││╎│╎   0x00003d55      41c644190122   mov byte [r9 + rbx + 1], 0x22 ; '\"'
│ │╎││╎│╎                                                              ; [0x22:1]=0
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x3d53
│ ────────> 0x00003d5b      488b5da8       mov rbx, qword [var_70h_2]
│ │╎││╎│╎   0x00003d5f      488d5302       lea rdx, [rbx + 2]
│ │╎││╎│╎   0x00003d63      4c39da         cmp rdx, r11
│ ────────< 0x00003d66      7306           jae 0x3d6e
│ │╎││╎│╎   0x00003d68      41c644190222   mov byte [r9 + rbx + 2], 0x22 ; '\"'
│ │╎││╎│╎                                                              ; [0x22:1]=0
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x3d66
│ ────────> 0x00003d6e      488b5da8       mov rbx, qword [var_70h_2]
│ │╎││╎│╎   0x00003d72      488d5303       lea rdx, [rbx + 3]
│ │╎││╎│╎   0x00003d76      4c39da         cmp rdx, r11
│ ────────< 0x00003d79      7306           jae 0x3d81
│ │╎││╎│╎   0x00003d7b      41c64419033f   mov byte [r9 + rbx + 3], 0x3f ; '?'
│ │╎││╎│╎                                                              ; [0x3f:1]=0
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x3d79
│ ────────> 0x00003d81      4889c3         mov rbx, rax
│ │╎││╎│╎   0x00003d84      488345a804     add qword [var_70h_2], 4
│ │╎││╎│╎   0x00003d89      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x00003d8c      4489c0         mov eax, r8d
│ │╎││╎│╎   0x00003d8f      0a45a3         or al, byte [var_5dh_3]
│ ────────< 0x00003d92      0f85a9fbffff   jne 0x3941
│ ────────< 0x00003d98      e97bfcffff     jmp 0x3a18
..
│ │╎││╎│╎   ;-- case 39:                                               ; from 0x0000390d
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x390d
│ │╎││╎│╎   0x00003da0      837da402       cmp dword [var_5ch_3], 2
│ │╎││╎│╎   0x00003da4      448855a0       mov byte [var_78h], r10b
│ │╎││╎│╎   0x00003da8      be27000000     mov esi, 0x27               ; '''
│ ────────< 0x00003dad      0f8582fbffff   jne case.0x390d.37
│ │╎││╎│╎   0x00003db3      807da300       cmp byte [var_5dh_3], 0
│ ────────< 0x00003db7      0f8599feffff   jne 0x3c56
│ │╎││╎│╎   0x00003dbd      4d85db         test r11, r11
│ ────────< 0x00003dc0      0f84300d0000   je 0x4af6
│ │╎││╎│╎   0x00003dc6      31d2           xor edx, edx
│ │╎││╎│╎   0x00003dc8      4883bd38ffff.  cmp qword [var_c8h_2], 0
│ ────────< 0x00003dd0      0f85200d0000   jne 0x4af6
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4b38
│ ────────> 0x00003dd6      4c899d38ffff.  mov qword [var_c8h_2], r11
│ │╎││╎│╎   0x00003ddd      31c0           xor eax, eax
│ │╎││╎│╎   0x00003ddf      4989d3         mov r11, rdx
│ │╎││╎│╎   0x00003de2      be27000000     mov esi, 0x27               ; '''
│ │╎││╎│╎   0x00003de7      488345a803     add qword [var_70h_2], 3
│ │╎││╎│╎   0x00003dec      448855a0       mov byte [var_78h], r10b
│ │╎││╎│╎   0x00003df0      c645a200       mov byte [var_5eh_2], 0
│ ────────< 0x00003df4      e92ffcffff     jmp 0x3a28
│ │╎││╎│╎   ;-- case 7:                                                ; from 0x0000390d
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x390d
│ │╎││╎│╎   0x00003df9      837da402       cmp dword [var_5ch_3], 2
│ │╎││╎│╎   0x00003dfd      be07000000     mov esi, 7
│ │╎││╎│╎   0x00003e02      b861000000     mov eax, 0x61               ; 'a'
│ │╎││╎│╎   0x00003e07      0f94c2         sete dl
│ ────────< 0x00003e0a      e919fbffff     jmp 0x3928
│ │╎││╎│╎   ;-- case 0:                                                ; from 0x0000390d
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x390d
│ │╎││╎│╎   0x00003e0f      807da100       cmp byte [var_5fh_2], 0
│ ────────< 0x00003e13      0f8507050000   jne case.0x42f2.0
│ │╎││╎│╎   0x00003e19      f68544ffffff.  test byte [var_bch_2], 1
│ ────────< 0x00003e20      0f85170d0000   jne 0x4b3d
│ │╎││╎│╎   0x00003e26      4531e4         xor r12d, r12d
│ │╎││╎│╎   0x00003e29      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x00003e2c      31f6           xor esi, esi
│ │╎││╎│╎   0x00003e2e      4489c0         mov eax, r8d
│ │╎││╎│╎   0x00003e31      0a45a3         or al, byte [var_5dh_3]
│ ────────< 0x00003e34      0f8507fbffff   jne 0x3941
│ ────────< 0x00003e3a      e9d9fbffff     jmp 0x3a18
│ │╎││╎│╎   ;-- case 35:                                               ; from 0x0000390d
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x390d, 0x419a
│ │╎││╎│╎   0x00003e3f      be23000000     mov esi, 0x23               ; '#'
│ │╎││╎│╎   0x00003e44      0f1f4000       nop dword [rax]
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x43b9, 0x4522, 0x4594, 0x47d6
│ ────────> 0x00003e48      4885db         test rbx, rbx
│ ────────< 0x00003e4b      0f85e1faffff   jne case.0x419a.33
│ ────────< 0x00003e51      e9e5fdffff     jmp 0x3c3b
│ │╎││╎│╎   ;-- case 32:                                               ; from 0x0000390d
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x390d
│ │╎││╎│╎   0x00003e56      be20000000     mov esi, 0x20               ; "@"
│ ────────< 0x00003e5b      e9dbfdffff     jmp 0x3c3b
│ │╎││╎│╎   ;-- case 9:                                                ; from 0x0000390d
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x390d
│ │╎││╎│╎   0x00003e60      be09000000     mov esi, 9
│ │╎││╎│╎   0x00003e65      b874000000     mov eax, 0x74               ; 't'
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x3e8e, 0x3e9a
│ ────────> 0x00003e6a      837da402       cmp dword [var_5ch_3], 2
│ │╎││╎│╎   0x00003e6e      440fb665a3     movzx r12d, byte [var_5dh_3]
│ │╎││╎│╎   0x00003e73      0f94c2         sete dl
│ │╎││╎│╎   0x00003e76      4120d4         and r12b, dl
│ ────────< 0x00003e79      0f84a9faffff   je 0x3928
│ ────────< 0x00003e7f      e9cbfdffff     jmp 0x3c4f
│ │╎││╎│╎   ;-- case 13:                                               ; from 0x0000390d
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x390d
│ │╎││╎│╎   0x00003e84      be0d000000     mov esi, 0xd
│ │╎││╎│╎   0x00003e89      b872000000     mov eax, 0x72               ; 'r'
│ ────────< 0x00003e8e      ebda           jmp 0x3e6a
│ │╎││╎│╎   ;-- case 10:                                               ; from 0x0000390d
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x390d
│ │╎││╎│╎   0x00003e90      be0a000000     mov esi, 0xa
│ │╎││╎│╎   0x00003e95      b86e000000     mov eax, 0x6e               ; 'n'
│ ────────< 0x00003e9a      ebce           jmp 0x3e6a
│ │╎││╎│╎   ;-- case 7:                                                ; from 0x000037b3
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x37b3
│ │╎││╎│╎   0x00003e9c      c6459801       mov byte [var_80h_2], 1
│ │╎││╎│╎   0x00003ea0      c645a000       mov byte [var_78h], 0
│ │╎││╎│╎   0x00003ea4      c645a200       mov byte [var_5eh_2], 0
│ │╎││╎│╎   0x00003ea8      48c78538ffff.  mov qword [var_c8h_2], 0
│ │╎││╎│╎   0x00003eb3      c645a300       mov byte [var_5dh_3], 0
│ │╎││╎│╎   0x00003eb7      c645a101       mov byte [var_5fh_2], 1
│ │╎││╎│╎   0x00003ebb      48c745880000.  mov qword [n], 0
│ │╎││╎│╎   0x00003ec3      48c78548ffff.  mov qword [s2], 0
│ │╎││╎│╎   0x00003ece      48c745a80000.  mov qword [var_70h_2], 0
│ ────────< 0x00003ed6      e9adf9ffff     jmp 0x3888
│ │╎││╎│╎   ;-- case 4:                                                ; from 0x000037b3
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x37b3
│ │╎││╎│╎   0x00003edb      c6459801       mov byte [var_80h_2], 1
│ │╎││╎│╎   0x00003edf      85db           test ebx, ebx
│ ────────< 0x00003ee1      0f852e010000   jne 0x4015
│ │╎││╎│╎   0x00003ee7      c645a200       mov byte [var_5eh_2], 0
│ │╎││╎│╎   0x00003eeb      31c0           xor eax, eax
│ │╎││╎│╎   0x00003eed      48c78538ffff.  mov qword [var_c8h_2], 0
│ │╎││╎│╎   0x00003ef8      c645a101       mov byte [var_5fh_2], 1
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x47be, 0x4edc
│ ────────> 0x00003efc      4d85db         test r11, r11
│ ────────< 0x00003eff      7404           je 0x3f05
│ │╎││╎│╎   0x00003f01      41c60127       mov byte [r9], 0x27         ; '''
│ │╎││╎│╎                                                              ; [0x27:1]=0
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x3eff
│ ────────> 0x00003f05      8845a0         mov byte [var_78h], al
│ │╎││╎│╎   0x00003f08      488d05752600.  lea rax, [0x00006584]       ; "'"
│ │╎││╎│╎   0x00003f0f      c645a300       mov byte [var_5dh_3], 0
│ │╎││╎│╎   0x00003f13      48c745880100.  mov qword [n], 1
│ │╎││╎│╎   0x00003f1b      48898548ffff.  mov qword [s2], rax
│ │╎││╎│╎   0x00003f22      48c745a80100.  mov qword [var_70h_2], 1
│ │╎││╎│╎   0x00003f2a      c745a4020000.  mov dword [var_5ch_3], 2
│ ────────< 0x00003f31      e952f9ffff     jmp 0x3888
│ │╎││╎│╎   ;-- case 0:                                                ; from 0x000037b3
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x37b3
│ │╎││╎│╎   0x00003f36      c6459801       mov byte [var_68h_2], 1
│ │╎││╎│╎   0x00003f3a      c645a000       mov byte [var_60h], 0
│ │╎││╎│╎   0x00003f3e      c645a200       mov byte [var_5eh], 0
│ │╎││╎│╎   0x00003f42      48c78538ffff.  mov qword [var_c8h], 0
│ │╎││╎│╎   0x00003f4d      c645a300       mov byte [var_5dh_2], 0
│ │╎││╎│╎   0x00003f51      c645a100       mov byte [var_5fh], 0
│ │╎││╎│╎   0x00003f55      48c745880000.  mov qword [var_78h], 0
│ │╎││╎│╎   0x00003f5d      48c78548ffff.  mov qword [var_b8h], 0
│ │╎││╎│╎   0x00003f68      48c745a80000.  mov qword [var_58h_2], 0
│ ────────< 0x00003f70      e913f9ffff     jmp 0x3888
│ │╎││╎│╎   ;-- case 5:                                                ; from 0x000037b3
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x37b3
│ │╎││╎│╎   0x00003f75      85db           test ebx, ebx
│ ────────< 0x00003f77      0f85830d0000   jne 0x4d00
│ │╎││╎│╎   0x00003f7d      4d85db         test r11, r11
│ ────────< 0x00003f80      7404           je 0x3f86
│ │╎││╎│╎   0x00003f82      41c60122       mov byte [r9], 0x22         ; '\"'
│ │╎││╎│╎                                                              ; [0x22:1]=0
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x3f80
│ ────────> 0x00003f86      488d05f52500.  lea rax, [0x00006582]       ; u"\"'\u07a1e\u80e2\x98\u4247\u3831\u33300\u656d\u6f6d\u7972\u6520\u6878\u7561\u7473\u6465\u2500s\u4f50\u4953X`\u7277\u7469\u2065\u7265\u6f72r\u4e47\u2055\u6f63\u6572\u7475\u6c69s\u6365\u6f68\u2500\u2073\u2528\u2973\u2520\u0a73\u2800\u2943\u5700\u6972\u7474\u6e65\u6220\u2079\u7325\u0a2e\u5700\u6972\u7474\u6e65\u6220\u2079\u7325\u6120"
│ │╎││╎│╎   0x00003f8d      c6459801       mov byte [var_80h_2], 1
│ │╎││╎│╎   0x00003f91      c645a000       mov byte [var_78h], 0
│ │╎││╎│╎   0x00003f95      c645a200       mov byte [var_5eh_2], 0
│ │╎││╎│╎   0x00003f99      48c78538ffff.  mov qword [var_c8h_2], 0
│ │╎││╎│╎   0x00003fa4      c645a300       mov byte [var_5dh_3], 0
│ │╎││╎│╎   0x00003fa8      c645a101       mov byte [var_5fh_2], 1
│ │╎││╎│╎   0x00003fac      48c745880100.  mov qword [n], 1
│ │╎││╎│╎   0x00003fb4      48898548ffff.  mov qword [s2], rax
│ │╎││╎│╎   0x00003fbb      48c745a80100.  mov qword [var_70h_2], 1
│ ────────< 0x00003fc3      e9c0f8ffff     jmp 0x3888
│ │╎││╎│╎   ;-- case 6:                                                ; from 0x000037b3
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x37b3
│ │╎││╎│╎   0x00003fc8      488d05b32500.  lea rax, [0x00006582]       ; u"\"'\u07a1e\u80e2\x98\u4247\u3831\u33300\u656d\u6f6d\u7972\u6520\u6878\u7561\u7473\u6465\u2500s\u4f50\u4953X`\u7277\u7469\u2065\u7265\u6f72r\u4e47\u2055\u6f63\u6572\u7475\u6c69s\u6365\u6f68\u2500\u2073\u2528\u2973\u2520\u0a73\u2800\u2943\u5700\u6972\u7474\u6e65\u6220\u2079\u7325\u0a2e\u5700\u6972\u7474\u6e65\u6220\u2079\u7325\u6120"
│ │╎││╎│╎   0x00003fcf      c6459801       mov byte [var_80h_2], 1
│ │╎││╎│╎   0x00003fd3      c645a000       mov byte [var_78h], 0
│ │╎││╎│╎   0x00003fd7      c645a200       mov byte [var_5eh_2], 0
│ │╎││╎│╎   0x00003fdb      48c78538ffff.  mov qword [var_c8h_2], 0
│ │╎││╎│╎   0x00003fe6      c645a301       mov byte [var_5dh_3], 1
│ │╎││╎│╎   0x00003fea      c645a101       mov byte [var_5fh_2], 1
│ │╎││╎│╎   0x00003fee      48c745880100.  mov qword [n], 1
│ │╎││╎│╎   0x00003ff6      48898548ffff.  mov qword [s2], rax
│ │╎││╎│╎   0x00003ffd      48c745a80000.  mov qword [var_70h_2], 0
│ │╎││╎│╎   0x00004005      c745a4050000.  mov dword [var_5ch_3], 5
│ ────────< 0x0000400c      e977f8ffff     jmp 0x3888
│ │╎││╎│╎   ;-- case 1:                                                ; from 0x000037b3
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x37b3
│ │╎││╎│╎   0x00004011      c6459801       mov byte [var_80h_2], 1
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x3ee1
│ ────────> 0x00004015      c645a000       mov byte [var_78h], 0
│ │╎││╎│╎   0x00004019      c645a200       mov byte [var_5eh_2], 0
│ │╎││╎│╎   0x0000401d      48c78538ffff.  mov qword [var_c8h_2], 0
│ │╎││╎│╎   0x00004028      c645a301       mov byte [var_5dh_3], 1
│ │╎││╎│╎   0x0000402c      c645a100       mov byte [var_5fh_2], 0
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4079
│ ────────> 0x00004030      488d054d2500.  lea rax, [0x00006584]       ; "'"
│ │╎││╎│╎   0x00004037      48c745880100.  mov qword [n], 1
│ │╎││╎│╎   0x0000403f      48898548ffff.  mov qword [s2], rax
│ │╎││╎│╎   0x00004046      48c745a80000.  mov qword [var_70h_2], 0
│ │╎││╎│╎   0x0000404e      c745a4020000.  mov dword [var_5ch_3], 2
│ ────────< 0x00004055      e92ef8ffff     jmp 0x3888
│ │╎││╎│╎   ;-- case 3:                                                ; from 0x000037b3
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x37b3
│ │╎││╎│╎   0x0000405a      c6459801       mov byte [var_80h_2], 1
│ │╎││╎│╎   0x0000405e      c645a000       mov byte [var_78h], 0
│ │╎││╎│╎   0x00004062      c645a200       mov byte [var_5eh_2], 0
│ │╎││╎│╎   0x00004066      48c78538ffff.  mov qword [var_c8h_2], 0
│ │╎││╎│╎   0x00004071      c645a301       mov byte [var_5dh_3], 1
│ │╎││╎│╎   0x00004075      c645a101       mov byte [var_5fh_2], 1
│ │╎││╎│╎   ; DATA XREF from fcn.00003610 @ 0x25c3
│ ────────< 0x00004079      ebb5           jmp 0x4030
..
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x38d5
│ ────────> 0x00004080      488b4588       mov rax, qword [n]
│ │╎││╎│╎   0x00004084      488d1418       lea rdx, [rax + rbx]
│ │╎││╎│╎   0x00004088      4983feff       cmp r14, 0xffffffffffffffff
│ ────────< 0x0000408c      7564           jne 0x40f2
│ │╎││╎│╎   0x0000408e      4883f801       cmp rax, 1
│ ────────< 0x00004092      765e           jbe 0x40f2
│ │╎││╎│╎   0x00004094      4c899d50ffff.  mov qword [var_c8h], r11
│ │╎││╎│╎   0x0000409b      4c898d58ffff.  mov qword [s1], r9
│ │╎││╎│╎   0x000040a2      48898d60ffff.  mov qword [var_b8h], rcx
│ │╎││╎│╎   0x000040a9      44889568ffff.  mov byte [var_b0h], r10b
│ │╎││╎│╎   0x000040b0      48899570ffff.  mov qword [var_90h_2], rdx
│ │╎││╎│╎   0x000040b7      44888578ffff.  mov byte [ps], r8b
│ │╎││╎│╎   0x000040be      e86de2ffff     call sym.imp.strlen         ; size_t strlen(const char *s)
│ │╎││╎│╎   0x000040c3      4c8b9d50ffff.  mov r11, qword [var_c8h]
│ │╎││╎│╎   ; DATA XREFS from fcn.00003610 @ 0x2620, 0x4f40
│ │╎││╎│╎   0x000040ca      4c8b8d58ffff.  mov r9, qword [s1]
│ │╎││╎│╎   0x000040d1      488b8d60ffff.  mov rcx, qword [var_b8h]
│ │╎││╎│╎   0x000040d8      440fb69568ff.  movzx r10d, byte [var_b0h]
│ │╎││╎│╎   0x000040e0      4989c6         mov r14, rax
│ │╎││╎│╎   0x000040e3      488b9570ffff.  mov rdx, qword [var_90h_2]
│ │╎││╎│╎   0x000040ea      440fb68578ff.  movzx r8d, byte [ps]
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x408c, 0x4092
│ ────────> 0x000040f2      4939d6         cmp r14, rdx
│ ────────< 0x000040f5      0f82c5010000   jb 0x42c0
│ │╎││╎│╎   0x000040fb      488b5588       mov rdx, qword [n]          ; size_t n
│ │╎││╎│╎   0x000040ff      488bb548ffff.  mov rsi, qword [s2]         ; const void *s2
│ │╎││╎│╎   0x00004106      4889cf         mov rdi, rcx                ; const void *s1
│ │╎││╎│╎   ; DATA XREF from fcn.00003610 @ 0x2524
│ │╎││╎│╎   0x00004109      4c899d58ffff.  mov qword [s1], r11
│ │╎││╎│╎   0x00004110      4c898d60ffff.  mov qword [var_b8h], r9
│ │╎││╎│╎   0x00004117      44889568ffff.  mov byte [var_b0h], r10b
│ │╎││╎│╎   0x0000411e      44888570ffff.  mov byte [var_90h_2], r8b
│ │╎││╎│╎   0x00004125      48898d78ffff.  mov qword [ps], rcx
│ │╎││╎│╎   0x0000412c      e85fe2ffff     call sym.imp.memcmp         ; int memcmp(const void *s1, const void *s2, size_t n)
│ │╎││╎│╎   0x00004131      488b8d78ffff.  mov rcx, qword [ps]
│ │╎││╎│╎   0x00004138      440fb68570ff.  movzx r8d, byte [var_90h_2]
│ │╎││╎│╎   0x00004140      85c0           test eax, eax
│ │╎││╎│╎   0x00004142      440fb69568ff.  movzx r10d, byte [var_b0h]
│ │╎││╎│╎   0x0000414a      4c8b8d60ffff.  mov r9, qword [var_b8h]
│ │╎││╎│╎   0x00004151      4c8b9d58ffff.  mov r11, qword [s1]
│ ────────< 0x00004158      0f8562010000   jne 0x42c0
│ │╎││╎│╎   0x0000415e      807da300       cmp byte [var_5dh_3], 0
│ ────────< 0x00004162      0f85fefaffff   jne 0x3c66
│ │╎││╎│╎   0x00004168      0fb631         movzx esi, byte [rcx]
│ │╎││╎│╎   0x0000416b      4080fe3f       cmp sil, 0x3f
│ ────────< 0x0000416f      0f8fbb060000   jg 0x4830
│ │╎││╎│╎   0x00004175      4084f6         test sil, sil
│ ────────< 0x00004178      0f88f2f8ffff   js case.0x419a.1
│ │╎││╎│╎   0x0000417e      4080fe3f       cmp sil, 0x3f
│ ────────< 0x00004182      0f87e8f8ffff   ja case.0x419a.1
│ │╎││╎│╎   0x00004188      488d15552000.  lea rdx, [0x000061e4]
│ │╎││╎│╎   0x0000418f      400fb6c6       movzx eax, sil
│ │╎││╎│╎   0x00004193      48630482       movsxd rax, dword [rdx + rax*4]
│ │╎││╎│╎   0x00004197      4801d0         add rax, rdx
│ │╎││╎│╎   ;-- switch
│ │╎││╎│╎   0x0000419a      3effe0         jmp rax                     ; switch table (64 cases) at 0x61e4
..
│ │╎││╎│╎   ;-- case 37:                                               ; from 0x0000419a
│ │╎││╎│╎   ;-- case 44...58:                                          ; from 0x0000419a
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x419a
│ │╎││╎│╎   0x000041a0      4589e2         mov r10d, r12d
│ │╎││╎│╎   0x000041a3      4489c0         mov eax, r8d
│ │╎││╎│╎   0x000041a6      0a45a3         or al, byte [var_5dh_3]
│ ────────< 0x000041a9      0f8592f7ffff   jne 0x3941
│ ────────< 0x000041af      e964f8ffff     jmp 0x3a18
│ │╎││╎│╎   ;-- case 10:                                               ; from 0x0000419a
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x419a
│ │╎││╎│╎   0x000041b4      31d2           xor edx, edx
│ │╎││╎│╎   0x000041b6      be0a000000     mov esi, 0xa
│ │╎││╎│╎   0x000041bb      b86e000000     mov eax, 0x6e               ; 'n'
│ ────────< 0x000041c0      e963f7ffff     jmp 0x3928
│ │╎││╎│╎   ;-- case 7:                                                ; from 0x0000419a
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x419a
│ │╎││╎│╎   0x000041c5      31d2           xor edx, edx
│ │╎││╎│╎   0x000041c7      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x000041ca      be61000000     mov esi, 0x61               ; 'a'
│ ────────< 0x000041cf      e9a5f7ffff     jmp 0x3979
│ │╎││╎│╎   ;-- case 0:                                                ; from 0x0000419a
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x419a
│ │╎││╎│╎   0x000041d4      488b45a8       mov rax, qword [var_70h_2]
│ │╎││╎│╎   0x000041d8      488d4801       lea rcx, [rax + 1]
│ │╎││╎│╎   0x000041dc      4489e0         mov eax, r12d
│ │╎││╎│╎   0x000041df      90             nop
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4342
│ ────────> 0x000041e0      488b75a8       mov rsi, qword [var_70h_2]
│ │╎││╎│╎   0x000041e4      4c39de         cmp rsi, r11
│ ────────< 0x000041e7      7305           jae 0x41ee
│ │╎││╎│╎   0x000041e9      41c604315c     mov byte [r9 + rsi], 0x5c   ; '\\'
│ │╎││╎│╎                                                              ; [0x5c:1]=0
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x41e7
│ ────────> 0x000041ee      4584c0         test r8b, r8b
│ ────────< 0x000041f1      0f8409f8ffff   je 0x3a00
│ │╎││╎│╎   0x000041f7      488d5301       lea rdx, [rbx + 1]
│ │╎││╎│╎   0x000041fb      4c39f2         cmp rdx, r14
│ ────────< 0x000041fe      731c           jae 0x421c
│ │╎││╎│╎   0x00004200      488b7590       mov rsi, qword [s]
│ │╎││╎│╎   0x00004204      0fb6741e01     movzx esi, byte [rsi + rbx + 1]
│ │╎││╎│╎   0x00004209      8d56d0         lea edx, [rsi - 0x30]
│ │╎││╎│╎   0x0000420c      4088b578ffff.  mov byte [ps], sil
│ │╎││╎│╎   0x00004213      80fa09         cmp dl, 9
│ ────────< 0x00004216      0f86690a0000   jbe 0x4c85
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x41fe, 0x4caa
│ ────────> 0x0000421c      4189c4         mov r12d, eax
│ │╎││╎│╎   0x0000421f      48894da8       mov qword [var_70h_2], rcx
│ │╎││╎│╎   0x00004223      4489d0         mov eax, r10d
│ │╎││╎│╎   0x00004226      be30000000     mov esi, 0x30               ; '0'
│ │╎││╎│╎   0x0000422b      4531d2         xor r10d, r10d
│ ────────< 0x0000422e      e910f7ffff     jmp 0x3943
│ │╎││╎│╎   ;-- case 9:                                                ; from 0x0000419a
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x419a
│ │╎││╎│╎   0x00004233      31d2           xor edx, edx
│ │╎││╎│╎   0x00004235      be09000000     mov esi, 9
│ │╎││╎│╎   0x0000423a      b874000000     mov eax, 0x74               ; 't'
│ ────────< 0x0000423f      e9e4f6ffff     jmp 0x3928
│ │╎││╎│╎   ;-- case 8:                                                ; from 0x0000419a
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x419a
│ │╎││╎│╎   0x00004244      31d2           xor edx, edx
│ │╎││╎│╎   0x00004246      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x00004249      be62000000     mov esi, 0x62               ; 'b'
│ ────────< 0x0000424e      e926f7ffff     jmp 0x3979
│ │╎││╎│╎   ;-- case 32:                                               ; from 0x0000419a
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x419a
│ │╎││╎│╎   0x00004253      4589e2         mov r10d, r12d
│ │╎││╎│╎   0x00004256      be20000000     mov esi, 0x20               ; "@"
│ │╎││╎│╎   0x0000425b      4489c0         mov eax, r8d
│ │╎││╎│╎   0x0000425e      0a45a3         or al, byte [var_5dh_3]
│ ────────< 0x00004261      0f85daf6ffff   jne 0x3941
│ ────────< 0x00004267      e9acf7ffff     jmp 0x3a18
│ │╎││╎│╎   ;-- case 11:                                               ; from 0x0000419a
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x419a
│ │╎││╎│╎   0x0000426c      31d2           xor edx, edx
│ │╎││╎│╎   0x0000426e      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x00004271      be76000000     mov esi, 0x76               ; 'v'
│ ────────< 0x00004276      e9fef6ffff     jmp 0x3979
│ │╎││╎│╎   ;-- case 13:                                               ; from 0x0000419a
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x419a
│ │╎││╎│╎   0x0000427b      31d2           xor edx, edx
│ │╎││╎│╎   0x0000427d      be0d000000     mov esi, 0xd
│ │╎││╎│╎   0x00004282      b872000000     mov eax, 0x72               ; 'r'
│ ────────< 0x00004287      e99cf6ffff     jmp 0x3928
│ │╎││╎│╎   ;-- case 12:                                               ; from 0x0000419a
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x419a
│ │╎││╎│╎   0x0000428c      31d2           xor edx, edx
│ │╎││╎│╎   0x0000428e      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x00004291      be66000000     mov esi, 0x66               ; 'f'
│ ────────< 0x00004296      e9def6ffff     jmp 0x3979
│ │╎││╎│╎   ;-- case 39:                                               ; from 0x0000419a
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x419a
│ │╎││╎│╎   0x0000429b      448865a0       mov byte [var_78h], r12b
│ │╎││╎│╎   0x0000429f      4589e2         mov r10d, r12d
│ │╎││╎│╎   0x000042a2      be27000000     mov esi, 0x27               ; '''
│ │╎││╎│╎   0x000042a7      4489c0         mov eax, r8d
│ │╎││╎│╎   0x000042aa      0a45a3         or al, byte [var_5dh_3]
│ ────────< 0x000042ad      0f858ef6ffff   jne 0x3941
│ ────────< 0x000042b3      e960f7ffff     jmp 0x3a18
..
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x40f5, 0x4158
│ ────────> 0x000042c0      0fb631         movzx esi, byte [rcx]
│ │╎││╎│╎   0x000042c3      4080fe3f       cmp sil, 0x3f
│ ────────< 0x000042c7      0f8f63020000   jg 0x4530
│ │╎││╎│╎   0x000042cd      4084f6         test sil, sil
│ ────────< 0x000042d0      0f8892f7ffff   js case.0x42f2.1
│ │╎││╎│╎   0x000042d6      4080fe3f       cmp sil, 0x3f
│ ────────< 0x000042da      0f8788f7ffff   ja case.0x42f2.1
│ │╎││╎│╎   0x000042e0      488d15fd1f00.  lea rdx, [0x000062e4]
│ │╎││╎│╎   0x000042e7      400fb6c6       movzx eax, sil
│ │╎││╎│╎   0x000042eb      48630482       movsxd rax, dword [rdx + rax*4]
│ │╎││╎│╎   0x000042ef      4801d0         add rax, rdx
│ │╎││╎│╎   ;-- switch
│ │╎││╎│╎   0x000042f2      3effe0         jmp rax                     ; switch table (64 cases) at 0x62e4
..
│ │╎││╎│╎   ;-- case 37:                                               ; from 0x000042f2
│ │╎││╎│╎   ;-- case 44...58:                                          ; from 0x000042f2
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x42f2
│ │╎││╎│╎   0x000042f8      4589e2         mov r10d, r12d
│ │╎││╎│╎   0x000042fb      4489c0         mov eax, r8d
│ │╎││╎│╎   0x000042fe      4531e4         xor r12d, r12d
│ │╎││╎│╎   0x00004301      0a45a3         or al, byte [var_5dh_3]
│ ────────< 0x00004304      0f8537f6ffff   jne 0x3941
│ ────────< 0x0000430a      e909f7ffff     jmp 0x3a18
..
│ │╎││╎│╎   ;-- case 33...34:                                          ; from 0x000042f2
│ │╎││╎│╎   ;-- case 36:                                               ; from 0x000042f2
│ │╎││╎│╎   ;-- case 38:                                               ; from 0x000042f2
│ │╎││╎│╎   ;-- case 41...42:                                          ; from 0x000042f2
│ │╎││╎│╎   ;-- case 59:                                               ; from 0x000042f2
│ │╎││╎│╎   ;-- case 60...62:                                          ; from 0x000042f2
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x42f2, 0x4567
│ ────────> 0x00004310      4531e4         xor r12d, r12d
│ ────────< 0x00004313      e91af6ffff     jmp case.0x419a.33
..
│ │╎││╎│╎   ;-- case 0:                                                ; from 0x000042f2
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x3e13, 0x42f2
│ ────────> 0x00004320      807da300       cmp byte [var_5dh_3], 0
│ ────────< 0x00004324      0f85e80a0000   jne 0x4e12
│ │╎││╎│╎   0x0000432a      0fb655a2       movzx edx, byte [var_5eh_2]
│ │╎││╎│╎   0x0000432e      837da402       cmp dword [var_5ch_3], 2
│ │╎││╎│╎   0x00004332      488b75a8       mov rsi, qword [var_70h_2]
│ │╎││╎│╎   0x00004336      0f94c0         sete al
│ │╎││╎│╎   0x00004339      83f201         xor edx, 1
│ │╎││╎│╎   0x0000433c      488d4e01       lea rcx, [rsi + 1]
│ │╎││╎│╎   0x00004340      20d0           and al, dl
│ ────────< 0x00004342      0f8498feffff   je 0x41e0
│ │╎││╎│╎   0x00004348      4c39de         cmp rsi, r11
│ ────────< 0x0000434b      7305           jae 0x4352
│ │╎││╎│╎   0x0000434d      41c6043127     mov byte [r9 + rsi], 0x27   ; '''
│ │╎││╎│╎                                                              ; [0x27:1]=0
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x434b
│ ────────> 0x00004352      4c39d9         cmp rcx, r11
│ ────────< 0x00004355      7305           jae 0x435c
│ │╎││╎│╎   0x00004357      41c6040924     mov byte [r9 + rcx], 0x24   ; '$'
│ │╎││╎│╎                                                              ; [0x24:1]=0
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4355
│ ────────> 0x0000435c      488b75a8       mov rsi, qword [var_70h_2]
│ │╎││╎│╎   0x00004360      488d5602       lea rdx, [rsi + 2]
│ │╎││╎│╎   0x00004364      4c39da         cmp rdx, r11
│ ────────< 0x00004367      7306           jae 0x436f
│ │╎││╎│╎   0x00004369      41c644310227   mov byte [r9 + rsi + 2], 0x27 ; '''
│ │╎││╎│╎                                                              ; [0x27:1]=0
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4367
│ ────────> 0x0000436f      488b75a8       mov rsi, qword [var_70h_2]
│ │╎││╎│╎   0x00004373      488d5603       lea rdx, [rsi + 3]
│ │╎││╎│╎   0x00004377      4883c604       add rsi, 4
│ │╎││╎│╎   0x0000437b      488975a8       mov qword [var_70h_2], rsi
│ │╎││╎│╎   0x0000437f      4c39da         cmp rdx, r11
│ ────────< 0x00004382      0f8375080000   jae 0x4bfd
│ │╎││╎│╎   0x00004388      41c604115c     mov byte [r9 + rdx], 0x5c   ; '\\'
│ │╎││╎│╎                                                              ; [0x5c:1]=0
│ │╎││╎│╎   0x0000438d      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x00004390      be30000000     mov esi, 0x30               ; '0'
│ │╎││╎│╎   0x00004395      8845a2         mov byte [var_5eh_2], al
│ ────────< 0x00004398      e98bf6ffff     jmp 0x3a28
│ │╎││╎│╎   ;-- case 10:                                               ; from 0x000042f2
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x42f2
│ │╎││╎│╎   0x0000439d      31d2           xor edx, edx
│ │╎││╎│╎   0x0000439f      4531e4         xor r12d, r12d
│ │╎││╎│╎   0x000043a2      be0a000000     mov esi, 0xa
│ │╎││╎│╎   0x000043a7      b86e000000     mov eax, 0x6e               ; 'n'
│ ────────< 0x000043ac      e977f5ffff     jmp 0x3928
│ │╎││╎│╎   ;-- case 35:                                               ; from 0x000042f2
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x42f2
│ │╎││╎│╎   0x000043b1      4531e4         xor r12d, r12d
│ │╎││╎│╎   0x000043b4      be23000000     mov esi, 0x23               ; '#'
│ ────────< 0x000043b9      e98afaffff     jmp 0x3e48
│ │╎││╎│╎   ;-- case 7:                                                ; from 0x000042f2
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x42f2
│ │╎││╎│╎   0x000043be      31d2           xor edx, edx
│ │╎││╎│╎   0x000043c0      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x000043c3      be61000000     mov esi, 0x61               ; 'a'
│ ────────< 0x000043c8      e9a2f5ffff     jmp 0x396f
│ │╎││╎│╎   ;-- case 63:                                               ; from 0x000042f2
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x42f2
│ │╎││╎│╎   0x000043cd      4531e4         xor r12d, r12d
│ │╎││╎│╎   0x000043d0      837da405       cmp dword [var_5ch_3], 5
│ ────────< 0x000043d4      0f84fcf8ffff   je 0x3cd6
│ │╎││╎│╎   0x000043da      660f1f440000   nop word [rax + rax]
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x3cd0, 0x3cdd
│ ────────> 0x000043e0      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x000043e3      be3f000000     mov esi, 0x3f               ; '?'
│ │╎││╎│╎   0x000043e8      4489c0         mov eax, r8d
│ │╎││╎│╎   0x000043eb      0a45a3         or al, byte [var_5dh_3]
│ ────────< 0x000043ee      0f854df5ffff   jne 0x3941
│ ────────< 0x000043f4      e91ff6ffff     jmp 0x3a18
│ │╎││╎│╎   ;-- case 39:                                               ; from 0x000042f2
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x42f2
│ │╎││╎│╎   0x000043f9      448865a0       mov byte [var_78h], r12b
│ │╎││╎│╎   0x000043fd      4589e2         mov r10d, r12d
│ │╎││╎│╎   0x00004400      be27000000     mov esi, 0x27               ; '''
│ │╎││╎│╎   0x00004405      4531e4         xor r12d, r12d
│ │╎││╎│╎   0x00004408      4489c0         mov eax, r8d
│ │╎││╎│╎   0x0000440b      0a45a3         or al, byte [var_5dh_3]
│ ────────< 0x0000440e      0f852df5ffff   jne 0x3941
│ ────────< 0x00004414      e9fff5ffff     jmp 0x3a18
│ │╎││╎│╎   ;-- case 13:                                               ; from 0x000042f2
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x42f2
│ │╎││╎│╎   0x00004419      31d2           xor edx, edx
│ │╎││╎│╎   0x0000441b      4531e4         xor r12d, r12d
│ │╎││╎│╎   0x0000441e      be0d000000     mov esi, 0xd
│ │╎││╎│╎   0x00004423      b872000000     mov eax, 0x72               ; 'r'
│ ────────< 0x00004428      e9fbf4ffff     jmp 0x3928
│ │╎││╎│╎   ;-- case 12:                                               ; from 0x000042f2
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x42f2
│ │╎││╎│╎   0x0000442d      31d2           xor edx, edx
│ │╎││╎│╎   0x0000442f      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x00004432      be66000000     mov esi, 0x66               ; 'f'
│ ────────< 0x00004437      e933f5ffff     jmp 0x396f
│ │╎││╎│╎   ;-- case 9:                                                ; from 0x000042f2
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x42f2
│ │╎││╎│╎   0x0000443c      31d2           xor edx, edx
│ │╎││╎│╎   0x0000443e      4531e4         xor r12d, r12d
│ │╎││╎│╎   0x00004441      be09000000     mov esi, 9
│ │╎││╎│╎   0x00004446      b874000000     mov eax, 0x74               ; 't'
│ ────────< 0x0000444b      e9d8f4ffff     jmp 0x3928
│ │╎││╎│╎   ;-- case 8:                                                ; from 0x000042f2
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x42f2
│ │╎││╎│╎   0x00004450      31d2           xor edx, edx
│ │╎││╎│╎   0x00004452      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x00004455      be62000000     mov esi, 0x62               ; 'b'
│ ────────< 0x0000445a      e910f5ffff     jmp 0x396f
│ │╎││╎│╎   ;-- case 11:                                               ; from 0x000042f2
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x42f2
│ │╎││╎│╎   0x0000445f      31d2           xor edx, edx
│ │╎││╎│╎   0x00004461      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x00004464      be76000000     mov esi, 0x76               ; 'v'
│ ────────< 0x00004469      e901f5ffff     jmp 0x396f
│ │╎││╎│╎   ;-- case 32:                                               ; from 0x000042f2
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x42f2
│ │╎││╎│╎   0x0000446e      4589e2         mov r10d, r12d
│ │╎││╎│╎   0x00004471      be20000000     mov esi, 0x20               ; "@"
│ │╎││╎│╎   0x00004476      4531e4         xor r12d, r12d
│ │╎││╎│╎   0x00004479      4489c0         mov eax, r8d
│ │╎││╎│╎   0x0000447c      0a45a3         or al, byte [var_5dh_3]
│ ────────< 0x0000447f      0f85bcf4ffff   jne 0x3941
│ ────────< 0x00004485      e98ef5ffff     jmp 0x3a18
..
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x38e2
│ ────────> 0x00004490      4080fe7a       cmp sil, 0x7a
│ ────────< 0x00004494      7f62           jg 0x44f8
│ │╎││╎│╎   0x00004496      4080fe40       cmp sil, 0x40               ; elf_phdr
│ ────────< 0x0000449a      0f84d0f5ffff   je case.0x419a.1
│ │╎││╎│╎   0x000044a0      8d4ebf         lea ecx, [rsi - 0x41]
│ │╎││╎│╎   0x000044a3      b801000000     mov eax, 1
│ │╎││╎│╎   0x000044a8      48baffffff53.  movabs rdx, 0x3ffffff53ffffff
│ │╎││╎│╎   0x000044b2      48d3e0         shl rax, cl
│ │╎││╎│╎   0x000044b5      4885d0         test rax, rdx
│ ────────< 0x000044b8      0f8577f4ffff   jne case.0x390d.37
│ │╎││╎│╎   0x000044be      a9000000a4     test eax, 0xa4000000
│ ────────< 0x000044c3      0f856ff7ffff   jne case.0x390d.33
│ │╎││╎│╎   0x000044c9      837da402       cmp dword [var_5ch_3], 2
│ ────────< 0x000044cd      0f859a000000   jne 0x456d
│ │╎││╎│╎   0x000044d3      807da300       cmp byte [var_5dh_3], 0
│ ────────< 0x000044d7      0f8579f7ffff   jne 0x3c56
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4587
│ ────────> 0x000044dd      0fb645a2       movzx eax, byte [var_5eh_2]
│ │╎││╎│╎   0x000044e1      4883c301       add rbx, 1
│ │╎││╎│╎   0x000044e5      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x000044e8      be5c000000     mov esi, 0x5c               ; '\\'
│ ────────< 0x000044ed      e940f5ffff     jmp 0x3a32
..
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4494
│ ────────> 0x000044f8      4080fe7d       cmp sil, 0x7d
│ ────────< 0x000044fc      7410           je 0x450e
│ ────────< 0x000044fe      0f8f8c000000   jg 0x4590
│ │╎││╎│╎   0x00004504      4080fe7b       cmp sil, 0x7b
│ ────────< 0x00004508      0f857f060000   jne 0x4b8d
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x44fc, 0x47f7, 0x4c3e, 0x4c4a, 0x4c5d
│ ────────> 0x0000450e      4983feff       cmp r14, 0xffffffffffffffff
│ ────────< 0x00004512      0f84b0020000   je 0x47c8
│ │╎││╎│╎   0x00004518      4983fe01       cmp r14, 1
│ ────────< 0x0000451c      0f8510f4ffff   jne case.0x419a.33
│ ────────< 0x00004522      e921f9ffff     jmp 0x3e48
..
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x42c7
│ ────────> 0x00004530      4080fe7a       cmp sil, 0x7a
│ ────────< 0x00004534      0f8fa6020000   jg 0x47e0
│ │╎││╎│╎   0x0000453a      4080fe40       cmp sil, 0x40               ; elf_phdr
│ ────────< 0x0000453e      0f8424f5ffff   je case.0x42f2.1
│ │╎││╎│╎   0x00004544      8d4ebf         lea ecx, [rsi - 0x41]
│ │╎││╎│╎   0x00004547      b801000000     mov eax, 1
│ │╎││╎│╎   0x0000454c      48baffffff53.  movabs rdx, 0x3ffffff53ffffff
│ │╎││╎│╎   0x00004556      48d3e0         shl rax, cl
│ │╎││╎│╎   0x00004559      4885d0         test rax, rdx
│ ────────< 0x0000455c      0f858e060000   jne 0x4bf0
│ │╎││╎│╎   0x00004562      a9000000a4     test eax, 0xa4000000
│ ────────< 0x00004567      0f85a3fdffff   jne case.0x42f2.33
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x44cd
│ ────────> 0x0000456d      440fb665a1     movzx r12d, byte [var_5fh_2]
│ │╎││╎│╎   0x00004572      442265a3       and r12b, byte [var_5dh_3]
│ ────────< 0x00004576      0f84f1020000   je 0x486d
│ │╎││╎│╎   0x0000457c      48837d8800     cmp qword [n], 0
│ ────────< 0x00004581      0f84dff6ffff   je 0x3c66
│ ────────< 0x00004587      e951ffffff     jmp 0x44dd
..
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x44fe
│ ────────> 0x00004590      4080fe7e       cmp sil, 0x7e
│ ────────< 0x00004594      0f84aef8ffff   je 0x3e48
│ │╎││╎│╎   0x0000459a      be7f000000     mov esi, 0x7f               ; '\x7f'
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4cc9
│ ────────> 0x0000459f      4883bd30ffff.  cmp qword [var_d0h_3], 1
│ ────────< 0x000045a7      0f84d1f4ffff   je 0x3a7e
│ │╎││╎│╎   0x000045ad      0f1f00         nop dword [rax]
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x3a78
│ ────────> 0x000045b0      488d45c0       lea rax, [var_58h_2]
│ │╎││╎│╎   0x000045b4      48c745c00000.  mov qword [var_58h_2], 0
│ │╎││╎│╎   0x000045bc      48898578ffff.  mov qword [ps], rax
│ │╎││╎│╎   0x000045c3      4983feff       cmp r14, 0xffffffffffffffff
│ ────────< 0x000045c7      7554           jne 0x461d
│ │╎││╎│╎   0x000045c9      488b7d90       mov rdi, qword [s]          ; const char *s
│ │╎││╎│╎   0x000045cd      4c899d50ffff.  mov qword [var_c8h], r11
│ │╎││╎│╎   0x000045d4      4c898d58ffff.  mov qword [s1], r9
│ │╎││╎│╎   0x000045db      4088b560ffff.  mov byte [var_b8h], sil
│ │╎││╎│╎   0x000045e2      44889568ffff.  mov byte [var_b0h], r10b
│ │╎││╎│╎   0x000045e9      44888570ffff.  mov byte [var_90h_2], r8b
│ │╎││╎│╎   0x000045f0      e83bddffff     call sym.imp.strlen         ; size_t strlen(const char *s)
│ │╎││╎│╎   0x000045f5      4c8b9d50ffff.  mov r11, qword [var_c8h]
│ │╎││╎│╎   0x000045fc      4c8b8d58ffff.  mov r9, qword [s1]
│ │╎││╎│╎   0x00004603      0fb6b560ffff.  movzx esi, byte [var_b8h]
│ │╎││╎│╎   0x0000460a      440fb69568ff.  movzx r10d, byte [var_b0h]
│ │╎││╎│╎   0x00004612      4989c6         mov r14, rax
│ │╎││╎│╎   0x00004615      440fb68570ff.  movzx r8d, byte [var_90h_2]
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x45c7
│ ────────> 0x0000461d      44889570ffff.  mov byte [var_90h_2], r10b
│ │╎││╎│╎   0x00004624      31c0           xor eax, eax
│ │╎││╎│╎   0x00004626      44888542ffff.  mov byte [var_beh], r8b
│ │╎││╎│╎   0x0000462d      48899d60ffff.  mov qword [var_b8h], rbx
│ │╎││╎│╎   0x00004634      44889543ffff.  mov byte [var_bdh], r10b
│ │╎││╎│╎   0x0000463b      4088b541ffff.  mov byte [var_bfh], sil
│ │╎││╎│╎   0x00004642      4488a540ffff.  mov byte [var_c0h_2], r12b
│ │╎││╎│╎   0x00004649      4c898d50ffff.  mov qword [var_c8h], r9
│ │╎││╎│╎   0x00004650      4c899d28ffff.  mov qword [var_d8h], r11
│ │╎││╎│╎   0x00004657      4c89ad20ffff.  mov qword [var_e0h], r13
│ │╎││╎│╎   0x0000465e      4c89bd18ffff.  mov qword [var_e8h], r15
│ │╎││╎│╎   0x00004665      4c89b558ffff.  mov qword [s1], r14
│ │╎││╎│╎   0x0000466c      4989c6         mov r14, rax
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x48e7
│ ────────> 0x0000466f      488b8560ffff.  mov rax, qword [var_b8h]
│ │╎││╎│╎   0x00004676      4a8d1c30       lea rbx, [rax + r14]
│ │╎││╎│╎   0x0000467a      488b4590       mov rax, qword [s]
│ │╎││╎│╎   0x0000467e      4c8d3c18       lea r15, [rax + rbx]
│ │╎││╎│╎   0x00004682      4d89fc         mov r12, r15
│ │╎││╎│╎   0x00004685      4d85ff         test r15, r15
│ ────────< 0x00004688      0f84c2020000   je 0x4950
│ │╎││╎│╎   0x0000468e      488b9558ffff.  mov rdx, qword [s1]
│ │╎││╎│╎   0x00004695      4c8d6dbc       lea r13, [wc]
│ │╎││╎│╎   0x00004699      4829da         sub rdx, rbx
│ │╎││╎│╎   0x0000469c      0f958568ffff.  setne byte [var_b0h]
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x496c
│ ────────> 0x000046a3      488b8d78ffff.  mov rcx, qword [ps]
│ │╎││╎│╎   0x000046aa      4c89e6         mov rsi, r12
│ │╎││╎│╎   0x000046ad      4c89ef         mov rdi, r13
│ │╎││╎│╎   0x000046b0      e8cbdcffff     call sym.imp.mbrtoc32
│ │╎││╎│╎   0x000046b5      4889c1         mov rcx, rax
│ │╎││╎│╎   0x000046b8      4883f8fd       cmp rax, 0xfffffffffffffffd
│ ────────< 0x000046bc      0f86c6010000   jbe 0x4888
│ │╎││╎│╎   0x000046c2      80bd68ffffff.  cmp byte [var_b0h], 0
│ ────────< 0x000046c9      0f84b9010000   je 0x4888
│ │╎││╎│╎   0x000046cf      48898568ffff.  mov qword [var_b0h], rax
│ │╎││╎│╎   0x000046d6      e835efffff     call fcn.00003610
│ │╎││╎│╎   0x000046db      84c0           test al, al
│ ────────< 0x000046dd      0f84e1040000   je 0x4bc4
│ │╎││╎│╎   0x000046e3      488b8d68ffff.  mov rcx, qword [var_b0h]
│ │╎││╎│╎   0x000046ea      4889da         mov rdx, rbx
│ │╎││╎│╎   0x000046ed      4c89f0         mov rax, r14
│ │╎││╎│╎   0x000046f0      440fb68542ff.  movzx r8d, byte [var_beh]
│ │╎││╎│╎   0x000046f8      488b9d60ffff.  mov rbx, qword [var_b8h]
│ │╎││╎│╎   0x000046ff      0fb6b541ffff.  movzx esi, byte [var_bfh]
│ │╎││╎│╎   0x00004706      4c8bb558ffff.  mov r14, qword [s1]
│ │╎││╎│╎   0x0000470d      440fb6a540ff.  movzx r12d, byte [var_c0h_2]
│ │╎││╎│╎   0x00004715      4c8b8d50ffff.  mov r9, qword [var_c8h]
│ │╎││╎│╎   0x0000471c      4c8b9d28ffff.  mov r11, qword [var_d8h]
│ │╎││╎│╎   0x00004723      4c8bad20ffff.  mov r13, qword [var_e0h]
│ │╎││╎│╎   0x0000472a      4c8bbd18ffff.  mov r15, qword [var_e8h]
│ │╎││╎│╎   0x00004731      4883f9ff       cmp rcx, 0xffffffffffffffff
│ ────────< 0x00004735      741c           je 0x4753
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4e82
│ ────────> 0x00004737      4c39f2         cmp rdx, r14
│ ────────< 0x0000473a      7317           jae 0x4753
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4751
│ ────────> 0x0000473c      488b4d90       mov rcx, qword [s]
│ │╎││╎│╎   0x00004740      803c1100       cmp byte [rcx + rdx], 0
│ ────────< 0x00004744      740d           je 0x4753
│ │╎││╎│╎   0x00004746      4883c001       add rax, 1
│ │╎││╎│╎   0x0000474a      488d1403       lea rdx, [rbx + rax]
│ │╎││╎│╎   0x0000474e      4c39f2         cmp rdx, r14
│ ────────< 0x00004751      72e9           jb 0x473c
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x4735, 0x473a, 0x4744, 0x4d86
│ ────────> 0x00004753      0fb655a1       movzx edx, byte [var_5fh_2]
│ │╎││╎│╎   0x00004757      4531d2         xor r10d, r10d
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4942
│ ────────> 0x0000475a      4883f801       cmp rax, 1
│ ────────< 0x0000475e      0f8784f3ffff   ja 0x3ae8
│ ────────< 0x00004764      e970f3ffff     jmp 0x3ad9
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x38ac
│ ────────> 0x00004769      837da402       cmp dword [wc], 2
│ │╎││╎│╎   0x0000476d      0f94c2         sete dl
│ │╎││╎│╎   0x00004770      48837da800     cmp qword [var_58h_2], 0
│ │╎││╎│╎   0x00004775      0f94c0         sete al
│ │╎││╎│╎   0x00004778      20d0           and al, dl
│ ────────< 0x0000477a      0f8470020000   je 0x49f0
│ │╎││╎│╎   0x00004780      807da300       cmp byte [var_5dh_3], 0
│ ────────< 0x00004784      0f85c5f4ffff   jne 0x3c4f
│ │╎││╎│╎   0x0000478a      807da000       cmp byte [var_78h], 0
│ ────────< 0x0000478e      0f84f3060000   je 0x4e87
│ │╎││╎│╎   0x00004794      807d9800       cmp byte [var_80h_2], 0
│ ────────< 0x00004798      0f858a060000   jne 0x4e28
│ │╎││╎│╎   0x0000479e      4883bd38ffff.  cmp qword [var_c8h_2], 0
│ │╎││╎│╎   0x000047a6      0f95c0         setne al
│ │╎││╎│╎   0x000047a9      4d85db         test r11, r11
│ │╎││╎│╎   0x000047ac      0f94c2         sete dl
│ │╎││╎│╎   0x000047af      20d0           and al, dl
│ ────────< 0x000047b1      0f8402070000   je 0x4eb9
│ │╎││╎│╎   0x000047b7      4c8b9d38ffff.  mov r11, qword [var_c8h_2]
│ ────────< 0x000047be      e939f7ffff     jmp 0x3efc
..
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4512
│ ────────> 0x000047c8      488b4590       mov rax, qword [s]
│ │╎││╎│╎   0x000047cc      80780100       cmp byte [rax + 1], 0
│ ────────< 0x000047d0      0f855cf1ffff   jne case.0x419a.33
│ ────────< 0x000047d6      e96df6ffff     jmp 0x3e48
..
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4534
│ ────────> 0x000047e0      4080fe7d       cmp sil, 0x7d
│ ────────< 0x000047e4      0f8470040000   je 0x4c5a
│ ────────< 0x000047ea      0f8f1d040000   jg 0x4c0d
│ │╎││╎│╎   0x000047f0      4531e4         xor r12d, r12d
│ │╎││╎│╎   0x000047f3      4080fe7b       cmp sil, 0x7b
│ ────────< 0x000047f7      0f8411fdffff   je 0x450e
│ │╎││╎│╎   0x000047fd      be7c000000     mov esi, 0x7c               ; '|'
│ ────────< 0x00004802      e92bf1ffff     jmp case.0x419a.33
..
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x3cc6
│ │╎│└────> 0x00004810      807da300       cmp byte [var_5dh_3], 0
│ ────────< 0x00004814      0f853cf4ffff   jne 0x3c56
│ │╎│ ╎│╎   0x0000481a      4531d2         xor r10d, r10d
│ │╎│ ╎│╎   0x0000481d      31c0           xor eax, eax
│ │╎│ ╎│╎   0x0000481f      be3f000000     mov esi, 0x3f               ; '?'
│ ────────< 0x00004824      e9fff1ffff     jmp 0x3a28
..
│ │╎│ ╎│╎   ; CODE XREF from fcn.00003610 @ 0x416f
│ ────────> 0x00004830      4080fe7a       cmp sil, 0x7a
│ │╎│┌────< 0x00004834      0f8f00040000   jg 0x4c3a
│ │╎││╎│╎   0x0000483a      4080fe40       cmp sil, 0x40               ; elf_phdr
│ ────────< 0x0000483e      0f842cf2ffff   je case.0x419a.1
│ │╎││╎│╎   0x00004844      8d4ebf         lea ecx, [rsi - 0x41]
│ │╎││╎│╎   0x00004847      b801000000     mov eax, 1
│ │╎││╎│╎   0x0000484c      48baffffff53.  movabs rdx, 0x3ffffff53ffffff
│ │╎││╎│╎   0x00004856      48d3e0         shl rax, cl
│ │╎││╎│╎   0x00004859      4885d0         test rax, rdx
│ ────────< 0x0000485c      0f854d040000   jne 0x4caf
│ │╎││╎│╎   0x00004862      a9000000a4     test eax, 0xa4000000
│ ────────< 0x00004867      0f85c5f0ffff   jne case.0x419a.33
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4576
│ ────────> 0x0000486d      807da100       cmp byte [var_5fh_2], 0
│ ────────< 0x00004871      0f84bbf0ffff   je case.0x419a.33
│ │╎││╎│╎   0x00004877      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x0000487a      be5c000000     mov esi, 0x5c               ; '\\'
│ ────────< 0x0000487f      e93cf1ffff     jmp 0x39c0
..
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x46bc, 0x46c9
│ ────────> 0x00004888      4885c9         test rcx, rcx
│ ────────< 0x0000488b      7460           je 0x48ed
│ │╎││╎│╎   0x0000488d      4883f9ff       cmp rcx, 0xffffffffffffffff
│ ────────< 0x00004891      0f84ab040000   je 0x4d42
│ │╎││╎│╎   0x00004897      4883f9fe       cmp rcx, 0xfffffffffffffffe
│ ────────< 0x0000489b      0f849a050000   je 0x4e3b
│ │╎││╎│╎   0x000048a1      4883f9fd       cmp rcx, 0xfffffffffffffffd
│ ────────< 0x000048a5      7413           je 0x48ba
│ │╎││╎│╎   0x000048a7      837da402       cmp dword [var_5ch_3], 2
│ ────────< 0x000048ab      750a           jne 0x48b7
│ │╎││╎│╎   0x000048ad      807da300       cmp byte [var_5dh_3], 0
│ ────────< 0x000048b1      0f85c1000000   jne 0x4978
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x48ab, 0x499f, 0x4beb
│ ────────> 0x000048b7      4901ce         add r14, rcx
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x48a5, 0x4c80
│ ────────> 0x000048ba      8b7dbc         mov edi, dword [wc]         ; wint_t wc
│ │╎││╎│╎   0x000048bd      e8dedbffff     call sym.imp.iswprint       ; int iswprint(wint_t wc)
│ │╎││╎│╎   0x000048c2      0fb69d70ffff.  movzx ebx, byte [var_90h_2]
│ │╎││╎│╎   0x000048c9      488bbd78ffff.  mov rdi, qword [ps]         ; const mbstate_t *ps
│ │╎││╎│╎   0x000048d0      85c0           test eax, eax
│ │╎││╎│╎   0x000048d2      b800000000     mov eax, 0
│ │╎││╎│╎   0x000048d7      0f44d8         cmove ebx, eax
│ │╎││╎│╎   0x000048da      889d70ffffff   mov byte [var_90h_2], bl
│ │╎││╎│╎   0x000048e0      e8abdbffff     call sym.imp.mbsinit        ; int mbsinit(const mbstate_t *ps)
│ │╎││╎│╎   0x000048e5      85c0           test eax, eax
│ ────────< 0x000048e7      0f8482fdffff   je 0x466f
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x488b
│ ────────> 0x000048ed      440fb69570ff.  movzx r10d, byte [var_90h_2]
│ │╎││╎│╎   0x000048f5      4c89f0         mov rax, r14
│ │╎││╎│╎   0x000048f8      440fb68542ff.  movzx r8d, byte [var_beh]
│ │╎││╎│╎   0x00004900      488b9d60ffff.  mov rbx, qword [var_b8h]
│ │╎││╎│╎   0x00004907      0fb6b541ffff.  movzx esi, byte [var_bfh]
│ │╎││╎│╎   0x0000490e      4489d2         mov edx, r10d
│ │╎││╎│╎   0x00004911      4c8bb558ffff.  mov r14, qword [s1]
│ │╎││╎│╎   0x00004918      440fb6a540ff.  movzx r12d, byte [var_c0h_2]
│ │╎││╎│╎   0x00004920      83f201         xor edx, 1
│ │╎││╎│╎   0x00004923      4c8b8d50ffff.  mov r9, qword [var_c8h]
│ │╎││╎│╎   0x0000492a      4c8b9d28ffff.  mov r11, qword [var_d8h]
│ │╎││╎│╎   0x00004931      4c8bad20ffff.  mov r13, qword [var_e0h]
│ │╎││╎│╎   0x00004938      4c8bbd18ffff.  mov r15, qword [var_e8h]
│ │╎││╎│╎   0x0000493f      2255a1         and dl, byte [var_5fh_2]
│ ────────< 0x00004942      e913feffff     jmp 0x475a
..
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4688
│ ────────> 0x00004950      0fb68543ffff.  movzx eax, byte [var_bdh]
│ │╎││╎│╎   0x00004957      4531ed         xor r13d, r13d
│ │╎││╎│╎   0x0000495a      ba01000000     mov edx, 1
│ │╎││╎│╎   0x0000495f      4c8d25bd1c00.  lea r12, [0x00006623]
│ │╎││╎│╎   0x00004966      888568ffffff   mov byte [var_b0h], al
│ ────────< 0x0000496c      e932fdffff     jmp 0x46a3
..
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x48b1
│ ────────> 0x00004978      4883f901       cmp rcx, 1
│ ────────< 0x0000497c      0f84fa020000   je 0x4c7c
│ │╎││╎│╎   0x00004982      488b4590       mov rax, qword [s]
│ │╎││╎│╎   0x00004986      4d8d040f       lea r8, [r15 + rcx]
│ │╎││╎│╎   0x0000498a      488d541801     lea rdx, [rax + rbx + 1]
│ ────────< 0x0000498f      eb14           jmp 0x49a5
..
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x49ad, 0x49bd
│ ────────> 0x00004998      4883c201       add rdx, 1
│ │╎││╎│╎   0x0000499c      4939d0         cmp r8, rdx
│ ────────< 0x0000499f      0f8412ffffff   je 0x48b7
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x498f
│ ────────> 0x000049a5      0fb602         movzx eax, byte [rdx]
│ │╎││╎│╎   0x000049a8      83e85b         sub eax, 0x5b
│ │╎││╎│╎   0x000049ab      3c21           cmp al, 0x21
│ ────────< 0x000049ad      77e9           ja 0x4998
│ │╎││╎│╎   0x000049af      48bb2b000000.  movabs rbx, 0x20000002b     ; '+' ; 8589934635
│ │╎││╎│╎   0x000049b9      480fa3c3       bt rbx, rax
│ ────────< 0x000049bd      73d9           jae 0x4998
│ │╎││╎│╎   0x000049bf      c745a4020000.  mov dword [var_5ch_3], 2
│ │╎││╎│╎   0x000049c6      4c8bb558ffff.  mov r14, qword [s1]
│ │╎││╎│╎   0x000049cd      4c8b8d50ffff.  mov r9, qword [var_c8h]
│ │╎││╎│╎   0x000049d4      4c8b9d28ffff.  mov r11, qword [var_d8h]
│ │╎││╎│╎   0x000049db      4c8bad20ffff.  mov r13, qword [var_e0h]
│ │╎││╎│╎   0x000049e2      4c8bbd18ffff.  mov r15, qword [var_e8h]
│ ────────< 0x000049e9      e968f2ffff     jmp 0x3c56
..
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x477a
│ ────────> 0x000049f0      0fb645a3       movzx eax, byte [var_5dh_2]
│ │╎││╎│╎   0x000049f4      83f001         xor eax, 1
│ │╎││╎│╎   0x000049f7      20c2           and dl, al
│ ────────< 0x000049f9      7576           jne 0x4a71
│ │╎││╎│╎   0x000049fb      4c89df         mov rdi, r11
│ │╎││╎│╎   0x000049fe      4c8b5da8       mov r11, qword [var_70h_2]
│ │╎││╎│╎   0x00004a02      4d89ca         mov r10, r9
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x4e90, 0x4ea1, 0x4eb4, 0x4ec6
│ ────────> 0x00004a05      488b9d48ffff.  mov rbx, qword [var_b8h]
│ │╎││╎│╎   0x00004a0c      4885db         test rbx, rbx
│ ────────< 0x00004a0f      742f           je 0x4a40
│ │╎││╎│╎   0x00004a11      84c0           test al, al
│ ────────< 0x00004a13      742b           je 0x4a40
│ │╎││╎│╎   0x00004a15      0fb60b         movzx ecx, byte [rbx]
│ │╎││╎│╎   0x00004a18      4889d8         mov rax, rbx
│ │╎││╎│╎   0x00004a1b      84c9           test cl, cl
│ ────────< 0x00004a1d      7421           je 0x4a40
│ │╎││╎│╎   0x00004a1f      4c89da         mov rdx, r11
│ │╎││╎│╎   0x00004a22      4c29d8         sub rax, r11
│ │╎││╎│╎   0x00004a25      4889fe         mov rsi, rdi
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4a3b
│ ────────> 0x00004a28      4839f2         cmp rdx, rsi
│ ────────< 0x00004a2b      7304           jae 0x4a31
│ │╎││╎│╎   0x00004a2d      41880c12       mov byte [r10 + rdx], cl
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4a2b
│ ────────> 0x00004a31      4883c201       add rdx, 1
│ │╎││╎│╎   0x00004a35      0fb60c10       movzx ecx, byte [rax + rdx]
│ │╎││╎│╎   0x00004a39      84c9           test cl, cl
│ ────────< 0x00004a3b      75eb           jne 0x4a28
│ │╎││╎│╎   0x00004a3d      4989d3         mov r11, rdx
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x4a0f, 0x4a13, 0x4a1d
│ ────────> 0x00004a40      4939fb         cmp r11, rdi
│ ────────< 0x00004a43      0f829b030000   jb 0x4de4
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4de9
│ ────────> 0x00004a49      488b45c8       mov rax, qword [var_38h_2]
│ │╎││╎│╎   0x00004a4d      64482b042528.  sub rax, qword fs:[0x28]
│ ────────< 0x00004a56      0f8585040000   jne 0x4ee1
│ │╎││╎│╎   0x00004a5c      4881c4c80000.  add rsp, 0xc8
│ │╎││╎│╎   0x00004a63      4c89d8         mov rax, r11
│ │╎││╎│╎   0x00004a66      5b             pop rbx
│ │╎││╎│╎   0x00004a67      415c           pop r12
│ │╎││╎│╎   0x00004a69      415d           pop r13
│ │╎││╎│╎   0x00004a6b      415e           pop r14
│ │╎││╎│╎   0x00004a6d      415f           pop r15
│ │╎││╎│╎   0x00004a6f      5d             pop rbp
│ │╎││╎│╎   0x00004a70      c3             ret
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x49f9
│ ────────> 0x00004a71      807da000       cmp byte [var_60h], 0
│ ────────< 0x00004a75      0f841a040000   je 0x4e95
│ │╎││╎│╎   0x00004a7b      807d9800       cmp byte [var_80h_2], 0
│ ────────< 0x00004a7f      0f85a3030000   jne 0x4e28
│ │╎││╎│╎   0x00004a85      4d85db         test r11, r11
│ │╎││╎│╎   0x00004a88      0f94c0         sete al
│ │╎││╎│╎   0x00004a8b      4883bd38ffff.  cmp qword [var_c8h_2], 0
│ │╎││╎│╎   0x00004a93      0f95c2         setne dl
│ │╎││╎│╎   0x00004a96      20d0           and al, dl
│ ────────< 0x00004a98      0f8408040000   je 0x4ea6
│ │╎││╎│╎   0x00004a9e      488b8d38ffff.  mov rcx, qword [var_c8h_2]
│ │╎││╎│╎   0x00004aa5      31d2           xor edx, edx
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4e0d
│ ────────> 0x00004aa7      488d1dd61a00.  lea rbx, [0x00006584]       ; "'"
│ │╎││╎│╎   0x00004aae      807d9800       cmp byte [var_80h_2], 0
│ │╎││╎│╎   0x00004ab2      c745a4020000.  mov dword [var_5ch_3], 2
│ │╎││╎│╎   0x00004ab9      48c745a80000.  mov qword [var_70h_2], 0
│ │╎││╎│╎   0x00004ac1      48899d48ffff.  mov qword [s2], rbx
│ │╎││╎│╎   0x00004ac8      48c745880100.  mov qword [n], 1
│ ────────< 0x00004ad0      0f84f5030000   je 0x4ecb
│ │╎││╎│╎   0x00004ad6      8845a0         mov byte [var_78h], al
│ │╎││╎│╎   0x00004ad9      0fb64598       movzx eax, byte [var_80h_2]
│ │╎││╎│╎   0x00004add      4c8b9d38ffff.  mov r11, qword [var_c8h_2]
│ │╎││╎│╎   0x00004ae4      885598         mov byte [var_80h_2], dl
│ │╎││╎│╎   0x00004ae7      48898d38ffff.  mov qword [var_c8h_2], rcx
│ │╎││╎│╎   0x00004aee      8845a3         mov byte [var_5dh_3], al
│ ────────< 0x00004af1      e992edffff     jmp 0x3888
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x3dc0, 0x3dd0
│ ────────> 0x00004af6      488b45a8       mov rax, qword [var_70h_2]
│ │╎││╎│╎   0x00004afa      4c39d8         cmp rax, r11
│ ────────< 0x00004afd      7305           jae 0x4b04
│ │╎││╎│╎   0x00004aff      41c6040127     mov byte [r9 + rax], 0x27   ; '''
│ │╎││╎│╎                                                              ; [0x27:1]=0
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4afd
│ ────────> 0x00004b04      488b75a8       mov rsi, qword [var_70h_2]
│ │╎││╎│╎   0x00004b08      488d4601       lea rax, [rsi + 1]
│ │╎││╎│╎   0x00004b0c      4c39d8         cmp rax, r11
│ ────────< 0x00004b0f      7306           jae 0x4b17
│ │╎││╎│╎   0x00004b11      41c64431015c   mov byte [r9 + rsi + 1], 0x5c ; '\\'
│ │╎││╎│╎                                                              ; [0x5c:1]=0
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4b0f
│ ────────> 0x00004b17      488b45a8       mov rax, qword [var_70h_2]
│ │╎││╎│╎   0x00004b1b      4883c002       add rax, 2
│ │╎││╎│╎   0x00004b1f      4c39d8         cmp rax, r11
│ ────────< 0x00004b22      730a           jae 0x4b2e
│ │╎││╎│╎   0x00004b24      488b45a8       mov rax, qword [var_70h_2]
│ │╎││╎│╎   0x00004b28      41c644010227   mov byte [r9 + rax + 2], 0x27 ; '''
│ │╎││╎│╎                                                              ; [0x27:1]=0
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4b22
│ ────────> 0x00004b2e      4c89da         mov rdx, r11
│ │╎││╎│╎   0x00004b31      4c8b9d38ffff.  mov r11, qword [var_c8h_2]
│ ────────< 0x00004b38      e999f2ffff     jmp 0x3dd6
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x3e20
│ ────────> 0x00004b3d      4883c301       add rbx, 1
│ ────────< 0x00004b41      e94aedffff     jmp 0x3890
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x3c00
│ ────────> 0x00004b46      448855a2       mov byte [var_5eh_2], r10b
│ │╎││╎│╎   0x00004b4a      4c8bb578ffff.  mov r14, qword [ps]
│ │╎││╎│╎   0x00004b51      4c8945a8       mov qword [var_70h_2], r8
│ │╎││╎│╎   0x00004b55      440fb69560ff.  movzx r10d, byte [var_b8h]
│ │╎││╎│╎   0x00004b5d      4c8bad70ffff.  mov r13, qword [var_90h_2]
│ │╎││╎│╎   0x00004b64      4c8bbd68ffff.  mov r15, qword [var_b0h]
│ ────────< 0x00004b6b      e9c2eeffff     jmp 0x3a32
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x3b32
│ ────────> 0x00004b70      8845a1         mov byte [var_5fh_2], al
│ │╎││╎│╎   0x00004b73      4c8bb578ffff.  mov r14, qword [ps]
│ │╎││╎│╎   0x00004b7a      4c8bad70ffff.  mov r13, qword [var_90h_2]
│ │╎││╎│╎   0x00004b81      4c8bbd68ffff.  mov r15, qword [var_b0h]
│ ────────< 0x00004b88      e9c9f0ffff     jmp 0x3c56
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4508
│ ────────> 0x00004b8d      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x00004b90      be7c000000     mov esi, 0x7c               ; '|'
│ ────────< 0x00004b95      e9a1f0ffff     jmp 0x3c3b
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x3bbc
│ ────────> 0x00004b9a      448855a2       mov byte [var_5eh_2], r10b
│ │╎││╎│╎   0x00004b9e      4c8bb578ffff.  mov r14, qword [ps]
│ │╎││╎│╎   0x00004ba5      4c8945a8       mov qword [var_70h_2], r8
│ │╎││╎│╎   0x00004ba9      440fb69560ff.  movzx r10d, byte [var_b8h]
│ │╎││╎│╎   0x00004bb1      4c8bad70ffff.  mov r13, qword [var_90h_2]
│ │╎││╎│╎   0x00004bb8      4c8bbd68ffff.  mov r15, qword [var_b0h]
│ ────────< 0x00004bbf      e913eeffff     jmp 0x39d7
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x46dd
│ ────────> 0x00004bc4      4d85ed         test r13, r13
│ ────────< 0x00004bc7      0f84af000000   je 0x4c7c
│ │╎││╎│╎   0x00004bcd      410fb60424     movzx eax, byte [r12]
│ │╎││╎│╎   0x00004bd2      837da402       cmp dword [var_5ch_3], 2
│ │╎││╎│╎   0x00004bd6      41894500       mov dword [r13], eax
│ ────────< 0x00004bda      750a           jne 0x4be6
│ │╎││╎│╎   0x00004bdc      807da300       cmp byte [var_5dh_3], 0
│ ────────< 0x00004be0      0f8596000000   jne 0x4c7c
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4bda
│ ────────> 0x00004be6      b901000000     mov ecx, 1
│ ────────< 0x00004beb      e9c7fcffff     jmp 0x48b7
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x455c
│ ────────> 0x00004bf0      31c0           xor eax, eax
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4cb2
│ ────────> 0x00004bf2      4589e2         mov r10d, r12d
│ │╎││╎│╎   0x00004bf5      4189c4         mov r12d, eax
│ ────────< 0x00004bf8      e944edffff     jmp 0x3941
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4382
│ ────────> 0x00004bfd      8845a2         mov byte [var_5eh_2], al
│ │╎││╎│╎   0x00004c00      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x00004c03      be30000000     mov esi, 0x30               ; '0'
│ ────────< 0x00004c08      e91beeffff     jmp 0x3a28
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x47ea
│ ────────> 0x00004c0d      31c0           xor eax, eax
│ │╎││╎│╎   0x00004c0f      4080fe7e       cmp sil, 0x7e
│ ────────< 0x00004c13      0f85a8010000   jne 0x4dc1
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4cbe
│ ────────> 0x00004c19      4885db         test rbx, rbx
│ ────────< 0x00004c1c      754c           jne 0x4c6a
│ │╎││╎│╎   0x00004c1e      4589e2         mov r10d, r12d
│ │╎││╎│╎   0x00004c21      be7e000000     mov esi, 0x7e               ; '~'
│ │╎││╎│╎   0x00004c26      4189c4         mov r12d, eax
│ │╎││╎│╎   0x00004c29      4489c0         mov eax, r8d
│ │╎││╎│╎   0x00004c2c      0a45a3         or al, byte [var_5dh_3]
│ ────────< 0x00004c2f      0f850cedffff   jne 0x3941
│ ────────< 0x00004c35      e9deedffff     jmp 0x3a18
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4834
│ │╎│└────> 0x00004c3a      4080fe7d       cmp sil, 0x7d
│ ────────< 0x00004c3e      0f84caf8ffff   je 0x450e
│ │╎│┌────< 0x00004c44      7f71           jg 0x4cb7
│ │╎││╎│╎   0x00004c46      4080fe7b       cmp sil, 0x7b
│ ────────< 0x00004c4a      0f84bef8ffff   je 0x450e
│ │╎││╎│╎   0x00004c50      be7c000000     mov esi, 0x7c               ; '|'
│ ────────< 0x00004c55      e9d8ecffff     jmp case.0x419a.33
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x47e4
│ ────────> 0x00004c5a      4531e4         xor r12d, r12d
│ ────────< 0x00004c5d      e9acf8ffff     jmp 0x450e
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x3c08
│ ────────> 0x00004c62      4531e4         xor r12d, r12d
│ ────────< 0x00004c65      e95aefffff     jmp 0x3bc4
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4c1c
│ ────────> 0x00004c6a      4189c4         mov r12d, eax
│ │╎││╎│╎   0x00004c6d      4531d2         xor r10d, r10d
│ │╎││╎│╎   0x00004c70      31c0           xor eax, eax
│ │╎││╎│╎   0x00004c72      be7e000000     mov esi, 0x7e               ; '~'
│ ────────< 0x00004c77      e9c7ecffff     jmp 0x3943
│ │╎││╎│╎   ; CODE XREFS from fcn.00003610 @ 0x497c, 0x4bc7, 0x4be0
│ ────────> 0x00004c7c      4983c601       add r14, 1
│ ────────< 0x00004c80      e935fcffff     jmp 0x48ba
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4216
│ ────────> 0x00004c85      4c39d9         cmp rcx, r11
│ ────────< 0x00004c88      7305           jae 0x4c8f
│ │╎││╎│╎   0x00004c8a      41c6040930     mov byte [r9 + rcx], 0x30   ; '0'
│ │╎││╎│╎                                                              ; [0x30:1]=0
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4c88
│ ────────> 0x00004c8f      488b75a8       mov rsi, qword [var_70h_2]
│ │╎││╎│╎   0x00004c93      488d5602       lea rdx, [rsi + 2]
│ │╎││╎│╎   0x00004c97      4c39da         cmp rdx, r11
│ ────────< 0x00004c9a      7306           jae 0x4ca2
│ │╎││╎│╎   0x00004c9c      41c644310230   mov byte [r9 + rsi + 2], 0x30 ; '0'
│ │╎││╎│╎                                                              ; [0x30:1]=0
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4c9a
│ ────────> 0x00004ca2      488b4da8       mov rcx, qword [var_70h_2]
│ │╎││╎│╎   0x00004ca6      4883c103       add rcx, 3
│ ────────< 0x00004caa      e96df5ffff     jmp 0x421c
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x485c
│ ────────> 0x00004caf      4489e0         mov eax, r12d
│ ────────< 0x00004cb2      e93bffffff     jmp 0x4bf2
│ │╎││╎│╎   ; CODE XREF from fcn.00003610 @ 0x4c44
│ │╎│└────> 0x00004cb7      4489e0         mov eax, r12d
│ │╎│ ╎│╎   0x00004cba      4080fe7e       cmp sil, 0x7e
│ ────────< 0x00004cbe      0f8455ffffff   je 0x4c19
│ │╎│ ╎│╎   0x00004cc4      be7f000000     mov esi, 0x7f               ; '\x7f'
│ ────────< 0x00004cc9      e9d1f8ffff     jmp 0x459f
│ │╎│ ╎│╎   ; CODE XREF from fcn.00003610 @ 0x3834
│ │╎│ ╎└──> 0x00004cce      410fb64500     movzx eax, byte [r13]
│ │╎│ ╎ ╎   0x00004cd3      84c0           test al, al
│ ────────< 0x00004cd5      0f845febffff   je 0x383a
│ │╎│ ╎ ╎   0x00004cdb      4531e4         xor r12d, r12d
│ │╎│ ╎ ╎   0x00004cde      6690           nop
│ │╎│ ╎ ╎   ; CODE XREF from fcn.00003610 @ 0x4cf5
│ │╎│ ╎┌──> 0x00004ce0      4d39dc         cmp r12, r11
│ │╎│┌────< 0x00004ce3      7304           jae 0x4ce9
│ │╎││╎╎╎   0x00004ce5      43880421       mov byte [r9 + r12], al
│ │╎││╎╎╎   ; CODE XREF from fcn.00003610 @ 0x4ce3
│ │╎│└────> 0x00004ce9      4983c401       add r12, 1
│ │╎│ ╎╎╎   0x00004ced      430fb6442500   movzx eax, byte [r13 + r12]
│ │╎│ ╎╎╎   0x00004cf3      84c0           test al, al
│ │╎│ ╎└──< 0x00004cf5      75e9           jne 0x4ce0
│ │╎│ ╎ ╎   0x00004cf7      4c8965a8       mov qword [var_70h_2], r12
│ ────────< 0x00004cfb      e93aebffff     jmp 0x383a
│ │╎│ ╎ ╎   ; CODE XREF from fcn.00003610 @ 0x3f77
│ ────────> 0x00004d00      488d057b1800.  lea rax, [0x00006582]       ; u"\"'\u07a1e\u80e2\x98\u4247\u3831\u33300\u656d\u6f6d\u7972\u6520\u6878\u7561\u7473\u6465\u2500s\u4f50\u4953X`\u7277\u7469\u2065\u7265\u6f72r\u4e47\u2055\u6f63\u6572\u7475\u6c69s\u6365\u6f68\u2500\u2073\u2528\u2973\u2520\u0a73\u2800\u2943\u5700\u6972\u7474\u6e65\u6220\u2079\u7325\u0a2e\u5700\u6972\u7474\u6e65\u6220\u2079\u7325\u6120"
│ │╎│ ╎ ╎   0x00004d07      c6459801       mov byte [var_80h_2], 1
│ │╎│ ╎ ╎   0x00004d0b      c645a000       mov byte [var_78h], 0
│ │╎│ ╎ ╎   0x00004d0f      c645a200       mov byte [var_5eh_2], 0
│ │╎│ ╎ ╎   0x00004d13      48c78538ffff.  mov qword [var_c8h_2], 0
│ │╎│ ╎ ╎   0x00004d1e      c645a301       mov byte [var_5dh_3], 1
│ │╎│ ╎ ╎   0x00004d22      c645a101       mov byte [var_5fh_2], 1
│ │╎│ ╎ ╎   0x00004d26      48c745880100.  mov qword [n], 1
│ │╎│ ╎ ╎   0x00004d2e      48898548ffff.  mov qword [s2], rax
│ │╎│ ╎ ╎   0x00004d35      48c745a80000.  mov qword [var_70h_2], 0
│ ────────< 0x00004d3d      e946ebffff     jmp 0x3888
│ │╎│ ╎ ╎   ; CODE XREF from fcn.00003610 @ 0x4891
│ ────────> 0x00004d42      4c89f0         mov rax, r14
│ │╎│ ╎ ╎   0x00004d45      440fb68542ff.  movzx r8d, byte [var_beh]
│ │╎│ ╎ ╎   0x00004d4d      488b9d60ffff.  mov rbx, qword [var_b8h]
│ │╎│ ╎ ╎   0x00004d54      0fb6b541ffff.  movzx esi, byte [var_bfh]
│ │╎│ ╎ ╎   0x00004d5b      4c8bb558ffff.  mov r14, qword [s1]
│ │╎│ ╎ ╎   0x00004d62      440fb6a540ff.  movzx r12d, byte [var_c0h_2]
│ │╎│ ╎ ╎   0x00004d6a      4c8b8d50ffff.  mov r9, qword [var_c8h]
│ │╎│ ╎ ╎   0x00004d71      4c8b9d28ffff.  mov r11, qword [var_d8h]
│ │╎│ ╎ ╎   0x00004d78      4c8bad20ffff.  mov r13, qword [var_e0h]
│ │╎│ ╎ ╎   0x00004d7f      4c8bbd18ffff.  mov r15, qword [var_e8h]
│ ────────< 0x00004d86      e9c8f9ffff     jmp 0x4753
│ │╎│ ╎ ╎   ; CODE XREF from fcn.00003610 @ 0x3824
│ └───────> 0x00004d8b      8b75a4         mov esi, dword [var_5ch_3]  ; int64_t arg2
│  ╎│ ╎ ╎   0x00004d8e      4889c7         mov rdi, rax                ; int64_t arg1
│  ╎│ ╎ ╎   0x00004d91      e8bae5ffff     call fcn.00003350
│  ╎│ ╎ ╎   0x00004d96      4c8b5d98       mov r11, qword [var_80h_2]
│  ╎│ ╎ ╎   0x00004d9a      4c8b4da8       mov r9, qword [var_70h_2]
│  ╎│ ╎ ╎   0x00004d9e      4989c7         mov r15, rax
│ ────────< 0x00004da1      e984eaffff     jmp 0x382a
│  ╎│ ╎ ╎   ; CODE XREF from fcn.00003610 @ 0x37f2
│  ╎└─────> 0x00004da6      8b75a4         mov esi, dword [var_5ch_3]  ; int64_t arg2
│  ╎  ╎ ╎   0x00004da9      4889c7         mov rdi, rax                ; int64_t arg1
│  ╎  ╎ ╎   0x00004dac      e89fe5ffff     call fcn.00003350
│  ╎  ╎ ╎   0x00004db1      4c8b5d98       mov r11, qword [var_80h_2]
│  ╎  ╎ ╎   0x00004db5      4c8b4da8       mov r9, qword [var_70h_2]
│  ╎  ╎ ╎   0x00004db9      4989c5         mov r13, rax
│  └──────< 0x00004dbc      e937eaffff     jmp 0x37f8
│     ╎ ╎   ; CODE XREF from fcn.00003610 @ 0x4c13
│ ────────> 0x00004dc1      4531e4         xor r12d, r12d
│     ╎ ╎   0x00004dc4      be7f000000     mov esi, 0x7f               ; '\x7f'
│ ────────< 0x00004dc9      e9a2ecffff     jmp case.0x419a.1
│     ╎ ╎   ; CODE XREFS from fcn.00003610 @ 0x3d0f, 0x3d2a
│ ────────> 0x00004dce      be3f000000     mov esi, 0x3f               ; '?'
│     ╎ ╎   0x00004dd3      4489c0         mov eax, r8d
│     ╎ ╎   0x00004dd6      0a45a3         or al, byte [var_5dh_3]
│ ────────< 0x00004dd9      0f8562ebffff   jne 0x3941
│ ────────< 0x00004ddf      e934ecffff     jmp 0x3a18
│     ╎ ╎   ; CODE XREF from fcn.00003610 @ 0x4a43
│ ────────> 0x00004de4      43c6041a00     mov byte [r10 + r11], 0
│ ────────< 0x00004de9      e95bfcffff     jmp 0x4a49
│     ╎ ╎   ;-- case 2:                                                ; from 0x000037b3
│     ╎ ╎   ; CODE XREF from fcn.00003610 @ 0x37b3
│     ╎ ╎   0x00004dee      0fb645a3       movzx eax, byte [var_5dh_3]
│     ╎ ╎   0x00004df2      c645a200       mov byte [var_5eh_2], 0
│     ╎ ╎   0x00004df6      ba01000000     mov edx, 1
│     ╎ ╎   0x00004dfb      31c9           xor ecx, ecx
│     ╎ ╎   0x00004dfd      4c899d38ffff.  mov qword [var_c8h_2], r11
│     ╎ ╎   0x00004e04      884598         mov byte [var_80h_2], al
│     ╎ ╎   0x00004e07      31c0           xor eax, eax
│     ╎ ╎   0x00004e09      c645a100       mov byte [var_5fh_2], 0
│ ────────< 0x00004e0d      e995fcffff     jmp 0x4aa7
│     ╎ ╎   ; CODE XREF from fcn.00003610 @ 0x4324
│ ────────> 0x00004e12      8b5da4         mov ebx, dword [var_5ch_3]
│     ╎ ╎   0x00004e15      b804000000     mov eax, 4
│     ╎ ╎   0x00004e1a      83fb02         cmp ebx, 2
│     ╎ ╎   0x00004e1d      0f45c3         cmovne eax, ebx
│     ╎ ╎   0x00004e20      8945a4         mov dword [var_5ch_3], eax
│ ────────< 0x00004e23      e93eeeffff     jmp 0x3c66
│     ╎ ╎   ; CODE XREFS from fcn.00003610 @ 0x4798, 0x4a7f
│ ────────> 0x00004e28      c745a4050000.  mov dword [var_5ch_3], 5
│     ╎ ╎   0x00004e2f      4c8b9d38ffff.  mov r11, qword [var_c8h_2]
│     └───< 0x00004e36      e935e9ffff     jmp 0x3770
│       ╎   ; CODE XREF from fcn.00003610 @ 0x489b
│ ────────> 0x00004e3b      4889da         mov rdx, rbx
│       ╎   0x00004e3e      4c89f0         mov rax, r14
│       ╎   0x00004e41      440fb68542ff.  movzx r8d, byte [var_beh]
│       ╎   0x00004e49      488b9d60ffff.  mov rbx, qword [var_b8h]
│       ╎   0x00004e50      0fb6b541ffff.  movzx esi, byte [var_bfh]
│       ╎   0x00004e57      4c8bb558ffff.  mov r14, qword [s1]
│       ╎   0x00004e5e      440fb6a540ff.  movzx r12d, byte [var_c0h_2]
│       ╎   0x00004e66      4c8b8d50ffff.  mov r9, qword [var_c8h]
│       ╎   0x00004e6d      4c8b9d28ffff.  mov r11, qword [var_d8h]
│       ╎   0x00004e74      4c8bad20ffff.  mov r13, qword [var_e0h]
│       ╎   0x00004e7b      4c8bbd18ffff.  mov r15, qword [var_e8h]
│ ────────< 0x00004e82      e9b0f8ffff     jmp 0x4737
│       ╎   ; CODE XREF from fcn.00003610 @ 0x478e
│ ────────> 0x00004e87      4c89df         mov rdi, r11
│       ╎   0x00004e8a      4d89ca         mov r10, r9
│       ╎   0x00004e8d      4531db         xor r11d, r11d
│ ────────< 0x00004e90      e970fbffff     jmp 0x4a05
│       ╎   ; CODE XREF from fcn.00003610 @ 0x4a75
│ ────────> 0x00004e95      4c89df         mov rdi, r11
│       ╎   0x00004e98      4d89ca         mov r10, r9
│       ╎   0x00004e9b      4c8b5da8       mov r11, qword [var_58h_2]
│       ╎   0x00004e9f      89d0           mov eax, edx
│ ────────< 0x00004ea1      e95ffbffff     jmp 0x4a05
│       ╎   ; CODE XREF from fcn.00003610 @ 0x4a98
│ ────────> 0x00004ea6      4c89df         mov rdi, r11
│       ╎   0x00004ea9      0fb645a0       movzx eax, byte [var_78h]
│       ╎   0x00004ead      4c8b5da8       mov r11, qword [var_70h_2]
│       ╎   0x00004eb1      4d89ca         mov r10, r9
│ ────────< 0x00004eb4      e94cfbffff     jmp 0x4a05
│       ╎   ; CODE XREF from fcn.00003610 @ 0x47b1
│ ────────> 0x00004eb9      4c89df         mov rdi, r11
│       ╎   0x00004ebc      0fb645a0       movzx eax, byte [var_78h]
│       ╎   0x00004ec0      4d89ca         mov r10, r9
│       ╎   0x00004ec3      4531db         xor r11d, r11d
│ ────────< 0x00004ec6      e93afbffff     jmp 0x4a05
│       ╎   ; CODE XREF from fcn.00003610 @ 0x4ad0
│ ────────> 0x00004ecb      4c8b9d38ffff.  mov r11, qword [var_c8h_2]
│       ╎   0x00004ed2      885598         mov byte [var_80h_2], dl
│       ╎   0x00004ed5      48898d38ffff.  mov qword [var_c8h_2], rcx
│ ────────< 0x00004edc      e91bf0ffff     jmp 0x3efc
│       ╎   ; CODE XREF from fcn.00003610 @ 0x4a56
│ ────────> 0x00004ee1      e85ad4ffff     call sym.imp.__stack_chk_fail
│       ╎   0x00004ee6      662e0f1f8400.  nop word cs:[rax + rax]
│       ╎   ; DATA XREF from fcn.00003610 @ 0x25e2
│       ╎   0x00004ef0      f30f1efa       endbr64
│       ╎   0x00004ef4      55             push rbp
│       ╎   0x00004ef5      4889e5         mov rbp, rsp
│       ╎   0x00004ef8      53             push rbx
│       ╎   0x00004ef9      4883ec08       sub rsp, 8
│       ╎   0x00004efd      488b05c44000.  mov rax, qword [reloc.stdout] ; [0x8fc8:8]=0
│       ╎   0x00004f04      488b38         mov rdi, qword [rax]        ; int64_t arg1
│       ╎   0x00004f07      e894e6ffff     call fcn.000035a0
│       ╎   0x00004f0c      85c0           test eax, eax
│      ┌──< 0x00004f0e      7440           je 0x4f50
│      │╎   0x00004f10      ba05000000     mov edx, 5
│      │╎   0x00004f15      488d35961600.  lea rsi, str.write_error    ; 0x65b2 ; "write error"
│      │╎   0x00004f1c      31ff           xor edi, edi
│      │╎   0x00004f1e      e8edd3ffff     call sym.imp.dcgettext
│      │╎   0x00004f23      4889c3         mov rbx, rax
│      │╎   0x00004f26      e875d3ffff     call sym.imp.__errno_location
│      │╎   0x00004f2b      31ff           xor edi, edi                ; int status
│      │╎   0x00004f2d      4889d9         mov rcx, rbx
│      │╎   0x00004f30      488d15701600.  lea rdx, [0x000065a7]       ; "%s" ; char *format
│      │╎   0x00004f37      8b30           mov esi, dword [rax]        ; int errname
│      │╎   0x00004f39      31c0           xor eax, eax
│      │╎   0x00004f3b      e8f0d4ffff     call sym.imp.error          ; void error(int status, int errname, char *format)
│      │╎   0x00004f40      8b3dca400000   mov edi, dword [0x00009010] ; [0x9010:4]=1
│      │╎   0x00004f46      e875d3ffff     call sym.imp._exit
│      │╎   0x00004f4b      0f1f440000     nop dword [rax + rax]
│      │╎   ; CODE XREF from fcn.00003610 @ 0x4f0e
│      └──> 0x00004f50      488b05a14000.  mov rax, qword [reloc.stderr] ; [0x8ff8:8]=0
│       ╎   0x00004f57      488b38         mov rdi, qword [rax]        ; int64_t arg1
│       ╎   0x00004f5a      e841e6ffff     call fcn.000035a0
│       ╎   0x00004f5f      85c0           test eax, eax
│      ┌──< 0x00004f61      7506           jne 0x4f69
│      │╎   0x00004f63      488b5df8       mov rbx, qword [var_8h]
│      │╎   0x00004f67      c9             leave
│      │╎   0x00004f68      c3             ret
│      │╎   ; CODE XREF from fcn.00003610 @ 0x4f61
│      └──> 0x00004f69      8b3da1400000   mov edi, dword [0x00009010] ; [0x9010:4]=1
│       ╎   0x00004f6f      e84cd3ffff     call sym.imp._exit
│       ╎   0x00004f74      66662e0f1f84.  nop word cs:[rax + rax]
│       ╎   0x00004f7f      90             nop
        ╎   ; CALL XREF from fcn.00003610 @ 0x2bc1
..
│      │╎   ; CODE XREF from fcn.00004f80 @ 0x4faa
│      │╎   ; CODE XREF from fcn.00004f80 @ 0x505b
│    │╎│╎   ; CODE XREF from fcn.00004f80 @ 0x5073
│  │╎│╎│╎   ; CODE XREF from fcn.00004f80 @ 0x502b
│  │ │  ╎   ; CODE XREF from fcn.00004f80 @ 0x5048
│  │   │╎   ; CODE XREF from fcn.00004f80 @ 0x5078
│  │   │╎   ; CODE XREF from fcn.00004f80 @ 0x5084
│  │   │╎   ;-- switch
│  │   │╎   ; CODE XREF from fcn.00004f80 @ 0x5052
│      │╎   ; CODE XREF from fcn.00004f80 @ 0x55eb
│     ╎│╎   ; CODE XREF from fcn.00004f80 @ 0x532e
│    ╎╎│╎   ;-- default:                                               ; from 0x5143
│    ╎╎│╎   ; XREFS: CODE 0x0000512f  CODE 0x00005143  CODE 0x000053be  
│    ╎╎│╎   ; XREFS: CODE 0x0000547d  CODE 0x00005506  CODE 0x00005544  
│    ╎╎│╎   ; XREFS: CODE 0x00005578  
│ ╎╎╎╎╎│╎   ;-- case 8:                                                ; from 0x00005143
│ ╎╎╎╎╎│╎   ; CODE XREF from fcn.00004f80 @ 0x5143
│ ╎╎╎ ╎│╎   ;-- case 7:                                                ; from 0x00005143
│ ╎╎╎ ╎│╎   ; CODE XREF from fcn.00004f80 @ 0x5143
│ ╎╎╎ ╎│╎   ; CODE XREF from fcn.00004f80 @ 0x541a
│ ╎╎╎╎╎│╎   ;-- case 6:                                                ; from 0x00005143
│ ╎╎╎╎╎│╎   ; CODE XREF from fcn.00004f80 @ 0x5143
│ ╎╎╎ ╎│╎   ;-- case 5:                                                ; from 0x00005143
│ ╎╎╎ ╎│╎   ; CODE XREF from fcn.00004f80 @ 0x5143
│ ╎╎╎ ╎│╎   ; CODE XREF from fcn.00004f80 @ 0x54c1
│ ╎╎╎╎╎│╎   ;-- case 4:                                                ; from 0x00005143
│ ╎╎╎╎╎│╎   ; CODE XREF from fcn.00004f80 @ 0x5143
│ ╎╎╎ ╎│╎   ;-- case 3:                                                ; from 0x00005143
│ ╎╎╎ ╎│╎   ; CODE XREF from fcn.00004f80 @ 0x5143
│  ╎╎ ╎│╎   ;-- case 2:                                                ; from 0x00005143
│  ╎╎ ╎│╎   ; CODE XREF from fcn.00004f80 @ 0x5143
│   ╎ ╎│╎   ;-- case 1:                                                ; from 0x00005143
│   ╎ ╎│╎   ; CODE XREF from fcn.00004f80 @ 0x5143
│     ╎│╎   ;-- case 9:                                                ; from 0x00005143
│     ╎│╎   ; CODE XREF from fcn.00004f80 @ 0x5143
│      │╎   ; CODE XREF from fcn.00004f80 @ 0x52ae
        ╎   ; CALL XREF from fcn.00003610 @ 0x25e9
            ;-- section..fini:
            ; DATA XREF from fcn.00003610 @ 0x379d
