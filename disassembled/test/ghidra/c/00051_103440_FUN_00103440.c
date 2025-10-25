
void FUN_00103440(void)

{
  undefined4 uVar1;
  undefined8 uVar2;
  
  uVar1 = DAT_00109010;
  uVar2 = dcgettext(0,"memory exhausted",5);
  error(uVar1,0,&DAT_001065a7,uVar2);
                    /* WARNING: Subroutine does not return */
  abort();
}

