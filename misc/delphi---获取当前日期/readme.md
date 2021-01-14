```delphi
program Project1;

{$APPTYPE CONSOLE}

uses
  SysUtils;

var
  Present: TDateTime;
  Year, Month, Day, Hour, Min, Sec, MSec: Word;
begin
  Present:= Now;
  SysUtils.DecodeDate(Present, Year, Month, Day);
  writeln('Today is: ' + IntToStr(Year) + '/' + IntToStr(Month) + '/' + IntToStr(Day));
  readln;
end.
```

参考链接：http://docwiki.embarcadero.com/CodeExamples/Sydney/en/DecodeDate_(Delphi)