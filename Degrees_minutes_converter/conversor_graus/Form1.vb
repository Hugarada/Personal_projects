Public Class Form1
    Dim converter, neversec, neverminute, needsconv, onlynums As Boolean
    Dim num, conver, radder As Double
    Dim tocov, i, j, x, z As Integer
    Dim tostringer, nexter, nexter2, numastring As String

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        If tocov = 0 Then
            tocov = 2
        Else
            conver = 2
        End If
        converting()
    End Sub

    Sub converting()
        If converter = False Then
            numvaluer()
            converter = True
            Label3.Text = "to"
        Else
            converter = False
            Select Case tocov
                Case 1
                    Select Case conver
                        Case 1
                            MsgBox("you must choose 2 different types of convertions")
                        Case 2
                            ''this piece of code extracts the minutes if theres a comma also removing the comma from the last string from degrees
                            tostringer = Convert.ToString(num)
                            For i = 0 To tostringer.Length - 1 Step 1
                                If tostringer.Chars(i) = (",") Then
                                    neverminute = True
                                    i += 1
                                    For j = i To ToString.Length - 1 Step 1
                                        If j = tostringer.Length Then
                                            Exit For
                                        End If
                                        nexter += (tostringer.Chars(j))
                                    Next
                                    i -= 1
                                    x = i
                                    For j = i To tostringer.Length - 1 Step 1
                                        tostringer = tostringer.Remove(x, 1)
                                    Next
                                    Exit For
                                End If
                            Next
                            If neverminute = False Then
                                restartvar()
                                MsgBox("there are no minutes or seconds")
                                Exit Select
                            End If
                            nexter = "0," + nexter
                            conver = Convert.ToDouble(nexter)
                            conver *= 60
                            nexter = Convert.ToString(conver)
                            num += Convert.ToDouble(nexter)
                            tostringer += "º"
                            ''from here this what it does is, if there is another comma, identify the seconds also removing the comma from the last string from the minutes
                            For i = 0 To nexter.Length - 1 Step 1
                                If nexter.Chars(i) = "," Then
                                    neversec = False
                                    i += 1
                                    For j = i To nexter.Length - 1 Step 1
                                        nexter2 += nexter.Chars(j)
                                    Next
                                    i -= 1
                                    x = i
                                    For j = i To nexter.Length - 1 Step 1
                                        nexter = nexter.Remove(x, 1)
                                    Next
                                    Exit For
                                Else
                                    neversec = True
                                End If
                            Next
                            If neversec = True Then
                                tostringer += nexter + "'"
                            Else
                                nexter2 = "0," + nexter2
                                conver = Convert.ToDouble(nexter2)
                                conver *= 60
                                nexter2 = Convert.ToString(conver)
                                num += Convert.ToDouble(nexter2)
                                tostringer += nexter + "'" + nexter2 + "''"
                            End If
                            TextBox2.Text = tostringer
                        Case 3
                            For i = 0 To TextBox1.Text.Length - 1 Step 1
                                ''this piece of code will check if there is a comma and if that is true then it will first convert it to degrees
                                If TextBox1.Text.Chars(i) = "," Then
                                    needsconv = True
                                End If
                                If needsconv = True Then
                                    minutetodegrees()
                                Else
                                    radder = Convert.ToInt32(TextBox1.Text)
                                    radder *= 2
                                    radder /= 360
                                End If
                                TextBox2.Text = Convert.ToString(radder) + "rad"
                                If neverminute = True Then
                                    Exit Select
                                End If
                            Next
                    End Select
                Case 2
                    Select Case conver
                        Case 1
                            minutetodegrees()
                    End Select
            End Select
            restartvar()
        End If
    End Sub

    Sub minutetodegrees()
        '' if there are indeed seconds or minutes, this code will take place
        If onlynums = False Then
            ''This code will take the string of the code and convert it to degrees
            For i = 0 To numastring.Length - 1 Step 1
                If numastring.Chars(i) = "º" Then
                    If numastring.Chars(i + 1) <> "" Then
                        i += 1
                        For j = i To numastring.Length - 1 Step 1
                            If j = numastring.Length Then
                                Exit For
                            End If
                            nexter += (numastring.Chars(j))
                        Next
                        i -= 1
                        x = i
                        For j = i To tostringer.Length - 1 Step 1
                            numastring = numastring.Remove(x, 1)
                        Next
                        For j = 0 To nexter.Length - 1 Step 1
                            If nexter.Chars(j) = "'" Then
                                j += 1
                                For x = j To nexter.Length - 1 Step 1
                                    nexter2 += numastring.Chars(j)
                                Next
                                j -= 1
                                z = j
                                For x = j To nexter.Length - 1 Step 1
                                    nexter.Remove(z, 1)
                                Next
                                Exit For
                            End If
                        Next
                        Exit For
                    End If
                ElseIf i = numastring.Length - 1 Then
                    MsgBox("You need minutes at least minutes to convert this")
                    neverminute = True
                    Exit Sub
                End If
                If nexter2 <> "" Then
                    TextBox2.Text = tostringer + "º" + nexter + "'" + nexter2 + "''"
                Else
                    TextBox2.Text = numastring + "º" + nexter + "'"
                End If
            Next
        End If
    End Sub

    Sub restartvar()
        radder = 0
        num = 0
        tocov = 0
        conver = 0
        i = 0
        j = 0
        x = 0
        tostringer = ""
        nexter = ""
        nexter2 = ""
        converter = False
        neversec = False
        needsconv = False
        Label3.Text = ("Convert from")
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        If tocov = 0 Then
            tocov = 1
        Else
            conver = 1
        End If
        converting()
    End Sub

    Sub numvaluer()
        For i = 0 To TextBox1.Text.Length - 1 Step 1
            If TextBox1.Text.Chars(i) = "º" Then
                onlynums = False
                Exit For
            Else
                onlynums = True
            End If
        Next
        If onlynums = True Then
            num = Convert.ToDouble(TextBox1.Text)
        Else
            numastring = TextBox1.Text
        End If
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Me.Close()
    End Sub

    Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click
        If tocov = 0 Then
            tocov = 3
        Else
            conver = 3
        End If
        converting()
    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Label3.Text = ("Convert from")
    End Sub

    Private Sub TextBox1_TextChanged(sender As Object, e As EventArgs) Handles TextBox1.TextChanged
        If TextBox1.Text <> "" Then
            Button2.Enabled = True
            Button3.Enabled = True
            Button4.Enabled = True
        Else
            Button2.Enabled = False
            Button3.Enabled = False
            Button4.Enabled = False
        End If
    End Sub
End Class
