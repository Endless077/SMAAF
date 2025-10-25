            ; CALL XREFS from fcn.00003610 @ 0x28f2, 0x2914
┌ 71: fcn.00003100 (int64_t arg1);
│           ; arg int64_t arg1 @ rdi
│           0x00003100      8d47bf         lea eax, [rdi - 0x41]       ; arg1
│           0x00003103      3c25           cmp al, 0x25
│       ┌─< 0x00003105      7719           ja case.0x3118.71
│       │   0x00003107      488d15122f00.  lea rdx, [0x00006020]       ; "`\xd1\xff\xffP\xd1\xff\xff\x10\xd1\xff\xff \xd1\xff\xff0\xd1\xff\xff@\xd1\xff\xff"
│       │   0x0000310e      0fb6c0         movzx eax, al
│       │   0x00003111      48630482       movsxd rax, dword [rdx + rax*4]
│       │   0x00003115      4801d0         add rax, rdx
│       │   ;-- switch
│       │   0x00003118      3effe0         jmp rax                     ; switch table (38 cases) at 0x6020
..
│       │   ;-- default:                                               ; from 0x3118
│       │   ; CODE XREFS from fcn.00003100 @ 0x3105, 0x3118
│       └─> 0x00003120      400fb6ff       movzx edi, dil
│           0x00003124      8d47d0         lea eax, [rdi - 0x30]
│           0x00003127      c3             ret
..
│           ;-- case 67:                                               ; from 0x00003118
│           ; CODE XREF from fcn.00003100 @ 0x3118
│           0x00003130      b80c000000     mov eax, 0xc
│           0x00003135      c3             ret
..
│           ;-- case 68:                                               ; from 0x00003118
│           ; CODE XREF from fcn.00003100 @ 0x3118
│           0x00003140      b80d000000     mov eax, 0xd
│           0x00003145      c3             ret
..
│           ;-- case 69:                                               ; from 0x00003118
│           ; CODE XREF from fcn.00003100 @ 0x3118
│           0x00003150      b80e000000     mov eax, 0xe
│           0x00003155      c3             ret
..
│           ;-- case 70:                                               ; from 0x00003118
│           ; CODE XREF from fcn.00003100 @ 0x3118
│           0x00003160      b80f000000     mov eax, 0xf
│           0x00003165      c3             ret
..
│           ;-- case 66:                                               ; from 0x00003118
│           ; CODE XREF from fcn.00003100 @ 0x3118
│           0x00003170      b80b000000     mov eax, 0xb
│           ; DATA XREF from fcn.00003350 @ 0x3412
│           0x00003175      c3             ret
..
│           ;-- case 65:                                               ; from 0x00003118
│           ; CODE XREF from fcn.00003100 @ 0x3118
│           0x00003180      b80a000000     mov eax, 0xa
└           0x00003185      c3             ret
