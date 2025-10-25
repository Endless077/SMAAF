int entry0 (int esi, int edx) {
    loc_0x3010:
        endbr6
        ebp = 0
        r9 = rdx      // arg3
        rsi = pop  ()
        rdx = rsp
        rsp &= 0xfffffffffffffff0
        push  (rax)
        push  (rsp)
        r8d = 0
        ecx = 0
        rdi = rip - 0xb5f // 0x24d0
        qword [reloc.__libc_start_main]  () // [0x8fb8:8]=0 // reloc.__libc_start_main(0x24d0, 0x0, 0x178008, 0x0)
        hl
         // (break)
}
