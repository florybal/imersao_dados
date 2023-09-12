import pandas as pd

in_csv = 'MICRODADOS_ENEM_2022.csv'

number_lines = sum(1 for row in(open(in_csv,'r', encoding="ISO-8859-1")))

rowsize = 500

for i in range(1,number_lines,rowsize):
    df = pd.read_csv(in_csv,
          header=None,
          nrows = rowsize,#number of rows to read at each loop
          skiprows = i)#skip rows that have been read
    
    out_csv = 'input' + str(i) + '.csv'

    df.to_csv(out_csv,
          index=False,
          header=False,
          mode='a',#append data to csv file
          chunksize=rowsize)#size of data to append for each loop