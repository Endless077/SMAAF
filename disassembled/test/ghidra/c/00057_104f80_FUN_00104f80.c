
void FUN_00104f80(undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
                 undefined8 param_5,undefined8 param_6,undefined8 param_7,undefined8 param_8,
                 FILE *param_9,undefined8 param_10,undefined8 param_11,undefined8 param_12,
                 undefined8 param_13,undefined8 param_14)

{
  char in_AL;
  undefined8 uVar1;
  long *plVar2;
  ulong uVar3;
  ulong uVar4;
  long lVar5;
  char *pcVar6;
  long lVar7;
  long in_FS_OFFSET;
  undefined8 local_190;
  undefined8 local_188;
  undefined8 local_180;
  undefined8 local_178;
  long local_170;
  long local_148 [11];
  long local_f0;
  long local_e8 [4];
  long local_c8 [4];
  undefined8 local_a8;
  undefined8 local_98;
  undefined8 local_88;
  undefined8 local_78;
  undefined8 local_68;
  undefined8 local_58;
  undefined8 local_48;
  
  local_c8[0] = param_13;
  local_c8[1] = param_14;
  if (in_AL != '\0') {
    local_c8[2] = param_1;
    local_a8 = param_2;
    local_98 = param_3;
    local_88 = param_4;
    local_78 = param_5;
    local_68 = param_6;
    local_58 = param_7;
    local_48 = param_8;
  }
  local_f0 = *(long *)(in_FS_OFFSET + 0x28);
  plVar2 = (long *)&stack0x00000008;
  lVar5 = 0;
  uVar4 = 0x20;
  do {
    if ((uint)uVar4 < 0x30) {
      uVar3 = (ulong)((uint)uVar4 + 8);
      lVar7 = *(long *)((long)local_e8 + uVar4);
      local_148[lVar5] = lVar7;
      if (lVar7 != 0) goto LAB_0010504a;
LAB_00105075:
      __fprintf_chk(param_9,2,"%s (%s) %s\n",&DAT_001065cc,"GNU coreutils",param_12);
      uVar1 = dcgettext(0,&DAT_001065dd,5);
      lVar7 = 0x7e7;
      __fprintf_chk(param_9,2,"Copyright %s %d Free Software Foundation, Inc.",uVar1);
      fputc_unlocked(10,param_9);
      uVar1 = dcgettext(0,
                        "License GPLv3+: GNU GPL version 3 or later <%s>.\nThis is free software: you are free to change and redistribute it.\nThere is NO WARRANTY, to the extent permitted by law.\n"
                        ,5);
      __fprintf_chk(param_9,2,uVar1,"https://gnu.org/licenses/gpl.html");
      fputc_unlocked(10,param_9);
      switch(lVar5) {
      default:
        goto switchD_00105143_caseD_0;
      case 1:
        uVar1 = dcgettext(0,"Written by %s.\n",5);
        __fprintf_chk(param_9,2,uVar1,local_148[0]);
        goto switchD_00105143_caseD_0;
      case 2:
        uVar1 = dcgettext(0,"Written by %s and %s.\n",5);
        __fprintf_chk(param_9,2,uVar1,local_148[0],local_148[1]);
        goto switchD_00105143_caseD_0;
      case 3:
        uVar1 = dcgettext(0,"Written by %s, %s, and %s.\n",5);
        __fprintf_chk(param_9,2,uVar1,local_148[0],local_148[1],local_148[2]);
        goto switchD_00105143_caseD_0;
      case 4:
        uVar1 = dcgettext(0,"Written by %s, %s, %s,\nand %s.\n",5);
        break;
      case 5:
        uVar1 = dcgettext(0,"Written by %s, %s, %s,\n%s, and %s.\n",5);
        lVar7 = local_148[4];
        break;
      case 6:
        local_148[6] = local_148[0];
        uVar1 = dcgettext(0,"Written by %s, %s, %s,\n%s, %s, and %s.\n",5);
        goto LAB_0010539d;
      case 7:
        uVar1 = dcgettext(0,"Written by %s, %s, %s,\n%s, %s, %s, and %s.\n",5);
LAB_0010539d:
        __fprintf_chk(param_9,2,uVar1,local_148[0],local_148[1],local_148[2],local_148[3],
                      local_148[4],local_148[5],local_148[6]);
        goto switchD_00105143_caseD_0;
      case 8:
        local_188 = local_148[7];
        local_180 = local_148[2];
        local_178 = local_148[1];
        local_170 = local_148[0];
        uVar1 = dcgettext(0,"Written by %s, %s, %s,\n%s, %s, %s, %s,\nand %s.\n",5);
        local_190 = uVar1;
        goto LAB_00105266;
      case 9:
        local_190 = local_148[8];
        local_188 = local_148[7];
        pcVar6 = "Written by %s, %s, %s,\n%s, %s, %s, %s,\n%s, and %s.\n";
        local_180 = local_148[2];
        local_178 = local_148[1];
        local_170 = local_148[0];
        goto LAB_00105253;
      }
      __fprintf_chk(param_9,2,uVar1,local_148[0],local_148[1],local_148[2],local_148[3],lVar7);
      goto switchD_00105143_caseD_0;
    }
    lVar7 = *plVar2;
    local_148[lVar5] = lVar7;
    plVar2 = plVar2 + 1;
    uVar3 = uVar4;
    if (lVar7 == 0) goto LAB_00105075;
LAB_0010504a:
    lVar5 = lVar5 + 1;
    uVar4 = uVar3;
  } while (lVar5 != 10);
  __fprintf_chk(param_9,2,"%s (%s) %s\n",&DAT_001065cc,"GNU coreutils",param_12);
  uVar1 = dcgettext(0,&DAT_001065dd,5);
  __fprintf_chk(param_9,2,"Copyright %s %d Free Software Foundation, Inc.",uVar1,0x7e7);
  fputc_unlocked(10,param_9);
  uVar1 = dcgettext(0,
                    "License GPLv3+: GNU GPL version 3 or later <%s>.\nThis is free software: you are free to change and redistribute it.\nThere is NO WARRANTY, to the extent permitted by law.\n"
                    ,5);
  __fprintf_chk(param_9,2,uVar1,"https://gnu.org/licenses/gpl.html");
  fputc_unlocked(10,param_9);
  pcVar6 = "Written by %s, %s, %s,\n%s, %s, %s, %s,\n%s, %s, and others.\n";
  local_190 = local_148[8];
  local_188 = local_148[7];
  local_180 = local_148[2];
  local_178 = local_148[1];
  local_170 = local_148[0];
LAB_00105253:
  uVar1 = dcgettext(0,pcVar6,5);
LAB_00105266:
  __fprintf_chk(param_9,2,uVar1,local_170,local_178,local_180,local_148[3],local_148[4],local_148[5]
                ,local_148[6],local_188,local_190);
switchD_00105143_caseD_0:
  if (local_f0 == *(long *)(in_FS_OFFSET + 0x28)) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

