
undefined * FUN_00103350(char *param_1,int param_2)

{
  byte bVar1;
  int iVar2;
  byte *pbVar3;
  undefined *puVar4;
  
  pbVar3 = (byte *)nl_langinfo(0xe);
  if ((pbVar3 != (byte *)0x0) && (*pbVar3 != 0)) {
    bVar1 = *pbVar3 & 0xdf;
    if (bVar1 == 0x55) {
      if ((((pbVar3[1] & 0xdf) == 0x54) && ((pbVar3[2] & 0xdf) == 0x46)) &&
         ((pbVar3[3] == 0x2d && ((pbVar3[4] == 0x38 && (pbVar3[5] == 0)))))) {
        puVar4 = &DAT_0010657b;
        if (*param_1 == '`') {
          puVar4 = &DAT_0010658a;
        }
        return puVar4;
      }
    }
    else if (((((bVar1 == 0x47) && ((pbVar3[1] & 0xdf) == 0x42)) && (pbVar3[2] == 0x31)) &&
             ((pbVar3[3] == 0x38 && (pbVar3[4] == 0x30)))) &&
            ((pbVar3[5] == 0x33 && (pbVar3[6] == 0x30)))) {
      iVar2 = FUN_00103190(pbVar3,"GB18030",0,0);
      if (iVar2 != 0) {
        puVar4 = &DAT_0010657f;
        if (*param_1 == '`') {
          puVar4 = &DAT_00106586;
        }
        return puVar4;
      }
    }
  }
  puVar4 = &DAT_00106584;
  if (param_2 == 9) {
    puVar4 = &DAT_00106582;
  }
  return puVar4;
}

