text = "X-DSPAM-Confidence:    0.8475";
num = text.find(':')
val = text[num+1:]
val = float(val)
print(val)
