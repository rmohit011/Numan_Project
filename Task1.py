import cProfile
import pandas as pd
import unittest
import sys
import pstats
import io

def task1():
    df_detail=pd.concat(pd.read_excel('data.xlsx', sheet_name=["Detail_67_1_1","Detail_67_1_1_1","Detail_67_1_1_2",'Detail_67_1_1_3','Detail_67_1_1_4','Detail_67_1_1_5','Detail_67_1_1_6']), ignore_index=True)
    df_detail_vol=pd.concat(pd.read_excel('data.xlsx',sheet_name=["DetailVol_67_1_1","DetailVol_67_1_1_1","DetailVol_67_1_1_2",'DetailVol_67_1_1_3','DetailVol_67_1_1_4','DetailVol_67_1_1_5','DetailVol_67_1_1_6']),ignore_index=True)
    df_detail_temp_0=pd.concat(pd.read_excel('data.xlsx',sheet_name=["DetailTemp_67_1_1","DetailTemp_67_1_1_1","DetailTemp_67_1_1_2"]),ignore_index=True)
    df_detail_temp_1=pd.concat(pd.read_excel('data_1.xlsx',sheet_name=["DetailTemp_67_1_1_3","DetailTemp_67_1_1_4",f"DetailTemp_67_1_1_5",'DetailTemp_67_1_1_6']),ignore_index=True)
    df_detail_temp=pd.concat([df_detail_temp_0,df_detail_temp_1],axis=0,ignore_index=True)
    a=df_detail.to_csv("detail.csv",index=False)
    b=df_detail_vol.to_csv("detailVol.csv",index=False)
    c=df_detail_temp.to_csv("detailTemp.csv",index=False)
    return [df_detail.shape,df_detail_vol.shape,df_detail_temp.shape]

def cprofile():
    pr = cProfile.Profile()
    pr.enable()
    my_result = task1()
    print(my_result)
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    ps.print_stats()
    with open('cprofile_task1.txt', 'w+') as f:
        f.write(s.getvalue())


class unit_test(unittest.TestCase):
    def test_task1(self):
        try:
            a = task1()
            self.assertEqual(a, [(416681, 11), (416681, 6), (416681, 6)])
        except Exception as e:
            print(e)


def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == '__main__':
    s=cprofile()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    with open('unit_test_task1.out', 'w') as f:
        main(f)
