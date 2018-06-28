import os
import shutil
import pandas as pd
from tqdm import tqdm


#os.mkdir('/Users/nataliejin/PycharmProjects/untitled1/balance_sheets')
wk_dir = '/Users/nataliejin/PycharmProjects/untitled1/financials'
bs_dir = '/Users/nataliejin/PycharmProjects/untitled1/balance_sheets'
csv_list = os.listdir(wk_dir)
after_list=[]
#print(csv_list)
for csv_file in csv_list:
    if csv_file.find('资产负债') > 0:
        after_list.append(csv_file)
         # shutil.copy(wk_dir + '/' + csv_file,bs_dir + '/' + csv_file)
        os.path.join(wk_dir, csv_file)


bs_list = os.listdir(bs_dir)

pbar = tqdm(total=len(bs_list))

results = pd.DataFrame(columns=['是否平衡'])

for bs in bs_list:
    pbar.update(1)
    df = pd.read_csv(bs_dir + '/' + bs, index_col=0)
    df = df.T
    df['差'] = abs(df['所有者权益(或股东权益)合计(万元)'] + df['负债合计(万元)'] - df['资产总计(万元)'])
    df['是否平衡'] = df.apply(lambda r: r['差'] < 1, axis=1)
    # print(df['是否平衡'].any())
    code = bs[:6]
    results.loc[code, '是否平衡'] = df['是否平衡'].any()

pbar.close()

results.to_csv('/Users/nataliejin/Desktop/1.csv')







