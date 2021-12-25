TextArray = InputText.ToCharArray()
string NewString = ""

int RepeatCounter = 0
for (int i = 0; i < TextArray.Length; i++)
    for (int j = 0; j < TextArray.Length; j++)
        if (TextArray[i] == TextArray[j] && i != j)
                            RepeatCounter++
                    if (RepeatCounter == 0)
                    
                        NewString += TextArray[i]
                    RepeatCounter = 0
                NewString += '.'
                return NewString
