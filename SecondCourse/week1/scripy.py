text = "X-DSPAM-Confidence:    0.8475";
output = text[text.find('0'):text.find('0')+6]

print(float(output))