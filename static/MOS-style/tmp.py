f = open("sentences.txt", "r", encoding='utf-8')
o = open("transcript.txt", "w", encoding='utf-8')
lines = f.readlines()
i = 0
for line in lines:
    out = 'audio_' + str(i) + '.wav|' + line
    i += 1
    o.writelines(out)
    print(out)
