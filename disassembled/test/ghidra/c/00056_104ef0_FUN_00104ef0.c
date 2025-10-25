
void FUN_00104ef0(void)

{
  int iVar1;
  undefined8 uVar2;
  int *piVar3;
  
  iVar1 = FUN_001035a0(*(undefined8 *)PTR_stdout_00108fc8);
  if (iVar1 != 0) {
    uVar2 = dcgettext(0,"write error",5);
    piVar3 = __errno_location();
    error(0,*piVar3,&DAT_001065a7,uVar2);
                    /* WARNING: Subroutine does not return */
    _exit(DAT_00109010);
  }
  iVar1 = FUN_001035a0(*(undefined8 *)PTR_stderr_00108ff8);
  if (iVar1 == 0) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  _exit(DAT_00109010);
}

