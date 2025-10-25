┌ 38: entry0 (int64_t arg3);
│           ; arg int64_t arg3 @ rdx
│           0x00003010      f30f1efa       endbr64
│           0x00003014      31ed           xor ebp, ebp
│           0x00003016      4989d1         mov r9, rdx                 ; arg3
│           0x00003019      5e             pop rsi
│           0x0000301a      4889e2         mov rdx, rsp
│           0x0000301d      4883e4f0       and rsp, 0xfffffffffffffff0
│           0x00003021      50             push rax
│           0x00003022      54             push rsp
│           0x00003023      4531c0         xor r8d, r8d
│           0x00003026      31c9           xor ecx, ecx
│           0x00003028      488d3da1f4ff.  lea rdi, [0x000024d0]
│           0x0000302f      ff15835f0000   call qword [reloc.__libc_start_main] ; [0x8fb8:8]=0
└           0x00003035      f4             hlt
