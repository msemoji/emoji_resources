
# coding: utf-8

# In[1]:


import pandas as pd # used for writing out to csv and reviewing data

filepath = 'emoji-test.txt'
output = 'latest_emoji.csv'
header = ['emoji', 'group', 'subgroup', 'name', 'qualified_status', 'edition', 'codepoint_readable', 'utf8_codepoint']
emoji_data_rows = []
emoji_data_rows.append(header)

with open(filepath) as fp:
    line = fp.readline()
    i = 0
    group = ''
    subgroup = ''
    while line:
        line = fp.readline()
        if "# group: " in line:
            group = line[9:].strip('\n')
        if "# subgroup: " in line:
            subgroup = line[12:].strip('\n')
        try:
            if line[0] != '#' and line != '\n':
                splita = line.strip('\n').split('; ')
                codepoint_readable = splita[0].strip()
                splitb = splita[1].split('# ')
                qualified_status = splitb[0].strip()
                splitc = splitb[1].split(' ')
                emoji = splitc[0].strip()
                edition = splitc[1].strip()
                name = ' '.join(splitc[2:])
                utf8_codepoints = emoji.encode('unicode_escape').decode('utf8')

                rownew = [emoji, group, subgroup, name, qualified_status, edition, codepoint_readable, utf8_codepoints]
                emoji_data_rows.append(rownew)

                i += 1
        except:
            i += 1

# Convert data to a csv of emojis            
print('Number of total emojis processed:', len(emoji_data_rows))


emojis_df = pd.DataFrame(emoji_data_rows[1:])
emojis_df.columns = emoji_data_rows[0]
#print(emojis_df.shape)
print('Number of emojis by qualified status')
print(emojis_df['qualified_status'].value_counts())
emojis_df.head()

emojis_df.to_csv('emojis_data_v13_1.csv')


# In[2]:


# create the sorted list of emojis so can copy and paste in to the Unicode_emojis_list.py file
# list_of_emojis == list_of_fully_qualified_emojis
list_of_fully_qualified_emojis = sorted(emojis_df[emojis_df['qualified_status']=='fully-qualified']['emoji'].tolist())

print(len(list_of_fully_qualified_emojis), 'list_of_emojis')
print(list_of_fully_qualified_emojis)
print()




list_of_all_emojis = sorted(emojis_df['emoji'].tolist())


print(len(list_of_all_emojis), 'list_of_all_emojis')
print(list_of_all_emojis)

