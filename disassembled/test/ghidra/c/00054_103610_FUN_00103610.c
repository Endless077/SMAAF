
/* WARNING: Type propagation algorithm not settling */

undefined8 FUN_00103610(void)

{
  int iVar1;
  char *__s;
  size_t sVar2;
  ulong uVar3;
  undefined4 extraout_var;
  undefined8 uVar4;
  ulong uVar5;
  long lVar6;
  char *pcVar7;
  long in_FS_OFFSET;
  byte bVar8;
  char local_128;
  char cStack_127;
  long local_20;
  
  bVar8 = 0;
  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  __s = setlocale(0,(char *)0x0);
  if ((__s != (char *)0x0) && (sVar2 = strlen(__s), sVar2 < 0x101)) {
    uVar3 = sVar2 + 1;
    pcVar7 = &local_128;
    if ((uint)uVar3 < 8) {
      if ((uVar3 & 4) == 0) goto LAB_00103689;
LAB_001036f0:
      *(undefined4 *)pcVar7 = *(undefined4 *)__s;
      lVar6 = 4;
    }
    else {
      for (uVar5 = uVar3 >> 3 & 0x1fffffff; uVar5 != 0; uVar5 = uVar5 - 1) {
        *(undefined8 *)pcVar7 = *(undefined8 *)__s;
        __s = __s + (ulong)bVar8 * -0x10 + 8;
        pcVar7 = pcVar7 + (ulong)bVar8 * -0x10 + 8;
      }
      if ((uVar3 & 4) != 0) goto LAB_001036f0;
LAB_00103689:
      lVar6 = 0;
    }
    if ((uVar3 & 2) != 0) {
      *(undefined2 *)(pcVar7 + lVar6) = *(undefined2 *)(__s + lVar6);
      lVar6 = lVar6 + 2;
    }
    if ((uVar3 & 1) != 0) {
      pcVar7[lVar6] = __s[lVar6];
    }
    if ((local_128 != 'C') || (cStack_127 != '\0')) {
      iVar1 = strcmp(&local_128,"POSIX");
      uVar4 = CONCAT71((int7)(CONCAT44(extraout_var,iVar1) >> 8),iVar1 != 0);
      goto LAB_0010364e;
    }
  }
  uVar4 = 0;
LAB_0010364e:
  if (local_20 == *(long *)(in_FS_OFFSET + 0x28)) {
    return uVar4;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

