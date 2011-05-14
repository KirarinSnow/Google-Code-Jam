REM  Problem: Old Magician
REM  Language: Visual Basic
REM  Author: KirarinSnow
REM  Usage: vbnc -out:prog.exe thisfile.vb && ./prog.exe <input.in >output.out


Module GCJ
  Sub Main()
    Dim i As Integer
    Dim line As String()
    Dim result As String
    For i = 1 To Console.ReadLine()
      line = Console.ReadLine().Split()
      If line(1) Mod 2 = 1 Then
        result = "BLACK"
      Else
        result = "WHITE"
      End If
      Console.WriteLine(String.Format("Case #{0}: {1}", i, result))
    Next
  End Sub
End Module
